## Why

The **documentation site** is what HSF evaluators and adopter maintainers actually read when they assess hep-metadex — the audience whose reading experience decides the project's credibility. Today that site (ADR-0007) runs Zensical's built-in theme with default settings: no color-scheme handling, so readers who prefer dark mode get none; the default favicon and logo, carrying no DUNE identity; a flat seven-page navigation with no grouping by audience; and a full page load on every click.

Now is the right time to close that gap, because the cost collapsed. Exploration on 2026-11-19, verified against the pinned Zensical 0.1.0 (zensical-ui 0.0.41), established that every improvement below is a config-only change to `zensical.toml`'s `[project.theme]` section: a scratch strict build with the full candidate config passed the staging pipeline unchanged, and every theme component rendered in the built HTML. Zensical 0.1.2 (zensical-ui 0.0.43), which carries bug fixes, is available to pin.

## What Changes

The site's theme and navigation are modernized entirely through `zensical.toml` configuration plus a dev-dependency bump in the **maintainer toolchain**:

- **Theme configuration** — a new `[project.theme]` section provides:
  - a three-way palette toggle — system preference (`prefers-color-scheme`) → light → dark — with the reader's choice persisted across pages;
  - the DUNE org avatar `https://avatars.githubusercontent.com/u/7131646?s=200&v=4` (fixed by the issue, not a delegated decision) as both favicon and header logo;
  - the reader-experience features: navigation footer (previous/next), instant navigation, instant prefetching, reading-progress indicator, automatic previews, anchor tracking, navigation sections, navigation-path breadcrumbs, navigation expansion, navigation pruning, TOC anchor following, and the back-to-top button.
- **Sectioned navigation** — the flat seven-entry `nav` becomes audience-oriented sections over the same existing pages (for example: Getting Started, Governance, Maintainers), with all titles in configuration and no page gaining front-matter.
- **Hosting-move edit set** — the avatar URL joins `repo_url` and `site_url` as the settings a hosting move edits in `zensical.toml`; the file's header comment is updated to say so.
- **Dependency bump** — the **maintainer toolchain** requires Zensical ≥ 0.1.2 (`pyproject.toml`) and locks 0.1.2 (`uv.lock`, up from 0.1.0).

Decisions deliberately left open for this change's later artifacts: final section grouping and titles (including whether Home stays an unsectioned top-level entry); primary/accent palette colors; expand-vs-prune tuning for a site of this size.

Out of scope, per the issue: in-site reference content (glossary, ADRs, specs, change archives — a follow-up issue), tools API documentation, custom domain, analytics, Zensical Studio, and any docs-source edit.

There are no breaking changes: the change is configuration-only, docs sources remain untouched, and the same seven pages publish at the same paths.

## Capabilities

### New Capabilities

- None. Everything this change introduces — palette toggle, branding URL, enabled theme features, sectioned navigation — is spec-level behavior of the same site the `docs-site` capability already owns: one config file, one build, one CI gate. Splitting a theme capability out would divide that ownership for no boundary benefit.

### Modified Capabilities

- `docs-site` — one delta at `specs/docs-site/spec.md`:
  - *Modified — In-place site build*: the site is configured with a reader-facing theme (palette toggle, branding, enabled features) instead of a "minimal theme", and the **maintainer toolchain** requires Zensical ≥ 0.1.2, locked to 0.1.2 in `uv.lock`.
  - *Modified — Site landing page and full navigation*: the flat list becomes audience sections over the same seven pages — titles in configuration, no front-matter, every page still covered.
  - *Modified — Out-of-tree link resolution*: the hosting-move scenario's edit set becomes `repo_url`, `site_url`, and the avatar URL.
  - *Added*: new requirements for the persisted three-way palette toggle, the favicon/logo branding, and the enabled theme feature set.
  - The remaining requirements — strict link validation, publish to GitHub Pages on `main`, and documentation paths and scaffolding untouched — are unchanged constraints this change must keep passing.

## Impact

- **Files changed:** `zensical.toml` (new `[project.theme]` section, sectioned `nav`, avatar URL, header-comment update), `pyproject.toml` (dev dependency → `zensical>=0.1.2`), `uv.lock` (0.1.0 → 0.1.2), and the change's `docs-site` delta spec. Nothing else.
- **Maintainer toolchain:** `tools/docs_site.py` needs no change — its derived-config serializer deep-copies every setting it does not itself derive, so the theme table round-trips through the staging wrapper unchanged.
- **CI:** `.github/workflows/docs.yml` is unchanged; `uv sync --locked` plus the wrapper build pick up the new pin, and GitHub Pages keeps deploying from `main` only. The strict build contains the link- and anchor-level risk; theme rendering is not CI-verified — the 2026-11-19 rendering check ran on 0.1.0, so applying this change re-runs the strict build and a rendered-HTML check on the 0.1.2 pin.
- **Docs sources:** untouched, per ADR-0007 — no page gains front-matter, the staging-pass link rewrite is unaffected, and docs sources keep their relative, **org-neutral** links.
- **Workflow scaffolding:** untouched — none of `zensical.toml`, `pyproject.toml`, `uv.lock`, or `tools/` are kit paths in KIT-MANIFEST.yaml, so no kit release follows.
- **Readers:** HSF evaluators and adopter maintainers gain color-scheme handling, fast in-site navigation, and an organized sidebar; no reader-facing URL changes.
- **Known trade-off, accepted by the issue:** the favicon and logo load from `avatars.githubusercontent.com` at read time, so branding depends on GitHub's avatar CDN availability.
