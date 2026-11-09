## Why

HSF evaluators and **experiment repository** maintainers currently read the hep-metadex **OpenSpec Store**'s documentation as raw Markdown in the GitHub file browser — discoverable, but not the highlighted, easy-to-read documentation the **HSF affiliation** checklist's documentation guideline expects. With the uv **maintainer toolchain** in place (#21), `docs/` can now publish in place as a Zensical-built **documentation site** on GitHub Pages — no format rewrites — with strict, CI-enforced link validation as the publishing gate.

## What Changes

- **Zensical configuration, in place.** Add `zensical.toml` (native TOML, not `mkdocs.yml` compat) with `docs_dir` pointing at `docs/` unchanged: site name and URL, explicit navigation, a minimal theme — and the single repo-URL setting that drives link rewriting.
- **Site landing page.** Add `docs/index.md`, written for the site audience (HSF evaluators and adopter maintainers); the README remains the repository front door, unchanged.
- **Toolchain dependency.** Pin Zensical as a uv dev dependency (`uv.lock`), extending the repo-local **maintainer toolchain**; nothing here enters the **workflow scaffolding** adopters copy.
- **Publishing workflow.** Add a uv-native GitHub Actions workflow (Zensical's documented Pages workflow with pip replaced by uv): pull requests run `zensical build --strict` and never publish; a push to `main` runs the same strict build and publishes to GitHub Pages. Triggers mirror `validate.yml` — push to `main` plus pull requests.
- **Out-of-tree link handling.** `docs/` sources keep their relative `../` links — they stay **org-neutral** and GitHub-friendly. A small build-time transform (part of the **maintainer toolchain**; mechanism and pipeline position settled in design.md) rewrites every `../`-escaping link to an absolute GitHub URL derived from the repo-URL setting — uniformly across all out-of-tree targets: the issue's enumerated set (README, CONTRIBUTING, LICENSE, `.github/`, `glossary/`, `adr/`) and other repo-root artifacts the docs cite (e.g., `openspec/`). The rewrite must take effect before link validation, so out-of-tree links pass strict builds as external links. A hosting move touches `zensical.toml` (repo URL, `site_url`) and the checklist's factual hosting citations — never the docs sources' relative links.
- **Checklist upgrade.** The `docs/hsf-affiliation.md` Documentation row gains the live site URL — a factual hosting citation, joining the public-repository URL already in that checklist. This is the one place the change edits a governance document, and the `governance-docs` delta below scopes the org-agnostic requirement accordingly.
- **ADR-0007.** Record the durable decisions: Zensical on GitHub Pages; native `zensical.toml`; uv-native workflow; build-time rewrite over source-editing or in-site inclusion; the factual-citation scoping of the org-agnostic governance requirement; and the uv symlink `link-mode` caveat as a consequence.
- **No removals, no breaking changes.** All six existing `docs/` pages stay at their current repo paths — including the spec-required `docs/setup.md`, `docs/usage.md`, `docs/governance.md`, `docs/hsf-affiliation.md` and the copy-listed `docs/intent-prompt-guidelines.md`.

## Capabilities

### New Capabilities

- `docs-site`: the repository publishes a **documentation site** for HSF evaluators and adopter maintainers. Enumerated contract: Zensical builds `docs/` in place from `zensical.toml`; a push to `main` publishes to GitHub Pages after a strict build; pull requests run the same strict build and never publish; the build passes `zensical build --strict` with zero invalid internal links or anchors; out-of-tree links resolve via the build-time rewrite driven by the single repo-URL setting; `docs/index.md` is the landing page; explicit navigation covers `index.md` plus every existing docs page, with titles in config so no existing page needs front-matter; spec-required paths and `docs/intent-prompt-guidelines.md` remain at their current repo paths.

### Modified Capabilities

- `governance-docs`: the HSF checklist mapping's Documentation row now cites the live **documentation site** alongside the README and `docs/` citations. Because that citation is an absolute URL that changes on a hosting move, the delta scopes the org-agnostic governance-text requirement: governance *processes* remain **org-neutral** and untouched by a hosting move, while factual hosting citations — the public-repository URL the checklist already carries, now the live site URL — are infrastructure facts exempt from the no-edit guarantee (recorded in ADR-0007). Only that scoping changes; the requirement's core guarantee holds.

## Impact

- **New files:** `zensical.toml`; `docs/index.md`; a new workflow under `.github/workflows/` (separate from the adopter-copied `validate.yml`, and not added to the **workflow scaffolding** copy-list); new **maintainer toolchain** code implementing the build-time link rewrite (Zensical hook or plugin — settled in design.md); `adr/0007-*.md`.
- **Modified files:** `pyproject.toml` and `uv.lock` (Zensical pinned as a dev dependency); `docs/hsf-affiliation.md` (Documentation row); `glossary/technical.md` (new **documentation site** term).
- **Dependencies:** Zensical and its dependencies join the repo-local **maintainer toolchain** (Python 3.14 + uv, ADR-0006). No runtime dependencies exist or change.
- **Systems:** GitHub Pages. One-time operational precondition: a repository admin enables Pages with the GitHub Actions publishing source — no pull request can accomplish this, and the publish requirement is untestable until it is done (carried as an implementation task). The site serves at the Pages project subpath (`<org>.github.io/hep-metadex`); `site_url` matches it.
- **Validation honesty:** Zensical's strict gate validates internal links and anchors at build time. The rewritten external GitHub URLs are guaranteed by the deterministic mapping — the build does not fetch-check external targets.
- **Guardrails:** nothing on the scaffolding copy-list (`.agents/skills/`, `.opencode/`, `openspec/schemas/intent-driven/`, `AGENTS.md`, `docs/intent-prompt-guidelines.md`, `.github/workflows/validate.yml`) is modified; README, runtime code, and public APIs are untouched.
- **Out of scope:** glossary/ADR site migration (candidate follow-up change), custom domain, analytics, blog, Zensical Studio, acceptance tests (issue #20), runtime code.
