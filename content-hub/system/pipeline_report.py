"""Print a factual pipeline snapshot from the consulting lead tracker.

This report is intentionally read-only. It never changes the tracker and it
keeps proposed, won, and received amounts separate.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path


ACTIVE_STAGES = {"New", "Contacted", "Qualified", "Proposal", "Nurture"}
PROSPECT_RESEARCH_STATUS = "research"
DATE_IN_TEXT = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")


def parse_amount(value: str) -> Decimal:
    """Return a tracker amount, treating blank or invalid values as zero."""

    cleaned = (value or "").replace(",", "").strip()
    if not cleaned:
        return Decimal("0")
    try:
        return Decimal(cleaned)
    except InvalidOperation:
        return Decimal("0")


def parse_int(value: str) -> int:
    """Return a non-negative tracker count, treating blank or invalid values as zero."""

    try:
        return max(0, int((value or "").strip()))
    except (TypeError, ValueError):
        return 0


def load_leads(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        return list(csv.DictReader(stream))


def latest_platform_rows(rows: list[dict[str, str]], as_of: date) -> list[dict[str, str]]:
    """Return the newest dated platform row for each platform up to the report date."""

    latest: dict[str, tuple[date, dict[str, str]]] = {}
    for row in rows:
        try:
            recorded = date.fromisoformat((row.get("date") or "").strip())
        except ValueError:
            continue
        if recorded > as_of:
            continue
        platform = (row.get("platform") or "Unspecified").strip()
        if platform not in latest or recorded >= latest[platform][0]:
            latest[platform] = (recorded, row)
    return [row for _, row in sorted(latest.values(), key=lambda item: item[1].get("platform", ""))]


def marketplace_totals(
    opportunities: list[dict[str, str]],
    platform_rows: list[dict[str, str]],
    referrals: list[dict[str, str]],
    as_of: date,
) -> tuple[int, int, int, int, int, int, int]:
    """Return research count, applications, replies, proposals, wins, income, and referrals sent."""

    research_count = sum(
        1 for row in opportunities if (row.get("application_status") or "").strip() == "research-qualified"
    )
    latest_rows = latest_platform_rows(platform_rows, as_of)
    applications = sum(parse_int(row.get("applications", "")) for row in latest_rows)
    replies = sum(parse_int(row.get("replies", "")) for row in latest_rows)
    proposals = sum(parse_int(row.get("proposals", "")) for row in latest_rows)
    wins = sum(parse_int(row.get("work_won", "")) for row in latest_rows)
    income = sum(parse_amount(row.get("received_income_ngn", "")) for row in latest_rows)
    referrals_sent = sum(1 for row in referrals if (row.get("date_sent") or "").strip())
    return research_count, applications, replies, proposals, wins, int(income), referrals_sent


def format_ngn(value: Decimal) -> str:
    return f"₦{value:,.0f}"


def prospect_readiness(prospects: list[dict[str, str]], as_of: date) -> tuple[int, int, int]:
    """Return research prospects, ready prospects, and stale route count."""

    ready = 0
    stale = 0
    research_prospects = [
        prospect
        for prospect in prospects
        if (prospect.get("status") or "").strip().lower() == PROSPECT_RESEARCH_STATUS
    ]
    for prospect in research_prospects:
        if all(
            (prospect.get(field) or "").strip()
            for field in ("public_contact_route", "draft_file", "next_action")
        ):
            ready += 1
        try:
            checked = date.fromisoformat((prospect.get("contact_checked") or "").strip())
        except ValueError:
            stale += 1
        else:
            if checked < as_of:
                stale += 1
    return len(research_prospects), ready, stale


def prospect_follow_ups(
    prospects: list[dict[str, str]], as_of: date
) -> list[tuple[date, dict[str, str]]]:
    """Return dated follow-ups for contacted prospects, oldest first."""

    follow_ups: list[tuple[date, dict[str, str]]] = []
    for prospect in prospects:
        if (prospect.get("status") or "").strip().lower() != "contacted":
            continue
        match = DATE_IN_TEXT.search(prospect.get("next_action") or "")
        if not match:
            continue
        try:
            due = date.fromisoformat(match.group(1))
        except ValueError:
            continue
        follow_ups.append((due, prospect))
    return sorted(follow_ups, key=lambda item: item[0])


def confirmed_income(income_rows: list[dict[str, str]], as_of: date) -> Decimal:
    """Sum only dated receipt rows on or before the report date."""

    total = Decimal("0")
    for row in income_rows:
        try:
            received = date.fromisoformat((row.get("date_received") or "").strip())
        except ValueError:
            continue
        if received <= as_of:
            total += parse_amount(row.get("amount_received_ngn", ""))
    return total


def report(
    leads: list[dict[str, str]],
    as_of: date,
    prospects: list[dict[str, str]] | None = None,
    income_rows: list[dict[str, str]] | None = None,
    opportunities: list[dict[str, str]] | None = None,
    platform_rows: list[dict[str, str]] | None = None,
    referrals: list[dict[str, str]] | None = None,
) -> str:
    stage_counts = Counter((lead.get("stage") or "Unstaged").strip() for lead in leads)
    sources = Counter((lead.get("source") or "Unspecified").strip() for lead in leads)
    offers = Counter((lead.get("offer") or "Unspecified").strip() for lead in leads)
    proposed = sum((parse_amount(lead.get("proposed_value_ngn", "")) for lead in leads), Decimal("0"))
    won = sum((parse_amount(lead.get("won_value_ngn", "")) for lead in leads), Decimal("0"))
    overdue: list[dict[str, str]] = []
    for lead in leads:
        due = (lead.get("next_action_due") or "").strip()
        try:
            due_date = datetime.strptime(due, "%Y-%m-%d").date()
        except ValueError:
            continue
        if due_date < as_of and (lead.get("stage") or "").strip() in ACTIVE_STAGES:
            overdue.append(lead)

    research_count, applications, replies, proposals, wins, marketplace_income, referrals_sent = marketplace_totals(
        opportunities or [], platform_rows or [], referrals or [], as_of
    )

    lines = [
        "# Consulting pipeline snapshot",
        "",
        f"As of: {as_of.isoformat()}",
        "",
        f"- Leads logged: {len(leads)}",
        f"- Active opportunities: {sum(stage_counts[stage] for stage in ACTIVE_STAGES)}",
        f"- Proposed value: {format_ngn(proposed)}",
        f"- Won value: {format_ngn(won)}",
        f"- Confirmed income received: {format_ngn(confirmed_income(income_rows or [], as_of))}",
        f"- Overdue follow-ups: {len(overdue)}",
        "",
        "## Stage counts",
        "",
    ]
    if stage_counts:
        lines.extend(f"- {stage}: {count}" for stage, count in sorted(stage_counts.items()))
    else:
        lines.append("- No leads logged yet; this snapshot reflects the empty tracker.")

    lines.extend(
        [
            "",
            "## Marketplace and referral activity",
            "",
            f"- Research-qualified freelance opportunities: {research_count}",
            f"- Applications recorded: {applications}",
            f"- Replies recorded: {replies}",
            f"- Proposals recorded: {proposals}",
            f"- Marketplace work won: {wins}",
            f"- Marketplace income recorded: {format_ngn(Decimal(marketplace_income))}",
            f"- Warm referral requests sent: {referrals_sent}",
            "- Marketplace research is excluded from leads until a client expresses identifiable interest.",
        ]
    )

    lines.extend(["", "## Top sources", ""])
    lines.extend(f"- {source}: {count}" for source, count in sources.most_common(5))
    if not sources:
        lines.append("- No source data yet.")

    lines.extend(["", "## Offers represented", ""])
    lines.extend(f"- {offer}: {count}" for offer, count in offers.most_common(5))
    if not offers:
        lines.append("- No offer data yet.")

    lines.extend(["", "## Follow-up queue", ""])
    if overdue:
        for lead in overdue:
            lines.append(
                f"- {lead.get('prospect') or 'Unnamed prospect'} — "
                f"{lead.get('next_action') or 'next action missing'} "
                f"(due {lead.get('next_action_due')})"
            )
    else:
        lines.append("- No overdue active follow-ups recorded.")

    if prospects is not None:
        total, ready, stale = prospect_readiness(prospects, as_of)
        contacted = [
            prospect
            for prospect in prospects
            if (prospect.get("status") or "").strip().lower() == "contacted"
        ]
        follow_up_review = [
            prospect
            for prospect in contacted
            if (prospect.get("follow_up_status") or "").strip().lower()
            == "created_for_review"
        ]
        prospect_follow_up_rows = prospect_follow_ups(prospects, as_of)
        ready_rows = [
            prospect
            for prospect in prospects
            if (prospect.get("status") or "").strip().lower() == PROSPECT_RESEARCH_STATUS
            and all(
                (prospect.get(field) or "").strip()
                for field in ("public_contact_route", "draft_file", "next_action")
            )
        ]
        lines.extend(
            [
                "",
                "## Prospect research queue",
                "",
                f"- Research prospects: {total}",
                f"- Contacted prospects: {len(contacted)}",
                f"- Follow-up drafts ready for review: {len(follow_up_review)}",
                f"- Ready for personalization: {ready}",
                f"- Contact routes needing re-check: {stale}",
                "- Research prospects are excluded from lead, opportunity, and income totals; contacted prospects remain outside the lead tracker until a response or identifiable interest is recorded.",
                "",
                "### Prospect follow-up queue",
                "",
            ]
        )
        if prospect_follow_up_rows:
            for due, prospect in prospect_follow_up_rows:
                timing = "overdue" if due < as_of else f"due {due.isoformat()}"
                lines.append(
                    f"- {prospect.get('company') or 'Unnamed company'} — "
                    f"{prospect.get('next_action') or 'follow-up action missing'} "
                    f"({timing})"
                )
        else:
            lines.append("- No dated prospect follow-ups recorded.")

        lines.extend(["", "### Next outreach batch", ""])
        if ready_rows:
            for prospect in ready_rows[:3]:
                lines.append(
                    f"- {prospect.get('company') or 'Unnamed company'} — "
                    f"{prospect.get('fit_offer') or 'offer not assigned'} — "
                    f"{prospect.get('public_contact_route')} — "
                    f"draft: {prospect.get('draft_file')}"
                )
        else:
            lines.append("- No prospects are ready for personalization.")

    return "\n".join(lines) + "\n"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--leads",
        type=Path,
        default=Path(__file__).with_name("leads.csv"),
        help="Path to the lead tracker CSV",
    )
    parser.add_argument(
        "--prospects",
        type=Path,
        default=Path(__file__).with_name("prospect-list.csv"),
        help="Path to the prospect research CSV",
    )
    parser.add_argument(
        "--income",
        type=Path,
        default=Path(__file__).with_name("income-ledger.csv"),
        help="Path to the confirmed income ledger CSV",
    )
    parser.add_argument(
        "--opportunities",
        type=Path,
        default=Path(__file__).with_name("freelance-opportunities.csv"),
        help="Path to the freelance opportunity tracker CSV",
    )
    parser.add_argument(
        "--platform-log",
        type=Path,
        default=Path(__file__).with_name("freelance-platform-test-log.csv"),
        help="Path to the platform measurement log CSV",
    )
    parser.add_argument(
        "--referrals",
        type=Path,
        default=Path(__file__).with_name("warm-referral-outreach.csv"),
        help="Path to the warm referral outreach CSV",
    )
    parser.add_argument(
        "--as-of",
        type=date.fromisoformat,
        default=date.today(),
        help="Snapshot date in YYYY-MM-DD format (defaults to today)",
    )
    args = parser.parse_args()
    print(
        report(
            load_leads(args.leads),
            args.as_of,
            load_leads(args.prospects),
            load_leads(args.income),
            load_leads(args.opportunities),
            load_leads(args.platform_log),
            load_leads(args.referrals),
        ),
        end="",
    )


if __name__ == "__main__":
    main()
