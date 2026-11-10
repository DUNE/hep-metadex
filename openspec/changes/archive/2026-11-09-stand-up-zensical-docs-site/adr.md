# ADR Review Manifest

- Status: completed
- Review date: 2026-11-09

## Review Summary

ADR review completed for this change. The design's decisions were assessed against the ADR bar — long-term architectural commitment, effect on future changes, not already captured by an in-force ADR. One qualified: publishing the **documentation site** with Zensical on GitHub Pages, built from `docs/` in place with out-of-tree links resolved by a **maintainer toolchain** staging pass (design D1/D2 are the decision's shape; D3's single `repo_url` setting and D4's uv-native CI are its implementation consequences; D6's factual-citation scoping of the org-agnostic governance requirement is a consequence the `governance-docs` delta carries). D5 (landing page and navigation) and D6's bookkeeping (divergence-manifest row, repository-map row, glossary term) are tactical, covered by the design. The design's open questions are resolved: the Module API revisit is recorded as a follow-up trigger inside the ADR, and acceptance automation stays deferred to #20 per the issue. No in-force ADR is superseded: ADR-0001 is extended (the site tooling joins the toolchain's repo-local non-channel pattern), ADR-0002 is clarified (factual hosting citations scoped as exempt infrastructure facts — via the spec delta, not an ADR edit), and ADR-0006's deferred uv-pinning question is closed by this change's CI pin.

## In-Force ADRs Reviewed

- `adr/0001-serve-experiments-via-readonly-store-references.md` — the two channels; the site tooling is a repo-local non-channel like the **maintainer toolchain** (extended, not superseded).
- `adr/0002-dune-incubation-with-hsf-endorsement-trigger.md` — **org-neutral** governance text; the hosting-move guarantee is scoped for factual hosting citations by the `governance-docs` delta (clarified, not superseded).
- `adr/0003-fenced-gherkin-single-source-validation-gate.md` — the spec-validation gate; untouched — the docs gate is a separate strict Zensical build.
- `adr/0004-apache-2-license-diverging-from-template-mit.md` — the divergence-manifest discipline the new site-tooling row follows.
- `adr/0005-distribute-spec-validation-ci-as-host-conditional-scaffolding.md` — the host-conditional kit precedent; the docs workflow deliberately does not join the kit (adopter docs sites are out of scope) — the mirror image of the toolchain boundary.
- `adr/0006-python-uv-as-repo-local-maintainer-toolchain.md` — the **maintainer toolchain**; Zensical lands in the reserved `[dependency-groups]`, and the deferred uv-pinning question is closed by this change's CI pin.

## New Durable ADRs Created

- `adr/0007-publish-zensical-docs-site-on-github-pages.md` — the hep-metadex **documentation site**: Zensical on GitHub Pages, built from `docs/` in place through a staging-pass link rewrite (`repo_url`-driven, strict-gated, uv-native CI), with the org-agnostic governance requirement scoped for factual hosting citations and the Module API revisit recorded.
