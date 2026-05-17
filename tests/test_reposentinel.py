"""Tests for RepoSentinel AI MVP."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from apps.api.app.cli import analyze_repo


ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "data/samples/repo"


class RepoSentinelTests(unittest.TestCase):
    def test_detects_repo_findings(self) -> None:
        findings, suggestions = analyze_repo(SAMPLE)
        kinds = {finding["kind"] for finding in findings}

        self.assertIn("secret.aws_access_key", kinds)
        self.assertIn("dependency.unpinned_python", kinds)
        self.assertIn("docker.latest_base", kinds)
        self.assertIn("docker.root_user", kinds)
        self.assertEqual(len(suggestions), len(findings))

    def test_cli_writes_review_comment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, "-m", "apps.api.app.cli", "--repo", str(SAMPLE), "--out-dir", tmp],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            findings = json.loads(Path(tmp, "findings.json").read_text(encoding="utf-8"))
            comment = Path(tmp, "review-comment.md").read_text(encoding="utf-8")
            self.assertIn("Generated", result.stdout)
            self.assertGreaterEqual(len(findings), 4)
            self.assertIn("RepoSentinel AI Security Review", comment)


if __name__ == "__main__":
    unittest.main()
