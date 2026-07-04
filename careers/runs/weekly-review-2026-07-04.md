# Weekly Review — 2026-07-04

## Registry Status

- **152 active companies**, **8 rejected** (unchanged from Jun 20)
- **No new companies or jobs found** in any run since Jun 29
- Jul 3 and Jul 4 runs explicitly found zero new entries
- Registry saturation confirmed — last meaningful addition was **athennian** (Jul 2)

---

## Careers Pages Flagged for Review

### Stale Entries (last_checked before Jun 1, still marked active)

Many companies were last checked in April or May. The following have been active for 60–90+ days without re-check. Recommend re-confirming or marking `needs_review`:

- **The I.T. Company** — last_checked 2026-04-16 (Airdrie AB, IT/software)
- **Benevity** — last_checked 2026-04-18
- **Precision AI** — last_checked 2026-04-14
- **headversity** — last_checked 2026-04-14
- **WestJet** — last_checked 2026-04-15
- **Enverus** — last_checked 2026-04-15
- **StackAdapt** — last_checked 2026-04-15
- **ICE** — last_checked 2026-04-15
- **Fullscript** — last_checked 2026-04-15
- **Garmin** — last_checked 2026-04-15
- **Canonical** — last_checked 2026-04-17
- **MongoDB** — last_checked 2026-04-17
- **Shopify** — last_checked 2026-04-18
- **ATB Financial** — last_checked 2026-04-18
- **Symend** — rejected; correctly flagged
- **Village Trust** — rejected; correctly flagged

Most of these are large/tracking companies where the careers page is unlikely to have changed substantially. A full re-check sweep is low-value given saturation. **No action recommended** unless specific roles need verification.

### Toast "Staff SWE, Tech Lead" — Filter Out

Added Jul 2: `builtincalgary.org/company/toast/jobs` — "Staff Software Engineer, Tech Lead" at Toast, Remote Canada. This is **remote Canada only**, not Calgary or Alberta. Per AGENTS.md inclusion rules, Canada-remote is only valid "if clearly Canada-remote." Toast's listing doesn't have a Calgary/Alberta signal. **Recommend marking `status=filtered_out`** or adding a note that this is Canada-remote only.

---

## Jobs Registry Review

### Duplicates (same company + title + location, different job URLs)

The following appear multiple times in jobs_registry — likely different posting URLs for the same role:

| Company | Title | Count | Notes |
|---------|-------|-------|-------|
| Canadian Pacific Kansas City | Analyst Software Developer | 2 | Likely different req numbers |
| Canadian Pacific Kansas City | Mainframe SWE (12mo term) | 2 | Same |
| Canadian Pacific Kansas City | Senior Specialist SWE Custom Solution | 2 | Same |
| Canadian Pacific Kansas City | Specialist Software Cloud Developer | 3 | Different reqs |
| BMO Financial Group | Software Application Developer | 3 | Gen AI + standard |
| LodgeLink Inc. | Senior Software Engineer Back-end Focus | 2 | Different reqs |
| Capgemini Canada Inc. | Full Stack Developer | 2 | Likely same posting, different sources |

These are not errors — they reflect different job req URLs. No action needed unless exact dedup is required.

### MobSquad Entries — All Closed

MobSquad has been rejected but jobs_registry still has 8 rows for MobSquad (4 roles, each appearing twice — same listing from eluta vs. direct). All MobSquad entries should be marked `closed`. No changes to careers_registry since MobSquad is already rejected.

---

## Seed List Gap

`companies_seed.csv` has only 12 seed entries from early April — all already in registry or rejected. Three new seed candidates identified this week:

| Company | Rationale |
|---------|-----------|
| **Proper AI** | Calgary-based AI company; raised USD $10M Series A (Aug 2024); building ERP AI agents; actively hiring senior engineers (LinkedIn, Jan 2026). |
| **360Learning** | Paris-based L&D SaaS; Canada-remote engineering roles; 700+ employees; hiring senior engineers. |
| **ThinkData Works** | Toronto-based data infrastructure SaaS; some Canadian-remote SWE roles; Series B. |

All three should be added to `companies_seed.csv` for the next daily run to resolve into `careers_registry.csv`.

---

## Outreach State

All outreach state files remain empty (same as Jun 20):

- `leads.csv` — 0 leads
- `threads.csv` — 0 active threads
- `approvals.csv` — 0 pending
- `suppression.csv` — 0 entries
- `activity.jsonl` — 68 entries (all queue checks return empty)

The outreach pipeline has been inactive since at least Jun 16. Career-targets sourcing crons are running and finding no new jobs. Nothing to update in outreach state.

---

## Notable Observations

- **athennian confirmed** (Jul 2): Governance SaaS; Work Remotely with Calgary presence confirmed; SWE CAD 90K-130K on eluta.ca. Strong addition to registry.
- **PayShepherd confirmed** (Jul 1): Vertical SaaS for heavy industries; Full Stack Developer (AI-Native) CAD 130K-160K; remote ok but Calgary presence present.
- **Sourcing is exhausted via current methods**: eluta.ca pagination is broken, DuckDuckGo is bot-blocked, Built In Calgary offset pagination is broken. Next phase requires browser automation or direct ATS API calls.
- **No weekly review written for Jun 27** — this review covers the gap period.

---

*Previous weekly review: 2026-06-20*
