# Confirmed income ledger

This ledger records money actually received for architecture, BIM, and
construction consulting. It is intentionally separate from `leads.csv`,
proposals, invoices, and won-opportunity value.

## Entry rule

Add one row per confirmed receipt only after checking a bank notification,
receipt, or other reliable payment record. Keep the client/company name and
project description to the minimum needed for the monthly review. Do not store
bank-account numbers, card details, passwords, or other payment credentials.

## Data discipline

- Use `amount_received_ngn` for the amount actually received in naira.
- Keep `invoice_reference` for reconciliation only; an invoice is not proof of
  receipt.
- Leave the amount blank when the payment cannot yet be verified.
- Record partial payments as separate receipts when they arrive on different
  dates.
- Use the notes field for the evidence location or reconciliation note, not
  sensitive financial data.

The pipeline report reads this file and reports confirmed receipts separately
from proposed and won value. An empty ledger correctly reports `₦0` received.
