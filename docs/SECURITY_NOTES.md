# Security Notes

RepoSentinel AI is defensive and review-focused.

## Safe Use

- Scan only repositories you own or have permission to assess.
- Do not commit real secrets, private source, customer repositories, or production scan outputs.
- Treat findings as sensitive because they can reveal vulnerable files and repository structure.

## Current Boundary

The MVP runs locally against safe sample files and does not call GitHub APIs. Secret evidence is redacted in generated findings.

## Before Production

- Add repository authorization and audit logging.
- Add secret redaction for all report paths.
- Add allow-list and suppression review.
- Add rate limits and timeout controls for hosted scans.
