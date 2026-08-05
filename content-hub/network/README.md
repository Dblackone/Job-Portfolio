# Professional Network Manager

Local, human-approved operating files for LinkedIn and other professional networking.

## Purpose

This layer prepares profile improvements, content ideas, comments, connection notes,
follow-ups, and review tasks. It does not log in to LinkedIn, scrape LinkedIn pages,
send invitations or messages, submit applications, or control a browser session.

The user remains the final approver and performs every LinkedIn action manually.

## Files

| File | Purpose |
|---|---|
| `profile-audit.md` | Evidence-based profile review and proposed edits |
| `index.html` | Local dashboard for the approved networking workflow |
| `linkedin-mcp-risk-assessment.md` | Current policy/API evidence and integration decision |
| `network-contacts.csv` | Human-entered relationship and conversation log |
| `weekly-plan.md` | Repeatable weekly networking rhythm |
| `network_draft.py` | Prints unsent connection, follow-up, and comment drafts |
| `network_report.py` | Read-only snapshot joining network contacts to existing pipeline data |

## Approval workflow

1. Add a person or company only from a legitimate professional context or a public
   company research source.
2. Draft the proposed note or message in the repository.
3. Review the identity, context, claim, tone, and destination before copying it.
4. Manually send or post on the platform.
5. Record the actual outcome, date, and next action here.

Never treat a drafted message as sent, a researched company as a lead, or a profile
view as commercial interest. Promote a contact into `content-hub/system/leads.csv`
only when there is an identifiable expression of interest, in line with
`content-hub/system/client-acquisition.md`.

## Source boundaries

- Permitted inputs: user-provided profile exports or screenshots, public company
  pages, user-supplied conversation notes, and repository portfolio evidence.
- No passwords, cookies, session tokens, or private LinkedIn data are stored here.
- No invented metrics, employers, credentials, client outcomes, or project scope.
- When evidence is missing, mark the field `TBC` and request manual confirmation.

## Report

Run from the repository root:

```text
python content-hub/network/network_report.py --as-of YYYY-MM-DD
```

The report is read-only and combines this folder's contact log with the existing
lead and freelance-opportunity trackers. It does not contact any external service.

For a draft, use `network_draft.py` with a confirmed recipient, specific context,
and one verified offer. The output is always labelled `DRAFT — NOT SENT`.
