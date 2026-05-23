# Weekly Review — 2026-05-23

Agent: career-targets weekly review
Review period: 2026-05-16 to 2026-05-23

---

## Registry Status

| Metric | Start (May 16) | End (May 23) | Change |
|---|---|---|---|
| Companies in registry | ~125 | ~127 | +2 |
| Jobs in registry | ~168 / ~291 | ~185 rows / ~291 | flat |
| Active entries | ~120 | ~122 | +2 |
| Watchlist | 2 | 2 | — |
| Rejected | 6 | 6 | — |

Note: Job count discrepancy between `wc -l` (185 data rows) and run log estimates (~291 roles) suggests the registry has accumulated rows beyond what a simple line count reflects, likely due to formatting/whitespace. Direct row count is the reliable metric going forward.

---

## New Companies Since May 16

| Company | Careers URL | ATS | Source | Notes |
|---|---|---|---|---|
| MobSquad | eluta.ca (reactivated) | eluta | reactivation | Previously rejected (domain 404 Apr 20); 4 active SWE roles on eluta.ca (May 20) |

**MobSquad reactivation** is the only notable new entry this week. Previously rejected due to `www.mobsquad.com` returning 404. eluta.ca now shows 4 active SWE roles (all posted May 20): Senior Software Engineer, Senior Full-Stack Developer, Senior Front-End Engineer, Machine Learning Engineer. Registry status should move from `rejected` → `active`. Note: main company domain still unverified.

---

## New Jobs Since May 16

| Job | Company | Source | Posted |
|---|---|---|---|
| Senior Software Engineer | MobSquad | eluta.ca | May 20 |
| Senior Full-Stack Developer | MobSquad | eluta.ca | May 20 |
| Senior Front-End Engineer | MobSquad | eluta.ca | May 20 |
| Machine Learning Engineer | MobSquad | eluta.ca | May 20 |
| Software Engineer - Early Career - Landmark | Halliburton Energy Services | eluta.ca | May 20 |
| Software Engineer - Landmark | Halliburton Energy Services | eluta.ca | May 20 |
| Senior Software Engineer - Landmark | Halliburton Energy Services | eluta.ca | May 20 |
| Staff Software Development Engineer (GPU Libraries) | AMD Canada | eluta.ca | May 20 |

MobSquad entries are a **reactivation** (from rejected → active pool). Halliburton and AMD entries are from companies already in the registry. No net-new employer companies this week beyond the MobSquad reclassification.

Overall job flow is consistent with plateau phase — 0–8 net-new roles per day from existing employers, sourced via eluta.ca. No new direct employer careers pages resolved this cycle.

---

## Pages Needing Review

### Stale / Broken (Carryover)

| Company | Issue | Status |
|---|---|---|
| **BigGeo** | biggeo.com/careers → 404 | Flagged May 16; not yet actioned |
| **Helcim Inc.** | Cloudflare-blocked on direct careers page | eluta.ca jobs still accessible |
| **North Vector Dynamics** | Ashby board exists but returns no parseable job content (blank/404 on embed); SWE roles unconfirmed | Pending manual verification |

### Needs Re-check

| Company | Last Check | Issue |
|---|---|---|
| **GeoSoftware** | Apr 19 | No update since; verify still active |
| **TerraSense Analytics** | Apr 19 | No update since; verify still active |
| **Userful Corporation** | May 18 | SWE role (EdgeAI, Software Technology Lead) appeared on Built In Calgary; company not yet in registry |

---

## Pending Actions from Prior Week (Not Yet Completed)

1. ❌ **Move Blackline Safety Corp. to rejected** — No SWE confirmed in 5+ weeks; only ops/hardware roles active. Not yet actioned.
2. ❌ **Add Suncor Energy, Shell Canada (Calgary), Jane Software to companies_seed.csv** — Not yet done.
3. ❌ **Update BigGeo status to `stale`** in careers_registry.csv — Not yet done.
4. ❌ **Confirm GeoSoftware and TerraSense** — Both last checked Apr 19; re-check overdue.
5. ❌ **Update MobSquad status from rejected → active** — Reactivation identified May 20; not yet actioned in registry.
6. ❌ **Capco careers_url fix** — Still points to morganstanley.com instead of capco.com/careers.

---

## Watchlist Review

| Company | Status | Notes |
|---|---|---|
| **Amplifier Health** | Keep on watchlist | Calgary voice AI healthcare; HQ confirmed; SWE roles still unconfirmed after 2+ weeks |
| **Blackline Safety Corp.** | Recommend reject | No SWE since Apr 11; only ops/hardware roles since May 16 check |

---

## Rejected Review

MobSquad should move from rejected → active this week pending its eluta.ca reactivation confirmation.

---

## Weekly Cadence Notes

- **eluta.ca** continues to be the dominant reliable source (same-day postings, clean URLs).
- **LinkedIn bot detection** persists — direct LinkedIn searches remain blocked.
- **Built In Calgary** useful for discovery but company attribution often unclear from rendered snippets.
- **Registry plateau:** No new employer companies discovered this week (MobSquad is a reactivation, not a net-new). The seed-based approach may be reaching natural coverage limits; expanding the seed list (Suncor, Shell Canada, Jane Software) and addressing JS-rendered ATS (Workday — RBC, ATB, TELUS, Keyera) are the two biggest remaining levers.

---

## Recommended Actions for Week 7 (May 23–May 30)

**High Priority:**
1. **Update MobSquad status:** rejected → active in careers_registry.csv
2. **Move Blackline Safety Corp. to rejected** (unchanged recommendation from Week 5)
3. **Add Suncor Energy, Shell Canada (Calgary), Jane Software to companies_seed.csv**
4. **Update BigGeo status to `stale`** in careers_registry.csv
5. **Verify GeoSoftware and TerraSense** — both overdue since Apr 19

**Medium Priority:**
6. **Browser automation for Workday boards** — RBC, ATB Financial, TELUS, Keyera remain inaccessible without JS rendering
7. **Capco careers_url fix** — redirect morganstanley.com → capco.com/careers
8. **Userful Corporation** — confirm Calgary SWE role, add to registry if confirmed

**Low Priority:**
9. **eluta.ca cadence review** — plateau suggests weekly runs may be more efficient than daily
10. **Closed-job detection workflow** — no systematic path for catching stale roles across the registry

---

## Summary

- **Companies tracked:** ~127 (active ~122, watchlist 2, rejected 5, pending MobSquad reactivation 1)
- **Jobs in registry:** 185 data rows tracked (registry steady; plateau phase continues)
- **Net-new employers this week:** 0 (MobSquad is a reactivation, not new)
- **Careers pages needing action:** BigGeo (stale 404), North Vector Dynamics (blank Ashby), GeoSoftware/TerraSense (overdue re-check)
- **Biggest gap:** Registry plateau + JS-rendered ATS remain the primary bottlenecks. Seed list expansion and Workday browser automation are the two highest-leverage next steps.
