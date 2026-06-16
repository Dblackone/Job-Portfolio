#!/usr/bin/env python3
"""
Build a print-ready PDF portfolio for Vollmann Olamide Akarakiri.

The PDF mirrors the web portfolio's design system one-to-one:
  Warm off-white (#F5F2EE) · Terracotta (#B85C38) · Slate grey (#4A4F5C)
  Typeface: Inter (bundled in pdf/fonts as static .woff2 weights)

Fonts and images are embedded as base64 data URIs so the rendered PDF is
fully self-contained. Source images live in ../assets and are optimised
(resized + recompressed) in-memory at build time — nothing extra is written
to the repository besides the final PDF.

Run:  python3 pdf/build.py
Out:  assets/vollmann-akarakiri-portfolio.pdf
"""

import base64
import io
import os

from PIL import Image
from weasyprint import HTML

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
PICS = os.path.join(ASSETS, "Project Pictures")
FONT_DIR = os.path.join(ROOT, "pdf", "fonts")
OUT = os.path.join(ASSETS, "vollmann-akarakiri-portfolio.pdf")


# ───────────────────────── asset embedding helpers ─────────────────────────

def font_uri(weight):
    with open(os.path.join(FONT_DIR, f"inter-{weight}.woff2"), "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode()
    return f"data:font/woff2;base64,{b64}"


def img_uri(path, max_px=1280, quality=82, keep_alpha=False):
    """Optimise an image and return a base64 data URI."""
    im = Image.open(path)
    # Downscale so the longest edge is at most max_px.
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


# ───────────────────────────── source images ───────────────────────────────

PROFILE = os.path.join(ASSETS, "vollmann-akarakiri-profile.png")
ADO = os.path.join(PICS, "Ado Hall of Worship")
HILL = os.path.join(PICS, "Hillside Project")
LAND = os.path.join(PICS, "Landscape Projects")
USELU = os.path.join(PICS, "Uselu Family house")
SIXFLAT = os.path.join(PICS, "6-flat ikotun lagos")
INTOP = os.path.join(PICS, "Interior Residential Operations")
SCHEMA = os.path.join(PICS, "Concept schema projects")
IKEJA = os.path.join(PICS, "Design For Ikeja confencens room")

IMG = {
    "profile":      img_uri(PROFILE, max_px=760, keep_alpha=True),
    # 01 — Hall of Worship, Ado
    "ado_ext":      img_uri(os.path.join(ADO, "Ado Hero 2.png")),
    "ado_struct":   img_uri(os.path.join(ADO, "ADO CENTER RAW 1.jpg")),
    "ado_plan":     img_uri(os.path.join(ADO, "Screenshot 2026-05-16 091207.png"),
                            max_px=1400, quality=86),
    # 02 — Hillside (concept)
    "hill_hero":    img_uri(os.path.join(HILL, "HERO IMG.png")),
    "hill_massing": img_uri(os.path.join(HILL, "RAW 1.jpg")),
    "hill_detail":  img_uri(os.path.join(HILL, "02 Detail Study.png")),
    # 03 — Landscape & Site Development
    "land_main":    img_uri(os.path.join(LAND, "Aerial Site Overview.png")),
    "land_b":       img_uri(os.path.join(LAND, "Aerial Parking Court.png")),
    "land_c":       img_uri(os.path.join(LAND, "Video1 - Snapshot7_003.jpg")),
    # 04 — 4-Bedroom Family House, Uselu
    "uselu_hero":   img_uri(os.path.join(USELU, "Usele Hero 1.png")),
    "uselu_night":  img_uri(os.path.join(USELU, "USELU - NIGHT VIEW.png")),
    "uselu_col":    img_uri(os.path.join(USELU, "USELU - COLAGE.png")),
    # 05 — 6-Flat Apartment Block, Ikotun
    "sixflat_hero": img_uri(os.path.join(SIXFLAT, "MR CHINEDU PROJECT.jpg")),
    "sixflat_b":    img_uri(os.path.join(SIXFLAT, "MR CHINEDU PROJECT 2.jpg")),
    "sixflat_c":    img_uri(os.path.join(SIXFLAT, "MR CHINEDU PROJECT raw.jpg")),
    # Other Projects — gallery of additional (unused) work
    "g1": img_uri(os.path.join(INTOP, "RENDER 1.png"), max_px=860, quality=80),
    "g2": img_uri(os.path.join(ADO, "Image8_005.png"), max_px=860, quality=80),
    "g3": img_uri(os.path.join(IKEJA, "Image4_034.png"), max_px=860, quality=80),
    "g4": img_uri(os.path.join(LAND, "Video2 - Snapshot12_001.jpg"), max_px=860, quality=80),
    "g5": img_uri(os.path.join(INTOP, "RENDER 2.png"), max_px=860, quality=80),
    "g6": img_uri(os.path.join(SIXFLAT, "MR CHINEDU PROJECT 4.jpg"), max_px=860, quality=80),
    "g7": img_uri(os.path.join(IKEJA, "Image1_061.png"), max_px=860, quality=80),
    "g8": img_uri(os.path.join(SCHEMA, "BIG SCHEMA RAW 1.jpg"), max_px=860, quality=80),
    "g9": img_uri(os.path.join(SCHEMA, "3 BEDROOM TRERACE WITH PENT HOUSE - RAW 1.jpg"),
                  max_px=860, quality=80),
}

FONT_FACES = "".join(
    f"""@font-face{{font-family:'Inter';font-style:normal;font-weight:{w};
    src:url('{font_uri(w)}') format('woff2');}}"""
    for w in (300, 400, 500, 600, 700, 800)
)


# ───────────────────────────────── styles ──────────────────────────────────

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

/* ───── COVER ───── */
.cover::before{ content:''; position:absolute; left:0; top:0; bottom:0;
  width:9px; background:var(--accent); }
.cover-shape{ position:absolute; right:-70px; top:120px; width:340px;
  height:340px; background:var(--light); border-radius:50%; opacity:.5; }
.cover-top{ display:flex; align-items:center; justify-content:space-between;
  margin-bottom:24mm; }
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
.headline{ font-size:53px; font-weight:800; line-height:1.06;
  letter-spacing:-0.03em; }
.headline span{ display:block; }
.headline .accent{ color:var(--accent); }
.headline .muted{ color:var(--text); }
.hero-sub{ font-size:13px; font-weight:300; color:var(--text);
  margin-top:18px; max-width:96mm; line-height:1.7; }
.hero-points{ list-style:none; margin-top:18px; }
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

/* ───── ABOUT ───── */
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

/* ───── SOFTWARE (dark) ───── */
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
.sw .lv{ font-size:9px; color:var(--accent); font-weight:600;
  margin-bottom:6px; }
.sw p{ font-size:9.5px; color:rgba(232,228,223,.66); line-height:1.55; }
.disc{ display:flex; flex-wrap:wrap; gap:8px; margin-top:11mm;
  padding-top:8mm; border-top:1px solid rgba(255,255,255,.1); }
.disc span{ font-size:9px; font-weight:600; color:var(--accent);
  background:rgba(184,92,56,.15); border:1px solid rgba(184,92,56,.32);
  padding:5px 12px; border-radius:100px; letter-spacing:0.04em; }

/* ───── EXPERIENCE ───── */
.tl{ list-style:none; }
.tl li{ position:relative; padding:0 0 8mm 22px;
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

/* ───── EXPERTISE CARDS ───── */
.cards{ display:grid; grid-template-columns:1fr 1fr; gap:13px; }
.card{ background:var(--white); border:1px solid var(--border);
  border-radius:10px; overflow:hidden; }
.card .top{ height:4px; background:var(--accent); }
.card .bd{ padding:16px 17px; }
.card .ic{ width:36px; height:36px; background:var(--light); border-radius:7px;
  color:var(--accent); font-size:15px; display:flex; align-items:center;
  justify-content:center; margin-bottom:11px; }
.card h3{ font-size:14px; margin-bottom:6px; }
.card p{ font-size:10px; line-height:1.55; color:var(--text);
  margin-bottom:9px; }
.card .tag{ font-size:8.5px; font-weight:600; letter-spacing:0.04em;
  color:var(--accent); }

/* ───── SELECTED WORK ───── */
.fig{ border-radius:9px; overflow:hidden; border:1px solid var(--border);
  background:var(--white); margin-bottom:11px; }
.fig img{ width:100%; display:block; object-fit:cover; }
.fig .cap{ padding:9px 13px; display:flex; justify-content:space-between;
  align-items:baseline; gap:10px; }
.fig .cap .t{ font-size:10.5px; font-weight:600; color:var(--dark); }
.fig .cap .m{ font-size:8.5px; font-weight:600; letter-spacing:0.06em;
  text-transform:uppercase; color:var(--accent); white-space:nowrap; }
.fig.big img{ height:96mm; }
.fig.big.contain img{ object-fit:contain; height:90mm; background:var(--white); }
.fig.half img{ height:62mm; }
.row2{ display:grid; grid-template-columns:1fr 1fr; gap:11px; }

/* ───── OTHER PROJECTS GRID ───── */
.other-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:11px; }
.tile{ border:1px solid var(--border); border-radius:8px; overflow:hidden;
  background:var(--white); }
.tile img{ width:100%; height:44mm; object-fit:cover; display:block; }
.tile .cap{ padding:7px 10px; }
.tile .cap .t{ font-size:9.5px; font-weight:600; color:var(--dark);
  display:block; line-height:1.3; }
.tile .cap .m{ font-size:7.5px; font-weight:600; letter-spacing:0.07em;
  text-transform:uppercase; color:var(--accent); }

/* ───── CONTACT (dark) ───── */
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

/* ───── page footer (light interior pages) ───── */
.pfoot{ position:absolute; left:16mm; right:16mm; bottom:9mm;
  display:flex; justify-content:space-between; align-items:center;
  font-size:8px; color:#9a948e; letter-spacing:0.05em;
  border-top:1px solid var(--border); padding-top:6px; }
.pfoot .nm{ text-transform:uppercase; }
"""


# ───────────────────────────────── content ─────────────────────────────────

def icon_card(glyph, dark=False):
    return glyph


PORTFOLIO_FOOTER = (
    '<div class="pfoot"><span class="nm">Vollmann Olamide Akarakiri · '
    'Construction Project Manager</span><span>{n} / 12</span></div>'
)

BODY = """
<!-- ════════ 1 · COVER ════════ -->
<section class="sheet cover">
  <div class="cover-shape"></div>
  <div class="cover-top">
    <div class="brand"><div class="mark">V</div>
      <div class="nm">Vollmann&nbsp;Akarakiri</div></div>
    <div class="cover-tag">Professional Portfolio · 2026</div>
  </div>

  <div class="hero">
    <div>
      <p class="label hero-label">Construction Project Manager · BIM Specialist · Lagos, Nigeria</p>
      <div class="headline">
        <span>Architecture.</span>
        <span class="accent">BIM.</span>
        <span>Construction.</span>
        <span class="muted">Delivered.</span>
      </div>
      <p class="hero-sub">From Revit model to built reality — concept through
        handover. Five years delivering residential, commercial and mixed-use
        projects across Nigeria.</p>
      <ul class="hero-points">
        <li>5+ years of progressive construction &amp; design leadership</li>
        <li>20+ concurrent project sites coordinated</li>
        <li>&#8358;350M+ cumulative project value · &#8358;10M+ savings delivered</li>
        <li>MSc Construction Engineering Management — UEL, London</li>
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
          <div class="b"><div class="n">20+</div><div class="l">Sites managed</div></div>
          <div class="b"><div class="n">&#8358;350M+</div><div class="l">Project value</div></div>
          <div class="b"><div class="n">5+</div><div class="l">Years</div></div>
        </div>
        <div class="psw">
          <span>Revit</span><span>Dynamo</span><span>AutoCAD</span>
          <span>Navisworks</span><span>MS Project</span>
        </div>
        <div class="avail"><div class="dot"></div>
          <span>Open to opportunities — worldwide &amp; remote</span></div>
      </div>
    </aside>
  </div>

  <div class="cover-foot">
    <div class="ci"><div class="cl">Phone</div><div class="cv">+234 816 367 5439</div></div>
    <div class="ci"><div class="cl">Email</div><div class="cv">vollmannakarakiri0@gmail.com</div></div>
    <div class="ci"><div class="cl">Location</div><div class="cv">Lagos, Nigeria</div></div>
    <div class="ci"><div class="cl">LinkedIn</div><div class="cv">linkedin.com/in/vollmannakarakiri</div></div>
  </div>
</section>

<!-- ════════ 2 · ABOUT ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Professional Profile</p>
    <h2>The Professional Behind the Work</h2></div>

  <div class="about">
    <div>
      <p>Vollmann Olamide Akarakiri is a results-driven Construction Project
        Manager with 5+ years delivering residential, commercial, and
        mixed-use building projects from planning and design through execution
        and completion across multiple Nigerian states.</p>
      <p>He has coordinated 20+ concurrent project sites and contributed to
        projects exceeding &#8358;350 million in cumulative value — generating
        over &#8358;10 million in savings through cost control, procurement
        oversight, and error prevention.</p>
      <p>Skilled in planning and scheduling, budgeting and cost forecasting,
        contract and procurement administration, regulatory compliance, site
        supervision and health &amp; safety — with strong technical capability
        in BIM (Revit, AutoCAD, Dynamo, Navisworks).</p>
      <div class="stat-grid">
        <div class="st"><div class="n">20+</div><div class="d">Concurrent sites coordinated</div></div>
        <div class="st"><div class="n">&#8358;350M+</div><div class="d">Cumulative project value</div></div>
        <div class="st"><div class="n">&#8358;10M+</div><div class="d">Savings delivered</div></div>
        <div class="st"><div class="n">110+</div><div class="d">Projects contributed to</div></div>
      </div>
    </div>

    <div>
      <p class="label" style="margin-bottom:9px;">Core Competencies</p>
      <div class="skill-group"><h4>Project &amp; Construction Management</h4>
        <div class="pills"><span>Planning &amp; Scheduling</span>
          <span>Budgeting &amp; Cost Forecasting</span>
          <span>Procurement &amp; Contracts</span>
          <span>Site &amp; Subcontractor Management</span>
          <span>Risk Management</span><span>Quality Control</span></div></div>
      <div class="skill-group"><h4>Design &amp; BIM</h4>
        <div class="pills"><span>Design Coordination</span>
          <span>BIM Modelling (Revit)</span><span>Dynamo Automation</span>
          <span>Navisworks Coordination</span><span>Working Drawings</span></div></div>
      <div class="skill-group"><h4>Compliance &amp; HSE</h4>
        <div class="pills"><span>Building Codes &amp; Approvals</span>
          <span>Health &amp; Safety (HSE)</span><span>Risk Assessments</span>
          <span>Stakeholder Reporting</span></div></div>
      <div class="skill-group"><h4>Specialist Areas</h4>
        <div class="pills"><span>Interior &amp; Landscape Design</span>
          <span>Furniture &amp; Kitchen Design</span><span>MEP Coordination</span>
          <span>Cost Estimation</span></div></div>
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

<!-- ════════ 3 · SOFTWARE & BIM ════════ -->
<section class="sheet dark">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Technical Expertise</p>
    <h2>Software &amp; BIM Skills</h2>
    <p class="sub">Industry-standard tools deployed across every project phase —
      from digital model to physical delivery.</p></div>

  <div class="sw-grid">
    <div class="sw"><div class="ic">&#9670;</div><h4>Autodesk Revit</h4>
      <div class="lv">Expert — BIM Modelling</div>
      <p>Full architectural BIM models for 30+ office, residential and interior
        projects. Family creation, documentation sheets, schedules and
        coordinated model production.</p></div>
    <div class="sw"><div class="ic">&#9671;</div><h4>Dynamo for Revit</h4>
      <div class="lv">Advanced — Parametric Automation</div>
      <p>Custom parametric workflows and automation scripts that reduce
        documentation time and enable data-driven design coordination.</p></div>
    <div class="sw"><div class="ic">&#9633;</div><h4>AutoCAD</h4>
      <div class="lv">Expert — Technical Drawing</div>
      <p>2D technical drawing, site plans, detailed construction and working
        drawings, and detailing packages for 10+ residential properties.</p></div>
    <div class="sw"><div class="ic">&#9650;</div><h4>Navisworks</h4>
      <div class="lv">Proficient — BIM Coordination</div>
      <p>Multi-discipline model coordination, clash detection and resolution,
        4D construction sequencing and project review workflows.</p></div>
    <div class="sw"><div class="ic">&#9632;</div><h4>Microsoft Project</h4>
      <div class="lv">Proficient — Project Scheduling</div>
      <p>Scheduling, milestone tracking, resource planning and programme
        management for large multi-site construction programmes.</p></div>
    <div class="sw"><div class="ic">&#9679;</div><h4>MS Excel &amp; Office Suite</h4>
      <div class="lv">Advanced — Reporting &amp; Cost Control</div>
      <p>Budget tracking, cost forecasting, progress reporting, procurement
        schedules and management reporting across concurrent sites.</p></div>
  </div>

  <div class="disc">
    <span>Project Planning &amp; Scheduling</span><span>BIM Coordination</span>
    <span>Budgeting &amp; Cost Forecasting</span><span>Procurement &amp; Contracts</span>
    <span>Site Engineering</span><span>Health &amp; Safety (HSE)</span>
    <span>Risk Management</span><span>Design Coordination</span>
    <span>Quality Control</span><span>Regulatory Compliance</span>
    <span>Stakeholder Reporting</span><span>MEP Coordination</span>
  </div>
</section>

<!-- ════════ 4 · EXPERIENCE ════════ -->
<section class="sheet">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Career History</p>
    <h2>Professional Experience</h2>
    <p class="sub">5+ years of progressive responsibility across construction,
      site engineering and design — from intern to Engineering Lead.</p></div>

  <ul class="tl">
    <li class="cur"><div class="pe">Aug 2021 – Feb 2026</div>
      <div class="ro">Project Manager / Engineering Lead</div>
      <div class="co">Nu-Avenue Company Resources</div>
      <ul><li>Directed construction delivery across 20+ concurrent project sites
        in multiple Nigerian states, contributing to projects exceeding
        &#8358;350 million in cumulative value.</li>
        <li>Generated over &#8358;10 million in savings through cost control,
          vendor coordination and error prevention.</li>
        <li>Produced BIM models for 30+ office, 10+ residential and 10+
          interior projects.</li>
        <li>Coordinated architects, consultants, engineers, suppliers and
          contractors to ensure quality, safety and on-time delivery.</li></ul></li>
    <li><div class="pe">Jun 2020 – Aug 2021</div>
      <div class="ro">Site Engineer / Assistant Technical Designer</div>
      <div class="co">Nature's Beauty Construction</div>
      <ul><li>Planned and supervised 110+ site-development and landscape
        projects across multiple states.</li>
        <li>Produced detailing packages for 10+ residential properties.</li>
        <li>Trained 5+ employees; contributed to business opportunities
          exceeding &#8358;20 million.</li></ul></li>
    <li><div class="pe">Dec 2019 – Apr 2020</div>
      <div class="ro">Site Supervisor</div>
      <div class="co">Lego Construction Company</div>
      <ul><li>Developed project plans, contract documents, schedules and
        budgets.</li>
        <li>Facilitated interdisciplinary coordination meetings and supported
          client engagement.</li></ul></li>
    <li><div class="pe">Aug 2017 – Dec 2017</div>
      <div class="ro">Architecture &amp; Planning Intern</div>
      <div class="co">Danzinger Nigeria Ltd</div>
      <ul><li>Assisted management of consulting activities exceeding
        &#8358;10 million.</li>
        <li>Assisted drafting, BIM updates and documentation.</li></ul></li>
    <li><div class="pe">Nov 2015 – Feb 2016</div>
      <div class="ro">Landscape Design &amp; HSE Intern</div>
      <div class="co">Nature's Beauty Construction</div>
      <ul><li>Participated in on-site HSE activities and risk assessments.</li>
        <li>Performed material, equipment and cost estimation for planning.</li></ul></li>
  </ul>

  <div class="metrics">
    <div class="st"><div class="n">&#8358;350M+</div><div class="d">Total project value managed</div></div>
    <div class="st"><div class="n">&#8358;10M+</div><div class="d">Savings generated</div></div>
    <div class="st"><div class="n">110+</div><div class="d">Projects contributed to</div></div>
    <div class="st"><div class="n">30+</div><div class="d">BIM models produced</div></div>
  </div>
  __FOOT4__
</section>

<!-- ════════ 5 · AREAS OF EXPERTISE ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Portfolio</p>
    <h2>Areas of Expertise</h2>
    <p class="sub">Seven specialist disciplines — one integrated professional
      delivering from concept to completion.</p></div>

  <div class="cards">
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9670;</div><h3>Building Projects</h3>
      <p>30+ office, 10+ residential and 10+ interior projects delivered. Full
        architectural design and BIM documentation from concept through
        construction drawings.</p>
      <div class="tag">50+ PROJECTS DELIVERED</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9671;</div><h3>BIM &amp; Revit</h3>
      <p>Advanced BIM modelling, Dynamo automation, Navisworks coordination and
        construction documentation across residential, office and interior
        projects.</p>
      <div class="tag">REVIT · DYNAMO · NAVISWORKS</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9633;</div><h3>Residential &amp; Schematic Design</h3>
      <p>Residential design and schematic drawings for housing developments —
        space planning, layout design and technical documentation packages.</p>
      <div class="tag">HOUSING &amp; LAYOUTS</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9650;</div><h3>Landscape Design</h3>
      <p>110+ site-development and landscape projects across multiple states —
        hardscape, softscape, drainage integration and site beautification.</p>
      <div class="tag">110+ SITE PROJECTS</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9632;</div><h3>Construction &amp; Site Engineering</h3>
      <p>End-to-end site engineering across 20+ concurrent sites — excavation,
        foundations, structural works, drainage, roofing, finishes and
        handover.</p>
      <div class="tag">20+ CONCURRENT SITES</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9679;</div><h3>Furniture &amp; Kitchen Design</h3>
      <p>Bespoke furniture and kitchen design — layout planning, material
        specification and design documentation for residential and commercial
        fit-outs.</p>
      <div class="tag">BESPOKE FIT-OUTS</div></div></div>
  </div>
  __FOOT5__
</section>

<!-- ════════ 6 · SELECTED WORK 01 — HALL OF WORSHIP, ADO ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 01</p>
    <h2>Hall of Worship, Ado</h2>
    <p class="sub">From architectural visualisation to coordinated structural
      model and construction documentation.</p></div>

  <div class="fig big"><img src="__ado_ext__" alt="Hall of Worship visualisation" />
    <div class="cap"><span class="t">Hall of Worship — Architectural Visualisation</span>
      <span class="m">Render</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__ado_struct__" alt="Structural BIM model" />
      <div class="cap"><span class="t">Structural BIM Model</span>
        <span class="m">Revit</span></div></div>
    <div class="fig half"><img src="__ado_plan__" alt="Proposed floor plan" />
      <div class="cap"><span class="t">Proposed Floor Plan</span>
        <span class="m">Documentation</span></div></div>
  </div>
  __FOOT6__
</section>

<!-- ════════ 7 · SELECTED WORK 02 — HILLSIDE (CONCEPT) ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 02</p>
    <h2>The Hillside Project</h2>
    <p class="sub">Concept design — residential apartments set into a
      challenging hillside terrain.</p></div>

  <div class="fig big"><img src="__hill_hero__" alt="Hillside residence street approach" />
    <div class="cap"><span class="t">Street Approach — Hillside Residence</span>
      <span class="m">Render</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__hill_massing__" alt="Hillside massing on sloped terrain" />
      <div class="cap"><span class="t">Massing on Sloped Terrain</span>
        <span class="m">Concept</span></div></div>
    <div class="fig half"><img src="__hill_detail__" alt="Hillside material and facade study" />
      <div class="cap"><span class="t">Material &amp; Façade Study</span>
        <span class="m">Detail</span></div></div>
  </div>
  __FOOT7__
</section>

<!-- ════════ 8 · SELECTED WORK 03 — LANDSCAPE & SITE DEVELOPMENT ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 03</p>
    <h2>Landscape &amp; Site Development</h2>
    <p class="sub">110+ site-development and landscape projects — master
      planning, hardscape and softscape integration, and visualisation.</p></div>

  <div class="fig big"><img src="__land_main__" alt="Aerial site overview" />
    <div class="cap"><span class="t">Site Master Plan — Aerial Overview</span>
      <span class="m">Aerial</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__land_b__" alt="Parking court and planting" />
      <div class="cap"><span class="t">Parking Court &amp; Planting</span>
        <span class="m">Render</span></div></div>
    <div class="fig half"><img src="__land_c__" alt="Residence and carport render" />
      <div class="cap"><span class="t">Residence &amp; Carport</span>
        <span class="m">Render</span></div></div>
  </div>
  __FOOT8__
</section>

<!-- ════════ 9 · SELECTED WORK 04 — 4-BEDROOM FAMILY HOUSE, USELU ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 04</p>
    <h2>4-Bedroom Family House, Uselu</h2>
    <p class="sub">A four-bedroom family residence — Uselu, Benin City.</p></div>

  <div class="fig big"><img src="__uselu_hero__" alt="Uselu family house street view" />
    <div class="cap"><span class="t">Street View — 4-Bedroom Family House</span>
      <span class="m">Render</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__uselu_night__" alt="Uselu family house night elevation" />
      <div class="cap"><span class="t">Night Elevation</span>
        <span class="m">Render</span></div></div>
    <div class="fig half"><img src="__uselu_col__" alt="Uselu material and detail study" />
      <div class="cap"><span class="t">Material &amp; Detail Study</span>
        <span class="m">Details</span></div></div>
  </div>
  __FOOT9__
</section>

<!-- ════════ 10 · SELECTED WORK 05 — 6-FLAT APARTMENT BLOCK, IKOTUN ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 05</p>
    <h2>6-Flat Apartment Block, Ikotun</h2>
    <p class="sub">Three-storey six-flat residential development — Ikotun,
      Lagos. BIM design, massing and material study.</p></div>

  <div class="fig big"><img src="__sixflat_hero__" alt="Six-flat apartment block model" />
    <div class="cap"><span class="t">Six-Flat Apartment Block</span>
      <span class="m">BIM Model</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__sixflat_b__" alt="Façade and material study" />
      <div class="cap"><span class="t">Façade &amp; Material Study</span>
        <span class="m">Detail</span></div></div>
    <div class="fig half"><img src="__sixflat_c__" alt="Massing and structure model" />
      <div class="cap"><span class="t">Massing &amp; Structure</span>
        <span class="m">Revit</span></div></div>
  </div>
  __FOOT10__
</section>

<!-- ════════ 11 · OTHER PROJECTS ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">More Work</p>
    <h2>Other Projects</h2>
    <p class="sub">A selection of additional design, interior and visualisation
      work from across the portfolio.</p></div>

  <div class="other-grid">
    <div class="tile"><img src="__g1__" alt="Interior living space" />
      <div class="cap"><span class="t">Living Space</span><span class="m">Interior</span></div></div>
    <div class="tile"><img src="__g2__" alt="Hall of Worship concept" />
      <div class="cap"><span class="t">Hall of Worship, Ado</span><span class="m">Concept</span></div></div>
    <div class="tile"><img src="__g3__" alt="Conference room, Ikeja" />
      <div class="cap"><span class="t">Conference Room, Ikeja</span><span class="m">Interior</span></div></div>
    <div class="tile"><img src="__g4__" alt="Residence and driveway" />
      <div class="cap"><span class="t">Residence &amp; Driveway</span><span class="m">Render</span></div></div>
    <div class="tile"><img src="__g5__" alt="Family lounge" />
      <div class="cap"><span class="t">Family Lounge</span><span class="m">Interior</span></div></div>
    <div class="tile"><img src="__g6__" alt="6-flat apartments model" />
      <div class="cap"><span class="t">6-Flat Apartments</span><span class="m">BIM Model</span></div></div>
    <div class="tile"><img src="__g7__" alt="Boardroom, Ikeja" />
      <div class="cap"><span class="t">Boardroom, Ikeja</span><span class="m">Interior</span></div></div>
    <div class="tile"><img src="__g8__" alt="Residential schematic" />
      <div class="cap"><span class="t">Residential Schematic</span><span class="m">Concept</span></div></div>
    <div class="tile"><img src="__g9__" alt="3-bedroom terrace schematic" />
      <div class="cap"><span class="t">3-Bedroom Terrace</span><span class="m">Concept</span></div></div>
  </div>
  __FOOT11__
</section>

<!-- ════════ 12 · CONTACT ════════ -->
<section class="sheet dark">
  <div class="contact">
    <p class="label">Get In Touch</p>
    <h2>Ready to Work Together?</h2>
    <p class="lead">Whether you are an architecture firm, construction company,
      BIM consultancy or project owner — let's discuss how I can add value to
      your next project or team.</p>
    <div class="cbtns">
      <a class="solid" href="mailto:vollmannakarakiri0@gmail.com">Send an Email</a>
      <a class="out" href="https://linkedin.com/in/vollmannakarakiri">LinkedIn Profile</a>
    </div>
    <div class="cdetails">
      <div class="ci"><div class="cl">Phone</div><div class="cv">+234 816 367 5439</div></div>
      <div class="ci"><div class="cl">Email</div><div class="cv">vollmannakarakiri0@gmail.com</div></div>
      <div class="ci"><div class="cl">Location</div><div class="cv">Lagos, Nigeria</div></div>
      <div class="ci"><div class="cl">LinkedIn</div><div class="cv">linkedin.com/in/vollmannakarakiri</div></div>
      <div class="ci"><div class="cl">Availability</div><div class="cv">Worldwide &amp; remote</div></div>
      <div class="ci"><div class="cl">Education</div><div class="cv">MSc CEM · UEL</div></div>
    </div>
  </div>
  <div class="cfoot">Vollmann Olamide Akarakiri · Architecture. BIM. Construction. Delivered.</div>
</section>
"""


def build():
    body = BODY
    for key, uri in IMG.items():
        body = body.replace(f"__{key}__", uri)
    for n in (2, 4, 5, 6, 7, 8, 9, 10, 11):
        body = body.replace(f"__FOOT{n}__", PORTFOLIO_FOOTER.format(n=f"{n:02d}"))

    html = (
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
        f"<style>{FONT_FACES}{CSS}</style></head><body>{body}</body></html>"
    )
    HTML(string=html, base_url=ROOT).write_pdf(OUT)
    print("Wrote", OUT, "·", round(os.path.getsize(OUT) / 1024), "KB")


if __name__ == "__main__":
    build()
