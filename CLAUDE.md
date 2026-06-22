# DOVA Futures — Project Rules

## Content Kit — Mandatory Reference

**For any task involving content, posts, captions, graphics, social media, or the content-hub automation system:**

Read `project/Content Kit.dc.html` before generating any output. This file is the single source of truth for all brand and content decisions. The 15 AI generation rules in Section 11 are absolute — no exceptions.

> Quick path: `/home/user/Job-Portfolio/project/Content Kit.dc.html`

---

## Binding Brand Rules (from Content Kit §11)

These apply to every caption, graphic brief, template, or schedule produced in this repo:

| Rule | Requirement |
|---|---|
| RULE 01 — VOICE | Confident, precise, premium. Never casual or salesy. Master-builder tone. |
| RULE 02 — NO EMOJI | Zero emoji anywhere — captions, graphics, CTAs, templates. |
| RULE 03 — CASING | Headlines: Bebas Neue ALL-CAPS. Eyebrows: UPPERCASE Inter. Body: sentence case. |
| RULE 04 — CURRENCY | Always ₦ symbol — never "NGN" or "Naira" before a number. |
| RULE 05 — REAL METRICS | No invented statistics. Approved benchmarks: 20+ concurrent sites · ₦350M+ project value · ₦10M+ client savings. |
| RULE 06 — COLOR | Primary: `#1C4636` green · Light surface: `#F5EFE8` cream · Accent: `#B85C38` clay (max 10%). Never purple, blue, or pink. |
| RULE 07 — TYPOGRAPHY | Display: Bebas Neue only. Body/UI: Inter only. No substitutes. |
| RULE 08 — IMAGERY | Real DOVA project photos only. No stock. No AI-generated photography. |
| RULE 09 — LOGO | White logo on dark. Standard logo on cream. Never recolor or distort. |
| RULE 10 — HOOK FIRST | Every caption starts with a hook. Never open with "We are" or "DOVA Futures is." |
| RULE 11 — CTA REQUIRED | Every caption ends with a CTA from the CTA Library (Content Kit §08). |
| RULE 12 — HASHTAGS | Instagram: 15–25 after two line breaks. LinkedIn: 5–8 at end. X: 1–3 max. Never mid-copy. |
| RULE 13 — PLATFORM TONE | IG: aspirational · LinkedIn: authoritative · X: concise · WhatsApp: direct · Facebook: narrative · Threads: casual but credible. |
| RULE 14 — PILLAR BALANCE | Design Inspiration 25% · Project Progress 20% · Showcase 20% · Educational 20% · Company 10% · Seasonal 5%. |
| RULE 15 — QUALITY | One exceptional post beats three mediocre ones. Flag any element that cannot be produced from the Content Kit alone. |

---

## Key Brand Reference

**Company:** DOVA Futures Limited  
**Tagline:** Rethink the Future  
**Headline pairing:** Designed With Intent. Built With Precision.  
**Master CTA:** Let's Build It Properly.  
**Contact:** info@dovafutures.com · +234 816 367 5439 · dovafutures.com  
**Social handle:** @dova_futures

**Preferred words:** integrated · precision · craftsmanship · engineered · handover · buildability · seamless · future-ready · transparent · landmark · coordinated · sustainable  
**Prohibited words:** cheap · affordable · discount · quick · easy · amazing · awesome · we're the best · unbeatable

---

## Content System Files

| File | Purpose |
|---|---|
| `project/Content Kit.dc.html` | Brand + content source of truth (read this first) |
| `project/Post Wireframes.dc.html` | Visual post layout wireframes |
| `content-hub/generate.py` | CLI for generating content packages |
| `content-hub/system/tracker.json` | Status tracker (draft → approved → scheduled → posted) |
| `content-hub/templates/category/` | 7 post templates (fill with `{{FIELD}}` replacement) |
| `content-hub/graphics/engine/build_graphics.py` | Social card renderer |
| `content-hub/system/hashtag-bank.md` | Hashtag reference |
| `content-hub/index.html` | Content hub dashboard |

---

## Development Branch

Active feature work goes on: `claude/social-media-automation-q7k2h0`
