# Weekly Review — 2026-10-03

## Registry Status

- **220 companies** in careers_registry (up from ~216 last week — Clio, Slalom Consulting, Syndio, Synechron added)
- **~479 jobs** in jobs_registry (up from ~465 last week)
- **Seed file:** Empty (clean)
- **Watchlist:** 0 companies
- **Rejected:** 7 companies (unchanged)

---

## Action Items from Last Week — Status Unchanged

### 3 Stale Careers Pages — Still Unresolved

All three were flagged Sep 12 and remain broken as of this review:

**Viridien** (`viridien.com/en`) — Still 404
- Careers URL inaccessible; Built In Calgary is the only known source
- Status: `active` in registry via Built In Calgary discovery
- **Recommendation:** Update careers_url to Built In Calgary link or mark `stale`

**Orion Steel Group LLC** (`orionsteels.com`) — Still down
- Connection failure confirmed Aug 6; only accessible via eluta ATS
- Status: `active` in registry via eluta only
- **Recommendation:** Mark `stale` since direct careers page is unresolvable

**Steel Reef Infrastructure Corp.** (`steelreef.com`) — Still inaccessible
- DNS/connection failure confirmed Aug 16; only eluta ATS confirmed
- Status: `active` in registry via eluta only
- **Recommendation:** Mark `stale` or find alternative direct URL

---

## Notable Developments Since Sep 26

### Net-New Companies Added This Week

- **Clio** — re-confirmed via Oct 2 eluta sweep; Staff Software Developer ($176K-$264K)
- **Slalom Consulting ULC** — Software Architect AI Accelerated Engineering Lead (eluta, Oct 1)
- **Syndio** — 3 Staff SWE roles (LinkedIn, Sep 26–29)
- **Synechron** — 2 Java backend SWE roles (Built In Calgary, Sep 29)
- **Canada West Land Services Ltd.** — Senior Full Stack Developer (eluta, Oct 2)
- **Halliburton Energy Services Inc.** — Software Developer Subsurface Applications (eluta, Oct 2)
- **RBC** — Software Developer Metadata (eluta, Oct 2)

### Clio Re-entry
Clio reappeared in the registry Oct 2 with a Staff Software Developer role on eluta at $176K-$264K. Clio is a major Canadian legal SaaS company (Vancouver HQ, Calgary office). Previously tracked in registry earlier in 2026.

### Registry Structural Issue — 65 eluta.ca URLs as Canonical careers_url
The AGENTS.md rule states: "Never use LinkedIn, Indeed, Eluta, Job Bank, or aggregator links as canonical careers pages." However, 65 of ~220 registry entries currently have `eluta.ca` as their `careers_url`. For many of these companies, eluta.ca is the only confirmed live job board — no direct employer ATS page has been found. This is a known limitation, not a deliberate violation. **Recommend a future cleanup pass** to systematically attempt ATS discovery for the top hiring companies among these 65, starting with high-signal employers.

### Oct 3 Run — Zero New Finds
Oct 3 daily run found no net-new SWE roles or companies. Market appears seasonally quiet post-Thanksgiving (Canada). Built In Calgary dominated by non-SWE listings. eluta sweeps returning thin results.

---

## This Week's Net-New Jobs (Oct 1–2 sweeps)

| Company | Title | Source | Date |
|---------|-------|--------|------|
| Slalom Consulting ULC | Software Architect - AI Accelerated Engineering Lead | eluta | Oct 1 |
| Canada West Land Services Ltd. | Senior Full Stack Developer | eluta | Oct 2 |
| Halliburton Energy Services Inc. | Software Developer, Subsurface Applications (Assoc-Sr) Landmark | eluta | Oct 2 |
| RBC | Software Developer Metadata | eluta | Oct 2 |
| Syndio | Staff Software Engineer, Integrations (Calgary) | LinkedIn | Sep 29 |
| Syndio | Staff Software Engineer, Essentials (Calgary) | LinkedIn | Sep 29 |
| Synechron | Java Software Engineer | Built In Calgary | Sep 29 |
| Synechron | Senior Java Software Engineer | Built In Calgary | Sep 29 |
| MNP LLP | Full Stack Software Engineer | eluta | Oct 2 |
| MNP LLP | Senior Back-End Developer | eluta | Oct 2 |
| MNP LLP | Senior Test Automation Developer | eluta | Oct 2 |
| MNP LLP | Intermediate Full Stack Developer | eluta | Oct 2 |
| Garmin Canada | Embedded Software Engineer | eluta | Oct 2 |
| Athennian | Software Engineer ($90K-$130K) | eluta | Oct 2 |

**Total net-new jobs this period: ~14** (from 9 companies; 0 new employers beyond prior-week additions)

---

## Pages / Roles Flagged for Follow-up

- **Cloudbeds** — Greenhouse board confirmed but careers_url currently points to `cloudbeds.com/careers` (custom); verify Greenhouse board URL as canonical
- **Viridien** — main careers page still 404; needs Built In Calgary URL or `stale` marking
- **Orion Steel Group LLC** — careers page unresolvable; eluta only; recommend `stale` status
- **Steel Reef Infrastructure Corp.** — DNS issue persists; eluta only; recommend `stale` status
- **The Mustard Seed** — Senior Web Developer (nonprofit, not a software company; excluded from pipeline)

---

## Seed List

No pending seed candidates this week. Seed file is empty.

---

## Watchlist

**Current watchlist: 0 companies** (unchanged).

---

## Summary

- **0 new employers added** this week (net-new companies were re-entries from prior registry)
- **~14 net-new SWE-relevant jobs** from 9 companies (Oct 1–2)
- **3 stale careers pages unchanged** (Viridien 404, Orion Steel down, Steel Reef DNS issue) — still unresolved since Sep 12
- **65 eluta.ca URLs** in registry as canonical — structural issue flagged for future cleanup
- **Market appears seasonally quiet** — zero new finds Oct 3; thin eluta sweep results
- **Outreach state files** — no outreach/ directory exists in this repo; nothing to update

---

*Previous weekly review: 2026-09-26*
