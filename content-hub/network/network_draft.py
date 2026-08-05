"""Generate unsent, human-reviewable professional networking drafts."""

from __future__ import annotations

import argparse
import re


PLACEHOLDER_RE = re.compile(r"\b(TBC|TBD|TODO|INSERT|PLACEHOLDER|NAME|COMPANY|CONTEXT)\b", re.I)


def clean(value: str) -> str:
    return " ".join(value.strip().split())


def require_real(label: str, value: str) -> str:
    value = clean(value)
    if not value or PLACEHOLDER_RE.search(value):
        raise ValueError(f"{label} must contain confirmed, non-placeholder context")
    return value


def draft(kind: str, name: str, company: str, context: str, offer: str) -> str:
    name = require_real("--name", name)
    context = require_real("--context", context)
    offer = require_real("--offer", offer)
    company = clean(company)
    salutation = f"Hello {name}."
    company_phrase = f" at {company}" if company else ""

    if kind == "connection":
        body = (
            f"{salutation} I came across {context}{company_phrase}. "
            f"I support architecture and construction teams with {offer}. "
            "I would be glad to connect and follow your work."
        )
    elif kind == "follow-up":
        body = (
            f"{salutation} I am following up on {context}. "
            f"My relevant support is {offer}. "
            "If the need is active, please share the project stage and the decision you need to make. "
            "If the timing is not right, I can leave this for a later review."
        )
    elif kind == "comment":
        body = (
            f"{context} The delivery implication is worth noting: "
            f"{offer} can make that decision easier to coordinate and review."
        )
    else:
        raise ValueError("--kind must be connection, follow-up, or comment")

    return "\n".join([
        "STATUS: DRAFT — NOT SENT",
        "APPROVAL: Review identity, context, claims, tone, and destination manually.",
        "",
        body,
        "",
        "MANUAL LOG: Record the actual send or publish date and outcome in network-contacts.csv.",
    ])


def main() -> None:
    parser = argparse.ArgumentParser(description="Print an unsent networking draft for manual review.")
    parser.add_argument("--kind", required=True, choices=("connection", "follow-up", "comment"))
    parser.add_argument("--name", required=True, help="Confirmed recipient name")
    parser.add_argument("--company", default="", help="Confirmed company name, if relevant")
    parser.add_argument("--context", required=True, help="Specific public or user-supplied context")
    parser.add_argument("--offer", required=True, help="One verified service lane")
    args = parser.parse_args()
    try:
        print(draft(args.kind, args.name, args.company, args.context, args.offer))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
