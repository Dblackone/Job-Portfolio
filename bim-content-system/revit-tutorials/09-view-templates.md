# Tutorial 26–27 — Visibility/Graphics, Filters and View Templates

**Objective:** control how the model appears, consistently, across hundreds of views at once.
**Difficulty:** ●● Intermediate
**Estimated time:** 60 + 45 minutes
**Prerequisites:** Tutorial 24–25 (Views).

---

## Part A — Visibility/Graphics

**1. Open Visibility/Graphics** (`VG` or `VV`) in any view. Six tabs:

| Tab | Controls |
|---|---|
| **Model Categories** | Walls, doors, floors — the model itself |
| **Annotation Categories** | Tags, dimensions, text, grids, levels |
| **Analytical Model Categories** | Analytical elements |
| **Imported Categories** | Linked and imported CAD |
| **Filters** | Rule-based overrides |
| **Revit Links** | Per-link visibility, and how each link's own settings are applied |

**2. Untick a category** to hide it in this view only. Note the word **only** — this affects
nothing else.

**3. Override graphics per category.** Expand the Projection/Surface and Cut columns to set
lines, patterns and transparency for that category in that view.

**4. Understand the override hierarchy.** From strongest to weakest:

```
Element override (per element)
   ↓
Filter override
   ↓
Category override (VG)
   ↓
Object Styles (project-wide default, Manage tab)
```

When something is not displaying the way you expect, work down this list. The answer is
almost always higher up it than you think.

---

## Part B — Filters

Filters override graphics based on **rules** rather than manual selection. This is how you make
fire-rated walls red across every view without touching a single wall.

**5. Create a filter.** `VG` → Filters tab → Edit/New → New → name it.

**6. Choose categories.** Which categories the filter can apply to — for example Walls.

**7. Set the rule.** For example: `Fire Rating` `equals` `60`. Rules can be combined with AND/OR.

**8. Apply and override.** Back in the Filters tab, add the filter to the view and set its
graphic overrides — line colour, pattern, transparency.

**9. Put the filter in a view template** so it applies everywhere, rather than in one view.

**Common uses:**

| Filter | Purpose |
|---|---|
| Fire rating | Fire strategy drawings |
| Phase or new/existing | Demolition drawings |
| Workset or discipline | Coordination views |
| Elements missing a required parameter | **Model auditing** |

`[Professional judgement]` That last one is underused and is one of the most valuable techniques
in Revit. A filter with the rule `Fire Rating` `has no value`, set to override elements in bright
red, turns model auditing into a visual check that takes seconds instead of a schedule review
that takes an hour.

---

## Part C — View templates

**10. Create a template from a view you have already set up.** Get one view exactly right, then:
View tab → View Templates → Create Template from Current View. Name it to convention.

**11. Understand what a template controls.** View scale, detail level, visual style, visibility
and graphic overrides, filters, view range, phase filter, discipline, and more. Each is
individually toggled by the **Include** checkbox in the template.

**12. Apply it.** Select views in the Project Browser (Ctrl-click for multiple) → right-click →
Apply View Template.

**13. Assign it permanently.** In view properties, set **View Template** to the template. The
view's settings are now **locked and greyed out** — they can only be changed by changing the
template.

That greying-out is not a limitation. It is the feature. It is what stops fifty people making
fifty small deviations.

**14. Edit the template, not the view.** View tab → View Templates → Manage View Templates →
select → change → OK. Every view assigned to it updates.

---

## Tips

- **Get one view perfect, then make it a template.** Do not try to build a template from scratch
  in the dialog.
- **Templates live in the project template.** Every drawing type your firm produces should have
  one before a project starts.
- **Use the Include checkboxes deliberately.** A template that controls scale is often wrong,
  because the same template may serve views at different scales.
- **Filters belong in templates**, not in individual views.
- **`TL`** (Thin Lines) when checking line weight overrides — line weights mask small differences.

---

## Common mistakes

| Mistake | What goes wrong |
|---|---|
| Fixing graphics view by view | The same fix is made fifty times and the set still drifts |
| Overriding individual elements | Invisible to everyone else, impossible to maintain, survives into the issued set |
| Not knowing the override hierarchy | Hours lost fighting an override at the wrong level |
| Using worksets to control graphics | Worksets are for ownership and loading. Use templates and filters. |
| Building templates mid-project | They should be in the project template already |
| Templates that control scale when they should not | Views forced to the wrong scale |
| Not assigning the template, just applying it once | The view drifts again the following week |

---

## Professional workflow

The rule: **graphics live in templates, never in views.**

If you find yourself opening Visibility/Graphics on a single view, stop and ask whether the fix
belongs in the template. Nine times out of ten it does.

The result is a drawing set that looks like one firm produced it — which is a quality signal
clients notice even when they cannot say why.

`[Professional judgement]` A model with fifty individually adjusted views is not a model with
fifty views. It is fifty small liabilities, each one waiting to be inconsistent in the issued set.

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `VG` / `VV` | Visibility/Graphics |
| `TL` | Thin Lines |
| `HR` | Reset temporary hide/isolate |
| `EH` | Hide element in view |
| `VH` | Hide category in view |

---

## Content hooks from this tutorial

- "Graphics live in templates, not in views." — Week 36 Monday post
- "Use a filter to find every element missing a required parameter. Auditing becomes visual."
  — Week 36 Wednesday tip, high-value
- "The override hierarchy: element, filter, category, object styles. Work down it." — Carousel
- "If you're opening VG on one view, the fix probably belongs in the template."
  — Best Practice post
