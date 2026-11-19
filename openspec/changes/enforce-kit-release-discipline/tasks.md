> Verification approach for this change (tasks-stage resolution, mirroring the #34 precedent
> and issue #20's suite deferral): no runtime application exists for an acceptance runner to
> boot, so acceptance-suite scaffolding stays deferred until the first runtime change; scenario
> verification here is the validation gate (`valid: true` per ADR-0003), unit tests for the
> gate script (the `tools/docs_site_test.py` stdlib-unittest pattern), scratch-state checks of
> the reminder's detection and the manifest derivation, the reminder running green on this
> change's own pull requests, and the gate's trivially-green run at this change's archive —
> the gate's first substantive exercise (reminder fires, gate passes on a real kit-touching
> change) verifies with #9.

## 1. Single-source copy-list (hep-metadex)

- [x] 1.1 Derive release.yml's bundle assembly from `KIT-MANIFEST.yaml`'s `paths:` block (design D5): awk extraction of the quoted keys in manifest order replaces the inlined tar list, with a comment naming the manifest as the single copy-list source
- [ ] 1.2 Verify bundle equivalence: assemble the bundle over the current tree both ways — the inlined list from git history and the derived list — and confirm identical tar member lists and order, so the bundle stays byte-identical (design D5)
- [ ] 1.3 Confirm the rest of the release workflow is untouched: bump detection, changelog-section gate, CLI-pin cross-check, tag-exists check, publication, and the tags-and-releases-only footprint (ADR-0009's contract unchanged)

## 2. CI reminder (hep-metadex)

- [ ] 2.1 Create `.github/workflows/kit-reminder.yml` (repo-local, never kit): `pull_request` (opened, synchronize) trigger; only `actions/checkout` plus the runner's preinstalled `git` and `gh`, with the DUNE-org action-policy comment as release.yml carries (design D1)
- [ ] 2.2 Implement detection (design D2): diff head against the pull request's base; a kit change is any changed path under a manifest `paths:` key (awk extraction, directory entries matching their subtrees); a corresponding bump is a changed `version:` value in `.metadex-kit` between base and head — a `cli:` change alone is not a bump
- [ ] 2.3 Implement the advisory surface (design D1): on kit-change-without-bump, post a `::warning::` annotation and a pull request comment via `gh pr comment --edit-last` (creating on first post); the job exits 0 in every outcome — no failing status is ever rendered
- [ ] 2.4 Verify detection against scratch states: kit-path change without bump → the advisory fires and the job stays green; kit-path change with a version bump → no advisory; non-kit change → no advisory; version-only diff → no advisory (discard scratch artifacts afterward)

## 3. Archive gate (hep-metadex)

- [ ] 3.1 Create `tools/kit_release_gate_test.py` test-first (design D3; the apply phase's TDD guidance): stdlib unittest per the `docs_site_test.py` pattern, covering manifest-path parsing, per-commit kit-path diffs, ancestry against published-release tags, and the version diagnosis
- [ ] 3.2 Implement `tools/kit_release_gate.py` (design D3): find the change's merged commits on `main` by the `(#N)` conventional-commit subject suffix; diff each commit against its parent restricted to manifest paths; require every kit-touching commit to be an ancestor of a tag from `gh release list` — a manually pushed tag with no release does not satisfy the gate; zero kit-touching commits passes without consulting releases
- [ ] 3.3 Implement the per-cause pasteable fix (design D3): `version:` equal at the latest release tag and `HEAD` → the forgotten-bump fix ("bump the kit version file, merge, and the release cuts"); `HEAD` newer → the misfire fix ("wait for a running release, else re-run via `workflow_dispatch`") — never advising a second bump; nonzero exit on failure with the fix printed
- [ ] 3.4 Wire the gate into the archive phase (design D4): add the guidance line to `operations.archive.guidance` in `openspec/config.yaml` beside the OpenSpec Sync rule — run the kit release gate before archiving and refuse on failure
- [ ] 3.5 Verify the gate against scratch histories: a kit-touching commit under no release tag fails with the bump fix; the same commit under a tag passes; a bump merged with nothing published fails with the re-run fix; a zero-kit-path change passes trivially (discard scratch repositories afterward)

## 4. Documentation and glossary (hep-metadex)

- [ ] 4.1 `docs/maintainer.md` Kit Releases section: document the reminder (advisory at review time, never blocking), the gate (its place in the archive phase, the per-cause pasteable fixes), and the single-source copy-list the three consumers read
- [ ] 4.2 `docs/maintainer.md` divergence manifest: add a row for `.github/workflows/kit-reminder.yml` (repo-local maintainer automation, never kit — the release.yml pattern, citing ADR-0010) and a row for `tools/kit_release_gate.py` (repo-local maintainer tooling, citing ADR-0006's pattern and ADR-0010), leaving the ADR-0007 documentation-site `tools/` row untouched (design D6)
- [ ] 4.3 Add glossary entries to `glossary/technical.md` for the coined terms (house precedent, #34's glossary task): `Kit reminder` (the repo-local advisory CI check that flags kit-path changes without a version bump on a pull request) and `Kit release gate` (the repo-local archive-phase check that blocks archiving a kit-touching change until a published kit release contains its changes)
- [ ] 4.4 Verify the docs: `uv run tools/docs_site.py build` passes the strict gate; the maintainer-guide edits render and the new manifest rows link their ADRs

## 5. Completion and acceptance (hep-metadex, then archive-time)

- [ ] 5.1 Run `openspec validate enforce-kit-release-discipline --type change` and confirm `valid: true` (the schema's `--strict` guidance is superseded by ADR-0003)
- [ ] 5.2 Sweep the kit-release-discipline scenarios against the implemented state: the reminder is always-green by construction and detection matches design D2; the gate implements D3's lineage semantics with the per-cause fixes; the config guidance line is in place; the maintainer guide documents both mechanisms; the divergence manifest carries both rows; and the no-bump claim holds — `git diff` between `main` and the change shows no changes under any manifest `paths:` key
- [ ] 5.3 Commit implementation work per BDD zone rules and conventional commits (`(#35)` subject suffix); cut the apply branch `35-apply-enforce-kit-release-discipline` from `main` after the planning merge, push, and open the implementation pull request per the git discipline
- [ ] 5.4 Confirm the merge behavior: no release fires on this change's merge (bump detection finds `.metadex-kit` unchanged — zero kit paths), and the reminder runs green on the planning and apply pull requests with nothing to advise
- [ ] 5.5 Gate smoke test (archive-time, final task): from `main`, run `uv run tools/kit_release_gate.py 35` before archiving — trivially green over zero kit paths, the gate's first-ever run; the archive-phase commit carries `Closes #35`; #9's own kit-touching change is the first substantive dogfood of both mechanisms
