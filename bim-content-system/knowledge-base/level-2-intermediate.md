# Level 2 — Intermediate

For someone who can model competently and now has to work on real projects with other people.

---

## L2.01 — BIM maturity levels

`[C]` The UK maturity model describes four levels:

| Level | Description |
|---|---|
| **0** | Unmanaged CAD |
| **1** | Managed CAD in 2D or 3D |
| **2** | Collaborative 3D with data attached, created in **separate discipline models** |
| **3** | A single collaborative online project model, including construction sequencing, cost and lifecycle management — never defined in detail |

(Source: https://www.designingbuildings.co.uk/wiki/BIM_maturity_levels)

`[STANDARD]` **Important currency note.** The notation "BIM Level 2" is **not used in the
ISO 19650 series**, although it was used extensively in UK procurement and industry
documentation. BSI and nima proposed the "IMI Framework" to replace it.
(Sources: https://www.bsigroup.com/globalassets/localfiles/en-gb/bim/iso-19650/new-iso19650_uk_transition_questions_answers_latestupdated_11_dec_2018.pdf,
https://ukbimframework.org/faq/)

`[OPINION]` So: learn the levels because you will hear them in interviews and old tender
documents, but do not write them into new documents. The current language is information
management to ISO 19650. This distinction is excellent content — it signals you are current.

---

## L2.02 — BIM dimensions 3D–7D `[CONTESTED]`

The generally used ladder:

| Dimension | Adds |
|---|---|
| **3D** | Geometry — the coordinated model |
| **4D** | Time — construction sequencing and programme |
| **5D** | Cost — quantities and cost data linked to elements |
| **6D** | *Disputed — see below* |
| **7D** | *Disputed — see below* |

**The dispute, stated honestly.** `[C]` NBS and Designing Buildings both record that there is
little international consensus beyond 5D:

- Some define **6D** as facility management information and **7D** as sustainability impact data.
- Others define **6D** as sustainability impact data and **7D** as facility management information.

There is no industry consensus on 6D or 7D. Dimensions above 7D (8D–11D) are **not formalised
or standardised** at all. NBS further notes the argument that cost is not really a "dimension"
— it is an additional information field.
(Sources: https://www.thenbs.com/knowledge/bim-dimensions-3d-4d-5d-6d-bim-explained,
https://www.designingbuildings.co.uk/wiki/BIM_dimensions)

`[PRACTICE]` **The professional response:** if specific information is required, specify the
information — not a dimension number. Write "provide asset data per the AIR at handover", not
"provide 6D BIM". If a client insists on dimension language, define precisely what they mean in
the BEP before signing anything.

`[OPINION]` This is the single best beginner-facing content topic in the whole knowledge base,
because the entire internet states 6D and 7D confidently and contradictorily, and almost
nobody says "the industry has not agreed."

---

## L2.03 — The BIM workflow end to end

1. **Requirements** — the client states what information they need and when. (See L3.03.)
2. **Planning** — the delivery team responds with a BIM Execution Plan. (See L2.16.)
3. **Design authoring** — each discipline models in its own file.
4. **Federation** — models are linked into a combined view. (See L2.05.)
5. **Coordination** — clashes and issues are found, assigned, and closed. (See L2.06–L2.07.)
6. **Documentation** — drawings and schedules are produced *from* the model. (See L2.17.)
7. **Construction** — the model supports sequencing, quantities, and site queries.
8. **Handover** — asset information is delivered in a structured format. (See L3.11.)
9. **Operation** — the asset information model is maintained and used. (See L3.05, L3.13.)

`[OPINION]` Notice that authoring — the part everyone thinks BIM *is* — is one step of nine.

---

## L2.04 — The Common Data Environment (CDE)

`[STANDARD]` A CDE is the agreed source of information for a project, used to collect, manage
and disseminate information containers through a managed process.

Information containers move through four states, with an agreed approval and authorisation
process required to move between them:

| State | Meaning |
|---|---|
| **Work in progress** | The author's own work. Not yet suitable for use by anyone else. |
| **Shared** | Released for **coordination only**. Recipients use it to advance their own work in a coordinated way — not as approved information. |
| **Published** | Has undergone stakeholder sign-off. Suitable for use. |
| **Archived** | A permanent record of progress, transactions, and change. |

Each container should have a unique ID following a documented convention, plus attributes
indicating status/suitability, revision, and classification.
(Sources: https://www.thenbs.com/knowledge/what-is-the-common-data-environment-cde,
UK BIM Framework Guidance Part C — https://ukbimframework.org/wp-content/uploads/2020/09/Guidance-Part-C_Facilitating-the-common-data-environment-workflow-and-technical-solutions_Edition-1.pdf)

`[PRACTICE]` A shared folder on a server is not a CDE. A CDE requires states, transitions,
approvals, and an audit trail. Autodesk Construction Cloud, Trimble Connect, Aconex, and
Viewpoint are examples of tools used as CDEs — but the CDE is the *process*, not the tool.

`[OPINION]` The most common real-world failure: teams implement WIP and Published, skip
Shared, and then argue about whether a model was "issued" or "just sent".

---

## L2.05 — Model federation

Federation means **linking** discipline models into a combined view, not merging them into one
file. Each discipline keeps authorship of and responsibility for its own model.

Why linking rather than merging:

- Ownership stays clear. The MEP engineer owns the MEP model; nobody else edits it.
- Each model can be updated independently and re-linked.
- Liability follows authorship.

`[PRACTICE]` Link, never import. An imported model is a frozen copy that will be out of date
within a week and cannot be traced back to its author.

`[PRACTICE]` Federation requires **shared coordinates** so linked models land in the right
place. Getting origin and coordinate setup right at the start is the cheapest hour on any
project (see L2.21).

---

## L2.06 — Clash detection

`[C]` Clash detection is checking a federated model for conflicts between elements. Three types:

| Type | Meaning | Example |
|---|---|---|
| **Hard clash** | Two elements occupy the same space | A duct passing through a beam |
| **Soft clash / clearance** | An element violates another's required clearance zone | A pipe 50mm from a panel that needs 900mm access |
| **Workflow / 4D clash** | Conflict in time or sequence rather than space | Two trades needing the same area in the same week |

(Source: https://www.designingbuildings.co.uk/wiki/Clash_Detection_in_3D_BIM_Models)

`[PRACTICE]` Clash detection is not the goal — **clash resolution** is. A report of 8,000
clashes is a failure of setup, not a productive output. Good practice:

- Run tests between *disciplines*, not everything against everything.
- Set sensible tolerances so insulation overlaps do not swamp real conflicts.
- Group clashes by cause. Eighty clashes usually come from three decisions.
- Assign an owner and a due date to each grouped issue.

`[OPINION]` The number that matters is not clashes found. It is clashes **closed before the
model went to site**.

---

## L2.07 — Coordination meetings

`[PRACTICE]` What actually happens in a well-run coordination meeting:

1. The federated model is on screen, updated with the current week's issued models.
2. Last week's assigned issues are reviewed first — closed, still open, or escalated.
3. New grouped clashes are walked through in the model, not in a spreadsheet.
4. Each issue leaves the room with **a named owner and a date**.
5. Minutes are the issue list, not a separate document.

Anti-patterns worth naming in content: reviewing clashes in a PDF, no assigned owners,
disciplines issuing models the morning of the meeting, and treating the meeting as a design
session rather than a resolution session.

---

## L2.08 — Model health and auditing

`[PRACTICE]` A model health check should be routine, not a rescue operation. What to check:

| Check | Why |
|---|---|
| **Warnings count and type** | Some warnings corrupt schedules and slow the model (see L2.22) |
| **File size trend** | A sudden jump means an import, a huge family, or a runaway link |
| **Purge unused** | Removes unused families and types |
| **Audit on open** | Detects and repairs file corruption |
| **Number of views not on sheets** | Working views are fine; hundreds of orphans are clutter |
| **Imported CAD instances** | Especially exploded imports (see L2.20) |
| **In-place families count** | High counts signal modelling shortcuts |
| **Unplaced rooms / unenclosed rooms** | Breaks area schedules |
| **Groups vs links** | Large nested groups are a common performance killer |

`[PRACTICE]` Do this weekly on a live project, and always before issuing to a CDE.

---

## L2.09 — Worksharing

Worksharing lets multiple people work in one Revit project simultaneously.

- **Central model** — the master file. Nobody works in it directly.
- **Local model** — each user's own copy. You work here.
- **Synchronise with Central (SWC)** — pushes your changes up and pulls others' down.
- **Worksets** — named collections of elements used to manage ownership and visibility.

`[PRACTICE]` Rules that prevent most worksharing pain:

1. Never open the central model directly. Always create a local.
2. Synchronise often — every 30–60 minutes. Long gaps mean painful reconciliation.
3. Relinquish all before you leave. Borrowed elements block your colleagues overnight.
4. Do not synchronise at the same time as everyone else. Stagger it.
5. Worksets are for **ownership and load control**, not for controlling drawing appearance.
   Use view templates and filters for graphics.

`[VENDOR]` Autodesk Platform Services has announced changes to Revit cloud model downloads from
Autodesk Docs / BIM 360 Docs starting 15 February 2026 — worth checking before relying on cloud
worksharing download behaviour.
(Source: https://aps.autodesk.com/blog/changes-are-coming-revit-cloud-model-downloads-autodeskbim-360-docs-starting-february-15-2026)

---

## L2.10 — Copy/Monitor

Copy/Monitor copies elements from a linked model into your own and **watches them for change**.

Typically used for levels, grids, columns, walls, floors, and MEP fixtures.

Why it matters: if the structural engineer moves Grid C by 150mm, you get a warning rather than
discovering it three weeks later in a section. The monitoring relationship is the value — the
copying is incidental.

`[PRACTICE]` Agree at project start **which discipline authors levels and grids**, and have
everyone else Copy/Monitor them. Two disciplines both authoring grids guarantees divergence.

---

## L2.11 — View templates

A view template is a saved set of view properties — scale, detail level, visual style,
visibility/graphics, filters, discipline — applied to many views at once.

`[PRACTICE]` The rule: **graphics live in templates, not in individual views.** If you find
yourself opening Visibility/Graphics on a single view to fix something, ask whether the fix
belongs in the template.

Benefits: a drawing set that looks like one firm produced it; a single change propagating to
200 views; new views that are correct the moment they are created.

---

## L2.12 — Project templates

The project template (`.rte`) is where firm standards live: line weights, text and dimension
styles, materials, wall/floor/roof types, browser organisation, view templates, sheet setup,
titleblocks, schedules, and starting views.

`[OPINION]` A firm without a maintained project template does not have BIM standards — it has
habits. The template is the cheapest quality-control device available, because it makes the
right thing the default.

`[PRACTICE]` Assign one owner. Version it. Review it after every project, not during.

---

## L2.13 — Naming conventions

`[STANDARD]` ISO 19650 requires each information container to have a unique ID following a
documented convention, with attributes for status, revision, and classification.
(Source: UK BIM Framework Guidance Part C)

`[PRACTICE]` What must be named consistently, in order of how much pain bad naming causes:

1. Files and information containers
2. Views (and browser organisation driven by view parameters)
3. Sheets and drawing numbers
4. Worksets
5. Families and types
6. Materials
7. Parameters

`[OPINION]` Naming conventions are the least glamorous and highest-leverage thing in BIM.
Content angle: "the boring skill that gets you hired."

---

## L2.14 — Level of Development (LOD)

`[C]` The **BIMForum LOD Specification** lets AEC practitioners specify and articulate the
content and reliability of BIM models at various stages of design and construction.
(Sources: https://bimforum.org/resource/lod-level-of-development-lod-specification/,
https://bimforum.org/wp-content/uploads/2022/06/BIMForum_LOD_2015_reprint.pdf)

The familiar ladder — LOD 100 through 500 — describes how developed and how *reliable* an
element is, not merely how detailed it looks.

`[PRACTICE]` The distinction that matters: **Level of Detail is how much geometry. Level of
Development is how much you can rely on it.** A photorealistic chair modelled from a guess is
high detail and low development.

---

## L2.15 — Level of Information Need

`[STANDARD]` The concepts "LOD" and "Level of Detail" have been superseded by
**BS EN ISO 19650, BS EN 17412-1 and the "Level of Information Need" approach**.
(Source: https://www.thenbs.com/knowledge/level-of-detail-lod-and-digital-plans-of-work)

`[C]` ISO 7817-1 (based on EN 17412-1) sets out the concepts and principles of Level of
Information Need, and the BIMForum LOD Specification supports implementation of its **geometric**
aspects — the two are intended to work together rather than compete.
(Sources: https://bimforum.org/event/level-of-information-need-and-lod/,
https://www.buildingsmart.org/methods-to-specify-information-requirements-in-digital-construction-projects/)

`[PRACTICE]` Level of Information Need covers geometrical information, alphanumerical
information, and documentation — and is driven by **the purpose the information will be used
for**. The governing question is no longer "what LOD are we at?" but "what decision does this
information have to support, and what is the minimum needed to support it?"

`[OPINION]` The most valuable idea here for a beginner: **more information is not better
information.** Over-modelling is a real and expensive failure mode.

---

## L2.16 — The BIM Execution Plan (BEP)

`[STANDARD]` The BEP is the delivery team's response to the client's exchange information
requirements — how information will be produced, managed, and delivered.
(Source: UK BIM Framework Guidance Part 2 — https://ukbimframework.org/wp-content/uploads/2020/05/ISO19650-2Edition4.pdf)

Typical contents:

- Information management roles and responsibilities
- Software, versions, and exchange formats
- The federation strategy and model breakdown
- Coordinate system, origin, and units
- Naming conventions and classification
- Level of information need by stage and by element
- The CDE, its states, and approval workflows
- Information delivery milestones, MIDP and TIDP (see L3.06)
- Model health and quality assurance procedures
- Clash detection strategy, tolerances, and responsibilities

`[STANDARD]` ISO 19650-2 distinguishes a **pre-appointment BEP** (submitted with the tender,
showing proposed approach and capability) from the **BEP after appointment** (the confirmed
plan the team works to).

---

## L2.17 — Documentation from a model

Drawings are outputs, not artefacts you draw.

- **Tags** read parameters from elements. If the tag is blank, the parameter is blank — the fix
  is in the model, not the tag.
- **Dimensions** should reference model geometry (grids, wall faces, element references) so they
  update when the model changes.
- **Legends** are the one view type that can be placed on multiple sheets.
- **Detail components and detail lines** are view-specific 2D annotation. Legitimate for
  detailing; illegitimate as a way of faking model content.

`[OPINION]` The test of a BIM-produced drawing set: change a door type and see how many
drawings you have to touch by hand. The answer should be zero.

---

## L2.18 — Quantity extraction

Revit schedules can produce counts, lengths, areas, volumes, and material takeoffs directly
from model elements.

`[PRACTICE]` What Revit gives you honestly:

- Counts of discrete items (doors, fittings, fixtures) — reliable.
- Areas and volumes of modelled elements — reliable *to the accuracy of the modelling*.
- Material takeoffs by layer — reliable if wall/floor types are properly layered.

`[PRACTICE]` What it does **not** give you:

- A priced bill of quantities. Rates, waste, labour, plant, preliminaries and measurement rules
  are not in the model.
- Anything that was not modelled. Un-modelled means un-measured.
- Compliance with a standard method of measurement, unless you build that mapping deliberately.

`[OPINION]` "The model gives us the BOQ" is one of the most damaging half-truths in the
industry. The model gives you **quantities**. Turning quantities into a bill is still
professional work.

---

## L2.19 — Phasing and design options

**Phasing** handles time: what is existing, what is demolished, what is new. Every element has
a *phase created* and *phase demolished*; every view has a *phase* and a *phase filter*.

**Design options** handle alternatives: two versions of the same thing coexisting in one model,
with views set to show whichever option you want.

`[PRACTICE]` Use phasing for existing/demolition/new. Use design options for genuine
alternatives under consideration. Do not use design options as a filing cabinet for
abandoned ideas — accept or delete them, because they carry a permanent performance cost.

---

## L2.20 — CAD linking vs importing

`[PRACTICE]` **Link CAD.** Do not import, and never explode.

| | Link | Import |
|---|---|---|
| Updates when the DWG changes | Yes | No |
| Can be removed cleanly | Yes | Partially |
| Brings in foreign line styles and text types | Contained | Permanently, into your project |
| Exploded | N/A | Injects thousands of line styles, text styles, and fill patterns that cannot easily be removed |

`[OPINION]` Exploding an imported DWG is the most common single act of permanent damage a
beginner does to a project file, and it is usually done to "just trace over it quickly."

Additional practice: link CAD into a **single dedicated view** rather than the whole project,
and switch the link off once you have modelled from it.

---

## L2.21 — Model organisation: origin and coordinates

Three things every Revit user must be able to distinguish:

| Point | What it is |
|---|---|
| **Internal origin** | Revit's own fixed 0,0,0. Never moves. |
| **Project base point** | The project's reference for measurement and levels. |
| **Survey point** | The real-world coordinate reference — where the project sits on Earth. |

`[PRACTICE]` The rules that prevent the worst coordination failures:

1. Model close to the internal origin. Models placed kilometres away develop accuracy and
   display problems.
2. Agree shared coordinates once, at the start, and record them in the BEP.
3. Acquire or publish coordinates deliberately — never nudge a link into place by eye.

`[OPINION]` "The links don't line up" is almost never a link problem. It is a coordinates
decision that was never made.

---

## L2.22 — Warnings management

Revit's warnings list is a running record of things Revit could not resolve.

`[PRACTICE]` A working triage:

| Priority | Warning type | Why |
|---|---|---|
| **Critical** | Duplicate instances in the same place | Doubles quantities. Corrupts schedules silently. |
| **Critical** | Elements have identical instances (Mark values duplicated) | Breaks tagging and scheduling |
| **High** | Room/area not enclosed, room not placed | Breaks area schedules and compliance checks |
| **High** | Highlighted elements are joined but do not intersect | Performance and geometry errors |
| **Medium** | Wall and room separation overlap | Area inaccuracy |
| **Low** | Minor slightly-off-axis lines | Tidy when convenient |

`[PRACTICE]` Track the **count over time**, not the absolute number. A model going from 400 to
900 warnings in a week means something structural went wrong that week.

---

## L2.23 — Revit performance

`[PRACTICE]` What actually makes a Revit model slow, roughly in order:

1. Imported and exploded CAD
2. Very large numbers of in-place families
3. Excessive groups, especially nested groups
4. Too many linked models loaded at once (use link visibility and worksets)
5. Complex families with unnecessary detail and unconstrained geometry
6. Very large numbers of warnings
7. Views with detail level Fine and shadows on, left open
8. Modelling far from the internal origin
9. Unpurged, unaudited files carried through many months
10. Over-modelling — geometry nobody will ever use

`[PRACTICE]` The habit that helps most: close views you are not using. Revit regenerates open
views.

---

## L2.24 — Navisworks

`[VENDOR]` Navisworks is Autodesk's model review and coordination tool. It aggregates models
from multiple sources into a single federated model for clash detection and constructability
review, and supports resolving clash and constructability issues between Revit and Navisworks.
(Source: https://www.autodesk.com/learn/ondemand/course/identify-and-resolve-clash-and-constructability-issues-between-revit-and)

What it is used for in practice:

- Federating models from different authoring tools and formats
- Running and managing clash tests (Clash Detective)
- Reviewing, marking up, and assigning issues
- 4D sequencing (TimeLiner)
- Walkthroughs and constructability review on models too heavy for authoring software

`[PRACTICE]` Navisworks reviews; it does not author. Fixes happen in the authoring model and
come back through a re-federation. Clash reports that do not result in authoring changes are
theatre.

---

## L2.25 — Autodesk Construction Cloud and BIM 360 `[VERIFY BEFORE POSTING]`

`[VENDOR]` The Autodesk cloud collaboration landscape has been in transition for several years.
What is documented by Autodesk:

- **BIM 360 platform** — Autodesk support material states there are no plans to retire the
  BIM 360 platform, but that it will no longer be improved or receive new features.
  (Source: https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Is-there-an-end-of-life-EOL-for-BIM-360-planned.html)
- **BIM 360 Glue** — scheduled for retirement on 31 July 2026.
  (Source: https://help.autodesk.com/view/BIM360/ENU/?guid=GUID-5277DEB0-74F7-4314-84D7-3EF51BDC35D2)
- **BIM 360 Plan** and **BIM 360 Team** — separate end-of-life notices exist.
  (Source: https://help.autodesk.com/view/BIM360P/ENU/?guid=GUID-C358A3D1-A19F-49D5-99D2-B57A311E9D74)
- **Revit cloud model downloads** from Autodesk Docs / BIM 360 Docs change from 15 February 2026.
  (Source: https://aps.autodesk.com/blog/changes-are-coming-revit-cloud-model-downloads-autodeskbim-360-docs-starting-february-15-2026)

> **Flag.** Product transition detail in this area changes frequently and search summaries of
> Autodesk's own transition articles were inconsistent during research (one summary conflated
> Autodesk Construction Cloud with Autodesk Forma, which are different products serving
> different purposes). **Re-check the Autodesk support article directly before publishing
> anything specific about product transitions or dates.** See `../research/01-verification-log.md`.

`[OPINION]` For teaching purposes, keep content at the concept level — *what a CDE does* — and
name tools only as examples. Concepts stay true; product names change every eighteen months.

---

## Sources for this level

- NBS, BIM dimensions — https://www.thenbs.com/knowledge/bim-dimensions-3d-4d-5d-6d-bim-explained
- NBS, What is the CDE? — https://www.thenbs.com/knowledge/what-is-the-common-data-environment-cde
- NBS, Level of detail and digital plans of work — https://www.thenbs.com/knowledge/level-of-detail-lod-and-digital-plans-of-work
- Designing Buildings, BIM maturity levels — https://www.designingbuildings.co.uk/wiki/BIM_maturity_levels
- Designing Buildings, BIM dimensions — https://www.designingbuildings.co.uk/wiki/BIM_dimensions
- Designing Buildings, Clash detection — https://www.designingbuildings.co.uk/wiki/Clash_Detection_in_3D_BIM_Models
- BIMForum, LOD Specification — https://bimforum.org/resource/lod-level-of-development-lod-specification/
- BIMForum, Level of Information Need and LOD — https://bimforum.org/event/level-of-information-need-and-lod/
- UK BIM Framework, Guidance Part C (CDE) — https://ukbimframework.org/wp-content/uploads/2020/09/Guidance-Part-C_Facilitating-the-common-data-environment-workflow-and-technical-solutions_Edition-1.pdf
- UK BIM Framework, Guidance Part 2 — https://ukbimframework.org/wp-content/uploads/2020/05/ISO19650-2Edition4.pdf
- UK BIM Framework, FAQ — https://ukbimframework.org/faq/
- BSI, ISO 19650 transition Q&A — https://www.bsigroup.com/globalassets/localfiles/en-gb/bim/iso-19650/new-iso19650_uk_transition_questions_answers_latestupdated_11_dec_2018.pdf
- Autodesk, Revit ↔ Navisworks clash course — https://www.autodesk.com/learn/ondemand/course/identify-and-resolve-clash-and-constructability-issues-between-revit-and
- Autodesk Support, BIM 360 EOL — https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Is-there-an-end-of-life-EOL-for-BIM-360-planned.html
- Autodesk Platform Services, Revit cloud model download changes — https://aps.autodesk.com/blog/changes-are-coming-revit-cloud-model-downloads-autodeskbim-360-docs-starting-february-15-2026
