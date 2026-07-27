# Accuracy Verification Log

Phase 13. What was verified, how, and what remains uncertain.

**Research date:** July 2026

---

## Method, stated honestly

Research was carried out using web search against a restricted set of authoritative domains
(ISO, buildingSMART, BSI, UK BIM Framework, NIBS, WBDG, NBS, BIMForum, CDBB, Autodesk,
Designing Buildings).

**An important limitation, and it affects how you should use this material.**

Several authoritative sites — including buildingsmart.org, technical.buildingsmart.org,
thenbs.com, and autodesk.com — returned HTTP 403 to direct page retrieval during this research
session. Their content was therefore reached through **search-engine summaries of those pages**
rather than by reading the pages directly.

This means:

| Confidence | What it applies to |
|---|---|
| **High** | Facts that appeared consistently across multiple independent authoritative sources, and that match well-established published standards (ISO 19650 structure, IFC as ISO 16739, CDE states, COBie definition, the 6D/7D dispute) |
| **Medium** | Specific wording attributed to a single source reached only via summary |
| **Low — flagged below** | Product transition details, dates, and figures |

**Practical rule before publishing:** for anything below marked `[VERIFY BEFORE PUBLISHING]`,
open the primary source directly and confirm. For everything else, the claim is sound but the
exact wording should be checked if you intend to quote rather than paraphrase.

**Nothing in this system was invented.** Where a fact could not be established, it is flagged
rather than filled in.

---

## Verified — high confidence

| Claim | Source | Notes |
|---|---|---|
| ISO 19650 is about information management across the whole asset life cycle | ISO 19650-1:2018 | Consistent across ISO, BSI, and UK BIM Framework |
| The series has parts 1–6; Part 6 (health and safety) published 2025 | BSI, ISO | Part 3 (2020), Part 4 (2022), Part 5 (2020) |
| ISO 19650-1 is under revision (ISO/DIS 19650-1, 2nd edition) | ISO | Confirms clause references should be checked against the current edition |
| "BIM Level 2" notation is not used in the ISO 19650 series | BSI transition Q&A, UK BIM Framework FAQ | BSI and nima proposed the IMI Framework in its place |
| UK maturity Levels 0–3 definitions | Designing Buildings | Level 3 was never defined in detail |
| The UK Government Construction Strategy 2011 set a 2016 requirement | Designing Buildings | Level 2 on centrally procured public projects from April 2016 |
| CDE container states: work in progress, shared, published, archived | NBS, UK BIM Framework Guidance Part C | With agreed approval and authorisation to move between states |
| "Shared" limits use to coordination activities | NBS | Important and frequently misunderstood |
| Containers require unique IDs, status, revision, classification attributes | UK BIM Framework Guidance Part C | |
| **There is no industry consensus on 6D or 7D BIM** | **NBS, Designing Buildings** | **Both record the same split. This is the single best-evidenced contested claim in the system.** |
| 8D–11D are not formalised or standardised | NBS, Designing Buildings | |
| NBS records the argument that cost is not really a dimension | NBS | |
| IFC is ISO 16739 | ISO, buildingSMART | ISO 16739-1:2018 is the edition confirmed |
| IFC 4.3 adds georeferencing and non-man-made object description | buildingSMART | |
| IFC4 extends IFC from building to infrastructure | buildingSMART | |
| COBie is a non-proprietary format for asset data rather than geometry | NBS, NIBS, WBDG | |
| COBie is formally a subset of IFC | NBS, Designing Buildings | Can also be conveyed as worksheets or databases |
| COBie was devised by William East (USACE), pilot standard 2007 | buildingSMART COBie history | |
| COBie is part of NBIMS-US | NIBS | |
| LOD and Level of Detail superseded by ISO 19650, EN 17412-1, Level of Information Need | NBS | |
| ISO 7817-1 (based on EN 17412-1) sets out Level of Information Need; BIMForum LOD supports its geometric aspects | BIMForum, buildingSMART | The two are complementary |
| Gemini Principles published December 2018 by CDBB | CDBB, Designing Buildings | |
| Digital twin = a realistic digital representation of assets, processes or systems, distinguished by connection to the physical twin via data | CDBB Gemini Principles | |
| The nine Gemini Principles | Designing Buildings, CDBB | Public good, value creation, insight, security, openness, quality, federation, curation, evolution |
| ISO 19650-5 covers security-minded information management | ISO 19650-5:2020 | |
| OIR / PIR / AIR / EIR hierarchy | ISO 19650-1, UK BIM Framework Guidance Part D | |
| **EIR means Exchange Information Requirements in ISO 19650** (previously Employer's) | UK BIM Framework Guidance Part D, BSI | Explicitly described as a clarification in the transition |
| AIR is used contractually in operational-phase appointments; EIR in delivery-phase | UK BIM Framework Guidance Part D | |
| Autodesk: CAD creates lines and arcs representing a design; BIM uses actual elements with parameters | Autodesk | Autodesk's own framing, appropriate to cite as vendor positioning |
| Autodesk: Revit hosts the information from which drawings and documents are derived | Autodesk | |
| Navisworks is used for federated clash detection and constructability review with Revit | Autodesk | |
| Dynamo can run clash tests using the Navisworks core and return clash indicators and 3D clash views into Revit | Autodesk blogs, Autodesk University handout | |
| Eastman (1975) described the Building Description System with a single integrated database for visual and quantitative analysis | Academic / multiple corroborating sources | |
| van Nederveen & Tolman (1992) first documented "Building Information Model" in *Automation in Construction*, December 1992 | Academic | Consistently reported across independent sources |
| Aish (1986) documented "Building Modelling" | Academic | |
| Scan-to-BIM quality depends on dense, clean, complete point clouds | Designing Buildings | |

---

## Flagged — verify before publishing

### F1. Autodesk product transitions `[VERIFY BEFORE PUBLISHING]`

**Status: partially verified, actively changing, and one summary was internally inconsistent.**

What Autodesk sources indicate:

- BIM 360 platform: no plans to retire, but no further improvement or new features.
- BIM 360 Glue: retirement 31 July 2026.
- BIM 360 Plan and BIM 360 Team: separate end-of-life notices exist.
- Revit cloud model downloads from Autodesk Docs / BIM 360 Docs change from 15 February 2026.

**The problem:** during research, a search summary of an Autodesk transition article stated that
projects should be migrated to "Autodesk Forma (formerly Autodesk Construction Cloud (ACC))".
**This is not correct as stated** — Autodesk Forma and Autodesk Construction Cloud are different
products serving different purposes, and Forma is not a rename of ACC. That summary is
unreliable, which means the whole transition picture from that source should be treated as
unreliable.

**Action:** open the Autodesk support articles directly before publishing anything specific
about product names, transitions, or dates. Do not repeat the Forma/ACC relationship in any
form.

**Mitigation already applied:** `knowledge-base/level-2-intermediate.md` L2.25 carries this flag
inline, and the content strategy keeps cloud-platform teaching at the concept level ("what a CDE
does") rather than the product level.

### F2. Revit corporate history figures `[SECONDARY SOURCE]`

Commonly reported: Charles River Software founded 1997 in Newton, Massachusetts, by Leonid Raiz
and Irwin Jungreis, both previously Pro/ENGINEER developers; renamed Revit Technology
Corporation January 2000; acquired by Autodesk in 2002 for approximately US$133 million; the
name derives from "Revise Instantly".

**These come from encyclopaedic and trade sources, not from an Autodesk or SEC primary source.**

**Action:** the founding and acquisition *timeline* is safe as background narrative. The
**US$133 million figure and the founders' names should not be stated as verified fact** without
a primary source. Carousel 02 slide 5 deliberately omits the figure for this reason.

### F3. IDS maturity and adoption `[VERIFY]`

Information Delivery Specification is referenced in `level-3-advanced.md` L3.10 as a
buildingSMART standard for machine-checkable information requirements. The general description
is sound, but **the current version number and adoption status were not verified** in this
research session.

**Action:** confirm against buildingSMART technical pages before making any claim about IDS
maturity, tool support, or version.

### F4. ISO 19650-4 publication year `[LOW CONFIDENCE]`

`level-3-advanced.md` L3.01 lists ISO 19650-4 (information exchange) as 2022. **This year was
not independently confirmed** in the research session — the search results confirmed Part 4
exists and covers information exchange, but not its publication year.

**Action:** confirm on iso.org before publishing the parts table, or state the parts without
years.

### F5. Revit keyboard shortcuts `[INHERENTLY UNVERIFIABLE IN GENERAL]`

Shortcuts listed in the tutorials and tip bank are **commonly-default** shortcuts. They can be
customised, and defaults vary by version and by discipline-specific installation.

**Action, already built into the content:** every shortcut list in this system carries the
instruction to verify via the `KS` dialog. The tip bank's first entry is specifically about
`KS`. **Do not publish a shortcut you have not confirmed in your own install.**

### F6. Anything about the Nigerian or West African BIM market `[OPINION]`

`level-3-advanced.md` L3.20 (BIM in developing markets) is **explicitly labelled professional
opinion**, not research. No adoption statistics, market sizes, or survey data were sourced for
any market.

**Action:** never present this section as research. It is grounded in practice and should be
framed that way — which is also what makes it credible. If a statistic about adoption in a
specific market is ever wanted, it must be sourced separately.

---

## Claims deliberately NOT made

The following circulate widely and are **excluded from this system** because no citation could
be established:

| Excluded claim | Why |
|---|---|
| "BIM saves 20/30/40% on rework" | No traceable study, sample, or year. The number varies by source, which is itself evidence it is folklore. |
| "BIM reduces project duration by X%" | Same |
| "X% of firms now use BIM" | Adoption figures are survey-dependent, region-dependent, and definition-dependent. Any such figure needs its survey named. |
| "Clash detection saves £X per clash" | No traceable source |
| "BIM is mandated in N countries" | buildingSMART publishes a mandates register; cite that document and its year rather than a remembered count. |
| Specific ROI figures of any kind | Standing rule |

This exclusion is **itself content** — Week 6's post is built entirely around it, and the rule
"if I cannot cite it, I do not post it" is a stated position that differentiates the account.

---

## Contested topics, and how they must be presented

| Topic | The disagreement | How to present it |
|---|---|---|
| **6D and 7D BIM** | Some say 6D = FM, 7D = sustainability. Others say the reverse. Both published. | **Always show both.** Never pick one. Cite NBS and Designing Buildings. This is the flagship contested topic. |
| **Whether cost is a "dimension"** | NBS records the argument it is just another information field | Mention as a secondary point, attributed |
| **BIM Levels vs ISO 19650** | Levels are widely used but not in the standard | Teach both: understand the levels, write ISO 19650 |
| **LOD vs Level of Information Need** | LOD is entrenched in practice; LOIN is the standardised approach | Present LOD as superseded but still spoken; explain LOIN as current |
| **openBIM vs closed BIM** | Genuine trade-offs, and strong vendor incentives on both sides | Present the trade-off table. Never advocate. |

---

## Re-verification schedule

| Frequency | What to re-check |
|---|---|
| **Before each publication** | Any claim marked `[VERIFY BEFORE PUBLISHING]` in this log or inline in the knowledge base |
| **Quarterly** | Autodesk product transitions (F1) — this area changes constantly |
| **Quarterly** | ISO 19650 revision status (ISO/DIS 19650-1) — a new edition changes clause references |
| **Annually** | The full sources register — check for superseded standards, new parts, and dead links |
| **On any standards news** | IFC versions, IDS status, new ISO 19650 parts, EN 17412 developments |

**Owner:** Vollmann Akarakiri. This log is not optional infrastructure — the entire positioning
of the account rests on the claim that the content is accurate and sourced. One confidently
stated wrong fact costs more credibility than ten good posts build.

---

## Standing accuracy rules

1. **Never invent a fact.** If it is not in the sources register, it does not get stated.
2. **Never invent a citation.** Attaching a real source to a claim it does not support is worse
   than no citation.
3. **Never quote a statistic you cannot trace** to a study, sample, and year.
4. **Label opinion as opinion.** `[OPINION]` in the knowledge base becomes "in my experience" or
   "my view" in the post.
5. **Present contested topics as contested.** The disagreement is more interesting than either
   side of it.
6. **Distinguish standard from practice from vendor behaviour.** These are three different kinds
   of truth and conflating them is how misinformation spreads in this industry.
7. **Say when you do not know.** It is a credibility asset, not a liability.
8. **Correct publicly and quickly** if something published turns out to be wrong. Edit the post,
   note the correction, update this log.
