"""CLI for RepoSentinel AI MVP."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from apps.api.app.services.ai_code_reviewer import suggest_fixes
from apps.api.app.services.dependency_checker import check_dependencies
from apps.api.app.services.pr_commenter import build_review_comment
from apps.api.app.services.repo_scanner import scan_files
from apps.api.app.services.secret_detector import detect_secrets


def analyze_repo(root: Path) -> tuple[list[dict], list[dict]]:
    """Analyze a local repository."""
    files = scan_files(root)
    findings = [*detect_secrets(files), *check_dependencies(files)]
    return findings, suggest_fixes(findings)


def main() -> None:
    parser = argparse.ArgumentParser(description="RepoSentinel AI local repo scanner")
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=Path("data/reports"))
    args = parser.parse_args()

    findings, suggestions = analyze_repo(args.repo)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "findings.json").write_text(json.dumps(findings, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "suggestions.json").write_text(json.dumps(suggestions, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "review-comment.md").write_text(build_review_comment(suggestions), encoding="utf-8")
    print(f"Generated {len(findings)} finding(s)")


if __name__ == "__main__":
    main()
