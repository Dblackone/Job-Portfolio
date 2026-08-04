# Client Acquisition System

This is the operating layer between portfolio visibility and paid architecture,
BIM, and construction consulting work. It is intentionally small: every live
opportunity needs a clear next action, a due date, and an honest stage.

## Offers

| Offer | Best-fit situation | First conversation | Evidence to send |
|---|---|---|---|
| BIM model and drawing review | A live Revit or drawing package needs an independent check | Ask for the project stage, disciplines, package size, and review deadline | BIM portfolio and model-review post |
| Design-to-site coordination | A team is moving from design intent to buildable information | Ask where coordination is currently breaking down and who owns decisions | Selected project work and coordination experience |
| Construction project controls | An active build needs stronger programme, procurement, cost, or reporting visibility | Ask for project phase, current reporting rhythm, and immediate delivery risk | Construction portfolio and project-management experience |

## Pipeline stages

| Stage | Meaning | Required next action |
|---|---|---|
| New | An identifiable person or company has shown interest | Log source, offer, and contact details |
| Contacted | A first response or outreach message has been sent | Set a follow-up date within 2 business days |
| Qualified | Scope, timing, decision-maker, and budget signal are understood | Confirm the consultation or request the relevant files |
| Proposal | A defined scope and fee framework has been sent | Follow up on the agreed date |
| Won | Scope accepted and start/payment is confirmed | Record agreed value and delivery start |
| Nurture | Relevant opportunity, not ready now | Set a specific re-contact date |
| Lost | Not proceeding or not a fit | Record reason; do not continue unqualified chasing |

## Minimum lead record

Every row in `leads.csv` should answer:

- Who is the prospect and how can they be reached?
- Which offer fits the problem?
- Where did the lead come from?
- What project stage and urgency did they describe?
- What is the next action and its due date?
- What value was proposed or confirmed, in `₦`?
- What happened, including the reason for a lost or dormant lead?

### Prospect research queue

`system/prospect-list.csv` is a separate research queue for public company
targets. A company belongs here when its public website suggests a plausible fit;
that is not evidence of interest. Do not count research-queue rows as leads,
qualified opportunities, or pipeline value. Move a company into `leads.csv`
only after a real contact, reply, referral, or other identifiable expression of
interest has been recorded.

Work the queue in small batches: review the public project context, choose the
most relevant offer, find the correct company contact route, and log the action
before sending anything. Keep personal contact details out of the research queue
unless the person has been contacted in a legitimate professional context and the
information is needed for the active follow-up.

Do not estimate a project value until the prospect has supplied enough scope to
support it. Keep unknown values blank or mark them `TBC`.

## Response and follow-up cadence

1. **Within 24 hours:** acknowledge the enquiry, restate the problem, and ask only
   for the information needed to qualify it.
2. **Within 2 business days:** follow up if the prospect has not replied.
3. **After qualification:** send a concise scope, assumptions, deliverables, fee,
   and proposed start date.
4. **On the agreed follow-up date:** ask for a decision or the missing input.
5. **After two unanswered follow-ups:** move the lead to `Nurture` with a future
   date, rather than leaving it indefinitely in the active pipeline.

## Weekly review

Review the tracker once per week and record:

- New leads by source and offer
- Qualified leads
- Consultations held
- Proposals sent
- Won value in `₦`
- Win rate: won opportunities divided by closed opportunities
- Average won value
- Leads with an overdue next action

The purpose is to learn which offer and channel produce conversations that can
become paid work. Do not use impressions or follower count as a substitute for
pipeline evidence.

## Source tags

Use one source tag per lead so the channel can be compared later:

`portfolio` · `linkedin` · `instagram` · `whatsapp` · `referral` · `direct outreach` · `repeat client` · `other`

## Weekly acquisition rhythm

Use this as a starting operating target, then adjust from measured response and
available time. The numbers below are activity targets, not claimed results.

| Day | Activity | Evidence of completion |
|---|---|---|
| Monday | Publish or repurpose one authority asset tied to an offer | Post URL and source offer |
| Tuesday | Identify 5 relevant architecture firms, BIM teams, contractors, or project owners | Five named prospects with a reason for fit |
| Wednesday | Send 3 personalized messages and log them as `Contacted` | Three tracker rows with next-action dates |
| Thursday | Follow up on open conversations and answer comments or replies | Updated stages and notes |
| Friday | Ask one past client, collaborator, or professional contact for a relevant introduction | Referral request logged, whether accepted or declined |
| Sunday | Review source, offer, stage, and overdue actions | Weekly pipeline review completed |

## Outreach templates

Personalize the bracketed fields. Do not send a generic batch message.

### Architecture firm or BIM team

> Hello [Name]. I reviewed [specific project, service, or visible need] and noticed
> your team works across [specific discipline]. I support architecture and
> construction teams with Revit documentation, model review, and design-to-site
> coordination. If you have a live package that needs an independent review or
> additional delivery capacity, I can share a concise scope for consideration.
> What stage is the current project at?

### Contractor or project owner

> Hello [Name]. I work across construction delivery, BIM coordination, and project
> controls. I am reaching out because [specific project or phase] appears to be at
> a point where clear information and follow-through matter. If useful, I can review
> the current package and outline the coordination or reporting support that would
> be most practical. What is the immediate delivery priority?

### Referral request

> I am opening a small number of consulting engagements for BIM model and drawing
> reviews, design-to-site coordination, and construction project controls. If you
> know a project owner, architecture firm, or contractor who is dealing with a live
> coordination or delivery issue, an introduction would be appreciated. I can send
> a clear scope after understanding the project stage and need.

### Follow-up

> Following up on [project or need]. If the timing is not right, I can move this to
> a later follow-up date. If the need is active, please share the project stage,
> relevant disciplines, and desired decision date so I can respond with a defined
> next step.
