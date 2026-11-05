# Adopter Onboarding

## ADDED Requirements

### Requirement: Quick start from a fresh repository
The README SHALL provide an adopter-facing quick start that takes a newcomer from a fresh **experiment repository** to a connected one — **scaffolding** installed, **Reference** declared, doctor green — without requiring any other document.

#### Scenario: A stranger bootstraps an experiment repository

```gherkin
Given a newcomer with a fresh experiment repository and a machine with git and the OpenSpec CLI
When the newcomer follows the README quick start
Then the repository contains the installed scaffolding and an openspec config declaring the hep-metadex reference
And openspec doctor verifies the store reference
```

### Requirement: Documented usage flows
`docs/setup.md` SHALL document the **Store** layout and **experiment repository** configuration. `docs/usage.md` SHALL document change-time work (an experiment proposing and implementing its own change with store context injected) and write-back (proposing a **common capability** improvement into the **Store** via `--store hep-metadex`).

#### Scenario: A reader finds the write-back flow

```gherkin
Given the adopter documentation set as delivered by this change
When a reader wants to propose an improvement to a common capability spec
Then docs/usage.md describes the write-back flow including the openspec command that names the store
```

### Requirement: Maintainer content preserved
The README rewrite MUST absorb existing maintainer content — template provenance, the divergence manifest, and update-from-upstream guidance — into the documentation set rather than deleting it.

#### Scenario: Provenance guidance survives the rewrite

```gherkin
Given the pre-change README documenting template provenance and the divergence manifest
When the README rewrite lands
Then a reader can still find the provenance baseline and the divergence manifest within the repository documentation
```
