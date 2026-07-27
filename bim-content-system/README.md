# BIM & Revit Content System

A research-backed content engine for **Vollmann Olamide Akarakiri** — BIM specialist, Autodesk Revit professional, and architectural designer — built to establish authority on LinkedIn and attract freelance, consulting, and training opportunities.

This system is **separate from the DOVA Futures corporate content hub** (`/content-hub`). That hub speaks as the company. This one speaks as the practitioner. See `BRAND.md` for how the two relate and which rules carry across.

---

## How this system works

```
Research  →  Knowledge Base  →  Strategy  →  Content  →  Verification
(sourced)    (leveled 1/2/3)    (52 weeks)   (5 platforms)  (before posting)
```

Every piece of content traces back to a knowledge-base entry, and every technical
claim in the knowledge base traces back to a source in the sources register.
**Nothing gets posted that cannot be traced.**

---

## Directory map

| Path | Phase | What it holds |
|---|---|---|
| `research/00-sources-register.md` | 1 | Every source consulted, what it supports, and its authority tier |
| `research/01-verification-log.md` | 13 | Claim-by-claim verification, flagged uncertainties, contested definitions |
| `knowledge-base/00-index-and-learning-paths.md` | 2 | Master index, difficulty levels, learning paths |
| `knowledge-base/level-1-foundations.md` | 2 | Beginner concepts |
| `knowledge-base/level-2-intermediate.md` | 2 | Standards, workflow, coordination |
| `knowledge-base/level-3-advanced.md` | 2 | ISO 19650 mechanics, openBIM, digital twins, automation |
| `knowledge-base/revit-and-bim.md` | 2 | Revit's exact relationship to BIM — can, cannot, misconceptions |
| `knowledge-base/glossary.md` | 2 | Plain-English definitions of every term used |
| `strategy/one-year-content-strategy.md` | 3 | 52-week sequenced curriculum |
| `strategy/seo-and-engagement.md` | 12 | Keywords, posting times, hashtag sets, engagement mechanics |
| `linkedin/posts-weeks-01-12.md` | 4, 12 | Fully written LinkedIn posts with full SEO metadata |
| `linkedin/carousels.md` | 5 | Slide-by-slide carousels with complete design specs |
| `instagram/carousels-adapted.md` | 6 | Instagram versions of every carousel |
| `whatsapp/status-series.md` | 7 | Status formats: tips, facts, myth-vs-fact, mini tutorials |
| `tiktok/scripts.md` | 8 | 30/60/90-second scripts with camera direction and B-roll |
| `revit-tutorials/00-index.md` | 9 | Full tutorial curriculum index (all 45 topics) |
| `revit-tutorials/*.md` | 9 | Written tutorials with objective, difficulty, steps, mistakes |
| `quick-tips/tip-bank.md` | 10 | 200 short-form educational posts across 10 formats |
| `BRAND.md` | 11 | Canvas sizes, type scale, colour, icons, layout rules for Canva/Figma |

---

## Working rules (non-negotiable)

1. **No invented facts.** If it is not in the sources register, it does not get stated as fact.
2. **No invented statistics.** No "BIM saves 30%" claims without a citation to the study.
3. **Standards vs opinion are labelled.** `[STANDARD]` = defined in a published standard. `[PRACTICE]` = common industry practice. `[OPINION]` = Vollmann's professional view.
4. **Contested terms are flagged, not smoothed over.** Where the industry disagrees (6D/7D BIM is the clearest case), the disagreement is the content.
5. **Plain English, technically correct.** Explain the term the first time it appears in any post.
6. **Consult the knowledge base first.** Before writing anything new, check what has already been said so the progression stays logical and nothing repeats.

---

## Quick start for a new post

1. Open `strategy/one-year-content-strategy.md`, find the current week.
2. Open the referenced knowledge-base entry and re-read it.
3. Check `research/01-verification-log.md` for any flags on that topic.
4. Draft using the structure in `linkedin/posts-weeks-01-12.md` (hook → explanation → example → takeaway → CTA → hashtags).
5. Build the graphic against `BRAND.md`.
6. Adapt to Instagram / WhatsApp / TikTok using the matching platform file.
