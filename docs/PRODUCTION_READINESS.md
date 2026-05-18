# Production Readiness

## Current Status

This repository has a working offline product MVP with deterministic local repo scanning, redacted findings, risk summary, PR comment output, triage output, tests, and generated reports. It is portfolio-ready but not production complete yet.

## Required Before Public Release

- Add GitHub authorization before scanning private repositories.
- Add tests for binary files, large files, and malformed manifests.
- Validate all untrusted inputs.
- Add structured logging without leaking secrets.
- Document local setup and deployment.
- Review all sample data for sensitive content.
- Add authentication and authorization before handling user repository data.
- Run dependency and secret scans before release.
- Add suppression review and audit logs.

## Definition of Done

- CI passes on pull requests.
- README has setup, usage, and security notes.
- Sample data is safe to publish.
- Error paths are handled clearly.
- No secrets or local machine paths are committed.
- Reports redact sensitive previews and include triage guidance.
