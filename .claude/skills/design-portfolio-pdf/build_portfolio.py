#!/usr/bin/env python3
"""
Data-driven builder for premium A4 PDF portfolios (Akarakiri house style:
warm off-white + terracotta + Inter).  See SKILL.md for the full method.

Fill CONFIG (or pass your own dict to build()) and run:

    python3 build_portfolio.py

Fonts/images are embedded as base64 so the PDF is fully self-contained.
Dependencies:  pip install weasyprint pillow   (QA: pip install pymupdf)

Every section is optional. The order of pages follows the keys present in
CONFIG: cover, about, skills, experience, expertise, then each item in
selected_work, then gallery, then contact. Page footers and the "n / total"
numbering are added automatically to the light content pages.
"""

import base64
import io
import os
import html as _html

from PIL import Image
from weasyprint import HTML

# Resolved per build() call; image paths in CONFIG are relative to this.
_BASE = "."


# ───────────────────────── asset embedding helpers ─────────────────────────

def _font_uri(font_dir, weight):
    with open(os.path.join(font_dir, f"inter-{weight}.woff2"), "rb") as fh:
        return "data:font/woff2;base64," + base64.b64encode(fh.read()).decode()


def img_uri(path, max_px=1280, quality=82, keep_alpha=False):
    """Optimise (downscale + recompress) an image -> base64 data URI."""
    im = Image.open(os.path.join(_BASE, path))
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
    return f"data:{mime};base64," + base64.b64encode(buf.getvalue()).decode()


def font_faces(font_dir):
    return "".join(
        "@font-face{font-family:'Inter';font-style:normal;font-weight:%d;"
        "src:url('%s') format('woff2');}" % (w, _font_uri(font_dir, w))
        for w in (300, 400, 500, 600, 700, 800)
    )


def esc(s):
    return _html.escape(str(s), quote=True)


# Geometric glyphs that exist in Inter (cycle for card icons).
ICONS = ["&#9670;", "&#9671;", "&#9633;", "&#9650;", "&#9632;", "&#9679;"]


# ───────────────────────────────── styles ──────────────────────────────────
# NOTE: this CSS is the proven design system; keep it in sync with the house
# style. (Generated/maintained alongside the reference project's build.py.)

CSS = r'''
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
.tl ul li::before{ content:'\2192'; left:0; top:2px; width:auto; height:auto;
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

/* ───── compact technical toolkit (merged onto the profile page) ───── */
.tk-grid{ display:grid; grid-template-columns:1fr 1fr; gap:7px; }
.tk{ background:var(--bg); border-radius:6px; padding:8px 11px;
  border-left:2px solid var(--accent); }
.tk .tkn{ display:block; font-size:10.5px; font-weight:600; color:var(--dark); }
.tk .tkl{ display:block; font-size:8.5px; color:var(--accent); margin-top:1px; }

/* ───── CASE STUDY ANNOTATION PAGE ───── */
.casestudy{ display:grid; grid-template-columns:1fr 1fr; gap:9mm 12mm; }
.cs-item .cs-label{ font-size:9px; font-weight:600; letter-spacing:0.14em;
  text-transform:uppercase; color:var(--accent); margin-bottom:6px;
  padding-bottom:6px; border-bottom:1px solid var(--border); }
.cs-item p{ font-size:10.5px; line-height:1.68; color:var(--text); }

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
'''


# ───────────────────────────── section builders ────────────────────────────
# Each returns one <section class="sheet …"> string. Builders that take a page
# footer include the literal token __FOOT__ which build() replaces with the
# numbered footer.

def _contact_items(contact, cls):
    out = []
    for label, val in contact.items():
        if isinstance(val, (list, tuple)):  # (display, href) -> clickable
            disp, href = val
            v = f'<a href="{esc(href)}">{esc(disp)}</a>'
        else:
            v = esc(val)
        out.append(f'<div class="ci"><div class="cl">{esc(label)}</div>'
                    f'<div class="cv">{v}</div></div>')
    return "".join(out)


def _band(band):
    if not band:
        return ""
    cap = f'<div class="cap">{esc(band["caption"])}</div>' if band.get("caption") else ""
    mp = band.get("max_px", 1600)
    return (f'<div class="img-band"><img src="{img_uri(band["image"], max_px=mp, quality=84)}" '
            f'alt="" />{cap}</div>')


def cover_sheet(p, band=None):
    head = "".join(
        f'<span class="{c}">{esc(t)}</span>' if c else f'<span>{esc(t)}</span>'
        for t, c in p["headline"])
    points = "".join(f"<li>{esc(x)}</li>" for x in p.get("hero_points", []))
    stats = "".join(f'<div class="b"><div class="n">{esc(n)}</div>'
                    f'<div class="l">{esc(l)}</div></div>'
                    for n, l in p.get("cover_stats", []))
    pills = "".join(f"<span>{esc(x)}</span>" for x in p.get("pills", []))
    avail = (f'<div class="avail"><div class="dot"></div><span>{esc(p["availability"])}'
             f'</span></div>') if p.get("availability") else ""
    profile_img = (f'<img class="photo" src="{img_uri(p["profile_photo"], max_px=760, keep_alpha=True)}" alt="" />'
                   if p.get("profile_photo") else "")
    return f"""
<section class="sheet cover">
  <div class="cover-shape"></div>
  <div class="cover-top">
    <div class="brand"><div class="mark">{esc(p.get("initial","•"))}</div>
      <div class="nm">{esc(p.get("brand", p["name"]))}</div></div>
    <div class="cover-tag">{esc(p.get("portfolio_tag","Professional Portfolio"))}</div>
  </div>
  <div class="hero">
    <div>
      <p class="label hero-label">{esc(p.get("kicker",""))}</p>
      <div class="headline">{head}</div>
      <p class="hero-sub">{esc(p.get("hero_sub",""))}</p>
      <ul class="hero-points">{points}</ul>
    </div>
    <aside class="pcard">{profile_img}
      <div class="info">
        <div class="accent-bar"></div>
        <h3>{esc(p["name"])}</h3>
        <div class="role">{esc(p.get("role",""))}</div>
        <div class="loc">{esc(p.get("location",""))}</div>
        <div class="pstats">{stats}</div>
        <div class="psw">{pills}</div>
        {avail}
      </div>
    </aside>
  </div>
  {_band(band)}
  <div class="cover-foot">{_contact_items(p.get("contact",{}), "cover")}</div>
</section>"""


def about_sheet(a, band=None):
    paras = "".join(f"<p>{esc(t)}</p>" for t in a.get("paragraphs", []))
    stats = "".join(f'<div class="st"><div class="n">{esc(n)}</div>'
                    f'<div class="d">{esc(d)}</div></div>'
                    for n, d in a.get("stats", []))
    groups = ""
    for g in a.get("competencies", []):
        pills = "".join(f"<span>{esc(x)}</span>" for x in g["items"])
        groups += f'<div class="skill-group"><h4>{esc(g["title"])}</h4><div class="pills">{pills}</div></div>'
    edu = ""
    for e in a.get("education", []):
        edu += (f'<div class="edu"><div class="dg">{esc(e["degree"])}</div>'
                f'<div class="in">{esc(e["institution"])}</div>'
                f'<div class="pe">{esc(e["period"])}</div></div>')
    edu_html = f'<div class="edu-grid">{edu}</div>' if edu else ""
    comp = (f'<p class="label" style="margin-bottom:9px;">{esc(a.get("competencies_label","Core Competencies"))}</p>'
            + groups) if groups else ""
    # Optional compact technical toolkit, folded onto the profile page so the
    # profile and toolkit share one page.
    tk = ""
    for name, level in a.get("toolkit", []):
        tk += (f'<div class="tk"><span class="tkn">{esc(name)}</span>'
               f'<span class="tkl">{esc(level)}</span></div>')
    tk_html = (f'<p class="label" style="margin:7mm 0 8px;">'
               f'{esc(a.get("toolkit_label","Technical Toolkit"))}</p>'
               f'<div class="tk-grid">{tk}</div>') if tk else ""
    return f"""
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">{esc(a.get("label","Professional Profile"))}</p>
    <h2>{esc(a.get("heading",""))}</h2></div>
  <div class="about">
    <div>{paras}<div class="stat-grid">{stats}</div></div>
    <div>{comp}{tk_html}</div>
  </div>
  {edu_html}
  {_band(band)}
  __FOOT__
</section>"""


def skills_sheet(s):
    cards = ""
    for i, c in enumerate(s.get("cards", [])):
        ic = c.get("icon", ICONS[i % len(ICONS)])
        cards += (f'<div class="sw"><div class="ic">{ic}</div><h4>{esc(c["name"])}</h4>'
                  f'<div class="lv">{esc(c.get("level",""))}</div>'
                  f'<p>{esc(c.get("desc",""))}</p></div>')
    tags = "".join(f"<span>{esc(x)}</span>" for x in s.get("tags", []))
    tags_html = f'<div class="disc">{tags}</div>' if tags else ""
    sub = f'<p class="sub">{esc(s["sub"])}</p>' if s.get("sub") else ""
    return f"""
<section class="sheet dark">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">{esc(s.get("label","Technical Expertise"))}</p>
    <h2>{esc(s.get("heading","Software & Skills"))}</h2>{sub}</div>
  <div class="sw-grid">{cards}</div>
  {tags_html}
</section>"""


def experience_sheet(e):
    items = ""
    for j in e.get("roles", []):
        bullets = "".join(f"<li>{esc(b)}</li>" for b in j.get("bullets", []))
        cur = " cur" if j.get("current") else ""
        items += (f'<li class="exp{cur}"><div class="pe">{esc(j["period"])}</div>'
                  f'<div class="ro">{esc(j["role"])}</div>'
                  f'<div class="co">{esc(j["company"])}</div><ul>{bullets}</ul></li>')
    metrics = "".join(f'<div class="st"><div class="n">{esc(n)}</div>'
                      f'<div class="d">{esc(d)}</div></div>'
                      for n, d in e.get("metrics", []))
    metrics_html = f'<div class="metrics">{metrics}</div>' if metrics else ""
    sub = f'<p class="sub">{esc(e["sub"])}</p>' if e.get("sub") else ""
    return f"""
<section class="sheet">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">{esc(e.get("label","Career History"))}</p>
    <h2>{esc(e.get("heading","Professional Experience"))}</h2>{sub}</div>
  <ul class="tl">{items}</ul>
  {metrics_html}
  __FOOT__
</section>"""


def expertise_sheet(x, band=None):
    cards = ""
    for i, c in enumerate(x.get("cards", [])):
        ic = c.get("icon", ICONS[i % len(ICONS)])
        tag = f'<div class="tag">{esc(c["tag"])}</div>' if c.get("tag") else ""
        cards += (f'<div class="card"><div class="top"></div><div class="bd">'
                  f'<div class="ic">{ic}</div><h3>{esc(c["title"])}</h3>'
                  f'<p>{esc(c.get("desc",""))}</p>{tag}</div></div>')
    sub = f'<p class="sub">{esc(x["sub"])}</p>' if x.get("sub") else ""
    return f"""
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">{esc(x.get("label","Portfolio"))}</p>
    <h2>{esc(x.get("heading","Areas of Expertise"))}</h2>{sub}</div>
  <div class="cards">{cards}</div>
  {_band(band)}
  __FOOT__
</section>"""


def _fig(item, big=False, contain=False):
    img, cap, tag = (item + ("", "", ""))[:3] if isinstance(item, (list, tuple)) else (item, "", "")
    cls = "fig big" + (" contain" if contain else "") if big else "fig half"
    mp = 1600 if big else 1100
    capbar = ""
    if cap or tag:
        capbar = (f'<div class="cap"><span class="t">{esc(cap)}</span>'
                  f'<span class="m">{esc(tag)}</span></div>')
    return (f'<div class="{cls}"><img src="{img_uri(img, max_px=mp)}" alt="" />{capbar}</div>')


def selectedwork_sheet(sw, idx):
    hero = _fig(sw["hero"], big=True, contain=sw.get("hero_contain", False))
    supp = "".join(_fig(s) for s in sw.get("supporting", []))
    row = f'<div class="row2">{supp}</div>' if supp else ""
    sub = f'<p class="sub">{esc(sw["sub"])}</p>' if sw.get("sub") else ""
    label = sw.get("label", f"Selected Work · {idx:02d}")
    return f"""
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">{esc(label)}</p>
    <h2>{esc(sw["title"])}</h2>{sub}</div>
  {hero}
  {row}
  __FOOT__
</section>"""


CASE_STUDY_FIELDS = [
    ("contribution", "My Contribution"),
    ("process", "Project Process"),
    ("constraints", "Project Constraints"),
    ("solutions", "Solutions"),
    ("highlights", "Project Highlights"),
    ("notes", "Additional Notes"),
]

def case_study_sheet(sw, idx):
    cs = sw.get("case_study", {})
    label = sw.get("label", f"Selected Work · {idx:02d}") + " — Case Study"
    items = "".join(
        f'<div class="cs-item"><div class="cs-label">{esc(title)}</div>'
        f'<p>{cs.get(key, "")}</p></div>'
        for key, title in CASE_STUDY_FIELDS
    )
    return f"""
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">{esc(label)}</p>
    <h2>{esc(sw["title"])}</h2></div>
  <div class="casestudy">{items}</div>
  __FOOT__
</section>"""


def gallery_sheet(g):
    tiles = ""
    for item in g.get("tiles", []):
        img, title, tag = (list(item) + ["", ""])[:3]
        tiles += (f'<div class="tile"><img src="{img_uri(img, max_px=860, quality=80)}" alt="" />'
                  f'<div class="cap"><span class="t">{esc(title)}</span>'
                  f'<span class="m">{esc(tag)}</span></div></div>')
    sub = f'<p class="sub">{esc(g["sub"])}</p>' if g.get("sub") else ""
    return f"""
<section class="sheet white">
  <div class="s-head"><div class="accent-bar"></div>
    <p class="label" style="margin-top:9px;">{esc(g.get("label","More Work"))}</p>
    <h2>{esc(g.get("heading","Other Projects"))}</h2>{sub}</div>
  <div class="other-grid">{tiles}</div>
  __FOOT__
</section>"""


def contact_sheet(c):
    btns = ""
    for b in c.get("buttons", []):
        cls = "solid" if b.get("primary") else "out"
        btns += f'<a class="{cls}" href="{esc(b["href"])}">{esc(b["label"])}</a>'
    btns_html = f'<div class="cbtns">{btns}</div>' if btns else ""
    details = f'<div class="cdetails">{_contact_items(c.get("details",{}), "c")}</div>' if c.get("details") else ""
    foot = f'<div class="cfoot">{esc(c["footer"])}</div>' if c.get("footer") else ""
    return f"""
<section class="sheet dark">
  <div class="contact">
    <p class="label">{esc(c.get("label","Get In Touch"))}</p>
    <h2>{esc(c.get("heading","Ready to Work Together?"))}</h2>
    <p class="lead">{esc(c.get("lead",""))}</p>
    {btns_html}
    {details}
  </div>
  {foot}
</section>"""


# ─────────────────────────────────── build ─────────────────────────────────

def build(config, base_dir=".", out=None, font_dir=None):
    global _BASE
    _BASE = base_dir
    font_dir = font_dir or config.get("fonts_dir") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "fonts")
    out = out or config.get("output", "portfolio.pdf")

    sheets = []
    if config.get("cover"):
        sheets.append(cover_sheet(config["cover"], config.get("cover_band")))
    if config.get("about"):
        sheets.append(about_sheet(config["about"], config["about"].get("band")))
    if config.get("skills"):
        sheets.append(skills_sheet(config["skills"]))
    if config.get("experience"):
        sheets.append(experience_sheet(config["experience"]))
    if config.get("expertise"):
        sheets.append(expertise_sheet(config["expertise"], config["expertise"].get("band")))
    for i, sw in enumerate(config.get("selected_work", []), start=1):
        sheets.append(selectedwork_sheet(sw, i))
        if sw.get("case_study"):
            sheets.append(case_study_sheet(sw, i))
    if config.get("gallery"):
        sheets.append(gallery_sheet(config["gallery"]))
    if config.get("contact"):
        sheets.append(contact_sheet(config["contact"]))

    total = len(sheets)
    foot_name = config.get("footer_text", config.get("cover", {}).get("name", ""))
    body = ""
    for n, sheet in enumerate(sheets, start=1):
        footer = (f'<div class="pfoot"><span class="nm">{esc(foot_name)}</span>'
                  f'<span>{n:02d} / {total:02d}</span></div>')
        body += sheet.replace("__FOOT__", footer)

    html = ("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
            f"<style>{font_faces(font_dir)}{CSS}</style></head><body>{body}</body></html>")
    HTML(string=html, base_url=base_dir).write_pdf(out)
    print("Wrote", out, "·", round(os.path.getsize(out) / 1024), "KB ·", total, "pages")
    return out


# ─────────────────────────── EXAMPLE CONFIG ────────────────────────────────
# Replace values + image paths with your own. Paths are relative to base_dir.
# This mirrors the structure of the reference construction portfolio.

EXAMPLE_CONFIG = {
    "output": "portfolio.pdf",
    "cover": {
        "name": "Your Name", "brand": "Your Name", "initial": "Y",
        "role": "Your Role", "location": "City, Country",
        "portfolio_tag": "Professional Design Portfolio · 2026",
        "kicker": "Your Role · Specialism · City",
        "headline": [("Word.", None), ("Accent.", "accent"),
                     ("Word.", None), ("Closer.", "muted")],
        "hero_sub": "One or two sentences of positioning.",
        "hero_points": ["Key point one", "Key point two", "Key point three"],
        "profile_photo": "assets/profile.png",
        "cover_stats": [("20+", "Metric"), ("100+", "Metric"), ("5+", "Years")],
        "pills": ["Tool", "Tool", "Tool", "Tool"],
        "availability": "Open to opportunities — worldwide & remote",
        "contact": {
            "Phone": "+000 000 0000",
            "Email": "you@example.com",
            "Location": "City, Country",
            # (display, href) tuple -> clickable link
            "LinkedIn": ("/in/your-handle", "https://www.linkedin.com/in/your-handle"),
        },
    },
    "cover_band": {"image": "assets/hero-band.jpg",
                   "caption": "Feature Project — Visualisation"},
    "about": {
        "label": "Professional Profile", "heading": "The Professional Behind the Work",
        "paragraphs": ["Bio paragraph one.", "Bio paragraph two."],
        "stats": [("20+", "Metric"), ("100+", "Metric"),
                  ("10+", "Metric"), ("5+", "Metric")],
        "competencies": [
            {"title": "Group A", "items": ["Skill", "Skill", "Skill"]},
            {"title": "Group B", "items": ["Skill", "Skill"]},
        ],
        "education": [
            {"degree": "Degree", "institution": "Institution", "period": "Year – Year"},
        ],
    },
    "skills": {
        "label": "Technical Expertise", "heading": "Software & Skills",
        "sub": "Tools used across every phase.",
        "cards": [
            {"name": "Tool", "level": "Expert", "desc": "What you do with it."},
            {"name": "Tool", "level": "Advanced", "desc": "What you do with it."},
        ],
        "tags": ["Discipline", "Discipline", "Discipline"],
    },
    "experience": {
        "label": "Career History", "heading": "Professional Experience",
        "sub": "Progressive responsibility across the field.",
        "roles": [
            {"period": "2021 – Present", "role": "Title", "company": "Company",
             "current": True, "bullets": ["Achievement one.", "Achievement two."]},
            {"period": "2019 – 2021", "role": "Title", "company": "Company",
             "bullets": ["Achievement."]},
        ],
        "metrics": [("100+", "Metric"), ("5+", "Metric")],
    },
    "expertise": {
        "label": "Portfolio", "heading": "Areas of Expertise",
        "sub": "Specialist disciplines.",
        "cards": [
            {"title": "Discipline", "desc": "Short description.", "tag": "TAG"},
            {"title": "Discipline", "desc": "Short description.", "tag": "TAG"},
        ],
        "band": {"image": "assets/expertise-band.jpg", "caption": "Project — Render"},
    },
    "selected_work": [
        {"title": "Project One", "sub": "One-line description.",
         "hero": ("assets/p1-hero.jpg", "Hero Caption", "Render"),
         "supporting": [("assets/p1-a.jpg", "Detail", "Detail"),
                        ("assets/p1-b.jpg", "Plan", "Documentation")]},
    ],
    "gallery": {
        "label": "More Work", "heading": "Other Projects",
        "sub": "Additional work from across the portfolio.",
        "tiles": [
            ("assets/g1.jpg", "Project", "Render"),
            ("assets/g2.jpg", "Project", "Concept"),
        ],
    },
    "contact": {
        "label": "Get In Touch", "heading": "Ready to Work Together?",
        "lead": "Closing call to action.",
        "buttons": [
            {"label": "Send an Email", "href": "mailto:you@example.com", "primary": True},
            {"label": "LinkedIn Profile", "href": "https://www.linkedin.com/in/your-handle"},
        ],
        "details": {
            "Phone": "+000 000 0000", "Email": "you@example.com",
            "Location": "City, Country",
            "LinkedIn": ("linkedin.com/in/your-handle", "https://www.linkedin.com/in/your-handle"),
        },
        "footer": "Your Name · Tagline.",
    },
}


if __name__ == "__main__":
    build(EXAMPLE_CONFIG, base_dir=".")
