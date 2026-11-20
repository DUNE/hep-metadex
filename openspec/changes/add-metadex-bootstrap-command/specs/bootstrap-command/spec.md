# Bootstrap Command

The `/hep-metadex-bootstrap` command automates the documented agent-assisted bootstrap prompt in `docs/setup.md` — the prompt is its specification and remains the fallback. It takes an uninitialized greenfield or brownfield repository to a connected one: kit installed from a versioned release, store reference declared, doctor green.

## ADDED Requirements

### Requirement: Kit-shipped command
The `/hep-metadex-bootstrap` command SHALL ship in the **workflow scaffolding** as an OpenCode command file at `.opencode/commands/hep-metadex-bootstrap.md` — zero-runtime agent instructions, not a script — carried in the kit bundle so it flows to **experiment repositories** by template install. The `hep-metadex` prefix keeps the kit's commands out of the bare `metadex-*` namespace adopters may claim for their own commands, and disambiguates them from the CLI-delivered `/opsx-*` lifecycle commands.

#### Scenario: The command ships in the kit bundle

```gherkin
Given a kit release bundle assembled after this change
When a reader lists the bundle's contents
Then it contains .opencode/commands/hep-metadex-bootstrap.md alongside the CLI-delivered command files
```

#### Scenario: A template install carries the command

```gherkin
Given an experiment repository receiving the kit by template install
When the install completes
Then the repository's agent harness offers the /hep-metadex-bootstrap command
```

### Requirement: Bootstrap one-liner
A documented one-liner SHALL fetch the command file from the latest kit release's standalone asset and hand it to the agent, so an uninitialized **experiment repository** — which has no scaffolding and therefore no installed command — can run the bootstrap. The one-liner's target SHALL be the release's command asset, not a floating main-branch URL, so what the agent executes is the released artifact.

#### Scenario: A fresh repository bootstraps from the fetched command

```gherkin
Given an uninitialized repository with no workflow scaffolding installed
When an adopter runs the documented one-liner and hands the fetched file to the agent
Then the agent executes the fetched command file and performs the bootstrap
```

#### Scenario: The one-liner fetches the released artifact

```gherkin
Given the latest kit release carrying the command file as a standalone asset
When the one-liner fetches the command file
Then it comes from the release's assets rather than a floating main-branch URL
```

### Requirement: Specification fidelity
The command SHALL automate the documented agent-assisted bootstrap prompt in `docs/setup.md` — the prompt is its specification. The documented prompt SHALL remain in place as the fallback, and drift between the command and the prompt is a defect.

#### Scenario: The command automates the documented prompt

```gherkin
Given the documented agent-assisted bootstrap prompt in docs/setup.md
When a reader compares the command's steps against the prompt
Then every prompt step is automated by the command
And the prompt remains documented as the fallback
```

#### Scenario: The prompt works without the command

```gherkin
Given an adopter who prefers the manual path
When the adopter pastes the documented prompt to an agent
Then the bootstrap completes exactly as before the command existed
```

### Requirement: Prerequisites check
Before writing anything, the command SHALL verify the machine prerequisites: the OpenSpec CLI version against the release's declared pin, and the hep-metadex **OpenSpec Store** registration. When a prerequisite is missing, the command MUST stop with a clear report naming it.

#### Scenario: Satisfied prerequisites proceed

```gherkin
Given a machine with the OpenSpec CLI at the release's declared pin
And the hep-metadex store registered on the machine
When the bootstrap runs
Then the prerequisites check passes and the bootstrap proceeds
```

#### Scenario: A CLI version below the declared pin stops the run

```gherkin
Given a machine whose OpenSpec CLI is older than the release's declared pin
When the bootstrap runs
Then it stops with a report naming the required CLI version
```

#### Scenario: An unregistered store stops the run

```gherkin
Given a machine where openspec store list does not show hep-metadex
When the bootstrap runs
Then it stops with a report naming the store registration prerequisite
```

### Requirement: Repository initialization
The command SHALL run `openspec init` for the agent tools the target repository uses before installing the kit.

#### Scenario: Init precedes the kit install

```gherkin
Given an uninitialized repository and satisfied prerequisites
When the bootstrap runs
Then openspec init has generated the repository's agent entry points before the kit install begins
```

### Requirement: Versioned kit install
The command SHALL install the kit from a versioned kit release — the latest release by default, an explicitly pinned release when the adopter names one. The fetched bundle MUST verify against the release's SHA256SUMS before extraction, and a failed verification MUST stop the install.

#### Scenario: The default install uses the latest release

```gherkin
Given satisfied prerequisites and no version named by the adopter
When the bootstrap installs the kit
Then it fetches the latest kit release's bundle and SHA256SUMS
And verifies the checksums before extracting
```

#### Scenario: An explicit pin installs the named release

```gherkin
Given an adopter naming an explicit kit version
When the bootstrap installs the kit
Then it fetches that version's release bundle and SHA256SUMS
And verifies the checksums before extracting
```

#### Scenario: A checksum failure stops the install

```gherkin
Given a fetched bundle whose checksum does not match the release's SHA256SUMS
When the bootstrap verifies it
Then it refuses to extract and reports the mismatch
```

### Requirement: Kit file placement
Kit files SHALL land at their natural repository paths. `AGENTS.md` is merge-guidance: an existing `AGENTS.md` MUST be merged with the kit's pointers, never overwritten. The **Kit version file** and KIT-MANIFEST arrive via the bundle — the version file landing as the **experiment repository**'s provenance stamp — and the command MUST NOT author the version file separately.

#### Scenario: An existing AGENTS.md is merged, not overwritten

```gherkin
Given a repository that already has an AGENTS.md
When the kit install places the kit's files
Then the kit's AGENTS.md pointers are merged into the existing file
And the existing file's own content is preserved
```

#### Scenario: The provenance stamp arrives with the install

```gherkin
Given a completed kit install
When the adopter reads the installed version file
Then it names the release the kit came from and the OpenSpec CLI version it requires
And the command authored no version file of its own
```

### Requirement: Host-conditional GitHub files
The command SHALL handle the host-conditional GitHub files as the documented prompt does. GitHub-hosted repositories keep the extracted spec-validation workflow and issue form; repositories on other hosts have the extracted `.github/` kit files removed and the equivalent validation gate and **Intent material** issue convention named for their own tooling — the kit ships GitHub implementations only.

#### Scenario: A GitHub-hosted repository keeps both files

```gherkin
Given a GitHub-hosted repository being bootstrapped
When the command handles the host-conditional files
Then .github/workflows/validate.yml and .github/ISSUE_TEMPLATE/ remain from the extraction
```

#### Scenario: A repository on another host gets the named equivalents

```gherkin
Given a repository hosted on a platform other than GitHub
When the command handles the host-conditional files
Then the extracted .github/ kit files are removed
And the equivalent valid: true gate and issue convention are named for the host's own tooling
```

### Requirement: Config authoring
The command SHALL write `openspec/config.yaml` with the intent-driven schema, a `references:` block naming the hep-metadex store id and remote, a `context:` block describing the repository's real domain and tech stack, and stage rules mirroring hep-metadex. The command MUST NOT add a `store:` line, and in a brownfield repository it MUST NOT overwrite an existing config beyond the references block.

#### Scenario: A greenfield config is authored without a store line

```gherkin
Given a repository with no existing openspec config
When the command authors the configuration
Then openspec/config.yaml declares the intent-driven schema
And a references block naming the hep-metadex store id and remote
And a context block describing the repository's real domain and tech stack
And no store: line anywhere in the file
```

#### Scenario: A brownfield config is preserved beyond the references block

```gherkin
Given a brownfield repository whose openspec config already declares its schema, context, and stage rules
When the command authors the configuration
Then only the references block is added
And the existing schema, context, and stage rules are preserved
```

### Requirement: Doctor to green
The command SHALL iterate `openspec doctor` until it reports the hep-metadex reference as ok, and the final doctor output SHALL appear in the bootstrap's report.

#### Scenario: The bootstrap ends with doctor green

```gherkin
Given a repository with the kit installed and the config authored
When the command runs openspec doctor
Then it iterates until the hep-metadex reference reports ok
And the final doctor output is included in the bootstrap report
```

### Requirement: Greenfield and brownfield support
The command SHALL complete the bootstrap for a greenfield repository and for a brownfield repository alike. In a brownfield repository the bootstrap is additive: existing code and CI stay untouched, the repository's real tech stack is recorded in `context:`, and the report notes that the repository's first change should be characterization-first.

#### Scenario: A greenfield bootstrap completes

```gherkin
Given a fresh repository with no code
When the bootstrap completes
Then the repository is connected: scaffolding installed, store reference declared, doctor green
```

#### Scenario: A brownfield bootstrap is additive

```gherkin
Given a repository that already has code and CI
When the bootstrap completes
Then the existing code and CI are untouched
And the repository's real tech stack is recorded in the config's context block
And the report notes that the first change should be characterization-first
```

### Requirement: Guardrails and final report
The command MUST NOT create a change and MUST NOT write implementation code in the target repository. The bootstrap SHALL end with a report of what was installed and the final `openspec doctor` output.

#### Scenario: The bootstrap creates no change and writes no implementation

```gherkin
Given a completed bootstrap
When the adopter inspects the repository
Then openspec/changes/ contains no change created by the bootstrap
And no implementation code was written
```

#### Scenario: The bootstrap ends with a report

```gherkin
Given a completed bootstrap
When the command finishes
Then it reports what was installed and the final doctor output
```
