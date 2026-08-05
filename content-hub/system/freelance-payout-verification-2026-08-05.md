# Freelance payout verification — 2026-08-05

## Decision

Launch Upwork first. Keep Contra as the second profile and service-offer test,
but do not treat it as a confirmed Nigerian payment route until the account
shows an available payout method and the user successfully verifies it.

## Upwork

Upwork's official help states that Direct to Local Bank supports Nigeria in NGN.
The stated fee is US$0.99 per withdrawal and the stated arrival time is within
four business days after the method is active. The bank-account beneficiary name
must match the verified Upwork name.

Source: https://support.upwork.com/hc/en-us/articles/211063888-How-to-withdraw-earnings-with-Direct-to-Local-Bank
Source: https://support.upwork.com/hc/en-us/articles/211060578-What-are-the-fees-limits-and-timing-of-Direct-to-Local-Bank-payments

Manual check still required: add the user's Nigerian bank details in Upwork and
confirm that the account accepts them before applying for work.

## Contra

Contra's official payout guidance lists local bank transfer, PayPal, Payoneer,
and crypto as payout options. Its current published processor-fee table does not
explicitly list Nigeria for local-bank payout. Therefore, availability for this
user is unverified until the account's payout setup displays a usable method.

Source: https://help.contra.com/en/articles/10008642-payouts
Source: https://help.contra.com/en/articles/9322934-fees-overview

Manual check still required: create the free profile, inspect payout settings,
confirm the beneficiary-name requirements, and record the available method and
fees before treating Contra as a revenue channel.

## Operating rule

No platform is counted as producing income until a client pays and the amount is
recorded in `income-ledger.csv` after the funds are actually received.
