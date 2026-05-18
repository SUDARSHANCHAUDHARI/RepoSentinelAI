"""Tests for RepoSentinel AI MVP."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from apps.api.app.cli import analyze_repo
from apps.api.app.services.risk_report import build_triage_report, summarize


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
        self.assertNotIn("AKIAIOSFODNN7EXAMPLE", str(findings))

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
            summary = json.loads(Path(tmp, "summary.json").read_text(encoding="utf-8"))
            comment = Path(tmp, "review-comment.md").read_text(encoding="utf-8")
            triage = Path(tmp, "triage.md").read_text(encoding="utf-8")
            self.assertIn("Generated", result.stdout)
            self.assertGreaterEqual(len(findings), 4)
            self.assertEqual("critical", findings[0]["severity"])
            self.assertEqual("high", summary["risk_level"])
            self.assertIn("RepoSentinel AI Security Review", comment)
            self.assertIn("Remediation Checklist", triage)

    def test_builds_summary_and_triage(self) -> None:
        findings, suggestions = analyze_repo(SAMPLE)
        summary = summarize(findings)
        triage = build_triage_report(findings, suggestions)

        self.assertEqual(4, summary["findings"])
        self.assertIn("secret", summary["by_category"])
        self.assertIn("RepoSentinel AI Triage", triage)


if __name__ == "__main__":
    unittest.main()
