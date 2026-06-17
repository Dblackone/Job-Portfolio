# Content Operations Workflow

How the hub runs day to day, how the repo and Notion fit together, and how to take
"orders".

---

## Repo ↔ Notion split

- **Repo (source of truth for craft):** brand guide, platform specs, pillars,
  templates, the graphics engine, generated graphics, and written post packages.
  Everything version-controlled and reproducible.
- **Notion (live ops board):** the *queue*. One row per scheduled post with: Date,
  Pillar, Platform(s), Status, Hook, Caption, Asset link, Graphic link. Drag through
  statuses: `Idea → Drafted → Graphic ready → Scheduled → Posted`.

The Notion DB schema and a 30-day seed are created by the hub (see
`calendar/` for the same data in markdown). Keep them in sync: the markdown calendar
is the durable record; Notion is the working board.

---

## Daily loop

1. **Open today's row** (Notion) / today's file (`posts/`).
2. Confirm the **source asset** exists (`assets/Project Pictures/...`) — view it.
3. Caption + script are pre-written; **proofread**, adjust for anything timely.
4. **Graphic**: pull from `graphics/output/` or rebuild via the engine.
5. **Post** per `brand/platform-specs.md`; mark row `Posted`.
6. **Engage back** for 30–60 min after posting (reply to every comment fast — this is
   the single biggest free engagement lever).

---

## Weekly loop (≈30 min, Sundays)

- Review last week's top performer; note *why* it worked.
- Refill the next 7 days in `posts/` from the pillar idea bank.
- Rebuild any new graphics. Re-sync Notion.

---

## Handling "orders"

An **order** = a specific, client- or campaign-driven piece (e.g. "promote the
Hillside project this Friday", "we need a hiring post", "announce a service").

1. Drop the order onto its target **date** in the calendar; mark `Pillar = Order`.
2. The pillar post that *was* on that date shifts to the next open slot (don't lose
   it — the rotation is a queue, not a fixed grid).
3. Build it with the same templates + engine so it stays on-brand.
4. Orders still obey the **≤ ~1 hard-sell/week** rule unless explicitly a campaign.

---

## Quality gate (before anything posts)

- [ ] Hook stops the scroll in line 1.
- [ ] One clear idea; one clear CTA.
- [ ] No invented facts/numbers/clients (see voice guide hard rules).
- [ ] On-brand graphic (palette, Inter, kicker, footer attribution).
- [ ] Correct hashtag count for the platform.
- [ ] Alt text written; video has captions.
- [ ] Handles/links correct.
