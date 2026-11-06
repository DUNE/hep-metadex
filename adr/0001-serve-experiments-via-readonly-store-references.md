# ADR-0001: Serve experiments through read-only store references and template-installed scaffolding

## Status

Accepted

## Date

2026-11-05

## Context and Problem Statement

hep-metadex must serve as the general-purpose reference for multiple experiments' metadata management systems, but as a repo-local OpenSpec project no **experiment repository** can consume its specifications or replicate its workflow. OpenSpec Stores (beta) can share specs across repositories, but its write-routing `store:` line would centralize every experiment's planning — the opposite of the mandate, where each experiment keeps its own domain-specific specs, changes, and implementation beside its code.

## Considered Options

- Read-only `references:` to a hep-metadex **OpenSpec Store**, with **workflow scaffolding** replicated by template install (two channels)
- The write-routing `store:` line on each experiment repository (single channel, fully centralized)
- Git submodule/subtree of a shared openspec folder
- A monorepo holding all experiments

## Decision Outcome

Chosen option: "read-only **store references** plus template-installed **workflow scaffolding**", because experiments must keep their own specs, changes, and implementation in their own repositories while consuming shared specifications; **store references** inject the **OpenSpec Store**'s **spec index** into artifact workflows read-only, and the **workflow scaffolding** kit (schema, skills, commands, subagents) does not flow through the **OpenSpec Store**, so it replicates at bootstrap time by template install with hep-metadex as its source.

### Consequences

- Good, because experiment planning stays local; **common capability** improvements route to the **OpenSpec Store** explicitly via `--store hep-metadex` from any directory.
- Good, because adopting a new experiment touches only its own repository plus one references block.
- Bad, because **workflow scaffolding** drifts between the **OpenSpec Store** and experiments until re-installed; the README provenance/divergence manifest is the reconciliation discipline.
- Bad, because references read from disk — stale store checkouts serve stale specs; pull discipline is manual.
- Follow-up: [dune-metadex](https://github.com/DUNE/dune-metadex) bootstraps as the first adoption; the first **common capability** spec is the follow-up change.
