# Weekly Review — 2026-04-25

Agent: career-targets weekly review
Review period: 2026-04-19 to 2026-04-25

---

## Registry Growth

| Metric | Start (Apr 18) | End (Apr 25) | Change |
|---|---|---|---|
| Companies in registry | 73 | 88 | +15 |
| Jobs in registry | 81 | 108 | +27 |
| Active careers pages | 68 | ~78 | +10 |
| Needs review | 4 | 0 | -4 (resolved) |
| Rejected | 1 | 6 | +5 |

Registry expanded again this week (15 new companies, 27 new jobs) via eluta.ca, Built In Calgary, and LinkedIn discovery. All 4 previously "needs_review" companies resolved this week.

---

## Jobs Discovery by Day

| Date | New Jobs | Notable |
|---|---|---|
| 2026-04-19 | 10 | GeoSoftware, Halliburton, TerraSense, MobSquad, Blackline Safety |
| 2026-04-20 | 3 | ACT Energy, Pleasant Solutions, geoLOGIC |
| 2026-04-21 | 3 | BMO Financial Group, University of Calgary |
| 2026-04-22 | 2 | Lightspeed Commerce (Staff iOS Developer) |
| 2026-04-23 | 5 | iON United, Sparrow Connected, atVenu |
| 2026-04-24 | 0 | — |
| 2026-04-25 | 0 | Keyera (new company, no net-new jobs) |

---

## Resolved Needs_Review Companies

| Company | Previous Status | Action | Outcome |
|---|---|---|---|
| Symend | needs_review | rejected | Greenhouse board decommissioned; no ATS found; no SWE roles confirmed |
| Village Trust | needs_review | rejected | DNS failure 7+ days; company defunct or renamed |
| Occupational Health | needs_review | rejected | DNS failure; not a tech employer |
| MobSquad | needs_review | rejected | Domain defunct (all pages 404; copyright 2022); jobs from Apr 14 likely expired |
| NDAX | needs_review | active | Workable board confirmed; 8+ open roles; Great Place to Work Certified |
| Amplifier Health | needs_review | watchlist | Real Calgary AI company; HQ confirmed; SWE roles still unconfirmed |

---

## Watchlist Changes

### Added this week
- **Blackline Safety Corp.** — Had Manufacturing SWE (eluta.ca, Apr 11). LinkedIn this week shows only Regional Sales Manager (non-SWE). Moved to watchlist pending confirmation.
- **Amplifier Health** — Real Calgary voice AI healthcare company; HQ confirmed; SWE roles not confirmed.

---

## Top Hiring Companies (current)

| Company | Est. Jobs | ATS | Notes |
|---|---|---|---|
| Canonical | 8 | unknown | Remote-first; highest volume hirer |
| NDAX | 8+ | Workable | Crypto exchange; Great Place to Work; newly confirmed this week |
| RBC | 5 | Workday | JS-rendered; roles from Feb may be stale |
| Affirm | 4 | unknown | 3 backend SWE roles; aggressive Calgary expansion |
| MongoDB | 4 | unknown | Growing Calgary presence |
| Quorum Software | 4 | unknown | Energy SaaS; Calgary hybrid |
| AMD | 2 | iCIMS | Staff SDE + GPU; Calgary office |

---

## Rejected Companies This Week

- **Symend** — Greenhouse board decommissioned; no ATS; no SWE roles confirmed
- **Village Trust** — DNS failure; defunct or renamed
- **Occupational Health** — DNS failure; not a tech company
- **MobSquad** — Domain defunct (all pages 404, copyright 2022); 4 SWE jobs in registry now likely expired

---

## Notable Market Observations (Apr 19–25)

- **Registry approaching saturation** — Apr 24 and Apr 25 runs found 0 new jobs. Current sourcing methods (eluta.ca, LinkedIn, Built In Calgary) are covering most visible market.
- **Energy sector strongest signal** — O&G tech (GeoSoftware, Halliburton, ACT Energy, geoLOGIC, TerraSense, Quorum, Enverus) remains the most consistent SWE hiring sector in Calgary.
- **AI/ML emerging cluster** — Precision AI, TerraSense Analytics, Amplifier Health, BlueMarvel AI all show AI/ML signals. Still nascent but growing.
- **JS-rendered ATS gap persists** — ~80% of companies use Workday/iCIMS/custom boards. Static extraction impossible; browser automation (Playwright) is the only path to scalable extraction.
- **DuckDuckGo completely bot-blocked** — Multiple runs this week returned errors. Not viable as search source.

---

## Recommended Actions for Week 3

**High Priority:**
1. Browser automation for Workday boards (RBC, ATB Financial, TELUS, Keyera) — single biggest unlock
2. Re-check Blackline Safety Corp. and Amplifier Health (watchlist)
3. Close expired MobSquad jobs in jobs_registry (4 roles from Apr 14, domain now defunct)
4. Seed list expansion: Suncor Energy, Shell Calgary, Jane Software, Clio, Arc'teryx tech, Cenovus, Enbridge

**Medium Priority:**
5. Systematic ATS slug discovery for unknown-ATS companies
6. RBC job freshness check (roles from February likely stale)
7. Decide on Data Engineer inclusion (nearly as common as SWE in Calgary)

**Low Priority:**
8. Closed-job detection workflow
9. eluta.ca daily monitoring cadence evaluation

---

## Summary

- **Companies tracked:** 88 (active ~78, watchlist 2, rejected 6)
- **Jobs tracked:** 108
- **New companies this week:** 15
- **New jobs this week:** 27
- **needs_review resolved:** 6 (4 rejected, 1 active, 1 watchlist)
- **Top hirers:** Canonical (8), NDAX (8+), RBC (5), Affirm/MongoDB/Quorum (4 each)
- **Biggest win:** NDAX confirmed active with Workable board; MobSquad domain proven defunct
- **Biggest gap:** 0 new jobs found Apr 24–25 — registry approaching saturation for current methods; browser automation needed to unlock JS-rendered boards