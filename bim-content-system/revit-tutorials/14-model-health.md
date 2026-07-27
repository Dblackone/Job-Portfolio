# Tutorial 42–45 — Model Cleanup, Audit, Warnings and Organisation

**Objective:** keep a model healthy, fast, and usable by other people, as a routine rather than
a rescue.
**Difficulty:** ●● Intermediate
**Estimated time:** 30 + 30 + 45 + 45 minutes
**Prerequisites:** Tutorials 36–40.

---

## Part A — Model cleanup and purging

**1. Purge Unused.** Manage tab → Purge Unused. Revit lists every unused family, type, material,
group and filter.

**2. Run it more than once.** Purging can make further items unused — an unused family type may
have been the only user of a material. Run it repeatedly until the list is empty or only contains
things you want to keep.

**3. Review before ticking everything.** If your template deliberately carries standard types
that are not yet used on this project, purging removes them. Uncheck those.

**4. Check what is making the file large:**

| Check | How |
|---|---|
| Imported CAD | Manage Links → CAD Formats. Any import (not link) is suspect. |
| In-place families | Schedule them, or filter for them. High counts signal shortcuts. |
| Groups | Large nested groups are a common performance killer |
| Unused views | A View List schedule shows every view not on a sheet |
| Loaded but unused families | Purge Unused |

---

## Part B — Audit and file recovery

**5. Audit on open.** File → Open → tick **Audit** before opening. Revit checks the file for
corruption and repairs what it can.

**6. When to audit:** weekly on a live project, always before issuing to a CDE, and immediately
if the model starts behaving strangely — random crashes, elements that will not select,
inexplicable errors.

**7. Audit takes a long time on a large model.** Schedule it, do not run it under deadline.

**8. If a model is corrupt:** open the most recent good backup. On a worksharing project,
backups are in the `_backup` folder alongside the central. Collaborate tab → Restore Backup.

**9. Save incremental milestone copies.** Not just backups — deliberate, named milestone files at
each issue. Backups roll over; milestones do not.

---

## Part C — Warnings management

**10. Open the warnings list.** Manage tab → Warnings. This is a running record of everything
Revit could not resolve.

**11. Triage rather than clearing blindly.** Not all warnings are equal:

| Priority | Warning | Why it matters |
|---|---|---|
| **Critical** | Duplicate instances in the same place | **Silently doubles your quantities.** The schedule is now wrong and nothing tells you. |
| **Critical** | Elements have duplicate Mark values | Breaks tagging and scheduling |
| **High** | Room not enclosed / room not placed | Breaks area schedules and compliance checks |
| **High** | Elements joined but do not intersect | Performance and geometry errors |
| **Medium** | Wall and room separation line overlap | Area inaccuracy |
| **Medium** | Elements have identical instances | Usually duplicates; check |
| **Low** | Line slightly off axis | Tidy when convenient |

**12. Export the warnings list.** The Warnings dialog has an export button. Export weekly and
track the count over time — **the trend matters more than the number.** A model going from 400
to 900 warnings in one week means something structural went wrong that week, and you can find
out what.

**13. Fix duplicates first.** Always. They are the ones that corrupt information rather than just
displaying badly.

---

## Part D — Model organisation

**14. Browser organisation.** Right-click "Views" in the Project Browser → Browser Organisation
→ New. Group by a parameter — discipline, phase, or a custom "View Type" project parameter.

Alphabetical view lists on a project with 300 views are unusable. Grouped ones are navigable by
someone who has never seen the project.

**15. Naming conventions.** Everything gets named to a convention: views, sheets, worksets,
families, types, materials, parameters. In that order of how much pain bad naming causes.

**16. Audit views with a View List.** View tab → Schedules → View List. Add fields for name,
view template, scale, phase, discipline. Now you can see in one table every view that has no
template assigned, or the wrong scale, or the wrong discipline.

**17. Audit missing data with filters.** Create a view filter with the rule
`[required parameter]` `has no value`, and override matching elements in bright red. Auditing
becomes a visual check that takes seconds. (See Tutorial 26–27.)

---

## The weekly model health routine

Run every Friday on every live project. Nine checks, roughly twenty minutes.

| # | Check | Looking for |
|---|---|---|
| 1 | Warnings count and type | Trend, and any new critical warnings |
| 2 | File size trend | A sudden jump means an import, a huge family, or a runaway link |
| 3 | Purge unused | Accumulated unused content |
| 4 | Audit on open | Corruption |
| 5 | Imported CAD instances | Any import rather than link; any exploded import |
| 6 | In-place family count | Modelling shortcuts creeping in |
| 7 | Unplaced or unenclosed rooms | Broken area schedules |
| 8 | Groups, especially nested | Performance risk |
| 9 | Views not on sheets | Working views are fine; hundreds of orphans are clutter |

Record the numbers. A one-line log per week is enough, and after two months it tells you exactly
when things started going wrong.

---

## Tips

- **Track trends, not absolutes.** 400 warnings that have been stable for months is a different
  situation from 400 warnings that were 100 last week.
- **Close views you are not using.** Revit regenerates every open view.
- **Purge repeatedly** in one session.
- **Audit on a schedule**, not in a panic.
- **Save named milestone files at each issue.**

---

## Common mistakes

| Mistake | What goes wrong |
|---|---|
| Ignoring warnings entirely | Duplicate instances silently corrupt every quantity you report |
| Clearing warnings blindly | Time spent on off-axis lines while duplicates go unfixed |
| Purging without reviewing | Standard template content removed from the project |
| Never auditing | Corruption goes undetected until the file will not open |
| Relying on automatic backups only | Backups roll over; the milestone you needed is gone |
| Alphabetical browser on a 300-view project | Nobody can find anything, including you |
| Health checks only when there is a problem | By then it is a rescue, not maintenance |

---

## Professional workflow

Model health is **scheduled maintenance**, and it belongs in the BEP with a named owner and a
frequency. Twenty minutes a week prevents the two-day rescue.

`[Professional judgement]` The honest indicators that a firm is actually doing BIM rather than
owning Revit: is there a maintained project template with an owner; do drawings come out of the
model without manual patching; is there a naming convention that is actually used; are models
federated and clash-checked on a schedule rather than in a panic; do warnings get triaged; can
someone other than the author use the model. A firm scoring well on those is doing better than
most, anywhere in the world.

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `VG` / `VV` | Visibility/Graphics |
| `TL` | Thin Lines |
| `ZF` | Zoom to fit |

Most model management operations are on the Manage and Collaborate tabs.

---

## Content hooks from this tutorial

- The nine-check weekly routine — Week 37 carousel
- "Duplicate instances silently double your quantities. That's the warning that matters."
  — Week 38 Monday post
- "Track the warning trend, not the number." — Week 37 Wednesday tip
- "Export your warnings weekly. When something breaks, you'll know which week." — Model Health Tip
- "A red filter on 'has no value' turns auditing into a visual check." — High-value tip
