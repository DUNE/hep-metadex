> Verification approach for this change (tasks-stage resolution, mirroring the #7 precedent
> and issue #20's suite deferral): no runtime application exists for an acceptance runner to
> boot, so acceptance-suite scaffolding stays deferred until the first runtime change; scenario
> verification here is the validation gate (`valid: true` per ADR-0003), scripted checks against
> the release workflow's gating logic, the docs strict build, and the actual v1.0.0 release cut
> on merge — the release workflow's first run is the acceptance run for the release scenarios.
> Enforcement scenarios (CI reminder, archive gate) verify with #35; command scenarios with
> #9 and #39.

## 1. Kit identity files (hep-metadex)

- [x] 1.1 Create `.metadex-kit` at the repository root: `version: 1.0.0`, `cli: 1.16.0` (design D1 — the file ships verbatim; nothing appends to it)
- [x] 1.2 Create `KIT-MANIFEST.yaml` at the repository root mapping every copy-list path — `.agents/skills/`, `.opencode/` (commands, skills, agent definitions), `openspec/schemas/intent-driven/`, `AGENTS.md`, `docs/intent-prompt-guidelines.md`, `.github/workflows/validate.yml`, `.github/ISSUE_TEMPLATE/`, `.metadex-kit`, and `KIT-MANIFEST.yaml` itself — to exactly one ownership class (cli-owned / kit-owned / merge-guidance / never-touch) with its refresh route (design D6)
- [x] 1.3 Create `CHANGELOG.md` at the repository root with a `## [1.0.0] - <date>` section: Keep a Changelog categories, every entry referencing its change issue in the `(#N)` style (design D3)
- [x] 1.4 Verify the identity files: `.metadex-kit`'s `cli:` matches `validate.yml`'s `OPENSPEC_VERSION` (1.16.0); every copy-list path appears in `KIT-MANIFEST.yaml` exactly once; the changelog section extracts cleanly between its heading and the next heading

## 2. Release workflow (hep-metadex)

- [ ] 2.1 Create `.github/workflows/release.yml` (repo-local, never kit): push-to-`main` and `workflow_dispatch` triggers; `contents: write` permission; only `actions/checkout` plus the runner's preinstalled `git` and `gh` — with the DUNE-org action-policy comment, as `docs.yml` already carries (design D5)
- [ ] 2.2 Implement bump detection: diff `.metadex-kit` against the latest `v*` tag; a changed version is the bump, and no prior tag existing counts the version file's introduction as a bump — the v1.0.0 path
- [ ] 2.3 Implement the gates: extract the `## [X.Y.Z]` section from `CHANGELOG.md` and fail without publishing when it is missing; cross-check `.metadex-kit`'s `cli:` against `validate.yml`'s `OPENSPEC_VERSION` and fail on mismatch
- [ ] 2.4 Implement publication: tag the merge commit `vX.Y.Z`; assemble `metadex-kit-<version>.tar.gz` containing exactly the copy-list plus `.metadex-kit` and `KIT-MANIFEST.yaml` at their natural paths; generate `SHA256SUMS` covering the bundle; `gh release create` with the extracted changelog section as the body and the required OpenSpec CLI version declared
- [ ] 2.5 Verify the gates against scratch states: a scratch tree with a bumped version but no matching changelog section fails extraction; a scratch `cli:` pin mismatch fails the cross-check; bundle assembly over the current tree produces exactly the copy-list paths and a verifying checksum (discard scratch artifacts afterward)
- [ ] 2.6 Verify the workflow's footprint by construction: review it end-to-end and confirm it creates tags and releases only — no commit or push to `main` anywhere — and contains no release-please-style PR automation

## 3. Documentation (hep-metadex)

- [ ] 3.1 README quick start: re-point steps 4–5 to the release bundle — fetch `metadex-kit-<version>.tar.gz` for the latest or a pinned release, verify against the release's `SHA256SUMS`, extract, copy — and add `.metadex-kit` and `KIT-MANIFEST.yaml` to step 4's copy-list; step 2 (clone and register the store) stays unchanged, because channel 1 still needs the checkout
- [ ] 3.2 `docs/setup.md`: extend the two-channels section and its Mermaid flowchart with the release channel (the kit flows from versioned releases; the registered checkout keeps floating for specs); add `.metadex-kit`, `KIT-MANIFEST.yaml`, and `CHANGELOG.md` rows to the store-layout table; re-point the agent-assisted bootstrap prompt's scaffolding-install step to the release bundle, with the machine-prerequisites checklist unchanged (the store clone remains a channel-1 prerequisite)
- [ ] 3.3 `docs/maintainer.md`: add divergence-manifest rows for `.metadex-kit` and `KIT-MANIFEST.yaml` (new kit files installed from the release bundle) and `.github/workflows/release.yml` (repo-local, never kit — the `docs.yml` pattern); add a release-process section: the bump-and-changelog-entry-in-the-same-change rule, the kit-only semver contract (MAJOR/MINOR/PATCH), the changelog conventions with `(#N)` entries, the date convention (authored at preparation; the GitHub release timestamp is authoritative), and the `workflow_dispatch` fallback
- [ ] 3.4 `docs/usage.md`: add a release-consumption section — fetch the bundle for a chosen version, verify against `SHA256SUMS`, read the provenance stamp — linking `../CHANGELOG.md`; cross-reference the kit's declared CLI version from the CLI-pinning section
- [ ] 3.5 Add glossary entries to `glossary/technical.md`: `Kit release` (a semantically versioned, checksum-verified bundle of the **workflow scaffolding** published as a GitHub release) and `Kit version file` (`.metadex-kit` — source-side release trigger and shipped provenance stamp)
- [ ] 3.6 Verify the docs: `uv run tools/docs_site.py build` passes the strict gate; the `../CHANGELOG.md` links from usage.md and maintainer.md rewrite to GitHub blob URLs in the staged tree

## 4. Completion and first-release acceptance (hep-metadex, then post-merge)

- [ ] 4.1 Run `openspec validate add-versioned-kit-releases --type change` and confirm `valid: true` (the schema's `--strict` guidance is superseded by ADR-0003)
- [ ] 4.2 Sweep the kit-releases scenarios against the implemented state: identity files present and formatted; the manifest covers the copy-list; the changelog section extracts; the workflow gates are in place; the docs sections exist; channel-1 surfaces untouched — no changes under `.openspec-store/`, and the registration and doctor guidance in `docs/setup.md` unchanged in meaning
- [ ] 4.3 Commit implementation work per BDD zone rules and conventional commits (`(#34)` suffix); cut the apply branch `34-apply-add-versioned-kit-releases` from `main` after the planning merge, push, and open the implementation PR per the git discipline
- [ ] 4.4 First-release acceptance (post-merge): on the change's merge to `main`, confirm the workflow cuts v1.0.0 — tag, bundle, `SHA256SUMS`, changelog-sourced body, declared CLI version; if the run misfires, re-run via `workflow_dispatch` and record what happened
- [ ] 4.5 Dogfood (post-merge, final task): re-run the kit install on dune-metadex from the v1.0.0 release — fetch, verify, copy — and confirm the first adopter carries the `.metadex-kit` stamp; record any diverged-file friction as design input for #39
