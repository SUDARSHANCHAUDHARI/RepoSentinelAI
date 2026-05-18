# Architecture

RepoSentinel AI is a defensive repository security reviewer.

## Flow

1. `repo_scanner.py` reads local repository text files.
2. `secret_detector.py` detects credential-like material and redacts evidence previews.
3. `dependency_checker.py` checks dependency and Dockerfile risks.
4. `ai_code_reviewer.py` attaches deterministic fix suggestions.
5. `risk_report.py` builds summary, risk report, and triage checklist outputs.
6. `pr_commenter.py` generates a PR-style review comment.

## Outputs

- findings JSON
- suggestions JSON
- summary JSON
- Markdown risk report
- Markdown triage checklist
- Markdown PR review comment

The MVP scans local fixtures only and does not call GitHub APIs.
