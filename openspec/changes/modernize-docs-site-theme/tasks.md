> Verification approach for this change (issue #47 deliverables and out-of-scope;
> ADR-0007's follow-up allocating acceptance-suite wiring to #20; ADR-0013;
> design D9, resolved): acceptance-suite scaffolding stays deferred to #20 —
> no `acceptance-tests/` exists to extend, and this change is configuration
> plus a regression test. The delta scenarios verify at the CI boundary, the
> external observer here: the strict docs build (`zensical build --strict`
> over the staged tree) gates every pull request and push, and the built
> `site/` output supplies the rendered-HTML marker checks (design D9). Spec
> validation gates on `valid: true` (non-strict per ADR-0003 — fenced Gherkin
> is the single scenario source). Implementation and test edits go through
> the senior-dev subagent in small batches, per the project context;
> senior-qa is not engaged — there is no acceptance wiring in this change.
> `tasks.md` is zone-neutral; every group below is code zone (nothing under
> `openspec/` is edited at apply time beyond these checkboxes).

## 1. Dependency bump — everything downstream verifies on the new pin (code zone)

- [x] 1.1 Raise the Zensical dev dependency to `zensical>=0.1.2` and re-lock: confirm `uv.lock` records zensical 0.1.2 with zensical-ui 0.0.43 riding along, and `uv sync --locked` is green on the pinned Python 3.14 (design D8; spec: `docs-site`, "In-place site build") — *apply note: zensical 0.1.2 pins zensical-ui==0.0.42 exactly (0.0.43 pairs with no released zensical); 0.1.2/0.0.42 accepted with user approval — the binding rules name only the ≥ 0.1.2 floor and the lock*
- [x] 1.2 Re-verify the flag vocabulary on the new pin before any config work: confirm the twelve feature flags and the `palette`/`features`/`favicon`/`logo` keys still exist in the installed zensical-ui 0.0.43 templates (design D4's mapping); if any drifted, stop and reconcile design D4 before proceeding (design D9, Risks) — *apply note: verified against the installed zensical-ui 0.0.42 — all twelve flags, all four theme keys, and the brightness-auto/-7/-4 toggle icons are present*
- [x] 1.3 Commit as `build(docs): raise zensical to 0.1.2 (#47)` — `pyproject.toml` plus `uv.lock`; code zone, nothing under `openspec/` uncommitted alongside

## 2. Serializer round-trip guard — red first (code zone)

- [x] 2.1 Via the senior-dev subagent: add a failing round-trip case to `tools/docs_site_test.py` — a committed-style config carrying a nested `[project.theme]` table (palette list of inline dicts with `media`/`scheme`/`primary`/`accent`/`toggle`, features string list, `favicon`/`logo` URLs) and a sectioned `nav` (dict-with-list entries) must survive `derive_config_text` → `tomllib.load` with every setting identical except the derived `docs_dir` (design D9; red before green) — *apply note: this is a regression guard for existing behavior; design D9 predicted (correctly) that it passes against the current serializer on first run*
- [x] 2.2 Confirm the existing serializer passes the new case unmodified; if it fails, fix the serializer — not the test — and record the correction against design D1's round-trip claim (design D9) — *apply note: `tools/docs_site.py` untouched; `docs_site_test.py` 23/23 green; one pre-existing, unrelated failure in `kit_release_gate_test.py` reproduces at HEAD (manifest/test drift from #9) — out of scope, flagged for a follow-up issue*
- [x] 2.3 Commit as `test(docs): guard theme and sectioned-nav round-trip through the staging config (#47)`

## 3. Theme, branding, and sectioned navigation configuration (code zone)

- [ ] 3.1 Via the senior-dev subagent: add `[project.theme]` to `zensical.toml` — the three-option palette (auto option with `media = "(prefers-color-scheme)"` and the `material/brightness-auto` icon; light option `scheme = "default"` with `material/brightness-7`; dark option `scheme = "slate"` with `material/brightness-4`; primary `indigo`, accent `light-blue` on both explicit schemes), the features list enabling exactly the twelve flags per design D4's mapping, and `favicon` + `logo` both set to `https://avatars.githubusercontent.com/u/7131646?s=200&v=4` (design D2/D3/D4/D7; spec: `docs-site`, "Three-way color palette toggle", "Site branding from the DUNE organization avatar", "Reader-experience theme features")
- [ ] 3.2 Via the senior-dev subagent: replace the flat `nav` with Home as the unsectioned top-level entry followed by the three audience sections — Getting Started (Setup, Usage), Governance (Governance, HSF Affiliation), Maintainers (Maintainer Guide, Intent Prompt Guidelines) — as dict-with-list entries with every title in configuration and no page gaining front-matter (design D5; spec: `docs-site`, "Site landing page and full navigation")
- [ ] 3.3 Update `zensical.toml`'s header comment: a hosting move edits `repo_url`, `site_url`, and the avatar URL (design D7; spec: `docs-site`, "Out-of-tree link resolution", hosting-move scenario)
- [ ] 3.4 Verify locally: `uv run tools/docs_site.py build` exits green under strict mode with zero invalid links and zero invalid anchors; the derived `.site-src.toml` shows the theme table and sectioned nav passed through untouched; `git status` shows no docs-source edits (spec: `docs-site`, "Reader-experience theme features", "In-place site build")
- [ ] 3.5 Built-HTML marker check on the new pin: `site/` output carries the palette radio inputs (`data-md-color-media`/`data-md-color-scheme`), the instant-navigation script, favicon and logo tags pointing at the avatar URL, the sectioned sidebar with Home plus the three sections, and the breadcrumb, footer, back-to-top, reading-progress, and TOC-follow markers (design D9)
- [ ] 3.6 Commit as `docs(site): configure the theme, palette toggle, branding, and sectioned navigation (#47)` — `zensical.toml` only

## 4. Verification and completion

- [ ] 4.1 After the planning PR merges to `main`, cut the apply branch per the apply workflow, push, and open the implementation PR referencing issue #47; confirm the strict docs gate runs green on the PR and that nothing is published from it (spec: `docs-site`, "A pull request never publishes")
- [ ] 4.2 Run `openspec validate modernize-docs-site-theme --type change` and confirm `valid: true` (non-strict per ADR-0003; fenced scenarios are the single source — the CLI's `--strict` step-detection warnings are the known issue ADR-0003 records)
- [ ] 4.3 Sweep the deliverables against issue #47's rules: the three-way palette toggle persists across pages; the DUNE org avatar serves as favicon and header logo and appears in the hosting-move comment; all twelve theme features are enabled; the sectioned navigation covers all seven pages with titles in configuration and no front-matter; the strict build passes through the staging wrapper; `git diff` shows zero changes under `docs/`; no kit path in KIT-MANIFEST.yaml is touched and the kit reminder stays green with no `.metadex-kit` bump (spec: `docs-site`, "Documentation paths and scaffolding untouched")
- [ ] 4.4 Merge the implementation PR; confirm the next Pages deploy from `main` serves the modernized site — the palette toggle cycles system → light → dark and persists across pages, in-site links navigate without full page reloads, sections and breadcrumbs and footer and back-to-top render, and the DUNE avatar brands the tab and header (spec: `docs-site`, added requirements)
- [ ] 4.5 Confirm the docs-source invariant on the merged diff: no file under `docs/` changed for the site's sake (ADR-0007; spec: `docs-site`, "Out-of-tree link resolution")
