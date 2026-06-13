# Weekly Review — 2026-06-13

## Tasks Completed

1. Reviewed `careers_registry.csv` — 2 stale/active companies flagged for rejection
2. Reviewed `jobs_registry.csv` — 4 non-SWE NDAX noise entries marked closed
3. Updated `watchlist.md`, `rejected.md`, and `notes.md` as needed
4. Wrote this run summary

---

## Careers Registry Changes

### Rejected This Week

- **BigGeo** → `rejected` (was `stale`)
  - Careers page (biggeo.com/careers) 404 since Apr 16 — 7+ weeks.
  - Company active via Vivid Theory brand (already in registry separately).
  - No ATS found; Vivid Theory entry covers their Calgary SWE roles.

- **North Vector Dynamics** → `rejected` (was `active`)
  - Ashby board (jobs.ashbyhq.com/northvectordynamics) never returned parseable content across multiple checks since May 5.
  - SWE roles never confirmed despite repeated attempts.
  - No ATS alternative found.

### New Companies Added from Seed

- **Suncor Energy** — Calgary energy giant; added from seed (was in companies_seed.csv since May 30, not yet in registry)
- **Shell Canada (Calgary)** — Major O&G company with Calgary office; added from seed
- **Jane Software** — Calgary project management SaaS; added from seed

---

## Jobs Registry Changes

### Noise Entries Marked Closed

- NDAX Head of Product Management — non-SWE role
- NDAX Compliance Associate — non-SWE role
- NDAX Corporate Legal Counsel — non-SWE role
- NDAX Trader - Market Making Specialist — non-SWE role

(Enverus Sales Development Representative was already marked closed in a prior run.)

---

## Watchlist Status

**Current watchlist: 0 companies** (unchanged).

---

## Seed File Cleanup

Removed Suncor Energy, Shell Canada (Calgary), and Jane Software from `companies_seed.csv` — all three are now in `careers_registry.csv`.

---

## Notable Observations

- **Registry growth:** 3 net-new companies added this week (Suncor, Shell, Jane) — first new entries since Jun 8.
- **Noise management:** 4 NDAX non-SWE roles (Product, Compliance, Legal, Trading) corrected from `new` to `closed`. These had been sitting in jobs_registry since Apr 21.
- **North Vector Dynamics persistent failure:** Ashby board has been non-functional since first check May 5; rejection is overdue.
- **BigGeo stale carryover:** 404 on careers page since Apr 16 (nearly 8 weeks); rejection is overdue.
- **Seed pipeline gap:** Suncor, Shell, and Jane were flagged as seed candidates on May 30 but never added to registry until now. This is the first time a seed candidate took 2+ weeks to be promoted.

---

*Previous weekly review: 2026-06-06*
