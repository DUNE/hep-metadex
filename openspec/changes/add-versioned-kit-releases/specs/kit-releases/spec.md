# Kit Releases

## ADDED Requirements

### Requirement: Kit version identity
The repository SHALL carry a kit version file at the repository root declaring the **workflow scaffolding**'s current version. The version file plays two roles: source-side it is the release trigger; shipped inside the kit bundle it is each **experiment repository**'s provenance stamp, so every install lands pre-stamped.

#### Scenario: A maintainer reads the current kit version

```gherkin
Given the hep-metadex repository with its kit version file at the root
When a maintainer reads the version file
Then it declares the workflow scaffolding's current version in semver form
```

#### Scenario: An installed kit lands pre-stamped

```gherkin
Given a kit release bundle assembled from the repository
When an adopter installs the kit from that release into an experiment repository
Then the installed kit includes the version file naming the release's version
```

### Requirement: Kit-only semantic versioning contract
The kit version SHALL follow semantic versioning and speak only about **workflow scaffolding** content: MAJOR for breaking changes to installed state (schema format changes, command renames or removals, coordinated OpenSpec CLI upgrades), MINOR for new kit components, PATCH for fixes and wording. Changes confined to specs, changes, non-kit docs, or repo-local tooling MUST NOT drive a kit release.

#### Scenario: A new kit component bumps the minor version

```gherkin
Given the kit at version 1.0.0
When a change adds a new command to the workflow scaffolding and bumps the version
Then the new version is 1.1.0
```

#### Scenario: A spec-only change drives no release

```gherkin
Given a change confined to the OpenSpec Store's specs
When the change merges to main
Then no kit release is cut
```

### Requirement: Version bump and changelog entry in the same change
A change that alters kit files MUST bump the kit version and add the matching `CHANGELOG.md` entry in the same change, mirroring the CLI-pin discipline (usage.md, "CLI Version Pinning and Upgrades").

#### Scenario: A kit-altering change carries both

```gherkin
Given an open change whose diff alters workflow scaffolding files
When a maintainer reviews the change
Then its diff bumps the kit version file
And its diff adds the matching CHANGELOG.md section
```

### Requirement: Changelog as the single source of release notes
The repository SHALL maintain a `CHANGELOG.md` at the repository root per the Keep a Changelog conventions — semver-compliant version headings with release dates, categorized entries, each entry referencing its change issue. The release workflow SHALL extract each GitHub release body from the changelog section for the released version and MUST fail the release when that section is missing.

#### Scenario: A release body reproduces its changelog section

```gherkin
Given the changelog carrying a section for version 1.1.0
When the release for 1.1.0 publishes
Then the GitHub release body is the changelog section for 1.1.0
```

#### Scenario: A missing changelog section fails the release

```gherkin
Given a version bump whose changelog section is missing
When the release workflow runs for that version
Then it fails without publishing a release
```

### Requirement: Bump-triggered release publication
When a kit version bump merges to `main`, a repo-local workflow SHALL tag `vX.Y.Z`, assemble the kit bundle — exactly the documented copy-list plus the version file and the KIT-MANIFEST — publish SHA256SUMS, and publish the GitHub release with the required OpenSpec CLI version declared. The workflow MUST NOT create commits on `main` (it creates tags and releases only) and MUST NOT use release-please-style PR generation.

#### Scenario: A bump merge cuts a release

```gherkin
Given main receiving a merged change that bumps the kit version to 1.1.0
When the release workflow runs on the merge
Then it tags v1.1.0
And publishes the kit bundle containing exactly the copy-list plus the version file and the KIT-MANIFEST
And publishes SHA256SUMS for the bundle
And declares the OpenSpec CLI version the kit requires
```

#### Scenario: The release workflow leaves no commits on main

```gherkin
Given a completed kit release
When a maintainer inspects main's history after the release
Then the release added a tag and a GitHub release
And added no commits to main
```

#### Scenario: The first release fires on its introducing merge

```gherkin
Given main merging the change that introduces the kit version file at 1.0.0 and the release workflow itself
When the merge lands
Then the workflow treats the version file's introduction as a version bump
And cuts the v1.0.0 release
```

### Requirement: KIT-MANIFEST ownership classes
The kit bundle SHALL carry a machine-readable KIT-MANIFEST mapping every copy-list path to exactly one ownership class: CLI-owned (`.opencode/commands/`, `.opencode/skills/` — refreshed via the OpenSpec CLI, never kit-copied over), kit-owned (`.opencode/agent/`, `.agents/skills/`, the schema copy, `docs/intent-prompt-guidelines.md`, host-conditional `.github/` files), merge-guidance (`AGENTS.md`), and never-touch (`openspec/config.yaml`).

#### Scenario: Every copy-list path carries an ownership class

```gherkin
Given the KIT-MANIFEST inside a kit release bundle
When a reader or tool inspects the manifest
Then every copy-list path maps to exactly one of the four ownership classes
```

#### Scenario: CLI-owned paths direct refresh through the CLI

```gherkin
Given the manifest's CLI-owned entries for .opencode/commands/ and .opencode/skills/
When an adopter reads those entries
Then they direct refresh through the OpenSpec CLI rather than a kit copy
```

### Requirement: Channel 1 preserved by the release channel
Kit releases MUST NOT change channel 1: **OpenSpec Store** registration, **Store reference** consumption, **spec index** injection, and the doctor fix are untouched, and the registered store checkout keeps floating on `main`.

#### Scenario: A connected experiment is unaffected by a release

```gherkin
Given an experiment repository connected by a Store reference
When a new kit release publishes
Then openspec doctor still reports the reference as ok
And the spec index still serves from the registered checkout on main
```

#### Scenario: The doctor fix is unchanged

```gherkin
Given a machine where the OpenSpec Store is not registered
When a contributor runs openspec doctor in a connected repository
Then the fix still prints the pasteable clone-and-register command
```

### Requirement: Release consumption documentation
`docs/usage.md` SHALL document adopter-facing release consumption: fetching the kit bundle for a chosen version, verifying it against SHA256SUMS, and reading the provenance stamp — the documented manual path for installing and syncing kits until command and installer automation takes over.

#### Scenario: A reader finds the checksum verification step

```gherkin
Given the release consumption section of docs/usage.md
When an adopter prepares to install a kit release
Then the documentation shows fetching the bundle for a chosen version
And verifying it against the release's SHA256SUMS
```
