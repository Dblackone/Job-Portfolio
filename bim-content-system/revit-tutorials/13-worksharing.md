# Tutorial 39–40 — Worksharing, Central Models and Worksets

**Objective:** work in one Revit project alongside other people without blocking them or losing
work.
**Difficulty:** ●●● Advanced
**Estimated time:** 90 + 60 minutes
**Prerequisites:** Tutorials 36–38 (Links).

---

## The concept first

| Term | Meaning |
|---|---|
| **Central model** | The master file. Nobody works in it directly. |
| **Local model** | Your own copy on your machine. You work here. |
| **Synchronise with Central (SWC)** | Push your changes up, pull everyone else's down |
| **Workset** | A named collection of elements, used to manage **ownership and loading** |
| **Borrowing** | Taking temporary ownership of an individual element |

---

## Step-by-step

### Setting up worksharing

**1. Open the project that will become central.** Collaborate tab → Collaborate.

**2. Choose the collaboration method** — in-network (a server path) or in the cloud
(Autodesk Docs / BIM 360). Follow the project's BEP.

**3. Create worksets.** Collaborate tab → Worksets. Revit creates `Workset1` and
`Shared Levels and Grids` by default. Rename `Workset1` — leaving it is a standard sign of an
unmanaged model.

**4. Name worksets to a convention.** A practical structure:

| Workset | Contains |
|---|---|
| `Shared Levels and Grids` | Datums (Revit creates this) |
| `Interior` | Internal walls, doors, partitions |
| `Exterior` | Façade, external walls, roof |
| `Structure` | Structural elements |
| `Site` | Topography, external works |
| `Link_STR` | The structural Revit link |
| `Link_MEP` | The MEP Revit link |
| `Link_CAD_Survey` | The survey DWG |

**One link per workset.** That is what makes selective unloading possible.

**5. Set "Visible in all views" deliberately.** A workset with this unticked is hidden by default
in new views. Useful for links; confusing if applied without thought.

**6. Save the central model** to the agreed network or cloud location.

### Working day to day

**7. Create a local model.** Open Revit → Open → browse to the central → **tick "Create New
Local"** → Open. Revit makes your local copy.

**Never open the central model directly.** If you do, you are editing the master and blocking
everyone.

**8. Set the active workset** before modelling. The workset selector is on the Collaborate tab
and in the status bar. **Elements go onto whatever workset is active when you create them** —
this catches everyone at least once.

**9. Model normally.** Revit borrows elements automatically as you edit them.

**10. Synchronise every 30 to 60 minutes.** Collaborate tab → Synchronize with Central. In the
dialog, tick **Relinquish** for user-created worksets, borrowed elements, family and view
worksets.

**11. Relinquish all before you leave.** Collaborate tab → Synchronize → tick everything, or
Collaborate → Relinquish All Mine. Borrowed elements block your colleagues all night.

**12. Handle "element is owned by" messages properly.** Revit offers to place an editing request.
Do that, then message the person. The request alone sits unnoticed; the message gets it released.

**13. Unload links you are not using.** Manage Links → Unload. On a large project this is often
the single biggest performance improvement available to an individual user.

---

## Tips

- **Recreate your local model regularly** — weekly is reasonable. Local files accumulate problems.
- **Stagger synchronisation.** Everyone syncing at 17:00 creates a queue, and long queues cause
  people to skip syncing, which causes worse problems.
- **Check the active workset before you model.** Make it a reflex, like checking mirrors.
- **Worksets manage ownership and loading, not graphics.** Use view templates and filters for
  appearance.
- **Do not put every category on its own workset.** Ten to fifteen well-chosen worksets beat
  fifty granular ones.

---

## Common mistakes

| Mistake | What goes wrong |
|---|---|
| Opening the central model directly | You block the whole team and risk corrupting the master |
| Not relinquishing before leaving | Colleagues cannot edit borrowed elements overnight |
| Synchronising once a day | Long, painful, conflict-heavy reconciliation |
| Elements on the wrong workset | Selective loading stops working, and coordination gets confusing |
| Leaving `Workset1` named `Workset1` | A reliable indicator that nobody manages this model |
| Using worksets to control graphics | Graphics belong in view templates and filters |
| Fifty granular worksets | Nobody can remember what goes where and everything lands on the wrong one |
| Never recreating the local | Local file problems accumulate and eventually cost a day |
| Placing an editing request and saying nothing | It goes unnoticed for hours |

---

## Professional workflow

The worksharing strategy is set out in the **BEP** before anyone opens the model: workset
structure and naming, who creates the central, where it lives, the synchronisation expectation,
the model naming convention, and the audit and backup schedule.

Five rules worth enforcing on every team:

1. Never open the central. Always create a local.
2. Synchronise every 30 to 60 minutes.
3. Relinquish all before you leave.
4. Stagger your syncs.
5. Worksets manage ownership and loading. Never graphics.

`[Professional judgement]` Worksharing decisions are cheapest on day one and brutal in month
four. Restructuring worksets on a live model with five people in it is one of the least pleasant
tasks in Revit, and it is entirely avoidable with thirty minutes of planning at the start.

`[Currency note]` Autodesk Platform Services has announced changes to Revit cloud model downloads
from Autodesk Docs and BIM 360 Docs starting 15 February 2026. If your project uses cloud
worksharing, check the current Autodesk guidance rather than relying on remembered behaviour.
(Source: https://aps.autodesk.com/blog/changes-are-coming-revit-cloud-model-downloads-autodeskbim-360-docs-starting-february-15-2026)

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `VG` / `VV` | Visibility/Graphics (Worksets tab) |
| `PN` | Pin |
| `RW` | Relinquish worksets (verify — not default in all versions) |

Most worksharing operations are on the Collaborate tab rather than mapped to shortcuts.

---

## Content hooks from this tutorial

- The five worksharing rules — Week 30 Friday post and a WhatsApp status series
- "Elements go onto whatever workset is active when you create them." — Common Mistake post
- "Relinquish all before you leave. Borrowed elements block colleagues overnight."
  — Wednesday quick tip
- "A workset still called Workset1 tells you everything about how that model is managed."
  — Did You Know
