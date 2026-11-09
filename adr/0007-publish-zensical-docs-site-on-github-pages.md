# ADR-0007: Publish the documentation site with Zensical on GitHub Pages, built from docs/ in place

## Status

Accepted

## Date

2026-11-09

## Context and Problem Statement

HSF evaluators and adopter maintainers read hep-metadex documentation as raw Markdown in the GitHub file browser, while the **HSF affiliation** checklist's documentation guideline expects a highlighted, easy-to-read user's guide. `docs/` is plain Markdown and ports to a static site generator without format rewrites, but two boundary conditions constrain the choice: the six `docs/` pages carry 58 relative links to repository-root artifacts (`glossary/`, `adr/`, README, LICENSE, CONTRIBUTING, `.github/`, `openspec/`) that a `docs_dir`-scoped build cannot resolve, and the repository's governance documents are spec-bound **org-neutral** — hardcoding absolute `github.com/DUNE/...` URLs into docs sources would break the hosting-move guarantee. The **maintainer toolchain** (ADR-0006) reserved a uv `[dependency-groups]` landing zone for exactly this build, and Zensical — its native `zensical.toml` config, build-time link validation, and `--strict` CI gate — is the documented fit; it runs no arbitrary plugins and exposes no hook API today.

## Considered Options

- Zensical on GitHub Pages, docs built in place via a **maintainer toolchain** staging pass that rewrites out-of-tree links to absolute GitHub URLs derived from one config setting
- Zensical with docs sources edited to absolute GitHub URLs directly
- In-site inclusion of `glossary/`, `adr/`, and repository-root documents (copies or build-time inclusions)
- Waiting for Zensical's native Module API to do the rewrite in-build

## Decision Outcome

Chosen option: "Zensical on GitHub Pages with the staging-pass link rewrite", because the **documentation site** must publish from `docs/` in place while docs sources stay **org-neutral** and GitHub-friendly; the staging pass (`tools/docs_site.py`, part of the **maintainer toolchain**) is the only semantics-preserving mechanism available today, and `repo_url` in the committed `zensical.toml` is the single setting a hosting move updates. The committed `zensical.toml` keeps `docs_dir = "docs"`; the strict build (`zensical build --strict`) runs against the staged, rewritten tree through a derived config, gating both pull requests (build only, never publish) and pushes to `main` (build plus GitHub Pages deploy). The uv-native CI pins uv, closing ADR-0006's deferred pinning question.

### Consequences

- Good, because evaluators get a published, navigable site whose strict build guarantees zero invalid internal links or anchors, and the HSF checklist's Documentation row can cite the live URL.
- Good, because docs sources never change for the site's sake: a hosting move edits `zensical.toml` (`repo_url`, `site_url`) and the checklist's factual hosting citations — which are thereby scoped, in the `governance-docs` spec, as infrastructure facts exempt from the org-neutral no-edit guarantee; governance processes remain **org-neutral** (ADR-0002 clarified, not superseded).
- Good, because the site tooling is a repo-local non-channel like the **maintainer toolchain**: ADR-0001's two channels are untouched and nothing joins the **workflow scaffolding** adopters copy.
- Bad, because the staging pass is maintainer-side machinery to keep working: `.site-src/` is regenerated on every build, and local preview wants the wrapper (`tools/docs_site.py serve`) rather than plain `zensical serve`, which warns on all 58 out-of-tree links.
- Bad, because uv's default cache link mode (hardlinks/symlinks) can misbehave on network or exotic local filesystems — CI on `ubuntu-latest` is unaffected; affected maintainers set `UV_LINK_MODE=copy`.
- Bad, because Zensical's strict validation covers internal links and anchors only; the rewritten external GitHub URLs are guaranteed by the deterministic mapping, not fetch-checked at build time.
- Follow-up: when Zensical's native Module API ships publicly, collapse the staging pass into an in-build module; glossary/ADR in-site inclusion remains the candidate follow-up change; acceptance-suite wiring stays with #20.
