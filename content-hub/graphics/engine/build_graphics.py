#!/usr/bin/env python3
"""
Akarakiri Content Hub — Social Graphics Engine
==============================================

Renders branded social-media cards in the Akarakiri house style
(warm off-white + terracotta + Inter), matching the portfolio in this repo.

Pipeline:  styled HTML  --WeasyPrint-->  single-page PDF (exact px page)  --PyMuPDF-->  PNG

Why this pipeline: it's self-contained (fonts embedded as base64), reproducible,
and uses the same toolchain as the design-portfolio-pdf skill already in this repo.

Card types
----------
- tip / explainer / insight : kicker + headline + bullets + footer   (any size)
- quote                     : big statement card                     (any size)
- spotlight                 : full-bleed image + gradient + caption   (any size)
- cta                       : closing call-to-action card             (any size)
- carousel                  : a list of slides -> one PNG per slide   (4:5)
- monthly-theme             : new-month opener, month-number texture  (portrait)
- holiday                   : warm greeting card, light background    (any size)
- announcement              : dark high-impact card, badge + rule     (portrait)

Sizes (px):  square 1080x1080 · portrait 1080x1350 · story 1080x1920

Usage
-----
    python3 build_graphics.py            # builds the SAMPLES at the bottom
    # or import and drive it:
    from build_graphics import build
    build(card_dict, out="output/my-card.png")

Requires:  pip install weasyprint pymupdf pillow
Fonts:     ../../../plugins/design-portfolio/skills/design-portfolio-pdf/fonts/inter-*.woff2
"""

from __future__ import annotations
import base64
import os
import mimetypes
from pathlib import Path

from weasyprint import HTML
import fitz  # PyMuPDF

# ----------------------------------------------------------------------------- paths
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]                       # .../Job-Portfolio
FONT_DIR = REPO / "plugins/design-portfolio/skills/design-portfolio-pdf/fonts"
OUT_DIR = HERE.parent / "output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------------------------- palette
PALETTE = {
    "bg":      "#F5F2EE",
    "accent":  "#B85C38",
    "accentD": "#9E4F30",
    "text":    "#4A4F5C",
    "dark":    "#2C2C2C",
    "white":   "#FFFFFF",
    "warm":    "#E8E4DF",
    "light":   "#F0DDD8",
    "border":  "#D1CBC6",
}

SIZES = {                # (width_px, height_px)
    "square":   (1080, 1080),
    "portrait": (1080, 1350),
    "story":    (1080, 1920),
}

FONT_WEIGHTS = {300: "inter-300.woff2", 400: "inter-400.woff2", 500: "inter-500.woff2",
                600: "inter-600.woff2", 700: "inter-700.woff2", 800: "inter-800.woff2"}

DEFAULT_FOOTER = "Vollmann Akarakiri · BIM · Architecture · Site"
DEFAULT_HANDLE = "@dova_futures"  # Instagram + TikTok confirmed


# ----------------------------------------------------------------------------- helpers
def _data_uri(path: Path) -> str:
    mime, _ = mimetypes.guess_type(str(path))
    mime = mime or "application/octet-stream"
    b64 = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{b64}"


def _font_face_css() -> str:
    faces = []
    for weight, fname in FONT_WEIGHTS.items():
        fp = FONT_DIR / fname
        if fp.exists():
            faces.append(
                "@font-face{font-family:'Inter';font-style:normal;"
                f"font-weight:{weight};src:url('{_data_uri(fp)}') format('woff2');}}"
            )
    return "\n".join(faces)


def _img_uri(img: str | None) -> str | None:
    if not img:
        return None
    p = Path(img)
    if not p.is_absolute():
        # resolve relative to repo root so "assets/..." works from anywhere
        p = (REPO / img)
    if not p.exists():
        raise FileNotFoundError(f"Image not found: {p}")
    return _data_uri(p)


# ----------------------------------------------------------------------------- CSS
def _base_css(w: int, h: int) -> str:
    # 1px == 1px: set the @page to the pixel size and use px throughout.
    return f"""
    {_font_face_css()}
    @page {{ size: {w}px {h}px; margin: 0; }}
    * {{ margin:0; padding:0; box-sizing:border-box; -weasy-print-color-adjust:exact;
         print-color-adjust:exact; }}
    html,body {{ width:{w}px; height:{h}px; font-family:'Inter',sans-serif;
                 color:{PALETTE['text']}; background:{PALETTE['bg']}; }}
    .card {{ position:relative; width:{w}px; height:{h}px; overflow:hidden; }}

    /* logo + kicker */
    .topbar {{ display:flex; align-items:center; gap:20px; }}
    .logo {{ width:64px; height:64px; border-radius:12px; background:{PALETTE['accent']};
             color:#fff; font-weight:800; font-size:26px; letter-spacing:-1px;
             display:flex; align-items:center; justify-content:center; flex-shrink:0; }}
    .kicker {{ font-weight:600; font-size:24px; letter-spacing:0.22em;
               text-transform:uppercase; color:{PALETTE['accent']}; }}

    h1.head {{ color:{PALETTE['dark']}; font-weight:800; line-height:1.08;
               letter-spacing:-0.02em; }}
    .accent {{ color:{PALETTE['accent']}; }}
    .sub {{ color:{PALETTE['text']}; font-weight:400; line-height:1.5; }}

    .rule {{ height:6px; width:96px; background:{PALETTE['accent']}; border-radius:3px; }}

    ul.bullets {{ list-style:none; display:flex; flex-direction:column; }}
    ul.bullets li {{ position:relative; color:{PALETTE['dark']}; font-weight:500;
                     line-height:1.4; }}
    ul.bullets li .num {{ color:{PALETTE['accent']}; font-weight:800; }}

    .footer {{ position:absolute; left:0; right:0; bottom:0;
               display:flex; align-items:center; justify-content:space-between; }}
    .footer .name {{ color:{PALETTE['text']}; font-weight:500; }}
    .footer .handle {{ color:{PALETTE['accent']}; font-weight:600; }}

    .dot {{ width:10px; height:10px; border-radius:50%; background:{PALETTE['accent']};
            display:inline-block; }}
    """


# ----------------------------------------------------------------------------- card renderers
def _topbar(kicker: str, fs_logo=26, fs_kick=24, logo="VA") -> str:
    return (f'<div class="topbar"><div class="logo" style="font-size:{fs_logo}px">{logo}</div>'
            f'<div class="kicker" style="font-size:{fs_kick}px">{kicker}</div></div>')


def _footer(card: dict, w: int) -> str:
    name = card.get("footer", DEFAULT_FOOTER)
    handle = card.get("handle", DEFAULT_HANDLE)
    return (f'<div class="footer" style="padding:0 {int(w*0.07)}px {int(w*0.06)}px;">'
            f'<span class="name" style="font-size:22px">{name}</span>'
            f'<span class="handle" style="font-size:22px">{handle}</span></div>')


def _html_text_card(card: dict, w: int, h: int) -> str:
    """tip / explainer / insight / quote / cta — text-forward cards."""
    pad = int(w * 0.085)
    is_quote = card["type"] == "quote"
    is_cta = card["type"] == "cta"
    dark = card.get("dark", is_cta)             # CTA defaults to dark card
    bg = PALETTE["dark"] if dark else PALETTE["bg"]
    head_color = PALETTE["white"] if dark else PALETTE["dark"]
    sub_color = "#C9C6C2" if dark else PALETTE["text"]

    head_fs = card.get("head_size", 78 if not is_quote else 64)
    head = card.get("headline", "")
    sub = card.get("sub", "")
    bullets = card.get("bullets", [])

    bullets_html = ""
    if bullets:
        items = ""
        for i, b in enumerate(bullets, 1):
            numbered = card.get("numbered", True)
            lead = f'<span class="num">{i:02d}</span>&nbsp;&nbsp;' if numbered else '<span class="num">—</span>&nbsp;&nbsp;'
            items += f'<li style="font-size:34px;margin-bottom:26px;color:{head_color}">{lead}{b}</li>'
        bullets_html = f'<ul class="bullets" style="margin-top:46px">{items}</ul>'

    quote_mark = ('<div style="font-size:160px;line-height:0.6;color:%s;font-weight:800;'
                  'margin-bottom:10px">&ldquo;</div>' % PALETTE["accent"]) if is_quote else ""

    sub_html = f'<p class="sub" style="font-size:32px;margin-top:30px;color:{sub_color};max-width:84%">{sub}</p>' if sub else ""

    cta_btn = ""
    if is_cta and card.get("button"):
        cta_btn = (f'<div style="margin-top:48px;display:inline-block;background:{PALETTE["accent"]};'
                   f'color:#fff;font-weight:700;font-size:30px;padding:22px 44px;border-radius:10px">'
                   f'{card["button"]}</div>')

    return f"""
    <div class="card" style="background:{bg}">
      <div style="padding:{pad}px {pad}px 0;">
        {_topbar(card.get('kicker','AKARAKIRI'))}
        <div class="rule" style="margin:{int(h*0.05)}px 0 36px;"></div>
        {quote_mark}
        <h1 class="head" style="font-size:{head_fs}px;color:{head_color};max-width:92%">{head}</h1>
        {sub_html}
        {bullets_html}
        {cta_btn}
      </div>
      {_footer(card, w)}
    </div>
    """


def _html_spotlight_card(card: dict, w: int, h: int) -> str:
    """Full-bleed image with gradient + caption. type: spotlight."""
    uri = _img_uri(card["image"])
    pad = int(w * 0.07)
    kicker = card.get("kicker", "PROJECT SPOTLIGHT")
    title = card.get("title", "")
    meta = card.get("meta", "")
    return f"""
    <div class="card" style="background:{PALETTE['dark']}">
      <img src="{uri}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
      <div style="position:absolute;inset:0;background:linear-gradient(180deg,
           rgba(44,44,44,0.55) 0%, rgba(44,44,44,0.05) 32%, rgba(44,44,44,0.1) 55%,
           rgba(44,44,44,0.85) 100%);"></div>
      <div style="position:absolute;top:{pad}px;left:{pad}px;right:{pad}px;">
        {_topbar(kicker, logo=card.get('logo','VA'))}
      </div>
      <div style="position:absolute;left:{pad}px;right:{pad}px;bottom:{int(h*0.085)}px;">
        <div class="rule" style="margin-bottom:28px;"></div>
        <h1 class="head" style="font-size:{card.get('head_size',72)}px;color:#fff;max-width:94%">{title}</h1>
        <p class="sub" style="font-size:28px;color:#EDEAE6;margin-top:18px">{meta}</p>
      </div>
      <div class="footer" style="padding:0 {pad}px {int(h*0.035)}px;">
        <span class="name" style="font-size:22px;color:#EDEAE6">{card.get('footer', DEFAULT_FOOTER)}</span>
        <span class="handle" style="font-size:22px">{card.get('handle', DEFAULT_HANDLE)}</span>
      </div>
    </div>
    """


def _html_monthly_theme_card(card: dict, w: int, h: int) -> str:
    """New Month opener — large typographic card with month number as background texture."""
    pad = int(w * 0.085)
    month_num = card.get("month_num", "07")
    month_name = card.get("month_name", "JULY")
    year = card.get("year", "2026")
    theme = card.get("headline", "")
    sub = card.get("sub", "")
    sub_html = (f'<p style="font-size:30px;color:#C9C6C2;margin-top:32px;'
                f'font-weight:400;line-height:1.5;max-width:82%">{sub}</p>') if sub else ""
    return f"""
    <div class="card" style="background:{PALETTE['dark']};overflow:hidden">
      <div style="position:absolute;font-size:{int(w * 1.1)}px;font-weight:800;
                  color:{PALETTE['accent']};opacity:0.07;
                  top:50%;left:50%;transform:translate(-50%,-45%);
                  line-height:1;letter-spacing:-0.05em;user-select:none;white-space:nowrap">
        {month_num}
      </div>
      <div style="position:relative;padding:{pad}px {pad}px 0;">
        {_topbar(f"NEW MONTH · {month_name} {year}", fs_kick=20)}
        <div class="rule" style="margin:{int(h * 0.06)}px 0 36px;"></div>
        <h1 class="head" style="font-size:96px;color:#fff;font-weight:800;
                                line-height:1.0;letter-spacing:-0.03em;max-width:90%">
          {theme}
        </h1>
        {sub_html}
      </div>
      {_footer(card, w)}
    </div>
    """


def _html_holiday_card(card: dict, w: int, h: int) -> str:
    """Holiday greeting — warm, restrained, brand-first."""
    pad = int(w * 0.085)
    holiday_name = card.get("holiday_name", "")
    headline = card.get("headline", f"Happy {holiday_name}")
    sub = card.get("sub", "")
    sub_html = (f'<p style="font-size:28px;color:{PALETTE["text"]};margin-top:28px;'
                f'line-height:1.5;max-width:85%">{sub}</p>') if sub else ""
    return f"""
    <div class="card" style="background:{PALETTE['light']}">
      <div style="padding:{pad}px {pad}px 0;">
        {_topbar(f"HAPPY {holiday_name.upper()}", fs_kick=20)}
        <div class="rule" style="margin:{int(h * 0.07)}px 0 40px;"></div>
        <h1 class="head" style="font-size:80px;color:{PALETTE['dark']};
                                font-weight:800;line-height:1.05;max-width:90%">
          {headline}
        </h1>
        {sub_html}
      </div>
      {_footer(card, w)}
    </div>
    """


def _html_announcement_card(card: dict, w: int, h: int) -> str:
    """Special announcement — dark, high-impact, authoritative."""
    pad = int(w * 0.085)
    badge_text = card.get("badge", "ANNOUNCEMENT")
    headline = card.get("headline", "")
    sub = card.get("sub", "")
    sub_html = (f'<p style="font-size:30px;color:#C9C6C2;margin-top:30px;'
                f'line-height:1.5;max-width:85%">{sub}</p>') if sub else ""
    return f"""
    <div class="card" style="background:{PALETTE['dark']}">
      <div style="padding:{pad}px {pad}px 0;">
        <div style="display:inline-block;background:{PALETTE['accent']};
                    color:#fff;font-weight:700;font-size:18px;letter-spacing:0.18em;
                    text-transform:uppercase;padding:8px 20px;border-radius:6px;
                    margin-bottom:{int(h * 0.05)}px">
          {badge_text}
        </div>
        <div class="rule" style="margin:28px 0 36px;"></div>
        <h1 class="head" style="font-size:82px;color:#fff;font-weight:800;
                                line-height:1.05;max-width:92%">{headline}</h1>
        {sub_html}
      </div>
      {_footer(card, w)}
    </div>
    """


_RENDERERS = {
    "tip": _html_text_card, "explainer": _html_text_card, "insight": _html_text_card,
    "quote": _html_text_card, "cta": _html_text_card, "spotlight": _html_spotlight_card,
    "monthly-theme": _html_monthly_theme_card,
    "holiday":        _html_holiday_card,
    "announcement":   _html_announcement_card,
}


# ----------------------------------------------------------------------------- build
def _render_html_to_png(html_str: str, css_str: str, w: int, h: int, out: Path,
                        scale: float = 1.0) -> Path:
    pdf_bytes = HTML(string=f"<style>{css_str}</style>{html_str}").write_pdf()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    page = doc[0]
    # page is sized in px (via @page), but PDF user units are pt (1px=0.75pt).
    # Render at a zoom that maps the page back to exactly w x h px.
    zoom_x = w / page.rect.width
    zoom_y = h / page.rect.height
    mat = fitz.Matrix(zoom_x * scale, zoom_y * scale)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    out.parent.mkdir(parents=True, exist_ok=True)
    pix.save(str(out))
    doc.close()
    return out


def build(card: dict, out: str | os.PathLike, scale: float = 1.0) -> Path:
    """Render a single card dict to a PNG. Returns the output path."""
    size = card.get("size", "portrait")
    w, h = SIZES[size]
    renderer = _RENDERERS.get(card["type"])
    if renderer is None:
        raise ValueError(f"Unknown card type: {card['type']!r}. "
                         f"Known: {sorted(_RENDERERS)} + 'carousel'")
    html_str = renderer(card, w, h)
    css_str = _base_css(w, h)
    out_path = Path(out)
    if not out_path.is_absolute():
        out_path = OUT_DIR / out_path
    return _render_html_to_png(html_str, css_str, w, h, out_path, scale)


def build_carousel(carousel: dict, out_prefix: str, scale: float = 1.0) -> list[Path]:
    """Render a carousel: list of slide dicts -> one PNG per slide (4:5)."""
    slides = carousel["slides"]
    paths = []
    for i, slide in enumerate(slides, 1):
        slide.setdefault("size", "portrait")
        slide.setdefault("kicker", carousel.get("kicker", "AKARAKIRI"))
        slide.setdefault("footer", carousel.get("footer", DEFAULT_FOOTER))
        slide.setdefault("handle", carousel.get("handle", DEFAULT_HANDLE))
        # auto-number the kicker per slide if requested
        if carousel.get("number_kicker"):
            slide["kicker"] = f'{carousel["kicker"]} · {i:02d}/{len(slides):02d}'
        p = build(slide, f"{out_prefix}-{i:02d}.png", scale=scale)
        paths.append(p)
    return paths


# ----------------------------------------------------------------------------- SAMPLES
SAMPLE_CARDS = [
    # 1. Revit tip carousel cover (portrait)
    {"name": "sample-revit-tip-cover", "card": {
        "type": "tip", "size": "portrait", "kicker": "REVIT TIP · 01",
        "headline": "5 Revit habits that save me hours every week.",
        "sub": "The small disciplines that keep a model clean and a deadline calm.",
    }},
    # 2. Revit tip payload slide with bullets
    {"name": "sample-revit-tip-list", "card": {
        "type": "tip", "size": "portrait", "kicker": "REVIT TIP · 01",
        "headline": "The 5 habits.",
        "bullets": [
            "Purge unused before every issue",
            "View templates, never manual overrides",
            "Schedules to auto-quantify",
            "Worksets from day one",
            "Dynamo for the boring 200-sheet jobs",
        ],
    }},
    # 3. BIM explained quote card (square)
    {"name": "sample-bim-quote", "card": {
        "type": "quote", "size": "square", "kicker": "BIM EXPLAINED",
        "headline": "BIM isn't 3D. It's a <span class='accent'>database</span> that happens to look like a building.",
        "footer": DEFAULT_FOOTER,
    }},
    # 4. CTA card (dark, story)
    {"name": "sample-cta", "card": {
        "type": "cta", "size": "story", "kicker": "WORK WITH ME",
        "headline": "Planning a build?",
        "sub": "I design it, model it in BIM, and help deliver it on site.",
        "button": "DM me for a consult",
    }},
    # 5. New Month — monthly-theme card (portrait)
    {"name": "sample-new-month-july", "card": {
        "type": "monthly-theme", "size": "portrait",
        "month_num": "07", "month_name": "JULY", "year": "2026",
        "headline": "Build.",
        "sub": "This month: one more project documented, one more lesson shared.",
    }},
    # 6. Holiday card — warm, brand-first (portrait)
    {"name": "sample-holiday-independence", "card": {
        "type": "holiday", "size": "portrait",
        "holiday_name": "Independence Day",
        "headline": "Happy Independence Day, Nigeria.",
        "sub": "65 years of building. Still going.",
    }},
    # 7. Announcement card — dark, high-impact (portrait)
    {"name": "sample-announcement-new-service", "card": {
        "type": "announcement", "size": "portrait",
        "badge": "ANNOUNCEMENT",
        "headline": "BIM Coordination is now a standalone service.",
        "sub": "Revit modelling · clash detection · coordination reports — from concept to site.",
    }},
]


def _build_samples():
    print("Building sample graphics →", OUT_DIR)
    for item in SAMPLE_CARDS:
        try:
            p = build(item["card"], f"{item['name']}.png")
            print("  ✓", p.relative_to(REPO))
        except Exception as e:
            print("  ✗", item["name"], "->", e)

    # a spotlight needs a real image; use one from the repo if present
    hero = REPO / "assets/Project Pictures/Ado Hall of Worship/Ado Hero Render.png"
    if hero.exists():
        try:
            p = build({"type": "spotlight", "size": "portrait",
                       "kicker": "PROJECT SPOTLIGHT",
                       "image": str(hero.relative_to(REPO)),
                       "title": "Ado Hall of Worship",
                       "meta": "Concept → BIM → Visualization · Ado-Ekiti, Nigeria"},
                      "sample-spotlight-ado.png")
            print("  ✓", p.relative_to(REPO))
        except Exception as e:
            print("  ✗ spotlight ->", e)
    else:
        print("  (skipped spotlight — sample hero image not found)")

    # a small carousel
    try:
        ps = build_carousel({
            "kicker": "BIM EXPLAINED", "number_kicker": True,
            "slides": [
                {"type": "tip", "headline": "What clash detection actually saves you.",
                 "sub": "A 30-second model check vs a ₦-millions site mistake."},
                {"type": "tip", "headline": "The problem.",
                 "sub": "Pipes, ducts and beams are drawn by different people, in different files."},
                {"type": "tip", "headline": "In BIM, the model catches it first.",
                 "sub": "Overlap the models, run a clash check, fix it on screen — not on site."},
                {"type": "cta", "headline": "Need this on your project?",
                 "sub": "I coordinate BIM models so problems die in the model.",
                 "button": "DM me"},
            ]}, "sample-carousel-clash")
        for p in ps:
            print("  ✓", p.relative_to(REPO))
    except Exception as e:
        print("  ✗ carousel ->", e)


if __name__ == "__main__":
    _build_samples()
