# ADR Review Manifest

- Status: completed
- Review date: 2026-11-12

## Review Summary

ADR review completed for this change. One major durable architectural decision met the bar: the channel-2 source refinement — the **workflow scaffolding** distributes as semantically versioned, checksum-verified kit releases decoupled from the store checkout. It extends ADR-0001's two-channel architecture (channel 2 gains a source and a version identity) without diverging from any in-force decision; no supersession is warranted.

## In-Force ADRs Reviewed

- ADR-0001 — serve experiments via read-only store references and template-installed scaffolding (extended by this change, not superseded)
- ADR-0002 — DUNE incubation with HSF endorsement trigger
- ADR-0003 — fenced Gherkin single-source validation gate
- ADR-0004 — Apache-2.0 license diverging from template MIT
- ADR-0005 — host-conditional validation CI as scaffolding (its copy source re-points to the release bundle; host-conditionality intact)
- ADR-0006 — Python + uv repo-local maintainer toolchain (the release workflow uses none of it — bash, git, and gh on the runner)
- ADR-0007 — Zensical docs site published from `docs/` in place (the changelog stays link-reached via out-of-tree rewriting; no staged copy)
- ADR-0008 — kit-layering routing rule (`.github/` carries the repo-local release automation, as docs.yml already does)

## New Durable ADRs Created

- `adr/0009-distribute-workflow-scaffolding-as-versioned-kit-releases.md` — records the versioned kit release channel: kit-only semver, the dual-role version file, the bump-triggered release workflow, and channel-1 preservation.
