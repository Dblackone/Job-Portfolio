# Tutorial 04–05 — Project Templates and Project Setup

**Objective:** start a project correctly, so that decisions made in the first hour do not cost
you months later.
**Difficulty:** ● Beginner (templates) · ●● Intermediate (coordinates)
**Estimated time:** 45 minutes + 45 minutes
**Prerequisites:** Tutorial 02–03.

---

## Part A — Project templates

A project template (`.rte`) is a starting point containing your standards: line weights, text
and dimension styles, materials, wall and floor types, view templates, browser organisation,
sheets, titleblocks, and schedules.

### Step-by-step

**1. Start a new project.** File → New → Project. Note the template selector. Whatever you pick
here determines most of what your project looks like for its entire life.

**2. Look at what a template actually contains.** Open Manage tab and work through:
Object Styles · Line Styles · Line Weights · Materials · Project Units · Project Information.
Every one of these is a firm standard, and every one of them lives in the template.

**3. Check the browser organisation.** Right-click "Views" in the Project Browser → Browser
Organisation. A good template sorts views by a parameter — discipline, phase, or a custom
"View Type" parameter — not alphabetically.

**4. Look at the view templates.** View tab → View Templates → Manage View Templates. A usable
template has view templates for every drawing type you produce.

**5. Save a project as a template.** File → Save As → Template. This is how a firm standard gets
created: take a finished, well-structured project, strip the geometry, keep the setup.

### Part B — Project setup

**6. Set project units.** Manage tab → Project Units (`UN`). Set length, area, volume, and
angle. Do this before modelling — changing units later is fine mechanically but every dimension
you have already checked needs rechecking.

**7. Fill in Project Information.** Manage tab → Project Information. Project name, number,
client, address, status. **These fields feed your titleblocks automatically.** Filling them in
now means never typing a project name on a sheet.

**8. Understand the three points.** This is the setup step that causes the most downstream pain
when skipped.

| Point | What it is | Moves? |
|---|---|---|
| **Internal origin** | Revit's own fixed 0,0,0 | Never |
| **Project base point** | The project's reference for measurement and levels | Yes |
| **Survey point** | Where the project sits in real-world coordinates | Yes |

**9. Reveal them.** In a site or level 1 plan: Visibility/Graphics (`VG`) → Site → tick Project
Base Point and Survey Point.

**10. Model near the internal origin.** Keep your building within roughly 1 km of it. Beyond
that, Revit develops accuracy and display problems — jittering geometry, failed joins, and
inaccurate snapping.

**11. Agree shared coordinates once.** If you are the first model, publish coordinates to the
others. If someone else is the datum, acquire coordinates from their link:
Manage tab → Coordinates → Acquire Coordinates → select the link.

**12. Record the decision in the BEP.** Coordinate system, origin, units, and who owns the datum.
This belongs in a document, not in one person's memory.

---

## Tips

- **Fill in Project Information on day one.** It takes three minutes and removes an entire
  category of drawing errors.
- **Never nudge a link into place by eye.** If a link does not land correctly, the coordinates
  are wrong, and moving it hides the problem rather than fixing it.
- **Set up your browser organisation before you have 200 views**, not after.
- **Keep a "template changes" log.** When something is wrong in the template, note it. Fix the
  template *between* projects, not during one.

---

## Common mistakes

| Mistake | Cost |
|---|---|
| Using the default out-of-box template on a real project | Every standard you need is missing, and you rebuild it under deadline |
| Modelling far from the internal origin | Geometry accuracy problems, failed joins, and unstable snapping — permanently |
| Never setting shared coordinates | "The links don't line up", every week, forever |
| Typing the project name on the titleblock | It is now wrong on some sheets and right on others |
| Moving a link to make it fit | You have hidden a coordinates problem that will resurface at federation |
| Changing units mid-project | Everything already checked needs rechecking |

---

## Professional workflow

On a real project the first hour is: template selected and confirmed with the team → units set →
project information filled → coordinate strategy agreed and recorded in the BEP → levels and
grids established or Copy/Monitored from the datum discipline.

No geometry is modelled until those are done. It feels slow. It is the fastest hour on the
project.

`[Professional judgement]` A firm without a maintained project template does not have BIM
standards — it has habits. Assign one owner, version it, and review it after each project.

---

## Shortcuts used

*Verify against your install with `KS`.*

| Shortcut | Action |
|---|---|
| `UN` | Project Units |
| `VG` / `VV` | Visibility/Graphics |
| `KS` | Keyboard Shortcuts dialog |

---

## Content hooks from this tutorial

- "'The links don't line up' is never a link problem. It is a coordinates decision nobody made."
  — Week 29 Friday post
- "Fill in Project Information on day one and never type a project name on a sheet again."
  — Wednesday quick tip
- "A firm without a template has habits, not standards." — Week 26 Friday post
- The three points (internal origin, project base point, survey point) — Week 29 carousel
