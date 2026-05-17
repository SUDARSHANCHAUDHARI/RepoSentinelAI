"""Local repository file scanner."""

from __future__ import annotations

from pathlib import Path


SKIP_DIRS = {".git", "node_modules", ".venv", "dist", "build", "__pycache__"}


def scan_files(root: Path) -> list[dict]:
    """Return text files from a repository root."""
    files: list[dict] = []
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        files.append({"path": str(path.relative_to(root)), "content": content})
    return files
