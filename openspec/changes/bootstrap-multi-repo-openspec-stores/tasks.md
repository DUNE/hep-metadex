> Verification approach for this change (design, Open Questions, resolved): no runtime
> application exists for an acceptance runner to boot, so acceptance-suite scaffolding is
> deferred until the first runtime change; scenario verification here is the validation
> gate (`valid: true`), scripted checks, and CI. The spec-index injection scenario
> (`experiment-references`) verifies with the first common capability change, when the
> OpenSpec Store publishes a spec to inject.

## 1. HSF checklist foundations (hep-metadex)

- [ ] 1.1 Add the full Apache-2.0 `LICENSE` at the repository root
- [ ] 1.2 Record the license divergence in the README divergence manifest: move `LICENSE.md` from the "Not installed" row to a deliberate-divergence entry referencing ADR-0004
- [ ] 1.3 Add a GitHub Actions workflow running `openspec validate` over all specs and changes, gating on `valid: true` (non-strict, per ADR-0003), with the OpenSpec CLI version pinned
- [ ] 1.4 Verify the CI gate locally: run the workflow's exact validate command, confirm exit 0 on the current tree, and confirm it exits non-zero against a deliberately broken scratch spec before discarding the scratch file

## 2. OpenSpec Store conversion (hep-metadex)

- [ ] 2.1 Resolve the conversion-mechanics open question: read-only inspection of `openspec store setup --help` (and docs) for in-place conversion of an existing repo-local root; fall back to hand-creating `.openspec-store/store.yaml` per the documented layout
- [ ] 2.2 Create `.openspec-store/store.yaml` declaring the org-neutral id `hep-metadex`
- [ ] 2.3 Register the development checkout as the OpenSpec Store (`openspec store register`), so the maintainer's checkout doubles as the store
- [ ] 2.4 Verify store-identity scenarios: `openspec doctor` reports the store with valid metadata, and `git status` shows no modification to any pre-existing path under `openspec/`

## 3. dune-metadex bootstrap (executed in the dune-metadex repository)

- [ ] 3.1 Clone dune-metadex and create a bootstrap branch
- [ ] 3.2 Install the workflow scaffolding from hep-metadex: `.agents/skills/`, `.opencode/` (commands and agent definitions), the `openspec/schemas/intent-driven/` copy, `AGENTS.md`, and `docs/intent-prompt-guidelines.md` (referenced by AGENTS.md)
- [ ] 3.3 Create `openspec/config.yaml`: `schema: intent-driven`, a `references:` block with the hep-metadex store id and clone URL (`https://github.com/DUNE/hep-metadex.git`), DUNE-specific context (domain: DUNE long-baseline neutrino experiment metadata management), and stage rules mirroring hep-metadex — no `store:` line
- [ ] 3.4 Seed `glossary/domain.md` and `glossary/technical.md` from hep-metadex, with DUNE domain entries added as they arise
- [ ] 3.5 Create experiment-local `openspec/specs/` and `openspec/changes/` directories
- [ ] 3.6 Verify the connection: `openspec doctor` in dune-metadex reports the hep-metadex reference as ok
- [ ] 3.7 Verify fresh-machine guidance: unregister the store, run `openspec doctor` in dune-metadex (expect the missing-store finding with a pasteable clone-and-register fix citing the declared remote), then re-register
- [ ] 3.8 Verify the config contract: the `references:` entry selects the store by id and the config contains no `store:` line
- [ ] 3.9 Verify experiment-local routing: create a probe change without `--store`, confirm it lands under dune-metadex/openspec/changes with the store working tree unchanged, then remove the probe
- [ ] 3.10 Verify write-back routing: create a probe change with `--store hep-metadex` from the dune-metadex directory, confirm it lands in the store's openspec/changes with the dune-metadex tree unchanged, then remove the probe
- [ ] 3.11 Commit the bootstrap (conventional commits, BDD zone rules), push the branch, and open a PR in dune-metadex

## 4. Adopter documentation (hep-metadex)

- [ ] 4.1 Rewrite the README as the adopter front door: what/why and the quick start (scaffolding install, store registration, `references:` declaration, doctor green); include a repository-map section linking stable paths only — directories and stable filenames (`docs/`, `CONTRIBUTING.md`, `adr/`, `glossary/`, `openspec/specs/`, `openspec/changes/` with its `archive/`) — never per-artifact deep links that churn as artifacts accumulate; move template provenance, the divergence manifest, and update-from-upstream guidance into a maintainer document under `docs/` that the README links
- [ ] 4.2 Write `docs/setup.md`: OpenSpec Store layout, experiment repository configuration, the two-channel architecture (specs via store, workflow scaffolding via template install), linking `glossary/` terms on first use, an adopting-into-an-existing-repository section — the plumbing is identical and additive (scaffolding install, config with the **Store reference**, doctor green, existing code and CI untouched), but the first change is characterization-first: spec the capability seams the refactor will touch as they behave today (agents draft from code, humans review), record the real tech stack and `stack:` in config, scaffold the acceptance suite against the bootable existing application to lock current behavior, then run refactor changes through the standard lifecycle with the suite green — and an agent-assisted bootstrap section: a machine-prerequisites checklist (pinned OpenSpec CLI, agent harness, OpenSpec Store clone and register), a copy-paste bootstrap prompt valid for greenfield and brownfield repositories alike (the agent verifies prerequisites, runs `openspec init`, installs the workflow scaffolding from hep-metadex, writes `openspec/config.yaml` with schema, references, and the repo's real context, and iterates `openspec doctor` until green), and a note that `/opsx-new` and `/opsx-propose` stop in uninitialized repositories by design, making this prompt the on-ramp; the fresh-repository quick start remains the verified dogfood path, and the existing-repository and agent-assisted sections are its documented variants
- [ ] 4.3 Write `docs/usage.md`: change-time work and write-back flows, store pull discipline, CLI version pinning and upgrade guidance, the validator-warning known-issue note (ADR-0003), and the full change lifecycle — one issue per change; propose branch `<issue>-<change>` → planning PR → merge to main; apply branch `<issue>-apply-<change>` cut from main after the planning merge → implementation PR → merge to main; verify → spec sync → archive run from main as a direct metadata commit, closing the issue — rendered as a Mermaid diagram (plain `flowchart` syntax, lightweight C4-inspired, consistent with this change's design.md) that shows both merge gates (proposal on main before apply; implementation on main before archive), using a generic example change with stage-appropriate branch names rather than this change's names; once the first change archives, deep-link it as a worked example of what a change looks like here
- [ ] 4.4 Write `docs/governance.md`: decision rights, review bar, and the org-neutral hosting roadmap per ADR-0002 (DUNE incubation, HSF endorsement trigger, HSF-org hosting as a separate follow-on), linking ADR-0002
- [ ] 4.5 Write `docs/hsf-affiliation.md`: the full required-guideline checklist mapping (public repository, suitable name, license, installation, documentation, test suite, contributor openness, issue tracking, general information) with license → `LICENSE` and test suite → spec-validation CI, linking ADR-0004 and ADR-0001 (the applicability-beyond-one-experiment evidence)
- [ ] 4.6 Write `CONTRIBUTING.md`: org-agnostic contribution policy — pull requests, issue tracker, conventional commits with every commit referencing its change's issue number as a `(#N)` subject suffix (`Closes #N` reserved for the archive-phase commit, since one issue tracks the whole lifecycle), glossary discipline
- [ ] 4.7 Dogfood-verify the quick start: confirm the README's steps match the bootstrap actually performed on dune-metadex in group 3, and that `docs/usage.md` describes the write-back command verified in task 3.10

## 5. Completion and verification (hep-metadex)

- [ ] 5.1 Run `openspec validate bootstrap-multi-repo-openspec-stores --type change` and confirm `valid: true` (the schema's `--strict` guidance is superseded by ADR-0003)
- [ ] 5.2 Sweep the governance-docs scenarios: Apache-2.0 `LICENSE` present and recorded as a divergence; every required HSF guideline mapped in `docs/hsf-affiliation.md`; governance and contribution text names no organization-specific process
- [ ] 5.3 Commit remaining work per BDD zone rules and conventional commits; push the branch and open the hep-metadex PR referencing issue #7
