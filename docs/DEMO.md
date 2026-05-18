# Demo

## Local CLI

```bash
python3 -m apps.api.app.cli --repo data/samples/repo --out-dir data/reports
```

Expected terminal output:

```text
Generated 4 finding(s)
Risk score: 100/100
```

## Review Outputs

```bash
cat data/reports/risk-report.md
cat data/reports/triage.md
cat data/reports/review-comment.md
```

## Docker CLI

```bash
docker compose run --rm api
```
