# ADR Review Manifest

- Status: completed
- Review date: 2026-11-10

## Review Summary

ADR review completed for this change. The design's decisions were assessed against the ADR bar — long-term architectural commitment, effect on future changes, not already captured by an in-force ADR. None qualified. The underlying policy (every change cuts an **issue branch** from `main` before its first commit) is a contributor-workflow rule, not an architectural commitment: it chooses no technology, boundary, or contract, and it is durably recorded on three surfaces that persist across changes — the amended skill gates, `CONTRIBUTING.md`'s pull-request section, and the `change-branching` spec. The vendored-skill fork follows the recorded-divergence discipline ADR-0004 already established, and the glossary-fork precedent (a skill fork with a manifest row and no ADR) governs. D1–D8 are tactical wording and placement decisions, covered by the design. The design's open question on ADR granularity is resolved: no new repository-level ADR. No in-force ADR is superseded.

## In-Force ADRs Reviewed

- `adr/0001-serve-experiments-via-readonly-store-references.md` — the two channels; the forked skill travels the **workflow scaffolding** channel to adopters, unchanged by this decision.
- `adr/0002-dune-incubation-with-hsf-endorsement-trigger.md` — hosting roadmap; untouched.
- `adr/0003-fenced-gherkin-single-source-validation-gate.md` — governs this change's delta-spec format and the `valid: true` verification gate; untouched.
- `adr/0004-apache-2-license-diverging-from-template-mit.md` — the recorded-divergence discipline the new manifest row follows.
- `adr/0005-distribute-spec-validation-ci-as-host-conditional-scaffolding.md` — the kit-distribution precedent; this change's fork rides the same channel.
- `adr/0006-python-uv-as-repo-local-maintainer-toolchain.md` — **maintainer toolchain**; untouched (no code or dependency changes).
- `adr/0007-publish-zensical-docs-site-on-github-pages.md` — **documentation site**; the out-of-scope #22 work, untouched.

## New Durable ADRs Created

- None — no major durable architectural decisions were introduced; the branch policy is recorded on the skill gates, `CONTRIBUTING.md`, and the `change-branching` spec instead, per the glossary-fork precedent.
