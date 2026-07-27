# Knowledge Base — Index and Learning Paths

The internal reference every piece of content is drawn from. Organised by difficulty so
content can move a complete beginner to genuine understanding in a logical order.

**Labelling convention used throughout:**

- `[STANDARD]` — defined in a published standard. The standard is named.
- `[PRACTICE]` — widespread industry practice, not codified. Attributed where possible.
- `[VENDOR]` — true of a specific software product, per that vendor's own documentation.
- `[OPINION]` — Vollmann's professional judgement. Must be presented as such in content.
- `[CONTESTED]` — the industry genuinely disagrees. The disagreement must be shown, not hidden.

---

## Level 1 — Foundations (`level-1-foundations.md`)

Someone who has never opened Revit and has only heard "BIM" in a meeting.

| # | Topic | Key idea |
|---|---|---|
| L1.01 | What BIM is | A managed information process, not a 3D model |
| L1.02 | What BIM is NOT | Not software, not 3D, not a deliverable, not automatic |
| L1.03 | History of BIM | 1975 Eastman → 1992 term coined → 2000s software → 2018 ISO 19650 |
| L1.04 | Why BIM exists | Rework, coordination failure, information loss at handover |
| L1.05 | BIM vs CAD | Lines that look like walls vs objects that are walls |
| L1.06 | Benefits of BIM | Coordination, single source of truth, better decisions earlier |
| L1.07 | Who uses BIM | Client, architect, structural, MEP, contractor, FM |
| L1.08 | The model is not the point | The information is the point |
| L1.09 | Introduction to Revit | What it is, what it is for |
| L1.10 | The Revit interface | Ribbon, Project Browser, Properties, View Control Bar |
| L1.11 | Views are windows, not drawings | The single most important Revit concept |
| L1.12 | Levels and grids | The skeleton every project hangs from |
| L1.13 | Walls, floors, roofs | System families and how they behave |
| L1.14 | Doors and windows | Hosted components |
| L1.15 | Families explained simply | System, loadable, in-place |
| L1.16 | Parameters explained simply | Type vs instance |
| L1.17 | Schedules | A live view of the model, not a table you type |
| L1.18 | Sheets and titleblocks | How a model becomes a drawing set |
| L1.19 | Why Revit feels hard at first | It refuses to let you fake it |
| L1.20 | Common beginner misconceptions | Ten things beginners get wrong |

---

## Level 2 — Intermediate (`level-2-intermediate.md`)

Someone who can model competently and now needs to work on real projects with other people.

| # | Topic | Key idea |
|---|---|---|
| L2.01 | BIM maturity levels | Levels 0–3, and why ISO 19650 dropped the language |
| L2.02 | BIM dimensions 3D–7D | What is agreed, and what is not |
| L2.03 | The BIM workflow end to end | Brief → design → coordinate → construct → operate |
| L2.04 | The Common Data Environment | Four container states, one source of truth |
| L2.05 | Model federation | Linking, not merging |
| L2.06 | Clash detection | Hard, soft, workflow clashes |
| L2.07 | Coordination meetings | What actually happens in one |
| L2.08 | Model health and auditing | Warnings, file size, purge, audit |
| L2.09 | Worksharing | Central model, local model, worksets |
| L2.10 | Copy/Monitor | Watching another discipline's grids and levels |
| L2.11 | View templates | Consistency at scale |
| L2.12 | Project templates | Where firm standards live |
| L2.13 | Naming conventions | Why the boring thing matters most |
| L2.14 | Level of Development (LOD) | BIMForum LOD 100–500 |
| L2.15 | Level of Information Need | What replaced LOD thinking |
| L2.16 | The BIM Execution Plan | What goes in one and who writes it |
| L2.17 | Documentation from a model | Annotation, tags, dimensions, legends |
| L2.18 | Quantity extraction | What Revit can and cannot tell you about cost |
| L2.19 | Phasing and design options | Existing, demolition, new — and alternatives |
| L2.20 | CAD linking vs importing | Why importing damages models |
| L2.21 | Model organisation | Origin, project base point, survey point |
| L2.22 | Warnings management | Which warnings actually matter |
| L2.23 | Revit performance | What makes a model slow |
| L2.24 | Navisworks | Federation and clash review |
| L2.25 | Autodesk Construction Cloud and BIM 360 | The current picture |

---

## Level 3 — Advanced (`level-3-advanced.md`)

Someone moving toward BIM Coordinator, BIM Manager, or consulting.

| # | Topic | Key idea |
|---|---|---|
| L3.01 | ISO 19650 series structure | Parts 1–6 and what each covers |
| L3.02 | Appointing / appointed party language | Why the words changed |
| L3.03 | Information requirements hierarchy | OIR → PIR → AIR → EIR |
| L3.04 | The delivery-phase process | Assessment through close-out |
| L3.05 | PIM and AIM | Project vs asset information model |
| L3.06 | MIDP and TIDP | Delivery planning |
| L3.07 | ISO 19650-5 security | Security-minded information management |
| L3.08 | openBIM vs closed BIM | The real trade-off |
| L3.09 | IFC in depth | Schema, versions, what survives export |
| L3.10 | Model View Definitions and IDS | Constraining what IFC must contain |
| L3.11 | COBie | Asset data for handover |
| L3.12 | Classification systems | Uniclass, OmniClass, MasterFormat |
| L3.13 | BIM in facility management | The handover gap |
| L3.14 | Digital twins | What makes a twin a twin |
| L3.15 | Scan-to-BIM | Point cloud to model |
| L3.16 | Dynamo and computational BIM | Visual programming for Revit |
| L3.17 | The Revit API and beyond | When Dynamo is not enough |
| L3.18 | BIM implementation in a firm | People, process, technology — in that order |
| L3.19 | Measuring BIM maturity | Assessing where a firm actually is |
| L3.20 | BIM in developing markets | Adoption without mandates |

---

## Revit and BIM (`revit-and-bim.md`)

The single most misunderstood relationship in the industry. Covers:

- Why Revit is a BIM **authoring** tool
- Revit vs AutoCAD, properly explained
- What Revit can do
- What Revit **cannot** do (the honest list)
- Where Revit sits in the BIM workflow
- Eight misconceptions about Revit and BIM

---

## Learning paths

Learning paths are the spine of the content strategy. Each path is a sequence where every
post assumes only what came before it.

### Path A — "I have never heard of BIM" (Weeks 1–12)
`L1.01 → L1.02 → L1.04 → L1.03 → L1.05 → L1.06 → L1.07 → L1.08 → L2.01 → L2.02 → L2.03 → L1.20`

Ends with: the learner can explain BIM correctly to a colleague and knows what it is not.

### Path B — "I want to open Revit" (Weeks 13–26)
`L1.09 → L1.10 → L1.11 → L1.12 → L1.13 → L1.14 → L1.15 → L1.16 → L1.17 → L1.18 → L2.12 → L2.11 → L2.17 → L1.19`

Ends with: the learner can produce a small, correctly structured, fully documented model.

### Path C — "I work with other people now" (Weeks 27–40)
`L2.04 → L2.05 → L2.09 → L2.10 → L2.13 → L2.20 → L2.21 → L2.06 → L2.24 → L2.07 → L2.08 → L2.22 → L2.23 → L2.19`

Ends with: the learner can hold their own on a coordinated multi-discipline project.

### Path D — "I want to lead BIM" (Weeks 41–52)
`L3.01 → L3.02 → L3.03 → L2.16 → L2.14 → L2.15 → L3.08 → L3.09 → L3.11 → L3.13 → L3.14 → L3.18`

Ends with: the learner understands the standards well enough to write and audit against them.

### Cross-cutting: BIM Career
Career content is woven through all four paths rather than isolated, so it lands with people
at every stage. Career topics are listed in `../strategy/one-year-content-strategy.md`.

---

## Rules for using this knowledge base

1. **Read the entry before writing the post.** Not the summary in this index — the entry.
2. **Never advance a level early.** A Level 3 idea dropped into Week 4 loses the audience.
3. **Repetition of a concept is allowed; repetition of a post is not.** Callbacks build a curriculum. Re-treading the same angle looks like you ran out of ideas.
4. **Every `[CONTESTED]` topic must be presented as contested.** These make the best content because almost nobody else does it honestly.
