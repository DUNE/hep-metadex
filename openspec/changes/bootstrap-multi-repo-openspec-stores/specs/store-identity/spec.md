# Store Identity

## ADDED Requirements

### Requirement: Store identity metadata
The hep-metadex repository SHALL include OpenSpec store identity metadata at `.openspec-store/store.yaml` declaring the store id `hep-metadex`.

#### Scenario: Doctor confirms store metadata

```gherkin
Given the hep-metadex repository on a machine where it is registered as a store
When a maintainer runs openspec doctor from the repository root
Then the doctor output reports the store hep-metadex with valid metadata
```

### Requirement: In-place store content
Conversion to a **Store** MUST NOT move, rename, or delete any existing path under `openspec/`; the store's specs, changes, and schema continue to live in the existing tree.

#### Scenario: Existing tree is untouched by conversion

```gherkin
Given the hep-metadex repository with its existing openspec tree
When the store identity metadata is added
Then git status reports no modifications to any pre-existing path under openspec
```

### Requirement: Org-neutral store id
The store id MUST be `hep-metadex` and MUST NOT name any GitHub organization, so that a hosting move requires no rename or re-registration.

#### Scenario: Identity survives a hosting move

```gherkin
Given the store registered on a contributor machine under the id hep-metadex
When the repository's git remote moves to a different GitHub organization
Then the store id and every references declaration that selects it remain valid
```

### Requirement: Common-spec change routing
An improvement to a **common capability** SHALL be proposable from any directory with `openspec new change <change> --store hep-metadex`, and the resulting change MUST land in the **Store** repository's `openspec/changes/` without writing to any **experiment repository**.

#### Scenario: Proposing a common-spec change from an experiment checkout

```gherkin
Given the hep-metadex store registered on a machine with a dune-metadex checkout
When a contributor runs openspec new change improve-provenance --store hep-metadex from the dune-metadex directory
Then the change is created under the store's openspec/changes directory
And the dune-metadex working tree is unchanged
```
