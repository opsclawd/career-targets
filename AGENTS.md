# Career Targets Agent Rules

You maintain a Calgary-focused direct-employer careers registry and a deduped job ledger.

## Objective

Every run must:

1. resolve missing direct employer careers pages
2. re-check known careers pages
3. append only net-new relevant jobs
4. write a run summary under `careers/runs/`
5. commit and push meaningful changes to `origin/main`

## Hard rules

- Prefer direct employer careers pages only.
- Never use LinkedIn, Indeed, Eluta, Job Bank, or aggregator links as canonical careers pages.
- Canonical careers pages must be:
  - company careers page
  - Ashby
  - Greenhouse
  - Lever
  - Workday
  - SmartRecruiters
  - other direct ATS page
- If a company has no careers page:
  1. try known ATS patterns first
  2. search the public web for `"<company> careers jobs"`
  3. verify the page is a real jobs page
  4. save it to `careers_registry.csv`
- Filter for senior software engineering roles relevant to Calgary.
- Include:
  - Calgary
  - Calgary, AB
  - Alberta
  - Hybrid Calgary
  - Remote Canada only if clearly Canada-remote
- Exclude:
  - US-only
  - Europe-only
  - internship
  - junior
  - student
  - unrelated roles
- Deduplicate by exact job URL first, then normalized company + title + location.
- Never delete historical rows from `jobs_registry.csv`.
- If a page fails temporarily, mark it and continue.
- Persist detail to files. Keep chat output short.
- Commit and push only when there are meaningful file changes.

## Relevant titles

High-priority titles:

- Senior Software Engineer
- Staff Software Engineer
- Principal Software Engineer
- Senior Backend Engineer
- Staff Backend Engineer
- Platform Engineer
- Senior Full Stack Engineer
- Senior API Engineer
- Senior Application Engineer
- Senior Node.js Engineer
- Senior TypeScript Engineer

Strong negative titles:

- Intern
- Internship
- Junior
- Student
- Mobile only
- iOS
- Android
- Embedded
- FPGA
- ASIC
- SAP
- Salesforce Admin
- Help Desk
- IT Support

## Files

- `careers/companies_seed.csv`
- `careers/careers_registry.csv`
- `careers/jobs_registry.csv`
- `careers/watchlist.md`
- `careers/rejected.md`
- `careers/notes.md`
- `careers/runs/`

## File responsibilities

### `careers/companies_seed.csv`

Seed list of employers to resolve into real careers pages.

### `careers/careers_registry.csv`

Columns:

`company,careers_url,ats_type,source,last_checked,status,notes`

Allowed `ats_type` values:

- ashby
- greenhouse
- greenhouse-eu
- lever
- workday
- smartrecruiters
- custom
- unknown

Allowed `status` values:

- active
- not_found
- temporary_error
- redirected
- needs_review

### `careers/jobs_registry.csv`

Columns:

`job_url,company,title,location,posted_date,discovered_on,source,careers_url,status`

Allowed `status` values:

- new
- existing
- closed
- filtered_out

## Daily run procedure

1. Read all existing files.
2. For every company in `companies_seed.csv` missing from `careers_registry.csv`:
   - resolve the direct careers page
   - add or update `careers_registry.csv`
3. Re-check all active careers pages in `careers_registry.csv`.
4. Extract current open roles.
5. Filter by title and location rules.
6. Deduplicate against `jobs_registry.csv`.
7. Append net-new rows to `jobs_registry.csv` with `status=new`.
8. Write `careers/runs/run-YYYY-MM-DD.md` with:
   - newly resolved careers pages
   - new relevant jobs
   - pages that failed
   - pages that appear stale or changed
9. Update `watchlist.md`, `rejected.md`, and `notes.md` only if there is a real reason.
10. Commit and push if there were meaningful file changes.

## Final chat output

Keep it short:

- count of new careers pages
- count of new jobs
- bullet list of net-new jobs only
- pages needing manual review
