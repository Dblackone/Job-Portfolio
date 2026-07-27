# Tutorial 19–22 — Families, Components and Parameters

**Objective:** understand Revit's content system well enough to load, place, modify and build
families, and to choose the right parameter type every time.
**Difficulty:** ● Beginner (concepts, placing) · ●● Intermediate (building, parameters)
**Estimated time:** 45 + 30 + 90 + 60 minutes
**Prerequisites:** Tutorials 09–16.

---

## Part A — Understanding families

### The three kinds

| Kind | Lives | Examples | Edited via |
|---|---|---|---|
| **System family** | Inside the project | Walls, floors, roofs, ceilings, stairs, dimensions, levels | Duplicate the type, Edit Type |
| **Loadable family** | External `.rfa` file | Doors, windows, furniture, fixtures, tags, titleblocks, generic models | Family Editor |
| **In-place family** | Inside the project, unique to it | A one-off feature that exists nowhere else | In-place editor |

### The hierarchy

**Family → Type → Instance.**

- **Family:** "Single-Flush Door" — the `.rfa` file, defining the geometry and the rules.
- **Type:** "900 × 2100" — a named variant with specific parameter values.
- **Instance:** the specific door in the store room.

Getting this hierarchy straight is the prerequisite for understanding parameters, and most
beginner confusion about Revit traces back to it.

---

## Part B — Loading and placing components

**1. Load a family.** Insert tab → Load Family → navigate → select the `.rfa` → Open.

**2. Place it.** Architecture tab → Component → Place a Component (`CM`). Select the type in the
Properties type selector, then click to place.

**3. Understand hosting.** Some families need a host, some do not.

| Host type | Behaviour |
|---|---|
| Wall-hosted | Needs a wall. Deleted with it. |
| Face-hosted | Attaches to any face — flexible, and the usual choice for MEP fixtures |
| Level-hosted | Sits on a level |
| Unhosted | Free-standing. Furniture is usually unhosted. |

**4. Use Create Similar** (`CS`) to place another of whatever you have selected. Faster than
navigating the type selector.

---

## Part C — Building a basic loadable family

Build a simple table. The goal is the workflow, not the object.

**5. File → New → Family.** Choose the right template — this decides the category, and the
category cannot easily be changed later. For a table: `Metric Furniture.rft`.

**6. Draw reference planes first.** Not geometry. Reference planes (`RP`) are the skeleton the
geometry will be constrained to. Draw one for the length and one for the width.

**7. Name the reference planes.** Select each → Properties → Name. Unnamed planes cannot be
selected as work planes later.

**8. Dimension between the reference planes.** Use `DI`. Do this **before** creating geometry.

**9. Label the dimensions to create parameters.** Select the dimension → Options Bar → Label →
Add Parameter. Name it "Table Length". Choose **Type** or **Instance**:

- **Type** — every table of this type is the same length. Correct here.
- **Instance** — each table can differ. Correct for something like a sill height.

**10. Create the geometry.** Create tab → Extrusion. Sketch the tabletop, aligning the sketch
lines to the reference planes and **locking each with the padlock**. The padlock is the whole
technique — without it, the geometry does not follow the parameters.

**11. Set the extrusion height** and finish the sketch.

**12. Flex the family.** This is the critical test. Family Types → change Table Length → Apply.
Does the geometry follow? If not, a lock is missing. **Flex before you ever load a family into a
project** — an unflexed family will break under someone else, at the worst time.

**13. Set the category and parameters.** Create tab → Family Category and Parameters. Confirm
the category is right.

**14. Load into the project.** Create tab → Load into Project.

---

## Part D — Parameters

### The four kinds

| Kind | Scope | Use for |
|---|---|---|
| **Family parameter** | Within one family | Internal dimensions and logic |
| **Project parameter** | Categories within one project | Information needed on this project only |
| **Shared parameter** | Defined in an external `.txt` file | Anything that must be **tagged AND scheduled**, or must stay consistent across projects |
| **Global parameter** | Project-wide value | Driving dimensions and other parameters across the model |

### Type vs instance — the rule that settles it

> **If two elements of the same type could legitimately differ on this value, it must be an
> instance parameter.**

A door's width: type. A window's sill height: instance. A wall's fire rating: type. A room's
occupancy: instance.

### The shared parameter rule

> **If a value must appear in both a tag and a schedule, it must be a shared parameter.**

This single fact resolves a large share of all "why can't I tag this?" questions in Revit.

**Setting one up:** Manage tab → Shared Parameters → Create/Browse a `.txt` file → create a
group → create the parameter. Then add it to the project via Project Parameters, or into a
family via Family Types → Add → Shared Parameter.

`[Critical]` The shared parameter `.txt` file must be **stored centrally and never regenerated**.
Regenerating it creates new GUIDs, and every parameter that referenced the old file silently
stops matching. This is one of the more painful failures in Revit and it is entirely avoidable.

---

## Tips

- **Reference planes first, geometry second, always.**
- **Lock every sketch line to a reference plane.** Unlocked geometry does not flex.
- **Flex before loading.** Every time, no exceptions.
- **Name reference planes** or you cannot use them as work planes.
- **Start from a similar existing family** rather than from a blank template when you can.
- **Keep the shared parameter file in one place**, backed up, owned by one person.

---

## Common mistakes

| Mistake | What goes wrong |
|---|---|
| Building geometry before reference planes | Nothing flexes and the family has to be rebuilt |
| Not locking sketch lines | Parameters change, geometry does not move |
| Never flexing | The family breaks in someone else's project, under deadline |
| Wrong family template | The category is wrong, so it schedules and tags in the wrong place |
| Using in-place families for repeated elements | File bloat, no reuse, inconsistent scheduling |
| Type where instance was needed | You end up with fifty near-identical types |
| Instance where type was needed | Values drift and become unreliable |
| Regenerating the shared parameter file | New GUIDs, and every existing reference silently breaks |
| Nested families without shared parameters | Nested content cannot be scheduled |

---

## Professional workflow

A firm's family library is **curated, not accumulated**. That means:

- A defined naming convention, applied to every family and type.
- A consistent parameter set across families of the same category.
- One shared parameter file, centrally stored, version-controlled, single owner.
- Every family flexed and reviewed before it enters the library.
- Families kept as simple as their purpose requires — level of information need applies to
  content as much as to models.

`[Professional judgement]` In-place families should be rare. Every one is unreusable content
that bloats the file and schedules inconsistently. If you are making the same in-place element
twice, it should be a loadable family.

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `CM` | Place a Component |
| `CS` | Create Similar |
| `RP` | Reference Plane |
| `DI` | Aligned dimension |
| `AL` | Align |
| `MA` | Match Type Properties |

---

## Content hooks from this tutorial

- "If two elements of the same type could differ on this value, it's an instance parameter."
  — Week 22 Wednesday tip
- "Tag AND schedule means shared parameter. That's the whole answer." — Week 23 Wednesday tip
- "Flex your family before you load it. Every time." — Best Practice post
- "Reference planes first. Geometry second. Always." — Family Tip
- "Never regenerate your shared parameter file." — Did You Know
