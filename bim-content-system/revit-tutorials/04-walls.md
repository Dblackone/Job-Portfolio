# Tutorial 09–11 — Walls: Drawing, Editing, and Compound Structures

**Objective:** build walls that are correct in geometry, correct in information, and measurable.
**Difficulty:** ● Beginner (drawing) · ●● Intermediate (editing and structures)
**Estimated time:** 60 + 45 + 45 minutes
**Prerequisites:** Tutorials 02–07.

---

## Part A — Drawing walls

### Step-by-step

**1. Open a floor plan** for the level you are building.

**2. Architecture tab → Build panel → Wall** (`WA`).

**3. Choose a type** from the Properties palette type selector. Do not accept whatever is
loaded — pick deliberately, or duplicate and make the type you need.

**4. Set the Options Bar before you draw.** Four settings, all of which matter:

| Setting | What it does |
|---|---|
| **Height / Depth** | Whether the wall goes up or down from the current level |
| **Top constraint** | Unconnected height, or attached to a level. **Attach to a level.** |
| **Location Line** | Which plane of the wall sits on the line you draw |
| **Chain** | Continuous drawing |

**5. Understand the Location Line.** This is the single most consequential wall setting and the
one most beginners never look at.

| Option | The line you draw is at |
|---|---|
| Wall Centreline | The centre of the whole wall |
| Core Centreline | The centre of the structural core only |
| Finish Face: Exterior | The outer finished face |
| Finish Face: Interior | The inner finished face |
| Core Face: Exterior | The outer face of the structural core |
| Core Face: Interior | The inner face of the structural core |

Walls that look right but measure wrong are almost always a location line problem. On a grid,
structural walls are usually drawn to **Core Centreline** or a core face so the structure aligns
with the grid regardless of finishes.

**6. Draw the walls.** Click a start point, click subsequent points, press `Esc` twice to finish.

**7. Set the top constraint properly.** Select the wall, and in Properties set Top Constraint to
"Up to level: [next level]" rather than leaving an unconnected height. A wall attached to a
level moves when the level moves. A wall with an unconnected height does not, and will be wrong
the moment the floor-to-floor height changes.

---

## Part B — Editing walls

**8. Edit profile.** Select a wall → Modify tab → Edit Profile. Choose an elevation view when
prompted. Sketch the shape you want. Use this for gable ends, sloped tops, and stepped bases.

**9. Attach top or base.** Select a wall → Modify tab → Attach Top/Base → pick a roof, floor or
ceiling. The wall now follows that element. This is nearly always better than editing a profile
manually, because it stays correct when the roof changes.

**10. Wall openings.** For a plain rectangular hole: Architecture tab → Opening → Wall. For
anything a door or window family exists for, use the family — it carries information the opening
does not.

**11. Wall joins.** Modify tab → Geometry panel → Wall Joins. Cycle through butt, mitre and
square-off. Use this when a corner displays incorrectly rather than moving the walls.

**12. Split and trim.** `SL` to split, `TR` to trim/extend. `AL` to align to a reference and then
lock with the padlock so the relationship is maintained.

---

## Part C — Compound wall structures

**13. Duplicate before editing.** Select a wall → Properties → Edit Type → **Duplicate**. Name
it to convention. **Never edit a wall type without duplicating first** — you will change every
instance in the project.

**14. Edit Structure.** In Type Properties → Structure → Edit. You now see the layer table.

**15. Build the layers.** Each row is a layer with a function, a material, and a thickness.

| Function | Use for |
|---|---|
| **Structure [1]** | The load-bearing core |
| **Substrate [2]** | Sheathing, backing boards |
| **Thermal/Air Layer [3]** | Insulation and cavities |
| **Finish 1 [4]** | Exterior finish |
| **Finish 2 [5]** | Interior finish |
| **Membrane Layer** | Zero-thickness membranes |

**16. Set the core boundaries.** The two "Core Boundary" rows define which layers count as the
structural core. This determines what Core Centreline and Core Face location lines refer to, and
what room boundaries measure to.

**17. Assign real materials.** Each layer gets a material with a cut pattern and a surface
pattern. This is what makes details legible and material takeoffs possible.

**18. Name the type properly.** Something like `EXT-200-Blockwork-Rendered` — readable, sortable,
and meaningful to someone who is not you.

---

## Tips

- **Attach walls to levels, not to a height.** They then follow level changes automatically.
- **Attach to roof rather than editing profile.** The attachment updates when the roof changes;
  the sketched profile does not.
- **Use `MA` (Match Type Properties)** to change a wall to match another wall you click.
- **`TL` (Thin Lines)** when checking alignment at low zoom — line weights hide small errors.
- **Duplicate, then edit. Always.** Say it out loud until it is a reflex.

---

## Common mistakes

| Mistake | What it costs |
|---|---|
| Editing a wall type without duplicating | Every wall of that type in the project changes |
| Ignoring the location line | Walls look right and measure wrong; grid alignment fails |
| Unconnected height instead of a level constraint | Walls do not follow when levels move |
| Single-layer generic walls | No material takeoff, no meaningful details, unhappy cost consultant |
| Modelling openings manually where a family exists | The opening carries no schedulable information |
| Moving walls to fix a corner | The join was the problem; use Wall Joins |
| Type names like "Wall 1" | Nobody, including future you, knows what it is |

---

## Professional workflow

Walls are set up **in the project template**, not per project. The firm's standard wall types —
correctly layered, correctly named, with real materials and correct core boundaries — exist
before the project starts.

On the project, you select from those types. If a project needs a new type, it is created by
duplicating the closest standard type, named to convention, and then reviewed for inclusion in
the template after the project completes.

`[Professional judgement]` The layer structure *is* the information. A wall modelled as a single
generic layer is geometry pretending to be BIM. It looks identical in a render and is worthless
in a takeoff.

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `WA` | Wall |
| `MA` | Match Type Properties |
| `AL` | Align |
| `TR` | Trim/Extend |
| `SL` | Split Element |
| `OF` | Offset |
| `MM` | Mirror — Pick Axis |
| `DM` | Mirror — Draw Axis |
| `TL` | Thin Lines |
| `CS` | Create Similar |

---

## Content hooks from this tutorial

- "Walls that look right but measure wrong are a location line problem." — Week 18 Wednesday tip
- "Duplicate before you edit. Otherwise you just changed 400 walls." — Common Mistake post
- "Attach walls to levels, not heights." — Best Practice post
- "A single-layer wall is geometry pretending to be BIM." — Week 19 Friday post
