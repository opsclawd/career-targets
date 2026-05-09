# Weekly Review — 2026-05-09

Agent: career-targets weekly review
Review period: 2026-05-03 to 2026-05-09

---

## Registry Status

| Metric | Start (May 2) | End (May 9) | Change |
|---|---|---|---|
| Companies in registry | 120 | 120 | — |
| Active | ~117 | ~117 | — |
| Watchlist | 2 | 2 | — |
| Rejected | 6 | 6 | — |
| Jobs in registry | ~153 | ~156 | +3 |

Registry growth has plateaued. Sourcing runs Apr 30 – May 8 found only 3 net-new job entries. This is consistent with the saturation signal noted in the May 2 review.

---

## New Jobs (Since May 2 Review)

| Job | Company | Source | Notes |
|---|---|---|---|
| Software Development Engineer (GPU Primitives Libraries) | AMD Canada | eluta.ca | Calgary AB; posted May 8 |
| Co-op Fall 2026 - Software Engineering Developer (16 months) | General Dynamics Mission Systems-Canada | eluta.ca | Calgary AB; posted May 7 |
| Full Stack Developer – Product Engineering | Showpass | eluta.ca | Calgary AB; duplicate — already in registry from May 4 |

**Net-new this week: 1** (AMD GPU Primitives — the GD co-op and Showpass were already tracked).

---

## Careers Pages Reviewed

### Pages with Issues

| Company | Status | Issue |
|---|---|---|
| BigGeo | stale | careers page at biggeo.com/careers returned 404 on Apr 16; company still active via Vivid Theory brand on eluta.ca |
| Helcim Inc. | blocked | careers page Cloudflare-blocked; jobs found via eluta.ca only |
| GeoSoftware | needs confirmation | last checked Apr 19; no update since |
| TerraSense Analytics | needs confirmation | last checked Apr 19; no update since |

### Pages Verified Active This Week

- **Showpass** — confirmed via careers page and eluta.ca
- **North Vector Dynamics** — confirmed via Ashby board
- **RigUp** — confirmed active; node.js/Python/Kotlin/React/TypeScript/Kafka/K8s stack; Calgary team
- **Connect First Credit Union** — confirmed via eluta.ca
- **Luxoft** — confirmed via eluta.ca (2 roles: Subsurface Backend Dev, Senior Java Dev)
- **CGI Inc.** — confirmed via eluta.ca (Senior Mobile Developer Android)
- **AMD** — confirmed via eluta.ca (GPU Primitives Libraries role, May 8)

---

## Watchlist Review

### Blackline Safety Corp.
- Last seen: Manufacturing SWE role on eluta.ca (Apr 11)
- LinkedIn search this week found no active SWE roles; only Regional Sales Manager US West
- **Action:** Keep on watchlist another week; if still no SWE confirmation by May 16, move to rejected

### Amplifier Health
- Last checked: Apr 23; confirmed Calgary HQ for voice AI healthcare company
- SWE roles not yet confirmed
- **Action:** Keep on watchlist; no further action until more evidence

### Newly Identified Watchlist Candidates
None this week — no new companies with uncertain SWE status found.

---

## Rejected Review

No changes to rejected list this week. MobSquad, Symend, Village Trust, Occupational Health, and Granite Solutions remain rejected.

---

## Seed List Candidates (Unresolved)

From the May 2 recommended actions:
- Suncor Energy — not yet in registry; Calgary energy giant
- Shell Calgary — not yet in registry; Calgary office
- Jane Software — Calgary project management SaaS
- Arc'teryx tech — not yet in registry
- Cenovus Energy — in registry as of Apr 18 but status unclear; needs confirmation
- Enbridge — in registry since Apr 18; confirmed active on eluta.ca this week (Technical Lead Full Stack Developer)
- Clio — in registry since Apr 17; confirmed active (Senior Developer Enterprise AI on eluta.ca, May 5)

**Recommendation:** Add Suncor Energy and Jane Software to companies_seed.csv this week.

---

## Jobs Registry Noise Patterns

No new noise patterns detected. Deduplication is working correctly — Showpass duplicate was caught (May 9 listing vs. May 4 listing).

**Known data quality issue (unresolved):**
- Capco careers_url in registry points to morganstanley.com instead of capco.com/careers. Should be corrected in next daily run.

---

## Notes Updates

### Registry Saturation
Registry is approaching ceiling for current search-based methods. Last 3 weeks of daily runs returned 0–2 net-new jobs. The highest-value remaining sources are:
1. eluta.ca — best quality, most reliable
2. LinkedIn job search — bot-blocked most days
3. Built In Calgary — good for company discovery, limited for job extraction

### Browser Automation Still the Biggest Gap
JS-rendered boards (Workday, iCIMS, custom) constitute ~80% of known ATS boards. No progress this week on Playwright extraction.

---

## Recommended Actions for Week 5

**High Priority:**
1. **Add Suncor Energy and Jane Software to companies_seed.csv**
2. **Confirm Cenovus Energy careers page** — in registry since Apr 18 but never confirmed active with SWE roles
3. **Re-check Blackline Safety Corp.** — if no SWE by May 16, reject
4. **Fix Capco careers_url** — should be capco.com/careers not morganstanley.com/careers

**Medium Priority:**
5. **Browser automation for Workday boards** — still the single biggest unlock; RBC, ATB Financial, TELUS, Keyera remain inaccessible
6. **Verify GeoSoftware and TerraSense** — both last checked Apr 19; confirm still active
7. **Enbridge job confirmation** — Technical Lead Full Stack Developer appeared on eluta.ca May 8; confirm matches registry entry

**Low Priority:**
8. **Closed-job detection workflow** — no systematic way to catch stale roles
9. **eluta.ca cadence review** — daily runs finding 0–1 jobs; consider whether daily frequency is still warranted

---

## Summary

- **Companies tracked:** 120 (active ~117, watchlist 2, rejected 6)
- **Jobs tracked:** ~156 (+3 since May 2, but only 1 net-new after dedup)
- **Careers pages flagged:** BigGeo (404 stale), Helcim (Cloudflare blocked), GeoSoftware/TerraSense (need re-check)
- **Watchlist status:** Blackline Safety Corp. pending confirmation; Amplifier Health stable
- **Seed list recommended additions:** Suncor Energy, Jane Software
- **Biggest gap:** Registry saturation + JS-rendered ATS still require browser automation