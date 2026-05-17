"""GitHub client placeholder for future remote scans."""

from __future__ import annotations


def describe_remote(repo: str) -> dict:
    """Return remote metadata placeholder without network access."""
    owner, _, name = repo.partition("/")
    return {"owner": owner, "name": name, "full_name": repo}
