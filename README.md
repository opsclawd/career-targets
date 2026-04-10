# career-targets

A dedicated OpenClaw workspace and Git-backed state store for ongoing Calgary-focused software engineering job sourcing through direct employer career pages.

## What this repo is for

This repo does four things:

1. Stores the durable career-sourcing pipeline under `careers/`.
2. Stores the prompt files that each OpenClaw cron job reads before it runs.
3. Stores a declarative cron schedule in `cron/jobs.json`.
4. Provides an installer that creates or replaces the cron jobs in OpenClaw from the repo contents.

## Repo layout

```text
.
├── AGENTS.md
├── TOOLS.md
├── MEMORY.md
├── README.md
├── .gitignore
├── config/
│   └── openclaw.example.json
├── cron/
│   ├── jobs.json
│   └── messages/
│       ├── daily-sourcing.txt
│       ├── midday-refresh.txt
│       └── weekly-review.txt
├── careers/
│   ├── companies_seed.csv
│   ├── careers_registry.csv
│   ├── jobs_registry.csv
│   ├── watchlist.md
│   ├── rejected.md
│   ├── notes.md
│   └── runs/
└── scripts/
    └── install_cron.py
```

## Prerequisites

- OpenClaw is installed and the gateway is running.
- This repo is cloned onto the same machine that owns the OpenClaw workspace.
- The repo has a working `origin` remote.
- Git on that machine can push to `origin/main` non-interactively.
- The OpenClaw workspace points at this repo path.

## Configure OpenClaw to use this repo as the workspace

Use `config/openclaw.example.json` as the template and set the workspace to the absolute path of this repo.

Example:

```json
{
  "agent": {
    "workspace": "/absolute/path/to/career-targets",
    "skipBootstrap": true
  }
}
```

## Install or refresh the cron jobs

From the repo root:

```bash
python3 scripts/install_cron.py
```

This script:

- reads `cron/jobs.json`
- removes existing cron jobs with the same names
- recreates them from the current repo files
- preserves OpenClaw as the runtime while keeping this repo as the source of truth

## Manual smoke test

Run one of the installed jobs manually after installation:

```bash
openclaw cron list
openclaw cron run <job-id>
openclaw cron runs --id <job-id> --limit 10
```

## Operating model

- The cron scheduler definition is versioned in this repo.
- The durable career-sourcing state is versioned in this repo.
- The actual installed cron jobs still live in OpenClaw's cron store.
- Each scheduled run must read and update the career files, then commit and push any meaningful changes directly to `origin/main`.

## Daily sourcing model

The agent should:

1. read `careers/companies_seed.csv`
2. resolve canonical direct employer career pages into `careers/careers_registry.csv`
3. inspect those career pages for relevant software-engineering roles
4. append only net-new jobs to `careers/jobs_registry.csv`
5. write a run report under `careers/runs/`
6. commit and push meaningful changes

## Canonical source rules

Canonical `careers_url` values should be direct employer or ATS pages only:

- company careers pages
- Ashby
- Greenhouse
- Lever
- Workday
- SmartRecruiters
- equivalent direct ATS pages

Do not store LinkedIn, Indeed, Eluta, Job Bank, or other aggregator URLs as canonical `careers_url` values.

## Failure modes to avoid

- Do not rely on session memory instead of files.
- Do not let Git auth expire on the gateway host.
- Do not run this repo as a shared general-purpose workspace.
- Do not manually edit OpenClaw's on-disk cron store while the gateway is running.
- Do not let the agent store aggregator URLs as canonical career-page targets.
