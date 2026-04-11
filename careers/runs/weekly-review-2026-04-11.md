# Weekly Review — 2026-04-11

Agent: career-targets weekly review
Review period: 2026-04-05 to 2026-04-11

---

## Careers Registry Assessment

### Stable / Active (5)

| Company | ATS | Status | Notes |
|---|---|---|---|
| Benevity | greenhouse | active | Greenhouse API confirmed. Job found this week. |
| Canadian Pacific Kansas City | greenhouse | active | Board at careers.cpr.ca; talent community only |
| ATB Financial | custom/workday | active | Workday likely; JS-rendered |
| RBC | workday | active | 3 relevant Calgary jobs found this week |
| Shopify | custom | active | JS-rendered; no content extracted |

### Needs Review / Unresolved (5)

| Company | Issue | Action |
|---|---|---|
| Symend | Careers page confirmed but ATS type unconfirmed | Try Greenhouse API slug: `symend` |
| Village Trust | DNS failure | Verify company is still operating; try alternate URL |
| Occupational Health | DNS failure | Likely not a tech employer; verify |
| TD Bank | No valid careers page | Needs alternate URL pattern |
| Mackenzie Financial | iCIMS; JS-rendered | No content; consider deprioritizing |

### Permanent Rejects (1)

| Company | Reason |
|---|---|
| Granite Solutions | Stone/masonry company, not software. No relevant roles possible. |

---

## Jobs Registry Assessment

- **Total jobs in registry:** 3 (all RBC, discovered 2026-04-11)
- **Noise patterns:** None detected this week; dedup logic held
- **Stale listings:** None — registry is fresh

---

## ATS Coverage Gaps

- Greenhouse API works for Benevity. Apply same pattern to Symend.
- Workday boards (RBC, ATB) are JS-rendered; consider adding browser-based extraction.
- iCIMS boards (Mackenzie) are JS-rendered; low priority.

---

## Seed List Health

The original `companies_seed.csv` contains outdated/broken URLs. Several were corrected in the 2026-04-11 daily run. The seed file should be refreshed with verified URLs before next expansion sweep.

---

## Recommended Actions

1. **Next week:** Try Greenhouse API slug discovery for Symend (`boards-api.greenhouse.io/v1/boards/symend/jobs`)
2. **Next week:** Search for valid TD Bank careers URL pattern
3. **Next week:** Expand seed list with additional Calgary employers (see watchlist.md suggestions)
4. **Consider:** Browser automation for Workday/iCIMS job extraction

---

## Summary

- **Active careers pages:** 5
- **Needs review:** 5
- **Permanent rejects added:** 1 (Granite Solutions)
- **Jobs in registry:** 3 RBC Calgary roles
- **Seed file:** Needs refresh with verified URLs
