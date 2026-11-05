# Governance Docs

## ADDED Requirements

### Requirement: Org-agnostic governance text
Governance and contribution documents SHALL be written **org-neutral** — naming no experiment-specific or organization-specific processes — so that a hosting move is purely an infrastructure event.

#### Scenario: A hosting move requires no governance edits

```gherkin
Given the governance and contribution documents as written by this change
When the repository transfers to a different GitHub organization
Then no governance or contribution text needs editing as a result of the move
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
