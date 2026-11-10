## Why

Change branches already follow the issue-number-first slug in practice (`17-align-bootstrap-prompt-ci-step`, merged as PR #18) and in the documented lifecycle (`docs/usage.md`), yet the `openspec-git-discipline` skill's "Before propose" gate still says "Prefer `main`" — permitting a change's first commits to land directly on `main`, with the branch offered only after propose — and `CONTRIBUTING.md` still has no branch-naming rule. Because the skill ships in the **workflow scaffolding** every adopting **experiment repository** installs from this **OpenSpec Store**, codifying the gate now keeps the replicated kit, the contributor guidance, and actual practice aligned.

## What Changes

- Require an **issue branch** for every new change: `<issue-number>-<change-slug>` is cut from `main` before the change's first commit, and change work — planning and implementation commits — reaches `main` only by pull-request merge, never by direct commits.
- Amend two gates in `.agents/skills/openspec-git-discipline/SKILL.md`; exact wording is delegated to design:
  - "Before propose" directs cutting the issue branch from `main` before the first commit, replacing "Prefer `main`". The gate is ask-first under the skill's no-auto-git rule (never create commits, branches, or merges unless the user explicitly asks): a decline keeps today's "warn and ask whether to continue intentionally" escape hatch, and refusal semantics are a design constraint.
  - "After propose" opens the PR from the branch that already exists, instead of offering to create one.
- Keep the rest of the discipline unchanged: the core rule (every OpenSpec state change crosses `main` before the next lifecycle phase depends on it), the phase sequence, the apply gate, and the archive gate stay as they are — including the archive phase's direct metadata commit on `main` documented in `docs/usage.md`. The no-auto-git rule remains intact; the new gate directs where work lands, not whether git actions happen without the user's ask.
- Add a divergence-manifest row in `docs/maintainer.md` recording the `openspec-git-discipline` edit as a fork of a vendored skill, following the glossary-fork precedent.
- Add a drift-impact entry in `docs/maintainer.md`: maintainers hand-merge upstream changes into the forked skill and re-apply the two amended gates after any sync — a naive sync silently reverts them.
- Extend `CONTRIBUTING.md`'s pull-request section: "Branch from `main`" gains the `<issue-number>-<change-slug>` naming rule for a change's planning branch; the documented `<issue>-apply-<change>` implementation pattern is unchanged.
- Add a one-line pointer in `AGENTS.md` to the issue-branch convention, so every agent session sees the rule without loading the skill.
- Add **issue branch** to `glossary/technical.md`, per this repo's glossary discipline for terms introduced in specs: the `<issue-number>-<change-slug>` branch cut from `main` before a change's first commit, whose pull-request merge is the only way the change's planning and implementation commits reach `main`.
- Out of scope: changing the recommended workflow beyond the two gates; the intent-material issue template and kit-layering ADR (#23); the Python/uv toolchain (#21, whose branch `21-adopt-python-uv-toolchain` already follows the convention); the **documentation site** (#22); and a repo-level ADR under `adr/` — the decision is recorded in this change's `adr.md` artifact, per the glossary-fork precedent.

## Capabilities

### New Capabilities
- `change-branching`: Governs where a change's work lands — every new change cuts an **issue branch** (`<issue-number>-<change-slug>`) from `main` before its first commit, change work reaches `main` only by pull-request merge, and the no-auto-git rule, phase sequence, merge gates, and archive bookkeeping commit are preserved — plus the paper trail that protects the amendment: the skill fork is recorded in the divergence manifest, and maintainer guidance explains hand-merging upstream changes and re-applying the two amended gates after any sync.

### Modified Capabilities
None — no published spec covers the change lifecycle or branching policy; `adopter-onboarding`, `docs-site`, `experiment-references`, `governance-docs`, and `store-identity` are unaffected at spec level (their divergence-manifest requirements concern the license and CI rows, which this change does not touch).

## Impact

- Affected files: `.agents/skills/openspec-git-discipline/SKILL.md` (two gates), `docs/maintainer.md` (divergence manifest and drift impact), `CONTRIBUTING.md` (pull-request section), `AGENTS.md` (one line), `glossary/technical.md` (one term). No code, API, or dependency changes; the **maintainer toolchain** and the repository's zero-runtime posture are untouched.
- Process: tracked by issue #24 on branch `24-require-issue-branch-for-changes` — itself cut per the convention this change mandates; commits carry the conventional `(#24)` subject suffix, with `Closes #24` only in the archive-phase commit.
- Downstream: the forked skill ships in the workflow scaffolding installed into each experiment repository, and the divergence manifest governs what adopters install — they inherit the amended gates on their next scaffolding sync, and the manifest plus drift-impact entry keep a future template sync from silently reverting them.
