# Tutorial 06–07 — Levels and Grids

**Objective:** build the skeleton every other element in the project will reference.
**Difficulty:** ● Beginner
**Estimated time:** 30 minutes each
**Prerequisites:** Tutorials 02–05.

---

## Why this comes first

Levels host floors, ceilings, roofs and most components. Grids are the shared coordinate
language between architecture and structure. Elements attached to a level move with it — that is
the whole point, and it is why placing levels late means moving everything twice.

---

## Part A — Levels

### Step-by-step

**1. Open an elevation view.** Project Browser → Elevations → South.

**Levels can only be created in elevation or section views.** Not in plan. Every beginner
learns this exactly once, usually after several minutes of confusion.

**2. Architecture tab → Datum panel → Level** (`LL`).

**3. Draw the level** by clicking a start and end point, or use **Pick Lines** with an offset
from an existing level — faster and more accurate when you know the floor-to-floor height.

**4. Name it immediately.** Click the level name and type. Use your firm's convention. If you
have none: `L00 Ground`, `L01 First`, `L02 Second`. Consistent, sortable, unambiguous.

**5. Set the elevation.** Click the elevation value and type the exact height. Do not drag levels
into position — type the number.

**6. Check that a plan view was created.** New levels drawn with the Level tool create associated
plan views. Levels created by **copying** an existing level do **not**. If your new level has no
plan view: View tab → Plan Views → Floor Plan → select the level.

**7. Control the extents.** Drag the endpoint circles to set how far the level line runs. Use the
padlock to lock levels so they resize together. Use the 2D/3D toggle to change the extent in one
view only rather than everywhere.

### Part B — Grids

**8. Open a plan view.** Grids are created in plan, the opposite of levels.

**9. Architecture tab → Datum panel → Grid** (`GR`).

**10. Draw the first grid line.** Name it `1` or `A` depending on your convention. Revit
auto-increments from there, which is why the first name matters.

**11. Copy rather than redraw.** Select the grid, `CO` to copy, and type the spacing. Copying
preserves alignment and inherits the naming sequence.

**12. Standard convention:** numbers in one direction, letters in the other. Follow whatever the
structural engineer is using — you are the one who should adapt.

**13. Lock grids once established.** Select all grids and `PN` to pin them. Nothing is more
disruptive than a grid moved accidentally three months in.

**14. Set 3D extents properly.** Grids have per-view (2D) and project-wide (3D) extents. Set the
3D extent so grids appear at every level, then adjust 2D extents per view for graphic clarity.

---

## Tips

- **Type the elevation, never drag it.** Dragging gives you 3,247 mm when you wanted 3,250 mm,
  and you will not notice for weeks.
- **Name levels and grids before you make any more.** Renaming later is possible; renaming later
  when 400 elements reference them is a different experience.
- **Pin your datums.** `PN`. It costs nothing.
- **On a multi-discipline project, one discipline authors datums** — usually structural — and
  everyone else uses **Copy/Monitor**. Two disciplines authoring grids guarantees divergence.

---

## Common mistakes

| Mistake | What goes wrong |
|---|---|
| Trying to create levels in plan view | The tool is unavailable and you assume something is broken |
| Copying a level instead of drawing one | No associated plan view is created |
| Dragging levels to position | Non-round elevations that break dimension strings |
| Not naming datums immediately | You end up with Level 3, Level 4, Level 7 and no Level 5 |
| Leaving grids unpinned | Someone moves one, and every element referencing it follows |
| Both architect and engineer authoring grids | They drift, and nobody notices until federation |
| Setting only 2D extents | Grids appear in one view and not the next, and it looks like a bug |

---

## Professional workflow

On a coordinated project:

1. The **structural engineer** publishes levels and grids in their model.
2. Every other discipline **links** that model and uses **Copy/Monitor** (Collaborate tab →
   Copy/Monitor → Select Link) to copy levels and grids into their own model.
3. When the engineer moves Grid C, everyone else gets a **coordination review warning** rather
   than discovering the change three weeks later in a section.

That monitoring relationship is the value. The copying is incidental.

`[Professional judgement]` The decision about who authors datums should be made in the BEP
before anyone models anything. It takes one sentence and prevents one of the most expensive
coordination failures there is.

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `LL` | Level |
| `GR` | Grid |
| `CO` / `CC` | Copy |
| `PN` | Pin |
| `UP` | Unpin |
| `AL` | Align |
| `DI` | Aligned dimension |

---

## Content hooks from this tutorial

- "Levels are made in elevation, not plan. Every beginner learns this exactly once."
  — Wednesday quick tip
- "Type the elevation. Never drag it." — Wednesday quick tip
- "Who should own grids on a multi-discipline project?" — Week 17 Friday post
- "Copy a level and you get no plan view. Draw one and you do." — Did You Know
