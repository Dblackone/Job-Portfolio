# Tutorial 33–34 — Sheets, Printing and PDF Export

**Objective:** turn a model into an issued drawing set that updates itself.
**Difficulty:** ● Beginner
**Estimated time:** 45 + 30 minutes
**Prerequisites:** Tutorials 24–27 (Views and templates).

---

## Step-by-step

### Sheets

**1. Create a sheet.** View tab → Sheet. Select a titleblock. If the one you need is not listed,
Load and browse to the `.rfa`.

**2. Set the sheet number and name.** Click them in the Project Browser or in the sheet
properties. Use the firm's convention — sheet numbers drive the drawing register and the sorting
of the whole browser.

**3. Place views.** Drag a view from the Project Browser onto the sheet. Position it, then click
to place.

**A view can be placed on one sheet only.** If you need it twice, duplicate the view. The one
exception is **legends**, which can be placed on any number of sheets.

**4. Adjust the viewport title.** Select the viewport → drag the title line ends → or change the
title type. The view name, detail number and scale fill in automatically.

**5. Set the detail number.** Viewport properties → Detail Number. Section and callout markers
elsewhere in the project now point correctly at this sheet and detail. **Never type a drawing
reference by hand** — this is what makes cross-references self-maintaining.

**6. Check the titleblock fields.** Project name, number, client and address should already be
populated from Project Information (Tutorial 04–05). Sheet-specific fields — sheet name, number,
date, revision — come from sheet properties. If you are typing any of these directly onto the
titleblock, the titleblock family is set up wrong.

**7. Set up revisions.** View tab → Revisions. Add a revision with a date and description. Then
use Annotate tab → Revision Cloud on the affected sheet, and tag it. The revision schedule in
the titleblock fills itself in.

**8. Create a sheet list.** View tab → Schedules → Sheet List. This is your drawing register,
generated rather than typed, and it cannot disagree with the sheets that exist.

---

### Printing and PDF export

**9. File → Print** (or Export → PDF in newer versions, which is generally better behaved).

**10. Select what to print.** Selected views/sheets → Select → tick the sheets. **Save the
selection set** with a name — you will reuse it at every issue.

**11. Check the settings:**

| Setting | Value |
|---|---|
| **Paper size** | Match the titleblock size |
| **Zoom** | 100% size, never "fit to page" |
| **Hidden line views** | Vector processing — much cleaner and smaller files |
| **Colours** | Black and white, or greyscale, unless the drawing requires colour |
| **Raster quality** | High for issue, lower for check prints |

**12. Set the file naming.** Configure the automatic naming so files come out as
`SheetNumber - SheetName.pdf` rather than a single combined file with a meaningless name.

**13. Open the PDF and check it.** Every time. Line weights, missing views, cropped titleblocks
and wrong revisions all show up in the PDF and not on screen.

---

## Tips

- **Save your print/export selection sets.** Naming them by issue package saves the same fifteen
  minutes at every single issue.
- **Print to PDF at 100%, never fit to page.** Fit-to-page silently changes the scale, and a
  drawing at the wrong scale is worse than no drawing.
- **Vector processing** for hidden line views produces cleaner output and smaller files.
- **Legends can go on multiple sheets.** Every other view type cannot.
- **Place schedules on sheets early** — an empty schedule on a sheet is a visible to-do list.
- **Check the sheet list against the actual sheets** before every issue.

---

## Common mistakes

| Mistake | What goes wrong |
|---|---|
| Typing drawing numbers on the titleblock | They become wrong, and nothing cross-references correctly |
| Typing the project name on each sheet | Inconsistent across the set the first time it changes |
| Trying to place a view on a second sheet | It will not work, and the reason is not obvious |
| Printing fit-to-page | The drawing is issued at the wrong scale |
| Not opening the PDF before issuing | Missing views and wrong revisions reach the client |
| Not saving print sets | Fifteen minutes lost at every issue, forever |
| Revision clouds without a revision assigned | The revision schedule stays empty |
| Titleblock fields typed rather than parametric | Every issue is a manual edit |

---

## Professional workflow

Sheets are created **early**, populated with views as they develop, and issued from saved
selection sets.

The test of a BIM-produced drawing set: **change a door type and count how many drawings you have
to touch by hand.** The answer should be zero. Every number, title, scale, cross-reference and
schedule value is generated. If any of them are typed, they are a future error waiting for a
deadline.

`[Professional judgement]` The drawing set is not a separate deliverable produced at the end. It
is a view of the model, produced continuously. Teams that treat it as a separate deliverable
discover at issue that the model and the set have diverged — and then spend the issue week
reconciling them.

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `TL` | Thin Lines — essential when checking sheets on screen |
| `ZS` | Zoom to sheet size |
| `ZF` | Zoom to fit |
| `VG` | Visibility/Graphics |

---

## Content hooks from this tutorial

- "Change a door type. How many drawings do you touch by hand? The answer should be zero."
  — Week 25 Monday post
- "Never type a drawing number." — Common Mistake post
- "Save your print selection sets. Fifteen minutes, every issue, forever." — Productivity hack
- "Fit to page silently changes your scale." — Documentation Tip
