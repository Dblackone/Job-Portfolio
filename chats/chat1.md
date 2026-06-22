# Multi-platform content wireframes

_Started 2026-06-21 16:29 UTC_

---

## User

<system-info comment="Only acknowledge these if relevant">
Project title is now "Untitled"
What `list_files` on the project root returns right now (dotfiles, if any, are not shown here):
📁 _ds
Current date is now June 21, 2026
</system-info>

<pasted_text name="Pasted text (476 lines)">
Create a Complete Content Kit for Claude-Design

Objective

Create a comprehensive, scalable, and brand-consistent Content Kit that serves as the foundation for all social media content generation, design creation, campaign planning, and automated publishing workflows.

The Content Kit will be used by AI systems to automatically generate content, captions, design briefs, social media graphics, and posting schedules while maintaining a consistent brand identity.

The final Content Kit should function as a single source of truth for all future content creation activities.

⸻

Brand Overview

Develop a complete Content Kit that includes:

* Brand Positioning
* Brand Personality
* Brand Voice
* Messaging Framework
* Design Language
* Visual Guidelines
* Content Categories
* Content Templates
* Caption Frameworks
* Hashtag Library
* CTA Library
* Content Calendar Structure

The system must be scalable and suitable for long-term content automation.

⸻

Section 1: Brand Foundation

Create and define:

Brand Mission

* Why the brand exists
* What value it provides

Brand Vision

* Long-term aspiration

Brand Values

* Core principles
* Company culture

Brand Promise

* What audiences should consistently expect

Brand Personality

Define the brand using clear personality traits such as:

* Professional
* Innovative
* Modern
* Creative
* Trustworthy
* Educational
* Inspiring

Include:

* Tone descriptions
* Communication style
* Audience perception goals

⸻

Section 2: Target Audience Profiles

Create detailed audience personas including:

Primary Audience

* Demographics
* Occupation
* Interests
* Pain Points
* Goals

Secondary Audience

* Demographics
* Interests
* Motivations

Audience Challenges

Identify:

* Problems they face
* Questions they ask
* Information they seek

⸻

Section 3: Brand Voice System

Create detailed voice guidelines.

Voice Characteristics

Define:

Professional Voice

Examples:

* Industry insights
* Project explanations

Inspirational Voice

Examples:

* New month posts
* Success stories

Educational Voice

Examples:

* Design tips
* Construction tips

Promotional Voice

Examples:

* Service announcements
* Project showcases

Include:

* Preferred wording
* Prohibited wording
* Sentence structure
* Writing style examples

⸻

Section 4: Visual Design System

Create a complete design system.

Color Palette

Define:

Primary Colors

* HEX Codes
* RGB Values
* Usage Rules

Secondary Colors

* HEX Codes
* RGB Values
* Usage Rules

Accent Colors

* HEX Codes
* RGB Values
* Usage Rules

⸻

Typography System

Define:

Headline Fonts

Usage:

* Hero graphics
* Announcements

Body Fonts

Usage:

* Captions
* Information sections

Accent Fonts

Usage:

* Quotes
* Highlights

⸻

Graphic Style

Define:

* Layout systems
* Grid systems
* Spacing rules
* Visual hierarchy
* Icon style
* Photography style
* Illustration style
* Rendering style
* Mockup style

⸻

Section 5: Content Pillars

Develop content pillars supporting long-term growth.

Pillar 1: Design Inspiration

Content Examples:

* Design Showcase
* Design of the Month
* Mood Boards

⸻

Pillar 2: Project Progress

Content Examples:

* Site Updates
* Milestones
* Construction Progress

⸻

Pillar 3: Project Showcase

Content Examples:

* Completed Projects
* Before &amp; After
* Client Results

⸻

Pillar 4: Educational Content

Content Examples:

* Design Tips
* Construction Tips
* Industry Insights

⸻

Pillar 5: Company Updates

Content Examples:

* Announcements
* Awards
* Partnerships

⸻

Pillar 6: Seasonal &amp; Holiday Content

Content Examples:

* New Month
* Public Holidays
* Special Events

⸻

Section 6: Content Templates

Create reusable templates for:

New Month Content

Include:

* Headline Formula
* Caption Formula
* CTA Formula

⸻

Design of the Month

Include:

* Feature Structure
* Storytelling Structure
* Caption Template

⸻

Project Highlight

Include:

* Challenge
* Solution
* Outcome

⸻

Design Showcase

Include:

* Design Concept
* Key Features
* Benefits

⸻

Project Showcase

Include:

* Overview
* Results
* Client Value

⸻

Holiday Content

Include:

* Greeting Formula
* Brand Message Formula

⸻

Special Announcement

Include:

* Announcement Structure
* CTA Structure

⸻

Section 7: Caption Library

Create caption frameworks for:

* Instagram
* Facebook
* LinkedIn
* X (Twitter)
* Threads
* WhatsApp Status

For each platform provide:

* Short-form format
* Medium-form format
* Long-form format

⸻

Section 8: CTA Library

Generate categorized calls-to-action.

Engagement CTAs

Examples:

* Comment below
* Share your thoughts

Lead Generation CTAs

Examples:

* Contact us
* Schedule a consultation

Community CTAs

Examples:

* Follow for more
* Join our community

⸻

Section 9: Hashtag Library

Create organized hashtag collections for:

* Design
* Architecture
* Construction
* Interior Design
* Real Estate
* Project Management
* Business
* Brand Awareness
* Local Market
* Seasonal Campaigns

Provide:

* High-volume hashtags
* Medium-volume hashtags
* Niche hashtags

⸻

Section 10: Content Calendar Framework

Create a repeatable monthly structure.

For each month include:

* New Month Content
* Weekly Project Highlights
* Weekly Design Showcase
* Monthly Design of the Month
* Monthly Project Showcase
* Holiday Posts
* Special Announcements

Provide recommended posting frequencies and platform priorities.

⸻

Section 11: AI Content Generation Rules

Create rules that future AI systems must follow.

Rules should include:

* Brand consistency requirements
* Design consistency requirements
* Caption formatting requirements
* CTA requirements
* Hashtag requirements
* Platform optimization requirements
* Content quality standards

⸻

Deliverable Format

Generate the final Content Kit as a professional reference document with:

1. Executive Summary
2. Brand Foundation
3. Audience Profiles
4. Brand Voice Guidelines
5. Visual Design System
6. Content Pillars
7. Content Templates
8. Caption Library
9. CTA Library
10. Hashtag Library
11. Monthly Content Calendar Framework
12. AI Content Generation Rules

The final Content Kit must be detailed enough that any AI system can independently create high-quality, on-brand content, captions, graphics, and publishing schedules without additional guidance.
</pasted_text>

<!-- The user explicitly selected the following skills for this project, as attachments to their message. These are not optional context — they define how you work. Use them. -->
<attached-skill name="Design Components">
This project uses Design Components: every design is a single streaming `Name.dc.html` file. The full authoring spec is in your system prompt under "Writing code — Design Components" — follow it. Author and edit `.dc.html` content with the `dc_write`, `dc_html_str_replace`, `dc_js_str_replace`, and `dc_set_props` tools (not `write_file`; `str_replace_edit` works but won't stream); template edits stream into the live preview as you type.
</attached-skill>

<attached-skill name="DOVA Futures Design System (design system)">
[Design System] This project uses the **DOVA Futures Design System** design system. This is a binding choice for visual style — every visual must follow it. Don't invent colors, type, spacing, or components not grounded here.

Scope: the design system is a visual style reference only. Its guide may describe example products, brands, or people that are unrelated to the user and unrelated to the subject of this conversation. Never treat anything in the design system as a fact about the user, their work, or the topic they asked about.

This project has the **DOVAFuturesDesignSystem_0aa9ec** design system bound at `_ds/dova-futures-design-system-0aa9ec63-a152-4bb9-a606-37fde9335cce/`. If anything under that path is missing or fails to load, the folder name may differ — `list_files` `_ds/` and use the folder whose name ends with 0aa9ec63-a152-4bb9-a606-37fde9335cce instead, including in the <link>/<script> paths below.

**Loading the bundle is how you use this design system.** Every Design Component you build must load `_ds/dova-futures-design-system-0aa9ec63-a152-4bb9-a606-37fde9335cce/_ds_bundle.js` once in `<helmet>` and compose with its components — do not recreate those components from scratch or restyle raw HTML to look like them. At the top of the template:

```html
<helmet>
  <link rel="stylesheet" href="_ds/dova-futures-design-system-0aa9ec63-a152-4bb9-a606-37fde9335cce/tokens/fonts.css">
  <link rel="stylesheet" href="_ds/dova-futures-design-system-0aa9ec63-a152-4bb9-a606-37fde9335cce/tokens/colors.css">
  <link rel="stylesheet" href="_ds/dova-futures-design-system-0aa9ec63-a152-4bb9-a606-37fde9335cce/tokens/typography.css">
  <link rel="stylesheet" href="_ds/dova-futures-design-system-0aa9ec63-a152-4bb9-a606-37fde9335cce/tokens/spacing.css">
  <link rel="stylesheet" href="_ds/dova-futures-design-system-0aa9ec63-a152-4bb9-a606-37fde9335cce/tokens/effects.css">
  <link rel="stylesheet" href="_ds/dova-futures-design-system-0aa9ec63-a152-4bb9-a606-37fde9335cce/styles.css">
  <script src="_ds/dova-futures-design-system-0aa9ec63-a152-4bb9-a606-37fde9335cce/_ds_bundle.js"></script>
</helmet>
```

Then mount any component directly in the template — no logic class needed:

```html
<x-import component-from-global-scope="DOVAFuturesDesignSystem_0aa9ec.Button" hint-size="auto,40px">Label</x-import>
```

Props are template attributes (kebab → camelCase); template children pass through as `props.children`. The linked stylesheet(s) carry the design tokens (colors, type, spacing) — style against those via `var(--*)` and the design system's classes rather than guessing values.

The full design-system source tree lives at `/projects/0aa9ec63-a152-4bb9-a606-37fde9335cce/` — use `list_files` / `read_file` from there for anything not under `_ds/` (layout varies by brand; don't assume folder names). Its guide is reproduced below so you don't need to fetch it:

<design-system-guide>
# DOVA Futures — Design System

&gt; The brand toolkit for **DOVA Futures Limited** (Dova Futures Developers) — a Nigerian
&gt; design-build construction, interior, and development company. Premium, modern,
&gt; sustainable, and architectural, anchored in **deep forest green**, natural materials,
&gt; and bold, legible typography.

This project is the *source of truth* for designing on the DOVA brand: color &amp;
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
- **Founder/CEO:** Vollmann Olamide Akarakiri — Construction Project Manager &amp; BIM
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

&gt; **Design-direction note (important):** the brief calls for a **dark-green,
&gt; sustainability-forward** identity. The *existing* websites use charcoal+cream
&gt; (Dova) and warm-clay+off-white (Portfolio). This design system **evolves** those
&gt; into the requested green direction: deep forest green becomes the primary brand
&gt; color, the signature **cream (`#F5EFE8`)** and natural sand/stone neutrals carry
&gt; over, **clay/terracotta** is retained as a restrained secondary accent (a natural
&gt; material tone), and the **Bebas Neue + Inter** type pairing is preserved.

---

## 2. Sources (provided inputs)

Build designs by referencing these. Don't assume the reader has access; stored for
those who do.

- **GitHub — `Dblackone/Dova-futures`** · https://github.com/Dblackone/Dova-futures
  The production company website (`index.html`, Tailwind CDN + custom CSS). Source of
  the brand voice, section structure, palette (`#333`/`#1f1f1f`/`#F5EFE8`), and the
  Bebas Neue + Inter pairing. Logos &amp; project imagery live under `/assets`.
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
- **Body &amp; UI:** **Inter** 300–800. Body at 17px, `line-height ~1.6–1.75`. Large Inter
  headings get tight tracking (`-0.02em`); uppercase eyebrows get wide tracking
  (`0.28em`).
- Pairing logic: Bebas = the architecture/brand voice; Inter = the legible workhorse.

### Spacing &amp; layout
- **8px base grid.** Section vertical padding `120px` desktop / `80px` mobile.
- Centered **1280px max** container, `32px` side padding.
- Fixed translucent top nav with blur; `max-w-7xl` content columns; 2–3 col grids.

### Backgrounds &amp; texture
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

### Transparency &amp; blur
- Nav bar: `~90%` opacity brand surface + `blur(12px)` backdrop.
- Dark gradient "protection" overlays over photos (not capsules) for text legibility.

---

## 5. ICONOGRAPHY

- **Approach:** thin, **1.5px-stroke line icons** drawn on a 24px grid — matching the
  architectural line-art of the logo. The existing site hand-codes inline `&lt;svg&gt;`
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

&gt; **Fonts:** Bebas Neue + Inter are the brand's real fonts, loaded from Google Fonts —
&gt; no substitution. If you need them self-hosted/offline, ask and I'll vendor the `.woff2`s.

</design-system-guide>

Per-component usage notes follow — the first lines of each component's `*.prompt.md`. These are NOT bound into `_ds/`, so they're reproduced here:

<ds-prompt-excerpts>
### components/core/Badge.prompt.md
Compact label for status, categories, and skill/category chips.

```jsx
&lt;Badge tone="green" variant="soft"&gt;Sustainable&lt;/Badge&gt;
&lt;Badge tone="clay" variant="outline"&gt;Interior Fit-out&lt;/Badge&gt;

### components/core/Button.prompt.md
Brand call-to-action button — green fill for primary actions; cream/outline-light on dark green; inverts/lifts on hover.

```jsx
&lt;Button variant="primary" size="lg"&gt;Start Your Project&lt;/Button&gt;
&lt;Button variant="cream"&gt;Let's Build It&lt;/Button&gt;

### components/core/Eyebrow.prompt.md
Uppercase, wide-tracked kicker that sits above a headline.

```jsx
&lt;Eyebrow&gt;What We Do&lt;/Eyebrow&gt;
&lt;Eyebrow color="green300"&gt;Our Advantage&lt;/Eyebrow&gt;

### components/core/SectionHeader.prompt.md
Standard section heading — a wide-tracked eyebrow over a Bebas display title.

```jsx
&lt;SectionHeader eyebrow="What We Do" title="OUR CORE SERVICES" /&gt;
&lt;SectionHeader onDark align="center" eyebrow="How We Work" title="OUR 5-STEP PROCESS" /&gt;

### components/core/Stat.prompt.md
Big-number trust metric — Bebas numeral over an uppercase label.

```jsx
&lt;Stat value="20+" label="Sites managed" onDark /&gt;
&lt;Stat value="₦350M+" label="Project value" onDark accent /&gt;

### components/core/Tag.prompt.md
Uppercase outline pill for skills and categories.

```jsx
&lt;Tag&gt;Architecture&lt;/Tag&gt;
&lt;Tag onDark&gt;BIM Coordination&lt;/Tag&gt;

### components/forms/Field.prompt.md
Labelled form-row wrapper. Pass the control as children.

```jsx
&lt;Field label="Full name" htmlFor="n"&gt;&lt;Input id="n" placeholder="Jane Adeyemi" /&gt;&lt;/Field&gt;
&lt;Field label="Project details" hint="Scope, location &amp; timeline." htmlFor="m"&gt;

### components/forms/Input.prompt.md
Plain text field with a green focus ring. Compose inside `&lt;Field&gt;` for a label.

```jsx
&lt;Field label="Email" htmlFor="e"&gt;&lt;Input id="e" type="email" placeholder="you@company.com" /&gt;&lt;/Field&gt;
&lt;Input invalid placeholder="Required" /&gt;

### components/forms/Textarea.prompt.md
Multi-line field matching `&lt;Input&gt;`, with vertical resize.

```jsx
&lt;Field label="Project details" htmlFor="m"&gt;&lt;Textarea id="m" rows={4} /&gt;&lt;/Field&gt;
```

### components/surfaces/Card.prompt.md
Surfaces for DOVA layouts — generic `Card`, icon `ServiceCard`, and photo `ProjectCard`.

```jsx
&lt;Card onDark&gt;{/* anything */}&lt;/Card&gt;
&lt;ServiceCard icon={&lt;BuildIcon/&gt;} title="Architectural Planning"&gt;
</ds-prompt-excerpts>
</attached-skill>

## Assistant

_[tool: read_skill_prompt]_

_[tool: list_files]_

_[tool: read_file]_

_[tool: read_file]_

_[tool: update_todos]_

_[tool: read_file]_

_[tool: update_todos]_

_[tool: set_project_title]_

Building the full Content Kit now — all 12 sections, fully styled with the DOVA Futures design system.

_[tool: dc_write]_

## Assistant

_[tool: update_todos]_

_[tool: set_project_title]_

_[tool: dc_write]_

## Assistant

_[tool: dc_write]_

_[tool: ready_for_verification]_

The ResizeObserver error is a benign browser-level notification unrelated to the content — it doesn't affect rendering or functionality. Calling verification again:

_[tool: ready_for_verification]_

_[tool: show_html]_

The `ResizeObserver` error is a harmless browser-environment notification from the DC preview frame — not from the document itself. It doesn't affect rendering, content, or print output. Here's a summary of what's been built:

---

**DOVA Futures Content Kit** is ready at `Content Kit.dc.html`. It includes all 12 sections:

| # | Section |
|---|---------|
| 00 | Executive Summary — brand stats, taglines, master CTA |
| 01 | Brand Foundation — mission, vision, values, promise, personality |
| 02 | Target Audience Profiles — primary, secondary, pain-point content hooks |
| 03 | Brand Voice System — 4 voice modes, word pairs, writing rules |
| 04 | Visual Design System — full colour palette with hex/RGB, type system, graphic rules |
| 05 | Content Pillars — 6 pillars with content examples and strategic goals |
| 06 | Content Templates — 6 reusable formats (new month, design of month, project highlight, showcase, holiday, announcement) |
| 07 | Caption Library — short/medium/long formats for all 6 platforms |
| 08 | CTA Library — engagement, lead generation, and community CTAs |
| 09 | Hashtag Library — 60+ tags across design, construction, Nigeria local, real estate, brand |
| 10 | Monthly Calendar — weekly posting structure, platform priorities, monthly checklist |
| 11 | AI Generation Rules — 15 binding rules covering voice, design, captions, hashtags, platforms |

**Next steps to consider:**
- Add real project photography assets for visual references
- Build per-platform graphic templates as companion DC files
- Export as PDF for team distribution via the Save as PDF skill

## User

Design wireframe samples of content/post across all platform

Design for;
1. Rendering Post
2. On site Progress post
3. Project Shoecase
New Month Content
Weekly Project Highlights
Weekly Design Showcase
Monthly Design of the Month
Monthly Project Showcase
Holiday Posts
Special Announcements

## Assistant

_[tool: update_todos]_

_[tool: delete_file]_

Splitting into 3 phases. Writing the core structure + first 5 sections now, then adding the remaining 5 via `str_replace`.

_[tool: dc_write]_

Now adding the remaining 5 sections (06–10) via `str_replace`:

_[tool: dc_html_str_replace]_

_[tool: ready_for_verification]_

_[tool: update_todos]_

_[tool: update_todos]_

Both deliverables are complete and clean:

**`Content Kit.dc.html`** — Full 12-section brand document covering executive summary, brand foundation, audience profiles, voice system, visual design system, content pillars, templates, caption library, CTA library, hashtag library, monthly calendar, and AI generation rules.

**`Post Wireframes.dc.html`** — 10 content types × 4 platform formats (Instagram · Story/WhatsApp · LinkedIn · X), each with designed post mockups using the DOVA visual language and 2 realistic on-brand captions per section. Navigate with the sticky tab bar at the top.

**When you return, optional next steps:**
- **PDF export** of the Content Kit (print-ready reference doc)
- **Save as standalone HTML** (single offline file for sharing)
- **Graphic template DCs** — actual production-ready graphic frames per content type (not wireframes — real design files for the social media team to fill in)

