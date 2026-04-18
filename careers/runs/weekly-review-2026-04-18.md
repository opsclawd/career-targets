# Weekly Review — 2026-04-18

Agent: career-targets weekly review
Review period: 2026-04-12 to 2026-04-18

---

## Registry Growth

| Metric | Start (Apr 12) | End (Apr 18) | Change |
|---|---|---|---|
| Companies in registry | ~30 | 73 | +43 |
| Jobs in registry | 3 | 81 | +78 |
| Active careers pages | ~5 | 68 | +63 |
| Needs review | 3 | 4 | +1 (NDAX) |
| Rejected | 1 | 1 | 0 |

The registry expanded massively this week, from a seed of ~30 companies to 73 after aggressive sourcing from LinkedIn, Built In Calgary, and web discovery.

---

## Top Hiring Companies (by job count)

| Company | Jobs | Notes |
|---|---|---|
| Canonical | 8 | Remote-first; multiple SWE roles open |
| RBC | 5 | Calgary's largest active hirer; Workday board |
| MongoDB | 4 | Growing Calgary presence |
| Affirm | 4 | 3 new backend SWE roles this week — aggressive Calgary expansion |
| Quorum Software | 4 | Energy SaaS, Calgary hybrid |
| Morgan Stanley | 3 | Calgary Dev roles |
| Precision AI | 3 | AI/ML roles |
| WestJet | 2 | Transitioning recruiting systems Apr 17–May 6 |
| AMD | 2 | Staff-level SDE + GPU roles in Calgary |

---

## Jobs Discovery by Day

| Date | New Jobs | Sources |
|---|---|---|
| 2026-04-11 | 3 | RBC Workday board |
| 2026-04-12 | 0 | Re-checks only |
| 2026-04-13 | 0 | Re-checks only |
| 2026-04-14 | 5 | Built In Calgary, Technology Alberta |
| 2026-04-15 | 35 | LinkedIn (primary), Built In Calgary |
| 2026-04-16 | 11 | LinkedIn, Built In Calgary |
| 2026-04-17 | 19 | LinkedIn, Built In Calgary, direct career pages |
| 2026-04-18 | 8 | LinkedIn, Built In Calgary, direct career pages |

April 15 was the breakout day (27 new companies + 35 jobs) when LinkedIn sourcing became the primary source.

---

## ATS Coverage Analysis

| ATS Type | Count | Extractable? | Notes |
|---|---|---|---|
| unknown | 60 | Varies | Most discovered via LinkedIn, not direct boards |
| custom | 4 | No (JS-rendered) | Shopify, CPKC, Symend, ATB Financial |
| workday | 3 | No (JS-rendered) | RBC, TD Bank, ATB Financial |
| icims | 2 | No (JS-rendered) | Mackenzie Investments, Capco |
| greenhouse | 2 | Yes (API) | Benevity, Orennia |
| lever | 1 | Yes (API) | 1 company |
| dover | 1 | Partial | Validere |

**Key gap:** 63 of 73 companies (86%) have unknown or JS-rendered ATS types that can't be scraped via API. LinkedIn and Built In Calgary are filling the gap, but direct ATS extraction is limited to Greenhouse and Lever boards.

---

## Persistent Issues

### Needs Review (4 companies)

| Company | Issue | Duration | Recommended Action |
|---|---|---|---|
| Symend | Greenhouse board decommissioned; no ATS found | 7 days | Mark inactive; search for alternate board or accept LinkedIn-only sourcing |
| Village Trust | DNS failure | 7 days | Likely defunct or renamed; mark rejected |
| Occupational Health | DNS failure; not a tech employer | 7 days | Not a software company; mark rejected |
| NDAX | Careers page 404 | 1 day | Calgary crypto exchange; search for alternate careers URL next run |

### JS-Rendered Boards (can't extract directly)

ATB Financial, CPKC, Mackenzie Investments, TD Bank, Shopify, WestJet (transitioning), Affirm, Cisco, ICE, Morgan Stanley, Workday (company), StackAdapt, Clio, GHGSat, and ~50 others.

These are effectively invisible to non-browser scraping. LinkedIn and Built In Calgary provide job data for many of these, but direct page monitoring is not possible without browser automation.

### Search Limitations

- **DuckDuckGo** rate-limited/blocked on multiple runs this week. Not reliable as primary search source.
- **LinkedIn** public job pages are the most productive source but require browser automation or manual search.
- **Built In Calgary** is useful but has limited company coverage.

---

## Notable Market Observations

### Calgary SWE Market Is Active

The Calgary senior/staff software engineering market shows significant activity this week:

- **Affirm** hired aggressively (3 backend roles in one day, including Staff level) — signals major Calgary expansion
- **Canonical** (8 roles) and **MongoDB** (4 roles) continue to build Calgary remote presence
- **O&G tech arms** are hiring: Cenovus, Enverus, Quorum Software, TC Energy, Subsurface Dynamics
- **Fintech** is well represented: RBC, Peoples Group, NDAX, ZayZoon, Alpaca, Neo Financial
- **Energy transition/climate** is emerging: GHGSat, Orennia, Validere, Precision AI

### Seniority Mix

The majority of roles cluster around Senior SWE (target hit), with notable Staff-level openings at Affirm, Canonical, LodgeLink, and AMD. Data Engineering roles are also prominent (S&P Global, IBM, HCLTech, TC Energy, Lumenalta).

---

## Recommended Actions for Next Week

### High Priority

1. **Resolve needs_review companies:** Mark Village Trust and Occupational Health as rejected. Attempt one more search for NDAX careers URL. Try Greenhouse API slug `symend` one final time, then mark inactive.
2. **Expand seed list:** Add major Calgary employers not yet in registry (Suncor, Shell Calgary, Enbridge direct roles, Jane Software, Clio direct ATS, Arc'teryx tech).
3. **Browser automation:** Consider adding Playwright-based job extraction for the top JS-rendered boards (RBC, ATB, TD, Affirm, WestJet). These represent the highest-value targets with the most Calgary roles.

### Medium Priority

4. **Greenhouse/ATS slug discovery:** For the ~60 companies with unknown ATS, systematically try known ATS URL patterns to find extractable boards.
5. **Stale job cleanup:** Some RBC roles were posted in February (2 months old). Review whether still active and mark closed if not.
6. **Track job status changes:** Implement re-checking of existing jobs to detect when roles close (status → closed).

### Low Priority

7. **DuckDuckGo alternative:** Find a more reliable web search source for career page discovery.
8. **Data Engineer role classification:** Decide whether to broaden target titles to include Data Engineer roles, given Calgary market composition.

---

## Summary

- **Companies tracked:** 73 (68 active, 4 needs_review, 1 rejected)
- **Jobs tracked:** 81
- **New companies this week:** ~43
- **New jobs this week:** 78
- **Top hirers:** Canonical (8), RBC (5), MongoDB (4), Affirm (4), Quorum Software (4)
- **Biggest win:** LinkedIn sourcing on Apr 15 unlocked 27 new companies and 35 jobs in a single day
- **Biggest gap:** 86% of companies can't be scraped via API (JS-rendered or unknown ATS) — needs browser automation or continued LinkedIn reliance
- **Persistent issues:** 3 needs_review companies (2 likely rejectable), DuckDuckGo search blocking