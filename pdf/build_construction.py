#!/usr/bin/env python3
"""
Construction Portfolio — Vollmann Olamide Akarakiri
Generates a print-ready A4 PDF showcasing construction, site engineering
and BIM project management work.

Run:  python3 pdf/build_construction.py
Out:  assets/vollmann-akarakiri-construction-portfolio.pdf
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
OUT = os.path.join(ASSETS, "vollmann-akarakiri-construction-portfolio.pdf")

TOTAL_PAGES = 12


def font_uri(weight):
    with open(os.path.join(FONT_DIR, f"inter-{weight}.woff2"), "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode()
    return f"data:font/woff2;base64,{b64}"


def img_uri(path, max_px=1280, quality=82, keep_alpha=False):
    im = Image.open(path)
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
        im.save(buf, format="JPEG", quality=quality, optimize=True, progressive=True)
        mime = "image/jpeg"
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"data:{mime};base64,{b64}"


ADO    = os.path.join(PICS, "Ado Hall of Worship")
HILL   = os.path.join(PICS, "Hillside Project")
LAND   = os.path.join(PICS, "Landscape Projects")
USELU  = os.path.join(PICS, "Uselu Family house")
SIXFL  = os.path.join(PICS, "6-flat ikotun lagos")
OTHER  = os.path.join(PICS, "Other Renders")
SCHEMA = os.path.join(PICS, "Concept schema projects")
RENO   = os.path.join(PICS, "Renovation Akure")

IMG = {
    "profile":      img_uri(os.path.join(ASSETS, "vollmann-akarakiri-profile.png"),
                            max_px=760, keep_alpha=True),
    # Cover band — aerial estate masterplan
    "cover_band":   img_uri(os.path.join(LAND, "Estate Aerial Hero.png"),
                            max_px=1600, quality=84),
    # About / expertise band — renovation render
    "reno_band":    img_uri(os.path.join(RENO, "Akure Family Home.png"),
                            max_px=1600, quality=84),

    # ── SW 01: Hall of Worship, Ado ──
    "ado_hero":     img_uri(os.path.join(ADO, "Ado Hero 2.png")),
    "ado_raw":      img_uri(os.path.join(ADO, "ADO CENTER RAW 1.jpg")),
    "ado_plan":     img_uri(os.path.join(ADO, "Screenshot 2026-05-16 091207.png"),
                            max_px=1400, quality=86),

    # ── SW 02: Landscape & Site Development ──
    "land_hero":    img_uri(os.path.join(LAND, "Aerial Site Overview.png")),
    "land_b":       img_uri(os.path.join(LAND, "Aerial Parking Court.png")),
    "land_c":       img_uri(os.path.join(LAND, "Video1 - Snapshot7_003.jpg")),

    # ── SW 03: 6-Flat Apartment Block, Ikotun ──
    "six_hero":     img_uri(os.path.join(SIXFL, "Chinedu Hero Render.png")),
    "six_b":        img_uri(os.path.join(SIXFL, "MR CHINEDU PROJECT 2.jpg")),
    "six_c":        img_uri(os.path.join(SIXFL, "MR CHINEDU PROJECT raw.jpg")),

    # ── SW 04: 4-Bedroom Family House, Uselu ──
    "uselu_hero":   img_uri(os.path.join(USELU, "Usele Hero 1.png")),
    "uselu_night":  img_uri(os.path.join(USELU, "USELU - NIGHT VIEW.png")),
    "uselu_col":    img_uri(os.path.join(USELU, "USELU - COLAGE.png")),

    # ── SW 05: Hillside Project ──
    "hill_hero":    img_uri(os.path.join(HILL, "HERO IMG.png")),
    "hill_massing": img_uri(os.path.join(HILL, "RAW 1.jpg")),
    "hill_detail":  img_uri(os.path.join(HILL, "02 Detail Study.png")),

    # ── Other Projects gallery (9 tiles) ──
    "g1":  img_uri(os.path.join(LAND, "CIVIL DEFECE HQ 1.jpg"),   max_px=860, quality=80),
    "g2":  img_uri(os.path.join(LAND, "CIVIL DEFECE HQ 2.jpg"),   max_px=860, quality=80),
    "g3":  img_uri(os.path.join(LAND, "NEW HOTEL 1.jpg"),          max_px=860, quality=80),
    "g4":  img_uri(os.path.join(LAND, "NEW HOTEL 2.jpg"),          max_px=860, quality=80),
    "g5":  img_uri(os.path.join(ADO,  "ADO CENTER RAW 2.jpg"),    max_px=860, quality=80),
    "g6":  img_uri(os.path.join(LAND, "SAPELE RD.jpg"),            max_px=860, quality=80),
    "g7":  img_uri(os.path.join(OTHER, "Building Model.png"),      max_px=860, quality=80),
    "g8":  img_uri(os.path.join(OTHER, "Event Hall Massing.png"),  max_px=860, quality=80),
    "g9":  img_uri(os.path.join(SCHEMA, "BIG SCHEMA RAW 1.jpg"),  max_px=860, quality=80),
}

FONT_FACES = "".join(
    f"""@font-face{{font-family:'Inter';font-style:normal;font-weight:{w};
    src:url('{font_uri(w)}') format('woff2');}}"""
    for w in (300, 400, 500, 600, 700, 800)
)

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
.headline{ font-size:50px; font-weight:800; line-height:1.06;
  letter-spacing:-0.03em; }
.headline span{ display:block; }
.headline .accent{ color:var(--accent); }
.headline .muted{ color:var(--text); }
.hero-sub{ font-size:13px; font-weight:300; color:var(--text);
  margin-top:18px; max-width:96mm; line-height:1.7; }
.hero-points{ list-style:none; margin-top:18px; }
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
  object-position:center 42%; display:block; }
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
.stat-grid .n{ font-size:25px; font-weight:700; color:var(--accent); line-height:1; }
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

/* ── SOFTWARE (dark) ── */
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

/* ── EXPERTISE CARDS ── */
.cards{ display:grid; grid-template-columns:1fr 1fr; gap:13px; }
.card{ background:var(--white); border:1px solid var(--border);
  border-radius:10px; overflow:hidden; }
.card .top{ height:4px; background:var(--accent); }
.card .bd{ padding:16px 17px; }
.card .ic{ width:36px; height:36px; background:var(--light); border-radius:7px;
  color:var(--accent); font-size:15px; display:flex; align-items:center;
  justify-content:center; margin-bottom:11px; }
.card h3{ font-size:14px; margin-bottom:6px; }
.card p{ font-size:10px; line-height:1.55; color:var(--text); margin-bottom:9px; }
.card .tag{ font-size:8.5px; font-weight:600; letter-spacing:0.04em;
  color:var(--accent); }

/* ── SELECTED WORK ── */
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

/* ── OTHER PROJECTS ── */
.other-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:11px; }
.tile{ border:1px solid var(--border); border-radius:8px; overflow:hidden;
  background:var(--white); }
.tile img{ width:100%; height:44mm; object-fit:cover; display:block; }
.tile .cap{ padding:7px 10px; }
.tile .cap .t{ font-size:9.5px; font-weight:600; color:var(--dark);
  display:block; line-height:1.3; }
.tile .cap .m{ font-size:7.5px; font-weight:600; letter-spacing:0.07em;
  text-transform:uppercase; color:var(--accent); }

/* ── CONTACT (dark) ── */
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
      <p class="label hero-label">Construction Project Manager · BIM Specialist · Lagos, Nigeria</p>
      <div class="headline">
        <span>Build.</span>
        <span class="accent">Coordinate.</span>
        <span>Deliver.</span>
        <span class="muted">On Time.</span>
      </div>
      <p class="hero-sub">From ground-breaking to handover — site engineering,
        BIM coordination and construction management across residential,
        commercial and infrastructure projects in Nigeria.</p>
      <ul class="hero-points">
        <li>7+ years of progressive construction &amp; site leadership</li>
        <li>30+ projects delivered across all disciplines</li>
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
          <div class="b"><div class="n">30+</div><div class="l">Total projects</div></div>
          <div class="b"><div class="n">&#8358;350M+</div><div class="l">Project value</div></div>
          <div class="b"><div class="n">7+</div><div class="l">Years</div></div>
        </div>
        <div class="psw">
          <span>Revit</span><span>Navisworks</span><span>AutoCAD</span>
          <span>MS Project</span><span>Dynamo</span>
        </div>
        <div class="avail"><div class="dot"></div>
          <span>Open to opportunities — worldwide &amp; remote</span></div>
      </div>
    </aside>
  </div>

  <div class="img-band">
    <img src="__cover_band__" alt="Residential estate — aerial site masterplan" />
    <div class="cap">Residential Estate — Aerial Site Masterplan</div>
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
    <h2>The Construction Professional</h2></div>

  <div class="about">
    <div>
      <p>Vollmann Olamide Akarakiri is a results-driven Construction Project
        Manager and BIM Specialist with 7+ years delivering residential,
        commercial and infrastructure projects from planning through completion
        across multiple Nigerian states.</p>
      <p>He has coordinated multiple project sites simultaneously and
        contributed to projects exceeding &#8358;350 million in cumulative value
        — generating over &#8358;10 million in cost savings through procurement
        oversight, error prevention and rigorous cost control.</p>
      <p>Experienced in end-to-end site engineering — excavation, foundations,
        structural works, drainage, roofing, finishes and handover — with
        advanced BIM capability in Revit, Dynamo, Navisworks and AutoCAD for
        coordinated model delivery and construction documentation.</p>
      <div class="stat-grid">
        <div class="st"><div class="n">30+</div><div class="d">Total projects across all disciplines</div></div>
        <div class="st"><div class="n">&#8358;350M+</div><div class="d">Cumulative project value</div></div>
        <div class="st"><div class="n">&#8358;10M+</div><div class="d">Savings delivered</div></div>
        <div class="st"><div class="n">7+</div><div class="d">Years of experience</div></div>
      </div>
    </div>

    <div>
      <p class="label" style="margin-bottom:9px;">Core Competencies</p>
      <div class="skill-group"><h4>Construction &amp; Site Management</h4>
        <div class="pills"><span>Site Engineering</span><span>Programme Management</span>
          <span>Subcontractor Coordination</span><span>Quality Control</span>
          <span>Health &amp; Safety (HSE)</span></div></div>
      <div class="skill-group"><h4>Project Management</h4>
        <div class="pills"><span>Planning &amp; Scheduling</span>
          <span>Budgeting &amp; Cost Forecasting</span>
          <span>Procurement &amp; Contracts</span>
          <span>Risk Management</span><span>Stakeholder Reporting</span></div></div>
      <div class="skill-group"><h4>BIM &amp; Digital Delivery</h4>
        <div class="pills"><span>BIM Modelling (Revit)</span>
          <span>Dynamo Automation</span><span>Navisworks Coordination</span>
          <span>Clash Detection</span><span>4D Sequencing</span></div></div>
      <div class="skill-group"><h4>Technical Specialisms</h4>
        <div class="pills"><span>Landscape Construction</span>
          <span>MEP Coordination</span><span>Regulatory Compliance</span>
          <span>Cost Estimation</span><span>Working Drawings</span></div></div>
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
    <p class="label" style="margin-top:9px;">Technical Expertise</p>
    <h2>BIM &amp; Construction Software</h2>
    <p class="sub">Industry-standard tools deployed across every phase of the
      construction programme — from digital model to physical delivery.</p></div>

  <div class="sw-grid">
    <div class="sw"><div class="ic">&#9670;</div><h4>Autodesk Revit</h4>
      <div class="lv">Expert — BIM Modelling &amp; Documentation</div>
      <p>Full architectural BIM models for 30+ office, residential and interior
        projects. Family creation, documentation sheets, schedules and
        coordinated model production for construction delivery.</p></div>
    <div class="sw"><div class="ic">&#9671;</div><h4>Navisworks</h4>
      <div class="lv">Proficient — BIM Coordination</div>
      <p>Multi-discipline model coordination, clash detection and resolution,
        4D construction sequencing and construction programme review
        workflows across multiple concurrent projects.</p></div>
    <div class="sw"><div class="ic">&#9633;</div><h4>AutoCAD</h4>
      <div class="lv">Expert — Technical Drawing</div>
      <p>2D technical drawing, site plans, detailed construction and working
        drawings, and full detailing packages for 10+ residential and
        commercial properties.</p></div>
    <div class="sw"><div class="ic">&#9650;</div><h4>Dynamo for Revit</h4>
      <div class="lv">Advanced — Parametric Automation</div>
      <p>Custom parametric workflows and automation scripts reducing
        documentation time and enabling data-driven design coordination
        across large, complex building programmes.</p></div>
    <div class="sw"><div class="ic">&#9632;</div><h4>Microsoft Project</h4>
      <div class="lv">Proficient — Project Scheduling</div>
      <p>Scheduling, milestone tracking, resource planning and programme
        management across large multi-site construction programmes and
        concurrent project portfolios.</p></div>
    <div class="sw"><div class="ic">&#9679;</div><h4>MS Excel &amp; Office Suite</h4>
      <div class="lv">Advanced — Cost Control &amp; Reporting</div>
      <p>Budget tracking, cost forecasting, progress reporting, procurement
        schedules and management reporting across concurrent construction
        sites and client accounts.</p></div>
  </div>

  <div class="disc">
    <span>Project Planning &amp; Scheduling</span><span>BIM Coordination</span>
    <span>Budgeting &amp; Cost Forecasting</span><span>Procurement &amp; Contracts</span>
    <span>Site Engineering</span><span>Health &amp; Safety (HSE)</span>
    <span>Risk Management</span><span>Clash Detection</span>
    <span>4D Sequencing</span><span>Regulatory Compliance</span>
    <span>Stakeholder Reporting</span><span>MEP Coordination</span>
  </div>
</section>

<!-- ════════ 4 · EXPERIENCE ════════ -->
<section class="sheet">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Career History</p>
    <h2>Professional Experience</h2>
    <p class="sub">7+ years of progressive responsibility across construction,
      site engineering and BIM delivery — from intern to Engineering Lead.</p></div>

  <ul class="tl">
    <li class="cur"><div class="pe">Aug 2021 – Feb 2026</div>
      <div class="ro">Project Manager / Engineering Lead</div>
      <div class="co">Nu-Avenue Company Resources</div>
      <ul><li>Directed construction delivery across multiple sites in
        multiple states, contributing to projects exceeding &#8358;350M in value.</li>
        <li>Generated over &#8358;10M in savings through cost control, vendor
          coordination and error prevention.</li>
        <li>Produced BIM models for 30+ office, 10+ residential and 10+
          interior projects using Revit and Dynamo.</li>
        <li>Coordinated architects, consultants, engineers, suppliers and
          contractors to ensure quality, safety and on-time delivery.</li></ul></li>
    <li><div class="pe">Jun 2020 – Aug 2021</div>
      <div class="ro">Site Engineer / Assistant Technical Designer</div>
      <div class="co">Nature's Beauty Construction</div>
      <ul><li>Planned and supervised site-development and landscape
        projects across multiple Nigerian states.</li>
        <li>Produced full detailing packages for 10+ residential properties.</li>
        <li>Trained 5+ employees; contributed to business opportunities
          exceeding &#8358;20 million.</li></ul></li>
    <li><div class="pe">Dec 2019 – Apr 2020</div>
      <div class="ro">Site Supervisor</div>
      <div class="co">Lego Construction Company</div>
      <ul><li>Developed project plans, contract documents, schedules and budgets.</li>
        <li>Facilitated interdisciplinary coordination meetings and client engagement.</li></ul></li>
    <li><div class="pe">Aug 2017 – Dec 2017</div>
      <div class="ro">Architecture &amp; Planning Intern</div>
      <div class="co">Danzinger Nigeria Ltd</div>
      <ul><li>Assisted management of consulting activities exceeding &#8358;10M.</li>
        <li>Assisted drafting, BIM updates and construction documentation.</li></ul></li>
  </ul>

  <div class="metrics">
    <div class="st"><div class="n">&#8358;350M+</div><div class="d">Total project value</div></div>
    <div class="st"><div class="n">&#8358;10M+</div><div class="d">Savings generated</div></div>
    <div class="st"><div class="n">30+</div><div class="d">Total projects across all disciplines</div></div>
    <div class="st"><div class="n">30+</div><div class="d">BIM models produced</div></div>
  </div>
  __FOOT4__
</section>

<!-- ════════ 5 · AREAS OF EXPERTISE ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Portfolio</p>
    <h2>Areas of Construction Expertise</h2>
    <p class="sub">Six specialist disciplines — integrated delivery from
      ground-breaking to handover and beyond.</p></div>

  <div class="cards">
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9670;</div><h3>Construction Project Management</h3>
      <p>End-to-end construction programme management across 3+ concurrent
        sites — planning, procurement, budgeting, contractor coordination,
        quality control and HSE oversight.</p>
      <div class="tag">MULTI-SITE DELIVERY</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9671;</div><h3>BIM &amp; Digital Construction</h3>
      <p>Advanced BIM modelling in Revit, Dynamo automation, Navisworks
        coordination and clash detection — digital workflows across residential,
        office and commercial projects.</p>
      <div class="tag">REVIT · DYNAMO · NAVISWORKS</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9633;</div><h3>Site Engineering</h3>
      <p>Hands-on site supervision — excavation, foundations, drainage,
        concrete, blockwork, reinforcement, roofing, finishes and MEP
        coordination through to practical completion.</p>
      <div class="tag">STRUCTURES · DRAINAGE · FINISHES</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9650;</div><h3>Landscape &amp; Site Development</h3>
      <p>Site-development and landscape projects — master planning,
        hardscape, softscape, drainage integration, site beautification
        and civil works.</p>
      <div class="tag">SITE &amp; LANDSCAPE WORK</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9632;</div><h3>Residential Building Projects</h3>
      <p>Residential design and delivery from schematic concept through
        construction drawings and site supervision to handover — apartments,
        family homes and mixed-use developments.</p>
      <div class="tag">RESIDENTIAL · MIXED-USE · APARTMENTS</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9679;</div><h3>Cost Control &amp; Procurement</h3>
      <p>Budgeting, cost forecasting, procurement strategy and contract
        administration — delivering &#8358;10M+ in verified savings through
        rigorous cost management disciplines.</p>
      <div class="tag">&#8358;10M+ SAVINGS DELIVERED</div></div></div>
  </div>

  <div class="img-band">
    <img src="__reno_band__" alt="Residential renovation proposal — Akure" />
    <div class="cap">Residential Renovation — Family Home, Akure</div>
  </div>
  __FOOT5__
</section>

<!-- ════════ 6 · SELECTED WORK 01 — HALL OF WORSHIP, ADO ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 01</p>
    <h2>Hall of Worship, Ado</h2>
    <p class="sub">Architectural visualisation, coordinated structural BIM model
      and full construction documentation package — Ado, Ekiti State.</p></div>

  <div class="fig big"><img src="__ado_hero__" alt="Hall of Worship architectural visualisation" />
    <div class="cap"><span class="t">Hall of Worship — Architectural Visualisation</span>
      <span class="m">Render</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__ado_raw__" alt="Structural BIM model — construction phase" />
      <div class="cap"><span class="t">Structural BIM Model — Construction Phase</span>
        <span class="m">Revit</span></div></div>
    <div class="fig half"><img src="__ado_plan__" alt="Proposed floor plan documentation" />
      <div class="cap"><span class="t">Proposed Floor Plan Documentation</span>
        <span class="m">Documentation</span></div></div>
  </div>
  __FOOT6__
</section>

<!-- ════════ 7 · SELECTED WORK 02 — LANDSCAPE & SITE DEVELOPMENT ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 02</p>
    <h2>Landscape &amp; Site Development</h2>
    <p class="sub">Site-development and landscape projects — master
      planning, hardscape and softscape integration, site infrastructure
      and visualisation across multiple states.</p></div>

  <div class="fig big"><img src="__land_hero__" alt="Site master plan — aerial overview" />
    <div class="cap"><span class="t">Site Master Plan — Aerial Overview</span>
      <span class="m">Aerial</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__land_b__" alt="Parking court and landscape planting" />
      <div class="cap"><span class="t">Parking Court &amp; Landscape Planting</span>
        <span class="m">Render</span></div></div>
    <div class="fig half"><img src="__land_c__" alt="Residence and carport render" />
      <div class="cap"><span class="t">Residence &amp; Carport</span>
        <span class="m">Render</span></div></div>
  </div>
  __FOOT7__
</section>

<!-- ════════ 8 · SELECTED WORK 03 — 6-FLAT APARTMENT BLOCK, IKOTUN ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 03</p>
    <h2>6-Flat Apartment Block, Ikotun</h2>
    <p class="sub">Three-storey six-flat residential development — Ikotun, Lagos.
      Full BIM design, massing study, façade development and construction
      documentation.</p></div>

  <div class="fig big"><img src="__six_hero__" alt="Six-flat apartment block render" />
    <div class="cap"><span class="t">Six-Flat Apartment Block — Street View</span>
      <span class="m">Render</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__six_b__" alt="Facade and material study" />
      <div class="cap"><span class="t">Façade &amp; Material Study</span>
        <span class="m">Detail</span></div></div>
    <div class="fig half"><img src="__six_c__" alt="Massing and structure model" />
      <div class="cap"><span class="t">Massing &amp; Structural Model</span>
        <span class="m">Revit</span></div></div>
  </div>
  __FOOT8__
</section>

<!-- ════════ 9 · SELECTED WORK 04 — 4-BEDROOM FAMILY HOUSE, USELU ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 04</p>
    <h2>4-Bedroom Family House, Uselu</h2>
    <p class="sub">A four-bedroom detached family residence — Uselu, Benin City.
      Architectural design, material study and photorealistic visualisation.</p></div>

  <div class="fig big"><img src="__uselu_hero__" alt="4-bedroom family house street view" />
    <div class="cap"><span class="t">4-Bedroom Family House — Street View</span>
      <span class="m">Render</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__uselu_night__" alt="Night elevation render" />
      <div class="cap"><span class="t">Night Elevation</span>
        <span class="m">Render</span></div></div>
    <div class="fig half"><img src="__uselu_col__" alt="Material and detail study" />
      <div class="cap"><span class="t">Material &amp; Detail Study</span>
        <span class="m">Details</span></div></div>
  </div>
  __FOOT9__
</section>

<!-- ════════ 10 · SELECTED WORK 05 — THE HILLSIDE PROJECT ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 05</p>
    <h2>The Hillside Project</h2>
    <p class="sub">Concept design for residential apartments set into a
      challenging hillside terrain — massing study, structural concept
      and façade development.</p></div>

  <div class="fig big"><img src="__hill_hero__" alt="Hillside residential concept render" />
    <div class="cap"><span class="t">Hillside Residence — Street Approach Render</span>
      <span class="m">Render</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__hill_massing__" alt="Massing model on sloped terrain" />
      <div class="cap"><span class="t">Massing on Sloped Terrain</span>
        <span class="m">Concept</span></div></div>
    <div class="fig half"><img src="__hill_detail__" alt="Facade and material study" />
      <div class="cap"><span class="t">Façade &amp; Material Study</span>
        <span class="m">Detail</span></div></div>
  </div>
  __FOOT10__
</section>

<!-- ════════ 11 · OTHER PROJECTS ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">More Work</p>
    <h2>Other Construction Projects</h2>
    <p class="sub">A further selection of construction, infrastructure,
      civil works and building projects from across the portfolio.</p></div>

  <div class="other-grid">
    <div class="tile"><img src="__g1__" alt="Civil Defence HQ project" />
      <div class="cap"><span class="t">Civil Defence HQ</span><span class="m">Infrastructure</span></div></div>
    <div class="tile"><img src="__g2__" alt="Civil Defence HQ view 2" />
      <div class="cap"><span class="t">Civil Defence HQ — View 2</span><span class="m">Infrastructure</span></div></div>
    <div class="tile"><img src="__g3__" alt="New hotel project" />
      <div class="cap"><span class="t">Hotel Development</span><span class="m">Commercial</span></div></div>
    <div class="tile"><img src="__g4__" alt="Hotel development view 2" />
      <div class="cap"><span class="t">Hotel Development — View 2</span><span class="m">Commercial</span></div></div>
    <div class="tile"><img src="__g5__" alt="Ado Centre construction progress" />
      <div class="cap"><span class="t">Ado Centre — Construction</span><span class="m">Site</span></div></div>
    <div class="tile"><img src="__g6__" alt="Sapele Road site project" />
      <div class="cap"><span class="t">Sapele Road Site Works</span><span class="m">Infrastructure</span></div></div>
    <div class="tile"><img src="__g7__" alt="Building massing model" />
      <div class="cap"><span class="t">Building Massing Model</span><span class="m">Concept</span></div></div>
    <div class="tile"><img src="__g8__" alt="Event hall massing study" />
      <div class="cap"><span class="t">Event Hall Massing</span><span class="m">Concept</span></div></div>
    <div class="tile"><img src="__g9__" alt="Large residential schema" />
      <div class="cap"><span class="t">Large Residential Schema</span><span class="m">Concept</span></div></div>
  </div>
  __FOOT11__
</section>

<!-- ════════ CONTACT ════════ -->
<section class="sheet dark">
  <div class="contact">
    <p class="label">Get In Touch</p>
    <h2>Ready to Build Something Great?</h2>
    <p class="lead">Whether you're a developer, contractor, architecture firm
      or project owner — let's discuss how I can drive your next construction
      programme to successful delivery.</p>
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
  <div class="cfoot">Vollmann Olamide Akarakiri · Build. Coordinate. Deliver. On Time.</div>
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
