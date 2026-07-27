# LinkedIn Carousels — Full Slide Specifications

Three fully specified carousels. Every slide gives slide number, title, text, visual
recommendation, icons, diagram, layout, and colour scheme — enough to build in Canva or Figma
without further decisions.

**All carousels use:** 1080 × 1350 px · export as PDF (LinkedIn document post) · type scale,
colours, margins and footer per `../BRAND.md`.

**Universal architecture:**

| Slide | Role | Scheme |
|---|---|---|
| 1 | Hook — the promise | **Dark** |
| 2 | The problem or the setup | Cream |
| 3–N-2 | One idea per slide | Cream |
| N-1 | The practical takeaway | Cream |
| N | CTA | **Dark** |

**Readability rule:** every carousel must make sense with no caption and no voiceover. Someone
who swipes and never reads the post should still learn the thing.

---
---

# CAROUSEL 01 — Who Actually Uses Your Model

**Week 7** · **Category:** BIM Basics · **KB:** L1.07 · **10 slides**
**Objective:** move the reader from "I build models" to "I build models for seven different people".

---

### Slide 1 — Hook

- **Eyebrow:** BIM BASICS · 01
- **Title:** `THE MODEL YOU ARE BUILDING IS NOT FOR YOU`
- **Text:** Seven people will use it. Each needs something different.
- **Visual:** Single large line icon, `users`, 200 × 200 px, clay, centred above the headline.
- **Icons:** `users` (Lucide)
- **Diagram:** None. Slide 1 is never busy.
- **Layout:** Icon centred at 30% height. Headline below, centred, 3 lines maximum. Sub-line
  below in Inter 36 px. Full name lockup at the bottom.
- **Colour:** **Dark scheme** — `#1C4636` background, `#F5EFE8` text, clay icon.

---

### Slide 2 — The setup

- **Eyebrow:** THE MISTAKE
- **Title:** `BUILT FOR ONE. USED BY SEVEN.`
- **Text:** Most models are structured around how the author works. Then six other people have
  to use them, and every one of them has to ask the author a question.
- **Visual:** Simple diagram — one filled clay circle on the left, six hollow green circles
  fanned to the right, thin clay arrows from the filled circle to each hollow one.
- **Icons:** None — the diagram carries it.
- **Layout:** Text block top half, diagram lower half, 400 px tall, centred.
- **Colour:** Cream scheme.

---

### Slides 3–9 — The seven roles

Identical layout. Only the icon, role, and text change. This repetition is the point — it makes
the carousel scannable and builds rhythm.

**Shared layout for slides 3–9:**

```
EYEBROW: ROLE 0[n] OF 07
[icon, 120 × 120 px, clay, left-aligned]
BEBAS HEADLINE — THE ROLE
──── clay rule
"They need:" (Inter 600, 36px)
• three bullets, Inter 30px
──── hairline
"They do not care about:" (Inter 400 italic, muted 24px, one line)
footer + slide number
```

| # | Role | Icon | They need | They do not care about |
|---|---|---|---|---|
| 3 | `THE CLIENT` | `briefcase` | Confidence the asset meets the brief · Structured asset data at handover · Cost certainty | Your view templates |
| 4 | `THE ARCHITECT` | `pen-tool` | Design intent held in one place · Spatial coordination · A drawing set that needs no patching | How many warnings you have — until they inherit them |
| 5 | `THE STRUCTURAL ENGINEER` | `frame` | Load paths · Member sizing · Grids that agree with yours | Your material finishes |
| 6 | `THE MEP ENGINEER` | `git-merge` | The space that is actually left · Real ceiling voids, not approximate ones · Coordinated risers | Your rendering settings |
| 7 | `THE CONTRACTOR` | `hard-hat` | Buildability · Sequencing · Quantities and site logistics | Design intent, once it is priced |
| 8 | `THE COST CONSULTANT` | `calculator` | Measurement tied to model elements · Layered wall and floor types · Consistent classification | Anything that is not measurable |
| 9 | `THE FACILITIES MANAGER` | `wrench` | What is installed and where · Maintenance intervals · Asset IDs that persist | The design model. They need the asset information model. |

**Colour for 3–9:** Cream scheme. Icon and clay rule in `#B85C38`. Role headline in `#1C4636`.

`[Design note]` Slide 9 gets one extra visual signal — a thin clay border on the left edge,
8 px — because the facilities manager is the punchline of the whole carousel and it should feel
slightly different without breaking the system.

---

### Slide 10 — The takeaway and CTA

- **Eyebrow:** THE TEST
- **Title:** `COULD SOMEONE WHO HAS NEVER MET YOU USE THIS MODEL?`
- **Text:** If the answer is no, it is not a BIM model. It is a personal drawing aid that
  happens to be three-dimensional.
  Build for the seventh person, not the first.
- **Visual:** The seven circles from slide 2, now all filled clay, connected by a single clean
  line — the visual resolution of the problem posed at the start.
- **Icons:** None.
- **Layout:** Headline top, 4 lines maximum. Diagram centre. CTA block bottom:
  "Vollmann Akarakiri — BIM Specialist, Autodesk Revit, Architectural Designer.
  Follow for 52 weeks of BIM from first principles."
- **Colour:** **Dark scheme.**

---
---

# CAROUSEL 02 — Fifty Years of BIM

**Week 4** · **Category:** BIM Basics · **KB:** L1.03 · **8 slides**
**Objective:** dismantle "BIM is a trend" with a timeline.

---

### Slide 1 — Hook

- **Eyebrow:** BIM BASICS · 02
- **Title:** `BIM IS OLDER THAN MOST OF THE PEOPLE DOING IT`
- **Text:** The idea was published in 1975.
- **Visual:** A single vertical clay line running the full height of the slide, 4 px, positioned
  at the 20% mark — the timeline spine that will appear on every subsequent slide.
- **Icons:** None.
- **Layout:** Text right of the spine. Large negative space above.
- **Colour:** **Dark scheme.**

---

### Slides 2–7 — The timeline

**Shared layout:** the clay timeline spine stays at the 20% mark on every slide. A clay dot
(24 px) marks the year. The year is set in Bebas Neue 140 px. Content sits to the right of the
spine.

| # | Year | Headline | Text | Visual |
|---|---|---|---|---|
| 2 | `1975` | `THE IDEA` | Charles Eastman describes the Building Description System: parametric design and computable 3D representations from a single integrated database for visual and quantitative analysis. That is BIM, fifty years ago. | Line illustration of a punched card / early terminal, 160 px, muted |
| 3 | `1986` | `THE ARGUMENT` | Robert Aish documents the term "Building Modelling" in a published paper, arguing for both the concept and the technology to deliver it. | Icon: `file-text` |
| 4 | `1992` | `THE NAME` | van Nederveen and Tolman publish the first documented use of "Building Information Model" in Automation in Construction. They describe aspect models from different participants combining into one reference model. That is federation. | Diagram: three small squares merging into one outlined square |
| 5 | `1997–2002` | `THE SOFTWARE` | Charles River Software is founded, becomes Revit Technology Corporation in 2000, and is acquired by Autodesk in 2002. | Icon: `box` |
| 6 | `2011–2016` | `THE MANDATE` | The UK Government Construction Strategy states government will require fully collaborative 3D BIM as a minimum by 2016. An industry gets a shared ladder and a deadline. | Icon: `landmark` or `flag` |
| 7 | `2018–2025` | `THE STANDARD` | ISO 19650-1 and -2 published 2018. Part 5, security, 2020. Part 6, health and safety information, 2025. Information management goes international. | Icon: `globe` with `book-open` |

**Colour for 2–7:** Cream scheme. Year in `#B85C38`. Headline in `#1C4636`.

`[Accuracy note]` Slide 5 uses only the corporate timeline, **not** the acquisition figure.
That figure comes from secondary sources — see `../research/01-verification-log.md`.

---

### Slide 8 — Takeaway and CTA

- **Eyebrow:** THE POINT
- **Title:** `IT DID NOT FAIL FOR DECADES BECAUSE IT WAS WRONG`
- **Text:** It waited for computing power, for interoperability standards, and for enough
  commercial pain to make the change worth making.
  All three arrived. That is why this is happening now.
- **Visual:** The full timeline compressed — the clay spine running horizontally across the
  slide with all six dots marked and years labelled small beneath.
- **Layout:** Headline top. Compressed timeline centre. CTA bottom.
- **Colour:** **Dark scheme.**

---
---

# CAROUSEL 03 — The BIM Dimensions Nobody Agrees On

**Week 10** · **Category:** BIM Workflow · **KB:** L2.02 `[CONTESTED]` · **10 slides**
**Objective:** the flagship credibility carousel. Almost no other content states the disagreement.

---

### Slide 1 — Hook

- **Eyebrow:** BIM WORKFLOW · 03
- **Title:** `THE INDUSTRY DOES NOT AGREE ON WHAT 6D AND 7D BIM MEAN`
- **Text:** Almost every article states it confidently. They contradict each other.
- **Visual:** Two clay arrows pointing in opposite directions from a single point, with question
  marks at each end. Simple, 2 px stroke, 400 px wide.
- **Layout:** Diagram above headline. Headline 4 lines maximum.
- **Colour:** **Dark scheme.**

---

### Slide 2 — What is agreed

- **Eyebrow:** AGREED
- **Title:** `3D · 4D · 5D`
- **Text:** These three are broadly settled across the industry. Everything above them is where
  it breaks down.
- **Visual:** Three stacked clay-outlined bars of increasing width, labelled 3D, 4D, 5D — the
  start of a ladder that will visibly fracture on slide 6.
- **Layout:** Text top third, bars centred.
- **Colour:** Cream scheme.

---

### Slides 3, 4, 5 — The agreed dimensions

**Shared layout:** large Bebas dimension number top-left (140 px, clay), headline beside it,
body below, icon bottom-right at 120 px.

| # | Dimension | Headline | Text | Icon |
|---|---|---|---|---|
| 3 | `3D` | `GEOMETRY` | The coordinated model. Elements that know what they are, positioned in space, checkable against each other. | `box` |
| 4 | `4D` | `TIME` | Model elements linked to a construction programme. You watch the sequence instead of reading it — and you find the conflicts that are about time, not space. | `clock` |
| 5 | `5D` | `COST` | Quantities and cost data linked to elements. Note: NBS records the argument that cost is not really a dimension at all, but an additional information field. | `calculator` |

**Colour:** Cream scheme.

---

### Slide 6 — The fracture

- **Eyebrow:** NOT AGREED
- **Title:** `THEN IT SPLITS`
- **Text:** Both of these positions are published. Both appear in real tender documents. There
  is no international consensus.
- **Visual:** **The key graphic of the carousel.** The ladder from slide 2 continues, then
  forks into two diverging branches:

```
        ┌────────────────────────────┐
        │   6D  Facility management  │
   ─────┤   7D  Sustainability       │   ← Position A
   5D   │                            │
   ─────┤   6D  Sustainability       │   ← Position B
        │   7D  Facility management  │
        └────────────────────────────┘
```

  Both branches drawn at equal weight in clay — neither is presented as correct.
- **Layout:** Headline top. Fork diagram occupying the lower two thirds.
- **Colour:** Cream scheme. This is the one slide where clay may exceed 10%, because the fork
  is the message.

---

### Slide 7 — It goes further

- **Eyebrow:** ALSO NOT STANDARDISED
- **Title:** `8D. 9D. 10D. 11D.`
- **Text:** You will find all of these confidently explained online. None of them are formalised
  or standardised. NBS records that there is little international consensus beyond 5D.
- **Visual:** Four ghosted, dashed-outline boxes labelled 8D–11D, at 30% opacity — visually
  present but visibly insubstantial.
- **Icons:** `alert-circle`, clay, 64 px, top-right.
- **Colour:** Cream scheme.

---

### Slide 8 — What to do about it

- **Eyebrow:** IN PRACTICE
- **Title:** `ASK BEFORE YOU PRICE IT`
- **Text:** When a tender asks for 6D BIM, do not guess and do not quietly assume.
  Ask: "Please confirm what is required under 6D — asset information for operations, or
  sustainability and carbon data. The scope and cost differ substantially."
- **Visual:** A message-bubble outline in clay containing the quoted question, set in Inter
  30 px. Treating it as a quotable script makes the slide screenshot-worthy on its own.
- **Icons:** `message-square`
- **Colour:** Cream scheme.

---

### Slide 9 — The professional position

- **Eyebrow:** THE RULE
- **Title:** `SPECIFY THE INFORMATION, NOT THE DIMENSION`
- **Text:**
  Write: "Provide asset data in accordance with the AIR at handover."
  Not: "Provide 6D BIM."
  One is deliverable and auditable. The other is an argument waiting to happen.
- **Visual:** Two-row comparison. Top row with a clay `check-circle`, bottom row with a muted
  `x-circle`. Hairline rule between.
- **Colour:** Cream scheme.

---

### Slide 10 — CTA

- **Eyebrow:** —
- **Title:** `DIMENSIONS EXPLAIN BIM. THEY DO NOT SPECIFY IT.`
- **Text:** Useful for teaching someone new. Poor for writing a contract.
  Sources: NBS, BIM dimensions explained · Designing Buildings, BIM dimensions
- **Visual:** None — text and lockup only.
- **Layout:** Headline centred. Sources line in Inter 20 px muted. CTA block bottom.
- **Colour:** **Dark scheme.**

`[Design note]` This is the only carousel that puts sources on the final slide rather than only
in the caption. On a contested topic the citation is part of the argument, and it belongs where
someone screenshotting the carousel will still see it.

---
---

## Specification template for the remaining 15 carousels

Weeks 11, 12, 14, 16, 21, 27, 29, 34, 37, 41, 43, 45, 46, 49, 51.

```
# CAROUSEL [n] — [Title]
**Week [n]** · **Category:** [pillar] · **KB:** [ref] · **[n] slides**
**Objective:** [what the reader can do afterwards that they could not before]

### Slide 1 — Hook
- Eyebrow / Title / Text / Visual / Icons / Layout / Colour: DARK

### Slide 2 — Problem or setup
- ... Colour: CREAM

### Slides 3 to N-2 — One idea each
- ... Colour: CREAM

### Slide N-1 — Practical takeaway
- ... Colour: CREAM

### Slide N — CTA
- ... Colour: DARK
```

**Checklist before building any carousel:**

- [ ] Objective stated as a capability, not a topic
- [ ] Slide 1 makes a promise the last slide keeps
- [ ] One idea per slide — no slide has two headline-weight elements
- [ ] Under 45 words per slide
- [ ] Readable with no caption and no voiceover
- [ ] Repeating slides share an identical layout (rhythm beats variety)
- [ ] At least one slide is independently screenshot-worthy
- [ ] Sources named in the caption, and on-slide for contested topics
- [ ] Slides 1 and N are dark; everything between is cream
- [ ] Clay under 10% except where the diagram is the message
- [ ] Zero emoji
