# Tools Guidance

## Preferred tools

Use browser and web-search tools for public career-page discovery and validation.

Use exec or filesystem tools only for:

- reading and writing repo files
- lightweight deduplication or normalization
- preparing run summaries
- committing and pushing changes

## Preferred discovery order

1. direct ATS pattern guess
2. employer careers page
3. public web search for `"<company> careers jobs"`
4. verification of the discovered page
5. extraction of relevant live roles

## Canonical ATS patterns

- Ashby: `https://jobs.ashbyhq.com/{slug}`
- Greenhouse: `https://job-boards.greenhouse.io/{slug}`
- Greenhouse EU: `https://job-boards.eu.greenhouse.io/{slug}`
- Lever: `https://jobs.lever.co/{slug}`

## Guardrails

- Do not treat job aggregators as canonical sources.
- Do not overwrite the CSV headers or column order.
- Do not delete historical rows from the registries.
- Do not create duplicate rows when the job URL already exists.
- Do not claim a careers page is valid unless it clearly contains jobs, listings, or an apply flow.
