---
name: design-portfolio-pdf
description: >-
  Generate a premium, multi-page A4 PDF portfolio in the "Akarakiri" house style
  (warm off-white + terracotta + Inter typography) from a person's details and
  categorized project images. Use whenever the user wants to create or update a
  professional, construction, architecture, engineering, interior, BIM, or any
  project-specific / discipline-specific PDF portfolio that should look designed
  and self-contained. Produces a print-ready PDF via WeasyPrint with embedded
  fonts and images.
---

# Design Portfolio PDF

Build a polished, print-ready **A4 PDF portfolio** that mirrors a clean editorial
design system (warm off-white, terracotta accent, slate text, Inter typeface).
The output is a fully self-contained PDF — fonts and images are embedded as
base64, so it renders identically anywhere.

This skill captures a proven method: a data-driven Python build script
(`build_portfolio.py`) renders styled HTML/CSS to PDF with **WeasyPrint**, plus a
QA loop that renders each page to an image for visual checking.

## When to use

- "Make me a PDF portfolio / design portfolio / construction portfolio."
- "Create a portfolio for <discipline> (architecture, BIM, interiors, landscape,
  project management, …)."
- "Turn my projects/CV/website into a designed PDF."
- Updating an existing portfolio built with this skill (swap images, add a
  Selected Work spread, change captions, etc.).

## Prerequisites

```bash
pip install weasyprint pillow      # build
pip install pymupdf                # QA: render PDF pages to PNG for inspection
```

Fonts: the six static **Inter** weights ship in `fonts/` (OFL licensed). If
missing, fetch them from the official repo (works where general CDNs are blocked):

```
https://raw.githubusercontent.com/rsms/inter/master/docs/font-files/Inter-Light.woff2
  …-Regular / -Medium / -SemiBold / -Bold / -ExtraBold  → save as inter-{300..800}.woff2
```

## Design system (the house style)

| Token | Value | Use |
|---|---|---|
| `--bg` | `#F5F2EE` | page background (warm off-white) |
| `--accent` | `#B85C38` | terracotta — labels, bars, icons, links |
| `--accent-d` | `#9e4f30` | hover/darker accent |
| `--text` | `#4A4F5C` | slate body text |
| `--dark` | `#2C2C2C` | headings + dark sections |
| `--white` `--warm` `--light` `--border` | `#FFF` `#E8E4DF` `#F0DDD8` `#D1CBC6` | surfaces |

- **Typeface:** Inter (weights 300–800), embedded.
- **Page:** A4, `@page{size:A4;margin:0}`. Each section is a `.sheet`
  (`width:210mm; height:297mm; padding:15mm 16mm 14mm; page-break-after:always`).
  Use a **fixed** `height:297mm` (not `min-height`) so absolutely-positioned page
  footers anchor to the true page bottom.
- **Color in print:** set `print-color-adjust:exact` so backgrounds/dark sections
  render.
- **Glyphs:** Inter includes `₦` (U+20A6) and `→` (U+2192). It does **not** include
  `⬡ ◈ ⬟` — use these instead for card icons: `◆ ◇ □ ▲ ■ ● ★`.

### Reusable layout primitives (CSS classes in the engine)

- `.sheet` / `.sheet.dark` / `.sheet.white` — a full page.
- `.s-head` — section kicker label + `h2` + sub.
- `.img-band` — full-width image band with gradient caption (great for filling
  empty space on the cover or any content page so it engages immediately).
- `.fig.big` / `.fig.big.contain` / `.fig.half` — Selected-Work hero + supporting
  images, with caption bar (`.cap .t` title, `.cap .m` uppercase accent tag).
  Use `.contain` to letterbox a square hero instead of cropping it.
- `.other-grid` + `.tile` — a 3-column gallery of small captioned tiles
  ("Other Projects"), no hero.
- `.cards` / `.sw-grid` / `.tl` (timeline) / `.skill-group` / `.stat-grid` /
  `.edu-grid` / `.cdetails` — about, skills, experience, expertise, contact.

## Section / page catalog

A typical portfolio orders sheets like this (all optional & repeatable):

1. **Cover** — kicker, stacked headline (one word per line, color one accent),
   sub, bullet points, profile card (photo, name, role, location, 3 stats, software
   pills, availability dot), contact row. Optional `cover_band` image.
2. **About** — profile paragraphs + stat tiles (left), competency `skill-group`s
   (right), education cards. Optional band.
3. **Software / Skills (dark)** — 6 cards + discipline tags.
4. **Experience** — timeline with terracotta dots + a 4-up metrics strip.
5. **Areas of Expertise** — discipline cards (+ optional band to fill space).
6…N. **Selected Work** — one spread per project: title, sub, hero + two
   supporting images with captions/tags.
- **Other Projects** — gallery grid of extra renders (no hero).
- **Contact (dark)** — CTA, buttons, contact details grid, footer line.

## Image specs (what to supply)

| Slot | On-page size | Aspect | Supply ≥ |
|---|---|---|---|
| Profile photo | card, ~60mm tall | portrait/any | 760px (transparent PNG ok) |
| Cover / section **band** | 178 × ~63mm | **~3:1 panoramic** | 1700 × 580 px |
| Selected-Work **hero** | 178 × 96mm | **~16:9** | 1600 × 900 px |
| Selected-Work **supporting** | ~87 × 62mm | ~3:2 | 1100px wide |
| Gallery **tile** | ~57 × 44mm | cover-cropped ~1.3:1 | 860–1000px wide |

Images use `object-fit:cover` (center-crop). For a square hero, set
`hero_contain: true` to letterbox it fully. The build auto-downscales to ~1280px
(bands/heroes ~1600px, tiles ~860px) and recompresses — **always supply the
largest originals you have.**

## Workflow

1. **Gather content** — name, role, location, tagline, bio, stats, experience,
   skills/competencies, education, services, contact (incl. real LinkedIn URL).
2. **Collect & curate images** per section. **View candidates first** (don't embed
   blank plans/white models unless intentional); pick the strongest hero + 2
   supporting per Selected-Work spread, and a varied set for the gallery.
3. **Fill `CONFIG`** in `build_portfolio.py` (or import the module and pass your
   own dict). Set `base_dir` to where the images live.
4. **Build:** `python3 build_portfolio.py` → writes the PDF.
5. **QA (important):** render every page to PNG and inspect for overflow,
   misalignment, wrong crops, and footer numbers:
   ```python
   import fitz
   d = fitz.open("portfolio.pdf")
   for i,p in enumerate(d): p.get_pixmap(dpi=120).save(f"/tmp/qa/p{i+1}.png")
   ```
   Also extract text (`page.get_text()`) to proofread copy and confirm clickable
   links (`page.get_links()`).
6. **Iterate** — swap images/captions and rebuild. Keep originals committed so the
   build is reproducible.
7. **(Optional) Wire into a website** — link the PDF from a "Download Portfolio"
   button.

## How to run

```bash
# 1. copy this skill folder next to your project (or work in place)
# 2. edit CONFIG at the top of build_portfolio.py (or write your own config)
# 3. drop images where CONFIG points (relative to base_dir)
python3 build_portfolio.py            # -> CONFIG["output"]
```

`build_portfolio.py` exposes `build(config, base_dir=".", out=...)` so you can
drive it programmatically for several portfolios from one content source.

## Gotchas / tips (learned the hard way)

- **Footer pinning:** use fixed `.sheet{height:297mm}`; with `min-height` the
  absolute footer floats to the middle of short pages.
- **Page count:** every `.sheet` is exactly one page; keep content within ~268mm
  of usable height or it spills to a blank page. QA the page count after building.
- **Fonts distinct weights:** Google Fonts' modern endpoint may serve one variable
  file for all weights — use the per-weight static woff2 from `rsms/inter`.
- **Self-contained output:** embed fonts and images as base64 data URIs.
- **Links:** wrap contact details in `<a href>` and add `a{color:inherit;
  text-decoration:none}` so they're clickable but look like plain text.
- **Discipline variants:** for a construction portfolio lead with site/BIM work; for
  architecture lead with visualizations; for interiors lead with renders — same
  engine, just reorder `selected_work` and swap the headline/skills.

See `build_portfolio.py` for the engine and a worked `CONFIG` example.
