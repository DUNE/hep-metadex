# Council Notes: proposal

## Author Summary
The author drafted the proposal around a single thesis: the published site's reading experience lags its HSF-evaluator audience, and 2026-11-19 exploration collapsed the cost to config-only `[project.theme]` settings plus a dependency bump. New capabilities judged none; the `docs-site` capability absorbs the delta (three modified requirements, new theme requirements added). Delegated decisions (section grouping/titles, palette colors, expand-vs-prune tuning) kept open; no breaking changes.

## Reviewer Challenges
- "navigation-path breadcrumbs" duplicated in the theme feature list (13 listed for the issue's 12).
- "list navigation" wording slip in the Impact readers bullet.
- The issue's out-of-scope boundary was missing entirely.
- The `zensical.toml` header comment (hosting-move edit set) goes stale and was unaccounted for.
- "Risk stays contained by the strict CI build" overclaims: the strict build covers links/anchors, not theme rendering.
- Serializer claim ("deep-copies every setting outside navigation") sharper than verified fact (it derives at least `docs_dir` too).
- The exact avatar URL — an issue SHALL, not a delegated decision — was dropped.
- Pin vs floor conflated (`uv.lock` locks 0.1.2; the ≥ 0.1.2 floor lives in `pyproject.toml`).
- Impact "Tooling" label missing the **maintainer toolchain** glossary term; "the rest of the configuration remains org-neutral" stretches the term beyond its glossary definition.
- Added theme requirements nested under the navigation bullet muddles ADDED vs MODIFIED delta structure.
- "No kit version bump required" infers beyond KIT-MANIFEST without tracing to kit-release discipline.
- Version-skew risk: all verification ran on 0.1.0; the change pins 0.1.2.
- Home placement (index.md) unaddressed by the issue's example sections.
- Remote avatar as a runtime branding dependency unacknowledged.

## Resolutions
- Accepted: de-duplicated the feature list to the issue's twelve; "fast in-site navigation" in the readers bullet; out-of-scope paragraph added mirroring the issue; header-comment update added to What Changes/Impact; CI claim scoped to link/anchor risk with an explicit re-verification line for 0.1.2; serializer claim rephrased to "deep-copies every setting it does not itself derive"; avatar URL carried verbatim and marked as fixed; pin/floor split stated per file; Impact label renamed to **Maintainer toolchain**; added theme requirements listed as their own ADDED line; kit claim softened to "no kit paths touched, so no kit release follows".
- Rejected: keeping "the rest of the configuration remains org-neutral" — the glossary scopes org-neutrality to identifiers and documents naming no organization; the sentence was dropped (the docs-sources bullet keeps the term where the existing spec already applies it).
- Deferred: Home's placement rule → specs phase (it falls under the delegated "final section grouping" decision; the delta must keep the all-seven-pages invariant); 0.1.2 re-verification steps → tasks phase; remote-avatar availability characteristics → design.

## Remaining Risks
- Verification evidence is 0.1.0-based; 0.1.2 (zensical-ui 0.0.43) could shift flag names or rendering — apply must re-run the strict build and rendered-HTML check on the new pin before merge.
- Home placement is interpretable; the spec delta must pin the full-navigation invariant explicitly so grouping stays a titled decision, not an accidental page drop.
- Branding depends on `avatars.githubusercontent.com` availability at read time (accepted by the issue, worth a design note).
