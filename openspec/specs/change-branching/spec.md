# Change Branching Specification

## Purpose

Defines where a change's work lands — an **issue branch** (`<issue-number>-<change-slug>`) cut from `main` before the change's first commit, change work reaching `main` only by pull-request merge (the archive phase's direct metadata commit excepted), the no-auto-git consent rule and phase sequence the `openspec-git-discipline` gates preserve, and the maintainer-docs record that keeps a template sync from silently reverting the forked gates.

## Requirements

### Requirement: Issue branch cut before a change's first commit
Every new change SHALL run on an **issue branch** — `<issue-number>-<change-slug>` cut from `main` before the change's first commit. The branch is created ask-first as part of the requested propose workflow: a decline keeps the standing escape hatch — warn and ask whether to continue intentionally — and no branch or commit is created without the user's consent.

#### Scenario: Propose begins on the issue branch

```gherkin
Given issue #42 tracking a new change add-data-catalog and a clean main
When a contributor or agent starts the propose workflow and accepts the gate's branch step
Then the change's work happens on the branch 42-add-data-catalog cut from main
And no commit for the change has landed on main
```

#### Scenario: Declining the branch keeps the escape hatch

```gherkin
Given the propose workflow offering to cut the issue branch
When the user declines the branch
Then the agent warns and asks whether to continue intentionally
And creates no branch and no commit
```

### Requirement: Change work reaches main only by pull-request merge
A change's planning and implementation commits SHALL reach `main` only by pull-request merge; change work SHALL NOT be committed directly on `main`. The archive phase's direct metadata commit on `main` is lifecycle bookkeeping, not change work, and remains as documented in `docs/usage.md`.

#### Scenario: Planning commits reach main by merge

```gherkin
Given the change's planning artifacts committed on the branch 42-add-data-catalog
When the planning pull request merges into main
Then the change's commits are on main by merge
And apply may start from that main
```

#### Scenario: The archive metadata commit stays direct on main

```gherkin
Given the change's implementation merged back into main
When archive runs from main
Then the sync-and-archive metadata commit lands directly on main carrying Closes #42
And it is the change's only direct commit on main, as lifecycle bookkeeping rather than change work
```

### Requirement: After propose opens the PR from the existing branch
The after-propose gate SHALL offer the planning pull request from the issue branch that already exists, and SHALL NOT offer to create a branch at that point.

#### Scenario: The planning PR is offered from the issue branch

```gherkin
Given the completed planning artifacts on the branch 42-add-data-catalog
When the after-propose checkpoint runs
Then the user is asked to commit any uncommitted artifacts
And offered the planning pull request from 42-add-data-catalog
```

### Requirement: Phase sequence and merge discipline preserved
The amended gates SHALL NOT alter the skill's core rule, phase sequence, apply gate, or archive gate: propose and continue artifacts still merge to `main` before apply starts, apply still begins only from a `main` that contains the proposal, and archive still runs from `main` after the implementation merges back.

#### Scenario: The apply gate is unchanged

```gherkin
Given a proposal change that exists only on a branch and not on main
When apply is requested
Then the agent refuses to start apply
And asks for the planning merge to main first
```

#### Scenario: The archive gate is unchanged

```gherkin
Given implementation work that has not merged back into main
When archive is requested
Then the agent stops and asks for the implementation merge first
```

### Requirement: No-auto-git rule intact
The amendment SHALL preserve the skill's consent rule — never create commits, branches, or merges unless the user explicitly asks. The amended gates direct where a change's work lands; they do not authorize git actions without the user's ask.

#### Scenario: The gate names the destination without acting

```gherkin
Given an agent session in the propose workflow for a new change
When the user has not asked for any git action
Then no commit, branch, or merge is created
And the gate names the issue branch as where the change's work will land once the user asks
```

### Requirement: Fork recorded and recoverable in maintainer guidance
`docs/maintainer.md` SHALL record the `openspec-git-discipline` gate amendment in its divergence manifest as a fork of a vendored skill, and its drift-impact guidance SHALL state the recovery procedure: hand-merge upstream changes into `.agents/skills/openspec-git-discipline/` and re-apply the two amended gates after any sync, because a naive sync silently reverts them.

#### Scenario: A maintainer finds the fork in the divergence manifest

```gherkin
Given the divergence manifest in docs/maintainer.md
When a maintainer looks for the openspec-git-discipline skill
Then a row records the two amended gates as a deliberate fork of a vendored skill with its reason
```

#### Scenario: A template sync survives the drift-impact guidance

```gherkin
Given a template sync that overwrote .agents/skills/openspec-git-discipline/
When the maintainer follows the drift-impact entry
Then upstream changes are hand-merged into the skill
And the two amended gates are re-applied so the issue-branch policy survives the sync
```

### Requirement: Contributor and agent surfaces carry the naming rule
`CONTRIBUTING.md`'s pull-request section SHALL carry the `<issue-number>-<change-slug>` naming rule for a change's planning branch — the documented `<issue>-apply-<change>` implementation pattern is unchanged — and `AGENTS.md` SHALL carry a one-line pointer to the issue-branch convention so agent sessions see it without loading the skill.

#### Scenario: A contributor finds the naming rule

```gherkin
Given the pull-request section of CONTRIBUTING.md
When a contributor prepares the planning pull request for issue #42's change add-data-catalog
Then the section tells them to branch from main as 42-add-data-catalog before the change's first commit
```

#### Scenario: An agent session sees the convention without the skill

```gherkin
Given an agent session that has read AGENTS.md but not loaded the openspec-git-discipline skill
When the session starts work on a new change
Then AGENTS.md states the issue-branch convention naming the branch pattern
```
