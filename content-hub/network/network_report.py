"""Read-only snapshot for the local professional networking workspace."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NETWORK = ROOT / "content-hub" / "network"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def parse_day(value: str) -> date | None:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def build_report(as_of: date) -> str:
    contacts = read_csv(NETWORK / "network-contacts.csv")
    leads = read_csv(ROOT / "content-hub" / "system" / "leads.csv")
    opportunities = read_csv(ROOT / "content-hub" / "system" / "freelance-opportunities.csv")

    active_contacts = [row for row in contacts if row.get("status", "").lower() not in {"closed", "declined", "do not contact"}]
    due = [
        row for row in active_contacts
        if (due_day := parse_day(row.get("next_action_due", ""))) and due_day <= as_of
    ]
    statuses = Counter(row.get("status", "TBC") or "TBC" for row in contacts)
    linked_leads = {row.get("lead_id") for row in contacts if row.get("lead_id")}
    linkedin_leads = [row for row in leads if row.get("source", "").lower() == "linkedin"]

    lines = [
        f"# Professional Network Snapshot — {as_of.isoformat()}",
        "",
        "This is a local, read-only report. No external service was contacted.",
        "",
        "## Network contacts",
        "",
        f"- Total contact records: {len(contacts)}",
        f"- Active contact records: {len(active_contacts)}",
        f"- Overdue or due next actions: {len(due)}",
        f"- LinkedIn-sourced leads already in the commercial tracker: {len(linkedin_leads)}",
        f"- Contacts linked to a lead record: {len(linked_leads)}",
        "",
        "### Status counts",
        "",
    ]
    lines.extend(f"- {status}: {count}" for status, count in sorted(statuses.items()))
    lines.extend(["", "### Action queue", ""])
    if due:
        for row in sorted(due, key=lambda item: item.get("next_action_due", "")):
            lines.append(
                f"- {row.get('next_action_due')}: {row.get('person') or row.get('company') or 'Unnamed'} — "
                f"{row.get('next_action') or 'next action missing'}"
            )
    else:
        lines.append("- No dated network actions are due.")
    lines.extend([
        "",
        "## Existing acquisition context",
        "",
        f"- Commercial lead records: {len(leads)}",
        f"- Freelance opportunity records: {len(opportunities)}",
        "- Research or drafted contacts are not counted as leads until identifiable interest is recorded.",
        "",
        "## Next review",
        "",
        "Run the manual approval workflow before sending or publishing anything.",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a read-only local networking snapshot.")
    parser.add_argument("--as-of", default=date.today().isoformat(), help="Report date in YYYY-MM-DD format")
    args = parser.parse_args()
    report_day = parse_day(args.as_of)
    if report_day is None:
        parser.error("--as-of must use YYYY-MM-DD")
    print(build_report(report_day), end="")


if __name__ == "__main__":
    main()
