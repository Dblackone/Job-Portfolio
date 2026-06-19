#!/usr/bin/env python3
"""
Construction Portfolio v2 — Vollmann Olamide Akarakiri
Focuses on 7 projects where physical site work was carried out.

Projects:
  01 · The Body Shop Outlets    — Ikeja City Mall + Circle Mall Lekki
  02 · Fina Trust Bank          — Sales outlet fit-out
  03 · Ikotun Apartments        — 6-flat ongoing structure (from foundation)
  04 · Ado 6-Bedroom Duplex     — Structural stage + interior finishes
  05 · Alcove Homes Yaba        — Residential + interior
  06 · Oluku Ultra Modern Market — Drainage system + shop structure
  07 · Office Interior, Ibafo   — Office fit-out

Missing project photos show styled terracotta placeholder tiles.
Drop site photos into the relevant assets/Project Pictures/<folder>/
then re-run this script to rebuild with real images.

Run:  python3 pdf/build_construction_v2.py
Out:  assets/vollmann-akarakiri-construction-v2.pdf
"""

import base64
import io
import os

from PIL import Image, ImageDraw, ImageFont, ImageOps
from weasyprint import HTML

ROOT     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS   = os.path.join(ROOT, "assets")
PICS     = os.path.join(ASSETS, "Project Pictures")
FONT_DIR = os.path.join(ROOT, "pdf", "fonts")
OUT      = os.path.join(ASSETS, "vollmann-akarakiri-construction-v2.pdf")

TOTAL_PAGES = 12


# ───────────────────────── helpers ─────────────────────────

def font_uri(weight):
    with open(os.path.join(FONT_DIR, f"inter-{weight}.woff2"), "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode()
    return f"data:font/woff2;base64,{b64}"


def img_uri(path, max_px=1280, quality=82, keep_alpha=False):
    """Load, EXIF-rotate, downscale and base64-encode an image."""
    im = Image.open(path)
    im = ImageOps.exif_transpose(im)          # fix phone-photo rotation
    w, h = im.size
    scale = min(1.0, max_px / float(max(w, h)))
    if scale < 1.0:
        im = im.resize((max(1, int(w * scale)), max(1, int(h * scale))),
                       Image.LANCZOS)
    buf = io.BytesIO()
    if keep_alpha and im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        im.save(buf, format="PNG", optimize=True)
        mime = "image/png"
    else:
        if im.mode != "RGB":
            im = im.convert("RGB")
        im.save(buf, format="JPEG", quality=quality, optimize=True,
                progressive=True)
        mime = "image/jpeg"
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"data:{mime};base64,{b64}"


def placeholder_uri(label="Photo Coming Soon", width=1600, height=900):
    """Return a terracotta placeholder tile as a base64 JPEG data URI."""
    im = Image.new("RGB", (width, height), color=(184, 92, 56))
    draw = ImageDraw.Draw(im)
    # Dark overlay strip at bottom
    draw.rectangle([(0, height - 80), (width, height)],
                   fill=(158, 79, 48))
    # Try to use a system font; fall back to default
    font_size = max(28, width // 28)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                                  font_size)
    except Exception:
        font = ImageFont.load_default()
    # Centre the label
    try:
        bbox = draw.textbbox((0, 0), label, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    except AttributeError:
        tw, th = draw.textsize(label, font=font)
    draw.text(((width - tw) // 2, (height - th) // 2), label,
              fill=(255, 255, 255, 200), font=font)
    # Arrow icon top-left
    draw.text((40, 40), "→", fill=(255, 255, 255, 120), font=font)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=82)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"data:image/jpeg;base64,{b64}"


def img_or_ph(path, label="Photo Coming Soon", **kwargs):
    """Return real image URI if path exists, else a placeholder."""
    if path and os.path.exists(path):
        return img_uri(path, **kwargs)
    return placeholder_uri(label)


# ───────────────────────── project image folders ───────────────────────────

BODY_SHOP = os.path.join(PICS, "Body Shop Outlets")
FINA      = os.path.join(PICS, "Fina Trust Bank")
IKOTUN    = os.path.join(PICS, "Ikotun Apartments")
ADO_DUP   = os.path.join(PICS, "Ado 6-Bedroom Duplex")
ALCOVE    = os.path.join(PICS, "Alcove Homes Yaba")
OLUKU     = os.path.join(PICS, "Oluku Modern Market")
IBAFO     = os.path.join(PICS, "Office Interior Ibafo")
LAND      = os.path.join(PICS, "Landscape Projects")
RENO      = os.path.join(PICS, "Renovation Akure")


# ───────────────────────── load all images ─────────────────────────────────

print("Loading images…")

IMG = {
    # Profile + cover
    "profile": img_uri(os.path.join(ASSETS, "vollmann-akarakiri-profile.png"),
                       max_px=760, keep_alpha=True),
    "cover_band": img_or_ph(
        os.path.join(BODY_SHOP, "body-shop-retail-floor.jpeg"),
        label="Cover — Site Photo", max_px=1600, quality=84),

    # ── SW01 · Body Shop Outlets ──────────────────────────────────────────
    "bs_hero": img_or_ph(
        os.path.join(BODY_SHOP, "body-shop-retail-floor.jpeg"),
        label="Body Shop — Interior", max_px=1600),
    "bs_b": img_or_ph(
        os.path.join(BODY_SHOP, "body-shop-mural-display.jpeg"),
        label="Body Shop — Mural Wall"),
    "bs_c": img_or_ph(
        os.path.join(BODY_SHOP, "body-shop-counter-display.jpeg"),
        label="Body Shop — Counter"),

    # ── SW02 · Fina Trust Bank ────────────────────────────────────────────
    "fina_hero": img_or_ph(None, label="Fina Trust Bank — Exterior / Frontage"),
    "fina_b":    img_or_ph(None, label="Fina Trust Bank — Counter Interior"),
    "fina_c":    img_or_ph(None, label="Fina Trust Bank — Signage / Detail"),

    # ── SW03 · Ikotun Apartments ──────────────────────────────────────────
    "ikt_hero": img_or_ph(
        os.path.join(IKOTUN, "ikotun-site-raw.jpg"),
        label="Ikotun — Site Overview", max_px=1600),
    "ikt_b": img_or_ph(
        os.path.join(IKOTUN, "ikotun-structure.jpg"),
        label="Ikotun — Structure"),
    "ikt_c": img_or_ph(
        os.path.join(IKOTUN, "ikotun-progress.jpg"),
        label="Ikotun — Progress"),

    # ── SW04 · Ado 6-Bedroom Duplex ───────────────────────────────────────
    "ado_hero": img_or_ph(None, label="Ado Duplex — Structural Stage"),
    "ado_b":    img_or_ph(None, label="Ado Duplex — Foundation / Slab"),
    "ado_c":    img_or_ph(None, label="Ado Duplex — Interior Finishes"),

    # ── SW05 · Alcove Homes Yaba ──────────────────────────────────────────
    "alc_hero": img_or_ph(None, label="Alcove Homes — Exterior"),
    "alc_b":    img_or_ph(None, label="Alcove Homes — Interior A"),
    "alc_c":    img_or_ph(None, label="Alcove Homes — Interior B"),

    # ── SW06 · Oluku Ultra Modern Market ──────────────────────────────────
    "olu_hero": img_or_ph(None, label="Oluku Market — Site Overview"),
    "olu_b":    img_or_ph(None, label="Oluku Market — Drainage System"),
    "olu_c":    img_or_ph(None, label="Oluku Market — Shop Structure"),

    # ── SW07 · Office Interior, Ibafo ─────────────────────────────────────
    "iba_hero": img_or_ph(None, label="Ibafo Office — Interior Overview"),
    "iba_b":    img_or_ph(None, label="Ibafo Office — Workstation Area"),
    "iba_c":    img_or_ph(None, label="Ibafo Office — Detail / Finish"),
}

print("Images loaded.")

FONT_FACES = "".join(
    f"""@font-face{{font-family:'Inter';font-style:normal;font-weight:{w};
    src:url('{font_uri(w)}') format('woff2');}}"""
    for w in (300, 400, 500, 600, 700, 800)
)


# ───────────────────────────────── CSS ─────────────────────────────────────

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
:root{
  --bg:#F5F2EE; --accent:#B85C38; --accent-d:#9e4f30; --text:#4A4F5C;
  --dark:#2C2C2C; --white:#FFFFFF; --warm:#E8E4DF; --light:#F0DDD8;
  --border:#D1CBC6;
}
html{ -weasy-print-color-adjust:exact; }
@page{ size:A4; margin:0; }
body{
  font-family:'Inter',sans-serif; color:var(--text); background:var(--bg);
  line-height:1.6; font-size:10.5px; -webkit-print-color-adjust:exact;
  print-color-adjust:exact;
}
h1,h2,h3,h4{ color:var(--dark); font-weight:700; line-height:1.12;
  letter-spacing:-0.02em; }
a{ color:inherit; text-decoration:none; }

.sheet{
  position:relative; width:210mm; height:297mm; padding:15mm 16mm 14mm;
  background:var(--bg); overflow:hidden; page-break-after:always;
}
.sheet:last-child{ page-break-after:auto; }
.sheet.dark{ background:var(--dark); }
.sheet.white{ background:var(--white); }

.label{ font-size:9px; font-weight:600; letter-spacing:0.22em;
  text-transform:uppercase; color:var(--accent); }
.accent-bar{ width:42px; height:4px; background:var(--accent);
  border-radius:2px; }

.s-head{ margin-bottom:9mm; }
.s-head h2{ font-size:30px; margin-top:7px; }
.s-head .sub{ font-size:12px; font-weight:300; color:var(--text);
  margin-top:8px; max-width:150mm; }

/* ── COVER ── */
.cover::before{ content:''; position:absolute; left:0; top:0; bottom:0;
  width:9px; background:var(--accent); }
.cover-shape{ position:absolute; right:-70px; top:120px; width:340px;
  height:340px; background:var(--light); border-radius:50%; opacity:.5; }
.cover-top{ display:flex; align-items:center; justify-content:space-between;
  margin-bottom:22mm; }
.brand{ display:flex; align-items:center; gap:11px; }
.brand .mark{ width:34px; height:34px; background:var(--accent);
  border-radius:5px; color:#fff; font-weight:800; font-size:17px;
  display:flex; align-items:center; justify-content:center; }
.brand .nm{ font-size:11px; font-weight:600; letter-spacing:0.09em;
  text-transform:uppercase; color:var(--dark); }
.cover-tag{ font-size:9px; font-weight:600; letter-spacing:0.22em;
  text-transform:uppercase; color:var(--accent); }

.hero{ display:grid; grid-template-columns:1fr 70mm; gap:12mm;
  align-items:start; position:relative; z-index:1; }
.hero-label{ margin-bottom:14px; }
.headline{ font-size:48px; font-weight:800; line-height:1.06;
  letter-spacing:-0.03em; }
.headline span{ display:block; }
.headline .accent{ color:var(--accent); }
.headline .muted{ color:var(--text); }
.hero-sub{ font-size:13px; font-weight:300; color:var(--text);
  margin-top:16px; max-width:96mm; line-height:1.7; }
.hero-points{ list-style:none; margin-top:16px; }
.hero-points li{ font-size:11.5px; padding:5px 0 5px 18px; position:relative;
  color:var(--text); }
.hero-points li::before{ content:'\2192'; position:absolute; left:0;
  color:var(--accent); font-weight:700; }

.pcard{ background:var(--white); border:1px solid var(--border);
  border-radius:14px; overflow:hidden; box-shadow:0 10px 34px rgba(44,44,44,.12); }
.pcard .photo{ width:100%; height:60mm; object-fit:cover;
  object-position:center top; background:var(--warm); display:block; }
.pcard .info{ padding:16px 16px 18px; }
.pcard .info .accent-bar{ margin-bottom:11px; }
.pcard h3{ font-size:15px; margin-bottom:3px; }
.pcard .role{ font-size:11px; color:var(--accent); font-weight:500; }
.pcard .loc{ font-size:10px; color:var(--text); margin-bottom:13px; }
.pstats{ display:flex; gap:7px; margin-bottom:13px; }
.pstats .b{ flex:1; background:var(--bg); border-radius:7px; padding:8px 6px;
  text-align:center; }
.pstats .n{ font-size:15px; font-weight:700; color:var(--dark); line-height:1.1; }
.pstats .l{ font-size:7.5px; color:var(--text); margin-top:2px; }
.psw{ display:flex; flex-wrap:wrap; gap:5px; margin-bottom:13px; }
.psw span{ font-size:9px; color:var(--dark); background:var(--light);
  border-radius:100px; padding:3px 9px; }
.avail{ display:flex; align-items:center; gap:7px; font-size:9.5px;
  color:var(--text); }
.avail .dot{ width:7px; height:7px; border-radius:50%; background:#3DB87A;
  box-shadow:0 0 0 3px rgba(61,184,122,.2); }

.cover-foot{ position:absolute; left:16mm; right:16mm; bottom:13mm;
  display:flex; gap:10mm; padding-top:8px; border-top:1px solid var(--border); }
.cover-foot .ci .cl{ font-size:8px; font-weight:600; letter-spacing:0.14em;
  text-transform:uppercase; color:var(--accent); margin-bottom:2px; }
.cover-foot .ci .cv{ font-size:10.5px; color:var(--dark); }

.img-band{ position:relative; margin-top:7mm; border-radius:12px;
  overflow:hidden; border:1px solid var(--border);
  box-shadow:0 6px 22px rgba(44,44,44,.08); }
.img-band img{ width:100%; height:66mm; object-fit:cover;
  object-position:center 35%; display:block; }
.img-band .cap{ position:absolute; left:0; right:0; bottom:0;
  padding:18px 14px 9px;
  background:linear-gradient(rgba(0,0,0,0), rgba(0,0,0,.58));
  color:#fff; font-size:9.5px; font-weight:600; letter-spacing:0.07em;
  text-transform:uppercase; }

/* ── ABOUT ── */
.about{ display:grid; grid-template-columns:1fr 1fr; gap:11mm;
  align-items:start; }
.about p{ font-size:11px; line-height:1.75; margin-bottom:11px; }
.stat-grid{ display:grid; grid-template-columns:1fr 1fr; gap:10px;
  margin-top:13px; }
.stat-grid .st{ background:var(--bg); border-radius:7px; padding:13px 14px; }
.sheet.white .stat-grid .st{ background:var(--bg); }
.stat-grid .n{ font-size:25px; font-weight:700; color:var(--accent);
  line-height:1; }
.stat-grid .d{ font-size:9.5px; color:var(--text); margin-top:4px; }

.skill-group{ background:var(--bg); border-radius:7px; padding:13px 15px;
  margin-bottom:10px; }
.sheet.white .skill-group{ background:var(--bg); }
.skill-group h4{ font-size:11.5px; margin-bottom:9px; }
.pills{ display:flex; flex-wrap:wrap; gap:6px; }
.pills span{ font-size:9px; padding:4px 11px; background:var(--white);
  border:1px solid var(--border); border-radius:100px; color:var(--text); }

.edu-grid{ display:grid; grid-template-columns:1fr 1fr; gap:14px;
  margin-top:11mm; }
.edu{ background:var(--bg); border-left:3px solid var(--accent);
  border-radius:6px; padding:15px 17px; }
.sheet.white .edu{ background:var(--bg); }
.edu .dg{ font-size:12px; font-weight:700; color:var(--dark); }
.edu .in{ font-size:10px; color:var(--text); margin:3px 0; }
.edu .pe{ font-size:9.5px; color:var(--accent); font-weight:600; }

/* ── SOFTWARE dark ── */
.dark .label{ color:var(--accent); }
.dark h2{ color:var(--white); }
.dark .s-head .sub{ color:var(--warm); }
.sw-grid{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }
.sw{ background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.09);
  border-radius:10px; padding:16px 17px; }
.sw .ic{ width:34px; height:34px; background:var(--accent); border-radius:7px;
  color:#fff; font-size:15px; display:flex; align-items:center;
  justify-content:center; margin-bottom:10px; }
.sw h4{ color:var(--white); font-size:12.5px; margin-bottom:3px; }
.sw .lv{ font-size:9px; color:var(--accent); font-weight:600; margin-bottom:6px; }
.sw p{ font-size:9.5px; color:rgba(232,228,223,.66); line-height:1.55; }
.disc{ display:flex; flex-wrap:wrap; gap:8px; margin-top:11mm;
  padding-top:8mm; border-top:1px solid rgba(255,255,255,.1); }
.disc span{ font-size:9px; font-weight:600; color:var(--accent);
  background:rgba(184,92,56,.15); border:1px solid rgba(184,92,56,.32);
  padding:5px 12px; border-radius:100px; letter-spacing:0.04em; }

/* ── EXPERIENCE ── */
.tl{ list-style:none; }
.tl li{ position:relative; padding:0 0 7mm 22px;
  border-left:2px solid var(--border); }
.tl li:last-child{ border-left-color:transparent; padding-bottom:0; }
.tl li::before{ content:''; position:absolute; left:-6px; top:4px;
  width:10px; height:10px; border-radius:50%; background:var(--accent);
  border:2px solid var(--bg); }
.tl li.cur::before{ box-shadow:0 0 0 4px rgba(184,92,56,.2); }
.tl .pe{ font-size:9.5px; color:var(--accent); font-weight:600; }
.tl .ro{ font-size:13px; font-weight:700; color:var(--dark); margin-top:2px; }
.tl .co{ font-size:10.5px; color:var(--text); margin-bottom:6px; }
.tl ul{ list-style:none; }
.tl ul li{ border:none; padding:2px 0 2px 14px; font-size:10px;
  line-height:1.5; color:var(--text); }
.tl ul li::before{ content:'\2192'; left:0; top:2px; width:auto; height:auto;
  background:none; border:none; border-radius:0; color:var(--accent);
  font-size:9px; }
.metrics{ display:grid; grid-template-columns:repeat(4,1fr); gap:10px;
  margin-top:9mm; padding-top:7mm; border-top:1px solid var(--border); }
.metrics .st{ background:var(--bg); border-radius:7px; padding:12px;
  text-align:center; }
.metrics .n{ font-size:21px; font-weight:700; color:var(--accent); }
.metrics .d{ font-size:8.5px; color:var(--text); margin-top:3px; }

/* ── SELECTED WORK ── */
.fig{ border-radius:9px; overflow:hidden; border:1px solid var(--border);
  background:var(--warm); margin-bottom:11px; }
.fig img{ width:100%; display:block; object-fit:cover; }
.fig .cap{ padding:9px 13px; display:flex; justify-content:space-between;
  align-items:baseline; gap:10px; }
.fig .cap .t{ font-size:10.5px; font-weight:600; color:var(--dark); }
.fig .cap .m{ font-size:8.5px; font-weight:600; letter-spacing:0.06em;
  text-transform:uppercase; color:var(--accent); white-space:nowrap; }
.fig.big img{ height:96mm; }
.fig.half img{ height:62mm; }
.row2{ display:grid; grid-template-columns:1fr 1fr; gap:11px; }

/* ── CONTACT dark ── */
.contact{ display:flex; flex-direction:column; align-items:center;
  justify-content:center; text-align:center; min-height:267mm; }
.contact h2{ color:var(--white); font-size:34px; margin:14px 0 16px;
  max-width:150mm; }
.contact .lead{ font-size:12.5px; color:var(--warm); max-width:130mm;
  line-height:1.7; }
.cbtns{ display:flex; gap:12px; margin-top:26px; }
.cbtns a{ font-size:11px; font-weight:600; padding:11px 26px;
  border-radius:5px; text-decoration:none; }
.cbtns .solid{ background:var(--white); color:var(--dark); }
.cbtns .out{ background:transparent; color:var(--white);
  border:1.5px solid rgba(255,255,255,.35); }
.cdetails{ display:grid; grid-template-columns:repeat(3,auto); gap:14mm 18mm;
  margin-top:20mm; padding-top:9mm;
  border-top:1px solid rgba(255,255,255,.12); }
.cdetails .ci .cl{ font-size:8px; font-weight:600; letter-spacing:0.16em;
  text-transform:uppercase; color:var(--accent); margin-bottom:4px; }
.cdetails .ci .cv{ font-size:11px; color:var(--white); }
.cfoot{ position:absolute; left:0; right:0; bottom:12mm; text-align:center;
  font-size:9px; color:rgba(232,228,223,.4); letter-spacing:0.04em; }

/* ── page footer ── */
.pfoot{ position:absolute; left:16mm; right:16mm; bottom:9mm;
  display:flex; justify-content:space-between; align-items:center;
  font-size:8px; color:#9a948e; letter-spacing:0.05em;
  border-top:1px solid var(--border); padding-top:6px; }
.pfoot .nm{ text-transform:uppercase; }
"""

FOOTER = (
    '<div class="pfoot"><span class="nm">Vollmann Olamide Akarakiri · '
    f'Construction Project Manager</span><span>{{n}} / {TOTAL_PAGES}</span></div>'
)


# ───────────────────────────────── HTML body ────────────────────────────────

BODY = """
<!-- ════════ 1 · COVER ════════ -->
<section class="sheet cover">
  <div class="cover-shape"></div>
  <div class="cover-top">
    <div class="brand"><div class="mark">V</div>
      <div class="nm">Vollmann&nbsp;Akarakiri</div></div>
    <div class="cover-tag">Construction Portfolio · Site Projects · 2026</div>
  </div>

  <div class="hero">
    <div>
      <p class="label hero-label">Construction Project Manager · Site Engineer · Lagos, Nigeria</p>
      <div class="headline">
        <span>Site.</span>
        <span class="accent">Structure.</span>
        <span>Delivered.</span>
        <span class="muted">On Time.</span>
      </div>
      <p class="hero-sub">Seven physical site projects — retail fit-outs, banking
        outlets, residential structures and market infrastructure — delivered
        across Lagos, Benin City and Ogun State.</p>
      <ul class="hero-points">
        <li>Commercial fit-outs: The Body Shop, Fina Trust Bank</li>
        <li>Residential construction: Ikotun 6-flat, Ado Duplex, Alcove Homes</li>
        <li>Civil &amp; infrastructure: Oluku Ultra Modern Market</li>
        <li>Corporate interiors: Office fit-out, Ibafo</li>
      </ul>
    </div>

    <aside class="pcard">
      <img class="photo" src="__profile__" alt="Vollmann Olamide Akarakiri" />
      <div class="info">
        <div class="accent-bar"></div>
        <h3>Vollmann Olamide Akarakiri</h3>
        <div class="role">Construction Project Manager</div>
        <div class="loc">Lagos, Nigeria · MSc CEM Candidate, UEL</div>
        <div class="pstats">
          <div class="b"><div class="n">30+</div><div class="l">Total projects</div></div>
          <div class="b"><div class="n">&#8358;350M+</div><div class="l">Project value</div></div>
          <div class="b"><div class="n">7+</div><div class="l">Years</div></div>
        </div>
        <div class="psw">
          <span>Revit</span><span>AutoCAD</span><span>Navisworks</span>
          <span>MS Project</span><span>Dynamo</span>
        </div>
        <div class="avail"><div class="dot"></div>
          <span>Open to opportunities — worldwide &amp; remote</span></div>
      </div>
    </aside>
  </div>

  <div class="img-band">
    <img src="__cover_band__" alt="The Body Shop outlet — fit-out" />
    <div class="cap">The Body Shop — Retail Fit-Out · Ikeja City Mall, Lagos</div>
  </div>

  <div class="cover-foot">
    <div class="ci"><div class="cl">Phone</div><div class="cv">+234 816 367 5439</div></div>
    <div class="ci"><div class="cl">Email</div><div class="cv">vollmannakarakiri0@gmail.com</div></div>
    <div class="ci"><div class="cl">Location</div><div class="cv">Lagos, Nigeria</div></div>
    <div class="ci"><div class="cl">LinkedIn</div><div class="cv"><a href="https://www.linkedin.com/in/vollmann-akarakiri-49127b1a0">/in/vollmann-akarakiri-49127b1a0</a></div></div>
  </div>
</section>

<!-- ════════ 2 · ABOUT ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Professional Profile</p>
    <h2>The Site Professional</h2></div>

  <div class="about">
    <div>
      <p>Vollmann Olamide Akarakiri is a Construction Project Manager and Site
        Engineer with 7+ years delivering physical construction and fit-out
        projects across commercial, residential and infrastructure sectors in
        Nigeria.</p>
      <p>His site experience spans retail fit-outs for international brands,
        banking outlet installations, residential buildings from foundation to
        finish, civil drainage infrastructure, and commercial office interiors —
        coordinating subcontractors, material procurement, quality control and
        programme management on each project.</p>
      <p>Backed by advanced BIM capability (Revit, Navisworks, AutoCAD), he
        bridges the gap between digital model and physical delivery — ensuring
        site work is coordinated, clash-free and built to specification.</p>
      <div class="stat-grid">
        <div class="st"><div class="n">30+</div><div class="d">Total projects across all disciplines</div></div>
        <div class="st"><div class="n">&#8358;350M+</div><div class="d">Cumulative project value</div></div>
        <div class="st"><div class="n">&#8358;10M+</div><div class="d">Savings delivered</div></div>
        <div class="st"><div class="n">7+</div><div class="d">Years of experience</div></div>
      </div>
    </div>

    <div>
      <p class="label" style="margin-bottom:9px;">Site &amp; Construction Competencies</p>
      <div class="skill-group"><h4>Site Engineering &amp; Supervision</h4>
        <div class="pills"><span>Subcontractor Management</span>
          <span>Quality Control</span><span>Site Safety (HSE)</span>
          <span>Snagging &amp; Handover</span><span>Material Procurement</span></div></div>
      <div class="skill-group"><h4>Commercial Fit-Outs</h4>
        <div class="pills"><span>Retail Fit-Out</span><span>Joinery &amp; Fixtures</span>
          <span>MEP Coordination</span><span>Flooring &amp; Ceilings</span>
          <span>Signage &amp; Branding Installation</span></div></div>
      <div class="skill-group"><h4>Structural &amp; Civil Works</h4>
        <div class="pills"><span>Foundations</span><span>Concrete &amp; Blockwork</span>
          <span>Drainage Systems</span><span>Roofing</span>
          <span>Structural Coordination</span></div></div>
      <div class="skill-group"><h4>Project &amp; Programme Management</h4>
        <div class="pills"><span>Planning &amp; Scheduling</span>
          <span>Cost Control</span><span>Procurement &amp; Contracts</span>
          <span>Stakeholder Reporting</span></div></div>
    </div>
  </div>

  <div class="edu-grid">
    <div class="edu"><div class="dg">MSc Construction Engineering Management</div>
      <div class="in">University of East London</div>
      <div class="pe">Sep 2024 – Present</div></div>
    <div class="edu"><div class="dg">BSc Building Technology</div>
      <div class="in">Federal University of Technology, Akure</div>
      <div class="pe">2014 – 2019</div></div>
  </div>
  __FOOT2__
</section>

<!-- ════════ 3 · BIM & SOFTWARE (dark) ════════ -->
<section class="sheet dark">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Technical Toolkit</p>
    <h2>Site &amp; Construction Software</h2>
    <p class="sub">Digital tools deployed from pre-construction coordination
      through to site delivery and project close-out.</p></div>

  <div class="sw-grid">
    <div class="sw"><div class="ic">&#9670;</div><h4>Autodesk Revit</h4>
      <div class="lv">Expert — BIM Modelling &amp; Coordination</div>
      <p>Coordinated BIM models for commercial, residential and fit-out projects
        — family creation, documentation, schedules and clash-free model
        production for site delivery.</p></div>
    <div class="sw"><div class="ic">&#9671;</div><h4>Navisworks</h4>
      <div class="lv">Proficient — Site Coordination</div>
      <p>Multi-discipline clash detection and 4D sequencing before site
        commences — reducing on-site rework, delays and procurement
        errors across commercial fit-out and residential projects.</p></div>
    <div class="sw"><div class="ic">&#9633;</div><h4>AutoCAD</h4>
      <div class="lv">Expert — Technical Drawing</div>
      <p>Site plans, shop drawings, fit-out layouts, drainage details and
        construction documentation — issued to subcontractors and
        approved for construction.</p></div>
    <div class="sw"><div class="ic">&#9650;</div><h4>Microsoft Project</h4>
      <div class="lv">Proficient — Programme Management</div>
      <p>Construction programmes, milestone tracking and resource scheduling
        across concurrent commercial and residential site operations.</p></div>
    <div class="sw"><div class="ic">&#9632;</div><h4>MS Excel &amp; Office</h4>
      <div class="lv">Advanced — Cost Control</div>
      <p>Budget tracking, BoQ management, procurement schedules and
        progress reporting for fit-out and construction projects.</p></div>
    <div class="sw"><div class="ic">&#9679;</div><h4>Dynamo for Revit</h4>
      <div class="lv">Advanced — Automation</div>
      <p>Parametric scripts to automate documentation and quantity extraction
        — reducing manual work on commercial and residential project
        delivery packages.</p></div>
  </div>

  <div class="disc">
    <span>Retail Fit-Out</span><span>Structural Construction</span>
    <span>Civil &amp; Drainage Works</span><span>MEP Coordination</span>
    <span>BIM &amp; Clash Detection</span><span>Site Safety (HSE)</span>
    <span>Procurement &amp; Contracts</span><span>Cost Control</span>
    <span>Programme Management</span><span>Quality Assurance</span>
    <span>Subcontractor Coordination</span><span>Snagging &amp; Handover</span>
  </div>
</section>

<!-- ════════ 4 · EXPERIENCE ════════ -->
<section class="sheet">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Career History</p>
    <h2>Professional Experience</h2>
    <p class="sub">7+ years on site — from intern to Engineering Lead,
      across commercial fit-outs, residential structures and infrastructure.</p></div>

  <ul class="tl">
    <li class="cur"><div class="pe">Aug 2021 – Feb 2026</div>
      <div class="ro">Project Manager / Engineering Lead</div>
      <div class="co">Nu-Avenue Company Resources</div>
      <ul><li>Directed site delivery across multiple projects in multiple
        states — commercial fit-outs, residential builds and infrastructure.</li>
        <li>Generated &#8358;10M+ in savings through procurement oversight,
          cost control and error prevention.</li>
        <li>Coordinated architects, consultants, engineers, suppliers and
          subcontractors to ensure quality, safety and on-time completion.</li>
        <li>Produced BIM documentation for 30+ office, residential and
          interior projects.</li></ul></li>
    <li><div class="pe">Jun 2020 – Aug 2021</div>
      <div class="ro">Site Engineer / Assistant Technical Designer</div>
      <div class="co">Nature's Beauty Construction</div>
      <ul><li>Planned and supervised site-development and landscape
        projects across multiple Nigerian states.</li>
        <li>Produced detailing packages for 10+ residential properties.</li>
        <li>Trained 5+ site operatives; contributed to &#8358;20M+ business
          pipeline.</li></ul></li>
    <li><div class="pe">Dec 2019 – Apr 2020</div>
      <div class="ro">Site Supervisor</div>
      <div class="co">Lego Construction Company</div>
      <ul><li>Developed project plans, contract documents, site schedules and
        budgets for multiple residential and commercial projects.</li></ul></li>
    <li><div class="pe">Aug 2017 – Dec 2017</div>
      <div class="ro">Architecture &amp; Planning Intern</div>
      <div class="co">Danzinger Nigeria Ltd</div>
      <ul><li>Assisted in drafting, BIM updates and construction documentation
        for consulting projects exceeding &#8358;10M.</li></ul></li>
  </ul>

  <div class="metrics">
    <div class="st"><div class="n">&#8358;350M+</div><div class="d">Total project value</div></div>
    <div class="st"><div class="n">&#8358;10M+</div><div class="d">Savings delivered</div></div>
    <div class="st"><div class="n">30+</div><div class="d">Total projects across all disciplines</div></div>
    <div class="st"><div class="n">7+</div><div class="d">Years on site</div></div>
  </div>
  __FOOT4__
</section>

<!-- ════════ 5 · SW01 · BODY SHOP ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 01</p>
    <h2>The Body Shop Outlets</h2>
    <p class="sub">Full retail fit-out for two The Body Shop outlets — Ikeja
      City Mall and Circle Mall Lekki, Lagos. Joinery, flooring, fixtures,
      MEP and brand installation.</p></div>

  <div class="fig big"><img src="__bs_hero__" alt="The Body Shop — retail interior" />
    <div class="cap"><span class="t">Retail Interior — The Body Shop, Ikeja City Mall</span>
      <span class="m">Fit-Out</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__bs_b__" alt="Body Shop mural wall and display" />
      <div class="cap"><span class="t">Mural Wall &amp; Product Display</span>
        <span class="m">Interior</span></div></div>
    <div class="fig half"><img src="__bs_c__" alt="Body Shop counter and display units" />
      <div class="cap"><span class="t">Counter &amp; Display Units</span>
        <span class="m">Joinery</span></div></div>
  </div>
  __FOOT5__
</section>

<!-- ════════ 6 · SW02 · FINA TRUST BANK ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 02</p>
    <h2>Fina Trust Bank — Sales Outlet</h2>
    <p class="sub">Fit-out of a Fina Trust Bank sales outlet — partition
      works, counter installation, flooring, ceiling, MEP rough-in and
      brand finishes to banking sector specification.</p></div>

  <div class="fig big"><img src="__fina_hero__" alt="Fina Trust Bank exterior or frontage" />
    <div class="cap"><span class="t">Fina Trust Bank — Exterior / Frontage</span>
      <span class="m">Fit-Out</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__fina_b__" alt="Counter and teller interior" />
      <div class="cap"><span class="t">Counter &amp; Teller Interior</span>
        <span class="m">Interior</span></div></div>
    <div class="fig half"><img src="__fina_c__" alt="Signage and brand installation" />
      <div class="cap"><span class="t">Signage &amp; Brand Installation</span>
        <span class="m">Detail</span></div></div>
  </div>
  __FOOT6__
</section>

<!-- ════════ 7 · SW03 · IKOTUN APARTMENTS ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 03</p>
    <h2>Ikotun Apartments — 6-Flat Block</h2>
    <p class="sub">Six-flat residential development, Ikotun, Lagos — ongoing
      construction from foundation. Structural works, column casting, slab
      construction and superstructure.</p></div>

  <div class="fig big"><img src="__ikt_hero__" alt="Ikotun apartments — site overview" />
    <div class="cap"><span class="t">Ikotun Apartments — Site Overview</span>
      <span class="m">Site</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__ikt_b__" alt="Ikotun structural works progress" />
      <div class="cap"><span class="t">Structural Works Progress</span>
        <span class="m">Structure</span></div></div>
    <div class="fig half"><img src="__ikt_c__" alt="Ikotun superstructure and elevation" />
      <div class="cap"><span class="t">Superstructure &amp; Elevation</span>
        <span class="m">Construction</span></div></div>
  </div>
  __FOOT7__
</section>

<!-- ════════ 8 · SW04 · ADO 6-BEDROOM DUPLEX ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 04</p>
    <h2>Ado 6-Bedroom Duplex</h2>
    <p class="sub">Six-bedroom duplex residence, Ado, Ekiti State — two-stage
      delivery: structural works (foundation, columns, slabs, roofing) followed
      by full interior finishes.</p></div>

  <div class="fig big"><img src="__ado_hero__" alt="Ado duplex — structural stage" />
    <div class="cap"><span class="t">Ado Duplex — Structural Stage</span>
      <span class="m">Structure</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__ado_b__" alt="Ado duplex — foundation and slab works" />
      <div class="cap"><span class="t">Foundation &amp; Slab Works</span>
        <span class="m">Civil</span></div></div>
    <div class="fig half"><img src="__ado_c__" alt="Ado duplex — interior finishes stage" />
      <div class="cap"><span class="t">Interior Finishes Stage</span>
        <span class="m">Interior</span></div></div>
  </div>
  __FOOT8__
</section>

<!-- ════════ 9 · SW05 · ALCOVE HOMES YABA ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 05</p>
    <h2>Alcove Homes, Yaba</h2>
    <p class="sub">Residential construction and interior fit-out — Yaba, Lagos.
      Structural works, external envelope and full interior: flooring,
      joinery, fixtures, finishes and MEP.</p></div>

  <div class="fig big"><img src="__alc_hero__" alt="Alcove Homes Yaba — exterior view" />
    <div class="cap"><span class="t">Alcove Homes — Exterior View</span>
      <span class="m">Site</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__alc_b__" alt="Alcove Homes — interior living space" />
      <div class="cap"><span class="t">Interior Living Space</span>
        <span class="m">Interior</span></div></div>
    <div class="fig half"><img src="__alc_c__" alt="Alcove Homes — interior detail finish" />
      <div class="cap"><span class="t">Interior Detail &amp; Finishes</span>
        <span class="m">Detail</span></div></div>
  </div>
  __FOOT9__
</section>

<!-- ════════ 10 · SW06 · OLUKU ULTRA MODERN MARKET ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 06</p>
    <h2>Oluku Ultra Modern Market</h2>
    <p class="sub">Two-stage market infrastructure project — Oluku, Benin City.
      Stage 1: drainage system design and construction. Stage 2: shop unit
      structures, roofing and site infrastructure.</p></div>

  <div class="fig big"><img src="__olu_hero__" alt="Oluku market — site overview" />
    <div class="cap"><span class="t">Oluku Ultra Modern Market — Site Overview</span>
      <span class="m">Civil</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__olu_b__" alt="Drainage system construction" />
      <div class="cap"><span class="t">Drainage System Construction</span>
        <span class="m">Stage 1</span></div></div>
    <div class="fig half"><img src="__olu_c__" alt="Shop unit structure works" />
      <div class="cap"><span class="t">Shop Unit Structure Works</span>
        <span class="m">Stage 2</span></div></div>
  </div>
  __FOOT10__
</section>

<!-- ════════ 11 · SW07 · OFFICE INTERIOR, IBAFO ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 07</p>
    <h2>Office Interior Setup, Ibafo</h2>
    <p class="sub">Complete office interior fit-out — Ibafo, Ogun State.
      Space planning, partition walls, suspended ceilings, workstation
      installation, flooring and full MEP coordination.</p></div>

  <div class="fig big"><img src="__iba_hero__" alt="Ibafo office — interior overview" />
    <div class="cap"><span class="t">Office Interior — Overview</span>
      <span class="m">Interior</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__iba_b__" alt="Ibafo office — workstation area" />
      <div class="cap"><span class="t">Workstation Area</span>
        <span class="m">Fit-Out</span></div></div>
    <div class="fig half"><img src="__iba_c__" alt="Ibafo office — finish and detail" />
      <div class="cap"><span class="t">Interior Finish &amp; Detail</span>
        <span class="m">Detail</span></div></div>
  </div>
  __FOOT11__
</section>

<!-- ════════ 12 · CONTACT ════════ -->
<section class="sheet dark">
  <div class="contact">
    <p class="label">Get In Touch</p>
    <h2>Ready to Deliver Your Next Project?</h2>
    <p class="lead">Whether you need a site engineer, construction project
      manager, or fit-out specialist — let's talk about how I can bring your
      project from ground-breaking to handover.</p>
    <div class="cbtns">
      <a class="solid" href="mailto:vollmannakarakiri0@gmail.com">Send an Email</a>
      <a class="out" href="https://www.linkedin.com/in/vollmann-akarakiri-49127b1a0">LinkedIn Profile</a>
    </div>
    <div class="cdetails">
      <div class="ci"><div class="cl">Phone</div><div class="cv">+234 816 367 5439</div></div>
      <div class="ci"><div class="cl">Email</div><div class="cv">vollmannakarakiri0@gmail.com</div></div>
      <div class="ci"><div class="cl">Location</div><div class="cv">Lagos, Nigeria</div></div>
      <div class="ci"><div class="cl">LinkedIn</div><div class="cv"><a href="https://www.linkedin.com/in/vollmann-akarakiri-49127b1a0">linkedin.com/in/vollmann-akarakiri-49127b1a0</a></div></div>
      <div class="ci"><div class="cl">Availability</div><div class="cv">Worldwide &amp; remote</div></div>
      <div class="ci"><div class="cl">Education</div><div class="cv">MSc CEM · UEL</div></div>
    </div>
  </div>
  <div class="cfoot">Vollmann Olamide Akarakiri · Site. Structure. Delivered. On Time.</div>
</section>
"""


def build():
    body = BODY
    for key, uri in IMG.items():
        body = body.replace(f"__{key}__", uri)
    for n in (2, 4, 5, 6, 7, 8, 9, 10, 11):
        body = body.replace(f"__FOOT{n}__", FOOTER.format(n=f"{n:02d}"))

    html = (
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
        f"<style>{FONT_FACES}{CSS}</style></head><body>{body}</body></html>"
    )
    HTML(string=html, base_url=ROOT).write_pdf(OUT)
    print("Wrote", OUT, "·", round(os.path.getsize(OUT) / 1024), "KB")


if __name__ == "__main__":
    build()
