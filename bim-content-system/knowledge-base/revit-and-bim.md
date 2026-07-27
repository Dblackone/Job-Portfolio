# Revit and BIM — The Relationship, Properly Explained

The most misunderstood relationship in the industry, and the topic most likely to establish
authority quickly because so much published content gets it wrong.

---

## 1. Why Revit is a BIM authoring software

`[VENDOR]` Autodesk describes Revit as hosting *the information that forms the model from which
drawings and documents are derived*, with parametric design tools supporting optioneering and
optimisation from concept through shop drawings.
(Source: https://www.autodesk.com/solutions/revit-vs-autocad)

Four properties make it an authoring tool rather than a drafting tool:

1. **Objects, not geometry.** A wall in Revit is a wall — an instance of a type, carrying
   material layers, fire rating, acoustic performance, cost, and classification.
2. **A single project database.** Every plan, section, elevation, 3D view, schedule, and sheet
   is a **view** of one dataset. There is no second copy to keep in sync.
3. **Parametric relationships.** Elements reference levels, grids, hosts, and each other.
   Change the datum and dependent geometry follows.
4. **Bidirectional information.** Editing a schedule cell edits the element. Tagging reads live
   parameter values. Information cannot silently diverge from the model.

**Authoring** is the key word. Revit is where information is *created*. It is one role among
several — review (Navisworks), coordination and common data environment (Autodesk Construction
Cloud and equivalents), analysis, estimating, and facility management are separate roles served
by separate tools.

---

## 2. Revit vs AutoCAD

`[VENDOR]` Autodesk's own framing: CAD uses a drafting tool to create *lines and arcs to
represent* a design; the BIM approach uses *actual elements to represent real-world components*
— three-dimensional, with parameters programmed into them.
(Sources: https://www.autodesk.com/solutions/revit-vs-autocad,
https://knowledge.autodesk.com/support/revit/learn-explore/caas/video/youtube/lesson/143344-courseId-100332.html)

| | AutoCAD | Revit |
|---|---|---|
| **Core unit** | Line, arc, polyline, block | Building element (wall, door, floor, system) |
| **Data model** | Drawing file | Project database |
| **Views** | Separate drawings you maintain | Live views of one model |
| **Coordination between views** | Manual | Automatic |
| **Quantities** | Counted or estimated | Scheduled from elements |
| **Change propagation** | You update every affected drawing | Update once |
| **Strength** | Total geometric freedom; fast 2D detailing | Coordinated multi-view documentation with information |
| **Weakness** | No inherent information; drift between views | Constrained; requires you to declare what things are |

`[OPINION]` **AutoCAD is not obsolete and saying so damages your credibility.** It remains
excellent for 2D detailing, site drawings, schematic layouts, survey drawings, fabrication
details, and any situation where geometric freedom beats structured information. Most real
practices run both. The professional position is *the right tool for the information required*,
not tribal loyalty.

`[OPINION]` The sentence that lands with beginners: **AutoCAD draws what a building looks like.
Revit describes what a building is.**

---

## 3. What Revit can do

- Author coordinated architectural, structural, and MEP models in one environment
- Produce a full construction documentation set from the model — plans, sections, elevations,
  details, schedules, sheets
- Schedule and quantify anything modelled — counts, areas, volumes, material takeoffs
- Support multi-user working through worksharing (central and local models, worksets)
- Link and coordinate with other discipline models, CAD files, point clouds, and topography
- Monitor another discipline's datums for change via Copy/Monitor
- Manage phasing (existing, demolition, new) and design options
- Carry classification and custom information through project, shared, and global parameters
- Export to open exchange formats including IFC, and to Navisworks for federation and clash review
- Be extended and automated through Dynamo and the Revit API
- Produce visualisation output and support analysis workflows through export to specialist tools

---

## 4. What Revit cannot do — the honest list

`[OPINION]` This section builds more credibility than any other content in the system, because
almost nobody publishes it.

1. **Revit is not a common data environment.** It has no information container states, no
   suitability codes, no approval workflow, no audit trail across organisations. Worksharing is
   not a CDE.
2. **Revit does not do BIM for you.** It will happily let you produce an uncoordinated,
   unclassified, unnamed model that meets no information requirement.
3. **Revit does not price anything.** It gives quantities. Rates, waste, labour, plant,
   preliminaries, and standard methods of measurement are not in the model. (See L2.18.)
4. **Revit is not a clash detection tool at project scale.** Interference Check exists and is
   useful within one model; federated multi-discipline clash management is Navisworks or an
   equivalent.
5. **Revit is not a scheduling tool.** 4D sequencing requires linking model elements to a
   programme in another tool.
6. **Revit is weak on complex freeform geometry** compared with dedicated surface modellers. It
   is a building modeller, not a NURBS modeller.
7. **Revit is not a rendering engine of last resort.** Presentation-grade visualisation
   generally goes to specialist tools.
8. **Revit is not a facility management system.** The AIM lives in an asset management platform;
   Revit contributes information to it.
9. **Revit does not guarantee code compliance.** It has no knowledge of building regulations.
10. **Revit does not enforce standards.** Templates, conventions, and QA processes do.
11. **Revit does not fix a bad process.** A firm with no standards that buys Revit gets faster,
    more expensive chaos.
12. **Revit models do not open backwards.** A model saved in a newer version cannot be opened in
    an older one. This has real contractual consequences and must be agreed in the BEP.

---

## 5. Where Revit sits in the BIM workflow

```
REQUIREMENTS            EIR / AIR                      (client, information manager)
      ↓
PLANNING                BEP, MIDP, TIDP                (lead appointed party)
      ↓
AUTHORING          ►►►  REVIT  ◄◄◄                     (each discipline, in its own model)
      ↓
EXCHANGE                IFC / native / data exchanges
      ↓
FEDERATION              Navisworks / ACC / equivalent  (coordination)
      ↓
REVIEW                  clash detection, issue management
      ↓
DOCUMENTATION      ►►►  REVIT  ◄◄◄                     (sheets issued to the CDE)
      ↓
CDE                     WIP → Shared → Published → Archived
      ↓
CONSTRUCTION            sequencing, quantities, site queries
      ↓
HANDOVER                COBie / structured asset data
      ↓
OPERATION               AIM in an asset management platform
```

`[OPINION]` Revit appears twice and is absent from most of the diagram. That is the point:
**Revit is where information is created, not where BIM happens.** BIM happens across the whole
chain. This diagram is the basis of one of the strongest carousels in the system.

---

## 6. Eight misconceptions about Revit and BIM

| # | Misconception | Correction |
|---|---|---|
| 1 | "Revit is BIM" | Revit is a BIM authoring tool. BIM is the information management process it serves. (ISO 19650) |
| 2 | "If we use Revit, we are doing BIM" | You can produce a fully non-compliant model in Revit. Doing BIM means meeting defined information requirements through a managed process. |
| 3 | "Revit replaced AutoCAD" | They solve different problems. Most practices run both. |
| 4 | "BIM is 3D, Revit is the 3D tool" | BIM is information management. Geometry is one carrier of information. |
| 5 | "Revit gives you the bill of quantities" | Revit gives quantities. Turning quantities into a priced bill is professional work Revit does not do. |
| 6 | "Learning Revit makes you a BIM Manager" | Authoring skill is one competency. A BIM Manager works on requirements, standards, process, coordination, and people. |
| 7 | "Higher LOD is better" | The correct level is the one that meets the level of information need for the decision at hand. Over-modelling is a cost, not a virtue. (EN 17412-1 / ISO 7817-1) |
| 8 | "The Revit model is the deliverable" | The information is the deliverable. The model is one container among several — alongside IFC, COBie, drawings, and schedules. |

---

## 7. How to talk about this in content

`[OPINION]` Three positioning rules that will do more for authority than any amount of
modelling content:

1. **Never be a Revit partisan.** Naming what Revit cannot do makes every claim about what it
   can do more believable.
2. **Always separate tool from process.** Every post that conflates Revit with BIM trains the
   audience to conflate them, and then the audience cannot understand anything you say about
   ISO 19650 later.
3. **Teach the workflow diagram early and refer back to it constantly.** It gives the audience
   a mental map, and a map is what turns a series of posts into a course.

---

## Sources

- Autodesk, BIM vs CAD with Revit and AutoCAD — https://www.autodesk.com/solutions/revit-vs-autocad
- Autodesk Knowledge, Understanding the Difference Between BIM and CAD — https://knowledge.autodesk.com/support/revit/learn-explore/caas/video/youtube/lesson/143344-courseId-100332.html
- Autodesk, Compare Revit LT vs AutoCAD LT — https://www.autodesk.com/ca-en/compare/lt-products
- Autodesk, Identify and resolve clash and constructability issues between Revit and Navisworks — https://www.autodesk.com/learn/ondemand/course/identify-and-resolve-clash-and-constructability-issues-between-revit-and
- ISO 19650-1:2018 — https://www.iso.org/standard/68078.html
- NBS, Level of detail and digital plans of work — https://www.thenbs.com/knowledge/level-of-detail-lod-and-digital-plans-of-work
- BIMForum, LOD Specification — https://bimforum.org/resource/lod-level-of-development-lod-specification/

### Revit corporate history `[E — secondary, flagged]`

Commonly reported: Charles River Software was founded in 1997 (Newton, Massachusetts) by Leonid
Raiz and Irwin Jungreis, both previously developers on PTC's Pro/ENGINEER; the company was
renamed Revit Technology Corporation in January 2000; Autodesk acquired it in 2002 for a figure
widely reported as approximately US$133 million. The product name derives from "Revise Instantly".

**These dates and figures come from secondary sources (encyclopaedic and trade), not from an
Autodesk primary source.** They are safe to use as background narrative. Do not present the
acquisition figure as a precise verified fact without an Autodesk or SEC primary source.
See `../research/01-verification-log.md`.
