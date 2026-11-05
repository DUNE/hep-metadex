## Why

hep-metadex exists to be the general-purpose reference for building experiment metadata management systems across high-energy physics, but as a repo-local OpenSpec project with zero specs it offers no way for an **experiment repository** to consume its specifications or replicate its workflow. This change makes it consumable — hep-metadex becomes a registered **OpenSpec Store**, dune-metadex becomes the first adopter, and the adoption-readiness gaps on the path to **HSF affiliation** (license, adopter documentation, spec-validation CI) close — proving the mechanism while the **OpenSpec Store**'s first **common capability** spec remains a follow-up change.

## What Changes

- **OpenSpec Store conversion (hep-metadex):** hep-metadex registers as an **OpenSpec Store** with the **org-neutral** id `hep-metadex`. `.openspec-store/store.yaml` holds the **OpenSpec Store**'s identity metadata; all content stays in the existing `openspec/` tree in place — no migration. The **OpenSpec Store**'s registered content is its **common capability** specs and their changes; improvements to them are proposed from any directory with `--store hep-metadex` and land as changes in the **OpenSpec Store** repository.
- **Experiment bootstrap (dune-metadex):** the **workflow scaffolding** (schema, skills, commands, subagents, agent guidance) is installed into dune-metadex from the template — **workflow scaffolding** replicates by template install and never flows through the **OpenSpec Store**. dune-metadex gains an `openspec/config.yaml` declaring a read-only **Store reference** to the `hep-metadex` **OpenSpec Store** plus experiment-specific context (domain description, stage rules, glossary entries), and experiment-local `specs/` and `changes/` directories. **Experiment repository** configs never use the write-routing `store:` line — their specs and changes stay in their own repository.
- **Adopter-facing documentation:** the README is rewritten as the adopter front door (what/why plus quick start), with existing maintainer content absorbed into the new documents, not lost. New documents: `docs/setup.md` (OpenSpec Store layout and **experiment repository** configuration), `docs/usage.md` (**change-time work** — an experiment proposing and implementing its own change with **OpenSpec Store** context injected — and **write-back** — an experiment proposing an improvement to a **common capability** spec into the **OpenSpec Store** via `--store hep-metadex`), `docs/governance.md` (decision rights, review bar, **org-neutral** hosting roadmap), `docs/hsf-affiliation.md` (affiliation path and full HSF checklist mapping), and `CONTRIBUTING.md`. The glossaries (`glossary/domain.md`, `glossary/technical.md`) anchor shared terminology.
- **Licensing:** an Apache-2.0 `LICENSE` is added — a deliberate divergence from the intent-driven template's MIT, recorded in the README divergence manifest (closes the HSF checklist license item).
- **Spec-validation CI:** a GitHub Actions workflow runs `openspec validate` over all specs and changes and fails when validation reports any artifact invalid — the test-suite interpretation for a zero-runtime-code repository (closes the HSF checklist test-suite item).
- **Hosting decision (ADR):** recorded as an ADR in this change: the DUNE organization incubates the **OpenSpec Store**; HSF Steering Group endorsement triggers **HSF affiliation**; hosting in the HSF GitHub organization is a separate, optional, mutually-agreed follow-on.
- **Out of scope:** the first **common capability** spec (the follow-up change that will propose one to the **OpenSpec Store**), experiment implementation code, EIC and sPHENIX repositories, the HSF affiliation application itself, and any HSF-org hosting move.

## Capabilities

### New Capabilities
- `store-identity`: hep-metadex behaving as a registered **OpenSpec Store** — **org-neutral** identity, in-place content (specs and changes under `openspec/`, identity metadata under `.openspec-store/`), and the `--store hep-metadex` route for proposing **common capability** improvements.
- `experiment-references`: how an **experiment repository** connects read-only via the `references:` block in `openspec/config.yaml` — the **OpenSpec Store**'s **spec index** injected into artifact workflows — and the prohibition on the write-routing `store:` line.
- `adopter-onboarding`: the documented path a stranger follows to adopt the **OpenSpec Store** and install the **workflow scaffolding** — quick start, setup, **change-time work** and **write-back** usage, and contributing.
- `governance-docs`: decision rights, review bar (including spec-validation CI and license/divergence recording), **org-neutral** hosting roadmap, and the **HSF affiliation** path with its checklist mapping.

### Modified Capabilities

None. hep-metadex has no existing behavior specifications — every capability in this change is new.

## Impact

- **Repositories:** `DUNE/hep-metadex` gains `.openspec-store/`, the adopter documentation set, `LICENSE`, and CI; its README is rewritten as the adopter front door with maintainer content absorbed into the docs. `DUNE/dune-metadex` (currently a bare README) gains its `openspec/` **workflow scaffolding**, config with the **Store reference**, and local specs/changes directories. This change's artifacts live in hep-metadex; dune-metadex tasks are executed against that repository's own checkout during apply.
- **No breaking changes:** the project has zero specs, zero changes, and no runtime code (tech stack remains TBD); dune-metadex is a bare README with nothing to preserve. Nothing existing depends on the current layout, so no **BREAKING** markers apply.
- **Tool dependency:** both repositories depend on OpenSpec CLI 1.16.0 Stores (beta) — **OpenSpec Store** registration, `references:` injection, and `--store` routing are beta features whose surface may evolve. CLI version pinning and upgrade guidance are covered in the adopter documentation, and the beta-evolution risk is recorded in this change's design document.
- **Process:** tracked as GitHub issue #7 ("Bootstrap multi-repo OpenSpec stores") on branch `7-bootstrap-multi-repo-openspec-stores`; conventional commits throughout.
- **Downstream:** EIC and sPHENIX **experiment repositories** will later follow the dune-metadex adoption pattern.
