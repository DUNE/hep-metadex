# ADR-0008: Route workflow conventions to kit layers, with the intent-driven schema fork deferred to explicit triggers

## Status

Accepted

## Date

2026-11-11

## Context and Problem Statement

hep-metadex's **workflow scaffolding** carries several distinct mechanism classes — the local intent-driven schema copy, `openspec/config.yaml` stage rules, vendored skills, `.opencode/` commands, the copy-listed `docs/intent-prompt-guidelines.md`, and host-conditional `.github/` automation (ADR-0005) — but nothing records which class of convention belongs in which layer. Standardizing issue authoring (#23) forced the question concretely: an issue-authoring convention could plausibly live in the schema, a new skill, a command, the guidelines doc, or `.github/`. Without a routing rule, each convention placement is re-argued per change, and the tempting answer — forking the intent-driven schema (`openspec schema fork`) to embed project-specific artifact structure — would divorce hep-metadex from upstream schema maintenance for a gain that is usually documentation, not structure.

## Considered Options

- A routing rule across the existing layers: the schema carries artifact structure inside changes; `openspec/config.yaml` rules carry per-stage discipline; skills carry agent-triggered discipline; commands carry procedure automation; the intent-prompt guidelines doc carries authoring guidance; `.github/` carries host-conditional automation per ADR-0005 — with the schema forked only on explicit triggers
- Fork the intent-driven schema now to embed hep-metadex-specific conventions in artifact structure
- Record conventions case-by-case with no standing rule (the status quo)
- Add a conventions-guide document as the single home for all workflow conventions

## Decision Outcome

Chosen option: "a routing rule across the existing layers", because each layer already has a distinct delivery and enforcement mechanism — the schema is upstream-vendored structure validated by the CLI, config rules are injected per stage, skills load on demand in agent sessions, commands automate procedures, the guidelines doc is copy-listed prose, and `.github/` is host-conditional — so every convention class has exactly one honest home. The issue form (#23) is the rule's first full application: it lands in `.github/` per the ADR-0005 pattern, its authoring guidance lands in the guidelines doc, and the schema is untouched. The intent-driven schema is NOT forked: a fork happens only when (1) upstream will not take structural artifact changes hep-metadex needs, (2) the schema comes to declare companion skills the project must diverge from, or (3) upstream maintenance stalls. Until a trigger fires, structural needs route upstream and everything else routes to the other layers.

### Consequences

- Good, because convention placement stops being re-argued per change: the contributor- and maintainer-facing surfaces (CONTRIBUTING.md's "Where Decisions Live", the maintainer guide's Repository Configuration section) point at one rule.
- Good, because the schema stays upstream-trackable — hep-metadex keeps taking upstream schema maintenance instead of maintaining a fork.
- Good, because the rule extends ADR-0005 rather than superseding it: host-conditional automation is one layer among six, and the issue form lands by the same pattern validate.yml set.
- Bad, because the rule constrains convenience: a convention that would sit naturally in artifact structure — say, a mandatory issue-material stage — must instead ride config rules or prose until a fork trigger fires.
- Bad, because the fork triggers are judgment calls (what counts as "upstream stalls"); the first trigger event will need its own decision record.
- Follow-up: #9's `/metadex-bootstrap` command lands procedure automation in the command layer under this rule; the routing rule is referenced from CONTRIBUTING.md and `docs/maintainer.md`.
