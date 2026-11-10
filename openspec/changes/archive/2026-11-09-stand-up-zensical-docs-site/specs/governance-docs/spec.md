# Governance Docs

## MODIFIED Requirements

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

## ADDED Requirements

### Requirement: Documentation row cites the published site
The Documentation row of the HSF checklist mapping in `docs/hsf-affiliation.md` SHALL cite the live **documentation site** URL alongside the repository's README and `docs/` citations.

#### Scenario: An evaluator reaches the site from the checklist

```gherkin
Given docs/hsf-affiliation.md as delivered by this change
When an evaluator reads the Documentation row of the required-guideline checklist
Then the row cites the live documentation site URL alongside the README and docs citations
```
