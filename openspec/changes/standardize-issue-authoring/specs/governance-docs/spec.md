# Governance Docs

## ADDED Requirements

### Requirement: Kit-layering routing rule recorded
The repository SHALL carry a durable ADR under `adr/` recording the kit-layering routing rule — the schema for artifact structure inside changes, `openspec/config.yaml` rules for per-stage discipline, skills for agent-triggered discipline, commands for procedure automation, the intent-prompt guidelines doc for authoring guidance, and `.github/` for host-conditional automation — and the trigger conditions for forking the intent-driven schema.

#### Scenario: The ADR maps each convention class to its home

```gherkin
Given the routing-rule ADR under adr/
When a reader looks up where a workflow convention belongs
Then it maps each convention class to its layer in the kit
And it records the trigger conditions for forking the intent-driven schema
```

### Requirement: Routing rule referenced from contributor and maintainer surfaces
CONTRIBUTING.md's "Where Decisions Live" section and `docs/maintainer.md`'s Repository Configuration section SHALL reference the routing-rule ADR.

#### Scenario: A contributor finds the routing rule from the contribution policy

```gherkin
Given a contributor deciding where a new workflow convention should live
When they read the Where Decisions Live section of CONTRIBUTING.md
Then it references the routing-rule ADR
```

#### Scenario: A maintainer reaches the routing rule from the maintainer guide

```gherkin
Given the Repository Configuration section of docs/maintainer.md
When a maintainer looks for how the kit's layers divide responsibility
Then the section references the routing-rule ADR
```
