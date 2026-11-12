# Adopter Onboarding Specification

## Purpose

Defines the documented path a newcomer follows to adopt the **OpenSpec Store** and install the **workflow scaffolding** — quick start, setup, **change-time work**, **write-back**, and contributing.

## Requirements

### Requirement: Quick start from a fresh repository
The README SHALL provide an adopter-facing quick start that takes a newcomer from a fresh **experiment repository** to a connected one — **workflow scaffolding** installed, **Store reference** declared, doctor green, spec-validation CI and the issue form in place per the adopter's host — without requiring any other document. The quick start MUST claim a bootstrap step only once the worked example, dune-metadex, has verified it: the **experiment repository** gains the spec-validation workflow and the issue form before the documentation claims them as steps.

#### Scenario: A stranger bootstraps an experiment repository

```gherkin
Given a newcomer with a fresh experiment repository and a machine with git and the OpenSpec CLI
When the newcomer follows the README quick start
Then the repository contains the installed workflow scaffolding and an openspec config declaring the hep-metadex store reference
And openspec doctor verifies the store reference
```

#### Scenario: A GitHub-hosted newcomer ends the quick start with a validation gate

```gherkin
Given a newcomer with a fresh GitHub-hosted experiment repository
When the newcomer follows the README quick start through its CI step
Then the repository contains the spec-validation workflow alongside the installed workflow scaffolding
And the workflow runs openspec validate --all over all specs and changes, gating on valid: true
```

#### Scenario: The claimed CI step is verified on the worked example

```gherkin
Given the README quick start claiming the spec-validation CI step
When a visitor checks dune-metadex, the worked example the quick start cites
Then the spec-validation workflow is present in that repository
And its CI gates openspec validate --all on valid: true
```

#### Scenario: The claimed issue-form step is verified on the worked example

```gherkin
Given the README quick start claiming the issue-form step
When a visitor checks dune-metadex, the worked example the quick start cites
Then the issue form and its config are present in that repository
And its new issues open through the intent-material form
```

### Requirement: Documented usage flows
`docs/setup.md` SHALL document the **OpenSpec Store** layout and **experiment repository** configuration. `docs/usage.md` SHALL document **change-time work** (an experiment proposing and implementing its own change with **OpenSpec Store** context injected) and **write-back** (proposing a **common capability** improvement into the **OpenSpec Store** via `--store hep-metadex`).

#### Scenario: A reader finds the write-back flow

```gherkin
Given the adopter documentation set as delivered by this change
When a reader wants to propose an improvement to a common capability spec
Then docs/usage.md describes the write-back flow including the openspec command that names the OpenSpec store
```

### Requirement: Maintainer content preserved
The README rewrite MUST absorb existing maintainer content — template provenance, the divergence manifest, and update-from-upstream guidance — into the documentation set rather than deleting it.

#### Scenario: Provenance guidance survives the rewrite

```gherkin
Given the pre-change README documenting template provenance and the divergence manifest
When the README rewrite lands
Then a reader can still find the provenance baseline and the divergence manifest within the repository documentation
```

### Requirement: Host-conditional spec-validation CI in the bootstrap documentation
The bootstrap documentation — `docs/setup.md` and the agent-assisted bootstrap prompt — SHALL present spec-validation CI as a bootstrap step conditional on the adopter's host. GitHub-hosted **experiment repositories** copy the provided GitHub Actions workflow from the hep-metadex checkout; repositories on other hosts wire the equivalent `valid: true` gate into their own CI, with the gate named but not implemented for them.

#### Scenario: A GitHub-hosted repository copies the provided workflow

```gherkin
Given a GitHub-hosted experiment repository being bootstrapped with the agent-assisted prompt
When the agent performs the bootstrap CI step
Then it copies the provided GitHub Actions workflow from the hep-metadex checkout into the repository
And the workflow runs openspec validate --all over all specs and changes, gating on valid: true
And the workflow pins the OpenSpec CLI to 1.16.0
```

#### Scenario: A repository on another host wires the named equivalent gate

```gherkin
Given an experiment repository hosted on a platform other than GitHub
When a reader follows the bootstrap documentation's CI step
Then the documentation names the equivalent valid: true gate to wire into that host's own CI
And the documentation ships no CI implementation for that host
```

### Requirement: Divergence manifest frames the validation workflow as scaffolding for GitHub hosts
The divergence-manifest entry for `.github/workflows/validate.yml` SHALL present the workflow as a component of **workflow scaffolding** that GitHub-hosted adopters copy at bootstrap, while remaining recorded as an intentional divergence from the intent-driven template.

#### Scenario: An adopter reads the workflow's manifest entry

```gherkin
Given the divergence manifest in the maintainer guide
When an adopter reads the entry for the spec-validation workflow
Then the entry presents the workflow as scaffolding that GitHub-hosted adopters copy at bootstrap
And a maintainer syncing from the template preserves it as an intentional divergence
```

### Requirement: Host-conditional issue form in the bootstrap documentation
The bootstrap documentation — `docs/setup.md` and the agent-assisted bootstrap prompt — SHALL present the issue form as a bootstrap step conditional on the adopter's host: `.github/ISSUE_TEMPLATE/` (the form and its config, one copy-list item) is copied by GitHub-hosted **experiment repositories** from the hep-metadex checkout; repositories on other hosts replicate the convention natively in their own issue tracker, named but not implemented for them — the ADR-0005 pattern.

#### Scenario: A GitHub-hosted repository copies the issue form

```gherkin
Given a GitHub-hosted experiment repository being bootstrapped with the agent-assisted prompt
When the agent performs the bootstrap issue-form step
Then it copies .github/ISSUE_TEMPLATE/ from the hep-metadex checkout into the same path in the repository
And new issues in that repository open through the intent-material form with the blank-issue path disabled
```

#### Scenario: A repository on another host replicates the convention natively

```gherkin
Given an experiment repository hosted on a platform other than GitHub
When a reader follows the bootstrap documentation's issue-form step
Then the documentation names the intent-material issue convention to replicate in that host's own issue tracker
And the documentation ships no issue-form implementation for that host
```

### Requirement: Divergence manifest frames the issue form as scaffolding for GitHub hosts
The divergence-manifest entry for `.github/ISSUE_TEMPLATE/` SHALL present the issue form as a component of **workflow scaffolding** that GitHub-hosted adopters copy at bootstrap, while remaining recorded as an intentional divergence from the intent-driven template.

#### Scenario: An adopter reads the issue form's manifest entry

```gherkin
Given the divergence manifest in the maintainer guide
When an adopter reads the entry for the issue form
Then the entry presents .github/ISSUE_TEMPLATE/ as scaffolding that GitHub-hosted adopters copy at bootstrap
And a maintainer syncing from the template preserves it as an intentional divergence
```
