## Why

The repository still declares its tech stack TBD — in the `openspec/config.yaml` context block and the `docs/hsf-affiliation.md` "General information" row — so maintainers have no pinned, reproducible toolchain for the dev tooling ahead (the Zensical docs build, #22) or for future utility scripts. Adopting Python + uv now establishes a **maintainer toolchain** while the repository stays zero-runtime, without constraining **experiment repositories** or pre-committing the acceptance-test language.

## What Changes

- **ADR-0006** — records the decision and its boundaries: Python + uv are the **maintainer toolchain** for hep-metadex itself, nothing is mandated for adopting repositories, and the acceptance `stack:` key stays unset with selection deferred until a runnable target exists (expected default: Python).
- **uv project scaffolding** — a deliberately bare `pyproject.toml` (`[project]` with `name = "hep-metadex"` and `requires-python = ">=3.14"`; no build system, no package scaffolding), `.python-version` pinning Python 3.14, a committed `uv.lock` for reproducible syncs, and `.gitignore` additions for the uv workspace. Dev tooling lands in uv's `[dependency-groups]` — empty in this change, reserved for #22's Zensical. Success is observable from a clean clone: `uv sync` succeeds and `uv run python -V` reports the pinned version.
- **`openspec/config.yaml` context** — replaces the `Tech stack: TBD` line with the Python/uv statement, leaving no "TBD" in the `context` block.
- **`docs/hsf-affiliation.md`** — rewrites the "General information" row so it no longer claims the tech stack is TBD by design: the **maintainer toolchain** is declared while the repository remains zero-runtime with no runtime dependencies.
- **`docs/maintainer.md` divergence manifest** — gains a row mirroring the existing "Not installed: `package.json`" row: `pyproject.toml`, `uv.lock`, and `.python-version` are **maintainer toolchain** files outside the install guide's file list, with the same semantics — not added during a template sync without a deliberate decision.
- **README repository map** — adds a note identifying the new Python files as **maintainer toolchain** tooling, not something adopters copy in.
- **`glossary/technical.md`** — defines the **maintainer toolchain** term beside **workflow scaffolding** — the Python + uv tooling (interpreter pin, project file, dev dependencies) used to maintain hep-metadex itself — so prose can distinguish this repository's own tooling from the kit that flows outward.
- **Out of scope** — acceptance-test scaffolding and any acceptance `stack:` declaration; the Zensical docs build and its CI (#22); runtime code; changes to the vendored skills or **workflow scaffolding** kit; any mandate on **experiment repositories**.

## Capabilities

### New Capabilities

None — the change is internal to hep-metadex: none of the four published specs (adopter-onboarding, experiment-references, governance-docs, store-identity) mentions the tech stack, so no new **common capability** is warranted.

### Modified Capabilities

None — no published requirement changes; the work is confined to the **maintainer toolchain** and its documentation.

## Impact

- **Repositories** — hep-metadex only, which implements the change itself; no **experiment repository** changes, because the toolchain is not part of the **workflow scaffolding** adopters copy by template install.
- **No breaking changes** — the repository stays zero-runtime and the **OpenSpec Store** contract is untouched: consumers keep reading the published specs read-only through their **Store reference**, and no adopting repository consumes the new files.
- **Tool dependency** — uv joins the **maintainer toolchain** and manages the pinned Python 3.14 interpreter; adopters are asked to install nothing new — the OpenSpec CLI remains the only tool the documented adoption path asks for.
- **Process** — tracked as issue #21 on branch `21-adopt-python-uv-toolchain`; commits use the conventional format with a `(#21)` subject suffix, and `Closes #21` appears only in the archive-phase commit, keeping the issue open until archive.
- **Downstream** — unblocks the Zensical docs build (#22): its dependency can land in the `[dependency-groups]` this scaffolding introduces, and its CI can rely on the committed `uv.lock` for reproducible builds. The pinned interpreter also anchors future utility scripts, and ADR-0006's record of the deferred `stack:` decision gives later changes a settled context.
