# Level 3 — Advanced

For someone moving toward BIM Coordinator, BIM Manager, or consulting work.

---

## L3.01 — The ISO 19650 series

`[STANDARD]` ISO 19650 is titled *Organization and digitization of information about buildings
and civil engineering works, including building information modelling (BIM) — Information
management using building information modelling.*

| Part | Subject | Published |
|---|---|---|
| **19650-1** | Concepts and principles | 2018 |
| **19650-2** | Delivery phase of the assets | 2018 |
| **19650-3** | Operational phase of the assets | 2020 |
| **19650-4** | Information exchange | 2022 |
| **19650-5** | Security-minded approach to information management | 2020 |
| **19650-6** | Health and safety information | 2025 |

(Sources: https://www.iso.org/standard/68078.html, https://www.iso.org/standard/68080.html,
https://www.iso.org/standard/74206.html,
https://www.bsigroup.com/en-GB/products-and-services/standards/iso-19650-building-information-modelling-bim/)

`[STANDARD]` ISO 19650-1 is applicable to the **whole life cycle** of any built asset —
strategic planning, initial design, engineering, development, documentation, construction,
day-to-day operation, maintenance, refurbishment, repair, and end of life. It provides
recommendations for a framework to manage information including exchanging, recording,
versioning, and organising it, for all actors.

**Currency note.** `[STANDARD]` ISO 19650-1 and -2 are under revision — a draft international
standard (ISO/DIS 19650-1, second edition) is in progress.
(Source: https://www.iso.org/standard/89703.html). Content referencing specific clause numbers
should be checked against the current edition before publication.

`[OPINION]` The most useful framing for a beginner: **ISO 19650 is not about modelling. It is
about who asks for what information, when, in what format, and how it is checked.** Almost
nothing in it is about geometry.

---

## L3.02 — Appointing and appointed parties

`[STANDARD]` ISO 19650 replaced client/contractor/subcontractor language with a role-based
vocabulary that works at every tier:

| Term | Meaning |
|---|---|
| **Appointing party** | The party requesting information (previously "employer" or "client") |
| **Lead appointed party** | The party coordinating a delivery team (previously "main contractor" or lead consultant) |
| **Appointed party** | A party delivering information (previously "supplier" or "subcontractor") |
| **Delivery team** | Lead appointed party plus its appointed parties |
| **Task team** | A group within a delivery team producing a defined set of information |

Why the change: the same organisation can be an appointing party in one relationship and an
appointed party in another. The vocabulary describes **the relationship**, not the company.

---

## L3.03 — The information requirements hierarchy

`[STANDARD]` ISO 19650-1 sets out a hierarchy where high-level organisational and project needs
cascade down into contractual information requirements.

```
OIR  Organizational Information Requirements
     Why the organisation needs information at all
        │
        ├──► AIR  Asset Information Requirements
        │         What the operational phase needs
        │            │
PIR  Project Information Requirements                 
     What this project needs                          
        │            │
        └──► EIR  Exchange Information Requirements ◄──┘
                  What a specific appointment must deliver,
                  in what format, at which milestones
```

- **OIR** — organisational information requirements: what the organisation needs to run itself.
- **PIR** — project information requirements: what is needed to deliver this project.
- **AIR** — asset information requirements: what is needed to operate the asset. Used
  contractually in **operational phase** appointments.
- **EIR** — exchange information requirements: the appointing party's formal statement of what
  information is needed, in what format, and at which project milestones. Used contractually in
  **delivery phase** appointments.

`[STANDARD]` **A precision point worth its own post:** in ISO 19650, EIR means **Exchange**
Information Requirements. Under the older PAS 1192 framework it meant **Employer's**
Information Requirements. The clarification reflects the standard's broader application.
(Sources: UK BIM Framework Guidance Part D —
https://www.ukbimframework.org/wp-content/uploads/2021/02/Guidance-Part-D_Developing-information-requirements_Edition-2.pdf,
BSI transition Q&A)

`[OPINION]` Using "employer's information requirements" in 2026 marks you as trained on
pre-2018 material. It is a small thing that experienced people notice immediately.

---

## L3.04 — The delivery-phase process

`[STANDARD]` ISO 19650-2 specifies the information management process for the delivery phase,
structured as a sequence of activities across the appointment lifecycle:

1. **Assessment and need** — the appointing party establishes requirements and the CDE
2. **Invitation to tender** — EIR issued with the tender
3. **Tender response** — pre-appointment BEP, capability and capacity assessment, mobilisation plan
4. **Appointment** — confirmed BEP, MIDP and TIDP agreed, responsibility matrix fixed
5. **Mobilisation** — resources, IT, and information standards put in place and tested
6. **Collaborative production of information** — modelling, checking, reviewing, approving
7. **Information model delivery** — submission, authorisation, acceptance
8. **Project close-out** — archiving and capture of lessons learned

(Source: UK BIM Framework Guidance Part 2 —
https://ukbimframework.org/wp-content/uploads/2020/05/ISO19650-2Edition4.pdf)

`[OPINION]` Notice that six of the eight activities happen before or around modelling. This is
the clearest possible answer to "why do I need standards, I can already model?"

---

## L3.05 — PIM and AIM

| Model | Phase | Purpose |
|---|---|---|
| **PIM — Project Information Model** | Delivery | Supports design and construction decisions |
| **AIM — Asset Information Model** | Operation | Supports operation, maintenance, and management |

`[STANDARD]` The PIM is developed during delivery. At handover, the information the operational
phase actually needs — defined by the AIR — transfers into the AIM, which is then maintained for
the life of the asset.
(Source: UK BIM Framework Guidance Part 3 —
https://ukbimframework.org/wp-content/uploads/2020/09/Guidance-Part-3_Operational-phase-of-the-asset-life-cycle_Edition-1.pdf)

`[OPINION]` The PIM is not the AIM. Handing an operations team the full design model is not a
handover — it is a data dump. Most of a design model is irrelevant to a maintenance engineer,
and the 5% that matters is buried.

---

## L3.06 — MIDP and TIDP

| Term | Meaning |
|---|---|
| **TIDP — Task Information Delivery Plan** | What one task team will deliver, when, and who is responsible |
| **MIDP — Master Information Delivery Plan** | All TIDPs consolidated into the delivery team's overall plan |

`[PRACTICE]` TIDPs roll up into the MIDP. The MIDP is the single schedule the lead appointed
party manages against, and it is where information delivery becomes a programme item rather
than an assumption.

---

## L3.07 — ISO 19650-5: security-minded information management

`[STANDARD]` ISO 19650-5:2020 specifies principles and requirements for security-minded
information management, and the security-minded management of sensitive information that is
obtained, created, processed, and stored.
(Source: https://www.iso.org/standard/74206.html)

`[PRACTICE]` Where this bites in practice: models of sensitive assets (utilities, transport,
defence, data centres, financial institutions) contain information that is valuable to people
you do not want to have it — service routes, security systems, structural vulnerabilities,
access control. A security-minded approach asks what could be inferred from an information
container, not just what is explicitly in it.

`[OPINION]` Rarely taught, increasingly asked about in interviews for infrastructure work.

---

## L3.08 — openBIM vs closed BIM

`[STANDARD]` **openBIM** is buildingSMART International's term for working with open,
vendor-neutral standards. IFC — ISO 16739 — is the official open standard underpinning it.
(Sources: https://www.buildingsmart.org/about/openbim/,
https://technical.buildingsmart.org/standards/ifc/)

`[PRACTICE]` The honest trade-off, stated without vendor bias:

| | Closed / native workflow | openBIM workflow |
|---|---|---|
| **Fidelity** | Full — nothing is lost between same-vendor tools | Constrained by what the exchange schema supports |
| **Editability** | Fully parametric and editable | Exchanged data is typically reference/read-oriented |
| **Lock-in** | High — the project depends on one vendor's file format | Low — data is readable without the authoring tool |
| **Long-term readability** | Depends on that vendor and version | Open, documented schema |
| **Setup effort** | Low | Requires deliberate mapping and testing |

`[STANDARD]` buildingSMART publishes a register of national openBIM/IFC mandates, evidencing
that a growing number of governments require IFC deliverables on public projects.
(Source: https://www.buildingsmart.org/wp-content/uploads/2025/03/IFC-Mandate_2025.pdf)

`[OPINION]` It is not a binary. Most real projects author in native formats and **exchange** in
open ones. The professional position is: choose the authoring tool for capability, and require
open formats for exchange and archive.

---

## L3.09 — IFC in depth

`[STANDARD]` IFC — Industry Foundation Classes — is a standardised digital description of the
built environment, including buildings and civil infrastructure. It is published as ISO 16739.
(Sources: https://technical.buildingsmart.org/standards/ifc/,
https://www.iso.org/standard/70303.html)

Versions in practical use:

| Version | Notes |
|---|---|
| **IFC2x3** | Long-standing workhorse; still widely required in project specifications |
| **IFC4** | Extends IFC beyond buildings toward infrastructure |
| **IFC4.3** | Major step for infrastructure — adds capability for describing non-man-made objects and georeferencing |

(Source: https://ifc43-docs.standards.buildingsmart.org/ and buildingSMART technical pages)

`[PRACTICE]` What every practitioner needs to know about IFC export:

1. **IFC is an exchange format, not a working format.** You do not design in IFC.
2. **What exports depends on mapping.** Elements must be mapped to the right IFC entity, or a
   wall becomes a generic building element and downstream tools cannot use it.
3. **Property sets carry the data.** Geometry exports easily; *information* exports only if you
   deliberately map parameters into property sets.
4. **Test your export early.** Export at concept stage, open it in a free IFC viewer, and check
   what survived. Discovering the mapping is wrong at handover is a project-scale problem.

`[OPINION]` "We'll just export IFC at the end" is the openBIM equivalent of "we'll set up
worksets later."

---

## L3.10 — Model View Definitions and IDS

`[STANDARD]` IFC is a large schema; most exchanges need only part of it.

- **MVD (Model View Definition)** — a defined subset of the IFC schema for a specific exchange
  purpose (for example coordination view, reference view).
- **IDS (Information Delivery Specification)** — a buildingSMART standard for expressing
  information requirements in a computer-interpretable way, so that a model can be **checked
  automatically** against what was asked for.

`[OPINION]` IDS is the most consequential development for BIM quality assurance in years,
because it turns "please include fire ratings on all doors" from an email into a machine-checkable
rule. Worth building content around as it matures. `[VERIFY]` — confirm current IDS version and
adoption status against buildingSMART technical pages before making claims about maturity.

---

## L3.11 — COBie

`[STANDARD]` COBie — **Construction to Operations Building Information Exchange** — is a
non-proprietary data format for publishing a subset of building information focused on
delivering **asset data rather than geometric information**.
(Sources: https://www.thenbs.com/knowledge/what-is-cobie, https://nibs.org/nbims/v3/cobie,
https://www.wbdg.org/bim/cobie)

What it contains: space, product, and equipment schedules from design drawings, combined with
as-built, operations & maintenance, and commissioning information captured during construction —
attributes of the facility, its systems and assets, product types, warranties, and maintenance
requirements.

Its purpose: to reduce or eliminate the delay between handover and the point at which the
facilities management system can begin operating and maintaining the assets.

`[STANDARD]` Formally, COBie is defined as **a subset of the Industry Foundation Classes**,
though it can also be conveyed as worksheets or in relational databases. It is a US national
specification of facility handover requirements, and forms part of the National BIM
Standard–United States.

`[STANDARD]` **Origin:** devised by William East of the United States Army Corps of Engineers,
who authored a pilot standard in 2007.
(Source: https://cobiecert.buildingsmart.org/history/)

`[OPINION]` COBie is widely misunderstood as "a spreadsheet". The spreadsheet is a *carrier*.
COBie is a specification of what asset information must exist at handover. The reason it has a
reputation for being painful is that teams treat it as an export at the end rather than a data
discipline from the start.

---

## L3.12 — Classification systems

`[PRACTICE]` Classification gives every element a standard code so information can be sorted,
compared, and costed across projects and organisations.

| System | Origin | Typically used for |
|---|---|---|
| **Uniclass** | UK (NBS) | Unified classification across the whole life cycle |
| **OmniClass** | North America | Classification tables for the construction industry |
| **MasterFormat** | North America | Specification section organisation |
| **UniFormat** | North America | Elemental classification for early cost planning |

`[STANDARD]` ISO 19650 requires information containers to carry classification as an attribute.
(Source: UK BIM Framework Guidance Part C)

`[OPINION]` Classification is the difference between data you can query and data you can only
read. Most firms skip it, then wonder why they cannot benchmark across projects.

---

## L3.13 — BIM in facility management

The handover gap is the largest unrealised value in BIM.

`[PRACTICE]` What operations actually needs, and what design models usually contain:

| Operations needs | Typical design model has |
|---|---|
| Asset register with unique IDs | Elements with no persistent identifiers |
| Manufacturer, model, serial number | Generic placeholder families |
| Warranty dates and terms | Nothing |
| Maintenance intervals | Nothing |
| Spatial location by room and system | Rooms, sometimes unenclosed |
| Replacement cost and expected life | Nothing |

`[STANDARD]` The mechanism to close this gap is the AIR (see L3.03) driving the EIR, so that
operational information is collected **during** delivery rather than reconstructed after it.
COBie (L3.11) is one delivery format for that information.

`[OPINION]` The uncomfortable truth: most BIM projects deliver a coordination benefit and stop.
The whole-life benefit is available and rarely claimed, because nobody defined the AIR.

---

## L3.14 — Digital twins

`[C]` The **Gemini Principles**, published by the Centre for Digital Built Britain in December
2018, define a digital twin in the built-environment context as *"a realistic digital
representation of assets, processes or systems in the built or natural environment."*

What distinguishes a digital twin from any other digital model is **its connection to the
physical twin, based on data from the physical asset or system.**
(Sources: https://www.cdbb.cam.ac.uk/system/files/documents/TheGeminiPrinciples.pdf,
https://www.designingbuildings.co.uk/wiki/Digital_twin)

The nine Gemini Principles: **public good, value creation, insight, security, openness, quality,
federation, curation, evolution.**
(Source: https://www.designingbuildings.co.uk/wiki/Gemini_principles)

`[PRACTICE]` The practical test, and a strong content hook: **if it does not receive data from
the real asset, it is not a twin — it is a model.** A BIM model with sensors feeding live data
into it and informing decisions is on the way to being a twin. A BIM model rendered nicely is not.

`[C]` BIM information management is the foundation digital twins are built on — without
structured, reliable asset information there is nothing for live data to attach to.
(Source: https://digitaltwinhub.co.uk/digital-twins-need-information-management-using-bim-for-the-built-environment/)

---

## L3.15 — Scan-to-BIM

`[C]` Scan-to-BIM converts a physical environment into an intelligent digital model using
laser scanning or photogrammetry to produce a point cloud, which is then modelled.

Quality driver: **dense, clean point clouds with minimal noise and complete coverage enable
faster, more accurate modelling** than sparse or noisy datasets with coverage gaps.
(Source: https://www.designingbuildings.co.uk/wiki/Scan_to_BIM_Workflow_and_Deliverables:_A_Technical_Guide)

`[PRACTICE]` The workflow:

1. **Survey planning** — scan positions, targets, control, and required accuracy
2. **Capture** — terrestrial laser scanning, mobile scanning, or photogrammetry
3. **Registration** — aligning individual scans into one coordinated cloud
4. **Cleaning and decimation** — removing noise, people, vehicles, reflections
5. **Georeferencing** — placing the cloud on real-world coordinates
6. **Modelling** — authoring BIM elements to a **defined level of information need**
7. **Verification** — deviation analysis of model against cloud

`[PRACTICE]` The commercial trap: scan-to-BIM scopes that say "model everything" are
unpriceable and unfinishable. The scope must state tolerance, coverage, and level of
information need per element type. `[OPINION]` This is where most scan-to-BIM projects lose money.

---

## L3.16 — Dynamo and computational BIM

`[VENDOR]` Dynamo is a visual programming environment that works with Revit, letting users
build scripts by connecting nodes rather than writing code. Autodesk documents workflows where
Dynamo scripts run clash tests using the Navisworks core and return visual feedback into the
active Revit project as clash indicators and 3D clash views.
(Sources: https://blogs.autodesk.com/revit/2017/10/25/revit-dynamo-navisworks-mep-coordination/,
https://static.au-uw2-prd.autodesk.com/Class_Handout_AS125109_How_to_Use_Dynamo_to_Visibly_Show_Navisworks_Clashes_into_Revit_Felix_Tan_1.pdf)

`[PRACTICE]` Where Dynamo genuinely earns its keep:

- Bulk parameter reading and writing across thousands of elements
- Renaming views and sheets to a convention
- Placing elements from external data (a spreadsheet of coordinates)
- Auditing — finding elements that violate a rule
- Generating and populating sheets
- Exporting model data to Excel and back

`[PRACTICE]` Where it does not: anything you will do once. A script that takes three hours to
write and saves ten minutes once is a hobby, not automation.

`[OPINION]` The honest rule for learning Dynamo: learn it when you have a specific repetitive
task that hurts. Learning it "because it is the future" produces people who can build a script
but cannot say why.

---

## L3.17 — The Revit API and beyond

`[PRACTICE]` Dynamo has limits — performance on very large operations, transaction control,
user interface, and distribution to a team. Beyond it sits the **Revit API** (C# / .NET),
used to build add-ins, and the growing ecosystem of open-source Revit tooling.

`[OPINION]` Career note: the jump from Dynamo to the API is the jump from "productive BIM
professional" to "BIM developer", and it substantially changes what you can charge. It is also
a genuine software-engineering discipline, not an extension of modelling.

---

## L3.18 — BIM implementation in a firm

`[OPINION]` The order that works, and the order most firms attempt:

| | Order that works | Order most firms attempt |
|---|---|---|
| 1 | People — who is accountable for information | Technology — buy licences |
| 2 | Process — standards, templates, conventions | People — send everyone on a course |
| 3 | Technology — tools that serve the process | Process — write a standard nobody reads |

`[PRACTICE]` A realistic implementation sequence:

1. Name an owner. Not a committee.
2. Pick **one** pilot project with a supportive team.
3. Build a project template and a naming convention. Nothing else.
4. Run the pilot. Record what broke.
5. Fix the template and convention from real evidence.
6. Only then write the firm's standard, and only then roll out.
7. Measure something specific — RFIs from coordination, drawing revision counts, time to produce a set.

`[OPINION]` The most common failure is buying training before defining standards. People come
back from the course, find no template, and revert within a month.

---

## L3.19 — Measuring BIM maturity

`[PRACTICE]` Honest indicators that a firm is actually doing BIM, rather than owning Revit:

- Is there a maintained project template with an owner?
- Do drawings come out of the model without manual patching?
- Is there a documented naming convention that is actually used?
- Are models federated and clash-checked on a schedule, not on panic?
- Is there a BEP, and does anyone read it after week two?
- Do warnings get triaged, or just accumulate?
- Can someone other than the author use the model?
- Does any information reach operations in a structured form?

`[OPINION]` A firm scoring well on the first four is doing better than most. A firm scoring
well on all eight is rare anywhere in the world.

---

## L3.20 — BIM in developing markets

`[OPINION]` This section is explicitly professional opinion grounded in practice, not standards.
It should always be labelled as such in content — and it is a genuine differentiator, because
almost all BIM content assumes a UK, EU, or North American context with a government mandate.

Realities where there is no national BIM mandate:

- **Adoption is client-led or contractor-led, not regulation-led.** The business case has to be
  made commercially, every time.
- **Skills are the binding constraint, not software.** Licences are obtainable; experienced
  coordinators are not.
- **Fragmented procurement** means models often stop at the end of design, with no path into
  construction or operations.
- **The value proposition is different.** Where labour is comparatively cheap and materials are
  comparatively expensive and import-dependent, *quantity accuracy and rework avoidance* are a
  stronger argument than *labour productivity*.
- **Partial adoption still pays.** Coordinated design and reliable quantities deliver most of
  the accessible value even with no CDE and no facility management pipeline.

`[PRACTICE]` The pragmatic ladder for a firm in a non-mandated market: coordinated authoring →
consistent templates and naming → federation and clash detection → CDE discipline → structured
handover. In that order, and no faster than the team can absorb.

---

## Sources for this level

- ISO 19650-1:2018 — https://www.iso.org/standard/68078.html
- ISO 19650-2:2018 — https://www.iso.org/standard/68080.html
- ISO 19650-5:2020 — https://www.iso.org/standard/74206.html
- ISO/DIS 19650-1 (revision) — https://www.iso.org/standard/89703.html
- ISO 16739-1:2018 (IFC) — https://www.iso.org/standard/70303.html
- BSI, ISO 19650 series — https://www.bsigroup.com/en-GB/products-and-services/standards/iso-19650-building-information-modelling-bim/
- UK BIM Framework, Guidance Parts 1, 2, 3, C, D, E — https://ukbimframework.org/
- buildingSMART, openBIM — https://www.buildingsmart.org/about/openbim/
- buildingSMART, IFC — https://technical.buildingsmart.org/standards/ifc/
- buildingSMART, IFC 4.3.2 documentation — https://ifc43-docs.standards.buildingsmart.org/
- buildingSMART, Global openBIM Mandates 2025 — https://www.buildingsmart.org/wp-content/uploads/2025/03/IFC-Mandate_2025.pdf
- buildingSMART, COBie history — https://cobiecert.buildingsmart.org/history/
- NIBS, COBie (NBIMS-US v3) — https://nibs.org/nbims/v3/cobie
- WBDG, COBie — https://www.wbdg.org/bim/cobie
- NBS, What is COBie? — https://www.thenbs.com/knowledge/what-is-cobie
- CDBB, The Gemini Principles — https://www.cdbb.cam.ac.uk/system/files/documents/TheGeminiPrinciples.pdf
- Designing Buildings, Digital twin — https://www.designingbuildings.co.uk/wiki/Digital_twin
- Designing Buildings, Scan to BIM — https://www.designingbuildings.co.uk/wiki/Scan_to_BIM_Workflow_and_Deliverables:_A_Technical_Guide
- Autodesk blogs, Revit/Dynamo/Navisworks MEP coordination — https://blogs.autodesk.com/revit/2017/10/25/revit-dynamo-navisworks-mep-coordination/
