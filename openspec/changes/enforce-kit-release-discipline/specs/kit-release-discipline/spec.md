# Kit Release Discipline

## ADDED Requirements

### Requirement: Review-time advisory reminder
The repository SHALL carry a repo-local reminder workflow — never part of the **workflow scaffolding** — that runs on pull requests: when a pull request's diff alters kit copy-list paths (the paths the `KIT-MANIFEST.yaml` `paths:` block lists) without a corresponding **Kit version file** version bump, it posts an advisory annotation naming the remedy — bump the kit version file so a release is cut on merge. The reminder MUST be advisory: it MUST NOT block merge, and it MUST NOT render a failing check status on the pull request.

#### Scenario: A kit change without a bump draws the advisory

```gherkin
Given an open pull request whose diff alters kit copy-list paths
And the diff does not change the version in the kit version file
When the reminder check runs on the pull request
Then it posts the advisory naming the remedy: bump the kit version file so a release is cut on merge
```

#### Scenario: The reminder never blocks the merge

```gherkin
Given a pull request on which the reminder has posted its advisory
When a maintainer merges the pull request without acting on it
Then the merge succeeds
And the pull request's checks show no failing status from the reminder
```

#### Scenario: A kit change with its bump draws no advisory

```gherkin
Given an open pull request whose diff alters kit copy-list paths
And the diff bumps the version in the kit version file
When the reminder check runs on the pull request
Then it posts no advisory
```

#### Scenario: A change outside the kit copy-list draws no advisory

```gherkin
Given an open pull request whose diff touches no kit copy-list paths
When the reminder check runs on the pull request
Then it posts no advisory
```

### Requirement: Archive-time release-containment gate
The archive phase SHALL run a release-containment gate before archiving a change whose implementation is merged to `main`: when the change's merged diff touched kit copy-list paths, a published **Kit release** MUST contain those changes before the change archives. On failure the gate MUST print a pasteable fix naming the exact remedy for the diagnosed cause — bump the **Kit version file**, merge, and the release cuts, for a forgotten bump; re-run the release workflow via `workflow_dispatch`, for a misfired release run — and the archive workflow MUST refuse to archive. A change whose merged diff touched no kit copy-list paths MUST pass the gate without requiring any release.

#### Scenario: The archive workflow runs the gate

```gherkin
Given a change whose implementation is merged back into main
When the archive phase begins
Then the archive workflow runs the release-containment gate before archiving
```

#### Scenario: A forgotten bump blocks the archive

```gherkin
Given a change whose merged diff touched kit copy-list paths
And no published kit release contains those changes because the version was never bumped
When the gate runs
Then it fails and prints the fix: bump the kit version file, merge, and the release cuts
And the archive workflow refuses to archive the change
```

#### Scenario: A misfired release run gets the re-run fix

```gherkin
Given a change whose merged diff bumped the kit version file
And the release workflow run misfired so no release published
When the gate runs
Then it fails and prints the fix: re-run the release workflow via workflow_dispatch
And it does not advise a second version bump
```

#### Scenario: A contained change archives

```gherkin
Given a change whose merged diff touched kit copy-list paths
And a published kit release contains those changes
When the gate runs
Then it passes and the archive proceeds
```

#### Scenario: A zero-kit-path change passes trivially

```gherkin
Given a change whose merged diff touched no kit copy-list paths
When the gate runs
Then it passes without requiring any published release
```

#### Scenario: A later increment is not contained by an earlier release

```gherkin
Given a change that bumped the kit version file and merged a first increment
And a published kit release contains the first increment
When a later increment touching kit copy-list paths merges without its own bump
Then the gate fails because the published release does not contain the later increment
And the fix names a new version bump whose release will contain it
```

### Requirement: Single-source copy-list
The kit copy-list definition SHALL live in one place — the `KIT-MANIFEST.yaml` `paths:` block — and the release workflow, the reminder, and the gate SHALL all derive their kit-path set from it. The release workflow's bundle assembly SHALL read the same definition, and the bundle it assembles MUST be identical in contents and member paths to the bundle the previously inlined list produced.

#### Scenario: All three consumers read the manifest

```gherkin
Given the KIT-MANIFEST paths block as the kit copy-list definition
When the release workflow assembles a bundle, the reminder detects kit-path changes, and the gate evaluates containment
Then all three derive their kit-path set from the manifest's paths block
```

#### Scenario: The derived bundle is unchanged

```gherkin
Given the release workflow deriving its bundle list from the manifest
When it assembles the kit bundle for a release
Then the bundle's contents and member paths are identical to those the previously inlined list produced
```

#### Scenario: A copy-list change reaches every consumer

```gherkin
Given a later change adding a path to the manifest's paths block
When the release workflow, the reminder, and the gate next run
Then all three see the added path without any separate list edit
```

### Requirement: Enforcement documentation in the maintainer guide
`docs/maintainer.md`'s release-process section SHALL document both mechanisms: the reminder's advisory, never-blocking role at review time, and the gate's place in the archive phase with its per-cause pasteable fixes. The divergence manifest SHALL record the reminder workflow and the gate script as repo-local maintainer automation that never ships in the **workflow scaffolding**.

#### Scenario: A maintainer finds the reminder documented

```gherkin
Given the release-process section of docs/maintainer.md
When a maintainer reviews a pull request that touched kit copy-list paths
Then the section documents the reminder as advisory and never blocking the merge
```

#### Scenario: A maintainer finds the gate documented

```gherkin
Given the release-process section of docs/maintainer.md
When a maintainer prepares to archive a change that touched kit copy-list paths
Then the section documents the gate's place in the archive phase
And its pasteable fixes for the forgotten-bump and misfire causes
```

#### Scenario: The divergence manifest records both artifacts as repo-local

```gherkin
Given the divergence manifest in docs/maintainer.md
When a reader looks for the reminder workflow and the gate script
Then the manifest records both as repo-local automation that never ships in the workflow scaffolding
```
