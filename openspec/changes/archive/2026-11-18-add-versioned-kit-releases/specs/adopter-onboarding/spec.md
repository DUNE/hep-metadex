# Adopter Onboarding

## MODIFIED Requirements

### Requirement: Quick start from a fresh repository
The README SHALL provide an adopter-facing quick start that takes a newcomer from a fresh **experiment repository** to a connected one — **workflow scaffolding** installed from a versioned kit release (checksum-verified and provenance-stamped), **Store reference** declared, doctor green, spec-validation CI and the issue form in place per the adopter's host — without requiring any other document. The quick start MUST claim a bootstrap step only once the worked example, dune-metadex, has verified it: the **experiment repository** gains the spec-validation workflow and the issue form before the documentation claims them as steps.

#### Scenario: A stranger bootstraps an experiment repository

```gherkin
Given a newcomer with a fresh experiment repository and a machine with git and the OpenSpec CLI
When the newcomer follows the README quick start
Then the repository contains the installed workflow scaffolding and an openspec config declaring the hep-metadex store reference
And the installed kit carries the version file of the release it came from
And openspec doctor verifies the store reference
```

#### Scenario: The quick start installs a verified kit from a release

```gherkin
Given the README quick start naming a kit release
When the newcomer follows its kit-install steps
Then the kit arrives from that release's bundle
And its checksums verify against the release's SHA256SUMS
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

### Requirement: Host-conditional spec-validation CI in the bootstrap documentation
The bootstrap documentation — `docs/setup.md` and the agent-assisted bootstrap prompt — SHALL present spec-validation CI as a bootstrap step conditional on the adopter's host. GitHub-hosted **experiment repositories** copy the provided GitHub Actions workflow from the kit release bundle; repositories on other hosts wire the equivalent `valid: true` gate into their own CI, with the gate named but not implemented for them.

#### Scenario: A GitHub-hosted repository copies the provided workflow

```gherkin
Given a GitHub-hosted experiment repository being bootstrapped with the agent-assisted prompt
When the agent performs the bootstrap CI step
Then it copies the provided GitHub Actions workflow from the kit release bundle into the repository
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

### Requirement: Host-conditional issue form in the bootstrap documentation
The bootstrap documentation — `docs/setup.md` and the agent-assisted bootstrap prompt — SHALL present the issue form as a bootstrap step conditional on the adopter's host: `.github/ISSUE_TEMPLATE/` (the form and its config, one copy-list item) is copied by GitHub-hosted **experiment repositories** from the kit release bundle; repositories on other hosts replicate the convention natively in their own issue tracker, named but not implemented for them — the ADR-0005 pattern.

#### Scenario: A GitHub-hosted repository copies the issue form

```gherkin
Given a GitHub-hosted experiment repository being bootstrapped with the agent-assisted prompt
When the agent performs the bootstrap issue-form step
Then it copies .github/ISSUE_TEMPLATE/ from the kit release bundle into the same path in the repository
And new issues in that repository open through the intent-material form with the blank-issue path disabled
```

#### Scenario: A repository on another host replicates the convention natively

```gherkin
Given an experiment repository hosted on a platform other than GitHub
When a reader follows the bootstrap documentation's issue-form step
Then the documentation names the intent-material issue convention to replicate in that host's own issue tracker
And the documentation ships no issue-form implementation for that host
```

## ADDED Requirements

### Requirement: Divergence manifest frames the kit release artifacts
The divergence-manifest entries for the kit version file and the release workflow SHALL present the version file as a **workflow scaffolding** component adopters install at bootstrap from the kit release bundle, and the release workflow as repo-local automation that never ships in the kit.

#### Scenario: An adopter reads the version file's manifest entry

```gherkin
Given the divergence manifest in the maintainer guide
When an adopter reads the entry for the kit version file
Then the entry presents it as a kit component installed from the release bundle
And a maintainer syncing from the template preserves it as an intentional divergence
```

#### Scenario: A reader sees the release workflow marked repo-local

```gherkin
Given the divergence manifest in the maintainer guide
When a reader reads the entry for the release workflow
Then the entry presents it as repo-local automation that never ships in the kit
```
