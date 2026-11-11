> Verification approach for this change (#20, per the archived precedents): no
> runtime application exists for an acceptance runner to boot, and the
> acceptance `stack:` key deliberately stays unset until a runnable target
> exists — so acceptance-suite scaffolding stays deferred. Verification is the
> validation gate (`valid: true`, non-strict per ADR-0003), the scripted checks
> in the task groups (YAML parse, strict docs build, dune-metadex dogfood),
> and the deliverable sweep in group 6.

## 1. Issue form and blank-issue policy (code zone)

- [x] 1.1 Create `.github/ISSUE_TEMPLATE/change.yml` per design D1 — GitHub YAML issue form with six required textareas in issue-body order (Context, Suggested change name, Actor, Deliverables, Rules, Out of scope; `validations: required: true` on each) plus one optional free-form textarea for the labeled optional sections (Gate, Trigger, Decisions inside the change, Provenance, References); no issue labels set; field microcopy written against the guidelines section from task 2.1 so the two never diverge; copy stays **org-neutral** (ADR-0002)
- [x] 1.2 Create `.github/ISSUE_TEMPLATE/config.yml` per design D2 — `blank_issues_enabled: false` and nothing else (no contact links, no extra templates)
- [x] 1.3 Verify both files parse as YAML with a local parser; the authoritative render check is GitHub's issue-form preview on the pull request
- [x] 1.4 Commit as `feat(issues): add the intent-material change form and disable blank issues (#23)` — code zone: nothing under `openspec/` uncommitted alongside

## 2. Writing Issues guidance (code zone)

- [x] 2.1 Add the "Writing Issues" section to `docs/intent-prompt-guidelines.md` per design D5 — directly after the existing Template section; define the six required sections and the five optional labeled sections with one-line use-when guidance each; note that the GitHub form pre-fills the sections with blank issues disabled and that repositories on other hosts replicate the convention natively; the document stays at its current path (docs-site spec pin)
- [x] 2.2 Rebuild the documentation site through the **maintainer toolchain** and confirm the strict build passes — zero invalid links or anchors (ADR-0007)
- [ ] 2.3 Commit as `docs(guidelines): define the intent-material template in Writing Issues (#23)`

## 3. Contributor, agent, and decision pointers (code zone)

- [ ] 3.1 Extend CONTRIBUTING.md's "Every Change Starts as an Issue" section per design D6 — point to the issue form and the Writing Issues guidance
- [ ] 3.2 Extend CONTRIBUTING.md's "Where Decisions Live" section per design D7 — reference ADR-0008's kit-layering routing rule for contributors deciding where a new convention belongs
- [ ] 3.3 Commit as `docs(contributing): point the issue policy and decisions sections at the template and routing rule (#23)`
- [ ] 3.4 Extend AGENTS.md's `docs/intent-prompt-guidelines.md` pointer per design D6 — agent-authored issues follow the **intent material** template through the existing guidelines-doc pointer; no new authoring skill
- [ ] 3.5 Commit as `docs(agents): extend the guidelines pointer to issue authoring (#23)`

## 4. Distribution: dune-metadex dogfood and the bootstrap copy-list

- [ ] 4.1 Open an issue (and PR) on dune-metadex installing `.github/ISSUE_TEMPLATE/` from the hep-metadex checkout — the dogfood precondition for the quick-start claim (design D4; the validate.yml precedent, dune-metadex#4); cross-repo coordination, not a commit in this repository
- [ ] 4.2 Widen the README quick start's host-conditional step per design D3 — spec-validation CI and the issue form (`.github/ISSUE_TEMPLATE/`, both files, one item) as the host-conditional kit files, with copy commands for each; GitHub-hosted adopters copy verbatim, other hosts get the named convention
- [ ] 4.3 Extend `docs/setup.md` per design D3 — the agent-assisted bootstrap prompt's host-conditional step covers both files; the two-channels prose and mermaid diagram gain the issue form beside validate.yml as a GitHub-hosts-only kit node
- [ ] 4.4 Confirm the dune-metadex form has landed (4.1 merged) before the quick-start claim merges — the MODIFIED quick-start requirement's MUST
- [ ] 4.5 Commit as `docs(readme): add the issue form to the host-conditional bootstrap steps (#23)`

## 5. Maintainer-guide records (code zone)

- [ ] 5.1 Add the divergence-manifest row for `.github/ISSUE_TEMPLATE/` per design D8 — kit the template never ships, distributed host-conditionally so GitHub-hosted adopters copy it at bootstrap, citing issue #23 and ADR-0008; framed like the validate.yml row
- [ ] 5.2 Add the routing-rule reference to `docs/maintainer.md`'s Repository Configuration section per design D7 — the section already maps skills, commands, and config to their roles; the ADR-0008 reference completes the map
- [ ] 5.3 Commit as `docs(maintainer): record the issue-form divergence and routing-rule reference (#23)`

## 6. Verification and completion

- [ ] 6.1 Run `openspec validate standardize-issue-authoring --type change` and confirm `valid: true` (non-strict per ADR-0003; fenced scenarios satisfy the gate, the validator's step-detection warnings are expected noise)
- [ ] 6.2 Re-run the strict docs build after every docs edit lands (groups 2-5) and confirm zero invalid links or anchors
- [ ] 6.3 Sweep the deliverables against issue #23's rules: the form carries the six **intent material** sections plus the optional catch-all; blank issues are disabled; the Writing Issues section defines the template and the optional labeled sections at the unchanged path; the CONTRIBUTING.md and AGENTS.md pointers exist with no new authoring skill; the README quick start and `docs/setup.md` carry the issue form as a host-conditional copy-list item with other hosts named-not-implemented; the divergence-manifest row is present; ADR-0008 records the routing rule and the schema-fork triggers and is referenced from the maintainer guide and CONTRIBUTING.md; the `intent material` glossary entry (landed with the planning) is in place; the intent-driven schema is not forked; `.github/workflows/validate.yml` is untouched; the `/metadex-bootstrap` command (#9), the toolchain (#21), and the site (#22) are untouched
- [ ] 6.4 Confirm zone discipline held: every commit in groups 1-5 is single-zone (all code zone) and carries the `(#23)` suffix
- [ ] 6.5 Push the apply branch `23-apply-standardize-issue-authoring` (cut from `main` after the planning merge) and open the implementation PR referencing issue #23 — `Closes #23` appears only in the archive-phase commit
