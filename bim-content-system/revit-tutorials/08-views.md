# Tutorial 24–25 — Views: Plans, Sections, Elevations and 3D

**Objective:** create and control views, and understand why something is missing from one.
**Difficulty:** ● Beginner
**Estimated time:** 45 + 30 minutes
**Prerequisites:** Tutorials 02–16.

---

## The concept first

A view is a **live window onto the model**, not a drawing. Nothing in it is drawn — it is
revealed, according to settings you control. Every troubleshooting problem in this tutorial
follows from that one fact.

---

## Step-by-step

### Creating views

**1. Floor plans.** View tab → Plan Views → Floor Plan → select a level. Only levels that do
not already have a plan appear in the list.

**2. Sections.** View tab → Section. Click a start and end point. Drag the depth arrow to set how
far the section looks. Double-click the section head to open the view, or find it in the Project
Browser.

**3. Elevations.** View tab → Elevation. Click near a wall — Revit orients it automatically.
The elevation marker has four tick boxes; tick each to add a direction.

**4. Callouts.** View tab → Callout. Draw a box in an existing view to create a detail view of
that region at a larger scale.

**5. 3D views.** The default 3D view is on the Quick Access Toolbar. Right-click the ViewCube →
Orient to View → to match a section or elevation.

**6. Section boxes.** In a 3D view: Properties → tick **Section Box**. Then drag its faces to cut
into the model. This is the fastest way to explain a spatial problem to somebody else and it is
underused.

**7. Duplicate views.** Right-click a view in the Project Browser:

| Option | Copies |
|---|---|
| **Duplicate** | The view only — no annotation |
| **Duplicate with Detailing** | The view plus its annotation |
| **Duplicate as Dependent** | A linked child view, used for splitting a large floor across sheets |

**8. Rename immediately.** "Copy of Level 1" is how a project becomes unnavigable. Rename on
creation, to convention.

---

### View range — the setting that hides your work

**9. Open view properties** (click empty space, look at the Properties palette) → **View Range**
→ Edit.

**10. Understand the four planes:**

| Plane | What it does |
|---|---|
| **Top** | The upper limit of what the view shows |
| **Cut Plane** | The height at which the model is cut. Elements here show as cut. |
| **Bottom** | The lower limit of the primary range |
| **View Depth** | How far below the bottom the view still shows elements, drawn as beyond |

**11. Test it.** Set the cut plane to 1200 mm and note which windows show as cut. Set it to
2400 mm and watch them change. This is the mechanism behind most "it disappeared" problems.

---

### The diagnostic order

When something is missing from a view, check in this exact order:

| # | Check | How |
|---|---|---|
| 1 | **View range** | View properties → View Range |
| 2 | **Temporary hide/isolate** | A cyan border on the view. `HR` to reset. |
| 3 | **Visibility/Graphics** | `VG` — is the category ticked? |
| 4 | **Filters** | `VG` → Filters tab — this one catches everyone |
| 5 | **Worksets** | Is the workset loaded and visible? |
| 6 | **Phase and phase filter** | View properties |
| 7 | **Design options** | View properties |
| 8 | **Discipline** | View properties — a view set to Structural hides architectural elements |
| 9 | **Crop region** | Is it cropping the element out? |
| 10 | **Scope box** | Is the element outside it? |

**Deleted is last on the list, not first.**

---

## Tips

- **`WT`** to tile a plan and a 3D view side by side while modelling.
- **Section box in 3D** is the fastest tool for explaining a coordination problem.
- **Duplicate as Dependent** for large floors split across multiple sheets — the parent view
  controls the settings for all children.
- **`TL`** (Thin Lines) when checking alignment at low zoom.
- **Name views on creation.** It takes two seconds and saves hours later.

---

## Common mistakes

| Mistake | What goes wrong |
|---|---|
| Assuming missing means deleted | Time lost, and occasionally elements re-modelled that already existed |
| Never opening View Range | You fight a symptom for months |
| Leaving "Copy of Copy of Level 1" names | The project becomes unnavigable for everyone else |
| Adjusting a single view instead of the template | The fix does not propagate and the set drifts |
| Using Duplicate when Duplicate with Detailing was needed | Annotation lost, and re-done by hand |
| Ignoring the cyan border | Elements stay hidden and everyone assumes the model is broken |
| Leaving a view's discipline wrong | Whole categories vanish for reasons that look like a bug |

---

## Professional workflow

Views are created **from view templates**, named to convention, and placed on sheets early.

The professional habit that matters most here: when a view looks wrong, the first question is
never "what happened to the model?" It is **"what is this view set to?"** Fixing a view fixes a
view. Fixing the model fixes every view. Knowing which problem you have saves the most time of
any single skill in Revit.

`[Professional judgement]` Teaching the ten-step diagnostic order to a junior on their first day
saves them, conservatively, several days over their first year. It is the highest-return five
minutes in Revit training.

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `VG` / `VV` | Visibility/Graphics |
| `HH` | Hide element (temporary) |
| `HC` | Hide category (temporary) |
| `HI` | Isolate element (temporary) |
| `IC` | Isolate category (temporary) |
| `HR` | Reset temporary hide/isolate |
| `EH` | Hide element in view (permanent) |
| `VH` | Hide category in view (permanent) |
| `ZF` | Zoom to fit |
| `WT` | Tile windows |
| `TL` | Thin lines |

---

## Content hooks from this tutorial

- The ten-step diagnostic order — Week 15 Friday post and a TikTok script
- "A cyan border means someone hid something and forgot. HR resets it." — Wednesday quick tip
- "View range is not a setting. It is the reason your work disappeared." — Week 16 carousel
- "Deleted is last on the diagnostic list, not first." — Common Mistake post
