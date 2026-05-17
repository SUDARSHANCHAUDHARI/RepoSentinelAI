"""Build PR-style security review comments."""

from __future__ import annotations


def build_review_comment(suggestions: list[dict]) -> str:
    """Return a Markdown review comment."""
    lines = ["# RepoSentinel AI Security Review", ""]
    if not suggestions:
        lines.append("No security findings detected.")
        return "\n".join(lines) + "\n"
    for item in suggestions:
        finding = item["finding"]
        evidence = finding.get("evidence", {})
        lines.extend(
            [
                f"## {finding['summary']}",
                "",
                f"- Severity: `{finding['severity']}`",
                f"- Type: `{finding['kind']}`",
                f"- Path: `{evidence.get('path', 'unknown')}`",
                f"- Suggestion: {item['suggestion']}",
                "",
            ]
        )
    return "\n".join(lines)
