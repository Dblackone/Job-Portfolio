# Tutorial 12–13 — Doors and Windows

**Objective:** place hosted components that schedule and tag correctly the first time.
**Difficulty:** ● Beginner
**Estimated time:** 30 minutes each
**Prerequisites:** Tutorials 09–11 (Walls).

---

## The concept first

Doors and windows are **hosted** components. They cannot exist without a wall. Delete the wall
and the door goes with it. They cut their own opening — you never model the opening separately.

They are also **loadable families**: external `.rfa` files loaded into the project. If the type
you need is not in the project, you load it rather than building it.

---

## Part A — Doors

### Step-by-step

**1. Open a floor plan.**

**2. Architecture tab → Build panel → Door** (`DR`).

**3. Check what types are available** in the Properties type selector. If nothing suitable is
there, load one: Insert tab → Load Family → navigate to the library → select the `.rfa`.

**4. Hover over a wall.** A door preview appears. Move the cursor across the wall centreline to
flip the swing direction before you click.

**5. Click to place.** Then use the **spacebar** before or after placing to flip the hand, and
the small flip arrows after placing to flip the swing side.

**6. Set the Mark.** Select the door, and in Properties find **Mark**. This is the instance
identifier the door tag reads. Revit auto-numbers it, but on a real project the numbering should
follow the firm's convention.

**7. Duplicate a type to make a size you need.** Properties → Edit Type → Duplicate → name it
(for example `SGL-FLUSH-900x2100`) → set Width and Height. **Never edit a type without
duplicating**, or every door of that type changes.

**8. Populate the type parameters that matter.** Fire rating. Acoustic rating. Finish. Frame
material. These are the parameters your schedule and your specification will read. Empty
parameters mean blank schedule cells and blank tags.

**9. Tag it.** Annotate tab → Tag by Category (`TG`), then click the door. If nothing appears,
the tag family is not loaded. Use **Tag All Not Tagged** to tag everything in a view at once.

---

## Part B — Windows

**10. Architecture tab → Build panel → Window** (`WN`).

**11. Place the same way** — hover over a wall, click. Windows are hosted identically to doors.

**12. Set the sill height.** This is an **instance** parameter, found in Properties as "Sill
Height". It is an instance parameter precisely because two windows of the same type can
legitimately sit at different heights.

**13. Check the level constraint.** The window's Level plus Sill Height determine its position.
If windows are at the wrong height, check the level before you check the sill.

---

## Tips

- **Spacebar flips the hand while placing.** Faster than placing and then correcting.
- **Place doors and windows in plan, then check them in a 3D view.** Sill heights and swing
  directions are hard to verify in plan alone.
- **Tag All Not Tagged** (Annotate tab) tags every untagged element of a category in the view in
  one operation.
- **A blank tag means a blank parameter.** Check the element before you blame the tag. This is
  true for every tag in Revit, without exception.
- **Load a small, deliberate family library.** Loading two hundred speculative families bloats
  the project and slows every operation.

---

## Common mistakes

| Mistake | What goes wrong |
|---|---|
| Editing a door type instead of duplicating | Every door of that type in the project changes |
| Leaving fire rating and acoustic rating empty | The schedule is blank and the specification cannot be produced |
| Modelling a wall opening for something that should be a door | No information, no schedule row, no tag |
| Assuming a blank tag is broken | It is reading an empty parameter — fix the model |
| Leaving auto-generated Mark values | Door numbering does not follow the drawing convention and has to be redone |
| Loading huge quantities of unused families | File bloat and slow operations |
| Placing windows without checking sill height in 3D | A row of windows at inconsistent heights, discovered at elevation stage |

---

## Professional workflow

On a real project:

1. The **family library is curated** before the project starts — a small set of correct,
   consistently-parameterised families.
2. **Types are created and named to convention** at the start, not improvised per door.
3. **Parameters that the specification and the schedule need are identified up front**, and if
   any of them need to be both tagged and scheduled, they are set up as **shared parameters**.
4. Door and window schedules are placed on sheets **early**, while they are still mostly empty.
   A visibly empty schedule is a running to-do list, and it is far more effective than a
   checklist nobody opens.

`[Professional judgement]` Placing your schedules on sheets at the start of a project, not the
end, is one of the highest-value habits in Revit. It converts documentation from a task at the
end into continuous feedback throughout.

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `DR` | Door |
| `WN` | Window |
| `TG` | Tag by Category |
| `CS` | Create Similar |
| `MA` | Match Type Properties |
| `Spacebar` | Flip hand while placing |

---

## Content hooks from this tutorial

- "A blank tag means a blank parameter. Check the model, not the tag." — Wednesday quick tip
- "Delete the wall, lose the door. That is what hosted means." — Did You Know
- "Put your schedules on sheets at the start of the project, not the end." — Best Practice post
- "Empty fire rating fields are why your door schedule is useless." — Common Mistake post
