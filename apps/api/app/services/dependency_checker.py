"""Detect dependency and Dockerfile risks."""

from __future__ import annotations


def check_dependencies(files: list[dict]) -> list[dict]:
    """Return dependency findings."""
    findings: list[dict] = []
    for file in files:
        path = file["path"].lower()
        content = file["content"]
        if path.endswith("requirements.txt"):
            for line_no, line in enumerate(content.splitlines(), start=1):
                stripped = line.strip()
                if stripped and "==" not in stripped and not stripped.startswith("#"):
                    findings.append(
                        {
                            "kind": "dependency.unpinned_python",
                            "severity": "medium",
                            "summary": "Python dependency is not pinned.",
                            "evidence": {"path": file["path"], "line": line_no, "dependency": stripped},
                        }
                    )
        if path.endswith("package.json") and '"latest"' in content:
            findings.append(
                {
                    "kind": "dependency.latest_tag",
                    "severity": "medium",
                    "summary": "package.json uses latest dependency tag.",
                    "evidence": {"path": file["path"]},
                }
            )
        if "dockerfile" in path:
            lowered = content.lower()
            if "from " in lowered and ":latest" in lowered:
                findings.append(
                    {
                        "kind": "docker.latest_base",
                        "severity": "medium",
                        "summary": "Dockerfile uses a latest base image tag.",
                        "evidence": {"path": file["path"]},
                    }
                )
            if "user " not in lowered:
                findings.append(
                    {
                        "kind": "docker.root_user",
                        "severity": "medium",
                        "summary": "Dockerfile does not set a non-root USER.",
                        "evidence": {"path": file["path"]},
                    }
                )
    return findings
