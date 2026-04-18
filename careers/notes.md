# Notes

Working notes about employers, ATS quirks, search patterns, and Calgary-market observations.

## Suggested notes to track

- ATS slug discoveries
- companies that require manual login
- recurring false positives
- location formatting quirks
- companies with strong hybrid-Calgary signals

---

## Weekly Review 2026-04-18

### ATS Patterns Observed

- **Greenhouse** — `boards-api.greenhouse.io/v1/boards/{slug}/jobs` works for Benevity and Orennia. Symend's board is decommissioned (404). Try slug variations before giving up.
- **Workday** — JS-rendered across the board. RBC, TD, ATB Financial all use Workday. No static extraction possible without browser automation.
- **Lever** — Orennia uses Lever. API-accessible at `api.lever.co/v0/postings/{slug}`.
- **Dover** — Validere uses Dover. Limited extraction experience.
- **iCIMS** — JS-rendered; Mackenzie Investments, Capco. Low priority.
- **Unknown/Custom** — 60 companies with unknown ATS. LinkedIn is the primary discovery source for these.

### Search Source Reliability

- **LinkedIn job search** — Most productive source this week. Delivers 100+ Calgary SWE results per sweep. Essential for companies with JS-rendered career pages.
- **Built In Calgary** — Good for company discovery and some job listings. Limited to member companies.
- **DuckDuckGo** — Unreliable due to rate-limiting and bot detection. Not viable as a primary search source.
- **Direct career page fetch** — Works only for Greenhouse/Lever boards. All Workday/iCIMS/custom pages are JS-rendered and return no content.

### Market Observations (Apr 12–18)

- Calgary SWE market is surprisingly active for mid-April. 81 roles tracked across 73 companies.
- **Affirm** is the biggest surprise — 3 new backend roles in one day suggests a major Calgary engineering expansion.
- **Canonical** continues to be the highest-volume hirer (8 roles) with remote-first model benefiting Calgary.
- **O&G tech** is well represented: Cenovus, Enverus, Quorum Software, TC Energy, Subsurface Dynamics, Validere, Orennia.
- **Fintech** cluster growing: RBC, Peoples Group, NDAX, ZayZoon, Alpaca, Neo Financial.
- **Data Engineering** roles are almost as common as SWE roles — consider whether to broaden scope.

### Data Quality Issues

- **Capco** entry in jobs_registry has wrong careers_url (points to morganstanley.com). Should be capco.com/careers.
- **BigGeo** careers page 404s; company recruits only via LinkedIn.
- **Several seed file URLs** were stale/broken. Most were corrected during the Apr 11–15 runs.
- **Job posted_date** is often "unknown" for LinkedIn-sourced entries. Consider adding date extraction.

### Infrastructure Notes

- **DuckDuckGo rate limiting** is consistent across runs. Consider rotating user-agents or using alternative search APIs.
- **Browser automation** would unlock Workday/iCIMS/custom board extraction — the single biggest improvement possible.
- **LinkedIn public pages** work without login but may require browser for full job detail access.