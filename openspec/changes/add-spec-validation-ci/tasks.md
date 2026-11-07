> Verification approach for this change (design, Open Questions, resolved): no runtime
> application exists for an acceptance runner to boot, so acceptance-suite scaffolding
> stays deferred until the first runtime change; scenario verification is the validation
> gate (`valid: true`, non-strict per ADR-0003), the scripted checks in groups 1 and 3,
> and the CI gate dogfooded on dune-metadex in group 1.

## 1. dune-metadex spec-validation CI (executed in the dune-metadex repository)

- [x] 1.1 File the issue in dune-metadex for adding the spec-validation workflow (record its number here when filed: #3), and cut the work branch per that repository's conventions
- [x] 1.2 Copy `.github/workflows/validate.yml` verbatim from the registered hep-metadex store checkout into dune-metadex — identical gate: `openspec validate --all` over all specs and changes, `valid: true` non-strict per ADR-0003, OpenSpec CLI pinned to 1.16.0 (design D2: no forked workflow, no adopter-specific edits)
- [x] 1.3 Verify the gate locally in dune-metadex: run the workflow's exact validate command and confirm exit 0 on the current tree, then confirm it exits non-zero against a deliberately broken scratch spec and discard the scratch file
- [x] 1.4 Commit per dune-metadex's conventions, push the branch, and open the PR referencing its issue
- [x] 1.5 Get the dune-metadex PR merged — the hep-metadex work in groups 2–3 may merge only after this lands (design D4)

## 2. Kit definition and bootstrap documentation (hep-metadex)

- [x] 2.1 Extend the **workflow scaffolding** definition in `glossary/technical.md` to include the CI workflow as a GitHub-host component (design D6, ADR-0005)
- [x] 2.2 Add the host-conditional CI step to `docs/setup.md`'s agent-assisted bootstrap prompt, immediately after the scaffolding-install step (design D3): GitHub-hosted repositories copy `.github/workflows/validate.yml` from the registered store checkout; repositories on other hosts wire the named equivalent `valid: true` gate into their own CI — and explain the host condition in the prose where the prompt lives
- [ ] 2.3 Reframe the `.github/workflows/validate.yml` entry in `docs/maintainer.md`'s divergence manifest from a local-only divergence ("the template ships no CI") to a component of **workflow scaffolding** that GitHub-hosted adopters copy at bootstrap — still recorded as an intentional divergence, referencing ADR-0005
- [ ] 2.4 Add the quick start's host-conditional CI step to `README.md`, immediately after the scaffolding-install step — the claim is verified by group 1 (the worked example has the workflow before the documentation claims the step)

## 3. Verification and completion (hep-metadex)

- [ ] 3.1 Run `openspec validate add-spec-validation-ci --type change` and confirm `valid: true` (non-strict; ADR-0003 supersedes the schema's `--strict` guidance)
- [ ] 3.2 Sweep the delta scenarios and deliverables: the bootstrap prompt presents CI host-conditionally (GitHub copies the provided workflow with the CLI pinned to 1.16.0; other hosts get the named gate, no implementation); the divergence-manifest entry presents the workflow as scaffolding that GitHub-hosted adopters copy at bootstrap and that a template sync preserves; the README quick start claims the CI step and dune-metadex — the worked example it cites — has the workflow gating CI on `valid: true`; the glossary definition carries the extended sense and the documentation uses the term consistently
- [ ] 3.3 Commit the hep-metadex work per conventional commits with the `(#12)` subject suffix and BDD zone rules, push the apply branch `12-apply-add-spec-validation-ci`, and open the implementation PR referencing issue #12 — merged only after the dune-metadex PR has merged (design D4; if that PR is rejected or abandoned, revert the documentation claims per design D5 before any merge)
