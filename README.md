# hep-metadex

## Development Workflow

This project uses [OpenSpec](https://github.com/Fission-AI/OpenSpec) with the
[intent-driven](openspec/schemas/intent-driven/schema.yaml) schema and
[OpenCode](https://opencode.ai/) for spec-driven development.

### Intent-Driven Workflow

Changes move through these artifacts in order:

```text
proposal -> specs -> design -> adr -> tasks
```

- `proposal` captures why the change matters.
- `specs` describe observable behaviour with Gherkin-style scenarios.
- `design` explains the implementation approach and trade-offs.
- `adr` records durable architectural decisions.
- `tasks` turn the accepted intent, behaviour, design, and decisions into work.

### Per-Stage Skills

`openspec/config.yaml` is the source of truth for stage rules. As configured,
each stage enforces:

| Stage | Skills | Effect |
|-------|--------|--------|
| `proposal` | `grill-me`, `adversarial-authoring`, `glossary` | Interrogate the plan until shared understanding; draft via author/reviewer subagents to reduce model bias; keep terminology consistent |
| `specs` | `spec-as-source` | Specs contain fenced Gherkin scenarios (authored with `gherkin-authoring`) that serve as the source for acceptance tests |
| `design` | `c4-diagrams`, `glossary` | C4 architecture diagrams (ASCII or Mermaid) plus terminology consistency |
| `adr` | `architectural-decision-records` | Durable decision records with rationale, tradeoffs, and supersession chains |
| `tasks` | `spec-as-source` | Acceptance-test-first work: configure and run the acceptance suite, then implement |
| `apply` / `archive` | `test-driven-development`, sync | Test-first implementation; run `/opsx-sync` before archiving |

Notes:

- `spec-as-source` is experimental upstream; it turns the back half of the
  lifecycle into BDD-style acceptance testing. Companion skills
  (`gherkin-authoring`, `acceptance-test-authoring`) are bundled in
  `.agents/skills/`.
- The first `tasks` implementation requires choosing an acceptance runner —
  cucumber-js (JavaScript) or behave (Python) — via the
  `acceptance-test-authoring` skill. The choice is recorded as `stack:` in
  `openspec/config.yaml`, which the skill reads before scaffolding anything.
- To lighten any stage, comment out the corresponding rule line in
  `openspec/config.yaml`.

### Commands

| Command | Purpose |
|---------|---------|
| `/opsx-new` | Start a new change |
| `/opsx-propose` | Create the proposal for a change |
| `/opsx-continue` | Create the next artifact |
| `/opsx-explore` | Explore a problem or idea before committing to a change |
| `/opsx-apply` | Implement tasks from a change |
| `/opsx-verify` | Verify an implemented change |
| `/opsx-update` | Update a change's planning artifacts |
| `/opsx-sync` | Sync delta specs into main specs |
| `/opsx-archive` | Archive a completed change |
| `/opsx-bulk-apply` | Apply multiple active changes concurrently in worktrees |
| `/opsx-bulk-archive` | Archive multiple completed changes |

### Writing Intent Prompts

Intents name the actor who receives the value — end users, platform
engineers, architects — plus verifiable rules. See
[docs/intent-prompt-guidelines.md](docs/intent-prompt-guidelines.md) for the
template, worked examples for non-end-user actors, and when Gherkin
acceptance tests fit:

```text
/opsx-new Allow <actor> to <capability>.

Actor: <who they are and what boundary they operate at>
Rules:
- <observable invariants, SHALL/MUST phrasing>
Out of scope: <what not to build>
```

### Configuration

- `openspec/config.yaml` selects the intent-driven schema and per-artifact
  rules (see [Per-Stage Skills](#per-stage-skills)). Its `context` block
  injects project background (domain, tech stack, subagent routing) into
  every artifact workflow.
- `AGENTS.md` enables OpenSpec git discipline: proposals land on `main`
  before apply, and implementation merges before archive.
- `.opencode/agent/` provides `senior-dev`, `senior-qa`, and adversarial
  author/reviewer subagents.
- `.agents/skills/` provides collaboration skills: `grill-me`, `c4-diagrams`,
  `architectural-decision-records`, `test-driven-development`,
  `gherkin-authoring`, `glossary`, `spec-as-source`, and more.
- `opencode.json.example` is an optional stub for per-project OpenCode
  configuration. OpenCode reads your global config
  (`~/.config/opencode/opencode.json`), which applies to every project, so
  this repo ships no active `opencode.json`. Copy the stub to `opencode.json`
  only if you need repo-specific settings (e.g., the optional Superpowers
  plugin). The stub contains only the `$schema` reference for editor
  validation and configures nothing.

## Template Provenance

This project's OpenSpec/OpenCode setup was installed on 2026-11-03 from
[intent-driven-template](https://github.com/intent-driven-dev/intent-driven-template)
at commit `b5bda460a2180a55fc508fdedc4ef058d95355db` (2026-10-15), following
its
[install guide](https://raw.githubusercontent.com/intent-driven-dev/intent-driven-template/refs/heads/main/INSTALL_TEMPLATE.md).
The bundled schema under `openspec/schemas/intent-driven/` is a local copy of
the [intent-driven schema](https://github.com/intent-driven-dev/openspec-schemas/tree/main/openspec/schemas/intent-driven)
from the openspec-schemas repository. The shared lifecycle commands and
skills under `.opencode/` are OpenSpec CLI 1.16.0 versions, newer than the
template's copies (generated by 1.14.0).

### Intentional Divergences

The files below intentionally differ from upstream. Treat this table as the
manifest when syncing with the template:

| Area | Divergence | Reason |
|------|------------|--------|
| `.opencode/commands/`, `.opencode/skills/` | Shared commands and skills are CLI 1.16.0 versions (template ships 1.14.0); `opsx-update` and `openspec-update-change` exist only locally | Avoided a downgrade; these files are CLI-owned, not template-owned |
| `opencode.json` | Renamed to `opencode.json.example` | Per-project OpenCode config is opt-in; global config is preferred |
| `openspec/config.yaml` | Active `context` block (tech stack, conventional commits, HEP domain, subagent routing) and all stage rules enabled | Project-specific configuration; designated customization point |
| `openspec/schemas/intent-driven/templates/spec.md` | "business rule" placeholders changed to "domain rule" | This is a high-energy physics domain, not a business domain; the local schema copy is the designated customization point |
| `.agents/skills/glossary/` | `glossary/business.md` convention renamed to `glossary/domain.md` (SKILL.md, README.md) | HEP domain terms should not be filed under a "business" label; **this is a fork of a vendored skill** |
| `.gitignore` | Minimal local file (template ships a broader one) | Only `openspec/.cache/` is needed so far |
| `AGENTS.md` | Added a pointer to `docs/intent-prompt-guidelines.md` for intent-prompt authoring | Project-specific contributor guidance; re-apply the pointer after a template sync |
| Not installed | `package.json`, `package-lock.json`, `skills-lock.json`, `LICENSE.md`, `.github/` | Outside the install guide's file list; do not add during a sync without a deliberate decision |

### Drift Impact

- **Designated customization points** (`openspec/config.yaml`, the local
  `openspec/schemas/intent-driven/` copy): upstream changes must be
  reconciled manually. A naive copy loses the project-specific values listed
  above.
- **Vendored skill fork** (`.agents/skills/glossary/`): a template sync that
  overwrites this directory silently reverts `glossary/domain.md` back to
  `glossary/business.md`. Re-apply the rename after updating, or merge
  upstream changes by hand.
- **CLI-generated files**: never copy the template's versions of the shared
  commands and skills over the local ones — the template currently ships
  older (1.14.0) versions than the installed CLI (1.16.0) produced. Update
  these via the OpenSpec CLI instead.
- **`README.md`**: project-owned documentation, not template-managed; a sync
  should not overwrite it.

### Updating From Upstream

1. **Record the baseline.** Before syncing, note the current upstream commit;
   after syncing, update the commit hash at the top of this section. Commit
   all local work first and sync on a branch.
2. **Never bulk-copy.** Clone the template outside the repository, diff it
   against the project, and copy only files that changed upstream and are not
   listed in the divergence manifest.
3. **Update CLI-owned files via the CLI.** Refresh the shared commands and
   skills under `.opencode/` with the OpenSpec CLI (`openspec --version` to
   check), not from the template.
4. **Re-apply the manifest.** After copying any template file, re-apply every
   affected divergence from the table above (config values, spec template
   wording, glossary rename).
5. **Validate before merging.** Run `openspec schema validate intent-driven`,
   review the full `git diff`, and merge only when the result matches the
   manifest.
