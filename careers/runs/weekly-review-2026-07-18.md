# Weekly Review — 2026-07-18

## Registry Status

- **152 active companies**, **8 rejected** (unchanged since Jul 4)
- Last meaningful addition was **Trail Appliances Ltd.** (Jul 17)
- No new companies found in any run since Jul 2 — registry saturation confirmed
- 3 seed candidates from Jul 4 still pending promotion: **Proper AI**, **360Learning**, **ThinkData Works**

---

## Careers Registry Review

### No stale, broken, or redirected entries found this review

All previously flagged entries remain stable:
- **BigGeo** — rejected (careers 404 since Apr 16); Vivid Theory covers the company
- **North Vector Dynamics** — rejected (Ashby board never returned parseable content)
- **MobSquad** — rejected (domain defunct; eluta board is source)
- **Symend / Village Trust / Occupational Health / Granite Solutions** — rejected

No new stale entries requiring action this week. Most April-checked companies are large/stable enterprises where the careers page is unlikely to have changed materially.

---

## Jobs Registry Review — Noise Patterns

### Non-SWE entries still in active state

The following entries should be marked `closed` in jobs_registry (they're not software engineering roles):

| Company | Title | Issue |
|---------|-------|-------|
| **Rokt** | Territory Account Executive | Sales role, not SWE |
| **Samsara** | Account Executive - Mid-Market | Sales role, not SWE |
| **NDAX** | Head of Product Management | Product management, not SWE |
| **NDAX** | Product Manager | Product management, not SWE |

**Action:** Mark these 4 jobs as `closed` in jobs_registry.

### Previously flagged items — no change needed

- **Enverus Sales Development Representative** — already marked `closed` ✓
- **MobSquad entries** — already marked `closed` ✓
- **Toast "Staff SWE, Tech Lead"** — remote Canada only, not Calgary/Alberta. Flagged Jul 4; no action taken since. Recommend marking `filtered_out` or removing from registry.

---

## Seed List

3 seed candidates from Jul 4 have **not yet been promoted** to careers_registry:

| Company | Status | Action |
|---------|--------|--------|
| **Proper AI** | In seed since Jul 4 | Promote to registry |
| **360Learning** | In seed since Jul 4 | Promote to registry (Canada-remote) |
| **ThinkData Works** | In seed since Jul 4 | Promote to registry (Canada-remote) |

**Seed file quality note:** `companies_seed.csv` still contains 5 companies that are already in `rejected.md`: Symend, Village Trust, Occupational Health, Granite Solutions, ATB Financial (some have duplicates with incorrect ATS types). These should be **removed from companies_seed.csv** to avoid confusion.

---

## Watchlist

**Current watchlist: 0 companies** (unchanged)

---

## Outreach State

All outreach state files unchanged — still empty:
- `leads.csv` — 0 leads
- `threads.csv` — 0 active threads
- `approvals.csv` — 0 pending
- `suppression.csv` — 0 entries
- `activity.jsonl` — 129 entries (all queue checks return empty)

Outreach pipeline has been inactive since at least Jun 16. No changes to push.

---

## Summary of Changes This Week

1. **jobs_registry.csv** — mark 4 non-SWE entries as `closed`: Rokt Territory Account Executive, Samsara Account Executive, NDAX Head of Product Management, NDAX Product Manager
2. **companies_seed.csv** — remove 5 rejected/duplicate entries (Symend, Village Trust, Occupational Health, Granite Solutions, ATB Financial)
3. **Promote to registry:** Proper AI, 360Learning, ThinkData Works

---

*Previous weekly review: 2026-07-04*
