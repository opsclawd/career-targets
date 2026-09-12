# Weekly Review — 2026-09-12

## Registry Status

- **201 active companies** in careers_registry
- **425 jobs** in jobs_registry (425 lines including header)
- **27 closed entries** in jobs_registry
- **Seed file:** Empty (clean)
- **Watchlist:** 0 companies
- **Rejected:** 8 companies

---

## New Companies This Week

**GitLab** — Global DevSecOps/platform company (NASDAQ: GTLB); Calgary office confirmed via Built In Calgary.
- Careers URL: `https://www.gitlab.com/company/careers`
- ATS: Greenhouse
- Source: Built In Calgary discovery (2026-09-12)
- Status: active
- Notes: Canada-remote SWE/SWE-adjacent roles active on Built In Calgary (Lead Enterprise Architect Professional Services, Senior Customer Engineer PostgreSQL, Senior Application Security Researcher); remote-first culture.

**Toast** — Restaurant POS platform; already in careers_registry (added 2026-09-12); roles confirmed via LinkedIn and Built In Calgary.

---

## Jobs Registry Review — Sep 6–12 Additions and Cleanup

### Sep 6–12 new job additions

| Company | Title | Date | Source |
|---|---|---|---|
| Infosys Ltd. | Technology Lead - Informatica Developer | Sep 6 | eluta.ca |
| Infosys Ltd. | AI Technical Lead | Sep 6 | eluta.ca |
| Modular Solutions | Data Migration Automation Developer | Sep 6 | eluta.ca |
| MISTRAS Group Inc. (Onstream Division) | Software Development Manager | Sep 9 | eluta.ca |
| Symend Inc. | Senior Software Engineer | Sep 9 | eluta.ca |
| Symend Inc. | Intermediate / Senior Product Engineer | Sep 4 | eluta.ca |
| SECURE Energy Services Inc. | SDET / Jr. Software Developer | Sep 9 | eluta.ca |
| General Dynamics Mission Systems-Canada | Co-op Winter 2025 - SW Engineering (TacCIS Solutions) - 12 Months | Sep 5 | eluta.ca |
| GitLab | Lead Enterprise Architect Professional Services (GitLab Professional Services) | unknown | Built In Calgary |
| GitLab | Senior Customer Engineer (PostgreSQL Automation) | Sep 10 | Built In Calgary |
| GitLab | Senior Application Security Researcher | Sep 6 | Built In Calgary |
| Toast | Lead Integration Engineer (Remote) | Sep 9 | Built In Calgary |
| Toast | Staff Software Engineer Employee Management (Remote) | Aug 25 | Built In Calgary |

### Noise Pattern: Precision AI typo URL

**Precision AI** has duplicate job entries with a malformed URL (`precisionai.ai.ai` instead of `precisionai.ai`):
- `https://www.precisionai.ai/careers` — valid
- `https://www.precisionai.ai/` — valid (canonical)
- `https://www.precisionai.ai.ai/` — **typo/double-extension** — both jobs using this URL should be closed

Two Precision AI jobs use the typo URL:
- AI Engineer (Built In Calgary, Apr 15)
- Embedded Engineer (LinkedIn, Apr 15)

**Action:** Mark Precision AI typo-URL jobs as closed.

### Noise Pattern: Mis-attributed Capco entry

jobs_registry has a Capco NodeJS/Java Developer entry with:
- `job_url`: LinkedIn URL
- `careers_url`: `morganstanley.com/careers` (should be `capco.com/careers`)
- `company`: Capco

The careers_url field is wrong — Capco's own careers page is `capco.com/careers`. LinkedIn may have listed this under the Morgan Stanley domain because Capco was a Morgan Stanley portfolio company at the time.

**Action:** Correct careers_url to `capco.com/careers` for this entry.

---

## Careers Registry Review

### Stale/Broken Entries

**Viridien** — careers page at viridien.com/en returns 404. Company is active on Built In Calgary (Calgary-based Subsurface Imaging IT/software role). The direct careers URL is unreliable; verify via Built In Calgary or LinkedIn. **Flag for correction or rejection if URL stays dead.**

**Orion Steel Group LLC** — careers URL listed as `orionsteels.com` (404). Jobs found via eluta only. The company's active URL appears to be a different domain. **Flag: investigate actual careers URL or mark stale.**

**Steel Reef Infrastructure Corp. (SRIC)** — careers page DNS issue noted Aug 16. Jobs still active on eluta. Careers URL at `steelreef.com` has DNS issue. **Flag stale.**

### Symend — Rejection Override

Symend was rejected Apr 25, 2026 because `boards.greenhouse.io/symend` was decommissioned (404). The direct careers page `symend.com/company/careers` was also dead at that time.

**Current status:** Symend has reappeared on eluta.ca with 2 active SWE roles (Sep 4–9, 2026). The careers_registry entry was updated to `active` on Sep 9. This is a legitimate reactivation — Symend appears to have moved to eluta ATS.

**Recommendation:** Remove Symend from rejected.md; it's now active via eluta.

### No action needed

- **BigGeo, North Vector Dynamics, Village Trust, Occupational Health, Granite Solutions, Amplifier Health, Blackline Safety** — all remain correctly rejected.

---

## Seed List

**Seed file is empty and clean.** No pending candidates this week.

---

## Watchlist

**Current watchlist: 0 companies** (unchanged).

---

## Summary

- **1 new company:** GitLab (already added to registry 2026-09-12)
- **Noise cleanup needed:**
  - Precision AI typo-URL jobs → mark closed
  - Capco mis-attributed careers_url → correct
- **3 careers pages flagged stale:** Viridien (404), Orion Steel (404), Steel Reef (DNS)
- **Symend reactivation** — remove from rejected (now active via eluta)
- **0 new seed additions**
- **0 new watchlist additions**
- Outreach pipeline remains idle

---

*Previous weekly review: 2026-09-05*
