# Monthly Income and Pipeline Review

This review separates attention metrics from commercial evidence. Complete it at
month end from `leads.csv` and confirmed payment records. Leave values blank when
the source data is unavailable; do not convert impressions, invoices, or proposals
into received income.

## Definitions

| Metric | Definition |
|---|---|
| Consulting income | Payment actually received for architecture, BIM, or construction consulting during the month |
| New leads | Unique prospects first added to `leads.csv` during the month |
| Qualified leads | New leads that have a defined problem, timing, decision-maker, and budget signal |
| Proposals sent | Defined scopes and fee frameworks sent during the month |
| Won opportunities | Opportunities accepted with start/payment confirmed |
| Won value | Confirmed value of won opportunities, regardless of whether all payment has been received |
| Win rate | Won opportunities divided by closed opportunities, where closed means `Won` or `Lost` |
| Average won value | Won value divided by won opportunities |

## Review questions

1. Which offer generated the most qualified conversations?
2. Which source generated proposals or paid work, not only attention?
3. Where did leads stall: response, qualification, proposal, or decision?
4. Which proof asset or post was connected to the strongest conversation?
5. What one change will be tested next month?

## Data discipline

- Record consulting income only when receipt is confirmed.
- Keep proposed, invoiced, and received amounts separate.
- Use `TBC` when a value is known to exist but cannot yet be confirmed.
- Never backfill a percentage or revenue figure from memory without a source.
- Store the supporting note or payment reference in the review row's notes field.
