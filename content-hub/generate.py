#!/usr/bin/env python3
"""
Dova Futures Content Hub — Social Media Automation CLI
=======================================================

Generates complete content packages for the 7 automation categories,
manages status tracking, produces monthly calendars, and creates
reminder schedules.

Usage
-----
    python3 generate.py new-month --month 2026-07
    python3 generate.py design-of-month --month 2026-07 --topic "Hillside Residence"
    python3 generate.py project-highlights --project "Ado Hall" --date 2026-07-07
    python3 generate.py design-showcase --date 2026-07-10
    python3 generate.py project-showcase --project "Uselu" --date 2026-07-14
    python3 generate.py holiday --name "Independence Day" --date 2026-10-01
    python3 generate.py special-announcement --title "New Service Launch" --date 2026-07-20

    python3 generate.py status list
    python3 generate.py status update --id 2026-07-01-new-month --to approved

    python3 generate.py schedule --month 2026-07
    python3 generate.py reminders --date 2026-07-07

Categories reference:  system/automation-categories.md
Templates:             templates/category/{category}.md
Tracker:               system/tracker.json
Posts output:          posts/YYYY/MM/{category}/YYYY-MM-DD-{category}-{slug}.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from calendar import monthrange
from datetime import date, datetime, timedelta
from pathlib import Path

# ──────────────────────────────────────────────────────────── paths
HERE = Path(__file__).resolve().parent
TRACKER_PATH = HERE / "system/tracker.json"
POSTS_ROOT = HERE / "posts"
TEMPLATES = HERE / "templates/category"
CALENDAR_DIR = HERE / "calendar"
DASHBOARD = HERE / "index.html"
CALENDAR_DIR.mkdir(parents=True, exist_ok=True)

VALID_STATUSES = ["draft", "approved", "scheduled", "posted"]

CATEGORY_COLORS = {
    "new-month":             "#B85C38",
    "design-of-month":       "#7E3AF2",
    "project-highlights":    "#1A56DB",
    "design-showcase":       "#E74694",
    "project-showcase":      "#7D5A50",
    "holiday-content":       "#0F9F6E",
    "special-announcements": "#E02424",
}

CATEGORY_LABELS = {
    "new-month":             "New Month",
    "design-of-month":       "Design of Month",
    "project-highlights":    "Project Highlights",
    "design-showcase":       "Design Showcase",
    "project-showcase":      "Project Showcase",
    "holiday-content":       "Holiday Content",
    "special-announcements": "Special Announcements",
}

# Recurring Nigerian + international holidays (MM-DD format)
HOLIDAYS = {
    "01-01": "New Year's Day",
    "01-15": "Armed Forces Remembrance Day",
    "05-01": "Workers' Day",
    "06-12": "Democracy Day",
    "10-01": "Independence Day",
    "12-25": "Christmas Day",
    "12-26": "Boxing Day",
}

# Weekday → existing pillar (0=Monday)
PILLAR_ROTATION = {
    0: "Revit Tip",
    1: "Project Spotlight",
    2: "BIM Explained",
    3: "Render Breakdown",
    4: "Construction Insight",
    5: "Design Presentation",
    6: "Engage / Personal",
}

# Pillar → color (matches index.html PC object)
PILLAR_COLORS = {
    "Revit Tip": "#E8720C",
    "Project Spotlight": "#1A56DB",
    "BIM Explained": "#7E3AF2",
    "Render Breakdown": "#E74694",
    "Construction Insight": "#7D5A50",
    "Design Presentation": "#0F9F6E",
    "Engage / Personal": "#C27803",
    "Order": "#E02424",
}


# ──────────────────────────────────────────────────────────── tracker I/O

def load_tracker() -> dict:
    if TRACKER_PATH.exists():
        return json.loads(TRACKER_PATH.read_text())
    return {"version": 1, "entries": {}, "status_history": []}


def save_tracker(data: dict) -> None:
    TRACKER_PATH.write_text(json.dumps(data, indent=2) + "\n")


def tracker_key(date_str: str, category: str) -> str:
    return f"{date_str}-{category}"


def add_tracker_entry(tracker: dict, date_str: str, category: str, slug: str,
                      post_file: str, graphics: list[str]) -> dict:
    year, month = date_str[:4], date_str[5:7]
    (tracker["entries"]
     .setdefault(year, {})
     .setdefault(month, {})
     .setdefault(category, []))
    entry = {
        "id": tracker_key(date_str, category),
        "date": date_str,
        "slug": slug,
        "status": "draft",
        "post_file": post_file,
        "graphics": graphics,
        "reminders_created": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    tracker["entries"][year][month][category].append(entry)
    return entry


def find_tracker_entry(tracker: dict, entry_id: str) -> dict | None:
    for year, months in tracker["entries"].items():
        for month, cats in months.items():
            for cat, entries in cats.items():
                for entry in entries:
                    if entry["id"] == entry_id:
                        return entry
    return None


def update_tracker_status(tracker: dict, entry_id: str, new_status: str) -> bool:
    entry = find_tracker_entry(tracker, entry_id)
    if not entry:
        return False
    old_status = entry["status"]
    entry["status"] = new_status
    entry["updated_at"] = datetime.now().isoformat(timespec="seconds")
    if new_status == "scheduled":
        entry["reminders_created"] = True
    tracker["status_history"].append({
        "id": entry_id,
        "from": old_status,
        "to": new_status,
        "at": datetime.now().isoformat(timespec="seconds"),
    })
    return True


# ──────────────────────────────────────────────────────────── template filler

def load_template(category: str) -> str:
    path = TEMPLATES / f"{category}.md"
    if not path.exists():
        raise FileNotFoundError(f"Template not found: {path}")
    return path.read_text()


def fill_template(template: str, fields: dict) -> str:
    result = template
    for key, value in fields.items():
        result = result.replace(f"{{{{{key}}}}}", str(value))
    return result


def write_post(category: str, date_str: str, slug: str, content: str) -> Path:
    year, month = date_str[:4], date_str[5:7]
    out_dir = POSTS_ROOT / year / month / category
    out_dir.mkdir(parents=True, exist_ok=True)
    fname = f"{date_str}-{category}-{slug}.md"
    out_path = out_dir / fname
    out_path.write_text(content)
    return out_path


# ──────────────────────────────────────────────────────────── dashboard injection

def inject_tracker_into_dashboard(tracker: dict) -> None:
    if not DASHBOARD.exists():
        return
    html = DASHBOARD.read_text()
    sentinel_start = "// ── TRACKER INJECTION START — DO NOT EDIT MANUALLY ──"
    sentinel_end = "// ── TRACKER INJECTION END ──"
    tracker_json = json.dumps(tracker, indent=2)
    injection_block = (
        f"{sentinel_start}\n"
        f"window.__TRACKER__ = {tracker_json};\n"
        f"{sentinel_end}"
    )
    if sentinel_start in html:
        pattern = re.compile(
            re.escape(sentinel_start) + r".*?" + re.escape(sentinel_end),
            re.DOTALL,
        )
        html = pattern.sub(injection_block, html)
    else:
        # Append before closing </script>
        html = html.replace("</script>\n</body>", f"{injection_block}\n</script>\n</body>")
    DASHBOARD.write_text(html)
    print(f"  ↳ tracker injected into {DASHBOARD.relative_to(HERE)}")


# ──────────────────────────────────────────────────────────── reminder generation

def generate_reminder_schedule(date_str: str, post_title: str, category: str,
                                post_time: str = "09:00") -> Path:
    post_dt = datetime.strptime(f"{date_str} {post_time}", "%Y-%m-%d %H:%M")
    t_minus_24 = post_dt - timedelta(hours=24)
    t_minus_2 = post_dt - timedelta(hours=2)

    lines = [
        f"# Reminder Schedule — {post_title}",
        f"**Category:** {CATEGORY_LABELS.get(category, category)}",
        f"**Post Date:** {date_str} at {post_time}",
        "",
        "## Checklist",
        f"- [ ] `{t_minus_24.strftime('%Y-%m-%d %H:%M')}` — **Prep & review** — Check draft, verify graphics, confirm captions are final",
        f"- [ ] `{t_minus_2.strftime('%Y-%m-%d %H:%M')}` — **Final check** — Export graphics, copy captions to clipboard, verify handles",
        f"- [ ] `{post_dt.strftime('%Y-%m-%d %H:%M')}` — **POST NOW** — {post_title}",
        "",
        "## Posting Order",
        "1. Instagram (carousel or single + hashtags)",
        "2. LinkedIn (first-person story caption)",
        "3. X / Twitter (thread or single)",
        "4. WhatsApp Status (personal, direct message)",
        "5. Facebook / Threads (repurpose Instagram caption)",
        "",
        "## Handles",
        "- Instagram / TikTok: @dova_futures",
        "- X / Twitter: @d_black_one",
        "- LinkedIn: linkedin.com/in/vollmann-akarakiri-49127b1a0",
        "- WhatsApp: wa.me/2348169477706",
        "",
        "## Todoist JSON (paste into MCP tool if needed)",
        "```json",
        json.dumps([
            {"content": f"Prep & review: {post_title}", "dueString": t_minus_24.strftime("%Y-%m-%d %H:%M"), "priority": "p2"},
            {"content": f"Final check: {post_title}", "dueString": t_minus_2.strftime("%Y-%m-%d %H:%M"), "priority": "p1"},
            {"content": f"POST NOW — {post_title}", "dueString": post_dt.strftime("%Y-%m-%d %H:%M"), "priority": "p1"},
        ], indent=2),
        "```",
    ]

    year, month = date_str[:4], date_str[5:7]
    out_dir = POSTS_ROOT / year / month / category
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{date_str}-{category}-reminder-schedule.md"
    out_path.write_text("\n".join(lines) + "\n")
    return out_path


# ──────────────────────────────────────────────────────────── calendar generator

def generate_monthly_calendar(year: int, month: int, tracker: dict) -> Path:
    month_str = f"{month:02d}"
    year_str = str(year)
    _, days_in_month = monthrange(year, month)

    # Build automation-category lookup for this month
    cat_by_date: dict[str, list[dict]] = {}
    month_entries = tracker["entries"].get(year_str, {}).get(month_str, {})
    for cat, entries in month_entries.items():
        for entry in entries:
            cat_by_date.setdefault(entry["date"], []).append({
                "category": cat,
                "slug": entry["slug"],
                "status": entry["status"],
            })

    status_symbols = {"draft": "☐", "approved": "◑", "scheduled": "◐", "posted": "★"}

    header = [
        f"# Content Calendar — {datetime(year, month, 1).strftime('%B %Y')}",
        "",
        "| Date | Day | Pillar | Category | Topic / Slug | Format | Status |",
        "|------|-----|--------|----------|--------------|--------|--------|",
    ]

    rows = []
    for day in range(1, days_in_month + 1):
        d = date(year, month, day)
        date_str = d.isoformat()
        pillar = PILLAR_ROTATION[d.weekday()]
        cats = cat_by_date.get(date_str, [])

        if cats:
            for c in cats:
                sym = status_symbols.get(c["status"], "☐")
                label = CATEGORY_LABELS.get(c["category"], c["category"])
                rows.append(
                    f"| {date_str} | {d.strftime('%a')} | {pillar} | **{label}** "
                    f"| {c['slug']} | — | {sym} {c['status'].capitalize()} |"
                )
        else:
            # Check for recurring holiday
            holiday = HOLIDAYS.get(d.strftime("%m-%d"))
            if holiday:
                rows.append(
                    f"| {date_str} | {d.strftime('%a')} | {pillar} | *(Holiday: {holiday})* "
                    f"| — | — | ☐ |"
                )
            else:
                rows.append(
                    f"| {date_str} | {d.strftime('%a')} | {pillar} | — | — | — | ☐ |"
                )

    month_name = datetime(year, month, 1).strftime("%B").lower()
    _, end_day = monthrange(year, month)
    fname = f"{year}-{month_str}-01_to_{month_str}-{end_day:02d}.md"
    out_path = CALENDAR_DIR / fname
    out_path.write_text("\n".join(header + rows) + "\n")
    return out_path


# ──────────────────────────────────────────────────────────── category generators

def _month_first_day(month_arg: str) -> str:
    """Return YYYY-MM-01 from a YYYY-MM argument."""
    parts = month_arg.split("-")
    return f"{parts[0]}-{parts[1]}-01"


def cmd_new_month(args: argparse.Namespace) -> None:
    month_parts = args.month.split("-")
    year, month_num = month_parts[0], month_parts[1]
    date_str = f"{year}-{month_num}-01"
    month_name = datetime(int(year), int(month_num), 1).strftime("%B")
    theme_word = args.theme or "Build"
    highlight = args.highlight or "Last month's strongest post carried the most honest insight."
    slug = f"{month_name.lower()}-kickoff"

    fields = {
        "ID": tracker_key(date_str, "new-month"),
        "TITLE": f"{month_name} {year} — {theme_word}",
        "DATE": date_str,
        "CORE_IDEA": f"Welcome {month_name} with intention: {theme_word}",
        "HOOK": f"{month_name} is here. One word for it: {theme_word}.",
        "COPY": (f"New month. Fresh start.\n\n"
                 f"Last month: {highlight}\n\n"
                 f"This month, one intention: {theme_word}.\n\n"
                 f"I'll be sharing the work, the lessons, and the builds — one post at a time.\n\n"
                 f"Follow along if that's useful to you."),
        "CTA": f"Follow along this {month_name} →",
        "GRAPHIC_FILE": f"graphics/output/{date_str}-new-month-cover.png",
        "MONTH_NAME": month_name.upper(),
        "YEAR": year,
        "THEME_WORD": theme_word,
        "INSTAGRAM_CAPTION": (
            f"{month_name} is here. One word for it: {theme_word}.\n\n"
            f"Last month: {highlight}\n\n"
            f"This month I'm sharing one idea per day — BIM, design, construction, and the reality of building in Nigeria.\n\n"
            f"Follow @dova_futures if that's your kind of content."
        ),
        "HASHTAGS_INSTAGRAM": (
            f"#NewMonth #{month_name}{year} #ArchitectLife #BuildInPublic "
            f"#NigerianArchitect #DovaFutures #BIM #Architecture #DesignAndBuild "
            f"#AECommunity #ConstructionNigeria #ArchitectsOfInstagram"
        ),
        "LINKEDIN_CAPTION": (
            f"{month_name} is here.\n\n"
            f"Last month: {highlight}\n\n"
            f"This month, I'm returning to one intention: {theme_word}.\n\n"
            f"I'll keep posting one idea per day — BIM coordination, architectural design, "
            f"and construction management insights from real projects.\n\n"
            f"If you work in AEC or are planning a build, follow along."
        ),
        "HASHTAGS_LINKEDIN": f"#Architecture #BIM #DesignAndBuild #Construction#{month_name}",
        "TWITTER_CAPTION": (
            f"{month_name}.\n\nOne word: {theme_word}.\n\n"
            f"Daily BIM + construction posts. Follow if that's useful."
        ),
        "HASHTAGS_TWITTER": "#BIM #Architecture",
        "WHATSAPP_CAPTION": (
            f"Happy new month! {month_name} is here — I'll be sharing daily posts on BIM, "
            f"architecture, and construction this month. Follow @dova_futures on Instagram "
            f"or reply here if there's anything specific you'd like me to cover."
        ),
    }

    template = load_template("new-month")
    content = fill_template(template, fields)
    post_path = write_post("new-month", date_str, slug, content)

    tracker = load_tracker()
    entry = add_tracker_entry(
        tracker, date_str, "new-month", slug,
        str(post_path.relative_to(HERE)),
        [f"graphics/output/{date_str}-new-month-cover.png"]
    )
    save_tracker(tracker)
    inject_tracker_into_dashboard(tracker)

    print(f"\n✓ New Month package generated")
    print(f"  Post:    {post_path.relative_to(HERE)}")
    print(f"  ID:      {entry['id']}")
    print(f"  Status:  {entry['status']}")
    print(f"\n  Next: python3 generate.py reminders --date {date_str}")
    print(f"  Approve: python3 generate.py status update --id {entry['id']} --to approved")


def cmd_design_of_month(args: argparse.Namespace) -> None:
    month_parts = args.month.split("-")
    year, month_num = month_parts[0], month_parts[1]
    # Default to 2nd of the month (Tuesday-ish)
    date_str = args.date or f"{year}-{month_num}-02"
    month_name = datetime(int(year), int(month_num), 1).strftime("%B")
    topic = args.topic or "Featured Project"
    slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")

    fields = {
        "ID": tracker_key(date_str, "design-of-month"),
        "TITLE": f"Design of the Month — {topic}",
        "DATE": date_str,
        "CORE_IDEA": f"Showcase {topic} as the standout design this month",
        "HOOK": f"This is the design I'm most proud of from {month_name}.",
        "DESIGN_STORY": f"[Describe the design story for {topic} here]",
        "KEY_DECISIONS": "[List the key design decisions — 3 specific, honest ones]",
        "SOURCE_ASSETS": f"[Add asset paths for {topic}]",
        "GRAPHIC_FILES": (
            f"graphics/output/{date_str}-design-of-month-01.png, "
            f"graphics/output/{date_str}-design-of-month-02.png, "
            f"graphics/output/{date_str}-design-of-month-03.png"
        ),
        "MONTH_NAME": month_name.upper(),
        "YEAR": year,
        "PROJECT_NAME": topic,
        "TAGLINE": f"[One-line description of {topic}]",
        "KEY_DECISION_1": "[First key design decision]",
        "KEY_DECISION_2": "[Second key design decision]",
        "KEY_DECISION_3": "[Third key design decision]",
        "CTA": "DM me if you're planning something similar.",
        "INSTAGRAM_CAPTION": (
            f"Design of the Month: {topic}.\n\n"
            f"[Write the Instagram caption here — hook, story, 3 decisions, CTA.]\n\n"
            f"Swipe to see the breakdown 👉\n\n"
            f"DM me if you're designing something similar."
        ),
        "HASHTAGS_INSTAGRAM": (
            "#DesignOfTheMonth #Architecture #ArchitectureNigeria #ResidentialDesign "
            "#ArchitecturalVisualization #BIM #Revit #NigerianArchitect #ModernArchitecture "
            "#DesignAndBuild #ArchitecturalDesign"
        ),
        "LINKEDIN_CAPTION": (
            f"Design of the Month — {month_name} {year}: {topic}.\n\n"
            f"[Write the LinkedIn caption here — professional tone, first-person, lessons.]\n\n"
            f"If you're planning a project and want design + BIM handled by the same person who "
            f"understands the site — let's talk."
        ),
        "HASHTAGS_LINKEDIN": "#Architecture #BIM #ResidentialDesign #DesignAndBuild",
        "TWITTER_CAPTION": (
            f"Design of the Month: {topic}.\n\n"
            f"[Key insight in 2–3 short lines.]\n\n"
            f"Thread below 👇"
        ),
        "HASHTAGS_TWITTER": "#Architecture #BIM",
        "WHATSAPP_CAPTION": (
            f"Hi 👋 Just posted a breakdown of {topic} — the design thinking behind it and the "
            f"key decisions. Take a look on Instagram @dova_futures."
        ),
    }

    template = load_template("design-of-month")
    content = fill_template(template, fields)
    post_path = write_post("design-of-month", date_str, slug, content)

    tracker = load_tracker()
    entry = add_tracker_entry(
        tracker, date_str, "design-of-month", slug,
        str(post_path.relative_to(HERE)),
        [f"graphics/output/{date_str}-design-of-month-{i:02d}.png" for i in range(1, 4)]
    )
    save_tracker(tracker)
    inject_tracker_into_dashboard(tracker)

    print(f"\n✓ Design of Month package generated")
    print(f"  Post:    {post_path.relative_to(HERE)}")
    print(f"  ID:      {entry['id']}")
    print(f"\n  NOTE: Fill in the design story and captions in the generated file.")
    print(f"  Approve: python3 generate.py status update --id {entry['id']} --to approved")


def cmd_project_highlights(args: argparse.Namespace) -> None:
    date_str = args.date
    project = args.project or "Featured Project"
    slug = re.sub(r"[^a-z0-9]+", "-", project.lower()).strip("-")
    subtype = args.subtype or "Project Kickoff"

    fields = {
        "ID": tracker_key(date_str, "project-highlights"),
        "TITLE": f"Project Highlights — {project}",
        "DATE": date_str,
        "CORE_IDEA": f"Highlight milestone for {project}: {subtype}",
        "HOOK": f"[Write a strong hook for the {project} highlight]",
        "PROJECT_STORY": f"[Describe the {project} story here — what happened, what was challenging, what was learned]",
        "CHALLENGE": f"[What was the main challenge on {project}?]",
        "SOLUTION": f"[How was it solved?]",
        "IMPACT": f"[What was the result/impact?]",
        "SOURCE_ASSETS": f"[Add asset paths for {project}]",
        "GRAPHIC_FILES": (
            f"graphics/output/{date_str}-project-highlights-01.png, "
            f"graphics/output/{date_str}-project-highlights-02.png"
        ),
        "SUBTYPE": subtype.upper(),
        "PROJECT_NAME": project,
        "PROJECT_LOCATION": args.location or "[Location]",
        "PROJECT_TYPE": args.project_type or "[Project Type]",
        "POINT_1": "[First key point about the project]",
        "POINT_2": "[Second key point]",
        "POINT_3": "[Third key point]",
        "MILESTONE_HEADLINE": f"{subtype} — what this means.",
        "MILESTONE_DETAIL": "[Describe the milestone in one clear sentence]",
        "CTA": "Follow along for the full project story.",
        "INSTAGRAM_CAPTION": f"[Write Instagram caption for {project} — {subtype}]",
        "HASHTAGS_INSTAGRAM": (
            "#Architecture #ArchitectureNigeria #ProjectHighlight #BIM #Revit "
            "#NigerianArchitect #DesignAndBuild #ConstructionNigeria #ProjectManagement "
            "#BuildingDesign #AEC #ArchitecturalVisualization"
        ),
        "LINKEDIN_CAPTION": f"[Write LinkedIn caption for {project} — {subtype}]",
        "HASHTAGS_LINKEDIN": "#Architecture #BIM #Construction #ProjectManagement",
        "TWITTER_CAPTION": f"[Write Twitter caption for {project} — {subtype}]",
        "HASHTAGS_TWITTER": "#BIM #Architecture",
        "WHATSAPP_CAPTION": (
            f"Hi 👋 Sharing a highlight from the {project} project today. "
            f"Check it out on Instagram @dova_futures."
        ),
        "ALT_TEXT": f"Project highlight carousel for {project}. Shows {subtype.lower()} stage.",
    }

    template = load_template("project-highlights")
    content = fill_template(template, fields)
    post_path = write_post("project-highlights", date_str, slug, content)

    tracker = load_tracker()
    entry = add_tracker_entry(
        tracker, date_str, "project-highlights", slug,
        str(post_path.relative_to(HERE)),
        [f"graphics/output/{date_str}-project-highlights-{i:02d}.png" for i in range(1, 3)]
    )
    save_tracker(tracker)
    inject_tracker_into_dashboard(tracker)

    print(f"\n✓ Project Highlights package generated")
    print(f"  Post:    {post_path.relative_to(HERE)}")
    print(f"  ID:      {entry['id']}")
    print(f"\n  NOTE: Fill in the hook, project story, and captions.")
    print(f"  Approve: python3 generate.py status update --id {entry['id']} --to approved")


def cmd_design_showcase(args: argparse.Namespace) -> None:
    date_str = args.date
    design_type = args.design_type or "Interior Design"
    design_name = args.name or "Featured Design"
    slug = re.sub(r"[^a-z0-9]+", "-", design_name.lower()).strip("-")

    fields = {
        "ID": tracker_key(date_str, "design-showcase"),
        "TITLE": f"Design Showcase — {design_name}",
        "DATE": date_str,
        "CORE_IDEA": f"Showcase {design_name} — {design_type}",
        "HOOK": f"[Write a strong hook for this {design_type} showcase]",
        "DESIGN_DESCRIPTION": f"[Describe {design_name} — what it is, where, what makes it stand out]",
        "DESIGN_PHILOSOPHY": f"[What was the design philosophy behind {design_name}?]",
        "KEY_FEATURES": f"[List 3 key design features]",
        "PROCESS_DESCRIPTION": f"[Describe the process from concept to final render]",
        "SOURCE_ASSETS": f"[Add render paths for {design_name}]",
        "GRAPHIC_FILES": (
            f"graphics/output/{date_str}-design-showcase-01.png, "
            f"graphics/output/{date_str}-design-showcase-02.png"
        ),
        "DESIGN_TYPE": design_type.upper(),
        "DESIGN_NAME": design_name,
        "DESIGN_TAGLINE": f"[One-line description of the design]",
        "FEATURE_1": "[First standout feature]",
        "FEATURE_2": "[Second standout feature]",
        "FEATURE_3": "[Third standout feature]",
        "CTA": "DM me to discuss your project.",
        "INSTAGRAM_CAPTION": f"[Write Instagram caption for {design_name} showcase]",
        "HASHTAGS_INSTAGRAM": (
            "#DesignShowcase #ArchViz #3DRendering #ArchitecturalVisualization "
            "#InteriorDesign #ExteriorDesign #Architecture #NigerianArchitect "
            "#Lumion #DesignAndBuild #RenderLovers #ArchitectureLovers"
        ),
        "LINKEDIN_CAPTION": f"[Write LinkedIn caption for {design_name} — focus on design thinking]",
        "HASHTAGS_LINKEDIN": "#Architecture #ArchViz #InteriorDesign #DesignProcess",
        "TWITTER_CAPTION": f"[Write Twitter caption for {design_name} — sharp and concise]",
        "HASHTAGS_TWITTER": "#ArchViz #Architecture",
        "WHATSAPP_CAPTION": (
            f"Hi 👋 Just posted a design showcase — {design_name}. "
            f"Check @dova_futures on Instagram."
        ),
        "ALT_TEXT": f"Design showcase: {design_name}. {design_type} render with design breakdown.",
    }

    template = load_template("design-showcase")
    content = fill_template(template, fields)
    post_path = write_post("design-showcase", date_str, slug, content)

    tracker = load_tracker()
    entry = add_tracker_entry(
        tracker, date_str, "design-showcase", slug,
        str(post_path.relative_to(HERE)),
        [f"graphics/output/{date_str}-design-showcase-{i:02d}.png" for i in range(1, 3)]
    )
    save_tracker(tracker)
    inject_tracker_into_dashboard(tracker)

    print(f"\n✓ Design Showcase package generated")
    print(f"  Post:    {post_path.relative_to(HERE)}")
    print(f"  ID:      {entry['id']}")
    print(f"  Approve: python3 generate.py status update --id {entry['id']} --to approved")


def cmd_project_showcase(args: argparse.Namespace) -> None:
    date_str = args.date
    project = args.project or "Featured Project"
    project_type = args.project_type or "Residential"
    slug = re.sub(r"[^a-z0-9]+", "-", project.lower()).strip("-")

    fields = {
        "ID": tracker_key(date_str, "project-showcase"),
        "TITLE": f"Project Showcase — {project}",
        "DATE": date_str,
        "CORE_IDEA": f"Showcase completed {project_type.lower()} project: {project}",
        "HOOK": f"[Write a strong hook for the {project} showcase]",
        "BEFORE_AFTER_STORY": f"[Describe the before/after story for {project}]",
        "PROJECT_RESULTS": f"[What were the concrete results? Be specific.]",
        "CLIENT_VALUE": f"[What value did the client receive?]",
        "SITE_LESSON": f"[What is the one site lesson from {project}?]",
        "SOURCE_ASSETS": f"[Add photo/render paths for {project}]",
        "GRAPHIC_FILES": (
            f"graphics/output/{date_str}-project-showcase-01.png, "
            f"graphics/output/{date_str}-project-showcase-02.png"
        ),
        "PROJECT_TYPE": project_type.upper(),
        "PROJECT_NAME": project,
        "PROJECT_LOCATION": args.location or "[Location]",
        "COMPLETION_PERIOD": args.completed or "[Month Year]",
        "LESSON_HEADLINE": "[What's the one lesson?]",
        "LESSON_POINT_1": "[First lesson point]",
        "LESSON_POINT_2": "[Second lesson point]",
        "LESSON_POINT_3": "[Third lesson point]",
        "RESULT_SUMMARY": "[One sentence on the project outcome]",
        "CTA": "DM me if you're planning a similar project.",
        "INSTAGRAM_CAPTION": f"[Write Instagram caption for {project} showcase]",
        "HASHTAGS_INSTAGRAM": (
            "#ProjectShowcase #Architecture #ArchitectureNigeria #Construction "
            "#DesignAndBuild #NigerianArchitect #BIM #RealEstateNigeria "
            "#ConstructionNigeria #ModernArchitecture #ProjectManagement"
        ),
        "LINKEDIN_CAPTION": f"[Write LinkedIn caption for {project} — professional, results-focused]",
        "HASHTAGS_LINKEDIN": "#Architecture #Construction #BIM #ProjectManagement",
        "TWITTER_CAPTION": f"[Write Twitter caption — before/after story in 3–4 lines]",
        "HASHTAGS_TWITTER": "#Architecture #Construction",
        "WHATSAPP_CAPTION": (
            f"Hi 👋 Just posted a showcase of the {project} project — the full story. "
            f"Check @dova_futures on Instagram."
        ),
        "ALT_TEXT": f"Project showcase: {project}. {project_type} project site photo and lessons.",
    }

    template = load_template("project-showcase")
    content = fill_template(template, fields)
    post_path = write_post("project-showcase", date_str, slug, content)

    tracker = load_tracker()
    entry = add_tracker_entry(
        tracker, date_str, "project-showcase", slug,
        str(post_path.relative_to(HERE)),
        [f"graphics/output/{date_str}-project-showcase-{i:02d}.png" for i in range(1, 3)]
    )
    save_tracker(tracker)
    inject_tracker_into_dashboard(tracker)

    print(f"\n✓ Project Showcase package generated")
    print(f"  Post:    {post_path.relative_to(HERE)}")
    print(f"  ID:      {entry['id']}")
    print(f"  Approve: python3 generate.py status update --id {entry['id']} --to approved")


def cmd_holiday(args: argparse.Namespace) -> None:
    date_str = args.date
    holiday_name = args.name
    slug = re.sub(r"[^a-z0-9]+", "-", holiday_name.lower()).strip("-")

    fields = {
        "ID": tracker_key(date_str, "holiday-content"),
        "TITLE": f"Happy {holiday_name}",
        "DATE": date_str,
        "CORE_IDEA": f"Celebrate {holiday_name} — brand-first, warm greeting",
        "HOOK": f"Happy {holiday_name} from Dova Futures.",
        "GREETING_MESSAGE": f"Wishing everyone a wonderful {holiday_name}.",
        "BRAND_MESSAGE": args.message or "From all of us at Dova Futures — keep building.",
        "HOLIDAY_NAME": holiday_name,
        "HOLIDAY_NAME_UPPER": holiday_name.upper(),
        "HOLIDAY_DATE": date_str,
        "GRAPHIC_FILE": f"graphics/output/{date_str}-holiday-{slug}.png",
        "HEADLINE": f"Happy {holiday_name}.",
        "SUB_TEXT": args.message or "From all of us at Dova Futures — keep building.",
        "CTA": "Follow @dova_futures for daily design and construction posts.",
        "INSTAGRAM_CAPTION": (
            f"Happy {holiday_name} 🙏\n\n"
            f"{args.message or 'Wishing everyone rest, joy, and a renewed sense of purpose.'}\n\n"
            f"From the Dova Futures team — keep building."
        ),
        "HASHTAGS_INSTAGRAM": (
            f"#{holiday_name.replace(' ', '')} #Nigeria #DovaFutures "
            f"#Architecture #NigerianArchitect #DesignAndBuild #BIM"
        ),
        "LINKEDIN_CAPTION": (
            f"Happy {holiday_name}.\n\n"
            f"{args.message or 'Wishing the entire AEC community rest and reflection.'}\n\n"
            f"— Vollmann Akarakiri, Dova Futures Limited"
        ),
        "HASHTAGS_LINKEDIN": f"#{holiday_name.replace(' ', '')} #Nigeria",
        "TWITTER_CAPTION": (
            f"Happy {holiday_name}.\n\n"
            f"{args.message or 'Rest. Reflect. Build better.'}"
        ),
        "HASHTAGS_TWITTER": f"#{holiday_name.replace(' ', '')}",
        "WHATSAPP_CAPTION": (
            f"Happy {holiday_name}! 🎉 Wishing you and your family a great celebration. "
            f"— Vollmann · Dova Futures"
        ),
    }

    template = load_template("holiday-content")
    content = fill_template(template, fields)
    post_path = write_post("holiday-content", date_str, slug, content)

    tracker = load_tracker()
    entry = add_tracker_entry(
        tracker, date_str, "holiday-content", slug,
        str(post_path.relative_to(HERE)),
        [f"graphics/output/{date_str}-holiday-{slug}.png"]
    )
    save_tracker(tracker)
    inject_tracker_into_dashboard(tracker)

    print(f"\n✓ Holiday Content package generated")
    print(f"  Post:    {post_path.relative_to(HERE)}")
    print(f"  ID:      {entry['id']}")
    print(f"  Approve: python3 generate.py status update --id {entry['id']} --to approved")


def cmd_special_announcement(args: argparse.Namespace) -> None:
    date_str = args.date
    title = args.title
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")

    fields = {
        "ID": tracker_key(date_str, "special-announcements"),
        "TITLE": title,
        "DATE": date_str,
        "CORE_IDEA": f"Announce: {title}",
        "HOOK": f"{title} — effective {args.effective or date_str}.",
        "ANNOUNCEMENT_BODY": args.body or f"[Describe the announcement: {title}]",
        "EFFECTIVE_DATE": args.effective or date_str,
        "ANNOUNCEMENT_HEADLINE": title,
        "ANNOUNCEMENT_HEADLINE_SHORT": title[:60] + ("…" if len(title) > 60 else ""),
        "ANNOUNCEMENT_SUB": args.body or "[Supporting detail for the announcement]",
        "GRAPHIC_FILE": f"graphics/output/{date_str}-announcement-{slug}.png",
        "CTA": "DM us or reply here for details.",
        "INSTAGRAM_CAPTION": (
            f"{title}.\n\n"
            f"{args.body or '[Full announcement copy here]'}\n\n"
            f"Questions? DM us or send a message on WhatsApp: wa.me/2348169477706"
        ),
        "HASHTAGS_INSTAGRAM": (
            "#Announcement #DovaFutures #Architecture #BIM #DesignAndBuild "
            "#NigerianArchitect #ConstructionNigeria"
        ),
        "LINKEDIN_CAPTION": (
            f"{title}.\n\n"
            f"{args.body or '[Full announcement copy — professional tone]'}\n\n"
            f"For enquiries: wa.me/2348169477706 or linkedin.com/in/vollmann-akarakiri-49127b1a0"
        ),
        "HASHTAGS_LINKEDIN": "#Announcement #Architecture #BIM #Construction",
        "TWITTER_CAPTION": (
            f"{title}.\n\n"
            f"{args.body or '[Key detail in 2 lines]'}"
        ),
        "HASHTAGS_TWITTER": "#Architecture #DovaFutures",
        "WHATSAPP_CAPTION": (
            f"📢 {title}\n\n"
            f"{args.body or '[Announcement detail]'}\n\n"
            f"Reply here for more info. — Vollmann · Dova Futures"
        ),
    }

    template = load_template("special-announcements")
    content = fill_template(template, fields)
    post_path = write_post("special-announcements", date_str, slug, content)

    tracker = load_tracker()
    entry = add_tracker_entry(
        tracker, date_str, "special-announcements", slug,
        str(post_path.relative_to(HERE)),
        [f"graphics/output/{date_str}-announcement-{slug}.png"]
    )
    save_tracker(tracker)
    inject_tracker_into_dashboard(tracker)

    print(f"\n✓ Special Announcement package generated")
    print(f"  Post:    {post_path.relative_to(HERE)}")
    print(f"  ID:      {entry['id']}")
    print(f"  Approve: python3 generate.py status update --id {entry['id']} --to approved")


# ──────────────────────────────────────────────────────────── status commands

def cmd_status_list(args: argparse.Namespace) -> None:
    tracker = load_tracker()
    if not tracker["entries"]:
        print("No entries in tracker yet. Run a generate command first.")
        return

    filter_month = args.month if hasattr(args, "month") and args.month else None
    filter_cat = args.category if hasattr(args, "category") and args.category else None

    rows = []
    for year, months in sorted(tracker["entries"].items()):
        for month, cats in sorted(months.items()):
            if filter_month and f"{year}-{month}" != filter_month:
                continue
            for cat, entries in sorted(cats.items()):
                if filter_cat and cat != filter_cat:
                    continue
                for entry in entries:
                    rows.append(entry)

    if not rows:
        print("No entries match the filter.")
        return

    status_symbols = {"draft": "○", "approved": "◑", "scheduled": "◐", "posted": "★"}
    col_widths = [12, 25, 20, 12, 10]
    header = f"{'Date':<{col_widths[0]}} {'ID':<{col_widths[1]}} {'Category':<{col_widths[2]}} {'Slug':<{col_widths[3]}} {'Status'}"
    print("\n" + header)
    print("─" * (sum(col_widths) + 4))
    for r in rows:
        sym = status_symbols.get(r["status"], "?")
        cat_label = CATEGORY_LABELS.get(r["id"].split("-", 3)[-1] if len(r["id"].split("-")) > 3 else "", r["id"])
        # derive category from entry id: YYYY-MM-DD-{category}
        parts = r["id"].split("-")
        cat_from_id = "-".join(parts[3:]) if len(parts) > 3 else "—"
        cat_label = CATEGORY_LABELS.get(cat_from_id, cat_from_id)
        print(f"{r['date']:<{col_widths[0]}} {r['id']:<{col_widths[1]}} {cat_label:<{col_widths[2]}} {r['slug']:<{col_widths[3]}} {sym} {r['status'].capitalize()}")
    print()


def cmd_status_update(args: argparse.Namespace) -> None:
    new_status = args.to
    if new_status not in VALID_STATUSES:
        print(f"Invalid status: {new_status!r}. Valid: {VALID_STATUSES}")
        sys.exit(1)

    tracker = load_tracker()
    if not update_tracker_status(tracker, args.id, new_status):
        print(f"Entry not found: {args.id}")
        sys.exit(1)

    save_tracker(tracker)
    inject_tracker_into_dashboard(tracker)
    print(f"✓ {args.id}  →  {new_status}")


# ──────────────────────────────────────────────────────────── schedule command

def cmd_schedule(args: argparse.Namespace) -> None:
    parts = args.month.split("-")
    year, month = int(parts[0]), int(parts[1])
    tracker = load_tracker()
    out_path = generate_monthly_calendar(year, month, tracker)
    month_name = datetime(year, month, 1).strftime("%B %Y")
    print(f"\n✓ Calendar generated for {month_name}")
    print(f"  File:  {out_path.relative_to(HERE)}")


# ──────────────────────────────────────────────────────────── reminders command

def cmd_reminders(args: argparse.Namespace) -> None:
    date_str = args.date
    post_time = args.time or "09:00"

    tracker = load_tracker()
    year, month = date_str[:4], date_str[5:7]
    month_entries = tracker["entries"].get(year, {}).get(month, {})

    # Find entries for this date
    entries_on_date = []
    for cat, entries in month_entries.items():
        for entry in entries:
            if entry["date"] == date_str:
                entries_on_date.append((cat, entry))

    if not entries_on_date:
        print(f"No tracker entries found for {date_str}.")
        print(f"Run a generate command first, then reminders.")
        sys.exit(1)

    for cat, entry in entries_on_date:
        post_title = entry["slug"].replace("-", " ").title()
        out_path = generate_reminder_schedule(date_str, post_title, cat, post_time)
        update_tracker_status(tracker, entry["id"], "scheduled")
        print(f"\n✓ Reminder schedule created")
        print(f"  Post:   {entry['id']}")
        print(f"  File:   {out_path.relative_to(HERE)}")
        print(f"  Status: scheduled")

    save_tracker(tracker)
    inject_tracker_into_dashboard(tracker)


# ──────────────────────────────────────────────────────────── argument parser

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Dova Futures Social Media Content Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command")

    # ── new-month
    p = sub.add_parser("new-month", help="Generate New Month content package")
    p.add_argument("--month", required=True, metavar="YYYY-MM", help="Month (e.g. 2026-07)")
    p.add_argument("--theme", metavar="WORD", help="Theme word for the month (default: Build)")
    p.add_argument("--highlight", metavar="TEXT", help="Key highlight from last month")

    # ── design-of-month
    p = sub.add_parser("design-of-month", help="Generate Design of the Month package")
    p.add_argument("--month", required=True, metavar="YYYY-MM")
    p.add_argument("--topic", metavar="NAME", help="Project or design name")
    p.add_argument("--date", metavar="YYYY-MM-DD", help="Override posting date")

    # ── project-highlights
    p = sub.add_parser("project-highlights", help="Generate Project Highlights package")
    p.add_argument("--project", required=True, metavar="NAME")
    p.add_argument("--date", required=True, metavar="YYYY-MM-DD")
    p.add_argument("--subtype", metavar="TYPE",
                   choices=["Project Kickoff", "Construction Progress", "Site Updates", "Project Completion"],
                   default="Project Kickoff")
    p.add_argument("--location", metavar="TEXT")
    p.add_argument("--project-type", dest="project_type", metavar="TYPE")

    # ── design-showcase
    p = sub.add_parser("design-showcase", help="Generate Design Showcase package")
    p.add_argument("--date", required=True, metavar="YYYY-MM-DD")
    p.add_argument("--name", metavar="NAME", help="Design name")
    p.add_argument("--design-type", dest="design_type", metavar="TYPE",
                   choices=["Interior Design", "Exterior Design", "Concept Design", "Architectural Visualization"],
                   default="Interior Design")

    # ── project-showcase
    p = sub.add_parser("project-showcase", help="Generate Project Showcase package")
    p.add_argument("--project", required=True, metavar="NAME")
    p.add_argument("--date", required=True, metavar="YYYY-MM-DD")
    p.add_argument("--project-type", dest="project_type", metavar="TYPE",
                   choices=["Residential", "Commercial", "Renovation", "Construction"],
                   default="Residential")
    p.add_argument("--location", metavar="TEXT")
    p.add_argument("--completed", metavar="PERIOD", help="Completion period, e.g. 'June 2026'")

    # ── holiday
    p = sub.add_parser("holiday", help="Generate Holiday Content package")
    p.add_argument("--name", required=True, metavar="NAME", help="Holiday name")
    p.add_argument("--date", required=True, metavar="YYYY-MM-DD")
    p.add_argument("--message", metavar="TEXT", help="Brand message for the holiday")

    # ── special-announcement
    p = sub.add_parser("special-announcement", help="Generate Special Announcement package")
    p.add_argument("--title", required=True, metavar="TITLE")
    p.add_argument("--date", required=True, metavar="YYYY-MM-DD")
    p.add_argument("--body", metavar="TEXT", help="Announcement body text")
    p.add_argument("--effective", metavar="YYYY-MM-DD", help="Effective date of announcement")

    # ── status
    sp = sub.add_parser("status", help="Manage content status")
    ssp = sp.add_subparsers(dest="status_command")

    sl = ssp.add_parser("list", help="List all tracker entries")
    sl.add_argument("--month", metavar="YYYY-MM", help="Filter by month")
    sl.add_argument("--category", metavar="CAT", help="Filter by category")

    su = ssp.add_parser("update", help="Update status of an entry")
    su.add_argument("--id", required=True, metavar="ID")
    su.add_argument("--to", required=True, metavar="STATUS",
                    choices=VALID_STATUSES)

    # ── schedule
    p = sub.add_parser("schedule", help="Generate monthly content calendar")
    p.add_argument("--month", required=True, metavar="YYYY-MM")

    # ── reminders
    p = sub.add_parser("reminders", help="Generate reminder schedule for a date")
    p.add_argument("--date", required=True, metavar="YYYY-MM-DD")
    p.add_argument("--time", metavar="HH:MM", help="Posting time (default 09:00)")

    return parser


# ──────────────────────────────────────────────────────────── main

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    dispatch = {
        "new-month":           cmd_new_month,
        "design-of-month":     cmd_design_of_month,
        "project-highlights":  cmd_project_highlights,
        "design-showcase":     cmd_design_showcase,
        "project-showcase":    cmd_project_showcase,
        "holiday":             cmd_holiday,
        "special-announcement": cmd_special_announcement,
        "schedule":            cmd_schedule,
        "reminders":           cmd_reminders,
    }

    if args.command == "status":
        if not hasattr(args, "status_command") or args.status_command is None:
            print("Usage: generate.py status list | generate.py status update --id ID --to STATUS")
            sys.exit(1)
        if args.status_command == "list":
            cmd_status_list(args)
        elif args.status_command == "update":
            cmd_status_update(args)
    elif args.command in dispatch:
        dispatch[args.command](args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
