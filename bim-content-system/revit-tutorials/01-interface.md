# Tutorial 02–03 — Understanding the Interface and Navigation

**Objective:** open Revit and know what every part of the screen does, so nothing that happens
next is a mystery.
**Difficulty:** ● Beginner
**Estimated time:** 45 minutes (interface) + 30 minutes (navigation)
**Prerequisites:** Revit installed.

---

## Part A — The interface

### Step-by-step

**1. Open the sample project or any project file.**
Do not start from a blank template for this tutorial. You need something on screen to look at.

**2. Identify the six regions.** Point at each one before you touch anything.

| Region | Where | What it is |
|---|---|---|
| **Ribbon** | Top | Tools grouped in tabs: Architecture, Structure, Systems, Insert, Annotate, Analyse, Massing & Site, Collaborate, View, Manage, Modify |
| **Options Bar** | Directly under the ribbon | Settings for the tool you are currently using. Changes constantly. |
| **Properties palette** | Left | Properties of whatever is selected. If nothing is selected, it shows the **view's** properties. |
| **Project Browser** | Left, below Properties | The table of contents for the entire project: every view, legend, schedule, sheet, family and group |
| **View Control Bar** | Bottom left of the drawing area | Scale, detail level, visual style, shadows, crop, temporary hide/isolate |
| **Status Bar** | Very bottom left | What Revit is waiting for you to do |

**3. Read the Status Bar deliberately.** Start a wall command and watch it. It tells you exactly
what input is expected. Beginners ignore this bar for a year; experienced users glance at it
constantly.

**4. Explore the Project Browser.** Expand Views, then Floor Plans, then Sheets. Notice that
sheets contain views — the same views listed above. That is the whole documentation model in
one tree.

**5. Select a wall.** Watch three things change simultaneously: the Properties palette fills
with that wall's properties, the ribbon switches to the Modify tab, and the Status Bar changes.

**6. Click empty space to deselect.** The Properties palette now shows the *view's* properties —
scale, detail level, view range, phase, discipline. This is the single most important thing on
the screen and most beginners never look at it.

**7. Practise the View Control Bar.** Change detail level from Coarse to Fine and watch wall
layers appear. Change visual style from Hidden Line to Shaded. Turn shadows on and off.

### Part B — Navigation

**8. Zoom:** scroll wheel. **Pan:** hold the middle mouse button and drag. **Orbit (3D views
only):** Shift + middle mouse button.

**9. Zoom to fit:** type `ZF`, or double-click the middle mouse button.

**10. Open a 3D view:** find `{3D}` under 3D Views in the Project Browser, or use the default
3D view button on the Quick Access Toolbar.

**11. Use the ViewCube** (top right of a 3D view) to snap to standard orientations. Click a
corner for an isometric, click a face for an orthographic view.

**12. Tile your views:** type `WT` to tile all open views, `WC` to cascade. Working with a plan
and a 3D view side by side is the fastest way to learn what you are actually building.

**13. Close hidden windows:** View tab → Close Inactive. Do this often. Revit regenerates every
open view, and this is the cheapest performance improvement available.

---

## Tips

- **Lost a palette?** View tab → User Interface → tick it back on. This is the single most
  common "my Revit is broken" panic, and it takes four seconds to fix.
- **Double-click the middle mouse button** to zoom to fit. It becomes reflexive within a day.
- **The Properties palette with nothing selected is your view settings.** Learn to check there
  first when a view looks wrong.
- **Type `KS`** to open the Keyboard Shortcuts dialog and see exactly what your install has
  mapped. Do not trust any shortcut list online, including this one, over that dialog.

---

## Common mistakes

| Mistake | What actually happens |
|---|---|
| Ignoring the Status Bar | You spend minutes wondering why a tool is not responding when it is waiting for a second click |
| Never checking view properties | You blame the model for what is a view setting, repeatedly |
| Leaving twenty views open | Revit slows down and you assume it is the model |
| Working only in plan | You build things that are wrong in section and do not find out for weeks |
| Memorising shortcuts from a blog | Your install may not match. Check `KS`. |

---

## Professional workflow

Experienced users work with **at least two views visible** — usually a plan and a 3D view, or a
plan and a section — tiled with `WT`. Modelling in a single plan view is how geometry ends up
correct in plan and wrong in every other direction.

They also close inactive views habitually, not as a rescue when things slow down.

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `ZF` | Zoom to fit |
| `ZR` | Zoom in region |
| `WT` | Tile windows |
| `WC` | Cascade windows |
| `KS` | Keyboard Shortcuts dialog |
| `TL` | Thin lines |
| Middle mouse drag | Pan |
| Shift + middle mouse | Orbit (3D views) |
| Double-click middle mouse | Zoom to fit |

---

## Content hooks from this tutorial

- "Type KS. That dialog is the only shortcut list that is true for you." — Wednesday quick tip
- "The Properties palette with nothing selected is your view settings. Most beginners never look
  there." — Wednesday quick tip
- "Close Inactive Views is the cheapest performance fix in Revit." — Productivity hack
- The six-region interface breakdown — Week 14 carousel
