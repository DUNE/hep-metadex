> Verification approach for this change (tasks-stage resolution, mirroring the #34/#35 precedent
> and issue #20's suite deferral): no runtime application exists for an acceptance runner to
> boot, so acceptance-suite scaffolding stays deferred until the first runtime change; scenario
> verification here is the validation gate (`valid: true` per ADR-0003), a repository-wide sweep
> of the unified pin, this change's own pull-request CI — the first real `@v7` runs of
> `validate.yml` and `release.yml`, exercising design D1's evidence in practice — the reminder
> running silent on the pull requests (the bump is present), the v1.0.1 release cutting on merge
> (design D3), and the gate's substantive archive run: if this change lands before #9, it is the
> reminder/gate pair's first substantive dogfood.

## 1. Pin unification (hep-metadex)

- [x] 1.1 Move `release.yml`'s checkout pin: `actions/checkout@v4` → `actions/checkout@v7` — the pin line only; the bump detection (`fetch-depth: 0`), the changelog/CLI-pin/tag gates, and publication stay untouched (design D1, D2)
- [x] 1.2 Move `validate.yml`'s checkout pin: `actions/checkout@v4` → `actions/checkout@v7` — the pin line only; `OPENSPEC_VERSION: v1.16.0` and the install/validate steps stay untouched (the issue's rule; design D2)
- [x] 1.3 Verify the conforming set rather than editing it: confirm `docs.yml` and `kit-reminder.yml` already pin `@v7` and are byte-unchanged in this change's diff (design D2)
- [x] 1.4 Sweep the unified-pin invariant: every `actions/checkout` use under `.github/workflows/` names the same major (`@v7`), the pin names the GitHub-created `actions/checkout`, and the diff contains no workflow logic beyond the two pin lines

## 2. Kit release discipline (hep-metadex)

- [x] 2.1 Bump the kit version file: `.metadex-kit` `version: 1.0.0` → `1.0.1` (PATCH — a fix to a kit component, per ADR-0009's semver contract; design D3); the `cli: 1.16.0` pin is untouched
- [x] 2.2 Add the matching `CHANGELOG.md` section: `## [1.0.1]` dated at preparation, `### Fixed` entry naming the unified checkout pin (`validate.yml` moves `@v4` → `@v7`, unifying all four workflows) and referencing `(#44)`, plus the `[1.0.1]` release link — Keep a Changelog style (design D3)
- [x] 2.3 Confirm the release gates will pass: the changelog section for 1.0.1 exists, `.metadex-kit`'s `cli:` matches `validate.yml`'s `OPENSPEC_VERSION` (both 1.16.0), and no `v1.0.1` tag exists yet (design D3)

## 3. Completion and acceptance (hep-metadex, then merge- and archive-time)

- [x] 3.1 Run `openspec validate unify-checkout-action-pin --type change` and confirm `valid: true` (the schema's `--strict` guidance is superseded by ADR-0003)
- [x] 3.2 Sweep the workflow-action-pinning scenarios against the implemented state: all four workflows pin the same major; the move was coordinated (no single-workflow move); the pin names the GitHub-created `actions/checkout`; a checkout-free workflow would be neither conforming nor violating; the OpenSpec CLI pin sits outside the invariant and is unchanged
- [x] 3.3 Commit implementation work per BDD zone rules and conventional commits (`(#44)` subject suffix): one code-zone commit carrying the two pin lines, the version bump, and the changelog entry — no `openspec/` files mixed in; cut the apply branch `44-apply-unify-checkout-action-pin` from `main` after the planning merge, push, and open the implementation pull request per the git discipline
- [ ] 3.4 Confirm this change's own pull-request runs green: `validate.yml` and `release.yml` run `@v7` for the first time — the Validate OpenSpec artifacts check passes and no workflow step errors; the kit reminder posts no advisory (kit paths changed, version bumped) (design D1, D3)
- [ ] 3.5 Confirm the merge behavior: the release workflow detects the `.metadex-kit` bump, passes its gates (changelog section, CLI-pin cross-check, tag novelty), and cuts kit release v1.0.1 with the bundle carrying `validate.yml` `@v7` — the release body naming the pin move is ADR-0011's adopter-facing visibility (design D3, D4)
- [ ] 3.6 Gate run (archive-time, final task): from `main`, run `uv run tools/kit_release_gate.py 44` before archiving — it passes only once v1.0.1 is published and contains the kit-touching commit (the reminder/gate pair's first substantive dogfood if this change lands before #9); on a misfire, re-run the release workflow via `workflow_dispatch` — never a second bump; the archive-phase commit carries `Closes #44`
