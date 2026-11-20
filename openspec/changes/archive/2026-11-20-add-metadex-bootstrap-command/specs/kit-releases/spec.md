# Kit Releases

## MODIFIED Requirements

### Requirement: KIT-MANIFEST ownership classes
The kit bundle SHALL carry a machine-readable KIT-MANIFEST mapping every copy-list path to exactly one ownership class: CLI-owned (`.opencode/skills/` and the CLI-delivered command files under `.opencode/commands/` — refreshed via the OpenSpec CLI, never kit-copied over), kit-owned (`.opencode/agent/`, `.agents/skills/`, the schema copy, `docs/intent-prompt-guidelines.md`, host-conditional `.github/` files, and the kit's own `hep-metadex-*` command files under `.opencode/commands/`), merge-guidance (`AGENTS.md`), and never-touch (`openspec/config.yaml`). Entries MAY nest — a per-file entry inside a directory entry — and when several entries match a path, the most specific matching path SHALL win.

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

#### Scenario: A kit-owned command wins inside a cli-owned directory

```gherkin
Given the manifest's per-file kit-owned entry for .opencode/commands/hep-metadex-bootstrap.md
And the manifest's cli-owned directory entry for .opencode/commands/
When a reader or tool resolves the command file's ownership class
Then the per-file kit-owned entry wins as the most specific matching path
And the CLI-delivered opsx-* files in the same directory stay cli-owned
```

### Requirement: Bump-triggered release publication
When a kit version bump merges to `main`, a repo-local workflow SHALL tag `vX.Y.Z`, assemble the kit bundle — exactly the documented copy-list plus the version file and the KIT-MANIFEST — publish SHA256SUMS, and publish the GitHub release with the required OpenSpec CLI version declared. The workflow SHALL additionally publish the kit's bootstrap command file (`.opencode/commands/hep-metadex-bootstrap.md`) as a standalone release asset derived from the same source file the bundle carries, covered by the release's SHA256SUMS. The workflow MUST NOT create commits on `main` (it creates tags and releases only) and MUST NOT use release-please-style PR generation.

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

#### Scenario: The release publishes the bootstrap command as a checksummed asset

```gherkin
Given a kit release cut after the bootstrap command joined the copy-list
When an adopter lists the release's assets
Then the command file is published alongside the bundle
And SHA256SUMS covers the command file
And its content matches the file the bundle carries
```

### Requirement: Release consumption documentation
`docs/usage.md` SHALL document adopter-facing release consumption: fetching the kit bundle for a chosen version, verifying it against SHA256SUMS, reading the provenance stamp, and minding the KIT-MANIFEST ownership classes — including that the kit's own `hep-metadex-*` command files under `.opencode/commands/` are kit-owned while the CLI-delivered files in the same directory stay cli-owned — the documented manual path for installing and syncing kits until command and installer automation takes over.

#### Scenario: A reader finds the checksum verification step

```gherkin
Given the release consumption section of docs/usage.md
When an adopter prepares to install a kit release
Then the documentation shows fetching the bundle for a chosen version
And verifying it against the release's SHA256SUMS
```

#### Scenario: A reader finds the per-file ownership exception

```gherkin
Given the release consumption section of docs/usage.md
When an adopter reads the ownership-class guidance
Then it names the kit's own command file as kit-owned inside the cli-owned commands directory
```
