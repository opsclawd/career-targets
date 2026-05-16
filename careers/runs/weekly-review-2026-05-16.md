# Weekly Review — 2026-05-16

Agent: career-targets weekly review
Review period: 2026-05-10 to 2026-05-16

---

## Registry Status

| Metric | Start (May 9) | End (May 16) | Change |
|---|---|---|---|
| Companies in registry | 120 | ~125 | +5 |
| Jobs in registry | ~156 | ~168 | +12 |
| Active | ~117 | ~120 | +3 |
| Watchlist | 2 | 2 | — |
| Rejected | 6 | 6 | — |

Registry continues to grow modestly. Daily runs May 10–16 found 8 net-new jobs across 5 new companies, consistent with plateau phase noted since late April.

---

## New Companies Since May 9

| Company | Careers URL | ATS | Source | Notes |
|---|---|---|---|---|
| North Vector Dynamics | jobs.ashbyhq.com/northvectordynamics | ashby | Built In Calgary | Defense tech (precision autonomous air defense); Calgary HQ |
| RigUp | rigup.com/careers | unknown | Built In Calgary | Energy source-to-pay SaaS; Calgary + Austin + Belfast |
| Connect First Credit Union | eluta.ca | unknown | eluta | Canada's largest credit union (Servus); CRM Salesforce dev |
| Luxoft | eluta.ca | unknown | eluta | Global IT consulting; Subsurface Backend Dev + Senior Java Dev |
| CGI Inc. | eluta.ca | unknown | eluta | Global IT services (Montreal HQ); Senior Mobile Developer Android |
| Capgemini Canada | capgemini.com/ca-en/careers | unknown | eluta | Global consulting; Full Stack Developer (ReactJS/Java/AWS) Calgary |
| DataVisor | datavisor.com/careers | unknown | eluta | AI-powered fraud/risk SaaS; Calgary office; Sr SWE $120K-$150K |
| CAWST | eluta.ca | eluta | eluta | Calgary non-profit (water/sanitation tech); Full Stack Developer |
| Pason Systems Corp. | pason.com/careers | unknown | eluta | Specialized data management for energy rigs; TOP EMPLOYER |
| Divine Hardwood Flooring Ltd. | divineflooring.com/careers | unknown | eluta | Calgary flooring supplier; Sr. Software Developer |

---

## New Jobs Since May 9

| Job | Company | Source | Posted |
|---|---|---|---|
| Full Stack Developer – Product Engineering | Showpass | eluta.ca | May 1 (confirm no dup) |
| Senior Staff Developer – Calgary AB | Benevity | eluta.ca | Apr 30 |
| Software Application Developer | BMO Financial Group | eluta.ca | Apr 29 |
| Lead Software Development Engineer in Test | Nutrien | LinkedIn | Apr 27 |
| Senior Software Quality Engineer | Galent | LinkedIn | May 1 |
| Senior Software Engineer | VantEdge | LinkedIn | May 2 |
| Software Engineer II – .net Backend / React Front End | Quorum Software | LinkedIn | May 1 |
| Software Developer - CRM Salesforce | Connect First Credit Union | eluta.ca | May 6 |
| Subsurface Backend Developer | Luxoft | eluta.ca | May 6 |
| Senior Java Developer | Luxoft | eluta.ca | May 4 |
| Senior Mobile Developer - Android | CGI Inc. | eluta.ca | May 6 |
| Senior Developer Enterprise AI | Clio | eluta.ca | May 5 |
| Software Development Engineer (GPU Primitives Libraries) | AMD Canada | eluta.ca | May 8 |
| Co-op Fall 2026 - Software Engineering Developer (16 months) | General Dynamics | eluta.ca | May 7 |
| Full Stack Developer (Calgary) | Capgemini Canada | eluta.ca | May 14 |
| Senior Software Engineer - Canada | DataVisor | eluta.ca | May 14 |
| Full Stack Developer | CAWST | eluta.ca | May 15 |
| Analyst Software Developer (Advanced Train Control) | CPKC | eluta.ca | May 15 |
| Specialist Software Cloud Developer | CPKC | eluta.ca | May 15 |
| Software Developer (Enterprise Applications) | Pason Systems Corp. | eluta.ca | May 15 |
| Sr. Software Developer | Divine Hardwood Flooring Ltd. | eluta.ca | May 15 |

**Net-new job additions this week: ~15** (after deduplication)

---

## Careers Pages Reviewed

### Stale / Broken Pages

| Company | Issue | Action |
|---|---|---|
| **BigGeo** | biggeo.com/careers returns 404; company active via Vivid Theory brand on eluta.ca | Update careers_registry.csv status to `stale`; note Vivid Theory as active brand |
| **Helcim Inc.** | careers page Cloudflare-blocked; jobs found via eluta.ca only | Keep entry as-is; note Cloudflare blocking in notes |

### Active Pages Verified This Week

- **Blackline Safety Corp.** — Still has a "Reliability Engineer/Specialist" role on their careers page (May 16 check). Not a SWE role. No manufacturing SWE seen since Apr 11.
- **Amplifier Health** — HQ confirmed Calgary; voice AI healthcare; SWE roles still unconfirmed.

### Pages Needing Confirmation

- **GeoSoftware** — last checked Apr 19; no update since. Verify still active.
- **TerraSense Analytics** — last checked Apr 19; no update since. Verify still active.

---

## Watchlist Review

### Blackline Safety Corp. — Pending Resolution
- **Last seen:** Manufacturing SWE on eluta.ca (Apr 11)
- **Today (May 16):** Careers page shows "Reliability Engineer/Specialist" — ops/hardware role, not SWE.
- **Conclusion:** No SWE role confirmed in 5+ weeks. Manufacturing SWE from Apr 11 has likely closed.
- **Recommendation:** Move from `watchlist` to `rejected`. The company's current hiring is hardware/ops focused.

### Amplifier Health — Keep on Watchlist
- **Status:** Calgary voice AI healthcare company with confirmed HQ.
- **Conclusion:** Still no SWE confirmation. Keep on watchlist another 2 weeks.

---

## Rejected Review

No new candidates for rejection this week, except Blackline Safety Corp. pending above.

---

## Seed List Candidates

**Add to companies_seed.csv:**
- **Suncor Energy** — Calgary energy giant; not yet in registry
- **Shell Canada (Calgary)** — Calgary office; not yet in registry
- **Jane Software** — Calgary project management SaaS; not yet in registry

**Already in registry (no action needed):**
- Cenovus Energy — added Apr 18
- Enbridge — added Apr 18, confirmed active
- Clio — added Apr 17, confirmed active

---

## Jobs Registry Noise Patterns

- **Duplicate:** Showpass Full Stack Developer appeared May 4 and May 9 — caught by dedup.
- **Indeed placeholder URLs:** Helcim Inc. and Millennium EMS have "indeed.com/viewjob?jk=XXXX" as placeholder URLs from eluta scrape. Not actionable — jobs are real but URL malformed. These appear to be edge cases from eluta.ca not providing clean URLs.

**No new noise patterns detected.**

---

## Recommended Actions for Week 6

**High Priority:**
1. **Move Blackline Safety Corp. to rejected** — No SWE in 5+ weeks; only ops/hardware roles active
2. **Add Suncor Energy, Shell Canada (Calgary), Jane Software to companies_seed.csv**
3. **Update BigGeo status to `stale`** in careers_registry.csv; note Vivid Theory as active brand
4. **Confirm GeoSoftware and TerraSense** — both last checked Apr 19

**Medium Priority:**
5. **Browser automation for Workday boards** — still the biggest unlock; RBC, ATB Financial, TELUS, Keyera remain inaccessible
6. **Capco careers_url** — still points to morganstanley.com instead of capco.com/careers

**Low Priority:**
7. **eluta.ca cadence** — daily runs finding 0–2 jobs; consider weekly cadence for efficiency
8. **Closed-job detection** — no systematic workflow for catching stale roles

---

## Summary

- **Companies tracked:** ~125 (active ~120, watchlist 2, rejected 6)
- **Jobs tracked:** ~168 (+12 since May 9)
- **Careers pages flagged:** BigGeo (stale 404), Helcim (Cloudflare blocked), GeoSoftware/TerraSense (need re-check)
- **Watchlist status:** Blackline Safety Corp. → recommend reject (no SWE since Apr 11); Amplifier Health stable
- **Seed list additions:** Suncor Energy, Shell Canada (Calgary), Jane Software
- **Biggest gap:** Registry plateau + JS-rendered ATS still require browser automation for full coverage