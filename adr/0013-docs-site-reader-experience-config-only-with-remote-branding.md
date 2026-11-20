# ADR-0013: Keep the docs site reader experience config-only with remotely referenced branding

## Status

Accepted

## Date

2026-11-20

## Context and Problem Statement

The **documentation site** ADR-0007 delivered publishes with Zensical's built-in theme at default settings: no color-scheme handling, the default favicon and logo, a flat seven-page navigation, and a full page load on every click. HSF evaluators and adopter maintainers — the audience the site exists for — expect a modern reading experience, while ADR-0007's boundaries stand: docs sources never change for the site's sake, the site tooling stays repo-local outside the **workflow scaffolding**, and a hosting move remains a `zensical.toml`-only infrastructure event. Exploration on 2026-11-19, verified against the pinned Zensical 0.1.0 (zensical-ui 0.0.41), established that the theme's palette toggle, branding, feature flags, and sectioned navigation are all `[project.theme]` and `nav` configuration that round-trips the staging pipeline (`tools/docs_site.py`) unchanged — while the DUNE organization avatar that should brand the site lives at a remote GitHub URL, not in the repository.

## Considered Options

- Configure the reader experience entirely in `zensical.toml` (`[project.theme]` plus sectioned `nav`), branding by remote avatar URL
- Modernize with custom CSS, theme overrides, and vendored brand assets
- Keep the default theme and spend the effort on in-site content expansion first

## Decision Outcome

Chosen option: "Configure the reader experience entirely in `zensical.toml`, branding by remote avatar URL", because it delivers the three-way palette toggle (persisted by the theme itself), instant navigation, the enabled feature set, and DUNE branding without breaching any ADR-0007 boundary: docs sources stay untouched, the staging wrapper and the strict CI gate stay as they are, and reader-facing behavior remains single-file configuration. Branding by URL keeps a hosting move enumerable: the settings such a move edits widen from `repo_url` and `site_url` to include the avatar URL — still an infrastructure event confined to `zensical.toml`. ADR-0007 is extended, not superseded.

### Consequences

- Good, because evaluators get color-scheme handling, fast in-site navigation, an audience-sectioned sidebar, and DUNE branding with zero docs-source edits and no new tooling to maintain.
- Good, because the widened hosting-move edit set stays in one file, and the **maintainer toolchain**'s strict build keeps enforcing zero invalid links and anchors through the unchanged wrapper.
- Bad, because branding depends on `avatars.githubusercontent.com` availability at read time — degradation is cosmetic (content and navigation are unaffected), and a vendored fallback is deliberately excluded because it would break the hosting-move property.
- Bad, because CI's strict gate cannot assert reader-runtime behavior (palette persistence, instant navigation); enforcement rests on the strict build plus built-HTML marker checks at apply time.
- Follow-up: re-verify feature flags and rendered markers whenever the Zensical pin moves (0.1.2 / zensical-ui 0.0.43 here); in-site reference content (glossary, ADRs, specs, change archives) remains a separate follow-up issue.
