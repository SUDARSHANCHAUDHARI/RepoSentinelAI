# RepoSentinel AI

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-product%20polish-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

GitHub security reviewer MVP for secrets, insecure configs, dependencies, Dockerfiles, and PR-style fix suggestions.

- **Portfolio group:** Product-style SaaS project
- **Status:** Product polish implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/RepoSentinelAI
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/RepoSentinelAI`

## MVP Snapshot

This repository includes a working MVP with safe sample repo data, deterministic security checks, redacted evidence, JSON outputs, Markdown risk report, triage checklist, PR-style comment, tests, and Docker demo support.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

## Core Features

- secret scanning
- insecure config detection
- dependency review
- Dockerfile issues
- AI fix suggestions
- PR comments
- risk scoring
- remediation checklist

## Suggested Stack

FastAPI, React, GitHub API, Docker.

## Status

Working CLI MVP.

## Quick Start

Scan the included sample repository:

```bash
python3 -m apps.api.app.cli --repo data/samples/repo --out-dir data/reports
```

Run tests:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

Generated outputs:

- `data/reports/findings.json`
- `data/reports/suggestions.json`
- `data/reports/summary.json`
- `data/reports/risk-report.md`
- `data/reports/triage.md`
- `data/reports/review-comment.md`

## Docker Demo

```bash
docker compose run --rm api
```

## Product Polish Capabilities

- Scans local repository files.
- Detects committed secret-like values.
- Flags unpinned Python dependencies.
- Flags Dockerfile `latest` base images and missing non-root users.
- Generates deterministic fix suggestions.
- Writes JSON findings, JSON suggestions, and a Markdown PR-style review comment.
- Redacts secret evidence and adds risk scoring, category summaries, and triage checklist.

## Roadmap

- Add GitHub App repo connection
- Add SARIF export
- Add inline PR review comments
- Add allow-list and suppression workflow
- Add web dashboard for repo scans
