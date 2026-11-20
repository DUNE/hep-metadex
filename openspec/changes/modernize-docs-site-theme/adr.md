# ADR Review Manifest

- Status: completed
- Review date: 2026-11-20

## Review Summary

ADR review completed for this change.

## In-Force ADRs Reviewed

- `adr/0001-serve-experiments-via-readonly-store-references.md` — Accepted
- `adr/0002-dune-incubation-with-hsf-endorsement-trigger.md` — Accepted
- `adr/0003-fenced-gherkin-single-source-validation-gate.md` — Accepted (governs how this change's delta spec validates)
- `adr/0004-apache-2-license-diverging-from-template-mit.md` — Accepted
- `adr/0005-distribute-spec-validation-ci-as-host-conditional-scaffolding.md` — Accepted
- `adr/0006-python-uv-as-repo-local-maintainer-toolchain.md` — Accepted (owns the toolchain the Zensical bump lands in)
- `adr/0007-publish-zensical-docs-site-on-github-pages.md` — Accepted (the live constraint set this change works within; extended, not superseded)
- `adr/0008-route-workflow-conventions-to-kit-layers.md` — Accepted
- `adr/0009-distribute-workflow-scaffolding-as-versioned-kit-releases.md` — Accepted
- `adr/0010-enforce-kit-release-discipline-with-reminder-and-archive-gate.md` — Accepted (no kit path is touched, so no kit release follows)
- `adr/0011-unify-checkout-action-pin-across-workflows.md` — Accepted
- `adr/0012-ship-kit-commands-as-kit-owned-files-fetched-from-kit-releases.md` — Accepted

No ADR carries a `Supersedes` field; all twelve are in force.

## New Durable ADRs Created

- `adr/0013-docs-site-reader-experience-config-only-with-remote-branding.md` — records that the documentation site's reader-facing experience stays configuration-only in `zensical.toml` with branding referenced by remote URL, widening the hosting-move edit set to `repo_url`, `site_url`, and the avatar URL. Extends ADR-0007; supersedes nothing. Design decisions below that bar (palette colors, section grouping and titles, expand-vs-prune tuning, apply-time verification steps) are tactical and are recorded in `design.md` only.
