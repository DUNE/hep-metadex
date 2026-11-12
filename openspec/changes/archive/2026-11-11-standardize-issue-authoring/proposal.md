## Why

The open issues were reformatted onto the **intent material** template, making each one ready-to-paste material for `/opsx-new` or `/opsx-propose` — but the convention is recorded nowhere, so future issues drift on author memory with no discoverable standard for human or agent authors. Exploration also settled a routing rule for where each class of workflow convention lives in the kit — durable architecture for this store and its adopting **experiment repositories** that exists only in an exploration thread and belongs in an ADR.

## What Changes

- Adds `.github/ISSUE_TEMPLATE/change.yml`, a GitHub issue form carrying the **intent material** sections as six required textareas in issue-body order — Context, Suggested change name, Actor, Deliverables, Rules, Out of scope — plus one optional free-form textarea for the labeled optional sections (Gate, Trigger, Decisions inside the change, Provenance, References).
- Adds `.github/ISSUE_TEMPLATE/config.yml` disabling the blank-issue path (`blank_issues_enabled: false`), making the form the single entry point for new issues.
- Adds a "Writing Issues" section to `docs/intent-prompt-guidelines.md` defining the template and its optional labeled sections as available additions; the document stays at its current path.
- Extends the authoring pointers: CONTRIBUTING.md's "Every Change Starts as an Issue" section points to the form and template, and AGENTS.md's existing guidelines-doc pointer extends to agent-authored issues — no new authoring skill.
- Extends the kit copy-list in the README quick start and `docs/setup.md`: `.github/ISSUE_TEMPLATE/` (both files, one item) joins the host-conditional items copied at bootstrap per the ADR-0005 pattern — GitHub-hosted adopters copy it verbatim; repositories on other hosts replicate the convention natively (named, not implemented).
- Adds a divergence-manifest row to `docs/maintainer.md` for the issue form, framed like the validate.yml row: a **workflow scaffolding** component that GitHub-hosted adopters copy at bootstrap.
- Adds ADR-0008 (created at this change's adr stage) recording the kit-layering routing rule — schema for artifact structure inside changes, `config.yaml` rules for per-stage discipline, skills for agent-triggered discipline, commands for procedure automation, the intent-prompt guidelines doc for authoring guidance, `.github/` for host-conditional automation — and the intent-driven schema-fork trigger conditions (structural artifact changes upstream won't take, schema-declared companion skills, upstream stalls). `docs/maintainer.md` (Repository Configuration) and CONTRIBUTING.md ("Where Decisions Live") reference it.
- Adds an **intent material** entry to `glossary/domain.md`, glossing the structured issue body the change workflows consume.

## Capabilities

### New Capabilities
- `issue-authoring`: The host-neutral issue-authoring convention — the **intent material** template (six required sections plus the optional labeled sections), the disabled blank-issue path that makes the form the single issue-entry point, the "Writing Issues" guidance in `docs/intent-prompt-guidelines.md`, the CONTRIBUTING.md and AGENTS.md pointers, and the **intent material** glossary entry. The GitHub issue form is this repository's implementation of the convention; repositories on other hosts replicate it natively.

### Modified Capabilities
- `adopter-onboarding`: Bootstrap distribution extends to carry the issue form alongside validate.yml — `.github/ISSUE_TEMPLATE/` joins the copy-list entries in the README quick start and `docs/setup.md` as a host-conditional item (GitHub-hosted adopters copy it at bootstrap; repositories on other hosts get the named convention), and the divergence manifest in `docs/maintainer.md` gains the framing row.
- `governance-docs`: The kit-layering routing rule is recorded as a durable ADR with the schema-fork trigger conditions, referenced from CONTRIBUTING.md's "Where Decisions Live" section and `docs/maintainer.md`'s Repository Configuration section.

## Impact

- New files: `.github/ISSUE_TEMPLATE/change.yml`, `.github/ISSUE_TEMPLATE/config.yml`, ADR-0008 under `adr/`.
- Modified files: `docs/intent-prompt-guidelines.md` (new section, same path), `CONTRIBUTING.md`, `AGENTS.md`, `README.md`, `docs/setup.md`, `docs/maintainer.md`, `glossary/domain.md`.
- Specs: adds the `issue-authoring` spec — a new **common capability** of the **OpenSpec Store**, injected read-only into every connected **experiment repository**'s artifact workflows — and extends `adopter-onboarding` and `governance-docs` additively. No breaking changes.
- No runtime code, schema files, skills, commands, or CI workflows change; the intent-driven schema is not forked (the ADR records the fork trigger conditions instead), and `.github/workflows/validate.yml` is untouched.
- The docs-site spec's path-pinning of `docs/intent-prompt-guidelines.md` is respected — a section is added, the path does not move.
- New form and guidance copy remains **org-neutral**, naming no organization-specific process.
