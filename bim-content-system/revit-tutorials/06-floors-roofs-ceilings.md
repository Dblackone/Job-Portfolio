# Tutorial 14–16 — Floors, Roofs and Ceilings

**Objective:** build horizontal system families that are correctly layered, correctly hosted, and
correctly related to walls.
**Difficulty:** ● Beginner (floors, ceilings) · ●● Intermediate (roofs)
**Estimated time:** 45 + 60 + 30 minutes
**Prerequisites:** Tutorials 06–11.

---

## Part A — Floors

### Step-by-step

**1. Open the plan for the level the floor belongs to.**

**2. Architecture tab → Build panel → Floor → Floor: Architectural.** You enter sketch mode —
the ribbon changes and the drawing area greys out. This is a mode, and you cannot do anything
else until you finish or cancel it.

**3. Sketch the boundary.** Either draw lines, or use **Pick Walls** to trace wall faces. Pick
Walls is better: it creates a relationship, so the floor updates when the walls move.

**4. The boundary must be a single closed loop.** If Revit refuses to finish the sketch, there is
a gap or an overlap. Use the error dialog's "Show" button to find it.

**5. Finish the sketch** with the green tick.

**6. Answer the join prompt.** Revit asks whether to attach walls that go up to this floor.
Answering yes creates a relationship and is usually correct.

**7. Set the type and the layers.** Edit Type → **Duplicate** → Edit Structure. Same layer table
as walls: function, material, thickness. Screed, insulation, structural slab, finish — each as
its own layer.

**8. Check the Height Offset From Level.** A floor's top surface normally sits at the level, so
the structural slab often needs a negative offset to allow for the finish build-up. Get this
wrong and everything hosted on the floor is out by the finish thickness.

---

## Part B — Roofs

**9. Open the plan for the level the roof springs from.**

**10. Architecture tab → Roof → Roof by Footprint.** Sketch mode again.

**11. Sketch the boundary,** usually with Pick Walls and an overhang value set on the Options Bar.

**12. Set which edges slope.** This is the step that defines the roof form. Select a boundary
line and tick or untick **Defines Slope** on the Options Bar. Set the slope angle in Properties.

| Sloping edges | Result |
|---|---|
| All four | Hipped roof |
| Two opposite | Gable roof |
| One | Mono-pitch |
| None | Flat roof |

**13. Finish the sketch.**

**14. Attach the walls.** Select the walls → Modify tab → Attach Top/Base → pick the roof. The
walls now follow the roof profile and will update if the roof changes. **Do this rather than
editing wall profiles by hand.**

**15. For more complex forms:** Roof by Extrusion (sketch the profile in elevation) or join
multiple roofs with Modify tab → Join/Unjoin Roof.

---

## Part C — Ceilings

**16. Open the ceiling plan** — the reflected ceiling plan for that level, not the floor plan.
This is a different view in the Project Browser and beginners routinely work in the wrong one.

**17. Architecture tab → Build panel → Ceiling** (`CL`).

**18. Use Automatic Ceiling** and click inside a room. Revit finds the bounding walls and creates
the ceiling. If it fails, the room is not enclosed — fix the walls or add room separation lines.

**19. Set the height.** Height Offset From Level in Properties. This is measured from the level,
not from the floor finish.

**20. For a grid ceiling,** pick a type with a grid (for example a 600 × 600 system) and then use
Modify tab → Align (`AL`) to position the grid where you want it, rather than accepting where
Revit put it.

---

## Tips

- **Pick Walls rather than drawing lines.** It creates a relationship. Drawn lines do not update.
- **In sketch mode you are trapped** until you finish or cancel. If the ribbon looks wrong and
  nothing works, check whether you are in a sketch.
- **Use the "Show" button** on sketch errors. It takes you straight to the gap.
- **Check floors and ceilings in section.** Plan view will not reveal a floor that is 50 mm out.
- **Reflected ceiling plan, not floor plan.** Every time.

---

## Common mistakes

| Mistake | What goes wrong |
|---|---|
| Sketch boundary not closed | The floor will not finish and the error message is unhelpful until you use "Show" |
| Drawing lines instead of picking walls | The floor does not follow when walls move |
| Ignoring Height Offset From Level | Everything hosted on the floor is out by the finish thickness |
| Editing wall profiles instead of attaching to roof | The walls do not update when the roof changes |
| Modelling ceilings in the floor plan | You cannot see what you are doing, and placement is guesswork |
| Automatic Ceiling failing and being ignored | The room is not enclosed — which also breaks your area schedules |
| Single-layer floors | No takeoff, no meaningful section detail |
| Overlapping floors between levels | Duplicate volume in quantities, and warnings that never get cleared |

---

## Professional workflow

Floor, roof and ceiling **types live in the project template**, correctly layered and named,
exactly as walls do.

The relationship discipline matters more here than anywhere else in the model:

- Floors **pick walls**, so they follow the plan.
- Walls **attach to roofs**, so they follow the section.
- Ceilings are bounded by **rooms**, so they follow the layout.

A model built with those three relationships in place updates coherently when the design changes.
A model built with sketched lines and manually edited profiles has to be rebuilt every time
something moves — and in early design, something moves every week.

`[Professional judgement]` This is the difference between a model that survives design
development and one that quietly becomes a drawing.

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `CL` | Ceiling |
| `AL` | Align |
| `TR` | Trim/Extend |
| `OF` | Offset |
| `MA` | Match Type Properties |
| `SD` | Shaded visual style |
| `HL` | Hidden Line visual style |

---

## Content hooks from this tutorial

- "Pick Walls, don't draw lines. One creates a relationship, the other creates a shape."
  — Best Practice post
- "Attach walls to the roof. Never edit the profile by hand." — Wednesday quick tip
- "Automatic Ceiling failed? Your room isn't enclosed — and your area schedule is wrong too."
  — Common Mistake post
- "Reflected ceiling plan. Not floor plan." — Quick tip
