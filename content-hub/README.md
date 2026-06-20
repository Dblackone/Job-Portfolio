# Akarakiri Content Hub

The content engine for **Vollmann Olamide Akarakiri** — CEO & Managing Director,
Dova Futures Limited. Multidisciplinary construction professional, BIM specialist,
architectural designer, and site engineer.

This hub produces daily social-media content for **Instagram, LinkedIn, TikTok,
Twitter/X, and WhatsApp**, in the same **Akarakiri house style** as the portfolio
in this repository (warm off-white · terracotta · slate · Inter). Every piece is
built to grow **engagement and exposure** for Vollmann and his work.

---

## What this hub produces

For each scheduled day, the hub delivers a **content package** containing:

1. **Text package** — hook, full caption per platform, hashtags, CTA, and the exact
   project image/asset to attach.
2. **Finished branded graphic(s)** — ready-to-post cards/carousels rendered in the
   Akarakiri style (square 1080×1080, portrait 1080×1350, story/reel 1080×1920).
3. **Short-form video script** (for Reels/TikTok days) — hook, shot list, on-screen
   text, voiceover, and audio direction.

---

## Folder map

| Folder | What's inside |
|---|---|
| `brand/` | Voice & style guide, per-platform format specs |
| `system/` | Content pillars, weekly rotation, hashtag & CTA bank, ops workflow |
| `templates/` | Reusable templates: post package, carousel, video script |
| `calendar/` | The rolling content calendar (30-day batches) |
| `posts/` | Fully-written post packages, one file per day |
| `graphics/engine/` | `build_graphics.py` — renders branded cards (HTML→PDF→PNG) |
| `graphics/output/` | Generated PNG graphics, ready to post |

---

## How a day flows

1. Look up the day in `calendar/` → it names the **pillar**, **topic**, **format**,
   and **source asset**.
2. The matching package in `posts/` has the finished captions + script.
3. The graphic for that day is in `graphics/output/` (or rebuild with the engine).
4. Post per `brand/platform-specs.md`; repurpose the one core idea across platforms.

The principle: **one strong idea per day, repurposed per platform** — not five
disconnected posts. This keeps output daily, on-brand, and sustainable.

---

## Producing more / fulfilling "orders"

To generate a new card: edit `CONFIG` in `graphics/engine/build_graphics.py`
(or import `build()`), then run `python3 build_graphics.py`. To extend the
calendar, copy the rotation in `system/content-pillars.md` forward and add
packages in `posts/`. The live queue and status board live in **Notion**
(see `system/workflow.md`).
