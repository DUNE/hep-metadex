# Experiment References Specification

## Purpose

Defines how an **experiment repository** connects read-only to the **OpenSpec Store** — declaring a `references:` block in its `openspec/config.yaml`, receiving the store's **spec index** in artifact workflows, and never declaring the write-routing `store:` line.

## Requirements

### Requirement: Read-only connection declaration
An **experiment repository** SHALL declare its connection to the **OpenSpec Store** in a `references:` block of its `openspec/config.yaml`, and MUST NOT declare the write-routing `store:` line.

#### Scenario: A connected experiment repository passes doctor

```gherkin
Given dune-metadex whose openspec config declares a reference to the hep-metadex OpenSpec store
And the hep-metadex OpenSpec store registered on the same machine
When a contributor runs openspec doctor in the dune-metadex repository
Then the doctor output reports the hep-metadex reference as ok
```

#### Scenario: The config contains no write-routing line

```gherkin
Given dune-metadex whose openspec config declares a reference to the hep-metadex OpenSpec store
When a reviewer inspects openspec/config.yaml
Then it contains a references entry selecting the OpenSpec store by id
And it contains no store line
```

### Requirement: Spec index injection
When an artifact workflow runs in a connected **experiment repository**, its instructions SHALL include the **OpenSpec Store**'s **spec index** — each **common capability** with a one-line summary and the exact command to fetch it.

#### Scenario: A change workflow sees the OpenSpec Store's specs

```gherkin
Given dune-metadex connected to a hep-metadex OpenSpec store that publishes a provenance spec
When an artifact workflow creates a change artifact in dune-metadex
Then the workflow instructions list provenance with a one-line summary
And include the fetch command that names the hep-metadex OpenSpec store
```

### Requirement: Experiment-local artifact routing
A change created in a connected **experiment repository** without `--store` MUST land in that repository's own `openspec/changes/`, leaving the **OpenSpec Store** untouched.

#### Scenario: A local change stays local

```gherkin
Given dune-metadex connected to the hep-metadex OpenSpec store
When a contributor runs openspec new change add-dune-catalog without a store flag
Then the change is created under dune-metadex/openspec/changes
And the hep-metadex OpenSpec store working tree is unchanged
```

### Requirement: Advisory remote for unregistered machines
A **Store reference** declaration SHALL include the **OpenSpec Store**'s clone URL so that `openspec doctor` can produce a pasteable clone-and-register fix on machines where the OpenSpec Store is not yet registered.

#### Scenario: Doctor guides a fresh machine

```gherkin
Given a machine where the hep-metadex OpenSpec store is not registered
And dune-metadex whose store reference declaration includes the OpenSpec store's clone URL
When a contributor runs openspec doctor in the dune-metadex repository
Then the output names the missing OpenSpec store with a pasteable clone and register fix
```
