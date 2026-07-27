# Level 1 — Foundations

For someone who has never opened Revit and has only heard "BIM" in a meeting.

---

## L1.01 — What BIM is

`[STANDARD]` BIM stands for Building Information Modelling. ISO 19650-1:2018 frames it as
**information management** across the whole life cycle of a built asset — strategic planning,
design, engineering, construction, operation, maintenance, refurbishment and end of life.
(Source: ISO 19650-1:2018, https://www.iso.org/standard/68078.html)

The critical word is **information**. A BIM model is a structured database that happens to
have geometry attached. When you place a door in a BIM model, you are not drawing a door
symbol — you are recording that a door of a specific type, size, fire rating, and cost exists
at a specific location in a specific room, and that record can be counted, scheduled, priced,
clashed, and handed to a facilities manager fifteen years later.

`[OPINION]` The most useful one-sentence definition for a beginner: **BIM is the discipline of
building the project as data before you build it as concrete.**

**Why this matters for content:** almost every beginner arrives believing BIM means "3D".
Correcting that is the entire purpose of Week 1.

---

## L1.02 — What BIM is NOT

Five corrections, each worth its own post.

1. **BIM is not software.** Revit is software. ArchiCAD is software. BIM is the process those
   tools serve. You can own Revit and not be doing BIM.
2. **BIM is not 3D.** A 3D model with no information is a 3D model. `[STANDARD]` ISO 19650 is
   about information management; geometry is one carrier of information among several.
3. **BIM is not a deliverable.** "Give me the BIM" is not a meaningful request. Meaningful
   requests name the information: a federated coordination model, an IFC export at a defined
   stage, a COBie asset register.
4. **BIM is not automatic.** Placing a wall does not produce coordinated information. Naming,
   classification, parameters and process discipline produce coordinated information.
5. **BIM is not only for large projects.** `[OPINION]` The coordination value is proportionally
   *higher* on small, tight-budget projects, where a single clash can eat the margin.

---

## L1.03 — History of BIM

`[D — academic]` The idea predates the acronym by decades.

- **1975** — Charles Eastman published a description of the **Building Description System (BDS)**,
  a prototype proposing parametric design and high-quality computable 3D representations
  drawn from *a single integrated database for visual and quantitative analysis*. That sentence
  is essentially the definition of BIM, written fifty years ago.
- **1986** — Robert Aish documented the term **"Building Modelling"** in a published paper,
  arguing for both the concept and the technology needed to implement it.
- **December 1992** — G.A. van Nederveen and F. Tolman published *"Modelling multiple views on
  buildings"* in *Automation in Construction*. This is the first documented published use of the
  term **"Building Information Model"**. Their proposal: aspect models from different project
  participants combine into a single building reference model — which is exactly what model
  federation means today.
- **1997–2002** — Charles River Software (founded 1997) became Revit Technology Corporation
  (2000) and was acquired by Autodesk (2002). See `revit-and-bim.md`.
- **2011** — The UK Government Construction Strategy stated the government would require
  fully collaborative 3D BIM as a minimum by 2016.
  (Source: https://www.designingbuildings.co.uk/wiki/BIM_level_2)
- **2018** — **ISO 19650-1 and -2 published**, taking BIM information management international.
- **2020** — ISO 19650-5 (security-minded approach) published.
- **2025** — ISO 19650-6 (health and safety information) published.
  (Source: https://www.bsigroup.com/en-GB/products-and-services/standards/iso-19650-building-information-modelling-bim/)

`[OPINION]` The lesson worth teaching: BIM is not a new trend. It is a fifty-year-old idea
that finally had the computing power, the standards, and the commercial pressure to land.

---

## L1.04 — Why BIM exists

BIM exists because of three specific, expensive failures in traditional delivery:

1. **Coordination failure.** Drawings from different disciplines are separate documents.
   Nothing in a 2D process forces the architect's ceiling and the engineer's duct to agree.
   They meet for the first time on site, at the worst possible cost.
2. **Information loss.** Design information is re-typed at every handoff — into schedules, into
   tender documents, into the O&M manual. Every re-typing is an opportunity to be wrong.
3. **Late discovery.** Decisions get cheap-to-change early and expensive-to-change late, but
   traditional process gives you the least information exactly when you have the most freedom.

`[OPINION]` BIM's real product is not a model. It is **moving discovery earlier**.

---

## L1.05 — BIM vs CAD

`[VENDOR]` Autodesk states the difference plainly: CAD is using a drafting tool to create
*lines and arcs to represent* a building design, whereas the BIM approach is to use *actual
elements to represent real-world components* — three-dimensional elements with parameters
programmed into them.
(Source: https://www.autodesk.com/solutions/revit-vs-autocad and
https://knowledge.autodesk.com/support/revit/learn-explore/caas/video/youtube/lesson/143344-courseId-100332.html)

The practical difference, stated for a beginner:

| | CAD | BIM |
|---|---|---|
| A wall is | two parallel lines | a wall object with height, material, fire rating, cost |
| Change the wall | you edit every drawing it appears in | you edit it once; every view updates |
| Count the walls | you count them by hand | you schedule them |
| The drawing is | the deliverable | a *view* of the model |

`[OPINION]` The sentence that makes it click: **in CAD you draw what a building looks like;
in BIM you describe what a building is.**

---

## L1.06 — Benefits of BIM

State these as mechanisms, not statistics. `[PRACTICE]` Widely reported benefits include:

- **Coordination before construction** — clashes found in a model cost drawing time; clashes
  found on site cost programme, materials, and relationships.
- **Single source of truth** — one model, many views, no drift between plan and section.
- **Automatic consistency** — schedules, tags, and quantities read the model rather than being
  typed, so they cannot silently disagree with it.
- **Better decisions earlier** — options can be tested when changing them is still cheap.
- **Information that survives handover** — asset data can flow into operations instead of
  dying in a box of drawings. (See L3.11 on COBie.)

> **Content rule:** do **not** quote percentage savings ("BIM saves 20% on rework") unless
> citing the specific study, its sample, and its year. Unsourced ROI numbers circulate
> endlessly in this industry and most trace back to nothing. See `../research/01-verification-log.md`.

---

## L1.07 — Who uses BIM

| Role | What they need from the model |
|---|---|
| **Client / appointing party** | Confidence the asset meets the brief; asset data at handover |
| **Architect** | Design intent, spatial coordination, drawing production |
| **Structural engineer** | Load paths, member sizing, coordination with architecture |
| **MEP engineer** | Routing services through the space that is actually left |
| **Contractor** | Buildability, sequencing, quantities, site logistics |
| **Cost consultant** | Reliable measurement tied to model elements |
| **Facilities manager** | What is installed, where, and when it needs maintenance |

`[OPINION]` A model that only serves the person who built it is not a BIM model. It is a
personal drawing aid.

---

## L1.08 — The model is not the point

`[OPINION]` This is the idea that separates BIM professionals from Revit operators.

A beautiful model with unnamed views, generic families, no parameters, and no naming convention
is worth very little to anyone downstream. A plain-looking model with correct classification,
consistent naming, complete type data, and clean warnings is worth a great deal.

The test: **can someone who has never met you use this model without asking you a question?**

---

## L1.09 — Introduction to Revit

`[VENDOR]` Revit is Autodesk's BIM authoring application for buildings. It hosts the
information that forms the model from which drawings and documents are derived.
(Source: https://www.autodesk.com/solutions/revit-vs-autocad)

Three things a beginner must understand on day one:

1. **There is one project file.** Plans, sections, elevations, 3D views, schedules and sheets
   are all views into that one file.
2. **You model once.** Every view updates because every view is looking at the same thing.
3. **Elements know what they are.** A wall knows it is a wall. That is why it can be scheduled,
   tagged, clashed, and priced.

---

## L1.10 — The Revit interface

| Element | What it does |
|---|---|
| **Ribbon** | Tools, grouped by tab (Architecture, Structure, Insert, Annotate, View, Manage) |
| **Project Browser** | The table of contents for the whole project — every view, sheet, family, group |
| **Properties palette** | Settings for whatever is currently selected, or for the view if nothing is |
| **View Control Bar** | Scale, detail level, visual style, temporary hide/isolate — bottom left |
| **Status Bar** | What Revit is waiting for you to do. Beginners ignore it; experts read it constantly. |
| **Options Bar** | Context-sensitive settings for the active tool, directly under the ribbon |

`[PRACTICE]` If the Project Browser or Properties palette disappears: **View tab → User
Interface** and re-tick it. This is the single most common "my Revit is broken" panic.

---

## L1.11 — Views are windows, not drawings

`[OPINION]` The most important concept in Revit, and the one most beginners never get told.

A floor plan in Revit is not a drawing you made. It is a **live view** of the model, cut at a
height you control, showing categories you control, at a scale you control, in a graphic style
you control. Nothing in a view is "drawn" — it is *revealed*.

Consequences that surprise beginners:

- Something missing from a plan is usually **not deleted**. It is outside the view range,
  hidden in that view, filtered out, or on a hidden workset.
- Two plans of the same floor can look completely different and both be correct.
- Fixing a view fixes a view. Fixing the model fixes every view.

**Diagnostic order when something is missing:** view range → temporary hide/isolate (the cyan
border) → Visibility/Graphics → filters → worksets → phase → design option → discipline.

---

## L1.12 — Levels and grids

**Levels** are horizontal datums — floor heights. **Grids** are vertical planes — structural
column lines. Together they are the skeleton every other element references.

Why they come first:

- Levels host floors, ceilings, roofs and most components. Placing them late means moving
  everything later.
- Elements attached to a level **move with it**. That is the point.
- Grids are the shared coordinate language between architecture and structure.

`[PRACTICE]` Levels are created in **elevation or section views**, never in plan. Grids are
created in plan. This trips up every beginner exactly once.

`[PRACTICE]` On a multi-discipline project, levels and grids should be authored by one
discipline (usually structural) and **Copy/Monitored** by the others. See L2.10.

---

## L1.13 — Walls, floors, roofs

These are **system families** — they live inside the project file and are built from layered
structures rather than loaded from an external file.

- A wall **type** defines its layers: finish, core, insulation, finish, each with a material
  and a thickness.
- Changing the type changes **every instance** of that type in the project. This is a feature,
  and it is also how beginners accidentally change 400 walls.
- Walls have a **location line** (which plane of the wall sits on the line you drew). Getting
  this wrong is the most common cause of walls that look right but measure wrong.

`[PRACTICE]` Never model a wall as a single generic layer if you intend to schedule materials
or produce details from it. The layer structure is the information.

---

## L1.14 — Doors and windows

Doors and windows are **hosted** components — they cannot exist without a wall to sit in.
Delete the wall and the door goes with it.

Key beginner points:

- They cut their own opening. You never model the opening separately.
- They are **loadable families** (see L1.15) — external `.rfa` files loaded into the project.
- Their tag reads a parameter (usually Mark or Type Mark), which is why door schedules can be
  generated rather than typed.

---

## L1.15 — Families explained simply

A family is a **category of thing** in Revit. There are three kinds:

| Kind | Lives where | Examples | Edit how |
|---|---|---|---|
| **System family** | Inside the project | Walls, floors, roofs, ceilings, stairs, dimensions | Duplicate and edit the type |
| **Loadable family** | External `.rfa` file | Doors, windows, furniture, fixtures, tags, titleblocks | Family Editor |
| **In-place family** | Inside the project, unique | A one-off feature that exists nowhere else | In-place editor |

`[PRACTICE]` Use in-place families sparingly. They cannot be reused, they bloat the file, and
they are difficult to schedule consistently.

**Family → Type → Instance** is the hierarchy. Family: "Single-Flush Door". Type: "900 × 2100".
Instance: the specific door in the store room.

---

## L1.16 — Parameters explained simply

A parameter is a piece of information attached to an element.

- **Type parameter** — changing it changes every element of that type. Width of a 900mm door
  type is a type parameter; change it and all 900mm doors change.
- **Instance parameter** — changing it changes only the one you selected. Sill height of one
  specific window is an instance parameter.

`[PRACTICE]` The rule of thumb: *if two elements of the same type could legitimately differ
on this value, it must be an instance parameter.*

Beyond built-in parameters there are **project parameters** (added to categories in one
project), **shared parameters** (defined in an external file so they can be scheduled and
tagged, and stay consistent across projects and firms), and **global parameters** (project-wide
values that can drive dimensions).

`[PRACTICE]` If a value must appear in both a **tag** and a **schedule**, it must be a
**shared parameter**. This single fact resolves a large share of "why can't I tag this" questions.

---

## L1.17 — Schedules

A schedule is a **view of the model in table form**. It is not a spreadsheet you fill in.

- Adding a door to the model adds a row to the door schedule automatically.
- Editing a cell in the schedule **edits the element in the model**. This is bidirectional and
  it surprises everyone the first time.
- Anything you can schedule, you can count, filter, sort, group, and total.

`[PRACTICE]` If you find yourself typing information into a schedule that the model should
already know, stop — the information belongs in the model.

---

## L1.18 — Sheets and titleblocks

A sheet is the printable page. A titleblock is a loadable family that gives the sheet its
border, logo, and metadata fields.

The flow: **model → views → sheets → drawing set.**

- You drag views from the Project Browser onto a sheet. A view can be placed on **one sheet
  only** — if you need it twice, duplicate the view.
- Titleblock fields (project name, number, date, revision) read from **project information** and
  **sheet parameters**, so they fill themselves in.
- View titles, scales, and detail numbers update automatically. Never type a drawing number by
  hand.

---

## L1.19 — Why Revit feels hard at first

`[OPINION]` Worth its own post, because it retains beginners who would otherwise quit.

AutoCAD lets you draw anything, anywhere, any way. Revit does not — it insists you tell it
*what* you are making. That resistance feels like the software fighting you. It is actually the
software refusing to let you produce information that is secretly wrong.

The learning curve is not about tools. It is about accepting that you now have to decide what
things *are* before you can draw them. Everyone who has learned Revit went through this. It
takes roughly three weeks.

---

## L1.20 — Common beginner misconceptions

Ten corrections, each a ready-made post:

1. "BIM means 3D." — No. BIM means managed information.
2. "I know Revit, so I know BIM." — Revit is one authoring tool inside a much larger process.
3. "The model is the deliverable." — The *information* is the deliverable.
4. "It disappeared, so I deleted it." — Usually view range or a hide/isolate.
5. "I'll set up worksets later." — Worksharing decisions are cheapest on day one.
6. "I'll just explode the CAD." — Exploding imported CAD injects thousands of junk line styles.
7. "Detail lines are fine for that." — Drawn lines carry no information and appear in one view only.
8. "Warnings don't matter." — Some do not. Some are why your model is slow and your schedule is wrong.
9. "In-place families are quicker." — Quicker today, expensive for the rest of the project.
10. "The model needs to be perfect." — It needs to meet a defined level of information need. See L2.15.

---

## Sources for this level

- ISO 19650-1:2018 — https://www.iso.org/standard/68078.html
- BSI, ISO 19650 series overview — https://www.bsigroup.com/en-GB/products-and-services/standards/iso-19650-building-information-modelling-bim/
- Autodesk, BIM vs CAD with Revit and AutoCAD — https://www.autodesk.com/solutions/revit-vs-autocad
- Autodesk Knowledge, Understanding the Difference Between BIM and CAD — https://knowledge.autodesk.com/support/revit/learn-explore/caas/video/youtube/lesson/143344-courseId-100332.html
- NBS, What is BIM? — https://www.thenbs.com/knowledge/what-is-building-information-modelling-bim
- Designing Buildings, BIM Level 2 — https://www.designingbuildings.co.uk/wiki/BIM_level_2
- Eastman, C. (1975), Building Description System
- van Nederveen, G.A. & Tolman, F.P. (1992), *Automation in Construction*
