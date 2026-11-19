# Workflow Action Pinning

## ADDED Requirements

### Requirement: One unified checkout pin across checkout-using workflows
Every GitHub Actions workflow in the repository that uses `actions/checkout` SHALL pin it at one unified major version — the same major in every such workflow — so a version move is a coordinated, repository-wide edit rather than per-file drift. The unified pin SHALL move only as one coordinated change across every checkout-using workflow: a move in some of them and not others violates this requirement. The invariant reaches only workflows that use `actions/checkout` — a workflow with no checkout step is neither conforming nor violating — and it governs the checkout action pin alone, not the OpenSpec CLI pin in `validate.yml` or any other version pin.

#### Scenario: The repository's workflows carry one checkout pin

```gherkin
Given the repository's workflows release.yml, validate.yml, docs.yml, and kit-reminder.yml
When a reader lists the actions/checkout pin in each workflow
Then every workflow pins actions/checkout at the same major version
```

#### Scenario: A pin move in one workflow only breaks the invariant

```gherkin
Given the repository's checkout-using workflows pinning actions/checkout at one unified major version
When a change moves the checkout pin in one workflow and leaves the others
Then the repository no longer carries one unified checkout pin
And restoring conformance takes the same coordinated move in every checkout-using workflow
```

#### Scenario: A new workflow adopts the unified pin

```gherkin
Given the repository's checkout-using workflows pinning actions/checkout at one unified major version
When a change adds a workflow that checks out the repository
Then the new workflow pins actions/checkout at that same unified major version
```

#### Scenario: A workflow without a checkout step is outside the invariant

```gherkin
Given a workflow in the repository that never uses actions/checkout
When the unified pin invariant is evaluated over the repository's workflows
Then the workflow is neither conforming nor violating
```

### Requirement: The unified pin stays a GitHub-created action
The unified checkout pin SHALL name a GitHub-created action, per the DUNE organization's Actions policy: only actions owned by DUNE, created by GitHub, or on the organization's allowlist may run in this repository's workflows, and `actions/checkout` qualifies at every major version. Moving the unified pin to another major of `actions/checkout` keeps this requirement satisfied by construction; replacing the checkout action with one outside the policy's allowed set violates it.

#### Scenario: The unified pin qualifies under the policy

```gherkin
Given the DUNE organization's Actions policy allowing only DUNE-owned, GitHub-created, or allowlisted actions
When the unified checkout pin names actions/checkout at its current major
Then the pin satisfies the policy because actions/checkout is a GitHub-created action
```

#### Scenario: A replacement action outside the policy does not land

```gherkin
Given the unified checkout pin held by a GitHub-created action
When a change proposes replacing actions/checkout with an action that is neither DUNE-owned, GitHub-created, nor on the organization's allowlist
Then the proposal violates the pin constraint
And the repository's workflows keep actions/checkout
```
