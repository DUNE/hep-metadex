> Verification approach for this change (tasks-stage resolution, mirroring the #34 precedent
> and issue #20's suite deferral): no runtime application exists for an acceptance runner to
> boot, so acceptance-suite scaffolding stays deferred until the first runtime change; scenario
> verification here is the validation gate (`valid: true` per ADR-0003), scripted checks against
> the release workflow's asset and dedupe logic, the docs strict build, the actual v1.1.0
> release cut on merge (the archive gate's first dogfood), and a scratch-repository bootstrap
> exercising the command end to end. Update-path scenarios verify with #39; signing with #36.

## 1. The command (hep-metadex kit source)

- [x] 1.1 Create `.opencode/commands/hep-metadex-bootstrap.md` with the house command shape — frontmatter `description:`, then Steps / Output / Guardrails — whose Steps mirror the documented prompt's numbered steps one to one (design D1)
- [x] 1.2 Implement the prerequisites phase (design D2): check that `openspec --version` runs and `openspec store list` shows hep-metadex; fetch the release's bundle, command asset, and SHA256SUMS into a temporary directory (latest by default, or the release named by `$ARGUMENTS` as a bare semver with a tolerated `v` prefix); verify with `sha256sum -c`; read the bundled `.metadex-kit`'s `cli:` pin and compare against the installed CLI; stop with a clear report naming the missing prerequisite on any failure — all before the first write to the target repository
- [x] 1.3 Implement the bootstrap steps in prompt order: `openspec init` for the repository's agent tools; extract the verified bundle at its natural paths with `AGENTS.md` merged per its merge-guidance class, never overwritten; handle the host-conditional GitHub files (GitHub-hosted: confirm `validate.yml` and `.github/ISSUE_TEMPLATE/` remain; other hosts: remove the extracted `.github/` kit files and name the equivalent `valid: true` gate and intent-material issue convention); author `openspec/config.yaml` (intent-driven schema, references block naming the store id and remote, context block for the repository's real stack, stage rules mirroring hep-metadex — never a `store:` line; brownfield: add only the references block); iterate `openspec doctor` to green
- [x] 1.4 Implement the output and guardrails (design D1, D5): the run creates no change and writes no implementation code; a fetched-command/installed-kit version skew warns and proceeds with both versions recorded; the final report lists what was installed, the versions in play, and the final doctor output
- [x] 1.5 Fidelity check: diff the command's steps against the agent-assisted bootstrap prompt in `docs/setup.md` — every prompt step is automated, nothing beyond the prompt's substance is added (the specification-fidelity requirement)

## 2. Manifest and release workflow (hep-metadex)

- [x] 2.1 Extend `KIT-MANIFEST.yaml`: add the per-file entry `".opencode/commands/hep-metadex-bootstrap.md": kit-owned` and state the most-specific-matching-path precedence in the header comment (design D4, D6)
- [x] 2.2 Extend `.github/workflows/release.yml` publication (design D3): publish the command file as the flat asset `hep-metadex-bootstrap.md` derived from the same checkout file the bundle carries; generate SHA256SUMS over both assets; attach bundle, SHA256SUMS, and the command asset to `gh release create` — no new Actions, the `@v7` checkout pin per ADR-0011
- [x] 2.3 Implement nested-entry dedupe in bundle assembly (design D4): when deriving the tar member list from the manifest's `paths:` block, drop any entry nested inside another entry, so the bundle's member set stays the pre-change set plus the new command file exactly once
- [x] 2.4 Verify against scratch states: the dedupe drops the nested per-file entry but keeps standalone entries; bundle assembly over the current tree contains the command file exactly once; a scratch two-asset SHA256SUMS passes `sha256sum -c` with both assets present and fails when either is altered (discard scratch artifacts afterward)

## 3. Documentation and glossary (hep-metadex)

- [x] 3.1 `docs/setup.md`, agent-assisted bootstrap section (design D7): document the one-liner — fetch `hep-metadex-bootstrap.md` from `releases/latest`, hand it to the agent — as the primary path; keep the machine-prerequisites checklist; reframe the documented prompt as the fallback and the specification; the prompt's five steps keep their order and substance
- [x] 3.2 Generalize the manual fetch detail (design D3) in the setup.md prompt's kit step, the README quick-start step 4, and `docs/usage.md`'s consumption section: fetch the assets SHA256SUMS lists (bundle and command file), one `sha256sum -c`, then extract the bundle; extend the README quick-start's pointer sentence to name the command (design D7)
- [x] 3.3 `docs/usage.md` ownership guidance: add the per-file kit-owned exception — the kit's `hep-metadex-*` command files are kit-owned while CLI-delivered files in the same directory stay cli-owned, most-specific matching path wins (design D6)
- [x] 3.4 `docs/maintainer.md`: add the divergence-manifest row for `.opencode/commands/hep-metadex-bootstrap.md` (the kit's first kit-owned command, inside the cli-owned commands directory; the template ships none) and extend the release-workflow row's description to the published command asset (design D6)
- [x] 3.5 Add the `Bootstrap command` term to `glossary/technical.md`: the `/hep-metadex-bootstrap` kit command automating the documented agent-assisted bootstrap prompt — kit-shipped and release-fetched per ADR-0012
- [x] 3.6 Verify the docs: `uv run tools/docs_site.py build` passes the strict gate; the setup.md two-channels Mermaid still matches the copy-list

## 4. Kit release and completion (hep-metadex, then post-merge)

- [x] 4.1 Bump `.metadex-kit` to `version: 1.1.0` (`cli: 1.16.0` unchanged) and add the `## [1.1.0] - <date>` `CHANGELOG.md` section — Added: the bootstrap command, the one-liner and its checksummed release asset, the per-file manifest entry — referencing `(#9)` (design D8)
- [x] 4.2 Run `openspec validate add-metadex-bootstrap-command --type change` and confirm `valid: true` (the schema's `--strict` guidance is superseded by ADR-0003)
- [x] 4.3 Sweep the change's scenarios against the implemented state: the command file ships in the copy-list and the bundle; the manifest's per-file entry resolves most-specific against the directory entry; the release workflow's gates and three-asset publication are in place; the docs sections exist; channel-1 surfaces untouched — nothing under `.openspec-store/` changes and the registration and doctor guidance keeps its meaning
- [x] 4.4 Commit implementation work per BDD zone rules and conventional commits (`(#9)` suffix); cut the apply branch `9-apply-add-metadex-bootstrap-command` from `main` after the planning merge, push, and open the implementation PR per the git discipline
- [x] 4.5 First-dogfood acceptance (post-merge): confirm the merge cuts v1.1.0 — tag, bundle with the command file exactly once, the `hep-metadex-bootstrap.md` asset, two-entry SHA256SUMS, changelog-sourced body, declared CLI version — and that the archive gate then passes (`uv run tools/kit_release_gate.py 9`), its first dogfood; if the release run misfires, re-run via `workflow_dispatch`, never a second bump
- [x] 4.6 Scratch-repository dogfood (post-merge, final task): run the one-liner and the command against a scratch greenfield repository and a scratch brownfield repository (existing `AGENTS.md` and `openspec/config.yaml`) — confirm the prerequisites stop behavior, checksum verification, the `AGENTS.md` merge, the references-only config edit, doctor green, the final report, and no change or implementation writes; record any friction as design input for #39
