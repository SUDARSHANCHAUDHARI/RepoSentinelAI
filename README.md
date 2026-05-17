# RepoSentinel AI

**Goal:** GitHub security reviewer.

**MVP:** Connect repo, scan files, show security findings.

## Core Features

- secret scanning
- insecure config detection
- dependency review
- Dockerfile issues
- AI fix suggestions
- PR comments

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

## MVP Capabilities

- Scans local repository files.
- Detects committed secret-like values.
- Flags unpinned Python dependencies.
- Flags Dockerfile `latest` base images and missing non-root users.
- Generates deterministic fix suggestions.
- Writes JSON findings, JSON suggestions, and a Markdown PR-style review comment.

## Repository Status

This repository contains the production-ready foundation for the RepoSentinel AI MVP. The current codebase is scaffolded and ready for focused implementation work.

## Production Foundation

- Private GitHub repository linked to `main`
- Initial MVP scaffold committed
- CI repository-health workflow
- Security policy
- Contribution guide
- Pull request and issue templates
- Production readiness checklist
- Safe ignore rules for local secrets and generated files
