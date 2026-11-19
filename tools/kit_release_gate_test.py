"""Unit tests for tools/kit_release_gate.py — stdlib unittest only.

The gate's git side runs against real scratch repositories (git is a
deterministic local boundary, so it is not mocked); its GitHub side runs
against a PATH-first `gh` stub, so no test ever reaches the network.

Run from the repository root:

    uv run python -m unittest discover -s tools -p "*_test.py"
"""

import contextlib
import importlib.util
import io
import json
import os
import shlex
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

# tools/ is not a package; load the module under test by file path so
# `python -m unittest discover -s tools` works without __init__.py.
_MODULE_PATH = Path(__file__).resolve().parent / "kit_release_gate.py"
_SPEC = importlib.util.spec_from_file_location("kit_release_gate", _MODULE_PATH)
kit_release_gate = importlib.util.module_from_spec(_SPEC)
sys.modules["kit_release_gate"] = kit_release_gate
_SPEC.loader.exec_module(kit_release_gate)

REPO_ROOT = Path(__file__).resolve().parent.parent
ISSUE = 35
# The manifest copy-list of the scratch gate repositories: a directory
# entry, file entries, and the kit version file itself.
KIT_PATHS = [".agents/skills/", "AGENTS.md", ".metadex-kit", "KIT-MANIFEST.yaml"]
KIT_VERSION_FILE = "# scratch kit version file\nversion: {version}\ncli: 1.16.0\n"
# The approved scratch area for the real git repositories the suite builds.
SCRATCH_DIR = Path("/tmp/opencode")


def scratch_dir() -> tempfile.TemporaryDirectory:
    """A temporary directory under the approved scratch area."""
    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)
    return tempfile.TemporaryDirectory(dir=SCRATCH_DIR)


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def make_repo(root: Path) -> Path:
    repo = root / "repo"
    repo.mkdir()
    run_git(repo, "init")
    run_git(repo, "config", "user.email", "gate-test@example.com")
    run_git(repo, "config", "user.name", "Gate Test")
    return repo


def commit_file(repo: Path, path: str, content: str, message: str) -> str:
    target = repo / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    run_git(repo, "add", "-A")
    run_git(repo, "commit", "-m", message)
    return run_git(repo, "rev-parse", "HEAD").strip()


def commit_empty(repo: Path, message: str, body: str | None = None) -> str:
    args = ["commit", "--allow-empty", "-m", message]
    if body is not None:
        args += ["-m", body]
    run_git(repo, *args)
    return run_git(repo, "rev-parse", "HEAD").strip()


def seed_gate_repo(root: Path) -> Path:
    """A scratch repository with a committed manifest and kit version file."""
    repo = make_repo(root)
    manifest = ["kit: test\n", "paths:\n"]
    manifest += [f'  "{path}": kit-owned\n' for path in KIT_PATHS]
    (repo / "KIT-MANIFEST.yaml").write_text("".join(manifest), encoding="utf-8")
    (repo / ".metadex-kit").write_text(
        KIT_VERSION_FILE.format(version="1.0.0"), encoding="utf-8"
    )
    run_git(repo, "add", "-A")
    run_git(repo, "commit", "-m", "chore: seed the scratch kit (#99)")
    return repo


def install_gh_stub(
    bin_dir: Path, *, tags: list[str] | None, marker: Path | None = None
) -> None:
    """Write an executable ``gh`` stub into ``bin_dir``.

    With ``tags`` the stub answers ``gh release list --json tagName`` with
    exactly those published tags; with ``tags=None`` it records its
    invocation on ``marker`` and fails, for gate runs that must not
    consult releases at all. Every invocation is recorded on ``marker``.
    """
    lines = ["#!/bin/sh"]
    if marker is not None:
        lines.append(f'echo "$@" >> {shlex.quote(str(marker))}')
    if tags is None:
        lines.append(
            'echo "gh was invoked by a gate run that must not consult releases" >&2'
        )
        lines.append("exit 99")
    else:
        payload = json.dumps([{"tagName": name} for name in tags])
        lines.append(f"echo {shlex.quote(payload)}")
    stub = bin_dir / "gh"
    stub.write_text("\n".join(lines) + "\n", encoding="utf-8")
    stub.chmod(0o755)


@contextlib.contextmanager
def gh_first_on_path(bin_dir: Path):
    """Prepend ``bin_dir`` to PATH so the ``gh`` stub resolves first."""
    path = f"{bin_dir}{os.pathsep}{os.environ.get('PATH', '')}"
    with mock.patch.dict(os.environ, {"PATH": path}):
        yield


def run_gate_captured(issue: int, repo: Path) -> tuple[int, str]:
    """Run the gate and return its exit code and captured stdout."""
    with contextlib.redirect_stdout(io.StringIO()) as out:
        code = kit_release_gate.run_gate(issue, repo)
    return code, out.getvalue()


class LoadKitPathsTest(unittest.TestCase):
    def test_returns_the_manifests_quoted_path_keys_in_order(self):
        paths = kit_release_gate.load_kit_paths(REPO_ROOT / "KIT-MANIFEST.yaml")
        self.assertEqual(
            paths,
            [
                ".agents/skills/",
                ".opencode/commands/",
                ".opencode/skills/",
                ".opencode/agent/",
                "openspec/schemas/intent-driven/",
                "AGENTS.md",
                "docs/intent-prompt-guidelines.md",
                ".github/workflows/validate.yml",
                ".github/ISSUE_TEMPLATE/",
                ".metadex-kit",
                "KIT-MANIFEST.yaml",
            ],
        )

    def test_stops_collecting_at_the_next_top_level_key(self):
        with scratch_dir() as tmp:
            manifest = Path(tmp) / "KIT-MANIFEST.yaml"
            manifest.write_text(
                "kit: test\n"
                "paths:\n"
                '  ".agents/skills/": kit-owned\n'
                '  "AGENTS.md": merge-guidance\n'
                "classes:\n"
                '  "not-a-kit-path": kit-owned\n',
                encoding="utf-8",
            )
            paths = kit_release_gate.load_kit_paths(manifest)
        self.assertEqual(paths, [".agents/skills/", "AGENTS.md"])

    def test_fails_loudly_when_the_manifest_is_missing(self):
        with scratch_dir() as tmp:
            manifest = Path(tmp) / "KIT-MANIFEST.yaml"
            with self.assertRaises(kit_release_gate.KitReleaseGateError):
                kit_release_gate.load_kit_paths(manifest)

    def test_fails_loudly_when_the_manifest_has_no_paths_block(self):
        with scratch_dir() as tmp:
            manifest = Path(tmp) / "KIT-MANIFEST.yaml"
            manifest.write_text(
                "kit: test\n" "classes:\n" '  "x": kit-owned\n', encoding="utf-8"
            )
            with self.assertRaises(kit_release_gate.KitReleaseGateError):
                kit_release_gate.load_kit_paths(manifest)

    def test_fails_loudly_when_the_paths_block_has_no_readable_keys(self):
        with scratch_dir() as tmp:
            manifest = Path(tmp) / "KIT-MANIFEST.yaml"
            manifest.write_text(
                "kit: test\n" "paths:\n" "classes:\n" '  "x": kit-owned\n',
                encoding="utf-8",
            )
            with self.assertRaises(kit_release_gate.KitReleaseGateError):
                kit_release_gate.load_kit_paths(manifest)


class FindChangeCommitsTest(unittest.TestCase):
    def test_finds_commits_whose_subject_ends_with_the_issue_suffix(self):
        with scratch_dir() as tmp:
            repo = make_repo(Path(tmp))
            commit_empty(repo, "chore: root")
            expected = commit_file(
                repo, ".agents/skills/a.md", "a\n", "feat: add skill (#35)"
            )
            commit_empty(repo, "fix: elsewhere (#36)")
            found = kit_release_gate.find_change_commits(repo, ISSUE)
        self.assertEqual(found, [expected])

    def test_ignores_a_commit_mentioning_the_issue_only_in_its_body(self):
        with scratch_dir() as tmp:
            repo = make_repo(Path(tmp))
            commit_empty(repo, "chore: root")
            commit_empty(
                repo,
                "feat: unrelated work",
                "The body mentions (#35) but the subject does not.",
            )
            found = kit_release_gate.find_change_commits(repo, ISSUE)
        self.assertEqual(found, [])

    def test_ignores_commits_of_other_changes(self):
        with scratch_dir() as tmp:
            repo = make_repo(Path(tmp))
            commit_empty(repo, "chore: root")
            commit_empty(repo, "feat: elsewhere (#36)")
            found = kit_release_gate.find_change_commits(repo, ISSUE)
        self.assertEqual(found, [])

    def test_does_not_match_a_subject_suffixed_with_a_longer_issue_number(self):
        with scratch_dir() as tmp:
            repo = make_repo(Path(tmp))
            commit_empty(repo, "chore: root")
            commit_empty(repo, "feat: bigger change (#133)")
            self.assertEqual(kit_release_gate.find_change_commits(repo, 13), [])
            self.assertEqual(
                len(kit_release_gate.find_change_commits(repo, 133)), 1
            )


class KitTouchingCommitsTest(unittest.TestCase):
    def test_collects_a_commit_touching_a_file_inside_a_directory_entry(self):
        with scratch_dir() as tmp:
            repo = make_repo(Path(tmp))
            commit_empty(repo, "chore: root")
            commit = commit_file(
                repo, ".agents/skills/new.md", "new\n", "feat: add skill (#35)"
            )
            touching = kit_release_gate.kit_touching_commits(
                repo, [commit], [".agents/skills/"]
            )
        self.assertEqual(touching, [commit])

    def test_collects_a_commit_touching_a_file_entry_by_equality(self):
        with scratch_dir() as tmp:
            repo = make_repo(Path(tmp))
            commit_empty(repo, "chore: root")
            commit = commit_file(repo, "AGENTS.md", "rules\n", "docs: rules (#35)")
            touching = kit_release_gate.kit_touching_commits(
                repo, [commit], [".agents/skills/", "AGENTS.md"]
            )
        self.assertEqual(touching, [commit])

    def test_skips_a_non_kit_commit_of_the_change_despite_interleaved_kit_commits(self):
        with scratch_dir() as tmp:
            repo = make_repo(Path(tmp))
            commit_empty(repo, "chore: root")
            kit_commit = commit_file(
                repo, ".agents/skills/a.md", "a\n", "feat: add skill (#35)"
            )
            commit_file(repo, ".agents/skills/b.md", "b\n", "fix: other change (#36)")
            commit_file(repo, "src/app.py", "app\n", "feat: app feature (#35)")
            commits = kit_release_gate.find_change_commits(repo, ISSUE)
            touching = kit_release_gate.kit_touching_commits(
                repo, commits, [".agents/skills/"]
            )
        self.assertEqual(set(touching), {kit_commit})

    def test_ignores_a_path_sharing_a_directory_prefix_without_its_slash(self):
        with scratch_dir() as tmp:
            repo = make_repo(Path(tmp))
            commit_empty(repo, "chore: root")
            commit = commit_file(
                repo, ".agents/skills-extra/tool.md", "x\n", "feat: extra (#35)"
            )
            touching = kit_release_gate.kit_touching_commits(
                repo, [commit], [".agents/skills/"]
            )
        self.assertEqual(touching, [])

    def test_diffs_a_merge_commit_against_its_first_parent(self):
        with scratch_dir() as tmp:
            repo = make_repo(Path(tmp))
            commit_file(repo, "README.md", "readme\n", "chore: root")
            main_branch = run_git(repo, "branch", "--show-current").strip()
            run_git(repo, "checkout", "-b", "feature")
            commit_file(
                repo, ".agents/skills/new.md", "new\n", "feat: add skill (#35)"
            )
            run_git(repo, "checkout", main_branch)
            commit_file(repo, "notes.md", "notes\n", "chore: advance main (#36)")
            run_git(
                repo, "merge", "--no-ff", "feature", "-m", "chore: merge feature (#35)"
            )
            merge = run_git(repo, "rev-parse", "HEAD").strip()
            touching = kit_release_gate.kit_touching_commits(
                repo, [merge], [".agents/skills/"]
            )
        self.assertEqual(touching, [merge])


class PublishedReleaseTagsTest(unittest.TestCase):
    def test_returns_the_tag_names_gh_reports(self):
        with scratch_dir() as tmp:
            root = Path(tmp)
            bin_dir = root / "bin"
            bin_dir.mkdir()
            install_gh_stub(bin_dir, tags=["v1.2.0", "v1.0.0"])
            with gh_first_on_path(bin_dir):
                tags = kit_release_gate.published_release_tags(root)
        self.assertEqual(sorted(tags), ["v1.0.0", "v1.2.0"])

    def test_fails_loudly_when_gh_fails(self):
        with scratch_dir() as tmp:
            root = Path(tmp)
            bin_dir = root / "bin"
            bin_dir.mkdir()
            install_gh_stub(bin_dir, tags=None)
            with gh_first_on_path(bin_dir):
                with self.assertRaises(
                    kit_release_gate.KitReleaseGateError
                ) as raised:
                    kit_release_gate.published_release_tags(root)
        self.assertIn("gh", str(raised.exception))


class ContainmentTest(unittest.TestCase):
    def test_a_tag_pointing_directly_at_the_commit_contains_it(self):
        with scratch_dir() as tmp:
            repo = make_repo(Path(tmp))
            commit = commit_empty(repo, "feat: add skill (#35)")
            run_git(repo, "tag", "v1.0.0")
            uncontained = kit_release_gate.uncontained_commits(
                repo, [commit], ["v1.0.0"]
            )
        self.assertEqual(uncontained, [])

    def test_a_commit_after_every_published_tag_is_not_contained(self):
        with scratch_dir() as tmp:
            repo = make_repo(Path(tmp))
            commit_empty(repo, "chore: seed")
            run_git(repo, "tag", "v1.0.0")
            commit = commit_empty(repo, "feat: add skill (#35)")
            uncontained = kit_release_gate.uncontained_commits(
                repo, [commit], ["v1.0.0"]
            )
        self.assertEqual(uncontained, [commit])

    def test_each_commit_may_be_contained_by_a_different_tag(self):
        with scratch_dir() as tmp:
            repo = make_repo(Path(tmp))
            first = commit_empty(repo, "feat: first increment (#35)")
            run_git(repo, "tag", "v1.0.0")
            second = commit_empty(repo, "feat: second increment (#35)")
            run_git(repo, "tag", "v1.1.0")
            uncontained = kit_release_gate.uncontained_commits(
                repo, [first, second], ["v1.0.0", "v1.1.0"]
            )
        self.assertEqual(uncontained, [])


class GatePassTest(unittest.TestCase):
    def test_passes_without_consulting_gh_when_no_commit_touches_kit_paths(self):
        with scratch_dir() as tmp:
            root = Path(tmp)
            repo = seed_gate_repo(root)
            commit_file(repo, "src/app.py", "app\n", "feat: app feature (#35)")
            bin_dir = root / "bin"
            bin_dir.mkdir()
            marker = root / "gh-invoked"
            install_gh_stub(bin_dir, tags=None, marker=marker)
            with gh_first_on_path(bin_dir):
                code, output = run_gate_captured(ISSUE, repo)
        self.assertEqual(code, 0)
        self.assertIn("PASS", output)
        self.assertIn("no kit paths touched", output)
        self.assertFalse(marker.exists())

    def test_passes_naming_the_release_when_kit_commits_are_contained(self):
        with scratch_dir() as tmp:
            root = Path(tmp)
            repo = seed_gate_repo(root)
            commit_file(
                repo, ".agents/skills/new.md", "new\n", "feat: add skill (#35)"
            )
            run_git(repo, "tag", "v1.0.0")
            bin_dir = root / "bin"
            bin_dir.mkdir()
            install_gh_stub(bin_dir, tags=["v1.0.0"])
            with gh_first_on_path(bin_dir):
                code, output = run_gate_captured(ISSUE, repo)
        self.assertEqual(code, 0)
        self.assertIn("PASS", output)
        self.assertIn("v1.0.0", output)


class GateFailTest(unittest.TestCase):
    def test_fails_with_the_bump_fix_when_head_equals_the_latest_release_version(self):
        with scratch_dir() as tmp:
            root = Path(tmp)
            repo = seed_gate_repo(root)
            run_git(repo, "tag", "v1.0.0")
            commit_file(
                repo, ".agents/skills/new.md", "new\n", "feat: add skill (#35)"
            )
            bin_dir = root / "bin"
            bin_dir.mkdir()
            install_gh_stub(bin_dir, tags=["v1.0.0"])
            with gh_first_on_path(bin_dir):
                code, output = run_gate_captured(ISSUE, repo)
        self.assertNotEqual(code, 0)
        self.assertIn("FAIL", output)
        self.assertIn("bump the kit version file, merge, and the release cuts", output)

    def test_fails_with_the_rerun_fix_when_head_is_newer_than_the_latest_release(self):
        with scratch_dir() as tmp:
            root = Path(tmp)
            repo = seed_gate_repo(root)
            run_git(repo, "tag", "v1.0.0")
            commit_file(
                repo, ".agents/skills/new.md", "new\n", "feat: add skill (#35)"
            )
            commit_file(
                repo,
                ".metadex-kit",
                KIT_VERSION_FILE.format(version="1.1.0"),
                "chore: release v1.1.0 (#35)",
            )
            bin_dir = root / "bin"
            bin_dir.mkdir()
            install_gh_stub(bin_dir, tags=["v1.0.0"])
            with gh_first_on_path(bin_dir):
                code, output = run_gate_captured(ISSUE, repo)
        self.assertNotEqual(code, 0)
        self.assertIn("FAIL", output)
        self.assertIn("wait for a running release", output)
        self.assertIn("workflow_dispatch", output)
        self.assertNotIn(
            "bump the kit version file, merge, and the release cuts", output
        )

    def test_fails_with_the_bump_fix_when_no_releases_are_published_at_all(self):
        with scratch_dir() as tmp:
            root = Path(tmp)
            repo = seed_gate_repo(root)
            commit_file(
                repo, ".agents/skills/new.md", "new\n", "feat: add skill (#35)"
            )
            bin_dir = root / "bin"
            bin_dir.mkdir()
            install_gh_stub(bin_dir, tags=[])
            with gh_first_on_path(bin_dir):
                code, output = run_gate_captured(ISSUE, repo)
        self.assertNotEqual(code, 0)
        self.assertIn("FAIL", output)
        self.assertIn("bump the kit version file, merge, and the release cuts", output)

    def test_a_manually_pushed_tag_without_a_release_does_not_satisfy_the_gate(self):
        with scratch_dir() as tmp:
            root = Path(tmp)
            repo = seed_gate_repo(root)
            run_git(repo, "tag", "v1.0.0")
            commit_file(
                repo, ".agents/skills/new.md", "new\n", "feat: add skill (#35)"
            )
            run_git(repo, "tag", "v1.1.0")
            bin_dir = root / "bin"
            bin_dir.mkdir()
            install_gh_stub(bin_dir, tags=["v1.0.0"])
            with gh_first_on_path(bin_dir):
                code, output = run_gate_captured(ISSUE, repo)
        self.assertNotEqual(code, 0)
        self.assertIn("FAIL", output)
        self.assertNotIn("PASS", output)


class MainTest(unittest.TestCase):
    def test_exits_2_with_usage_when_the_issue_number_is_missing(self):
        with contextlib.redirect_stderr(io.StringIO()) as errors:
            with self.assertRaises(SystemExit) as raised:
                kit_release_gate.main([])
        self.assertEqual(raised.exception.code, 2)
        self.assertIn("usage", errors.getvalue())

    def test_exits_2_with_usage_when_the_issue_number_is_not_numeric(self):
        with self.assertRaises(SystemExit) as raised:
            kit_release_gate.main(["not-a-number"])
        self.assertEqual(raised.exception.code, 2)

    def test_runs_the_gate_against_the_current_working_directory(self):
        with scratch_dir() as tmp:
            root = Path(tmp)
            repo = seed_gate_repo(root)
            commit_file(repo, "src/app.py", "app\n", "feat: app feature (#35)")
            bin_dir = root / "bin"
            bin_dir.mkdir()
            marker = root / "gh-invoked"
            install_gh_stub(bin_dir, tags=None, marker=marker)
            previous = Path.cwd()
            os.chdir(repo)
            try:
                with gh_first_on_path(bin_dir):
                    with contextlib.redirect_stdout(io.StringIO()) as out:
                        code = kit_release_gate.main([str(ISSUE)])
            finally:
                os.chdir(previous)
        self.assertEqual(code, 0)
        self.assertIn("PASS", out.getvalue())
        self.assertFalse(marker.exists())


if __name__ == "__main__":
    unittest.main()
