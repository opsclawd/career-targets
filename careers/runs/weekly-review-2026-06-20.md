# Weekly Review — 2026-06-20

## Tasks Completed

1. Reviewed `careers_registry.csv` — removed blank line data quality issues
2. Reviewed `jobs_registry.csv` — marked stale RBC Feb roles closed; confirmed Vista Projects ETL noise
3. Updated `watchlist.md`, `rejected.md`, and `notes.md` as needed
4. Wrote this run summary

---

## Careers Registry Changes

### Data Quality Fix
- **Removed 6 blank lines** from `careers_registry.csv` — empty rows were causing awk parsing errors. File reduced from 156 to 150 lines (1 header + 149 company entries).

### Registry Status
- **149 companies** total (down from 156 after blank line removal)
- **~131 active**, **~18 rejected** (unchanged counts after fix)

---

## Jobs Registry Changes

### RBC Stale Roles Confirmed Closed
RBC Senior Software Developer (R-0000154331) fetched and returned HTTP 410 — **job is filled/closed**. All three Feb 2026 RBC roles confirmed closed:
- RBC Senior Software Developer (2026-02-03) — closed (was existing)
- RBC Lead ML Platform Engineer (2026-02-26) — closed (was existing)
- RBC Staff AI Engineer (2026-02-25) — closed (was existing)

### Noise Entry Corrected
- **Vista Projects Limited ETL Application Specialist** — ETL/data specialist role, not SWE. Marked closed (was new).

---

## Watchlist Status

**Current watchlist: 0 companies** (unchanged from Jun 13).

---

## Seed File Status

`companies_seed.csv` contains 12 seed entries from early April. Most are already in `careers_registry.csv` (Benevity, ATB Financial, RBC, TD, Shopify, etc.) or rejected. The seed file is serving its purpose as a source of truth. No changes needed this week.

---

## Outreach State Summary

All outreach state files remain empty or near-empty:
- `leads.csv` — 0 leads
- `threads.csv` — 0 active threads
- `approvals.csv` — 0 pending
- `suppression.csv` — 0 entries
- `activity.jsonl` — 15 log entries; all queue checks return empty

The outreach pipeline has been inactive since Jun 16. No new leads or replies have been generated this week.

---

## Notable Observations

- **Jun 20 run added 3Play Media** — video accessibility SaaS with Calgary office; Ruby/Rails, React, Python, K8s stack. Added to registry; no active SWE board but pipeline candidate.
- **Registry cleanup done** — 6 blank lines removed; 3 RBC Feb jobs confirmed closed via HTTP 410.
- **Vista Projects noise resolved** — ETL Application Specialist is not a SWE role; marked closed.
- **Outreach pipeline stalled** — no leads in pipeline since Jun 16. The career-targets system is running sourcing daily but nothing is flowing into outreach queues.

---

*Previous weekly review: 2026-06-13*
