# PDF Portfolio

A print-ready PDF portfolio for Vollmann Olamide Akarakiri, generated from the
same design system as the web portfolio (`/index.html`):

* **Palette** — Warm off-white `#F5F2EE` · Terracotta `#B85C38` · Slate `#4A4F5C`
* **Type** — Inter (bundled in `fonts/` as static `.woff2` weights)
* **Output** — `../assets/vollmann-akarakiri-portfolio.pdf` (12 × A4 pages)

## Contents

1. Cover — headline, profile card, key stats, contact
2. Professional profile, core competencies & education
3. Software & BIM skills (Revit, Dynamo, AutoCAD, Navisworks, MS Project, Excel)
4. Professional experience timeline
5. Areas of expertise
6. Selected work 01 — Hall of Worship, Ado
7. Selected work 02 — The Hillside Project (concept)
8. Selected work 03 — Landscape & Site Development
9. Selected work 04 — 4-Bedroom Family House, Uselu
10. Selected work 05 — 6-Flat Apartment Block, Ikotun
11. Other projects — gallery of additional work
12. Contact

Project imagery is pulled from `../assets/Project Pictures/` and optimised
(resized + recompressed) in-memory at build time, so no extra image files are
added to the repository — only the final PDF.

## Rebuild

```bash
pip install weasyprint pillow
python3 pdf/build.py
```

Fonts and images are embedded as base64 data URIs, so the resulting PDF is fully
self-contained.
