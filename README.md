# career-targets

Source of truth for job site targets used by career-ops automation.

## Purpose

This repo contains `portals.yml` — the configuration file that defines:
- Job title filters (what roles to target / exclude)
- Search queries across job boards (LinkedIn, Greenhouse, Ashby, Lever, Wellfound, etc.)
- Tracked companies with their career page URLs

This repo is cloned by career-ops installations and serves as the central, version-controlled list of job sites to scan.

## Usage

In your career-ops installation, add this as a git submodule or clone it alongside your career-ops repo:

```bash
# Option 1: Git submodule
cd career-ops
git submodule add https://github.com/opsclawd/career-targets.git targets
ln -sf targets/portals.yml portals.yml

# Option 2: Clone directly
git clone https://github.com/opsclawd/career-targets.git
cp career-targets/portals.yml .
```

Then customize `portals.yml` for your needs and push changes back to this repo.

## Cron Job

A daily cron job runs to update and compile the job site list from this repo. See `.github/workflows/daily-sync.yml` for details.

## Contributing

1. Edit `portals.yml` to add/remove job sites or adjust filters
2. Commit and push changes
3. The daily cron will pick up the updates automatically

## File Structure

```
career-targets/
├── portals.yml          # Main config file
├── README.md            # This file
└── .github/
    └── workflows/
        └── daily-sync.yml  # Daily cron job workflow
```
