# Governance Docs Specification

## Purpose

Defines the repository's governance and contribution documents — decision rights and a review bar backed by spec-validation CI, the **org-neutral** hosting roadmap, and the **HSF affiliation** path with its checklist mapping.

## Requirements

### Requirement: Org-agnostic governance text
Governance and contribution documents SHALL be written **org-neutral** — naming no experiment-specific or organization-specific processes — so that a hosting move is purely an infrastructure event. Factual hosting citations — the public-repository URL the checklist already carries, and the live **documentation site** URL added to the HSF checklist's Documentation row — are infrastructure facts rather than processes: they MAY name the current hosting organization, and they are updated as part of a hosting move's infrastructure work.

#### Scenario: A hosting move requires no governance edits

```gherkin
Given the governance and contribution documents as written by this change
When the repository transfers to a different GitHub organization
Then no governance or contribution process text needs editing as a result of the move
And only the factual hosting citations change, as infrastructure facts
```

#### Scenario: The checklist's site citation follows a hosting move

```gherkin
Given the Documentation row of the HSF checklist citing the live documentation site URL
When the repository transfers to a different GitHub organization
Then the site citation is updated alongside the public-repository citation as part of the move
And no governance or contribution process text is touched
```

### Requirement: Hosting roadmap recorded
`docs/governance.md` SHALL record the hosting roadmap: incubation in the DUNE organization, HSF Steering Group endorsement as the trigger for **HSF affiliation**, and HSF-organization hosting as a separate, optional, mutually-agreed follow-on.

#### Scenario: A reader finds the hosting roadmap

```gherkin
Given docs/governance.md as delivered by this change
When a reader looks for where the OpenSpec store is hosted and what would change that
Then the document names the incubating organization and the endorsement trigger
And presents HSF-organization hosting as a distinct follow-on decision
```

### Requirement: HSF checklist mapping
`docs/hsf-affiliation.md` SHALL map every required HSF affiliated-project guideline — public repository, suitable name, open-source license, installation instructions, documentation, test suite, contributor openness, issue tracking, and general information — to the place in this repository where it is satisfied.

#### Scenario: Every required checklist item is mapped

```gherkin
Given docs/hsf-affiliation.md as delivered by this change
When an evaluator walks the HSF required guidelines
Then each guideline has an entry naming where this repository satisfies it
```

### Requirement: Apache-2.0 license recorded as a divergence
The repository SHALL carry an Apache-2.0 `LICENSE` file, and the README divergence manifest SHALL record it as a deliberate divergence from the intent-driven template's MIT license.

#### Scenario: The license and its record are discoverable

```gherkin
Given the repository as delivered by this change
When a visitor or automated license check examines the repository root
Then an Apache-2.0 LICENSE file is present
And the divergence manifest records the deliberate divergence from the template's MIT license
```

### Requirement: Spec-validation CI
Continuous integration SHALL run `openspec validate` over all specs and changes and fail when validation reports any artifact invalid.

#### Scenario: An invalid change fails CI

```gherkin
Given a pull request that adds a spec file failing strict validation
When continuous integration runs on the pull request
Then the validation workflow fails
```

#### Scenario: A valid repository passes CI

```gherkin
Given the repository with all specs and changes passing strict validation
When continuous integration runs
Then the validation workflow succeeds
```

### Requirement: Documentation row cites the published site
The Documentation row of the HSF checklist mapping in `docs/hsf-affiliation.md` SHALL cite the live **documentation site** URL alongside the repository's README and `docs/` citations.

#### Scenario: An evaluator reaches the site from the checklist

```gherkin
Given docs/hsf-affiliation.md as delivered by this change
When an evaluator reads the Documentation row of the required-guideline checklist
Then the row cites the live documentation site URL alongside the README and docs citations
```

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
