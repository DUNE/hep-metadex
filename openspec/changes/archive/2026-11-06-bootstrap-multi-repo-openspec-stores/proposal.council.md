# Council Notes: proposal.md

## Author Summary

Adversarial author drafted the proposal from the explored background: a two-sentence Why (repo-local project cannot serve its reference mandate; store conversion + first adoption + HSF-checklist gap closure fixes that), seven What Changes bullets (store conversion, dune-metadex bootstrap, documentation set, Apache-2.0 license, spec-validation CI, hosting ADR, out of scope), the four fixed new capabilities, an explicit empty Modified Capabilities section, and a five-part Impact.

## Reviewer Challenges

- Required: the two-channel architecture was half-stated — the scaffolding channel (template install, never through the store) was missing, leaving `store-identity`'s registered content ambiguous.
- Required: "write-back" (and "change-time") used undefined inside the Capabilities contract.
- Required: store-layout claims did not reconcile on a first read (`.openspec-store/` vs "no migration").
- Required: glossary bolding applied inconsistently across prose uses.
- Advisory: two competing "mandates" in Why; empty-store expectation missing; no explicit no-breaking statement; "what that injects" vagueness; license and CI had no capability home; vague phrases ("DUNE-specific context", "first consuming change"); checklist honesty (3 of 9 items named).
- Risks raised: cross-repo change mechanics (artifacts in one repo, work in two); unverified Stores-beta specifics; the mandate premise's traceability; dune-metadex ground truth; adopter exposure to beta drift.

## Resolutions

- Accepted: scaffolding channel stated in both the bootstrap bullet and `store-identity`; write-back and change-time defined parenthetically at first use; glossary bolding unified across all prose uses; single-mandate framing with HSF affiliation as the milestone; empty-store expectation folded into Why; explicit no-breaking clause in Impact; "spec index" made concrete in `experiment-references`; license and CI homed under `governance-docs`; vague phrases glossed; checklist-honesty clause added; version-pinning/beta-drift line added to Impact; cross-repo tracking stated in Impact (artifacts live in hep-metadex; dune-metadex tasks execute against that repository's checkout).
- Resolved by evidence (not changes): store-layout reconciliation verified against the OpenSpec Stores documentation during exploration — `.openspec-store/store.yaml` holds identity, content stays in `openspec/`; the mandate premise is the project's stated purpose, which this change's README rewrite documents; dune-metadex confirmed a bare README (one commit) during exploration.
- Rejected: none materially. Reviewer suggestions that restated existing content were folded in rather than rejected.
- Deferred: ADR content (adr stage owns it); dune-metadex apply mechanics detail (tasks stage owns it).

## Remaining Risks

- Stores (beta) surface may evolve between OpenSpec CLI releases; mitigations: version pinning and upgrade guidance in the adopter docs, risk recorded in design.md.
- Cross-repo apply: this change tracks dune-metadex work as tasks, but apply edits are repo-scoped to hep-metadex; the bootstrap executes against dune-metadex's own checkout.
- Perception risk of an initially-empty store (no common capability specs at launch); mitigated by explicit expectation-setting in Why and by dune-metadex proving the adoption pattern.
