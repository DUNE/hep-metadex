# hep-metadex

The general-purpose reference for building experiment metadata management
systems across high-energy physics, published as an
[OpenSpec Store](glossary/technical.md): a standalone, registered OpenSpec
repository whose [common capability](glossary/domain.md) specifications any
experiment can consume read-only — plus the
[workflow scaffolding](glossary/technical.md) (schema, skills, commands,
subagents) that experiments install by template.

Content reaches an [experiment repository](glossary/domain.md) through two
independent channels:

1. **Specs flow through the store, read-only.** A
   [Store reference](glossary/technical.md) declaration injects the store's
   spec index into the experiment's artifact workflows; experiments cite
   shared specs without copying them, and keep their own specs, changes, and
   implementation in their own repositories.
2. **Workflow scaffolding replicates by template install.** The kit is
   copied from a hep-metadex checkout at bootstrap time; it never flows
   through the store.

[dune-metadex](https://github.com/DUNE/dune-metadex) is the first adopter, proving the mechanism end to end. The
store currently launches with no common capability specs by design — the
first is the immediate follow-up change — so early adopters connect to the
workflow and grow with the store's first specs.

## Quick Start

Takes a fresh experiment repository from nothing to a connected one:
scaffolding installed, store registered, reference declared, doctor green.
The same steps were verified end to end on [dune-metadex](https://github.com/DUNE/dune-metadex); the full
explanation, an adopting-into-an-existing-repository variant, and an
agent-assisted bootstrap prompt live in [docs/setup.md](docs/setup.md).

1. **Install the OpenSpec CLI (pinned to 1.16.0):**

   ```bash
   curl -fsSL https://openspec.dev/cli/install.sh | OPENSPEC_VERSION=v1.16.0 sh
   ```

2. **Register the hep-metadex store (once per machine):**

   ```bash
   git clone https://github.com/DUNE/hep-metadex.git ~/openspec/hep-metadex
   openspec store register ~/openspec/hep-metadex --id hep-metadex
   ```

3. **Initialize OpenSpec in your experiment repository** (from its root,
   with your agent tool — `opencode` here):

   ```bash
   openspec init --tools opencode
   ```

4. **Install the workflow scaffolding.** Copy the following files and
   directories from the local store checkout you registered in step 2
   (for example `~/openspec/hep-metadex`) into the same paths in your
   repository:

   - `.agents/skills/`
   - `.opencode/` (commands and agent definitions)
   - `openspec/schemas/intent-driven/`
   - `AGENTS.md`
   - `docs/intent-prompt-guidelines.md` (referenced by `AGENTS.md`)

5. **Declare the Store reference** in your `openspec/config.yaml` — and never
   a `store:` line, which would route your planning into the central
   repository:

   ```yaml
   schema: intent-driven

   references:
     - id: hep-metadex
       remote: https://github.com/DUNE/hep-metadex.git

   context: |
     Tech stack: <your real stack>
     We use conventional commits; every commit references its change's issue number as a (#N) subject suffix; Closes #N appears only in the archive-phase commit
     Domain: <your experiment's metadata management domain>
   ```

   Stage rules mirror hep-metadex; see
   [docs/setup.md](docs/setup.md#experiment-repository-configuration) for the
   full configuration and the worked example.

6. **Verify the connection:**

   ```bash
   openspec doctor
   ```

   The `hep-metadex` reference reports `ok`. (On a machine where the store
   is not yet registered, doctor prints a pasteable clone-and-register fix
   citing the declared remote.)

From here, `/opsx-new` or `/opsx-propose` starts your first change, and the
store's spec index appears in every artifact workflow.
[docs/usage.md](docs/usage.md) covers change-time work, write-back to the
store, and the change lifecycle.

## Repository Map

Stable locations; everything else links from here.

| Path | What lives there |
|------|------------------|
| `docs/` | Adopter and maintainer documentation: [setup](docs/setup.md), [usage](docs/usage.md), [governance](docs/governance.md), [HSF affiliation](docs/hsf-affiliation.md), the [maintainer guide](docs/maintainer.md) (template provenance, divergence manifest, update-from-upstream), and [intent-prompt guidelines](docs/intent-prompt-guidelines.md) |
| `CONTRIBUTING.md` | Contribution policy — issues, pull requests, conventional commits, glossary discipline |
| `adr/` | Durable architectural decisions, newest last |
| `glossary/` | Domain and technical terms with use-when/avoid guidance |
| `openspec/specs/` | The store's published capability specifications |
| `openspec/changes/` | In-flight changes; `openspec/changes/archive/` holds completed ones |
| `LICENSE` | Apache-2.0 — a deliberate divergence from the template's MIT, recorded in the [divergence manifest](docs/maintainer.md#intentional-divergences) |

## Who This Is For

- **Adopting an experiment:** [docs/setup.md](docs/setup.md) then
  [docs/usage.md](docs/usage.md).
- **Contributing a change:** [CONTRIBUTING.md](CONTRIBUTING.md).
- **Evaluating the project** (HSF or otherwise):
  [docs/governance.md](docs/governance.md) and
  [docs/hsf-affiliation.md](docs/hsf-affiliation.md).
- **Maintaining this repository and its template relationship:**
  [docs/maintainer.md](docs/maintainer.md).
