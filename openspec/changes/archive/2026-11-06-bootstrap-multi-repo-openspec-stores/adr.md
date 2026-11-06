# ADR Review Manifest

- Status: completed
- Review date: 2026-11-05

## Review Summary

ADR review completed for this change. No repository-level ADRs existed before this change, so no in-force decisions constrained the design. The design's durable decisions were reviewed against the ADR bar — long-term architectural commitment, effect on future changes, not already captured — and four qualified. The design's D6 (CI as the HSF test-suite interpretation) and D7 (documentation architecture) were assessed and left as design context: documented where they live, below the ADR bar.

## In-Force ADRs Reviewed

- None — `<repo>/adr/` had no in-force ADRs when this change began.

## New Durable ADRs Created

- `adr/0001-serve-experiments-via-readonly-store-references.md` — experiments consume hep-metadex through read-only **store references**, with **workflow scaffolding** replicating by template install (two channels).
- `adr/0002-dune-incubation-with-hsf-endorsement-trigger.md` — DUNE-org incubation; HSF Steering Group endorsement is the **HSF affiliation** trigger; HSF-org hosting is a separate, optional, mutually-agreed follow-on.
- `adr/0003-fenced-gherkin-single-source-validation-gate.md` — fenced Gherkin is the single scenario source; validation gates on `valid: true`; strict-mode compatibility is revisited on CLI upgrade.
- `adr/0004-apache-2-license-diverging-from-template-mit.md` — Apache-2.0 adopted, with the divergence from the template's MIT recorded in the README divergence manifest.
