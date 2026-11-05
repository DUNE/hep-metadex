# Contributing

Thanks for contributing. This policy is deliberately
[org-agnostic](glossary/domain.md): it names no organization-specific
process, so contributors from any experiment or institution work the same
way, and a hosting move changes nothing here.

## Every Change Starts as an Issue

Open a GitHub issue describing the problem or capability before proposing a
change. **One issue per change**, and the issue tracks the change's entire
lifecycle — proposal, implementation, verification, archive — so it stays
open until the change archives. The issue tracker is publicly viewable,
open and closed tickets alike.

## Pull Requests

All work lands through pull requests:

- Branch from `main`, open the PR against `main`, and keep the
  [change lifecycle](docs/usage.md#the-change-lifecycle) — planning artifacts
  merge before implementation starts; implementation merges before anything
  archives.
- Spec-validation CI must pass: `openspec validate` over all specs and
  changes, gating on `valid: true` ([ADR-0003](adr/0003-fenced-gherkin-single-source-validation-gate.md)).
- Proposing an improvement to a [common capability](glossary/domain.md) spec?
  That is [write-back](docs/usage.md#write-back-improving-a-common-capability):
  create the change with `--store hep-metadex` so it lands in this
  repository, from any directory.

## Conventional Commits

Commits use the conventional format, and **every commit references its
change's issue number as a `(#N)` subject suffix**:

```text
feat(catalog): add experiment reference resolution (#42)
docs(usage): describe store pull discipline (#42)
```

`Closes #N` appears **only in the archive-phase commit**, since one issue
tracks a change's entire lifecycle — closing it earlier would orphan the
later phases. Pull-request descriptions should not close the issue either;
the archive commit does.

## Glossary Discipline

Shared vocabulary is an artifact here, not an accident:

- When you introduce a term — in specs, docs, or code — add it to
  [glossary/domain.md](glossary/domain.md) (domain terms) or
  [glossary/technical.md](glossary/technical.md) (technical terms) with a
  definition, a *use when*, and an *avoid* column.
- Use existing terms per their *use when*/*avoid* guidance, and link a term
  on first use in a document.
- The [glossary skill](.agents/skills/glossary/SKILL.md) enforces this in
  agent-driven artifact workflows; human reviewers hold the same bar.

## Where Decisions Live

Durable architectural decisions — topology, validation gates, licensing,
hosting — live as ADRs in [adr/](adr/), proposed through a change's `adr`
stage. If your change commits the project long-term, expect the review to
ask for one. See [docs/governance.md](docs/governance.md) for decision
rights and the review bar, and [docs/maintainer.md](docs/maintainer.md) for
how this repository relates to its upstream template.
