> Verification approach for this change (design, Open Questions, resolved):
> no runtime application exists for an acceptance runner to boot, and the
> acceptance `stack:` key deliberately stays unset until a runnable target
> exists (#20) — so acceptance-suite scaffolding stays deferred. The
> scenarios verify as content-rubric checks: the validation gate
> (`valid: true`, non-strict per ADR-0003) plus the scripted sweeps in
> group 4. No `src/` work and no acceptance tests exist in this change, so
> the senior-dev and senior-qa subagent routing does not trigger. Every
> edit is a code-zone file (outside `openspec/`); `tasks.md` is
> zone-neutral and may accompany either zone.

## 1. Amend the two skill gates (code zone)

- [x] 1.1 Replace the "Before propose" row in `.agents/skills/openspec-git-discipline/SKILL.md` with design D1's exact wording — *Cut the change's issue branch `<issue-number>-<change-slug>` from `main` before its first commit (ask-first; on decline, warn and ask whether to continue intentionally)* — replacing "Prefer `main`" (spec: Issue branch cut before a change's first commit, both scenarios)
- [x] 1.2 Replace the "After propose" row with design D2's exact wording — *Ask the user to commit proposal artifacts on the issue branch; offer to open the planning PR from the branch that already exists* — replacing the offer to create a PR branch (spec: After propose opens the PR from the existing branch)
- [x] 1.3 Confirm the rest of `SKILL.md` is untouched — Core Rule, "During continue", "Before apply", "Before archive", "After archive", Required Checks, and Red Flags all byte-identical to the pre-change version (spec: Phase sequence and merge discipline preserved; No-auto-git rule intact)
- [x] 1.4 Commit as `docs(skill): require the issue branch before a change's first commit (#24)`

## 2. Maintainer guidance: record the fork (code zone)

- [x] 2.1 Add the divergence-manifest row in `docs/maintainer.md` per design D4 — Area `.agents/skills/openspec-git-discipline/`; divergence: the two amended gates requiring the `<issue-number>-<change-slug>` issue branch cut from `main` before a change's first commit; reason: standing policy that change work reaches `main` only by pull-request merge; carry the glossary row's "fork of a vendored skill" marker (spec: Fork recorded and recoverable in maintainer guidance, scenario 1)
- [x] 2.2 Add the drift-impact bullet per design D5, parallel to the glossary fork's — a template sync that overwrites the skill silently reverts the two amended gates; recover by hand-merging upstream changes into `.agents/skills/openspec-git-discipline/` and re-applying the two gates (spec scenario 2)
- [x] 2.3 Commit as `docs(maintainer): record the git-discipline skill fork and its drift impact (#24)`

## 3. Contributor and agent surfaces (code zone)

- [x] 3.1 Extend the pull-request bullet in `CONTRIBUTING.md` per design D6 — "Branch from `main`" gains `<issue-number>-<change-slug>` cut before the change's first commit, with the parenthetical that implementation branches follow the documented `<issue>-apply-<change>` pattern (spec: Contributor and agent surfaces carry the naming rule, scenario 1)
- [ ] 3.2 Add the fourth bullet to `AGENTS.md` per design D7 — the one-line issue-branch convention, ending with the pointer to the openspec-git-discipline skill (spec scenario 2)
- [ ] 3.3 Add the **issue branch** term to `glossary/technical.md` per design D8 — definition scoped to planning and implementation commits, with use-when and avoid columns per the glossary discipline (avoid: the apply-phase `<issue>-apply-<change>` branch and the archive phase's direct metadata commit)
- [ ] 3.4 Commit as `docs(contributing): add the issue-branch naming rule to the PR section (#24)`
- [ ] 3.5 Commit as `docs(agents): point agent sessions at the issue-branch convention (#24)`
- [ ] 3.6 Commit as `docs(glossary): define the issue-branch term (#24)`

## 4. Verification and completion

- [ ] 4.1 Run `openspec validate require-issue-branch-for-changes --type change` and confirm `valid: true` (non-strict per ADR-0003 — fenced Gherkin is the single scenario source, so CLI 1.16.0's step-detection warnings are expected noise, not failures)
- [ ] 4.2 Scripted sweep of the delta scenarios against the delivered files: both gate rows match D1/D2 verbatim; the manifest row and drift bullet are present in `docs/maintainer.md`; the CONTRIBUTING bullet carries the naming rule and the apply-pattern pointer; `AGENTS.md` carries the convention; the glossary term's definition is scoped to planning and implementation commits
- [ ] 4.3 Check issue #24's five rules one by one against the delivered state: branch cut before the first commit; change work reaches `main` only by pull-request merge with the archive bookkeeping exception; phase sequence and merge discipline unchanged; the no-auto-git rule intact; maintainer guidance explains the hand-merge and re-apply recovery
- [ ] 4.4 Commit any remaining work per conventional commits with the `(#24)` suffix, push the apply branch `24-apply-require-issue-branch-for-changes` (cut from `main` after the planning merge), and open the implementation PR referencing issue #24
