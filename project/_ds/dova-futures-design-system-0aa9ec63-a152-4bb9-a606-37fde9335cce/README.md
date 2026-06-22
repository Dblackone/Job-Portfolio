# DOVA Futures — Design System

> The brand toolkit for **DOVA Futures Limited** (Dova Futures Developers) — a Nigerian
> design-build construction, interior, and development company. Premium, modern,
> sustainable, and architectural, anchored in **deep forest green**, natural materials,
> and bold, legible typography.

This project is the *source of truth* for designing on the DOVA brand: color &
type tokens, brand assets, reusable UI components, and full-screen UI-kit
recreations of the company's real products. Consuming projects link the single
root `styles.css`; the compiler indexes everything else.

---

## 1. Company context

**DOVA Futures Limited** delivers integrated **design-build** construction across
Nigeria — architectural planning, full-scale construction, premium interior
fit-outs, renovations, landscaping, and real-estate development. The pitch:
*design and construction under one roof* — eliminating the disconnect between
drawings and on-site execution for predictable budgets and exceptional outcomes.

- **Tagline:** "Rethink the future" · headline voice: *"Designed With Intent. Built With Precision."*
- **Positioning:** premium, professional, innovative, reliable, long-term value.
- **Brand pillars:** professionalism, innovation, reliability, sustainability.
- **Founder/CEO:** Vollmann Olamide Akarakiri — Construction Project Manager & BIM
  specialist (Revit, Dynamo, AutoCAD, Navisworks). The company's depth is in BIM-led,
  technology-driven project delivery.
- **Reach:** Lagos HQ; projects across Ondo, Ekiti, Edo and multiple Nigerian states.
  Currency is the **Naira (₦)**.
- **Contact:** info@dovafutures.com · +234 816 367 5439 · dovafutures.com ·
  Instagram / TikTok / WhatsApp.

### Products represented
1. **Dova Futures website** (`dovafutures.com`) — the primary marketing product. A
   premium single-page design-build site: hero with a before/after "draft → render"
   reveal slider, services, projects portfolio, 5-step process, why-us, contact.
2. **Akarakiri AEC Portfolio** — the founder's professional portfolio product
   (architecture / BIM / construction / landscape). A warm, polished case-study site.

> **Design-direction note (important):** the brief calls for a **dark-green,
> sustainability-forward** identity. The *existing* websites use charcoal+cream
> (Dova) and warm-clay+off-white (Portfolio). This design system **evolves** those
> into the requested green direction: deep forest green becomes the primary brand
> color, the signature **cream (`#F5EFE8`)** and natural sand/stone neutrals carry
> over, **clay/terracotta** is retained as a restrained secondary accent (a natural
> material tone), and the **Bebas Neue + Inter** type pairing is preserved.

---

## 2. Sources (provided inputs)

Build designs by referencing these. Don't assume the reader has access; stored for
those who do.

- **GitHub — `Dblackone/Dova-futures`** · https://github.com/Dblackone/Dova-futures
  The production company website (`index.html`, Tailwind CDN + custom CSS). Source of
  the brand voice, section structure, palette (`#333`/`#1f1f1f`/`#F5EFE8`), and the
  Bebas Neue + Inter pairing. Logos & project imagery live under `/assets`.
- **GitHub — `Dblackone/Job-Portfolio`** · https://github.com/Dblackone/Job-Portfolio
  The "Akarakiri Portfolio System" — founder's AEC portfolio. A more developed CSS
  token system (`css/styles.css`: warm off-white, terracotta `#B85C38`, slate text,
  reveal animations, pill tags, stat boxes). Source for component patterns and the
  clay accent.

Explore these repos further to recreate DOVA designs with higher fidelity.

**Assets imported into this system** (`/assets/`):
- `logo/DOVA Logo.png` — black line-art building skyline + wordmark (light backgrounds)
- `logo/DOVA Logo - W.png` — white version (dark/green backgrounds)
- `logo/DOVA Logo metadata.png` — bold wordmark variant
- `projects/ado-hall/before.jpg`, `after.png` — before/after hero reveal imagery
- `widgets/icons/{instagram,tiktok,whatsapp}.svg` — social glyphs

---

## 3. CONTENT FUNDAMENTALS — how DOVA writes

**Voice:** confident, precise, premium. Speaks like a master builder who is also a
designer — engineering language ("precision", "engineered", "coordination",
"buildability") fused with aspiration ("landmarks", "vision", "future-ready").

- **Person:** addresses the client as **"you / your project / your vision"**; the
  company is **"we / our"**. Warm but authoritative — a trusted partner, not a vendor.
- **Casing:**
  - Display headlines in **Bebas Neue ALL-CAPS** (the font is caps-only).
  - **Eyebrows / kickers** are short uppercase Inter labels with wide tracking
    (`Who We Are`, `What We Do`, `Our Advantage`) — always above a headline.
  - Body copy is sentence case.
- **Headline style:** short, declarative, often paired clauses with periods —
  *"Designed With Intent. Built With Precision."* · *"Let's Build It Properly."* ·
  *"Building Tomorrow's Landmarks."* Confident full stops, not exclamation marks.
- **Body copy:** measured, benefit-led, no fluff. Sentences run 1–3 lines. Leads with
  outcomes (transparency, predictable budgets, quality) then mechanism (design-build,
  one roof, structured supervision).
- **Numbers:** real metrics build trust — `20+ concurrent sites`, `₦350M+ project
  value`, `₦10M+ savings`, `5-step process`. Always Naira `₦` for money.
- **Punctuation flourish:** the en-dash in **"design–build"** is part of the brand
  lexicon. Section CTAs use first-person-plural invitations ("Let's discuss…").
- **Tone words to reach for:** integrated, seamless, precision, premium, transparent,
  buildability, handover, craftsmanship, future-ready, sustainable.
- **Emoji:** **none.** This is a premium professional brand. Use real icons/logos,
  never emoji, never decorative unicode in marketing surfaces.

**Examples (verbatim from the site):**
- Eyebrow → headline: `WHAT WE DO` / **OUR CORE SERVICES**
- Hero sub: *"Rethink the future — integrated design and construction excellence,
  engineered for precision."*
- Difference: *"We eliminate the disconnect between architectural drawings and on-site
  execution."*
- CTA: **"Let's Build It Properly."**

---

## 4. VISUAL FOUNDATIONS

**Overall vibe:** premium architectural minimalism. Dark, confident surfaces; generous
negative space; thin framing lines; big condensed type; real project photography. It
should feel like a high-end architecture monograph — calm, precise, expensive.

### Color
- **Primary:** deep **forest green** `--green-700 #1C4636`, deepening to
  `--green-800/900/950` for full-bleed dark sections (the brand's signature surface).
  Green replaces the legacy charcoal as the identity color while keeping the same
  dark, premium feel.
- **Natural neutrals:** signature **cream `#F5EFE8`** for light "material" sections,
  plus **sand** and **stone** for borders/sunken surfaces. These carry the
  sustainability / natural-material story.
- **Ink:** near-black `#1A1A1A` for headings on light; **slate `#4A4F5C`** for body.
- **Accent:** **clay / terracotta `#B85C38`** — used sparingly (links, small accents,
  one-off highlights). A warm natural counterpoint to the green, never dominant.
- **Usage rhythm:** alternate dark-green sections with cream sections down a page for
  intentional contrast. Green is the hero; cream is the breather; clay is the spark.

### Type
- **Display:** **Bebas Neue** — condensed all-caps, slight positive tracking
  (`0.02em`). Used huge for hero/section headlines (`clamp(64px,9vw,128px)`).
- **Body & UI:** **Inter** 300–800. Body at 17px, `line-height ~1.6–1.75`. Large Inter
  headings get tight tracking (`-0.02em`); uppercase eyebrows get wide tracking
  (`0.28em`).
- Pairing logic: Bebas = the architecture/brand voice; Inter = the legible workhorse.

### Spacing & layout
- **8px base grid.** Section vertical padding `120px` desktop / `80px` mobile.
- Centered **1280px max** container, `32px` side padding.
- Fixed translucent top nav with blur; `max-w-7xl` content columns; 2–3 col grids.

### Backgrounds & texture
- Full-bleed **dark green** surfaces; **cream** material sections.
- **Faint blueprint grid** overlay on dark heroes (`60px` lines at ~3–4% white) — a
  subtle engineering/drafting cue, never loud.
- **Real project photography** (warm, architectural, daylight) behind dark gradient
  protection overlays. No stock-looking gradients-as-decoration, no purple/blue
  gradients, no AI-slop imagery.
- Signature **before/after reveal slider** (draft → render) as a hero device.

### Borders, radii, shadows
- **Radii:** architectural restraint — mostly **sharp** (`0–4px`). Cards/buttons use
  `2–4px`; inputs `8px`; pills only for tags/skill chips. Avoid big rounded corners.
- **Borders:** **hairline framing** — `1px` lines at low-opacity white on dark
  (`rgba(245,239,232,0.14)`) or `--stone` on light. Thin outlined boxes around icons
  and offset framing rectangles are a recurring motif.
- **Shadows:** soft and restrained — `0 4px 24px rgba(26,26,26,.08)` for cards,
  deeper `0 12px 48px` on hover-lift. A green-tinted shadow for primary buttons.

### Motion
- Calm `cubic-bezier(0.22,0.61,0.36,1)` easing, `0.3s` base.
- **Scroll-reveal**: fade + 32px rise, small stagger (`0.1s` steps).
- **Hover:** links get an underline that grows from the left; cards **lift**
  (`translateY(-4 to -6px)`) + deepen shadow; project cards reveal a caption that
  slides up from the bottom. Outlined buttons **invert** (fill on hover).
- **Press:** subtle — color shift / slight translate. No bouncy or playful motion.
- Respect `prefers-reduced-motion`.

### Hover / press states (quick reference)
- **Primary button** (green fill): darkens to `--green-800`, slight lift + green shadow.
- **Outline button:** transparent → fills (cream/green) on hover, text inverts.
- **Nav link:** color → green/clay, underline grows from left.
- **Card:** lift + shadow; inner caption fades/slides in.

### Transparency & blur
- Nav bar: `~90%` opacity brand surface + `blur(12px)` backdrop.
- Dark gradient "protection" overlays over photos (not capsules) for text legibility.

---

## 5. ICONOGRAPHY

- **Approach:** thin, **1.5px-stroke line icons** drawn on a 24px grid — matching the
  architectural line-art of the logo. The existing site hand-codes inline `<svg>`
  stroke icons (building, home, layers, shield, clock, users, star, eye, phone,
  envelope). Geometric, outline, no fills.
- **Recommended set:** **Lucide** (https://lucide.dev) — its 1.5–2px geometric outline
  style is the closest CDN match to the site's hand-rolled icons. Use Lucide via CDN
  in kits/slides rather than re-drawing SVGs. *(Substitution flagged: the brand has no
  packaged icon font; Lucide is the nearest match to its existing inline strokes.)*
- **Social glyphs:** brand-provided SVGs in `assets/widgets/icons/`
  (Instagram, TikTok, WhatsApp).
- **Emoji:** never. **Unicode geometric marks** (⬡ ◈ ⬟ ⬗ ◉) appear as decorative
  bullets in the portfolio product only — acceptable there, but prefer Lucide line
  icons for DOVA-brand surfaces.
- **Logo:** the line-art building-skyline mark + "DOVA FUTURES DEVELOPERS" wordmark.
  Use `DOVA Logo - W.png` on green/dark, `DOVA Logo.png` on cream/light. Give it clear
  space; never recolor or stretch.

---

## 6. Index / manifest

**Root**
- `styles.css` — global entry point (consumers link this). `@import`s only.
- `README.md` — this guide.
- `SKILL.md` — Agent-Skill wrapper.

**`tokens/`** — `fonts.css` · `colors.css` · `typography.css` · `spacing.css` · `effects.css`

**`assets/`** — `logo/` (3 logo variants) · `projects/ado-hall/` (before/after) ·
`widgets/icons/` (social SVGs)

**`guidelines/`** — 12 foundation specimen cards (Design System tab): Colors (green
scale, neutrals, ink, accent/semantic) · Type (display, body, eyebrow) · Spacing
(scale, shadows) · Brand (logo, surfaces, blueprint grid).

**`components/`** — `core/` Button, Eyebrow/SectionHeader, Badge/Tag, Stat ·
`surfaces/` Card/ServiceCard/ProjectCard · `forms/` Field/Input/Textarea. Each has
`.d.ts` + a `@dsCard` demo; key ones have `.prompt.md`. Mount via
`window.DOVAFuturesDesignSystem_0aa9ec`.

**UI kits** — `ui_kits/dova-website/` — interactive recreation of the marketing site
(Home with before/after reveal slider, filterable Projects, Contact form).
`ui_kits/akarakiri-portfolio/` is a noted next step (secondary product).

---

## 7. Status / next up

✅ Tokens, fonts, `styles.css`, brand assets, README · 12 foundation cards ·
13 components (3 demo cards) · `dova-website` UI kit · `SKILL.md`.
🔜 Akarakiri AEC-portfolio UI kit (secondary product) · self-hosted webfonts if needed ·
real per-project photography to replace the Ado Hall stand-in imagery.

> **Fonts:** Bebas Neue + Inter are the brand's real fonts, loaded from Google Fonts —
> no substitution. If you need them self-hosted/offline, ask and I'll vendor the `.woff2`s.
