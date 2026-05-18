"""Detect committed secret-like material."""

from __future__ import annotations

import re


PATTERNS = (
    ("secret.aws_access_key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("secret.private_key", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")),
    ("secret.bearer_token", re.compile(r"Bearer\s+[A-Za-z0-9._-]{16,}", re.IGNORECASE)),
    ("secret.env_assignment", re.compile(r"(api_key|secret|password)\s*=\s*['\"][^'\"]{8,}['\"]", re.IGNORECASE)),
)


def _redact_preview(line: str) -> str:
    redacted = line
    for _, pattern in PATTERNS:
        redacted = pattern.sub("[REDACTED]", redacted)
    return redacted[:120]


def detect_secrets(files: list[dict]) -> list[dict]:
    """Return secret findings."""
    findings: list[dict] = []
    for file in files:
        for line_no, line in enumerate(file["content"].splitlines(), start=1):
            for kind, pattern in PATTERNS:
                if pattern.search(line):
                    findings.append(
                        {
                            "kind": kind,
                            "severity": "critical",
                            "summary": "File contains credential-like material.",
                            "evidence": {"path": file["path"], "line": line_no, "preview": _redact_preview(line)},
                        }
                    )
                    break
    return findings
