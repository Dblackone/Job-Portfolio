#!/usr/bin/env python3
"""One-off build script for the July 2026 kickoff post (Alcove Homes, Yaba)."""
from build_graphics import build

build(
    {
        "type": "spotlight",
        "size": "portrait",
        "logo": "DF",
        "kicker": "NEW MONTH · JULY 2026",
        "image": "assets/Project Pictures/Alcove Home Interior/Alcove Home Feature Wall.png",
        "title": "ALCOVE HOMES, YABA",
        "meta": "Let's Build It Properly.",
        "footer": "Vollmann Akarakiri",
        "handle": "@dova_futures",
    },
    "2026-07-01-new-month-cover.png",
)
print("Built content-hub/graphics/output/2026-07-01-new-month-cover.png")
