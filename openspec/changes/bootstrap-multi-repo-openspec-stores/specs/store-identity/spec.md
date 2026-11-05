# OpenSpec Store Identity

## ADDED Requirements

### Requirement: OpenSpec Store identity metadata
The hep-metadex repository SHALL include **OpenSpec Store** identity metadata at `.openspec-store/store.yaml` declaring the id `hep-metadex`.

#### Scenario: Doctor confirms OpenSpec Store metadata

```gherkin
Given the hep-metadex repository on a machine where it is registered as an OpenSpec store
When a maintainer runs openspec doctor from the repository root
Then the doctor output reports the OpenSpec store hep-metadex with valid metadata
```

### Requirement: In-place OpenSpec Store content
Conversion to an **OpenSpec Store** MUST NOT move, rename, or delete any existing path under `openspec/`; the **OpenSpec Store**'s specs, changes, and schema continue to live in the existing tree.

#### Scenario: Existing tree is untouched by conversion

```gherkin
Given the hep-metadex repository with its existing openspec tree
When the OpenSpec Store identity metadata is added
Then git status reports no modifications to any pre-existing path under openspec
```

### Requirement: Org-neutral OpenSpec Store id
The **OpenSpec Store** id MUST be `hep-metadex` and MUST NOT name any GitHub organization, so that a hosting move requires no rename or re-registration.

#### Scenario: Identity survives a hosting move

```gherkin
Given the OpenSpec store registered on a contributor machine under the id hep-metadex
When the repository's git remote moves to a different GitHub organization
Then the store id and every store reference that selects it remain valid
```

### Requirement: Common-spec change routing
An improvement to a **common capability** SHALL be proposable from any directory with `openspec new change <change> --store hep-metadex`, and the resulting change MUST land in the **OpenSpec Store** repository's `openspec/changes/` without writing to any **experiment repository**.

#### Scenario: Proposing a common-spec change from an experiment checkout

```gherkin
Given the hep-metadex OpenSpec store registered on a machine with a dune-metadex checkout
When a contributor runs openspec new change improve-provenance --store hep-metadex from the dune-metadex directory
Then the change is created under the OpenSpec store's openspec/changes directory
And the dune-metadex working tree is unchanged
```
