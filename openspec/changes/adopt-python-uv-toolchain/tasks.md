> Verification approach for this change (ADR-0006; design, Open Questions,
> resolved): no runtime application exists for an acceptance runner to boot,
> and the acceptance `stack:` key deliberately stays unset until a runnable
> target exists (#20) — so acceptance-suite scaffolding stays deferred.
> Verification is the validation gate (`valid: true`, non-strict per
> ADR-0003), the scripted checks in groups 1 and 3 (clean-clone `uv sync`,
> pinned-version check), and the deliverable sweep in group 3.

## 1. uv project scaffolding (code zone)

- [ ] 1.1 Create `pyproject.toml` — bare `[project]` with `name = "hep-metadex"`, a `version`, and `requires-python = ">=3.14"`; no build system, no package scaffolding; dev tooling reserved for uv's `[dependency-groups]`, introduced empty (design D2, ADR-0006)
- [ ] 1.2 Create `.python-version` pinning `3.14` — the major-minor pin lets uv absorb patch releases (design D2)
- [ ] 1.3 Extend `.gitignore` with `.venv/` (design D2)
- [ ] 1.4 Run `uv sync` to generate `uv.lock` and the environment; verify `uv run python -V` reports 3.14.x
- [ ] 1.5 Commit as `chore(toolchain): add uv scaffolding with the Python 3.14 pin (#21)` — code zone: nothing under `openspec/` uncommitted alongside

## 2. Governance and documentation alignment

- [ ] 2.1 Rewrite the `context` line in `openspec/config.yaml` per design D4 — Python 3.14 managed by uv, repo-local **maintainer toolchain**, zero-runtime, no adopter mandate — leaving no "TBD" and declaring no acceptance stack; commit as `docs(openspec): replace tech stack TBD with the maintainer toolchain (#21)` (specs zone: its own commit, landed before any code-zone work in 2.2–2.4 begins)
- [ ] 2.2 Rewrite the "General information" row in `docs/hsf-affiliation.md` per design D5 — name the **maintainer toolchain** (Python 3.14 via uv, pinned interpreter, no runtime code) while preserving the row's claims that the repository map describes the layout and adopters' tool dependency is unchanged (the OpenSpec CLI, pinned 1.16.0); keep the wording **org-neutral** (ADR-0002); commit as `docs(governance): rewrite the general-information row for the declared toolchain (#21)`
- [ ] 2.3 Add the divergence-manifest row in `docs/maintainer.md` per design D6 — `pyproject.toml`, `uv.lock`, and `.python-version` as **maintainer toolchain** files outside the install guide's file list, mirroring the existing `package.json` row's sync semantics — and update the existing `.gitignore` row's reason to "Only `openspec/.cache/` and `.venv/` are needed so far"; commit as `docs(maintainer): record the maintainer toolchain divergence rows (#21)`
- [ ] 2.4 Add the **maintainer toolchain** row to the README repository map per design D6 — the files are maintainer-side tooling, explicitly not part of what adopters copy; commit as `docs(readme): note the maintainer toolchain in the repository map (#21)`

## 3. Verification and completion

- [ ] 3.1 Clean-clone verification (issue #21 rule): clone the apply branch to a scratch directory, run `uv sync` and confirm it succeeds, and confirm `uv run python -V` reports the pinned 3.14.x
- [ ] 3.2 Run `openspec validate adopt-python-uv-toolchain --type change` and confirm `valid: true` (non-strict per ADR-0003; this change declares `skip_specs`, so no delta scenarios exist)
- [ ] 3.3 Sweep the deliverables against issue #21's rules: no "TBD" remains in the `context` block; the acceptance `stack:` key is absent from `openspec/config.yaml`; the hsf-affiliation row still maps every required guideline; the divergence manifest, the README repository map, and the glossary term carry the same repo-local boundary; no adopter-facing artifact changed — the README step-4 copy list and the **workflow scaffolding** kit are untouched
- [ ] 3.4 Commit any remaining work per conventional commits with the `(#21)` suffix and the BDD zone rules, push the apply branch `21-apply-adopt-python-uv-toolchain` (cut from `main` after the planning merge), and open the implementation PR referencing issue #21
