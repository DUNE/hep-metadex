## Why

An **experiment repository** bootstrapped onto the hep-metadex **OpenSpec Store** workflow installs the agent-facing pieces of **workflow scaffolding** — schema, skills, commands, subagents, and agent guidance — yet ends up with no automated gate that its specs and changes actually validate, even though hep-metadex itself runs exactly that gate in CI. The divergence manifest compounds the gap by recording `.github/workflows/validate.yml` as a purely local divergence from the intent-driven template rather than something adopters receive, so the documented adoption path omits CI at precisely the moment the first adopter, dune-metadex, is live and can dogfood the missing step end to end.

## What Changes

- **Spec-validation CI (dune-metadex):** the first adopter **experiment repository** gains the validation gate hep-metadex already runs — the same `.github/workflows/validate.yml` the bootstrap step will tell future adopters to copy — executing `openspec validate --all` over all specs and changes and gating on `valid: true` (non-strict, per ADR-0003), with the OpenSpec CLI pinned to 1.16.0. Delivered in the dune-metadex checkout as that repository's own issue and PR, and tracked as a deliverable in this change's tasks.md.
- **Host-conditional CI step (docs/setup.md):** the agent-assisted bootstrap prompt gains a CI step conditioned on the adopter's hosting: GitHub-hosted repositories copy the provided GitHub Actions workflow, while repositories on other hosts wire the equivalent `valid: true` gate into their own CI. The documentation names the equivalent gate for non-GitHub hosts but ships no implementation for them.
- **Workflow-scaffolding reframe (docs/maintainer.md):** the intentional-divergence entry for `.github/workflows/validate.yml` stops reading as a local-only divergence ("the template ships no CI") and instead presents the workflow as a component of **workflow scaffolding** for GitHub hosts that adopters copy at bootstrap. The existing **workflow scaffolding** glossary term is extended accordingly (definition updated at apply time) — no new term is introduced.
- **Dogfooded quick start (README):** the README quick start gains the same host-conditional CI step, merged only after the dune-metadex PR lands, so the claimed path stays verified end to end: the **experiment repository** gains the workflow before the documentation claims it as a step.
- **Out of scope:** the first **common capability** spec; a `/metadex-bootstrap` command; non-GitHub CI implementations (the docs name the equivalent gate only); changes to the hep-metadex workflow itself — the adoption path is extended, not redesigned.

## Capabilities

### New Capabilities

None — every deliverable extends the already-specified adoption path rather than opening a new capability boundary.

### Modified Capabilities

- `adopter-onboarding`: the documented adoption path now carries a host-conditional spec-validation CI step — the bootstrap prompt installs CI based on the adopter's host, the divergence manifest presents the GitHub workflow as **workflow scaffolding** for GitHub hosts instead of a local-only divergence, and the README quick start claims the step only once dune-metadex, the worked example, has landed it, preserving the dogfooded consistency rule.

## Impact

- **Repositories:** two repositories change. dune-metadex gains `.github/workflows/validate.yml` via its own issue and PR; hep-metadex changes its adopter documentation (docs/setup.md, docs/maintainer.md, the README quick start), the **workflow scaffolding** glossary entry, and one stored capability spec — `adopter-onboarding`, modified by this change's delta and synced into `openspec/specs/` at archive. The **Store reference** channel is unchanged: specs still reach adopters read-only.
- **No breaking changes:** all changes are additive — existing bootstrap steps are untouched, the CI step is conditional on the host, and repositories on non-GitHub hosts are unaffected until they wire their own equivalent gate.
- **Tool dependency:** adopter CI depends on the OpenSpec CLI, pinned to 1.16.0 — the same pin hep-metadex's own workflow uses — and gates on `valid: true` non-strict, per ADR-0003.
- **Process:** tracked as GitHub issue #12 on planning branch `12-add-spec-validation-ci`, with conventional commits carrying the `(#12)` subject suffix and the issue staying open until archive. The dune-metadex workflow is delivered from this change's apply phase as that repository's own issue and PR; the hep-metadex documentation that claims the CI step merges only after that PR lands.
- **Downstream:** every **experiment repository** bootstrapped through the documented path from now on acquires the validation gate, making spec drift CI-visible in adopters rather than store-only. The divergence-manifest entry remains but describes intended, distributed **workflow scaffolding** instead of an unexplained local divergence. Non-GitHub hosts receive a named equivalent gate but no implementation — a deliberate seam for future host guides.
