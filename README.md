# RepoSentinel AI

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-MVP-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

GitHub security reviewer MVP for secrets, insecure configs, dependencies, Dockerfiles, and PR-style fix suggestions.

- **Portfolio group:** Product-style SaaS project
- **Status:** MVP implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/RepoSentinelAI
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/RepoSentinelAI`

## MVP Snapshot

This repository includes a working MVP with safe sample data, deterministic detection or analysis logic, local tests, and generated output reports where relevant. It is ready for README/demo polish or deeper product work.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

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

## Roadmap

- Polish sample output screenshots or terminal demos
- Add architecture diagram and deeper implementation notes
- Expand test coverage around edge cases
- Add Docker or local demo workflow where useful
- Prepare `v0.1.0-mvp` release notes
