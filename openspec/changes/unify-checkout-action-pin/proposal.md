## Why

The repository's four GitHub Actions workflows pin `actions/checkout` inconsistently: `docs.yml` and `kit-reminder.yml` — the two newest — pin `@v7`, while `release.yml` and `validate.yml` still pin `@v4`. The split is accidental drift, not a decision: `docs.yml` moved to `@v7` when it landed (#22), `kit-reminder.yml` followed the newest precedent (#35), and the two older workflows were never revisited. The inconsistency is invisible day to day, but the moment a v4-specific behavior or security advisory motivates a move, four files need coordinated edits and reviewers must re-derive which pin is current.

Two facts make now the right time to fix it. `@v4` is a floating major tag that already moved under the older workflows (v4.4.0, July 2026, carrying the same security backport as the v7 line) — the pin that looks like standing still keeps changing unreviewed. And `.github/workflows/validate.yml` is a kit copy-list path, so every **Kit release** of the **workflow scaffolding** ships the lagging `@v4` pin into installed **experiment repositories**: the reference repository keeps exporting drift its own newest workflows have already moved past.

## What Changes

- Unify the `actions/checkout` pin at `@v7` — the newest major, already running in `docs.yml` and `kit-reminder.yml`:
  - `.github/workflows/release.yml`: pin line `@v4` → `@v7`.
  - `.github/workflows/validate.yml`: pin line `@v4` → `@v7`; the `OPENSPEC_VERSION` CLI pin (`v1.16.0`) is untouched.
  - `.github/workflows/docs.yml` and `.github/workflows/kit-reminder.yml`: already `@v7` — verified, not edited.
- The issue left the target major open to the change's own investigation; that investigation found no runner or behavior constraint for these workflows' events and usage. The evidence lands in design.md and ADR 0011, including the one adopter-facing consequence worth examining rather than assuming away: runner currency for self-hosted adopters.
- Because `validate.yml` is a kit copy-list path, the change is kit-touching and carries the kit release discipline in the same change: bump the **Kit version file** (`.metadex-kit`) 1.0.0 → 1.0.1 (PATCH — a fix to a kit component) and add the matching `## [1.0.1]` section to `CHANGELOG.md` (Keep a Changelog style, `### Fixed`, referencing `(#44)`), so the release workflow cuts **Kit release** v1.0.1 automatically on merge to `main`.
- Out of scope, unchanged: any workflow's logic beyond the pin line; other action pins or workflow refactors; the OpenSpec CLI pin and its cross-check; the enforcement mechanisms themselves (#35 owns them — this change adds no enforcement); the DUNE organization's Actions policy is applied, not re-evaluated. No existing documentation changes — no doc or divergence-manifest row references the checkout pins today; the decision itself lands as a new ADR.

## Capabilities

### New Capabilities
- `workflow-action-pinning`: Owns the repository's workflow action-pinning invariant, delivered here for `actions/checkout`: every workflow in the repository that uses `actions/checkout` pins it at one unified major version, and the pinned action remains a GitHub-created action per the DUNE organization's Actions policy. The requirements are durable and universal — workflows that use no checkout step sit outside the invariant, the four current workflows are the conforming set rather than the definition, and a future tightening (for example SHA pinning) lands as a modification, not a contradiction. The capability does not govern the OpenSpec CLI pin or any other pin.

### Modified Capabilities
None — the change applies `kit-release-discipline` exactly as written (version bump plus changelog entry in the same change) and leaves every existing capability's specified behavior untouched; `kit-releases` continues to govern the release workflow, whose logic does not change.

## Impact

- Files: `.github/workflows/release.yml` and `.github/workflows/validate.yml` change one line each (the checkout pin); `.metadex-kit` bumps 1.0.0 → 1.0.1; `CHANGELOG.md` gains the `## [1.0.1]` section; `specs/workflow-action-pinning/spec.md` (this change's delta) and `adr/0011-*.md` are added. `docs.yml` and `kit-reminder.yml` are verified `@v7` and untouched. No runtime code, no dependencies.
- Kit and adopters: the release workflow cuts **Kit release** v1.0.1 on merge to `main`; **experiment repositories** that update pick up `validate.yml` with the unified pin. The shipped workflow's triggers (push, pull_request, workflow_dispatch) do not include the event types v7's behavior change touches, so the move is behavior-neutral for adopters on GitHub-hosted runners; the self-hosted-runner question is examined in design.md and ADR 0011. The **Kit reminder** stays silent on this change's PR (the version bump is present), and the **Kit release gate** holds archive until published release v1.0.1 contains the kit-touching commit.
