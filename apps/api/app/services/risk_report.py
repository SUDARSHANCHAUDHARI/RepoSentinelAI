"""Build RepoSentinel summary and triage reports."""

from __future__ import annotations

from collections import Counter
import json


POINTS = {"critical": 60, "high": 35, "medium": 15, "low": 5}
SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def sort_findings(findings: list[dict]) -> list[dict]:
    return sorted(findings, key=lambda item: (SEVERITY_ORDER.get(str(item["severity"]), 9), item["kind"]))


def summarize(findings: list[dict]) -> dict[str, object]:
    score = min(100, sum(POINTS.get(str(finding["severity"]), 0) for finding in findings))
    return {
        "findings": len(findings),
        "risk_score": score,
        "risk_level": "high" if score >= 80 else "medium" if score >= 45 else "low",
        "by_severity": dict(Counter(str(finding["severity"]) for finding in findings)),
        "by_category": dict(Counter(str(finding["kind"]).split(".", 1)[0] for finding in findings)),
        "top_priority": sort_findings(findings)[0] if findings else None,
    }


def build_markdown_report(findings: list[dict], suggestions: list[dict]) -> str:
    ordered = sort_findings(findings)
    suggestion_by_kind = {item["finding"]["kind"]: item["suggestion"] for item in suggestions}
    summary = summarize(ordered)
    lines = [
        "# RepoSentinel AI Risk Report",
        "",
        f"- Findings: {summary['findings']}",
        f"- Risk score: {summary['risk_score']}/100",
        f"- Risk level: {summary['risk_level']}",
        "",
        "## Priority Queue",
        "",
    ]
    if not ordered:
        lines.append("No repository security findings were detected.")
    for index, finding in enumerate(ordered, start=1):
        evidence = finding.get("evidence", {})
        lines.extend(
            [
                f"### {index}. {finding['summary']}",
                "",
                f"- Severity: `{finding['severity']}`",
                f"- Type: `{finding['kind']}`",
                f"- Path: `{evidence.get('path', 'unknown')}`",
                f"- Evidence: `{json.dumps(evidence, sort_keys=True)}`",
                f"- Suggested fix: {suggestion_by_kind.get(finding['kind'], 'Review and remediate this finding.')}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def build_triage_report(findings: list[dict], suggestions: list[dict]) -> str:
    ordered = sort_findings(findings)
    suggestion_by_kind = {item["finding"]["kind"]: item["suggestion"] for item in suggestions}
    lines = [
        "# RepoSentinel AI Triage",
        "",
        "## Remediation Checklist",
        "",
    ]
    if not ordered:
        lines.append("No remediation items were generated.")
    for finding in ordered:
        evidence = finding.get("evidence", {})
        lines.append(
            f"- [ ] `{finding['severity']}` {finding['kind']} in `{evidence.get('path', 'unknown')}`: "
            f"{suggestion_by_kind.get(finding['kind'], 'Review and remediate this finding.')}"
        )
    return "\n".join(lines).rstrip() + "\n"
