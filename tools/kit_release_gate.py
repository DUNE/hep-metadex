"""Maintainer toolchain archive-phase gate for kit release discipline.

The archive phase runs this gate before archiving a change and refuses on
failure. It finds the change's commits on ``main`` by their
conventional-commit ``(#N)`` subject suffix, diffs each commit against
its first parent restricted to the ``KIT-MANIFEST.yaml`` ``paths:``
copy-list, and requires every kit-touching commit to be an ancestor of a
tag belonging to a published release (``gh release list``, never bare
``git tag``). With no kit-touching commits it passes without consulting
releases; on failure it prints the diagnosed cause and its pasteable fix.

Usage (from the repository root):

    uv run tools/kit_release_gate.py <issue-number>
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

MANIFEST_NAME = "KIT-MANIFEST.yaml"
KIT_VERSION_FILE_NAME = ".metadex-kit"

FORGOTTEN_BUMP_FIX = (
    "Fix: bump the kit version file, merge, and the release cuts — the new "
    "release will contain this change's kit changes."
)
RELEASE_MISFIRE_FIX = (
    "Fix: wait for a running release to finish; otherwise re-run the "
    "release workflow via workflow_dispatch. Do not bump the version a "
    "second time — the bump is already merged, and a second one would "
    "scope the release wrong."
)

# An indented, quoted key of a `paths:` entry: `".agents/skills/": kit-owned`.
_QUOTED_PATH_KEY = re.compile(r'^\s+"([^"]+)"\s*:')
# A release tag or kit version: `v1.16.0` or `1.16.0`.
_SEMVER = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)$")
_KIT_VERSION_LINE = re.compile(r"^version:\s*(\S+)\s*$", re.MULTILINE)


class KitReleaseGateError(Exception):
    """A user-facing failure: unreadable inputs or a failing boundary."""


def _git(repo: Path, *args: str) -> str:
    """Run a git command in ``repo`` and return its stdout, failing loudly."""
    result = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise KitReleaseGateError(
            f"git {' '.join(args)} failed in {repo}: {result.stderr.strip()}"
        )
    return result.stdout


def load_kit_paths(manifest_path: Path) -> list[str]:
    """Return the manifest's quoted ``paths:`` keys, in file order.

    Collection starts at the top-level ``paths:`` key and stops at the
    next top-level key. A manifest with no readable keys is an error —
    the gate fails loudly rather than silently treating every path as
    non-kit.
    """
    if not manifest_path.is_file():
        raise KitReleaseGateError(
            f"kit manifest not found: {manifest_path} — the gate needs the "
            "paths: copy-list to decide kit containment"
        )
    paths: list[str] = []
    in_paths_block = False
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line[0].isspace():
            in_paths_block = line.split(":", 1)[0].strip() == "paths"
            continue
        if not in_paths_block:
            continue
        key = _QUOTED_PATH_KEY.match(line)
        if key is None:
            raise KitReleaseGateError(
                f"cannot read a paths: entry in {manifest_path}: "
                f"{line.strip()!r}"
            )
        paths.append(key.group(1))
    if not paths:
        raise KitReleaseGateError(
            f"{manifest_path} has no readable paths: entries — the gate "
            "cannot decide kit containment without the copy-list"
        )
    return paths


def find_change_commits(repo: Path, issue: int) -> list[str]:
    """Return the hashes of the change's commits reachable from ``HEAD``.

    A commit belongs to the change when its subject ends with the
    conventional ``(#N)`` suffix for the issue number; a body that merely
    mentions ``(#N)`` does not count.
    """
    suffix = re.compile(rf"\(#{issue}\)$")
    commits: list[str] = []
    for entry in _git(repo, "log", "--format=%H%x1f%s").splitlines():
        if not entry:
            continue
        commit_hash, _, subject = entry.partition("\x1f")
        if suffix.search(subject):
            commits.append(commit_hash)
    return commits


def kit_touching_commits(
    repo: Path, commits: list[str], kit_paths: list[str]
) -> list[str]:
    """Return the commits whose first-parent diff touches a manifest path.

    Each commit is diffed against its own first parent (``<commit>^``),
    the semantics that show what a merge introduced on ``main``, so
    commits from other changes interleaved on ``main`` cannot pollute the
    set. File entries match by equality; directory entries (trailing
    slash) match their subtrees.
    """
    touching: list[str] = []
    for commit in commits:
        changed = _git(
            repo, "diff", "--name-only", f"{commit}^", commit
        ).splitlines()
        if any(_is_kit_path(path, kit_paths) for path in changed):
            touching.append(commit)
    return touching


def _is_kit_path(path: str, kit_paths: list[str]) -> bool:
    for entry in kit_paths:
        if entry.endswith("/"):
            if path.startswith(entry):
                return True
        elif path == entry:
            return True
    return False


def published_release_tags(repo: Path) -> list[str]:
    """Return the tags of published releases via ``gh release list``.

    Published releases are the only containment witness: a tag pushed to
    git without a release does not appear here and does not satisfy the
    gate.
    """
    result = subprocess.run(
        ["gh", "release", "list", "--json", "tagName"],
        cwd=str(repo),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise KitReleaseGateError(
            "gh release list failed — the gate consults published releases "
            f"through the GitHub CLI: {result.stderr.strip()}"
        )
    try:
        payload = json.loads(result.stdout)
        return [entry["tagName"] for entry in payload]
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        raise KitReleaseGateError(
            f"gh release list returned unparseable output: {result.stdout!r}"
        ) from error


def uncontained_commits(
    repo: Path, commits: list[str], release_tags: list[str]
) -> list[str]:
    """Return the commits that are ancestors of no published release tag."""
    return [
        commit
        for commit in commits
        if not any(_is_ancestor(repo, commit, tag) for tag in release_tags)
    ]


def _is_ancestor(repo: Path, commit: str, tag: str) -> bool:
    result = subprocess.run(
        ["git", "-C", str(repo), "merge-base", "--is-ancestor", commit, tag],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        return True
    if result.returncode == 1:
        return False
    raise KitReleaseGateError(
        f"git merge-base --is-ancestor {commit} {tag} failed: "
        f"{result.stderr.strip()}"
    )


def _semver_key(value: str) -> tuple[int, int, int]:
    """Return the semver triple of a release tag or kit version."""
    match = _SEMVER.match(value)
    if match is None:
        raise KitReleaseGateError(
            f"cannot parse {value!r} as a kit version or release tag (semver)"
        )
    return (int(match.group(1)), int(match.group(2)), int(match.group(3)))


def _kit_version_at(repo: Path, rev: str) -> str:
    """Return the ``version:`` value of the kit version file at ``rev``."""
    content = _git(repo, "show", f"{rev}:{KIT_VERSION_FILE_NAME}")
    match = _KIT_VERSION_LINE.search(content)
    if match is None:
        raise KitReleaseGateError(
            f"{KIT_VERSION_FILE_NAME} at {rev} has no version: line — the "
            "gate needs the kit version for its diagnosis"
        )
    return match.group(1)


def diagnose_failure(repo: Path, release_tags: list[str]) -> tuple[str, str]:
    """Return the ``(cause, fix)`` pair for a containment failure.

    The kit version at the latest published release tag decides the
    cause: equal to ``HEAD`` (or no published releases at all) means the
    bump was forgotten; newer at ``HEAD`` means the bump is merged but no
    release was cut.
    """
    if not release_tags:
        return (
            "no published releases exist yet; the version bump was forgotten",
            FORGOTTEN_BUMP_FIX,
        )
    latest_tag = max(release_tags, key=_semver_key)
    released_version = _kit_version_at(repo, latest_tag)
    head_version = _kit_version_at(repo, "HEAD")
    if _semver_key(head_version) > _semver_key(released_version):
        return (
            f"the kit version at HEAD ({head_version}) is newer than the "
            f"latest published release ({latest_tag} ships {released_version}); "
            "the bump is merged but no release was cut — the release run "
            "misfired or is still in flight",
            RELEASE_MISFIRE_FIX,
        )
    return (
        f"the kit version at HEAD ({head_version}) is not newer than the "
        f"latest published release ({latest_tag} ships {released_version}); "
        "the version bump was forgotten",
        FORGOTTEN_BUMP_FIX,
    )


def run_gate(issue: int, repo: Path) -> int:
    """Run the gate for the change's issue against ``repo``.

    Prints the verdict on stdout and returns the exit code: 0 when the
    change touches no kit paths or all of its kit-touching commits are
    ancestors of published release tags, 1 with the diagnosed cause and
    its pasteable fix otherwise.
    """
    kit_paths = load_kit_paths(repo / MANIFEST_NAME)
    change_commits = find_change_commits(repo, issue)
    kit_commits = kit_touching_commits(repo, change_commits, kit_paths)
    if not kit_commits:
        plural = "s" if len(change_commits) != 1 else ""
        print(
            f"PASS: no kit paths touched by the {len(change_commits)} "
            f"commit{plural} of change #{issue} — no release required."
        )
        return 0
    release_tags = published_release_tags(repo)
    uncontained = uncontained_commits(repo, kit_commits, release_tags)
    plural = "s" if len(kit_commits) != 1 else ""
    verb = "are" if len(kit_commits) != 1 else "is"
    if not uncontained:
        latest_tag = max(release_tags, key=_semver_key)
        print(
            f"PASS: all {len(kit_commits)} kit-touching commit{plural} of "
            f"change #{issue} {verb} contained in published releases "
            f"(latest {latest_tag})."
        )
        return 0
    print(
        f"FAIL: {len(uncontained)} of {len(kit_commits)} kit-touching "
        f"commit{plural} of change #{issue} {verb} not contained in any "
        "published release."
    )
    cause, fix = diagnose_failure(repo, release_tags)
    print(f"Cause: {cause}.")
    print(fix)
    return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="tools/kit_release_gate.py",
        description=(
            "Archive-phase gate for kit release discipline: refuse a change "
            "whose kit changes no published release contains."
        ),
    )
    parser.add_argument(
        "issue",
        type=int,
        help=(
            "issue number of the change being archived (its commits carry "
            "it as the (#N) subject suffix)"
        ),
    )
    args = parser.parse_args(argv)
    try:
        return run_gate(args.issue, Path.cwd())
    except KitReleaseGateError as error:
        print(f"kit_release_gate: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
