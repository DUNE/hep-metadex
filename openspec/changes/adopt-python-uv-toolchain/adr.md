# ADR Review Manifest

- Status: completed
- Review date: 2026-11-08

## Review Summary

ADR review completed for this change. The design's decisions were assessed against the ADR bar — long-term architectural commitment, effect on future changes, not already captured by an in-force ADR. One qualified: establishing Python 3.14 managed by uv as the repo-local **maintainer toolchain** — a technology and boundary commitment (design D1's non-channel framing, with D2/D3 as its implementation shape) that affects every future change's injected context, #22's docs build, and #20's eventual acceptance-stack selection. D4 (context-line content), D5 (hsf-affiliation row wording), and D6 (manifest and map placement) are tactical documentation decisions, covered by the design. The design's open question on granularity is resolved: one ADR, with the acceptance-`stack:` deferral recorded as a consequence rather than a separate record. No in-force ADR is superseded; ADR-0001 is clarified — the toolchain sits outside both channels — not amended.

## In-Force ADRs Reviewed

- `adr/0001-serve-experiments-via-readonly-store-references.md` — the two channels; the **maintainer toolchain** is explicitly outside both (clarified, not superseded).
- `adr/0002-dune-incubation-with-hsf-endorsement-trigger.md` — **org-neutral** governance text; the hsf-affiliation rewrite preserves it.
- `adr/0003-fenced-gherkin-single-source-validation-gate.md` — gate semantics; untouched by this change.
- `adr/0004-apache-2-license-diverging-from-template-mit.md` — the divergence-manifest discipline the new row follows.
- `adr/0005-distribute-spec-validation-ci-as-host-conditional-scaffolding.md` — the host-conditional kit precedent; the toolchain is deliberately not kit — the mirror image of this pattern.

## New Durable ADRs Created

- `adr/0006-python-uv-as-repo-local-maintainer-toolchain.md` — Python 3.14 managed by uv is the **maintainer toolchain** for hep-metadex itself: repo-local (a non-channel), no adopter mandate, committed lockfile as the reproducibility anchor, acceptance `stack:` deferred with Python as the expected default.
