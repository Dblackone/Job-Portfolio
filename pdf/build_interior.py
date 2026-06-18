#!/usr/bin/env python3
"""
Interior Design Portfolio — Vollmann Olamide Akarakiri
Generates a print-ready A4 PDF showcasing interior design work.

Run:  python3 pdf/build_interior.py
Out:  assets/vollmann-akarakiri-interior-portfolio.pdf
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
OUT = os.path.join(ASSETS, "vollmann-akarakiri-interior-portfolio.pdf")

TOTAL_PAGES = 9


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


INTOP = os.path.join(PICS, "Interior Residential Operations")
IKEJA = os.path.join(PICS, "Design For Ikeja confencens room")
SCHEMA = os.path.join(PICS, "Concept schema projects")
LAND = os.path.join(PICS, "Landscape Projects")
OTHER = os.path.join(PICS, "Other Renders")
RENO = os.path.join(PICS, "Renovation Akure")

IMG = {
    "profile":      img_uri(os.path.join(ASSETS, "vollmann-akarakiri-profile.png"),
                            max_px=760, keep_alpha=True),
    # Cover band — living space render as a wide panoramic hero
    "cover_band":   img_uri(os.path.join(INTOP, "Living Space.png"),
                            max_px=1600, quality=84),

    # ── SW 01: Ikeja Conference Room ──
    "ikeja_hero":   img_uri(os.path.join(IKEJA, "Image2_050.png")),
    "ikeja_b":      img_uri(os.path.join(IKEJA, "Image4_034.png")),
    "ikeja_c":      img_uri(os.path.join(IKEJA, "Image6_014.png")),

    # ── SW 02: Residential Living Spaces ──
    "res_hero":     img_uri(os.path.join(INTOP, "RENDER 1.png")),
    "res_b":        img_uri(os.path.join(INTOP, "RENDER 2.png")),
    "res_c":        img_uri(os.path.join(INTOP, "Image2_048.png")),

    # ── SW 03: Executive Boardroom & Corporate Spaces ──
    "board_hero":   img_uri(os.path.join(INTOP, "Executive Boardroom.jpeg")),
    "board_b":      img_uri(os.path.join(INTOP, "Bathroom Suite.png")),
    "board_c":      img_uri(os.path.join(INTOP, "Image3_033.png")),

    # ── Expertise band: Renovation render ──
    "exp_band":     img_uri(os.path.join(RENO, "Akure Family Home.png"),
                            max_px=1600, quality=84),

    # ── Other Projects gallery (9 tiles) ──
    "g1":  img_uri(os.path.join(IKEJA, "Image1_062.png"),         max_px=860, quality=80),
    "g2":  img_uri(os.path.join(IKEJA, "Image1_061.png"),         max_px=860, quality=80),
    "g3":  img_uri(os.path.join(IKEJA, "Image2_051.png"),         max_px=860, quality=80),
    "g4":  img_uri(os.path.join(SCHEMA, "SCHEMA 01 - CLIAMTE COLAGE.png"),
                                                                    max_px=860, quality=80),
    "g5":  img_uri(os.path.join(SCHEMA, "LOFT RAW 1.jpg"),        max_px=860, quality=80),
    "g6":  img_uri(os.path.join(SCHEMA, "BIG SCHEMA RAW 1.jpg"),  max_px=860, quality=80),
    "g7":  img_uri(os.path.join(OTHER, "Event Hall.png"),         max_px=860, quality=80),
    "g8":  img_uri(os.path.join(OTHER, "Entrance Gatehouse.png"), max_px=860, quality=80),
    "g9":  img_uri(os.path.join(SCHEMA, "3 BEDROOM TRERACE WITH PENT HOUSE - RAW 1.jpg"),
                                                                    max_px=860, quality=80),
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
  margin-bottom:18mm; }
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
    f'Interior Design Specialist</span><span>{{n}} / {TOTAL_PAGES}</span></div>'
)

BODY = """
<!-- ════════ 1 · COVER ════════ -->
<section class="sheet cover">
  <div class="cover-shape"></div>
  <div class="cover-top">
    <div class="brand"><div class="mark">V</div>
      <div class="nm">Vollmann&nbsp;Akarakiri</div></div>
    <div class="cover-tag">Interior Design Portfolio · 2026</div>
  </div>

  <div class="hero">
    <div>
      <p class="label hero-label">Interior Design Specialist · Lagos, Nigeria</p>
      <div class="headline">
        <span>Space.</span>
        <span class="accent">Light.</span>
        <span>Materiality.</span>
        <span class="muted">Delivered.</span>
      </div>
      <p class="hero-sub">Transforming interiors into purposeful, beautiful
        environments — from residential living spaces to corporate conference
        rooms and executive boardrooms across Nigeria.</p>
      <ul class="hero-points">
        <li>10+ completed interior design &amp; fit-out projects</li>
        <li>Residential, corporate &amp; commercial typologies</li>
        <li>3D visualisation · Space planning · Material specification</li>
        <li>MSc Construction Engineering Management — UEL, London</li>
      </ul>
    </div>

    <aside class="pcard">
      <img class="photo" src="__profile__" alt="Vollmann Olamide Akarakiri" />
      <div class="info">
        <div class="accent-bar"></div>
        <h3>Vollmann Olamide Akarakiri</h3>
        <div class="role">Interior Design Specialist</div>
        <div class="loc">Lagos, Nigeria · MSc CEM Candidate, UEL</div>
        <div class="pstats">
          <div class="b"><div class="n">10+</div><div class="l">Interior projects</div></div>
          <div class="b"><div class="n">5+</div><div class="l">Years practice</div></div>
          <div class="b"><div class="n">3D</div><div class="l">Visualisation</div></div>
        </div>
        <div class="psw">
          <span>Revit</span><span>Lumion</span><span>AutoCAD</span>
          <span>SketchUp</span><span>Qmotion</span>
        </div>
        <div class="avail"><div class="dot"></div>
          <span>Open to opportunities — worldwide &amp; remote</span></div>
      </div>
    </aside>
  </div>

  <div class="img-band">
    <img src="__cover_band__" alt="Interior living space — residential visualisation" />
    <div class="cap">Residential Living Space — Interior Visualisation</div>
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
    <h2>The Designer Behind the Work</h2></div>

  <div class="about">
    <div>
      <p>Vollmann Olamide Akarakiri is a multidisciplinary design professional
        specialising in interior design, space planning, and 3D visualisation.
        With 5+ years in the built environment, he brings architectural rigour
        and creative vision to every interior — from intimate residential spaces
        to large corporate fit-outs.</p>
      <p>He has delivered interior design solutions for residential living rooms,
        dining areas, bathroom suites, executive boardrooms, and corporate
        conference spaces — coordinating materials, finishes, furniture layouts,
        and lighting to create harmonious environments that serve both
        aesthetics and function.</p>
      <p>Backed by a strong BIM and construction background, Vollmann's designs
        are buildable, coordinated, and delivered on time — bridging the gap
        between concept render and physical reality.</p>
      <div class="stat-grid">
        <div class="st"><div class="n">10+</div><div class="d">Interior projects delivered</div></div>
        <div class="st"><div class="n">30+</div><div class="d">BIM models produced</div></div>
        <div class="st"><div class="n">5+</div><div class="d">Years of design experience</div></div>
        <div class="st"><div class="n">2</div><div class="d">Typologies — residential &amp; corporate</div></div>
      </div>
    </div>

    <div>
      <p class="label" style="margin-bottom:9px;">Design Competencies</p>
      <div class="skill-group"><h4>Space Planning &amp; Layout Design</h4>
        <div class="pills"><span>Space Planning</span><span>Furniture Layout</span>
          <span>Circulation &amp; Flow</span><span>Zoning</span>
          <span>Client Briefing</span></div></div>
      <div class="skill-group"><h4>Materials &amp; Finishes</h4>
        <div class="pills"><span>Material Specification</span>
          <span>Colour Palettes</span><span>Surface Finishes</span>
          <span>Fixture Selection</span><span>Lighting Design</span></div></div>
      <div class="skill-group"><h4>Visualisation &amp; Presentation</h4>
        <div class="pills"><span>3D Rendering (Lumion)</span>
          <span>Photorealistic Renders</span><span>Design Presentations</span>
          <span>Revit BIM Interiors</span><span>AutoCAD Drawings</span></div></div>
      <div class="skill-group"><h4>Fit-Out Coordination</h4>
        <div class="pills"><span>Contractor Management</span>
          <span>MEP Coordination</span><span>Kitchen &amp; Joinery</span>
          <span>Quality Control</span></div></div>
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

<!-- ════════ 3 · DESIGN TOOLS (dark) ════════ -->
<section class="sheet dark">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Technical Toolkit</p>
    <h2>Design Software &amp; Tools</h2>
    <p class="sub">Industry-leading tools applied across every stage of the
      interior design process — from concept sketch to photorealistic render.</p></div>

  <div class="sw-grid">
    <div class="sw"><div class="ic">&#9670;</div><h4>Autodesk Revit</h4>
      <div class="lv">Expert — BIM Interior Modelling</div>
      <p>Fully coordinated interior BIM models with furniture families, material
        assignments, room schedules and documentation sheets for handover.</p></div>
    <div class="sw"><div class="ic">&#9671;</div><h4>Lumion &amp; Qmotion</h4>
      <div class="lv">Advanced — Photorealistic Rendering</div>
      <p>High-fidelity interior renders and walkthroughs communicating lighting,
        material quality and spatial atmosphere to clients and stakeholders.</p></div>
    <div class="sw"><div class="ic">&#9633;</div><h4>AutoCAD</h4>
      <div class="lv">Expert — Technical Drawings</div>
      <p>Detailed floor plans, reflected ceiling plans, elevation drawings and
        joinery details — construction-ready documentation packages.</p></div>
    <div class="sw"><div class="ic">&#9650;</div><h4>SketchUp</h4>
      <div class="lv">Proficient — Concept Modelling</div>
      <p>Rapid 3D massing and concept modelling for early-stage client
        presentations and design development workshops.</p></div>
    <div class="sw"><div class="ic">&#9632;</div><h4>Microsoft Office Suite</h4>
      <div class="lv">Advanced — Project Reporting</div>
      <p>Design briefs, material schedules, procurement lists, cost estimates
        and progress reports for clients and project teams.</p></div>
    <div class="sw"><div class="ic">&#9679;</div><h4>Navisworks</h4>
      <div class="lv">Proficient — Coordination</div>
      <p>Multi-discipline model coordination and clash detection to ensure
        interior fit-out works align with structural and MEP systems.</p></div>
  </div>

  <div class="disc">
    <span>Space Planning</span><span>3D Visualisation</span>
    <span>Material Specification</span><span>Lighting Design</span>
    <span>Furniture Layout</span><span>Kitchen &amp; Joinery Design</span>
    <span>Fit-Out Coordination</span><span>MEP Coordination</span>
    <span>Client Presentations</span><span>Design Documentation</span>
    <span>Residential Interiors</span><span>Corporate Fit-Outs</span>
  </div>
</section>

<!-- ════════ 4 · AREAS OF EXPERTISE ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Services</p>
    <h2>Interior Design Expertise</h2>
    <p class="sub">End-to-end interior design services — from client brief and
      concept to detailed drawings and fit-out oversight.</p></div>

  <div class="cards">
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9670;</div><h3>Residential Interiors</h3>
      <p>Living rooms, dining areas, bedrooms, kitchens and bathrooms — complete
        home interior packages tailored to each client's lifestyle, preferences
        and budget.</p>
      <div class="tag">LIVING · DINING · BEDROOMS</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9671;</div><h3>Corporate &amp; Office Spaces</h3>
      <p>Executive boardrooms, conference rooms, open-plan offices and reception
        areas — environments designed for productivity, brand identity and
        professional impact.</p>
      <div class="tag">BOARDROOMS · CONFERENCE · OFFICES</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9633;</div><h3>3D Visualisation</h3>
      <p>Photorealistic renders and walkthroughs that communicate design intent
        with clarity — helping clients visualise and approve designs before
        construction begins.</p>
      <div class="tag">RENDERS · WALKTHROUGHS · PRESENTATIONS</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9650;</div><h3>Material &amp; Finish Specification</h3>
      <p>Comprehensive material schedules covering flooring, wall finishes,
        ceiling treatments, fixtures, fittings and bespoke joinery — fully
        coordinated for procurement.</p>
      <div class="tag">MATERIALS · FINISHES · SCHEDULES</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9632;</div><h3>Kitchen &amp; Joinery Design</h3>
      <p>Bespoke kitchen layouts, cabinetry design, island configuration and
        storage solutions — designed and documented for manufacture and
        installation.</p>
      <div class="tag">KITCHENS · CABINETRY · BESPOKE</div></div></div>
    <div class="card"><div class="top"></div><div class="bd">
      <div class="ic">&#9679;</div><h3>Fit-Out Project Management</h3>
      <p>End-to-end fit-out coordination — contractor management, quality
        control, procurement oversight and programme management from design
        through handover.</p>
      <div class="tag">FIT-OUT · DELIVERY · HANDOVER</div></div></div>
  </div>

  <div class="img-band">
    <img src="__exp_band__" alt="Residential renovation proposal — Akure family home" />
    <div class="cap">Residential Renovation — Family Home, Akure</div>
  </div>
  __FOOT4__
</section>

<!-- ════════ 5 · SELECTED WORK 01 — IKEJA CONFERENCE ROOM ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 01</p>
    <h2>Ikeja Conference Room Design</h2>
    <p class="sub">A contemporary conference and meeting space — Ikeja, Lagos.
      Space planning, material specification and full 3D visualisation package.</p></div>

  <div class="fig big"><img src="__ikeja_hero__" alt="Ikeja conference room interior render" />
    <div class="cap"><span class="t">Conference Room — Interior Render</span>
      <span class="m">Render</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__ikeja_b__" alt="Ikeja meeting room layout view" />
      <div class="cap"><span class="t">Meeting Room — Layout View</span>
        <span class="m">Interior</span></div></div>
    <div class="fig half"><img src="__ikeja_c__" alt="Ikeja conference room material study" />
      <div class="cap"><span class="t">Material &amp; Finish Study</span>
        <span class="m">Detail</span></div></div>
  </div>
  __FOOT5__
</section>

<!-- ════════ 6 · SELECTED WORK 02 — RESIDENTIAL LIVING SPACES ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 02</p>
    <h2>Residential Living Spaces</h2>
    <p class="sub">Family living and dining interiors — furniture layout,
      material palettes and photorealistic renders for residential clients
      across Lagos.</p></div>

  <div class="fig big"><img src="__res_hero__" alt="Residential interior render — living room" />
    <div class="cap"><span class="t">Residential Living Room — Interior Render</span>
      <span class="m">Render</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__res_b__" alt="Family lounge render" />
      <div class="cap"><span class="t">Family Lounge &amp; Dining Area</span>
        <span class="m">Render</span></div></div>
    <div class="fig half"><img src="__res_c__" alt="Living space interior study" />
      <div class="cap"><span class="t">Space Planning &amp; Layout Study</span>
        <span class="m">Interior</span></div></div>
  </div>
  __FOOT6__
</section>

<!-- ════════ 7 · SELECTED WORK 03 — EXECUTIVE BOARDROOM & CORPORATE ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 03</p>
    <h2>Executive Boardroom &amp; Corporate Spaces</h2>
    <p class="sub">High-end executive and corporate interior environments —
      designed for authority, comfort and professional presence.</p></div>

  <div class="fig big"><img src="__board_hero__" alt="Executive boardroom interior render" />
    <div class="cap"><span class="t">Executive Boardroom — Interior Render</span>
      <span class="m">Render</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__board_b__" alt="Luxury bathroom suite render" />
      <div class="cap"><span class="t">Luxury Bathroom Suite</span>
        <span class="m">Render</span></div></div>
    <div class="fig half"><img src="__board_c__" alt="Corporate interior study" />
      <div class="cap"><span class="t">Corporate Interior Study</span>
        <span class="m">Interior</span></div></div>
  </div>
  __FOOT7__
</section>

<!-- ════════ 8 · OTHER PROJECTS ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">More Work</p>
    <h2>Other Interior &amp; Design Projects</h2>
    <p class="sub">A selection of additional concept designs, space studies and
      visualisations from across the portfolio.</p></div>

  <div class="other-grid">
    <div class="tile"><img src="__g1__" alt="Conference room concept view" />
      <div class="cap"><span class="t">Conference Concept A</span><span class="m">Interior</span></div></div>
    <div class="tile"><img src="__g2__" alt="Conference room concept B" />
      <div class="cap"><span class="t">Conference Concept B</span><span class="m">Interior</span></div></div>
    <div class="tile"><img src="__g3__" alt="Conference room concept C" />
      <div class="cap"><span class="t">Meeting Room Concept</span><span class="m">Interior</span></div></div>
    <div class="tile"><img src="__g4__" alt="Climate collage design concept" />
      <div class="cap"><span class="t">Climate Collage Concept</span><span class="m">Concept</span></div></div>
    <div class="tile"><img src="__g5__" alt="Loft apartment schematic" />
      <div class="cap"><span class="t">Loft Apartment Scheme</span><span class="m">Concept</span></div></div>
    <div class="tile"><img src="__g6__" alt="Large schema project" />
      <div class="cap"><span class="t">Open Plan Schema</span><span class="m">Concept</span></div></div>
    <div class="tile"><img src="__g7__" alt="Event hall interior" />
      <div class="cap"><span class="t">Event Hall Interior</span><span class="m">Render</span></div></div>
    <div class="tile"><img src="__g8__" alt="Entrance and reception gatehouse" />
      <div class="cap"><span class="t">Entrance &amp; Reception</span><span class="m">Render</span></div></div>
    <div class="tile"><img src="__g9__" alt="3-bedroom terrace with penthouse" />
      <div class="cap"><span class="t">3-Bed Terrace Penthouse</span><span class="m">Concept</span></div></div>
  </div>
  __FOOT8__
</section>

<!-- ════════ 9 · CONTACT ════════ -->
<section class="sheet dark">
  <div class="contact">
    <p class="label">Get In Touch</p>
    <h2>Let's Create Something Beautiful.</h2>
    <p class="lead">Whether you're a homeowner, developer, architect or hospitality
      brand — I'd love to discuss how thoughtful interior design can transform
      your space into something truly exceptional.</p>
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
  <div class="cfoot">Vollmann Olamide Akarakiri · Interior Design Specialist · Lagos, Nigeria</div>
</section>
"""


def build():
    body = BODY
    for key, uri in IMG.items():
        body = body.replace(f"__{key}__", uri)
    for n in (2, 4, 5, 6, 7, 8):
        body = body.replace(f"__FOOT{n}__", FOOTER.format(n=f"{n:02d}"))

    html = (
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
        f"<style>{FONT_FACES}{CSS}</style></head><body>{body}</body></html>"
    )
    HTML(string=html, base_url=ROOT).write_pdf(OUT)
    print("Wrote", OUT, "·", round(os.path.getsize(OUT) / 1024), "KB")


if __name__ == "__main__":
    build()
