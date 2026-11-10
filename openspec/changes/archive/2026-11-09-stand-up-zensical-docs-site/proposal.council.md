# Council Notes: proposal

## Author Summary

Single author round (`adversarial-author`). Draft covered all seven issue deliverables, respected the scaffolding copy-list and path-stability rules, and matched the settled grill-me decisions (build-time rewrite, new `docs/index.md`, PR strict-build gate, `docs-site` + `governance-docs` split). The author flagged three risks itself: the live-URL-in-checklist vs. hosting-move tension, out-of-scope placement, and the Pages-via-Actions assumption.

## Reviewer Challenges

- The draft claimed the hosting-move invariant "keeps holding" while adding an absolute live site URL to `docs/hsf-affiliation.md` — a self-contradiction the rewrite mechanism cannot fix (site URLs are not `../` links).
- The build-time rewrite was load-bearing but had no owner in the Impact file list, and rested on unstated assumptions (rewrite-before-validation ordering; whether strict mode covers rewritten external URLs).
- The `docs-site` capability said nothing about navigation coverage — pages could be silently dropped from an explicit nav; the front-matter question (titles vs. "no format rewrites") was open.
- Claimed the workflow "mirrors `validate.yml`" while describing a different trigger set.
- Suggested: enumerate the capability's contract items; make "PRs never publish" an explicit negative; trim repeated "runtime code untouched" claims; elevate the Pages prerequisite to a named operational precondition; use the **OpenSpec Store** glossary term.
- Risks raised: external-link validation scope; transform pipeline position; out-of-tree straggler targets beyond the issue's enumerated set; Pages subpath handling; capability overlap with `store-identity`/`adopter-onboarding`; publishing the copy-listed `docs/intent-prompt-guidelines.md`.

## Resolutions

- Accepted: named the live-URL/hosting-move collision in What Changes and Modified Capabilities; the delta scopes the org-agnostic requirement (processes stay org-neutral; factual hosting citations are exempt infrastructure facts, recorded in ADR-0007); corrected the "one config line" claim (hosting move touches `zensical.toml` and factual citations, never relative links).
- Accepted: the rewrite transform now has an owner in Impact (new maintainer-toolchain code; mechanism settled in design.md); the rewrite-covers-all-out-of-tree-targets rule (including `openspec/` stragglers found by grep) and the rewrite-before-validation requirement are stated; validation honesty added (strict gate = internal links/anchors; external URLs guaranteed by mapping, not fetch-checked).
- Accepted: navigation coverage enumerated in the capability; verified against Zensical's navigation docs that nav titles live in `zensical.toml`, so no existing page needs front-matter.
- Accepted (improvements): enumerated contract in `docs-site`; explicit "PRs never publish"; trimmed repetition; Pages-enabled-via-Actions elevated to a named one-time precondition (verified as required in Zensical/GitHub docs); **OpenSpec Store** term used in Why.
- Rejected: the mirroring-inconsistency challenge's premise — `validate.yml` triggers on push to `main` + pull requests, not any-branch pushes, so the mirror claim is accurate; trigger sets are nonetheless now stated explicitly.
- Resolved by research (not deferred): out-of-tree stragglers (grep found `../openspec/` targets; rewrite is uniform); nav front-matter question (config-side titles verified); external-link validation scope (Zensical docs: "validates all internal links").
- Resolved by spec reading: no `store-identity`/`adopter-onboarding` overlap (README quick-start behavior untouched; docs-site adds publishing, not content changes); no spec restricts publishing the copy-listed guidelines page.

## Remaining Risks

- Rewrite-before-validation ordering is a design-stage feasibility item: the chosen hook/plugin mechanism must transform page content before link validation runs, or all 58 out-of-tree links fail strict builds.
- Pages project-subpath serving (`<org>.github.io/hep-metadex`): `site_url` and any path-sensitive settings must match; design stage confirms.
- Zensical's Python 3.14 compatibility is assumed (2025-era tool, pinned interpreter is 3.14); verify at implementation via `uv add --dev zensical` resolution.
