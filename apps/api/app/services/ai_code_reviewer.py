"""Generate deterministic fix suggestions."""

from __future__ import annotations


SUGGESTIONS = {
    "secret": "Remove the secret from git history, rotate it, and load it from a secret manager or environment variable.",
    "dependency": "Pin the dependency to a reviewed version and enable dependency scanning.",
    "docker": "Use a pinned base image and run the container as a non-root user.",
}


def suggest_fixes(findings: list[dict]) -> list[dict]:
    """Attach fix suggestions to findings."""
    suggestions: list[dict] = []
    for finding in findings:
        prefix = str(finding["kind"]).split(".", 1)[0]
        suggestions.append(
            {
                "finding": finding,
                "suggestion": SUGGESTIONS.get(prefix, "Review and remediate this security issue."),
            }
        )
    return suggestions
