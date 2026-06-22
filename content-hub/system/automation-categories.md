# Social Media Automation — Category Reference

Seven special-event categories layered on top of the existing 7-pillar weekly rotation.
Categories function like "Orders" in `workflow.md` — they take a date slot; the displaced
pillar shifts forward one day.

---

## Category Definitions

### A. New Month
**Trigger:** First day of every month (automated, calendar-driven).
**Pillar mapping:** Engage / Personal slot.
**Purpose:** Welcome the new month, set intention, reinforce brand presence.
**Card type:** `monthly-theme` (portrait 1080×1350, dark variant).
**Monthly cadence:** 1 per month (mandatory).

CLI: `python3 generate.py new-month --month YYYY-MM`
Required inputs: `month_name`, `year`, `theme_word`, `highlight_from_last_month`

---

### B. Design of the Month
**Trigger:** Day 2–5 of the month, Tuesday slot.
**Pillar mapping:** Design Presentation slot.
**Purpose:** Highlight one outstanding design — showcase creativity and expertise.
**Card type:** `spotlight` (hero) + `explainer` (breakdown) — 3-slide carousel.
**Monthly cadence:** 1 per month.

CLI: `python3 generate.py design-of-month --month YYYY-MM --topic "Project Name"`
Required inputs: `project_name`, `hero_image`, `design_story`, `key_decisions`

---

### C. Project Highlights
**Trigger:** Weekly (1st Tuesday of month, then Thursdays).
**Pillar mapping:** Project Spotlight slot.
**Purpose:** Highlight important project milestones — kickoff, progress, completion.
**Card type:** `spotlight` (hero) + `tip` (milestones) — 3–4 slide carousel.
**Monthly cadence:** 4 per month.

CLI: `python3 generate.py project-highlights --project "Name" --date YYYY-MM-DD`
Required inputs: `project_name`, `project_folder`, `hero_image`, `project_story`

Subtypes: Kickoff · Construction Progress · Site Updates · Project Completion

---

### D. Design Showcase
**Trigger:** Weekly, Thursday (Render Breakdown slot).
**Pillar mapping:** Render Breakdown slot.
**Purpose:** Present completed designs — render reveal, design philosophy.
**Card type:** `spotlight` (before) + `explainer` (process) + `cta`.
**Monthly cadence:** 4 per month.

CLI: `python3 generate.py design-showcase --date YYYY-MM-DD`
Required inputs: `render_images`, `process_description`, `design_type`

Subtypes: Interior · Exterior · Concept · Architectural Visualization

---

### E. Project Showcase
**Trigger:** Weekly, Friday (Construction Insight slot).
**Pillar mapping:** Construction Insight slot.
**Purpose:** Showcase completed projects — before/after, results, client value.
**Card type:** `spotlight` + `insight` — 2–3 slide.
**Monthly cadence:** 4 per month.

CLI: `python3 generate.py project-showcase --project "Name" --date YYYY-MM-DD`
Required inputs: `project_name`, `site_lesson`, `site_images`

Subtypes: Residential · Commercial · Renovation · Construction

---

### F. Holiday Content
**Trigger:** Calendar-driven (Nigerian + international holidays, see list below).
**Pillar mapping:** Replaces nearest Engage / Personal slot.
**Purpose:** Celebrate holidays — warm, brand-first, not festive clutter.
**Card type:** `holiday` (portrait or square).
**Monthly cadence:** Seasonal (0–3 per month depending on calendar).

CLI: `python3 generate.py holiday --name "Holiday Name" --date YYYY-MM-DD`
Required inputs: `holiday_name`, `holiday_date`, `brand_message`

**Holiday calendar (recurring):**
| Date | Holiday |
|---|---|
| Jan 1 | New Year's Day |
| Jan 15 | Armed Forces Remembrance Day (Nigeria) |
| Apr (varies) | Good Friday / Easter |
| May 1 | Workers' Day |
| Jun (varies) | Eid al-Adha |
| Jun 12 | Democracy Day (Nigeria) |
| Jun (3rd Sunday) | Father's Day |
| Oct 1 | Independence Day (Nigeria) |
| Dec 25 | Christmas |
| Dec 26 | Boxing Day |
| Mar (2nd Sunday) | Mother's Day |

---

### G. Special Announcements
**Trigger:** Manual (as needed).
**Pillar mapping:** Replaces nearest available slot or posts as bonus content.
**Purpose:** Communicate important company updates.
**Card type:** `announcement` (portrait, dark).
**Monthly cadence:** Ad-hoc (0–2 per month).

CLI: `python3 generate.py special-announcement --title "Title" --date YYYY-MM-DD`
Required inputs: `announcement_title`, `announcement_body`, `effective_date`

Subtypes: New Service · Milestone · Partnership · Award · Event Invitation · Recruitment

---

## Pillar + Category Coexistence

Categories do not break the pillar rotation. They **overlay** it:

```
Week 1 of July 2026 (example):
Wed Jun 30  ── (last of June)
Thu Jul 01  ── NEW MONTH  ←── replaces BIM Explained; BIM shifts to Jul 2
Fri Jul 02  ── BIM Explained (shifted)
Sat Jul 03  ── Construction Insight (shifted)
Sun Jul 04  ── Design Presentation
Mon Jul 05  ── Engage / Personal
Tue Jul 06  ── Revit Tip
Wed Jul 07  ── DESIGN OF MONTH  ←── replaces Project Spotlight
```

---

## Recommended Monthly Cadence

| Category | Count | When |
|---|---|---|
| New Month | 1 | Day 1 |
| Design of Month | 1 | Day 2–5 (Tuesday) |
| Project Highlights | 4 | Weekly (Tuesdays) |
| Design Showcase | 4 | Weekly (Thursdays) |
| Project Showcase | 4 | Weekly (Fridays) |
| Holiday Content | 0–3 | As calendar dictates |
| Special Announcements | 0–2 | As needed |

**Total automation-category posts per month: 14–24** (on top of regular pillar rotation for remaining days).

---

## Status Lifecycle

```
draft  →  approved  →  scheduled  →  posted
  ↑ generated       ↑ human review    ↑ reminders created   ↑ confirmed after posting
```

Manage with: `python3 generate.py status list`
Transition with: `python3 generate.py status update --id ID --to STATUS`
