# ADR Review Manifest

- Status: completed
- Review date: 2026-11-19

## Review Summary

ADR review completed for this change.

## In-Force ADRs Reviewed

- `adr/0001-serve-experiments-via-readonly-store-references.md` — the two channels; the unified pin reaches adopters only through channel 2 (the kit bundle carrying `validate.yml`), never through the store.
- `adr/0002-dune-incubation-with-hsf-endorsement-trigger.md` — the DUNE-organization hosting that makes the GitHub-created action policy load-bearing; hosting context only, not re-evaluated.
- `adr/0003-fenced-gherkin-single-source-validation-gate.md` — the change's delta spec follows the fenced-Gherkin single source; validation stays non-strict.
- `adr/0004-apache-2-license-diverging-from-template-mit.md` — no bearing on the decision.
- `adr/0005-distribute-spec-validation-ci-as-host-conditional-scaffolding.md` — the distribution channel the pin move travels: the same `validate.yml` ships, one line different; the host-conditional contract is unchanged.
- `adr/0006-python-uv-as-repo-local-maintainer-toolchain.md` — no direct bearing (no maintainer-toolchain edits in this change).
- `adr/0007-publish-zensical-docs-site-on-github-pages.md` — no bearing (docs.yml's pin is verified, not edited; site tooling untouched).
- `adr/0008-route-workflow-conventions-to-kit-layers.md` — routing untouched: `.github/` automation stays where it is, and the change adds no new layer or convention.
- `adr/0009-distribute-workflow-scaffolding-as-versioned-kit-releases.md` — the release mechanism exercised as designed: PATCH bump plus changelog entry in the same change; not superseded.
- `adr/0010-enforce-kit-release-discipline-with-reminder-and-archive-gate.md` — the enforcement layer applied, not modified: the reminder observes this change silently (bump present), the gate holds archive until v1.0.1 contains the kit-touching commit.

## New Durable ADRs Created

- `adr/0011-unify-checkout-action-pin-across-workflows.md` — records the unified-pin decision: every checkout-using workflow pins `actions/checkout` at one floating major (today `@v7`), moves are coordinated single changes, the pin stays GitHub-created per the DUNE policy, and the kit ships the move as PATCH release v1.0.1. Extends ADR-0005's channel and ADR-0009's discipline; supersedes neither.
