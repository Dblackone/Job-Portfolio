# Tutorial 32 — Schedules

**Objective:** build schedules that maintain themselves and can be trusted for measurement.
**Difficulty:** ●● Intermediate
**Estimated time:** 60 minutes
**Prerequisites:** Tutorials 19–22 (Families and Parameters).

---

## The concept first

A schedule is **a view of the model in table form**. It is not a spreadsheet you fill in.

- Add a door to the model and a row appears.
- Edit a cell and **you edit the element in the model**.
- Anything you can schedule, you can count, filter, sort, group and total.

That bidirectionality surprises everyone the first time, and it is the reason schedules are
useful rather than decorative.

---

## Step-by-step

**1. View tab → Schedules → Schedule/Quantities.**

**2. Choose a category** — Doors, Windows, Walls, Rooms. Then name the schedule to convention.

**3. Fields tab — add only what the schedule must answer.** If you cannot say why a field is
there, remove it. A schedule with thirty columns is a schedule nobody reads.

**4. Add a calculated value if you need one.** Fields tab → Calculated Value. Give it a name, a
type (Number, Length, Area, Formula), and the formula. Field names in formulas are
case-sensitive and must match exactly.

**5. Filter tab — restrict the rows.** For example `Level` `equals` `Level 1`. Filters are what
make one schedule serve one drawing rather than one schedule serving everything badly.

**6. Sorting/Grouping tab.** Sort by a field, then:

| Option | Effect |
|---|---|
| **Header** | A heading row per group |
| **Footer** | A subtotal row per group |
| **Blank line** | Visual separation |
| **Grand totals** | A total row for the whole schedule |
| **Itemise every instance** | Untick to collapse identical rows into a count |

Unticking **Itemise every instance** is how you turn a list of 240 doors into a summary of 6
door types with quantities.

**7. Formatting tab.** Set the heading text, alignment, and field formatting. Tick **Calculate
totals** for any numeric field you want summed.

**8. Appearance tab.** Grid lines, outline, blank row before data, header and body text styles.
Set these in the project template so every schedule matches.

**9. Place it on a sheet.** Drag from the Project Browser onto a sheet, the same way as any other
view. A schedule too long for one sheet can be split — drag the break handle at the bottom, then
move the second segment.

**10. Test bidirectionality.** Change a value in a cell. Go and look at the element. It changed.

---

## Special schedule types

| Type | Purpose |
|---|---|
| **Material Takeoff** | Quantities by material layer rather than by element. Requires correctly layered types. |
| **Sheet List** | A schedule of sheets — the drawing register, generated rather than typed |
| **Note Block** | Schedules annotation symbols, used for general notes and keynotes |
| **View List** | A schedule of views. Excellent for auditing view naming and template assignment. |
| **Key Schedule** | Define a set of values once, then apply the key to many elements |

`[Professional judgement]` The **View List** is one of the most useful and least used views in
Revit. It shows every view with its name, template, scale, phase and discipline in one table,
and it turns view-standard auditing from an inspection into a five-minute read.

---

## Tips

- **Place schedules on sheets at the start of the project, not the end.** A visibly empty
  schedule is a running to-do list that everyone can see.
- **Untick "Itemise every instance"** for summary schedules.
- **Filter, do not delete.** If a schedule shows too much, filter it. Never work around it by
  changing the model.
- **Use a schedule to fix data in bulk.** It is often the fastest way to populate a parameter
  across hundreds of elements — much faster than selecting them in a view.
- **Schedule what is missing.** Filter on `has no value` to list every element lacking a
  required parameter. Combined with a red view filter (Tutorial 26–27), this is a complete
  model-audit workflow.

---

## Common mistakes

| Mistake | What goes wrong |
|---|---|
| Typing data into a schedule the model should know | The typed value is now the only place that information exists |
| Thirty-column schedules | Nobody reads them and they never get checked |
| Not unticking "Itemise every instance" | A 240-row list where a 6-row summary was wanted |
| Case-mismatched field names in formulas | The formula fails with a message that does not explain why |
| Scheduling walls that are single generic layers | Material takeoff returns nothing useful |
| Trusting quantities from an incompletely modelled area | Un-modelled means un-measured, and the schedule will not warn you |
| Appearance set per schedule | The drawing set looks inconsistent |

---

## Professional workflow

Schedules are set up **in the project template** — door schedule, window schedule, room schedule,
sheet list, view list — with correct fields, formatting and appearance already defined.

On the project, they are placed on sheets during the first week. From then on they act as live
quality control: an empty cell in a schedule on a sheet is visible to the whole team, and gets
fixed. A missing parameter buried in the model does not.

`[Professional judgement — measurement]` Be honest about what a schedule is. It gives you
**quantities**, accurate to the accuracy of the modelling. It does not give you a priced bill of
quantities — rates, waste, labour, plant, preliminaries and standard methods of measurement are
not in the model. Anything not modelled is not measured, and the schedule will not tell you that
either. Saying this plainly to a client builds more trust than promising a BOQ the model cannot
produce.

---

## Shortcuts used

*Verify against your install with `KS`.*

Schedules have few default shortcuts. Access is via View tab → Schedules.

| Shortcut | Action |
|---|---|
| `VG` | Visibility/Graphics (schedules respect view filters via the model, not directly) |
| `KS` | Keyboard Shortcuts dialog |

---

## Content hooks from this tutorial

- "A schedule is a view, not a spreadsheet. Edit a cell and you edit the model."
  — Week 24 Monday post
- "Put your schedules on sheets in week one. An empty schedule is a to-do list everyone can see."
  — Week 24 Friday post
- "Filter on 'has no value' to find every element missing a parameter." — Model Health Tip
- "The View List is the most useful view in Revit that nobody opens." — Did You Know
- "The model gives you quantities. It does not give you a bill of quantities."
  — Week 19 Friday post
