# ADR Review Manifest

- Status: completed
- Review date: 2026-11-11

## Review Summary

ADR review completed for this change. The design's decisions were assessed against the ADR bar — long-term architectural commitment, effect on future changes, not already captured by an in-force ADR. One qualified: the kit-layering routing rule with the intent-driven schema-fork trigger conditions (design D7) — a placement contract for every future workflow convention, forced by this change's need to place the issue-authoring convention, that generalizes ADR-0005's host-conditional pattern without superseding it. D1 (form shape), D2 (blank issues disabled), D3 (copy-list item), D4 (dogfood sequencing), D5 (guidelines section), D6 (pointers), and D8 (manifest row) are tactical documentation and distribution decisions, covered by the design. The design's open questions are resolved: one ADR covers both the routing rule and the fork triggers; the sequence number is 0008 — no other ADR-bearing change is active. No in-force ADR is superseded; ADR-0005 is extended in pattern, not amended.

## In-Force ADRs Reviewed

- `adr/0001-serve-experiments-via-readonly-store-references.md` — the two channels; the issue form rides channel 2 (template install), the new spec rides channel 1 (read-only store).
- `adr/0002-dune-incubation-with-hsf-endorsement-trigger.md` — **org-neutral** governance text; all new form and guidance copy stays org-neutral.
- `adr/0003-fenced-gherkin-single-source-validation-gate.md` — gate semantics; the new delta specs are fenced Gherkin and the validation gate is untouched.
- `adr/0004-apache-2-license-diverging-from-template-mit.md` — the divergence-manifest discipline the new row follows.
- `adr/0005-distribute-spec-validation-ci-as-host-conditional-scaffolding.md` — the host-conditional kit precedent; the issue form is the pattern's second instance, and ADR-0008 generalizes the layering it established.
- `adr/0006-python-uv-as-repo-local-maintainer-toolchain.md` — repo-local **maintainer toolchain**; no runtime code is involved in this change.
- `adr/0007-publish-zensical-docs-site-on-github-pages.md` — the strict docs build; the new guidelines section's cross-references must stay strict-clean.

## New Durable ADRs Created

- `adr/0008-route-workflow-conventions-to-kit-layers.md` — the kit-layering routing rule: the schema for artifact structure inside changes, `openspec/config.yaml` rules for per-stage discipline, skills for agent-triggered discipline, commands for procedure automation, the intent-prompt guidelines doc for authoring guidance, `.github/` for host-conditional automation — with the intent-driven schema fork deferred to explicit triggers (upstream will not take structural artifact changes, the schema declares companion skills, upstream stalls).
