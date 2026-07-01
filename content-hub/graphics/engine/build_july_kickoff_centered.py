#!/usr/bin/env python3
"""One-off build script: July 2026 kickoff, centered 'Happy New Month' variant.

Same source photo as the corner-anchored kickoff graphic, but the greeting
message is the dominant, centered visual element rather than a footer label.
"""
from build_graphics import build

build(
    {
        "type": "spotlight",
        "size": "portrait",
        "layout": "center",
        "logo": "DF",
        "kicker": "NEW MONTH · JULY 2026",
        "image": "assets/Project Pictures/Alcove Home Interior/Alcove Home Feature Wall.png",
        "title": "HAPPY NEW MONTH",
        "meta": "Let's Build It Properly.",
        "footer": "Vollmann Akarakiri",
        "handle": "@dova_futures",
    },
    "2026-07-01-new-month-centered.png",
)
print("Built content-hub/graphics/output/2026-07-01-new-month-centered.png")
