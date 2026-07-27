# Glossary

Plain-English definitions. Every term used in any post must be defined here, and defined in the
post the first time it appears.

`[S]` = defined in a published standard · `[P]` = industry practice · `[V]` = vendor-specific

---

## BIM and information management

| Term | Plain-English meaning | Tier |
|---|---|---|
| **AIM** — Asset Information Model | The information model used to operate and maintain the asset after handover | `[S]` ISO 19650 |
| **AIR** — Asset Information Requirements | What the operations team needs to know, stated formally | `[S]` ISO 19650 |
| **Appointed party** | Whoever is delivering information under an appointment (old word: supplier) | `[S]` ISO 19650 |
| **Appointing party** | Whoever is asking for information (old word: employer or client) | `[S]` ISO 19650 |
| **BEP** — BIM Execution Plan | The delivery team's plan for how information will be produced and managed | `[S]` ISO 19650-2 |
| **BIM** — Building Information Modelling | Managing information about a built asset across its whole life | `[S]` ISO 19650-1 |
| **CDE** — Common Data Environment | The agreed single source of project information, with managed states and approvals | `[S]` ISO 19650 |
| **Classification** | A standard code applied to elements so information can be sorted and compared | `[S]` |
| **COBie** | A non-proprietary format for delivering asset data (not geometry) at handover | `[S]` NBIMS-US |
| **Delivery team** | A lead appointed party together with its appointed parties | `[S]` ISO 19650 |
| **Digital twin** | A digital representation **connected to the physical asset by live data** | `[S]` Gemini Principles |
| **EIR** — Exchange Information Requirements | What information an appointment must deliver, in what format, at which milestones | `[S]` ISO 19650 |
| **Federation** | Linking discipline models into a combined view without merging authorship | `[P]` |
| **IDS** — Information Delivery Specification | A machine-readable statement of information requirements, checkable automatically | `[S]` buildingSMART |
| **IFC** — Industry Foundation Classes | The open, vendor-neutral standard for describing built assets (ISO 16739) | `[S]` |
| **Information container** | Any named, versioned set of information in the CDE — a model, drawing, schedule, or document | `[S]` ISO 19650 |
| **Information manager** | The role accountable for the information management function | `[S]` ISO 19650 |
| **ISO 19650** | The international standard series for information management using BIM | `[S]` |
| **Level of Information Need** | How much information is needed, driven by the decision it must support | `[S]` EN 17412-1 / ISO 7817-1 |
| **LOD** — Level of Development | How developed and how *reliable* a model element is at a given stage | `[P]` BIMForum |
| **Level of Detail** | How much geometric detail an element has. **Not the same as LOD.** | `[P]` |
| **MIDP** — Master Information Delivery Plan | All task delivery plans consolidated into the delivery team's schedule | `[S]` ISO 19650-2 |
| **MVD** — Model View Definition | A defined subset of IFC for a specific exchange purpose | `[S]` buildingSMART |
| **openBIM** | Working with open, vendor-neutral standards for exchange | `[S]` buildingSMART |
| **OIR** — Organizational Information Requirements | What an organisation needs to know to run itself | `[S]` ISO 19650 |
| **PIM** — Project Information Model | The information model developed during design and construction | `[S]` ISO 19650 |
| **PIR** — Project Information Requirements | What information this project needs to be delivered successfully | `[S]` ISO 19650 |
| **Point cloud** | Millions of measured 3D points captured by laser scanning or photogrammetry | `[P]` |
| **Scan-to-BIM** | Turning a point cloud of an existing building into a BIM model | `[P]` |
| **Shared coordinates** | An agreed real-world coordinate system so linked models land in the right place | `[V]` |
| **Suitability / status code** | A label saying what an information container may be used for | `[S]` ISO 19650 |
| **TIDP** — Task Information Delivery Plan | What one task team will deliver and when | `[S]` ISO 19650-2 |
| **Uniclass / OmniClass / MasterFormat** | Classification systems used to code construction information | `[P]` |

---

## Coordination and review

| Term | Plain-English meaning | Tier |
|---|---|---|
| **Clash detection** | Automatically checking a federated model for conflicts | `[P]` |
| **Hard clash** | Two elements occupying the same physical space | `[P]` |
| **Soft clash / clearance clash** | An element intruding into a required clearance zone | `[P]` |
| **Workflow clash / 4D clash** | A conflict in time or sequence rather than space | `[P]` |
| **Interference Check** | Revit's built-in clash tool, for use within a single model | `[V]` |
| **Issue** | A recorded problem with an owner and a due date | `[P]` |
| **Model audit** | A structured check of a model's health and compliance | `[P]` |
| **Navisworks** | Autodesk's model review, federation, clash detection and 4D tool | `[V]` |

---

## Revit terms

| Term | Plain-English meaning |
|---|---|
| **Category** | The kind of thing an element is — Walls, Doors, Furniture. Drives visibility and scheduling. |
| **Central model** | The master worksharing file that everyone's local model syncs to |
| **Copy/Monitor** | Copying elements from a link and being warned when the original changes |
| **Design option** | An alternative version of part of the model, coexisting with the main design |
| **Detail component / detail line** | 2D annotation that exists in one view only and carries no model information |
| **Family** | A category of thing in Revit. System, loadable, or in-place. |
| **Family Editor** | The environment where loadable families are built |
| **Global parameter** | A project-wide value that can drive dimensions and other parameters |
| **Grid** | A vertical datum plane — a structural column line |
| **In-place family** | A one-off element modelled directly in the project. Use sparingly. |
| **Instance** | One specific placed element |
| **Instance parameter** | A value that can differ between elements of the same type |
| **Internal origin** | Revit's fixed 0,0,0. Never moves. Model near it. |
| **Level** | A horizontal datum — a floor height. Hosts most elements. |
| **Loadable family** | An external `.rfa` file loaded into a project — doors, windows, furniture, tags |
| **Local model** | Your personal working copy of a central model |
| **Location line** | Which plane of a wall sits on the line you drew |
| **Phase** | Whether an element is existing, demolished, or new |
| **Phase filter** | How a view displays elements from different phases |
| **Project Browser** | The table of contents for every view, sheet, family and group in the project |
| **Project base point** | The project's own reference point for measurement |
| **Project parameter** | A parameter added to categories within one project |
| **Project template (.rte)** | The file firm standards live in — types, styles, view templates, sheets |
| **Purge unused** | Removing unused families, types and materials from a project |
| **Schedule** | A live table view of model elements. Editing it edits the model. |
| **Shared parameter** | A parameter defined in an external file so it can be tagged **and** scheduled |
| **Sheet** | The printable page views are placed on |
| **Survey point** | Where the project sits in real-world coordinates |
| **Synchronise with Central (SWC)** | Pushing your changes up and pulling everyone else's down |
| **System family** | A family that lives inside the project — walls, floors, roofs, ceilings, stairs |
| **Tag** | An annotation that reads a parameter value from an element |
| **Titleblock** | The loadable family providing a sheet's border and metadata fields |
| **Type** | A named variant of a family — "Single-Flush Door, 900 × 2100" |
| **Type parameter** | A value shared by every element of that type |
| **View range** | The invisible cut and depth settings that decide what a plan shows |
| **View template** | A saved set of view settings applied to many views at once |
| **Visibility/Graphics (VG/VV)** | Per-view control of what is shown and how |
| **Warning** | Something Revit could not resolve. Some are harmless; some corrupt data. |
| **Workset** | A named group of elements used to manage ownership and loading |
| **Worksharing** | Multiple people working in one Revit project at the same time |

---

## Automation

| Term | Plain-English meaning |
|---|---|
| **Dynamo** | Visual programming for Revit — build scripts by connecting nodes |
| **Node** | One operation in a Dynamo script |
| **Revit API** | The programming interface used to build Revit add-ins in C#/.NET |
| **Script** | A saved sequence of automated operations |

---

## Terms to use carefully

| Term | Why care is needed |
|---|---|
| **6D / 7D BIM** | The industry does not agree what these mean. Always state the disagreement. (NBS) |
| **BIM Level 2** | Not used in ISO 19650. Explain it as historical UK terminology. (BSI) |
| **Employer's Information Requirements** | Superseded. In ISO 19650, EIR is **Exchange** Information Requirements. |
| **"The BIM"** | Not a thing. Name the information container you actually mean. |
| **"BIM software"** | Prefer "BIM authoring software" — it keeps tool and process separate. |
| **"BIM saves X%"** | Never state without citing the specific study, sample, and year. |
