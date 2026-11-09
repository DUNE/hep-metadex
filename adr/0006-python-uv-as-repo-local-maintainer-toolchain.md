# ADR-0006: Adopt Python and uv as the repo-local maintainer toolchain

## Status

Accepted

## Date

2026-11-08

## Context and Problem Statement

hep-metadex is a zero-runtime specification repository — an **OpenSpec Store** whose content reaches **experiment repositories** through two channels (ADR-0001: specs read-only through the store, **workflow scaffolding** by template install). Its own tooling story is a declared absence: `openspec/config.yaml`'s `context` block opens `Tech stack: TBD`, and `docs/hsf-affiliation.md` claims the stack is TBD by design until the first runtime change. But tooling needs arrive ahead of any runtime change: the Zensical docs build (#22) needs a pinned interpreter and a dependency anchor, future utility scripts need a base, and the acceptance suite deliberately stays unscaffolded until a runnable target exists (#20) — so the acceptance stack must not be pre-committed either. Leaving the stack TBD invites ad-hoc tool choices that could leak into the kit or read as an adopter mandate.

## Considered Options

- Python 3.14 managed by uv as a repo-local **maintainer toolchain**: pinned interpreter, bare project file, committed lockfile; no adopter mandate; acceptance `stack:` deferred
- Keep the stack TBD until the first runtime change (the documented status quo)
- Declare a family-wide stack: Python for the store and every adopting repository
- Node.js as the toolchain, matching the kit's JavaScript acceptance pack and gherkin-lint

## Decision Outcome

Chosen option: "Python 3.14 managed by uv as a repo-local **maintainer toolchain**", because the repository needs a pinned, reproducible toolchain now — not at some future runtime change — while the store's adopter-autonomy mandate forbids any family-wide stack; uv's bare project shape (`[project]`, no build system) matches the zero-runtime reality, its committed lockfile anchors reproducibility for #22's CI, and its `[dependency-groups]` reserves the landing zone for Zensical. The toolchain is repo-local — a non-channel: it flows through neither of ADR-0001's channels, appears on no adopter copy-list, and the acceptance `stack:` key stays unset, with Python recorded here as the expected default only once a runnable target exists (#20). uv itself is unpinned; the lockfile is the compatibility anchor.

### Consequences

- Good, because every future artifact workflow is injected a true stack statement instead of TBD, and #22 can land Zensical with `uv add --dev` against the reserved `[dependency-groups]`.
- Good, because the boundary is recorded in three places maintainers read — the **maintainer toolchain** glossary term, the divergence-manifest row, the README repository map — so the toolchain cannot silently become kit.
- Good, because the deferred `stack:` keeps the acceptance suite honest: no runner is scaffolded and no language is forced while nothing runnable exists.
- Bad, because maintainers' machines need uv (a second tool beside the pinned OpenSpec CLI) for docs and tooling work; adopters never do.
- Bad, because the 3.14 pin and lockfile carry occasional maintenance — a minor bump is a one-line `.python-version` edit plus `uv sync` and a lockfile commit.
- Follow-up: #22 lands Zensical in the `[dependency-groups]` and revisits uv pinning when its CI installs uv explicitly; #20 scaffolds the acceptance suite and records the `stack:` key when the first runtime target exists.
