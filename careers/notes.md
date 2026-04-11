# Notes

Working notes about employers, ATS quirks, search patterns, and Calgary-market observations.

## Suggested notes to track

- ATS slug discoveries
- companies that require manual login
- recurring false positives
- location formatting quirks
- companies with strong hybrid-Calgary signals

---

## Weekly Review 2026-04-11

### ATS Patterns Observed

- **Greenhouse** — `boards-api.greenhouse.io/v1/boards/{slug}/jobs` is a reliable API endpoint for job extraction. Check if slug matches company name or known brand.
- **Workday** — JS-rendered; no static job content. May need browser automation or Workday API discovery.
- **iCIMS** — JS-rendered; no static content. Job extraction blocked.
- **Lever, Ashby, SmartRecruiters** — Not yet encountered in this seed; watch for future companies.

### Noise Patterns

- Several seed companies had outdated/broken careers URLs from the original seed file. These were corrected in the 2026-04-11 run. The seed file appears to be stale — consider refreshing it with verified URLs.
- TD Bank has no valid direct careers page accessible; the td.com/careers redirect leads to a generic page. TD may require a specific job board URL pattern.

### Market Observations

- Calgary senior software engineering roles are sparse on direct employer boards right now. RBC is the most productive find so far.
- Many Calgary fintech/insurtech companies (Symend, Village Trust) have small engineering teams and may not have active senior postings.
