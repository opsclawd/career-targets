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

---

## Weekly Review 2026-04-25

### Registry Status (End of Week 2)

- **88 companies** in careers_registry (up from ~73 at Apr 18)
- **108 jobs** in jobs_registry (up from ~81)
- **0 needs_review** — all previously unresolved companies either rejected (Symend, Village Trust, Occupational Health, MobSquad) or moved to watchlist (Blackline Safety Corp., Amplifier Health)
- **6 rejected** total (Granite Solutions, Symend, Village Trust, Occupational Health + 2 prior)
- **4 watchlist** additions this week (Blackline Safety Corp., Amplifier Health + the new Top Hiring companies NDAX and Keyera)

### Key Developments This Week

1. **NDAX confirmed active** — Workable board at apply.workable.com/ndax; 8+ open roles; Great Place to Work Certified. Previously a needs_review company resolved this week.
2. **MobSquad domain defunct** — All pages return 404 (copyright 2022 on defunct GoDaddy site). 4 SWE jobs in jobs_registry from Apr 14 eluta.ca discovery — roles likely expired. Rejected.
3. **Blackline Safety Corp.** — had Manufacturing SWE role Apr 11 (eluta.ca). LinkedIn search this week shows only 1 non-SWE role (Regional Sales Manager US West). Moved to watchlist pending confirmation of SWE availability.
4. **Amplifier Health** — real Calgary voice AI healthcare company with confirmed HQ, but SWE roles still not confirmed despite multiple checks. Watchlist pending further evidence.
5. **Keyera added** — Calgary energy midstream; Workday ATS (keyera.wd10.myworkdayjobs.com); on Built In Calgary; tech/IT roles present.

### Search Source Reliability (Week 2 Update)

- **eluta.ca** — Best source for direct employer career page SWE listings. Produced the most reliable new company discoveries this week (GeoSoftware, Halliburton, TerraSense, ACT Energy, Pleasant Solutions, geoLOGIC).
- **LinkedIn job search** — Productive for job-level discovery but bot-detection on career page lookups is inconsistent. Best used for job URL confirmation.
- **Built In Calgary** — Useful for company discovery; limited for job extraction (JS-rendered). Key new finds: Keyera, BMO.
- **DuckDuckGo** — Consistently bot-blocked this week. Multiple runs returned errors. Not reliable.
- **Web fetch (direct)** — Works for static careers pages; fails completely for JS-rendered ATS (Workday, iCIMS, Greenhouse custom) which constitute ~90% of known ATS boards.

### Market Observations (Apr 26–May 2)

- **Registry approaching saturation** — Apr 24–May 2 runs consistently found 0–2 new jobs. eluta.ca remains the highest-quality source; LinkedIn is bot-blocked or rate-limited most days.
- **New companies this week:** De Havilland Aircraft (aerospace, moving HQ to Calgary), Vivid Theory/BigGeo (geospatial SaaS), Capco, VantEdge.
- **MobSquad domain confirmed defunct** — All pages 404; 4 SWE jobs from Apr 14 marked closed this week.
- **RBC Feb jobs very stale** — 3 roles from Feb 3/25/26 (Senior SDE, Lead ML Platform, Staff AI Engineer) demoted to existing pending freshness re-check.
- **Energy sector strongest signal** — O&G tech continues as the most consistent SWE hiring sector in Calgary.
- **JS-rendered ATS still the biggest gap** — ~80% of boards require browser automation for extraction.

### Data Quality Notes

- **MobSquad jobs marked closed** — 4 jobs in jobs_registry (Apr 14 discovery) closed this week; company domain defunct.
- **RBC Feb jobs demoted to existing** — 3 roles from early-to-mid February (Senior SDE, Lead ML Platform, Staff AI Engineer) are very stale (~3 months old); demoted from `new` to `existing` pending freshness re-check.
- **job posted_date** — Still frequently "unknown" for LinkedIn/BuiltIn sources. Manual extraction not attempted in current workflow.

### Recommended Actions for Week 4

**High Priority:**
1. **Browser automation for Workday boards** — RBC, ATB Financial, TELUS, Keyera all use Workday. Playwright extraction is the single biggest unlock.
2. **Re-check Blackline Safety Corp. and Amplifier Health** — Both on watchlist; confirm whether SWE roles are still active.
3. **Seed list expansion** — Add: Suncor Energy, Shell Calgary, Jane Software, Clio, Arc'teryx tech, Cenovus, Enbridge.
4. **RBC job freshness re-check** — 3 Feb roles likely stale; need browser or direct verification.

**Medium Priority:**
5. **Greenhouse/ATS slug discovery** — Systematically try known ATS URL patterns for unknown-ATS companies.
6. **Data Engineer inclusion decision** — DE roles nearly as common as SWE; decide whether to include in scope.

**Low Priority:**
7. **Closed-job detection workflow** — Periodic re-check of existing jobs.
8. **eluta.ca monitoring cadence** — Most reliable source; consider daily vs. weekly cadence.