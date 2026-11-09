# HSF Affiliation

The path to [HSF affiliation](../glossary/domain.md) — endorsement by the
HEP Software Foundation Steering Group under its affiliated-projects process —
and the mapping of every required guideline to the place in this repository
where it is satisfied. Affiliation is valid for five years, after which the
evaluation is reviewed for continuation.

## Required-Guideline Checklist Mapping

The HSF's general guidelines are required for affiliation. Each one maps to
a satisfying artifact in this repository:

| Required guideline | Where hep-metadex satisfies it |
|--------------------|-------------------------------|
| **Public repository** — code accessible in anonymous read-only mode | [github.com/DUNE/hep-metadex](https://github.com/DUNE/hep-metadex), publicly readable; the [OpenSpec Store](../glossary/technical.md) is consumed read-only by exactly that mode |
| **A suitable name** — conveys what the project is about; no pre-existing trademarks | `hep-metadex` — high-energy physics metadata management reference; deliberately [org-neutral](../glossary/domain.md) so the name survives a hosting move ([ADR-0002](../adr/0002-dune-incubation-with-hsf-endorsement-trigger.md)) |
| **Licensing** — an open-source license attached | Apache-2.0, full text in [`LICENSE`](../LICENSE) — a deliberate divergence from the template's MIT, chosen for the explicit patent grant and contribution terms a cross-institution standards artifact needs ([ADR-0004](../adr/0004-apache-2-license-diverging-from-template-mit.md)), recorded in the [divergence manifest](maintainer.md#intentional-divergences) |
| **Installation** — instructions trivial to find; standard procedure | The [README quick start](../README.md#quick-start): install the OpenSpec CLI (pinned version), register the store, install the [workflow scaffolding](../glossary/technical.md), declare the [Store reference](../glossary/technical.md), `openspec doctor` green. Detailed in [setup.md](setup.md), including the agent-assisted bootstrap |
| **Documentation** — suitably documented; a user's guide at least as a quick start, highlighted | The README is the adopter front door (what/why + quick start + repository map); `docs/` covers [setup](setup.md), [usage](usage.md), [governance](governance.md), and [maintaining](maintainer.md); `glossary/` anchors terminology; and the [documentation site](https://dune.github.io/hep-metadex/) publishes it all at `dune.github.io/hep-metadex` |
| **Test suite** — comprehensively tested; coverage encouraged and displayed | Spec-validation CI ([`.github/workflows/validate.yml`](../.github/workflows/validate.yml)) runs `openspec validate` over all specs and changes on every push and pull request, gating on `valid: true` ([ADR-0003](../adr/0003-fenced-gherkin-single-source-validation-gate.md)) — the honest reading of a test suite for a zero-runtime specification repository, verified to fail on invalid artifacts. Runtime test coverage arrives with the first runtime change, scaffolded against the acceptance suite |
| **Open to contributors** — contributions encouraged; pull requests never disabled | [CONTRIBUTING.md](../CONTRIBUTING.md) — an [org-agnostic](../glossary/domain.md) policy; pull requests are open to any GitHub user, cross-org writes included ([ADR-0002](../adr/0002-dune-incubation-with-hsf-endorsement-trigger.md)) |
| **Issue tracking** — an issue tracker with anonymous view of open and closed tickets | GitHub issues, publicly viewable; one issue per change, tracking the change's entire lifecycle ([usage.md](usage.md#the-change-lifecycle)) |
| **General information** — dependencies, supported platforms, and similar | The [repository map](../README.md#repository-map) describes the layout; the [maintainer toolchain](../glossary/technical.md) is Python 3.14 managed by uv (pinned interpreter, no runtime code) for maintaining this repository itself; adopting repositories are unconstrained by it — their single tool dependency remains the OpenSpec CLI (pinned 1.16.0 — see [usage.md](usage.md#cli-version-pinning-and-upgrades)) |

## The Affiliation Path

Recorded in [ADR-0002](../adr/0002-dune-incubation-with-hsf-endorsement-trigger.md):

1. **Incubation** in the DUNE GitHub organization while internal reviews
   greenlight the approach and adoption evidence accumulates.
2. **HSF Steering Group endorsement** — the affiliation event. An evaluator
   walks the checklist above; this document is the review map, and
   [governance.md](governance.md) records decision rights and the review bar
   behind it.
3. **HSF-organization hosting** remains a separate, optional, mutually
   agreed follow-on — affiliation does not imply it.

## Applicability Beyond One Experiment

The store's mandate is to serve experiment metadata management across
high-energy physics, not one collaboration. The mechanism-level evidence:

- The two-channel design — specs shared read-only through the
  [OpenSpec Store](../glossary/technical.md), workflow scaffolding installed
  by template — was proven by the first adoption: [**dune-metadex**](https://github.com/DUNE/dune-metadex) bootstrapped
  from a bare repository to a connected experiment repository
  ([ADR-0001](../adr/0001-serve-experiments-via-readonly-store-references.md),
  [setup.md](setup.md#experiment-repository-configuration)).
- Adoption touches only the adopting repository plus one `references:` block
  — no change to the store, no experiment relocation
  ([ADR-0001](../adr/0001-serve-experiments-via-readonly-store-references.md)).
- Additional experiments (EIC, sPHENIX) follow the same path without store
  changes; the [org-neutral](../glossary/domain.md) id and governance text
  keep the door open regardless of hosting.
