# Networking Drafts

Draft outputs belong here only after the user has reviewed them and chosen to keep
them as durable records. A generated draft is not evidence that anything was sent.

Generate a draft from the repository root:

```text
python content-hub/network/network_draft.py --kind connection --name "Ada Okafor" --company "Example Build" --context "your team's published BIM coordination case study" --offer "Revit model and drawing-package review"
```

Supported kinds:

- `connection`: short context-led connection note;
- `follow-up`: asks for project stage and the decision that needs support;
- `comment`: substantive response to a specific post or project observation.

The command prints text only. It does not save, send, publish, browse, or call a
network service. Do not use a draft until the recipient, context, offer, and claims
have been manually verified.
