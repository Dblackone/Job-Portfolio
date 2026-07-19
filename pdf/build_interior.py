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

from PIL import Image, ImageOps
from weasyprint import HTML

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
PICS = os.path.join(ASSETS, "Project Pictures")
FONT_DIR = os.path.join(ROOT, "pdf", "fonts")
OUT = os.path.join(ASSETS, "vollmann-akarakiri-interior-portfolio.pdf")

TOTAL_PAGES = 12


def font_uri(weight):
    with open(os.path.join(FONT_DIR, f"inter-{weight}.woff2"), "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode()
    return f"data:font/woff2;base64,{b64}"


def img_uri(path, max_px=1280, quality=82, keep_alpha=False):
    im = Image.open(path)
    im = ImageOps.exif_transpose(im)          # keep phone photos upright
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
BODY_SHOP = os.path.join(PICS, "Body Shop Outlets")
ALCOVE = os.path.join(PICS, "Alcove Home Interior")
ADO = os.path.join(PICS, "Ado 6-Bedroom Duplex")
FINA = os.path.join(PICS, "Fina Trust Bank")
SAPELE = os.path.join(PICS, "Sapele Road Project")

IMG = {
    "profile":      img_uri(os.path.join(ASSETS, "vollmann-akarakiri-profile.png"),
                            max_px=760, keep_alpha=True),
    # Cover band — living space render as a wide panoramic hero
    "cover_band":   img_uri(os.path.join(INTOP, "Living Space.png"),
                            max_px=1600, quality=84),

    # ── SW 01: Ikeja Conference Room (render) ──
    "ikeja_hero":   img_uri(os.path.join(IKEJA, "Image2_050.png")),
    "ikeja_b":      img_uri(os.path.join(IKEJA, "Image4_034.png")),
    "ikeja_c":      img_uri(os.path.join(IKEJA, "Image6_014.png")),

    # ── SW 02: Residential Living Spaces (render) ──
    "res_hero":     img_uri(os.path.join(INTOP, "RENDER 1.png")),
    "res_b":        img_uri(os.path.join(INTOP, "RENDER 2.png")),
    "res_c":        img_uri(os.path.join(INTOP, "Image2_048.png")),

    # ── SW 03: The Body Shop — retail interior fit-out ──
    "bs_hero":      img_uri(os.path.join(BODY_SHOP, "body-shop-mural-display.jpeg")),
    "bs_b":         img_uri(os.path.join(BODY_SHOP, "body-shop-retail-floor.jpeg")),
    "bs_c":         img_uri(os.path.join(BODY_SHOP, "body-shop-counter-display.jpeg")),

    # ── SW 04: Alcove Homes — residential interior ──
    "alc_hero":     img_uri(os.path.join(ALCOVE, "Alcove Home Feature Wall.png")),
    "alc_b":        img_uri(os.path.join(ALCOVE, "alcove-homes-06.jpg")),
    "alc_c":        img_uri(os.path.join(ALCOVE, "alcove-homes-09.jpg")),

    # ── SW 05: Six-Bedroom Duplex Interior, Ado ──
    "ado_hero":     img_uri(os.path.join(ADO, "ado-duplex-interior-05.jpg")),
    "ado_b":        img_uri(os.path.join(ADO, "ado-duplex-interior-01.jpg")),
    "ado_c":        img_uri(os.path.join(ADO, "ado-duplex-interior-07.jpg")),

    # ── SW 06: Fina Trust Bank — sales outlet interior ──
    "fina_hero":    img_uri(os.path.join(FINA, "fina-outlet-01.jpg")),
    "fina_b":       img_uri(os.path.join(FINA, "fina-outlet-02.jpg")),
    "fina_c":       img_uri(os.path.join(FINA, "fina-outlet-03.jpg")),

    # ── SW 07: Sapele Road — bespoke joinery & kitchen ──
    "sap_hero":     img_uri(os.path.join(SAPELE, "sapele-road-01.jpg")),
    "sap_b":        img_uri(os.path.join(SAPELE, "sapele-road-05.jpg")),
    "sap_c":        img_uri(os.path.join(SAPELE, "sapele-road-03.jpg")),

    # ── Expertise band: built interior ──
    "exp_band":     img_uri(os.path.join(ADO, "ado-duplex-interior-06.jpg"),
                            max_px=1600, quality=84),

    # ── More Work gallery (6 tiles — real interior only) ──
    "gm1":  img_uri(os.path.join(ADO, "ado-duplex-interior-10.jpg"),   max_px=860, quality=80),
    "gm2":  img_uri(os.path.join(ADO, "ado-duplex-interior-08.jpg"),   max_px=860, quality=80),
    "gm3":  img_uri(os.path.join(ALCOVE, "alcove-homes-05.jpg"),       max_px=860, quality=80),
    "gm4":  img_uri(os.path.join(ALCOVE, "alcove-homes-07.jpg"),       max_px=860, quality=80),
    "gm5":  img_uri(os.path.join(SAPELE, "sapele-road-04.jpg"),        max_px=860, quality=80),
    "gm6":  img_uri(os.path.join(ADO, "ado-duplex-interior-09.jpg"),   max_px=860, quality=80),
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

/* ── compact technical toolkit (merged onto profile page) ── */
.tk-grid{ display:grid; grid-template-columns:1fr 1fr; gap:7px; }
.tk{ background:var(--bg); border-radius:6px; padding:8px 11px;
  border-left:2px solid var(--accent); }
.tk .tkn{ display:block; font-size:10.5px; font-weight:600; color:var(--dark); }
.tk .tkl{ display:block; font-size:8.5px; color:var(--accent); margin-top:1px; }

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
          <div class="b"><div class="n">7+</div><div class="l">Years practice</div></div>
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

<!-- ════════ 2 · PROFILE + TECHNICAL TOOLKIT (merged) ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Professional Profile</p>
    <h2>The Designer Behind the Work</h2></div>

  <div class="about">
    <div>
      <p>Vollmann Olamide Akarakiri is a multidisciplinary design professional
        specialising in interior design, space planning and 3D visualisation.
        With 7+ years in the built environment, he brings architectural rigour
        and creative vision to every interior — from intimate residential spaces
        to large corporate fit-outs.</p>
      <p>Backed by a strong BIM and construction background, his designs are
        buildable, coordinated and delivered on time — bridging the gap between
        concept render and physical reality across residential living spaces,
        boardrooms and corporate conference suites.</p>
      <div class="stat-grid">
        <div class="st"><div class="n">10+</div><div class="d">Interior projects delivered</div></div>
        <div class="st"><div class="n">30+</div><div class="d">BIM models produced</div></div>
        <div class="st"><div class="n">7+</div><div class="d">Years of design experience</div></div>
        <div class="st"><div class="n">2</div><div class="d">Typologies — residential &amp; corporate</div></div>
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
      <p class="label" style="margin-bottom:9px;">Design Competencies</p>
      <div class="skill-group"><h4>Space Planning &amp; Layout</h4>
        <div class="pills"><span>Space Planning</span><span>Furniture Layout</span>
          <span>Circulation &amp; Flow</span><span>Zoning</span></div></div>
      <div class="skill-group"><h4>Materials &amp; Finishes</h4>
        <div class="pills"><span>Material Specification</span>
          <span>Colour Palettes</span><span>Lighting Design</span>
          <span>Fixture Selection</span></div></div>
      <div class="skill-group"><h4>Visualisation &amp; Fit-Out</h4>
        <div class="pills"><span>3D Rendering (Lumion)</span>
          <span>Revit BIM Interiors</span><span>Kitchen &amp; Joinery</span>
          <span>MEP Coordination</span></div></div>

      <p class="label" style="margin:7mm 0 8px;">Technical Toolkit</p>
      <div class="tk-grid">
        <div class="tk"><span class="tkn">Autodesk Revit</span><span class="tkl">Expert · BIM interiors</span></div>
        <div class="tk"><span class="tkn">Lumion &amp; Qmotion</span><span class="tkl">Advanced · Rendering</span></div>
        <div class="tk"><span class="tkn">AutoCAD</span><span class="tkl">Expert · Technical drawings</span></div>
        <div class="tk"><span class="tkn">SketchUp</span><span class="tkl">Proficient · Concept modelling</span></div>
        <div class="tk"><span class="tkn">Navisworks</span><span class="tkl">Proficient · Coordination</span></div>
        <div class="tk"><span class="tkn">MS Office Suite</span><span class="tkl">Advanced · Reporting</span></div>
      </div>
    </div>
  </div>
  __FOOT2__
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
    <img src="__exp_band__" alt="Built interior — six-bedroom duplex, Ado" />
    <div class="cap">Built Interior — Six-Bedroom Duplex, Ado</div>
  </div>
  __FOOT3__
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
  __FOOT4__
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
  __FOOT5__
</section>

<!-- ════════ 7 · SELECTED WORK 03 — THE BODY SHOP ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 03</p>
    <h2>The Body Shop — Retail Interior</h2>
    <p class="sub">Retail interior fit-out for The Body Shop — Ikeja City Mall and
      Circle Mall, Lagos. Feature mural wall, timber shelving, display counters
      and lighting delivered from bare shell to trading floor.</p></div>

  <div class="fig big"><img src="__bs_hero__" alt="Body Shop feature mural wall interior" />
    <div class="cap"><span class="t">Feature Mural Wall &amp; Display Zone</span>
      <span class="m">Built Interior</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__bs_b__" alt="Body Shop retail trading floor" />
      <div class="cap"><span class="t">Retail Trading Floor</span>
        <span class="m">Fit-Out</span></div></div>
    <div class="fig half"><img src="__bs_c__" alt="Body Shop counter and display" />
      <div class="cap"><span class="t">Counter &amp; Display Detail</span>
        <span class="m">Interior</span></div></div>
  </div>
  __FOOT6__
</section>

<!-- ════════ 8 · SELECTED WORK 04 — ALCOVE HOMES ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 04</p>
    <h2>Alcove Homes — Residential Interior</h2>
    <p class="sub">A contemporary apartment interior — marble feature wall with
      cove lighting, bespoke joinery, console and display units in a warm
      timber-and-charcoal palette.</p></div>

  <div class="fig big"><img src="__alc_hero__" alt="Alcove Homes marble feature wall" />
    <div class="cap"><span class="t">Living Room — Marble Feature Wall</span>
      <span class="m">Built Interior</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__alc_b__" alt="Alcove Homes console and mirror" />
      <div class="cap"><span class="t">Console &amp; Mirror Joinery</span>
        <span class="m">Joinery</span></div></div>
    <div class="fig half"><img src="__alc_c__" alt="Alcove Homes study joinery" />
      <div class="cap"><span class="t">Study &amp; Display Joinery</span>
        <span class="m">Interior</span></div></div>
  </div>
  __FOOT7__
</section>

<!-- ════════ 9 · SELECTED WORK 05 — SIX-BEDROOM DUPLEX INTERIOR, ADO ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 05</p>
    <h2>Six-Bedroom Duplex Interior, Ado</h2>
    <p class="sub">Full interior finishes for a six-bedroom duplex — living,
      kitchen and dining spaces with marble surfaces, feature walls, bespoke
      cabinetry and coordinated lighting.</p></div>

  <div class="fig big"><img src="__ado_hero__" alt="Ado duplex living room interior" />
    <div class="cap"><span class="t">Living Room — Feature Wall &amp; Media Unit</span>
      <span class="m">Built Interior</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__ado_b__" alt="Ado duplex marble kitchen" />
      <div class="cap"><span class="t">Kitchen &amp; Island</span>
        <span class="m">Interior</span></div></div>
    <div class="fig half"><img src="__ado_c__" alt="Ado duplex dining room" />
      <div class="cap"><span class="t">Dining Room</span>
        <span class="m">Interior</span></div></div>
  </div>
  __FOOT8__
</section>

<!-- ════════ 10 · SELECTED WORK 06 — FINA TRUST BANK ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 06</p>
    <h2>Fina Trust Bank — Sales Outlet</h2>
    <p class="sub">Interior fit-out of a banking sales outlet — Orile, Lagos.
      Branded reception lounge, glazed partitions and workstation zones planned
      and delivered to the adopted layout.</p></div>

  <div class="fig big"><img src="__fina_hero__" alt="Fina Trust Bank branded reception lounge" />
    <div class="cap"><span class="t">Branded Reception Lounge</span>
      <span class="m">Built Interior</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__fina_b__" alt="Fina Trust Bank workstations" />
      <div class="cap"><span class="t">Workstation Zone</span>
        <span class="m">Fit-Out</span></div></div>
    <div class="fig half"><img src="__fina_c__" alt="Fina Trust Bank glazed partitions" />
      <div class="cap"><span class="t">Glazed Partitions &amp; Entrance</span>
        <span class="m">Interior</span></div></div>
  </div>
  __FOOT9__
</section>

<!-- ════════ 11 · SELECTED WORK 07 — SAPELE ROAD ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">Selected Work · 07</p>
    <h2>Sapele Road — Bespoke Joinery</h2>
    <p class="sub">Interior joinery and kitchen package for a private residence —
      fitted kitchen, media wall and wardrobe units in fluted timber, gloss
      lacquer and marble against porcelain surfaces.</p></div>

  <div class="fig big"><img src="__sap_hero__" alt="Sapele Road fitted kitchen" />
    <div class="cap"><span class="t">Fitted Kitchen</span>
      <span class="m">Built Interior</span></div></div>
  <div class="row2">
    <div class="fig half"><img src="__sap_b__" alt="Sapele Road media wall unit" />
      <div class="cap"><span class="t">Media Wall Unit</span>
        <span class="m">Joinery</span></div></div>
    <div class="fig half"><img src="__sap_c__" alt="Sapele Road wardrobe joinery" />
      <div class="cap"><span class="t">Wardrobe &amp; Storage</span>
        <span class="m">Interior</span></div></div>
  </div>
  __FOOT10__
</section>

<!-- ════════ 12 · MORE WORK ════════ -->
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">More Work</p>
    <h2>More Interior Details</h2>
    <p class="sub">Further finished interiors and bespoke joinery from across the
      completed residential and commercial projects.</p></div>

  <div class="other-grid">
    <div class="tile"><img src="__gm1__" alt="Ado duplex master bedroom" />
      <div class="cap"><span class="t">Master Bedroom Suite</span><span class="m">Interior</span></div></div>
    <div class="tile"><img src="__gm2__" alt="Ado duplex display niche joinery" />
      <div class="cap"><span class="t">Display Niche &amp; Joinery</span><span class="m">Interior</span></div></div>
    <div class="tile"><img src="__gm3__" alt="Alcove Homes marble media wall" />
      <div class="cap"><span class="t">Marble Media Wall</span><span class="m">Interior</span></div></div>
    <div class="tile"><img src="__gm4__" alt="Alcove Homes corridor light niche" />
      <div class="cap"><span class="t">Corridor Light Niche</span><span class="m">Interior</span></div></div>
    <div class="tile"><img src="__gm5__" alt="Sapele Road kitchen island and vanity" />
      <div class="cap"><span class="t">Kitchen Island &amp; Vanity</span><span class="m">Joinery</span></div></div>
    <div class="tile"><img src="__gm6__" alt="Ado duplex 3D textured feature wall" />
      <div class="cap"><span class="t">3D Textured Feature Wall</span><span class="m">Interior</span></div></div>
  </div>
  __FOOT11__
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
    for n in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11):
        body = body.replace(f"__FOOT{n}__", FOOTER.format(n=f"{n:02d}"))

    html = (
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
        f"<style>{FONT_FACES}{CSS}</style></head><body>{body}</body></html>"
    )
    HTML(string=html, base_url=ROOT).write_pdf(OUT)
    print("Wrote", OUT, "·", round(os.path.getsize(OUT) / 1024), "KB")


if __name__ == "__main__":
    build()
