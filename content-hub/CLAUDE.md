# Content Hub — Session Rules

## Read the Content Kit First

Before generating any post, caption, graphic brief, template fill, or calendar entry, read:

```
project/Content Kit.dc.html
```

(relative to repo root: `/home/user/Job-Portfolio/project/Content Kit.dc.html`)

This is the authoritative brand and content standard. All 15 AI generation rules in Section 11 are binding. The root `CLAUDE.md` has a quick-reference table of all 15 rules — check it when the full Content Kit is not loaded.

---

## Content Generation Workflow

1. **Read** `project/Content Kit.dc.html` — confirm voice, color, CTA, and hashtag rules for the category
2. **Run** `python3 generate.py <category> [options]` to scaffold the post package
3. **Fill** all `{{FIELD}}` placeholders in the generated `.md` — no placeholder may remain in a finished post
4. **Check** the Quality Gate section at the bottom of each generated file
5. **Update** status via `python3 generate.py status update --id <id> --to <status>`
6. **Verify** `system/tracker.json` reflects the new state and `index.html` has the injected tracker data

## Status Lifecycle

`draft` → `approved` → `scheduled` → `posted`

Never skip a stage. Status history is written to `system/tracker.json` automatically by `generate.py`.

---

## Category → Pillar Mapping

| Category | Content Pillar | Typical Day |
|---|---|---|
| new-month | Seasonal & Holiday | 1st of month |
| design-of-month | Design Inspiration | Week 2 |
| project-highlights | Project Showcase | Week 1 & 3 |
| design-showcase | Design Inspiration | Mon / Sat |
| project-showcase | Project Showcase | Fri |
| holiday-content | Seasonal & Holiday | Holiday date |
| special-announcements | Company Updates | As needed |

---

## CLI Quick Reference

```bash
python3 generate.py new-month --month 2026-07
python3 generate.py design-of-month --month 2026-07 --topic "Project Name"
python3 generate.py project-highlights --project "Project Name" --date 2026-07-07
python3 generate.py design-showcase --date 2026-07-10
python3 generate.py project-showcase --project "Project Name" --date 2026-07-14
python3 generate.py holiday --name "Holiday Name" --date 2026-10-01
python3 generate.py special-announcement --title "Title" --date 2026-07-20
python3 generate.py status list
python3 generate.py status update --id <id> --to approved
python3 generate.py schedule --month 2026-07
python3 generate.py reminders --date 2026-07-07
```
