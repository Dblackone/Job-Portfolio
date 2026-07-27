# Tutorial 36–38 — Linking CAD, Importing CAD, and Linking Revit Models

**Objective:** bring external information into your project without damaging it.
**Difficulty:** ● Beginner (CAD) · ●● Intermediate (Revit links)
**Estimated time:** 30 + 20 + 45 minutes
**Prerequisites:** Tutorial 04–05 (coordinates).

---

## Part A — Linking CAD

**1. Open the view you want the CAD in.** Not any view — the specific one. Links come in per-view
or project-wide depending on a checkbox, and getting this wrong scatters CAD through your model.

**2. Insert tab → Link CAD.**

**3. Set the options in the dialog before clicking Open:**

| Option | Set to |
|---|---|
| **Current view only** | **Tick it** for a survey or reference you are tracing from |
| **Colors** | Black and White, or Preserve if the layers carry meaning |
| **Layers/Levels** | All, or Specify to bring in only what you need |
| **Import units** | Auto-detect usually works. If the link comes in at 1/1000 scale, set it manually. |
| **Positioning** | Auto - Origin to Origin, or Auto - Centre to Centre |
| **Place at** | The correct level |
| **Correct lines that are slightly off axis** | Tick — this cleans up survey data |

**4. Click Open.**

**5. Lock it.** Select the link → `PN` to pin. A CAD link nudged by accident is very hard to
notice and invalidates everything traced from it.

**6. Control its visibility.** `VG` → Imported Categories tab. You can turn individual DWG
layers on and off here, which is how you use a busy survey drawing without drowning in it.

**7. Switch it off when done.** Once you have modelled from it, untick the link. Leaving CAD
visible under a model is a common cause of confusing printed output.

**8. Manage links.** Insert tab → Manage Links → CAD Formats. Reload, unload, or remove links
here. Reloading brings in an updated DWG — which is the entire reason for linking rather than
importing.

---

## Part B — Importing CAD, and why not to

`[Critical]` **Link. Do not import. Never explode.**

| | Link | Import |
|---|---|---|
| Updates when the DWG changes | Yes | No |
| Removed cleanly | Yes | Partially |
| Foreign line styles and text types | Contained within the link | Loaded permanently into your project |
| Exploded | Not applicable | **Injects thousands of line styles, text styles and fill patterns that cannot easily be removed** |

Exploding an imported DWG is the most common single act of permanent damage a beginner does to a
project file. It is usually done to "just trace over it quickly." The line styles it creates —
often with names like `A-WALL-0001` — appear in every line style dropdown for the rest of the
project's life, and purging does not reliably remove them.

**If it has already happened:** Manage tab → Purge Unused, run repeatedly. Then check Line
Styles and Object Styles for foreign entries. Some will not go. In severe cases the correct
answer is to start a new project file from the template and copy clean elements across.

---

## Part C — Linking Revit models

**9. Insert tab → Link Revit.**

**10. Set the positioning.** For a coordinated project, **Auto - By Shared Coordinates**. This
is the entire reason shared coordinates were set up in Tutorial 04–05.

**11. Never nudge a link into place.** If a link does not land correctly, the coordinates are
wrong. Moving it hides the problem and it will resurface at federation, usually in front of
other people.

**12. Set Attachment vs Overlay.** Manage Links → Reference Type:

| Type | Behaviour when your model is itself linked into another |
|---|---|
| **Attachment** | The nested link comes through |
| **Overlay** | The nested link does not come through |

**Overlay is the usual choice.** Attachment causes models to arrive four levels deep and
enormous.

**13. Control link visibility.** `VG` → Revit Links tab. Per link, choose whether it displays By
Host View, By Linked View, or with custom settings. "By Linked View" lets you use the other
team's view settings, which is occasionally exactly what you want and usually not.

**14. Set worksets for links.** Put each link on its own workset. Team members can then unload
links they are not using, which is one of the largest performance improvements available on a
big project.

**15. Copy/Monitor levels and grids** from the datum discipline's link. See Tutorial 41 in the
index.

---

## Tips

- **Pin every link**, CAD and Revit alike.
- **One link, one workset.** It makes selective loading possible.
- **Current view only** for CAD you are tracing from.
- **Reload links before every coordination meeting.** Reviewing last month's model wastes
  everybody's hour.
- **Check Manage Links regularly** for links whose path has broken.

---

## Common mistakes

| Mistake | What it costs |
|---|---|
| Importing instead of linking | The reference never updates and cannot be cleanly removed |
| Exploding an import | Permanent line style and text style pollution |
| Not pinning links | A nudged link invalidates everything traced from it |
| Nudging a Revit link into position | A coordinates problem hidden, not solved |
| Attachment instead of Overlay | Nested links stack and the model becomes enormous |
| Links not on their own worksets | Nobody can unload what they are not using |
| Linking CAD into all views | Survey linework appears on drawings nobody expected |
| Not reloading before coordination | The meeting reviews out-of-date information |

---

## Professional workflow

The link strategy is agreed **in the BEP**, before anyone links anything: which models are
linked, by whom, with what reference type, on which worksets, positioned by shared coordinates,
and reloaded on what schedule.

CAD is treated as a **temporary reference**, not as project content. It comes in linked, into
one view, pinned, and it goes off as soon as it has been modelled from.

`[Professional judgement]` "The links don't line up" is almost never a link problem. It is a
coordinates decision that was never made, or was made by one person and never written down.
Recording it in the BEP takes one sentence and prevents a recurring weekly argument.

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `PN` | Pin |
| `UP` | Unpin |
| `VG` / `VV` | Visibility/Graphics |
| `AL` | Align |

---

## Content hooks from this tutorial

- "Link. Never import. Never explode." — Week 33 Monday post
- "Exploding a DWG is the most common act of permanent damage to a Revit project."
  — Week 33 Friday post
- "'The links don't line up' is never a link problem." — Week 29 Friday post
- "One link, one workset. Then people can unload what they aren't using." — Productivity hack
