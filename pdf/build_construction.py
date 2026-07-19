#!/usr/bin/env python3
"""
Construction Portfolio — Vollmann Olamide Akarakiri
Merged construction + site-projects portfolio built around four flagship site
projects with real site photography.

Selected works:
  01 · 6-Flat Residential Block — Ikotun, Lagos
  02 · 6-Bedroom Duplex         — Ado, Ekiti State
  03 · Oluku Ultra Modern Market — Benin City (drainage + shop structures)
  04 · The Body Shop Outlets    — Ikeja City Mall + Circle Mall Lekki

Structure: cover · merged profile+toolkit · four selected works · contact.

Run:  python3 pdf/build_construction.py
Out:  assets/vollmann-akarakiri-construction-portfolio.pdf
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
OUT      = os.path.join(ASSETS, "vollmann-akarakiri-construction-portfolio.pdf")

TOTAL_PAGES = 7


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
    "cover_band": img_uri(os.path.join(IKOTUN, "ikotun-facade.jpg"),
                          max_px=1600, quality=84),

    # ── SW01 · Ikotun 6-Flat Block ────────────────────────────────────────
    "ikt_hero": img_uri(os.path.join(IKOTUN, "ikotun-onsite-01.jpg"), max_px=1600),
    "ikt_b":    img_uri(os.path.join(IKOTUN, "ikotun-onsite-03.jpg")),
    "ikt_c":    img_uri(os.path.join(IKOTUN, "ikotun-render.png")),

    # ── SW02 · Ado 6-Bedroom Duplex ───────────────────────────────────────
    "ado_hero": img_uri(os.path.join(ADO_DUP, "ado-duplex-structural-01.jpg"), max_px=1600),
    "ado_b":    img_uri(os.path.join(ADO_DUP, "ado-duplex-structural-04.jpg")),
    "ado_c":    img_uri(os.path.join(ADO_DUP, "ado-duplex-interior-05.jpg")),

    # ── SW03 · Oluku Ultra Modern Market ──────────────────────────────────
    "olu_hero": img_uri(os.path.join(OLUKU, "oluku-site-00.jpg"), max_px=1600),
    "olu_b":    img_uri(os.path.join(OLUKU, "oluku-site-06.jpg")),
    "olu_c":    img_uri(os.path.join(OLUKU, "oluku-site-07.jpg")),

    # ── SW04 · The Body Shop Outlets ──────────────────────────────────────
    "bs_hero":  img_uri(os.path.join(BODY_SHOP, "body-shop-retail-floor.jpeg"), max_px=1600),
    "bs_b":     img_uri(os.path.join(BODY_SHOP, "body-shop-wip-01.jpg")),
    "bs_c":     img_uri(os.path.join(BODY_SHOP, "body-shop-mural-display.jpeg")),
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
.hero-points li::before{ content:'\\2192'; position:absolute; left:0;
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
.tl ul li::before{ content:'\\2192'; left:0; top:2px; width:auto; height:auto;
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

/* compact technical toolkit (merged onto the profile page) */
.tk-grid{ display:grid; grid-template-columns:1fr 1fr; gap:7px; }
.tk{ background:var(--bg); border-radius:6px; padding:8px 11px;
  border-left:2px solid var(--accent); }
.tk .tkn{ display:block; font-size:10.5px; font-weight:600; color:var(--dark); }
.tk .tkl{ display:block; font-size:8.5px; color:var(--accent); margin-top:1px; }

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
    <div class="cover-tag">Construction Portfolio · 2026</div>
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
      <p class="hero-sub">Four flagship site projects — a six-flat residential
        block, a six-bedroom duplex, a market infrastructure scheme and an
        international retail fit-out — delivered across Lagos, Ekiti and Benin
        City.</p>
      <ul class="hero-points">
        <li>6-Flat Residential Block — Ikotun, Lagos</li>
        <li>6-Bedroom Duplex — Ado, Ekiti State</li>
        <li>Oluku Ultra Modern Market — Benin City</li>
        <li>The Body Shop retail fit-out — Ikeja &amp; Lekki, Lagos</li>
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
    <img src="__cover_band__" alt="6-Flat residential block — Ikotun, Lagos" />
    <div class="cap">6-Flat Residential Block — Ikotun, Lagos</div>
  </div>

  <div class="cover-foot">
    <div class="ci"><div class="cl">Phone</div><div class="cv">+234 816 367 5439</div></div>
    <div class="ci"><div class="cl">Email</div><div class="cv">vollmannakarakiri0@gmail.com</div></div>
    <div class="ci"><div class="cl">Location</div><div class="cv">Lagos, Nigeria</div></div>
    <div class="ci"><div class="cl">LinkedIn</div><div class="cv"><a href="https://www.linkedin.com/in/vollmann-akarakiri-49127b1a0">/in/vollmann-akarakiri-49127b1a0</a></div></div>
  </div>
</section>

<!-- ════════ 2 · PROFILE + TECHNICAL TOOLKIT (merged) ════════ -->
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
      <p>His site experience spans residential buildings from foundation to
        finish, market and drainage infrastructure, and retail fit-outs for
        international brands — coordinating subcontractors, procurement, quality
        control and programme on each project, and bridging BIM model to built
        reality.</p>
      <div class="stat-grid">
        <div class="st"><div class="n">30+</div><div class="d">Total projects across all disciplines</div></div>
        <div class="st"><div class="n">&#8358;350M+</div><div class="d">Cumulative project value</div></div>
        <div class="st"><div class="n">&#8358;10M+</div><div class="d">Savings delivered</div></div>
        <div class="st"><div class="n">7+</div><div class="d">Years of experience</div></div>
      </div>
      <div class="edu-grid" style="margin-top:8mm;">
        <div class="edu"><div class="dg">MSc Construction Engineering Management</div>
          <div class="in">University of East London</div>
          <div class="pe">Sep 2024 – Present</div></div>
        <div class="edu"><div class="dg">BSc Building Technology</div>
          <div class="in">Federal University of Technology, Akure</div>
          <div class="pe">2014 – 2019</div></div>
      </div>
    </div>

    <div>
      <p class="label" style="margin-bottom:9px;">Site &amp; Construction Competencies</p>
      <div class="skill-group"><h4>Site Engineering &amp; Supervision</h4>
        <div class="pills"><span>Subcontractor Management</span>
          <span>Quality Control</span><span>Site Safety (HSE)</span>
          <span>Snagging &amp; Handover</span></div></div>
      <div class="skill-group"><h4>Structural, Civil &amp; Fit-Out</h4>
        <div class="pills"><span>Foundations &amp; Blockwork</span>
          <span>Drainage Systems</span><span>Roofing</span>
          <span>Retail Fit-Out</span><span>Joinery &amp; MEP</span></div></div>
      <div class="skill-group"><h4>Project &amp; Programme Management</h4>
        <div class="pills"><span>Planning &amp; Scheduling</span>
          <span>Cost Control</span><span>Procurement &amp; Contracts</span>
          <span>Stakeholder Reporting</span></div></div>

      <p class="label" style="margin:7mm 0 8px;">Technical Toolkit</p>
      <div class="tk-grid">
        <div class="tk"><span class="tkn">Autodesk Revit</span><span class="tkl">Expert · BIM coordination</span></div>
        <div class="tk"><span class="tkn">Navisworks</span><span class="tkl">Proficient · Clash detection</span></div>
        <div class="tk"><span class="tkn">AutoCAD</span><span class="tkl">Expert · Shop drawings</span></div>
        <div class="tk"><span class="tkn">MS Project</span><span class="tkl">Proficient · Programme</span></div>
        <div class="tk"><span class="tkn">Dynamo</span><span class="tkl">Advanced · Automation</span></div>
        <div class="tk"><span class="tkn">MS Excel &amp; Office</span><span class="tkl">Advanced · Cost control</span></div>
      </div>
    </div>
  </div>
  __FOOT2__
</section>

<!-- ════════ 3 · SW01 · IKOTUN 6-FLAT BLOCK ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 01</p>
    <h2>6-Flat Residential Block, Ikotun</h2>
    <p class="sub">Six-flat residential development, Ikotun, Lagos — built from
      foundation. Structural frame, column casting, suspended slabs and
      superstructure through to the finished block.</p></div>

  <div class="fig big"><img src="__ikt_hero__" alt="Ikotun 6-flat — structural works" />
    <div class="cap"><span class="t">Superstructure Under Construction</span>
      <span class="m">Structure</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__ikt_b__" alt="Ikotun suspended slab works" />
      <div class="cap"><span class="t">Suspended Slab &amp; Deck Works</span>
        <span class="m">Civil</span></div></div>
    <div class="fig half"><img src="__ikt_c__" alt="Ikotun completed block render" />
      <div class="cap"><span class="t">Completed 6-Flat Block</span>
        <span class="m">Outcome</span></div></div>
  </div>
  __FOOT3__
</section>

<!-- ════════ 4 · SW02 · ADO 6-BEDROOM DUPLEX ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 02</p>
    <h2>6-Bedroom Duplex, Ado</h2>
    <p class="sub">Six-bedroom duplex residence, Ado, Ekiti State — two-stage
      delivery: structural works (foundation, columns, slabs, roofing) followed
      by full interior finishes.</p></div>

  <div class="fig big"><img src="__ado_hero__" alt="Ado duplex — structural stage" />
    <div class="cap"><span class="t">Structural Stage &amp; Roofing</span>
      <span class="m">Structure</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__ado_b__" alt="Ado duplex — scaffolded elevation" />
      <div class="cap"><span class="t">Scaffolded Front Elevation</span>
        <span class="m">Construction</span></div></div>
    <div class="fig half"><img src="__ado_c__" alt="Ado duplex — interior finishes stage" />
      <div class="cap"><span class="t">Interior Finishes Stage</span>
        <span class="m">Finish</span></div></div>
  </div>
  __FOOT4__
</section>

<!-- ════════ 5 · SW03 · OLUKU ULTRA MODERN MARKET ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 03</p>
    <h2>Oluku Ultra Modern Market</h2>
    <p class="sub">Two-stage market infrastructure project — Oluku, Benin City.
      Stage 1: drainage system design and construction. Stage 2: shop unit
      structures, setting-out and site infrastructure.</p></div>

  <div class="fig big"><img src="__olu_hero__" alt="Oluku market — drainage channel" />
    <div class="cap"><span class="t">Reinforced Drainage Channel</span>
      <span class="m">Civil · Stage 1</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__olu_b__" alt="Oluku shop unit structure works" />
      <div class="cap"><span class="t">Shop Unit Structures</span>
        <span class="m">Stage 2</span></div></div>
    <div class="fig half"><img src="__olu_c__" alt="Oluku setting-out and survey" />
      <div class="cap"><span class="t">Setting-Out &amp; Survey</span>
        <span class="m">Site</span></div></div>
  </div>
  __FOOT5__
</section>

<!-- ════════ 6 · SW04 · THE BODY SHOP ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 04</p>
    <h2>The Body Shop Outlets</h2>
    <p class="sub">Retail fit-out for two The Body Shop outlets — Ikeja City Mall
      and Circle Mall Lekki, Lagos. Delivered from bare shell to trading floor:
      joinery, flooring, fixtures, MEP and brand installation.</p></div>

  <div class="fig big"><img src="__bs_hero__" alt="The Body Shop — finished retail floor" />
    <div class="cap"><span class="t">Finished Retail Trading Floor</span>
      <span class="m">Fit-Out</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__bs_b__" alt="Body Shop bare shell before fit-out" />
      <div class="cap"><span class="t">Bare Shell — Before Fit-Out</span>
        <span class="m">Stage</span></div></div>
    <div class="fig half"><img src="__bs_c__" alt="Body Shop mural feature wall and display" />
      <div class="cap"><span class="t">Feature Mural Wall &amp; Display</span>
        <span class="m">Interior</span></div></div>
  </div>
  __FOOT6__
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
    for n in (2, 3, 4, 5, 6):
        body = body.replace(f"__FOOT{n}__", FOOTER.format(n=f"{n:02d}"))

    html = (
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
        f"<style>{FONT_FACES}{CSS}</style></head><body>{body}</body></html>"
    )
    HTML(string=html, base_url=ROOT).write_pdf(OUT)
    print("Wrote", OUT, "·", round(os.path.getsize(OUT) / 1024), "KB")


if __name__ == "__main__":
    build()
