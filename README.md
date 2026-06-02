# RepoSentinel AI

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#requirements)
[![Status](https://img.shields.io/badge/status-MVP-green)](#status)
[![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#safe-use)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Repository security reviewer. Scans a local clone for secrets, insecure configs, vulnerable dependencies, risky Dockerfiles, and surfaces PR-style fix suggestions.

---

## Overview

RepoSentinel AI is a defensive analysis tool that audits a local repository for security issues before code review. It detects hard-coded secrets, dangerous configuration patterns, vulnerable dependency pins, insecure Dockerfile practices, and produces a PR-comment-style risk report ready for handoff to a reviewer.

The current MVP is a Python CLI. A FastAPI + React web dashboard is scaffolded under `apps/` for future development.

## Features

- Secret detection (API keys, private keys, tokens, passwords)
- Dependency vulnerability checks against an offline ruleset
- Dockerfile security audit (root user, latest tags, missing pinned digests)
- Insecure config patterns (debug flags, CORS wildcards, hardcoded URLs)
- AI-style code review explanations
- PR comment preview output for reviewer handoff
- Outputs JSON findings, risk summary, Markdown report, and triage handoff

## Requirements

- Python 3.10 or newer
- Linux, macOS, or Windows
- No third-party Python packages (standard library only)
- Optional: Docker for the demo container

## Installation

```bash
git clone https://github.com/SUDARSHANCHAUDHARI/RepoSentinelAI.git
cd RepoSentinelAI
pip install .
```

This registers the `repo-sentinel` CLI command.

To run without installing:

```bash
python3 main.py --help
```

## Usage

Scan the included sample repository:

```bash
python3 main.py --repo data/samples/repo --out-dir data/reports
```

Generated outputs in `data/reports/`:

- `findings.json` — all detected security issues
- `secrets.json` — hardcoded secrets
- `dependencies.json` — vulnerable / risky dependencies
- `dockerfile.json` — Dockerfile audit findings
- `summary.json` — risk score and severity breakdown
- `pr-comments.md` — PR-style review comments
- `report.md` — full Markdown risk report
- `triage.md` — analyst triage checklist

## Project Structure

```
RepoSentinelAI/
├── apps/
│   ├── api/        FastAPI app scaffold (planned)
│   └── web/        React/Next.js app scaffold (planned)
├── data/
│   ├── samples/    Safe sample repository for demo
│   └── reports/    Example generated output
├── docker/         Dockerfile + compose support
├── docs/           Architecture, security notes, demo
├── scripts/        Setup, seed, run helpers
├── tests/          Unit and integration tests
├── main.py         CLI entrypoint
├── pyproject.toml  Package metadata
└── LICENSE
```

## Testing

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Docker Demo

```bash
docker compose run --rm api
```

## Safe Use

This project is defensive and analysis-focused. Use only on repositories you own or have explicit written permission to scan.

## Status

Working Python CLI MVP. Web dashboard scaffold present but not yet implemented.

## Roadmap

- GitHub App flow for posting real PR comments
- Live CVE / OSV integration
- IaC scanning (Terraform, Kubernetes manifests)
- Custom rule packs per language / framework
- Web dashboard for findings triage

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software with attribution.

## Author

**Sudarshan Chaudhari** — [SudarshanTechLabs](https://github.com/SUDARSHANCHAUDHARI)
Bangkok, Thailand

For inquiries: open an issue on [GitHub](https://github.com/SUDARSHANCHAUDHARI/RepoSentinelAI/issues).
