# Weekly Review — 2026-09-19

## Registry Status

- **201 active companies** in careers_registry
- **441 jobs** in jobs_registry (442 lines including header)
- **30 closed entries** in jobs_registry
- **404 entries with `new` status** in jobs_registry (see Stale Jobs issue below)
- **Seed file:** Empty (clean)
- **Watchlist:** 0 companies
- **Rejected:** 7 companies (Symend removed this week — see below)

---

## Action Items Completed This Week

### Symend — Removed from Rejected

Symend was listed in rejected.md with a "REACTIVATED" note since Sep 12. The action item was to remove it from rejected. Done this week — Symend remains `active` in careers_registry via eluta ATS.

### Precision AI typo URLs — Already Fixed

The two `precisionai.ai.ai` (double-extension) job entries were closed in the Sep 12 weekly review. The single remaining Precision AI entry (`precisionai.ai/careers`) is still `new` and active. No action needed.

### Capco careers_url — Already Corrected

The `careers_url` field in jobs_registry for the Capco NodeJS/Java Developer entry shows `capco.com/careers` — the correct value. The `job_url` (Morgan Stanley domain) reflects LinkedIn's attribution at time of discovery and is not a data error. No action needed.

---

## Stale Careers Pages — 3 Companies

All three were flagged on Sep 12 and remain unresolved:

### Viridien — Still Stale
- **careers_url:** `viridien.com/en` (returns 404, even with /careers appended)
- **Status:** `active` in registry (via Built In Calgary / LinkedIn discovery)
- **Action needed:** Change careers_url to Built In Calgary link or mark `stale`; main careers page is inaccessible

### Orion Steel Group LLC — Still Stale
- **careers_url:** `orionsteels.com` — domain returns connection failure (confirmed Sep 19)
- **Status:** `active` in registry (jobs found via eluta only)
- **Action needed:** Find actual careers page URL or mark `stale`

### Steel Reef Infrastructure Corp. (SRIC) — Still Stale
- **careers_url:** `steelreef.com` — returns 403 Forbidden (confirmed Sep 19)
- **Status:** `active` in registry (jobs found via eluta only)
- **Action needed:** Use eluta ATS as primary URL or mark `stale`

---

## Stale Jobs Issue — Bulk Refresh Needed

jobs_registry.csv has **404 entries marked `new`**, the vast majority from April–June 2026. These roles are stale (80+ days old) but still labeled `new`. This has been noted since Jun 13 with no bulk resolution.

**Recommended action:** A one-time bulk pass to either:
1. Mark all `new` entries older than 60 days as `existing`, OR
2. Close entries where the role is obviously expired (e.g., short-term, co-op, specific req numbers)

This is a data hygiene issue — it does not affect daily sourcing but inflates the apparent novelty of the registry.

---

## Notable This Week

- **CPKC reposted 2 SWE roles** on eluta (Specialist SWE Cloud Developer Sep 16, Sr Specialist SWD Custom Solution Sep 17). Today's run (Sep 19) added both to registry.
- **Market remains quiet** — Sep 16–19 runs found no net-new companies. eluta and Built In Calgary sweeps returning minimal new activity.
- **Seed file is empty** — no pending candidates awaiting promotion.
- **Outreach pipeline is idle** — all outreach state files empty (headers only); no active leads, drafts, or threads.

---

## Seed List

No pending seed candidates this week.

---

## Watchlist

**Current watchlist: 0 companies** (unchanged).

---

## Summary

- **Symend removed from rejected** (reactivated via eluta; already in registry as active)
- **3 stale careers pages unchanged** (Viridien 404, Orion Steel down, Steel Reef 403) — careers_url corrections or `stale` status recommended
- **Stale jobs bulk refresh still pending** (404 `new` entries from Apr–Jun)
- **0 new seed additions**
- **0 new watchlist additions**
- **Outreach pipeline remains idle**

---

*Previous weekly review: 2026-09-12*
