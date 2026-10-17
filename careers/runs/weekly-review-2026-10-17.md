# Weekly Review — 2026-10-17

## Registry Status

- **225 companies** in careers_registry
- **496 jobs** in jobs_registry (495 data rows + header)
- **Seed file:** Empty (clean)
- **Watchlist:** 0 companies
- **Rejected:** 7 companies

---

## Action Items from Last Week — Status

### 3 Stale Careers Pages — Resolved This Week

All three were flagged Sep 12 and remained broken as of Oct 10. Status updated to `needs_review` this week:

| Company | Previous Status | New Status | Issue |
|---------|---------------|------------|-------|
| Viridien | active | needs_review | main careers page viridien.com/en returns 404 (since Aug 25); Built In Calgary profile is the only known active source |
| Orion Steel Group LLC | active | needs_review | orionsteels.com down; eluta.ca ATS is the only confirmed source |
| Steel Reef Infrastructure Corp. (SRIC) | active | needs_review | steelreef.com DNS failure (since Aug 16); eluta ATS confirmed as active source |

---

## Noise Cleanup: Intern/Junior/Student Jobs

**18 jobs** with intern, junior, or student in the title were incorrectly marked `new`. Per AGENTS.md exclusion rules (Intern, Internship, Junior, Student), all 18 have been reclassified to `filtered_out`:

| Company | Title | Issue |
|---------|-------|-------|
| Canonical | Junior Ubuntu Software Engineer | Junior |
| Canonical | Junior Software Developer - Observability | Junior |
| PBS Systems Inc. | Junior Software Developer | Junior |
| DV8 Energy Inc. | Junior Embedded IoT Edge Software Developer | Junior |
| Calgary Sports and Entertainment Corp. (CSEC) | Junior Developer | Junior |
| AMD Canada | Summer 2027 Long Term Software Engineering Intern/Co-op | Intern |
| NovAtel Inc. (Hexagon) | Software Engineering Intern | Intern |
| NovAtel Inc. (Hexagon) | Software Test Engineering Intern | Intern |
| AMD Canada | Short Term 2027 Software Engineering Intern/Co-Op | Intern |
| Pason Systems Corp. | Software Developer Intern (Rigsite) | Intern |
| Pason Systems Corp. | Software Developer Intern (Enterprise Applications) | Intern |
| Pason Systems Corp. | Software Developer Intern (DataHub) | Intern |
| Pason Systems Corp. | Software Developer Intern (IWS) | Intern |
| Pason Systems Corp. | Software Developer Intern (Quality Assurance) | Intern |
| SECURE Energy Services Inc. | Software Developer Intern | Intern |
| geoLOGIC Systems Ltd. | Junior Software Developer | Junior |
| Ecolab Co. (CoolIT Systems) | Junior Quality Control Software Developer | Junior |
| Cenovus Energy | Student AI and Software Engineering (May 2027) | Student |

**Note:** Benevity "Infrastructure Developer Internal Apps" was flagged by substring matching but contains "Internal" (not "Intern") and is a legitimate role — retained as `new`.

---

## Net-New Jobs This Week (Oct 11–17 sweeps)

| Company | Title | Source | Date |
|---------|-------|--------|------|
| Benevity | Software Development Manager | eluta | Oct 10 |
| Clio | Senior Data Engineer | eluta | Oct 9 |
| Clio | Software Developer Co-op (8-month, Jan-Aug 2027) | eluta | Oct 8 |
| Canadian Pacific Kansas City | Mainframe Software Developer (7-month term) | eluta | Oct 16 |
| Benevity | Lead Developer Experience and SDLC Modernization | Built In Calgary | Oct 10 |
| Benevity | Senior Staff Developer User Identity Access Management (UIAM) | Built In Calgary | Oct 10 |
| AltaML | Senior AI Solutions Architect | Built In Calgary | Oct 17 |

**Total net-new jobs this period: 7** (from 3 companies — Benevity, Clio, CPKC, AltaML)

---

## Careers Pages / Roles Flagged for Follow-up

- **Viridien** — careers page 404; update careers_url to Built In Calgary or keep eluta as canonical; status: needs_review
- **Orion Steel Group LLC** — own site down; eluta only; status: needs_review
- **Steel Reef Infrastructure Corp.** — own site DNS failure; eluta active; status: needs_review

---

## Seed List

No pending seed candidates this week. Seed file is empty.

---

## Watchlist

**Current watchlist: 0 companies** (unchanged).

---

## Rejected

**7 companies** (unchanged): Granite Solutions, Village Trust, Occupational Health, Amplifier Health, BigGeo, Blackline Safety Corp., North Vector Dynamics.

---

## Outreach State Files

- `outreach/state/leads.csv` — headers only, empty
- `outreach/state/threads.csv` — headers only, empty
- `outreach/state/approvals.csv` — headers only, empty
- `outreach/state/suppression.csv` — headers only, empty
- `outreach/state/activity.jsonl` — all events report `idle`/`no_active_leads`/`no_replies`; outreach pipeline is idle

**No outreach state changes needed this week.**

---

## Summary

- **0 new employers added** this week
- **7 net-new SWE-relevant jobs** from 4 companies (Oct 11–17)
- **18 intern/junior/student noise jobs** reclassified to filtered_out
- **3 stale careers pages** updated to `needs_review` (Viridien, Orion Steel, Steel Reef)
- **Outreach pipeline** — idle, no state changes

---

*Previous weekly review: 2026-10-10*
