# ADR Review Manifest

- Status: completed
- Review date: 2026-11-07

## Review Summary

ADR review completed for this change. The design's decisions were assessed against the ADR bar — long-term architectural commitment, effect on future changes, not already captured by an in-force ADR. One qualified: distributing the spec-validation workflow through the template-install channel as a host-conditional **workflow scaffolding** component (design D1, with D2's identical-gate rule as its consequence). D3 (documentation step placement), D4/D5 (cross-repo sequencing and the stall exit), and D6 (glossary-extension timing) are tactical or process decisions, documented in the design and the delta spec. No in-force ADR is superseded; ADR-0005 extends the application of ADR-0001 and ADR-0003.

## In-Force ADRs Reviewed

- `adr/0001-serve-experiments-via-readonly-store-references.md` — the two channels; the template-install channel is the one this change extends (not superseded).
- `adr/0002-dune-incubation-with-hsf-endorsement-trigger.md` — hosting context; unaffected.
- `adr/0003-fenced-gherkin-single-source-validation-gate.md` — gate semantics (`valid: true` non-strict, CLI pinned) reused unchanged by the distributed workflow (not superseded).
- `adr/0004-apache-2-license-diverging-from-template-mit.md` — the divergence-manifest discipline the reframed entry follows.

## New Durable ADRs Created

- `adr/0005-distribute-spec-validation-ci-as-host-conditional-scaffolding.md` — the validation workflow joins the distributed **workflow scaffolding** kit: GitHub-hosted adopters copy the provided workflow verbatim; repositories on other hosts receive the named equivalent gate only.
