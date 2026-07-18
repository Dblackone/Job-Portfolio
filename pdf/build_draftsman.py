#!/usr/bin/env python3
"""Draftsman / 2D technical drawings portfolio — black & white with green accent.

Drives the design-portfolio-pdf skill engine with a recolored design system:
white pages, near-black ink, DOVA green (#1C4636) as the single accent —
in the style of a minimal architectural process portfolio.

Run from the repo root:  python3 pdf/build_draftsman.py
"""

import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENGINE = os.path.join(ROOT, ".claude", "skills", "design-portfolio-pdf",
                      "build_portfolio.py")

spec = importlib.util.spec_from_file_location("portfolio_engine", ENGINE)
eng = importlib.util.module_from_spec(spec)
sys.modules["portfolio_engine"] = eng
spec.loader.exec_module(eng)

# ── recolor the house style: white / near-black / DOVA green ──
RECOLOR = {
    "#F5F2EE": "#FFFFFF",   # page background -> white
    "#B85C38": "#1C4636",   # accent terracotta -> DOVA green
    "#9e4f30": "#143528",   # darker accent
    "#4A4F5C": "#3D4340",   # body text -> neutral graphite
    "#2C2C2C": "#141915",   # dark sheets -> near-black green
    "#E8E4DF": "#F0F0EE",   # warm surface -> light grey
    "#F0DDD8": "#E3EBE6",   # tinted surface -> pale green
    "#D1CBC6": "#D8DAD6",   # borders
}
for old, new in RECOLOR.items():
    eng.CSS = eng.CSS.replace(old, new)
eng.CSS = eng.CSS.replace("184,92,56", "28,70,54")

# Deep green reads poorly on the near-black sheets — lift accent text there.
eng.CSS += """
.dark .label, .dark .sw .lv{ color:#8FBFAA; }
.dark .accent-bar{ background:#8FBFAA; }
.dark .disc span{ color:#A8CBBB; background:rgba(143,191,170,.12);
  border:1px solid rgba(143,191,170,.35); }
"""

PICS = "assets/Project Pictures"

CONFIG = {
    "output": os.path.join(ROOT, "portfolio",
                           "Vollmann_Akarakiri_Draftsman_2D_Portfolio.pdf"),
    "footer_text": "Vollmann Olamide Akarakiri · Draftsman",
    "cover": {
        "name": "Vollmann Akarakiri", "brand": "Vollmann Akarakiri",
        "initial": "V",
        "role": "Draftsman · Technical Designer",
        "location": "Lagos, Nigeria",
        "portfolio_tag": "Drafting & 2D Plans Portfolio · 2026",
        "kicker": "Draftsman · AutoCAD & Revit · Lagos, Nigeria",
        "headline": [("Draw.", None), ("Detail.", "accent"),
                     ("Document.", None), ("Deliver.", "muted")],
        "hero_sub": "Accurate technical drawings, working drawings and "
                    "construction documentation — from architectural and "
                    "engineering specifications to buildable sheets on site.",
        "hero_points": [
            "Full documentation packages — plans, sections, details, schedules",
            "Expert AutoCAD · advanced Revit, Dynamo and Navisworks",
            "Detailing packages produced for 10+ residential and commercial buildings",
            "Site measurements and drawing verification across 20+ project sites",
        ],
        "cover_stats": [("30+", "BIM models"), ("50+", "Drawing sets"),
                        ("5+", "Years")],
        "pills": ["AutoCAD", "Revit", "Dynamo", "Navisworks"],
        "availability": "Available for drafting roles — Lagos & remote",
        "contact": {
            "Phone": "+234 816 367 5439",
            "Email": "vollmannakarakiri0@gmail.com",
            "Location": "Lagos, Nigeria",
            "LinkedIn": ("/in/vollmannakarakiri",
                         "https://www.linkedin.com/in/vollmannakarakiri"),
        },
    },
    "cover_band": {
        "image": f"{PICS}/Ado Hall of Worship/Screenshot 2026-05-10 091613.png",
        "caption": "Hall of Worship, Ado — Structural Frame, Hidden-Line Axonometric",
    },
    "about": {
        "label": "Professional Profile",
        "heading": "The Draftsman Behind the Drawings",
        "paragraphs": [
            "Vollmann Olamide Akarakiri is a detail-oriented draftsman and "
            "technical designer with over five years preparing technical "
            "drawings, working drawings and construction documentation for "
            "residential, commercial and mixed-use projects across Nigeria.",
            "His drawings are grounded in site reality: he conducts "
            "measurements, verifies dimensions on site and coordinates with "
            "architects, structural engineers and contractors so that every "
            "sheet issued is accurate, compliant and buildable.",
        ],
        "stats": [("30+", "BIM models produced"), ("10+", "Detailing packages"),
                  ("20+", "Sites measured & verified"), ("5+", "Years drafting")],
        "competencies": [
            {"title": "Drafting & Documentation",
             "items": ["Working Drawings", "Floor Plans & Sections",
                       "Construction Details", "Setting-Out Drawings",
                       "Drawing Registers", "Title Blocks & Standards"]},
            {"title": "Coordination & Compliance",
             "items": ["Architectural & Structural Drawing Interpretation",
                       "Building Regulations", "Clash Detection",
                       "Site Measurements", "Quantity Take-Offs"]},
        ],
        "education": [
            {"degree": "MSc, Construction Engineering Management",
             "institution": "University of East London",
             "period": "Sep 2024 – Present"},
            {"degree": "BSc, Building Technology",
             "institution": "Federal University of Technology, Akure",
             "period": "2014 – 2019"},
        ],
    },
    "skills": {
        "label": "Technical Expertise", "heading": "Drafting Software & Skills",
        "sub": "Industry-standard tools deployed from survey sketch to issued sheet.",
        "cards": [
            {"name": "AutoCAD", "level": "Expert — 2D Technical Drawing",
             "desc": "2D technical drawings, site plans, detailed construction "
                     "and working drawings, and full detailing packages for "
                     "10+ residential and commercial properties."},
            {"name": "Autodesk Revit", "level": "Advanced — BIM Documentation",
             "desc": "Coordinated models and documentation sheets — plans, "
                     "sections, elevations, schedules — for 30+ office, "
                     "residential and interior projects."},
            {"name": "Dynamo", "level": "Advanced — Automation",
             "desc": "Parametric scripts that automate repetitive drafting and "
                     "sheet production, cutting documentation time on large "
                     "programmes."},
            {"name": "Navisworks", "level": "Proficient — Coordination",
             "desc": "Multi-discipline model coordination and clash detection "
                     "so drawing sets agree before they reach site."},
            {"name": "MS Project", "level": "Proficient — Programme Support",
             "desc": "Drawing-issue schedules and milestone tracking aligned "
                     "with construction programmes."},
            {"name": "Excel & Office", "level": "Advanced — Registers & Take-Offs",
             "desc": "Drawing registers, quantity take-offs, and progress "
                     "reporting across concurrent projects."},
        ],
        "tags": ["Working Drawings", "Shop Drawing Support", "Construction Details",
                 "Site Plans", "Interior Elevations", "Structural Coordination",
                 "Regulatory Compliance"],
    },
    "experience": {
        "label": "Career History", "heading": "Professional Experience",
        "sub": "Five-plus years of progressive drafting, documentation and "
               "site-verification responsibility.",
        "roles": [
            {"period": "Aug 2021 – Feb 2026",
             "role": "Project Manager / Engineering Lead",
             "company": "Nu-Avenue Company Resources", "current": True,
             "bullets": [
                 "Prepared and reviewed technical drawings and construction "
                 "documentation for projects exceeding ₦350M in value.",
                 "Produced BIM models and drawing sets in Revit and AutoCAD "
                 "for 30+ office, 10+ residential and 10+ interior projects.",
                 "Conducted site visits and measurements across 20+ sites to "
                 "verify dimensions and resolve drawing discrepancies.",
                 "Prevented rework worth over ₦10M by catching drawing errors "
                 "and specification conflicts before construction."]},
            {"period": "Jun 2020 – Aug 2021",
             "role": "Site Engineer / Assistant Technical Designer",
             "company": "Nature's Beauty Construction",
             "bullets": [
                 "Produced full detailing packages for 10+ residential "
                 "properties — construction details, setting-out drawings and "
                 "material specifications.",
                 "Supervised works on site, ensuring construction matched the "
                 "issued drawings and design standards."]},
            {"period": "Dec 2019 – Apr 2020", "role": "Site Supervisor",
             "company": "Lego Construction Company",
             "bullets": [
                 "Prepared project plans, contract documents, drawings and "
                 "schedules; coordinated design and site teams."]},
            {"period": "Aug 2017 – Dec 2017",
             "role": "Architecture & Planning Intern",
             "company": "Danzinger Nigeria Ltd",
             "bullets": [
                 "Assisted drafting, BIM updates and construction "
                 "documentation on consulting engagements exceeding ₦10M."]},
        ],
        "metrics": [("50+", "Drawing sets issued"), ("30+", "BIM models"),
                    ("10+", "Detailing packages"), ("₦10M+", "Rework prevented")],
    },
    "selected_work": [
        {"title": "Hall of Worship, Ado-Ekiti",
         "sub": "Full construction documentation — dimensioned floor plans on "
                "titled sheets, coordinated structural model and site layout.",
         "hero": (f"{PICS}/Ado Hall of Worship/Screenshot 2026-05-16 091207.png",
                  "Proposed Floor Plan — Dimensioned Documentation Sheet, 1:60",
                  "AutoCAD · Sheet A106"),
         "hero_contain": True,
         "supporting": [
             (f"{PICS}/Ado Hall of Worship/Screenshot 2026-05-10 091613.png",
              "Structural Frame — Hidden-Line Axonometric", "Revit"),
             (f"{PICS}/Ado Hall of Worship/Screenshot 2026-05-16 091805.png",
              "Site Layout — Massing & Landscape", "Site Plan"),
         ]},
        {"title": "Residential Model Studies",
         "sub": "White-model and hidden-line studies that carry a design from "
                "massing to documented, buildable geometry.",
         "hero": (f"{PICS}/Concept schema projects/BIG SCHEMA RAW 1.jpg",
                  "Private Residence — Hidden-Line Perspective Study", "Revit"),
         "supporting": [
             (f"{PICS}/Concept schema projects/3 BEDROOM TRERACE WITH PENT HOUSE - RAW 1.jpg",
              "Terrace with Penthouse — Sloped-Site Model", "Massing"),
             (f"{PICS}/Ikotun Apartments/ikotun-structure.jpg",
              "6-Flat Block, Ikotun — Level Datum Study", "Levels"),
         ]},
        {"title": "Linework & Joinery Details",
         "sub": "From building-scale hidden-line views to millimetre-level "
                "interior joinery elevations.",
         "hero": (f"{PICS}/Renderings of Interior Residences (Kitchens)/tv-entertainment-unit-elevation.png",
                  "TV & Entertainment Wall — Joinery Elevation", "Interior Detail"),
         "hero_contain": True,
         "supporting": [
             (f"{PICS}/Other Renders/Event Hall Massing.png",
              "Event Hall — Hidden-Line Axonometric", "Linework"),
             (f"{PICS}/Concept schema projects/LOFT RAW 1.jpg",
              "Loft Outbuilding — Hidden-Line Study", "Linework"),
         ]},
    ],
    "gallery": {
        "label": "More Work", "heading": "Further Drawing Studies",
        "sub": "Additional hidden-line, massing and documentation studies from "
               "across the portfolio.",
        "tiles": [
            (f"{PICS}/Other Renders/Building Model.png",
             "Two-Storey Office", "Hidden Line"),
            (f"{PICS}/Ado Hall of Worship/Screenshot 2026-05-16 091805.png",
             "Ado Site Layout", "Site Plan"),
            (f"{PICS}/Concept schema projects/LOFT RAW 1.jpg",
             "Loft Outbuilding", "Linework"),
            (f"{PICS}/Other Renders/Event Hall Massing.png",
             "Event Hall", "Linework"),
            (f"{PICS}/Ikotun Apartments/ikotun-structure.jpg",
             "6-Flat Block, Ikotun", "Levels"),
            (f"{PICS}/Concept schema projects/BIG SCHEMA RAW 1.jpg",
             "Private Residence", "Hidden Line"),
        ],
    },
    "contact": {
        "label": "Get In Touch", "heading": "Need Drawings You Can Build From?",
        "lead": "Accurate sheets, coordinated details and documentation that "
                "stands up on site — let's talk about your next project.",
        "buttons": [
            {"label": "Send an Email",
             "href": "mailto:vollmannakarakiri0@gmail.com", "primary": True},
            {"label": "LinkedIn Profile",
             "href": "https://www.linkedin.com/in/vollmannakarakiri"},
        ],
        "details": {
            "Phone": "+234 816 367 5439",
            "Email": "vollmannakarakiri0@gmail.com",
            "Location": "Lagos, Nigeria",
            "LinkedIn": ("linkedin.com/in/vollmannakarakiri",
                         "https://www.linkedin.com/in/vollmannakarakiri"),
        },
        "footer": "Vollmann Olamide Akarakiri · Draw. Detail. Document. Deliver.",
    },
}

if __name__ == "__main__":
    eng.build(CONFIG, base_dir=ROOT,
              font_dir=os.path.join(ROOT, "pdf", "fonts"))
