# ADR-0011: Unify the actions/checkout pin across the repository's workflows at the newest major

## Status

Accepted

## Date

2026-11-19

## Context and Problem Statement

The repository's four GitHub Actions workflows pinned `actions/checkout` two ways: `docs.yml` and `kit-reminder.yml` — the two newest — at `@v7` (#22 and #35 set the precedent), while `release.yml` and `validate.yml` stayed at `@v4`, never revisited. The split was drift, not decision, and floating major tags made it worse than static: `@v4` moved to v4.4.0 (July 2026) carrying the same fork-checkout security backport as the v7 line, so the older pin kept changing unreviewed. Because `validate.yml` is a kit copy-list path, every **Kit release** exported the lagging `@v4` pin into **experiment repositories** — the template source kept shipping drift its own newest workflows had moved past. A future v4-specific advisory would force four coordinated edits with reviewers re-deriving which pin is current. The DUNE organization's Actions policy constrains the choice — only DUNE-owned, GitHub-created, or allowlisted actions, and `actions/checkout` qualifies at every major — and issue #44 set the expected direction (`@v7`) unless the change's own investigation found a runner or behavior constraint.

The investigation found none: v7.0.0's behavior change (refusing fork pull request checkouts under `pull_request_target` and `workflow_run`) cannot fire — the workflows trigger on push, pull_request, and workflow_dispatch; `fetch-depth: 0` fetches full history and tags identically across v4 through v7, preserving `release.yml`'s tag-based bump detection; and the node24 runtime the v5+ line requires is satisfied on the GitHub-hosted runners where `@v7` already runs green in `docs.yml` and `kit-reminder.yml`.

## Considered Options

- Unify at `@v7`, the newest major, keeping the floating-major pin style: one coordinated move of `release.yml` and `validate.yml` (`docs.yml` and `kit-reminder.yml` already conform), the move shipping to adopters as PATCH **Kit release** v1.0.1 per ADR-0009's release discipline
- Coordinate on `@v4` instead (rejected — the kit would keep shipping the lagging pin, the move contradicts the newest precedent, and `@v4` floats regardless: staying is not standing still)
- SHA or exact-version pinning (rejected — out of scope per #44, and it freezes out the automatic security backports that the `@v4` move demonstrated arriving under floating tags)
- Defer until a v4-specific advisory forces the move (rejected — each intervening kit release exports the drift, and the fix is cheapest while only two files lag)

## Decision Outcome

Chosen option: "unify at `@v7`", because a floating tag makes a split pin actively harmful — the two pins diverge silently over time — while a unified floating tag turns every future move into one visible, coordinated edit. Every workflow in the repository that uses `actions/checkout` pins it at one unified floating major version, today `@v7`, and pin moves are coordinated single changes across every checkout-using workflow (the `workflow-action-pinning` capability carries the invariant). The pinned action remains GitHub-created per the DUNE policy. The floating-major style stays: security backports keep arriving automatically. Because `validate.yml` is kit-owned, the move lands as **Kit release** v1.0.1 (PATCH) with its **Kit version file** bump and `CHANGELOG.md` entry in the same change, per ADR-0009's and ADR-0010's discipline.

### Consequences

- Good, because the pin's answer is single and durable — reviewers and future changes read one major, and a single-workflow pin move is a visible spec violation rather than silent drift.
- Good, because the template source stops exporting the lagging pin: **experiment repositories** updating to v1.0.1 receive `validate.yml` at the same major the reference repository's newest workflows set, and the release body names the change at update time.
- Bad, because a floating tag keeps moving under the unified pin: each `@v7` patch release lands unreviewed — accepted for the automatic backports, the same trade the repository already made for `@v4`.
- Bad, because a self-hosted adopter whose runner predates the node24 line (below 2.327.1) cannot run the updated `validate.yml` — GitHub-hosted adopters are unaffected, and the runtime requirement is the action's own, inherited with any `@v5`+ checkout.
- Follow-up: the first `@v7` runs of `validate.yml` and `release.yml` are this change's own pull requests; the `workflow-action-pinning` spec makes future drift reviewable; a future tightening (SHA pinning) or loosening lands as a modification to that capability, superseding this ADR only if the floating-major style itself is revisited.
