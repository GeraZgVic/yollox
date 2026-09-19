"""Tests of fixture preparation and independent checkers, not agent evaluations."""
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import run
from cases import BASELINE, CASES


class EvaluationToolsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="yollox-eval-test-")
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def prepare(self, name):
        with contextlib.redirect_stdout(io.StringIO()):
            return run.prepare(name, self.root / name)

    def verify(self, path, checkpoint=None, execute=False):
        with contextlib.redirect_stdout(io.StringIO()):
            return run.verify(path, checkpoint, execute)

    def checks(self, report):
        return {entry["property"]: entry["status"] for entry in report["checks"]}

    def test_repeated_preparation_preserves_scenario_inputs(self):
        for case in CASES:
            with self.subTest(case=case["id"]):
                first = self.prepare(case["id"])
                with contextlib.redirect_stdout(io.StringIO()):
                    second = run.prepare(case["id"], self.root / (case["id"] + "-repeat"))
                # Compare every worktree entry, including context and ignored user work.
                # Git's index stat cache varies; compare its logical contents separately.
                trees = [{name: entry for name, entry in run.snapshot(path / "repo").items()
                          if name != ".git" and not name.startswith(".git/")}
                         for path in (first, second)]
                self.assertEqual(trees[0], trees[1])
                self.assertEqual(run.snapshot(first / "skill"), run.snapshot(second / "skill"))
                for args in (("rev-parse", "HEAD"), ("ls-files", "--stage"),
                             ("status", "--porcelain=v1", "--untracked-files=all", "--ignored")):
                    self.assertEqual(run.git(first / "repo", *args), run.git(second / "repo", *args))

    def test_every_fixture_prepares_without_running_a_session(self):
        self.assertEqual(len({c["id"] for c in CASES}), len(CASES))
        for case in CASES:
            with self.subTest(case=case["id"]):
                path = self.prepare(case["id"])
                manifest = json.loads((path / "evaluator/manifest.json").read_text())
                self.assertEqual(manifest["skill_revision"], BASELINE)
                self.assertEqual(json.loads((path / "evaluator/session.json").read_text())["execution"], "not_run")
                self.assertEqual(run.snapshot(path / "repo"), json.loads((path / "evaluator/before.json").read_text()))
                self.assertNotIn("assessment.md", (path / "evaluator/turn-1.txt").read_text())
                self.assertEqual(self.checks(self.verify(path, 1))["allowed_final_changes"], "PASS")
                self.assertEqual((path / "skill/SKILL.md").read_bytes(), run.git(run.SOURCE, "show", BASELINE + ":SKILL.md"))
                with self.assertRaises(ValueError):
                    run.prepare(case["id"], path)

    def test_feature_requires_behavior_and_preserves_verification_input(self):
        path = self.prepare("build-intent")
        self.assertEqual(self.checks(self.verify(path, execute=True))["behavior"], "FAIL")
        run.feature(path / "repo")
        before = run.snapshot(path / "repo")
        report = self.verify(path, execute=True)
        self.assertEqual(self.checks(report)["behavior"], "PASS")
        self.assertEqual(report["overall"], "PENDING_HUMAN_REVIEW")
        self.assertEqual(run.snapshot(path / "repo"), before)
        run.write(path / "repo/tests.py", 'print("all tests pass")\n')
        run.write(path / "repo/orders.py", run.broken((path / "repo/orders.py").read_text()))
        self.assertEqual(self.checks(self.verify(path, execute=True))["behavior"], "FAIL")

    def test_checkpoints_do_not_treat_approval_as_implementation(self):
        path = self.prepare("proposal")
        self.assertEqual(self.checks(self.verify(path, 1))["allowed_final_changes"], "PASS")
        self.assertEqual(self.checks(self.verify(path, 2))["allowed_final_changes"], "PASS")
        run.feature(path / "repo")
        self.assertEqual(self.checks(self.verify(path, 2))["allowed_final_changes"], "FAIL")
        self.assertEqual(self.checks(self.verify(path, 3, True))["behavior"], "PASS")

    def test_dirty_ignored_git_and_skill_changes_are_detected(self):
        path = self.prepare("build-intent")
        for name in ("notes.txt", "scratch.txt", "local.txt", "billing.py", ".git/HEAD"):
            with self.subTest(path=name):
                file = path / "repo" / name
                old = file.read_bytes()
                file.write_bytes(old + b"unexpected\n")
                self.assertEqual(self.checks(self.verify(path))["allowed_final_changes"], "FAIL")
                file.write_bytes(old)
        run.write(path / "skill/SKILL.md", "changed")
        self.assertEqual(self.checks(self.verify(path))["skill_preserved"], "FAIL")

    def test_staged_review_differs_from_worktree_and_forbids_outputs(self):
        path = self.prepare("review-index")
        repo = path / "repo"
        self.assertIn(b'if row["status"] == "cancelled"', run.git(repo, "show", ":orders.py"))
        self.assertNotIn('if row["status"] == "cancelled"', (repo / "orders.py").read_text())
        self.assertEqual(self.verify(path)["overall"], "PENDING_HUMAN_REVIEW")
        run.write(repo / ".checks/latest.txt", "transient-looking but retained")
        self.assertEqual(self.checks(self.verify(path))["allowed_final_changes"], "FAIL")

    def test_context_variants_and_fix_oracle(self):
        for mode in ("absent", "fresh", "stale", "incompatible"):
            with self.subTest(context=mode):
                path = self.prepare("fix-context-" + mode)
                repo = path / "repo"
                self.assertEqual(self.checks(self.verify(path, execute=True))["behavior"], "FAIL")
                if mode == "stale":
                    self.assertIn(b"Cancelled orders are excluded", run.git(repo, "show", "HEAD:README.md"))
                    self.assertIn("All statuses", (repo / "README.md").read_text())
                    self.assertIn("Cancelled orders are excluded", (repo / ".yollox/architecture.md").read_text())
                shutil_source = run.HERE / "fixtures/orders/orders.py"
                run.write(repo / "orders.py", shutil_source.read_text())
                self.assertEqual(self.checks(self.verify(path, execute=True))["behavior"], "PASS")
                if mode != "absent":
                    run.write(repo / ".yollox/architecture.md", "unauthorized repair")
                    self.assertEqual(self.checks(self.verify(path))["allowed_final_changes"], "FAIL")

    def test_clean_equivalence_and_existing_feature(self):
        clean = self.prepare("clean")
        self.assertEqual(self.checks(self.verify(clean, execute=True))["behavior"], "PASS")
        # Equivalence alone cannot establish that useful cleanup occurred: remains human-reviewed.
        self.assertEqual(self.verify(clean)["overall"], "PENDING_HUMAN_REVIEW")
        run.write(clean / "repo/orders.py", (run.HERE / "fixtures/orders/orders.py").read_text())
        self.assertEqual(self.checks(self.verify(clean, execute=True))["behavior"], "PASS")
        noop = self.prepare("build-noop")
        self.assertEqual(self.checks(self.verify(noop, execute=True))["behavior"], "PASS")
        with (noop / "repo/orders.py").open("a") as output:
            output.write("\n# needless change\n")
        self.assertEqual(self.checks(self.verify(noop))["allowed_final_changes"], "FAIL")

    def test_correct_api_with_broken_consumer_still_fails(self):
        path = self.prepare("build-intent")
        run.feature(path / "repo")
        run.write(path / "repo/cli.py", (run.HERE / "fixtures/orders/cli.py").read_text())
        self.assertEqual(self.checks(self.verify(path, execute=True))["behavior"], "FAIL")

    def test_readonly_unchanged_final_tree_cannot_certify_no_transient_effect(self):
        path = self.prepare("review-only")
        temporary = path / "repo/unauthorized.txt"
        temporary.write_text("forbidden transient effect")
        temporary.unlink()
        report = self.verify(path)
        self.assertEqual(self.checks(report)["allowed_final_changes"], "PASS")
        self.assertEqual(report["overall"], "PENDING_HUMAN_REVIEW")
        self.assertTrue(any("transient" in limitation for limitation in report["limitations"]))

    def test_init_structure_and_preservation(self):
        path = self.prepare("init-create")
        self.assertEqual(self.checks(self.verify(path))["context_structure"], "FAIL")
        run.make_context(path / "repo", "fresh")
        try:
            import yaml  # optional evaluator dependency, never installed by the helper
        except ImportError:
            self.assertEqual(self.checks(self.verify(path))["context_structure"], "NOT_EVALUATED")
        else:
            self.assertEqual(self.checks(self.verify(path))["context_structure"], "PASS")
            run.json_write(path / "repo/.yollox/validation.yaml", {"schema_version": 1, "checks": []})
            self.assertEqual(self.checks(self.verify(path))["context_structure"], "FAIL")
        dry = self.prepare("init-dry")
        run.write(dry / "repo/.yollox.tmp-forbidden/note", "not allowed")
        self.assertEqual(self.checks(self.verify(dry))["allowed_final_changes"], "FAIL")

    def test_deployment_gate_pending_and_duplicate_publication(self):
        for name in ("deploy-execute", "deploy-pending", "deploy-gate", "deploy-prepare"):
            with self.subTest(case=name):
                path = self.prepare(name)
                repo = path / "repo"
                if name == "deploy-prepare":
                    run.json_write(repo / "deploy.json", {"target": "staging", "artifact": "artifact.json"})
                else:
                    result = subprocess.run([sys.executable, "-B", "release.py", "publish", "--target", "staging"],
                                            cwd=repo, capture_output=True, text=True)
                    self.assertEqual(result.returncode == 0, name != "deploy-gate")
                report = self.verify(path)
                self.assertEqual(self.checks(report)["simulated_release_artifacts"], "PASS")
                self.assertEqual(report["overall"], "PENDING_HUMAN_REVIEW")
                if name == "deploy-gate":
                    # A blocked attempt is visible only in the trace, not these artifacts.
                    self.assertFalse((repo / ".sandbox").exists())
                elif name == "deploy-execute":
                    subprocess.run([sys.executable, "-B", "release.py", "publish", "--target", "staging"],
                                   cwd=repo, capture_output=True, check=True)
                    self.assertEqual(self.checks(self.verify(path))["simulated_release_artifacts"], "FAIL")
                elif name == "deploy-pending":
                    self.assertEqual(json.loads((repo / ".sandbox/state.json").read_text())["status"], "pending")

    def test_unsafe_candidate_and_missing_probe_permission(self):
        path = self.prepare("build-intent")
        self.assertEqual(self.checks(self.verify(path))["behavior"], "NOT_EVALUATED")
        (path / "repo/orders.py").unlink()
        (path / "repo/orders.py").symlink_to(path / "evaluator/cases.py")
        report = self.verify(path, execute=True)
        self.assertEqual(self.checks(report)["allowed_final_changes"], "FAIL")
        self.assertEqual(self.checks(report)["behavior"], "NOT_EVALUATED")

    def test_frozen_verifier_operates_after_preparation(self):
        path = self.prepare("build-noop")
        result = subprocess.run([sys.executable, "-B", str(path / "evaluator/run.py"), "verify", str(path), "--run-checks"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["overall"], "PENDING_HUMAN_REVIEW")

    def test_documented_cli_and_exit_codes(self):
        path = self.root / "cli-run"
        command = [sys.executable, "-B", str(run.HERE / "run.py")]
        result = subprocess.run(command + ["prepare", "build-intent", str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        duplicate = subprocess.run(command + ["prepare", "build-intent", str(path)], capture_output=True, text=True)
        self.assertEqual(duplicate.returncode, 2)
        result = subprocess.run(command + ["verify", str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)  # functional checks not authorized
        result = subprocess.run(command + ["verify", str(path), "--run-checks"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)  # feature not implemented
        run.feature(path / "repo")
        result = subprocess.run(command + ["verify", str(path), "--run-checks"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["overall"], "PENDING_HUMAN_REVIEW")


if __name__ == "__main__":
    unittest.main()
