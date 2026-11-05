# Governance

Who decides what, the bar a change must clear, and where this repository is
hosted and headed. The processes below are [org-neutral](../glossary/domain.md)
by design: they name no organization-specific process, so a hosting move is a
purely infrastructure event ([ADR-0002](../adr/0002-dune-incubation-with-hsf-endorsement-trigger.md)).

## Decision Rights

| Decision | Who |
|----------|-----|
| [Common capability](../glossary/domain.md) specs and their changes (the store's `openspec/specs/` and `openspec/changes/`) | Store maintainers — any contributor may propose via [write-back](../glossary/domain.md); maintainers review and merge |
| An [experiment repository](../glossary/domain.md)'s own specs, changes, and implementation | That experiment's team, alone — the store is read-only for them |
| Durable architectural decisions | Anyone may propose; the decision lands as an ADR in `adr/` through a change's `adr` stage |
| Terminology | Contributors, through glossary discipline (see [CONTRIBUTING.md](../CONTRIBUTING.md)) |
| Hosting and affiliation | Store maintainers, with the HSF Steering Group as the endorsement body (see the [hosting roadmap](#hosting-roadmap) below) |

No decision above requires membership in any particular organization:
write-back works from any directory, cross-organization pull requests are
ordinary GitHub workflow, and experiment teams never cede control of their
own repositories ([ADR-0001](../adr/0001-serve-experiments-via-readonly-store-references.md)).

## Review Bar

Every change — in the store or in an experiment repository — must clear:

- **The two merge gates.** Planning artifacts are reviewed and merged to
  `main` before implementation starts; implementation is merged to `main`
  before anything is archived. See
  [the change lifecycle](usage.md#the-change-lifecycle).
- **A green validation gate.** CI runs `openspec validate` over all specs
  and changes and fails on any invalid artifact — the test-suite
  interpretation for a zero-runtime specification repository
  ([ADR-0003](../adr/0003-fenced-gherkin-single-source-validation-gate.md)).
- **Single-source scenarios.** Requirements carry fenced Gherkin scenarios
  authored once; bullets-mirroring-fences are not accepted
  ([ADR-0003](../adr/0003-fenced-gherkin-single-source-validation-gate.md)).
- **Recorded divergences.** Any deliberate divergence from the intent-driven
  template — license choice, added CI, renamed conventions — must be recorded
  in the divergence manifest
  ([maintainer.md](maintainer.md#intentional-divergences)). The Apache-2.0
  license is the precedent: adopted for its explicit patent grant, recorded
  as a divergence from the template's MIT
  ([ADR-0004](../adr/0004-apache-2-license-diverging-from-template-mit.md)).
- **Durable decisions as ADRs.** A decision that binds future changes —
  topology, validation gates, licensing, hosting — graduates from a change's
  design notes to a repository ADR through the `adr` stage.
- **Glossary discipline.** New terms land in `glossary/` with
  use-when/avoid guidance, and documents use them consistently.

## Hosting Roadmap

Recorded in [ADR-0002](../adr/0002-dune-incubation-with-hsf-endorsement-trigger.md):

1. **Incubation — now.** The repository is incubated in the DUNE GitHub
   organization while internal reviews greenlight the approach and adoption
   evidence accumulates.
2. **Endorsement — the trigger.** Endorsement by the HEP Software Foundation
   Steering Group, under its affiliated-projects process, is the
   [HSF affiliation](../glossary/domain.md) event. The checklist mapping an
   evaluator walks lives in [hsf-affiliation.md](hsf-affiliation.md).
   Affiliation is valid for five years, then reviewed.
3. **HSF-organization hosting — a separate follow-on.** Moving the repository
   into the HSF GitHub organization is optional and mutually agreed, and is
   **not** implied by affiliation. If it happens, it is one infrastructure
   transfer: git remotes change, and the advisory `remote:` line in
   experiment configs is updated. The [org-neutral](../glossary/domain.md)
   store id `hep-metadex`, every store registration, and all governance text
   survive unchanged — which is exactly why the processes above name no
   organization.
