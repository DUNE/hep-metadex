# ADR Review Manifest

- Status: completed
- Review date: 2026-11-18

## Review Summary

ADR review completed for this change.

## In-Force ADRs Reviewed

- `adr/0001-serve-experiments-via-readonly-store-references.md` — the two channels; enforcement stays inside hep-metadex and flows through neither channel.
- `adr/0002-dune-incubation-with-hsf-endorsement-trigger.md` — hosting context only; no bearing on the decision.
- `adr/0003-fenced-gherkin-single-source-validation-gate.md` — the change's delta spec follows the fenced-Gherkin single source; validation stays non-strict.
- `adr/0004-apache-2-license-diverging-from-template-mit.md` — no bearing on the decision.
- `adr/0005-distribute-spec-validation-ci-as-host-conditional-scaffolding.md` — the kit-shipped `.github/` precedent; the reminder is deliberately NOT this pattern — it is repo-local like docs.yml and release.yml, because experiment repositories cut no kit releases.
- `adr/0006-python-uv-as-repo-local-maintainer-toolchain.md` — the gate script joins this toolchain under `tools/`; the repo-local non-channel boundary keeps it out of the kit.
- `adr/0007-publish-zensical-docs-site-on-github-pages.md` — the existing `tools/` divergence-manifest row belongs to this decision's documentation-site scope, which is why the gate script gets a row of its own.
- `adr/0008-route-workflow-conventions-to-kit-layers.md` — the routing rule the gate's wiring applies: config rules for archive-phase discipline, `.github/` for the reminder, repo-local tooling for the script; no schema fork.
- `adr/0009-distribute-workflow-scaffolding-as-versioned-kit-releases.md` — the release mechanism being guarded; extended read-side only (bundle assembly derives from the manifest) with its observable contract unchanged; not superseded.

## New Durable ADRs Created

- `adr/0010-enforce-kit-release-discipline-with-reminder-and-archive-gate.md` — records the reminder-plus-archive-gate enforcement decision, the repo-local layer routing of both mechanisms (config guidance and `.github/`, never the kit-owned skill), and the single-source copy-list anchored in the KIT-MANIFEST `paths:` block. Extends ADR-0008 and ADR-0009; supersedes neither.
