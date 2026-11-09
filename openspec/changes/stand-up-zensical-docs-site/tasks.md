> Verification approach for this change (issue #22 out-of-scope; ADR-0006's
> acceptance-`stack:` deferral; ADR-0007; design, Open Questions, resolved):
> acceptance-suite scaffolding stays deferred to #20 — no runtime application
> exists for a runner to boot, and the issue scopes acceptance tests out. The
> delta scenarios verify at the CI boundary, which is the external observer
> here: the strict docs build (`zensical build --strict` over the staged
> tree) gates every pull request and push, and the published site is the
> walkable artifact. Spec validation gates on `valid: true` (non-strict per
> ADR-0003 — fenced Gherkin is the single scenario source). Implementation of
> `tools/docs_site.py` goes through the senior-dev subagent in a small batch,
> per the project context; senior-qa is not engaged — there is no acceptance
> wiring in this change. `tasks.md` is zone-neutral; every group below is
> code zone (nothing under `openspec/` is edited at apply time).

## 1. Toolchain dependency and feasibility spike (code zone)

- [x] 1.1 Run `uv add --dev zensical` — Zensical lands in the `[dependency-groups]` ADR-0006 reserved; confirm it resolves on the pinned Python 3.14 and `uv.lock` updates (design D2 spike, ADR-0007)
- [x] 1.2 Spike the staging approach before any other build work: stage one docs page into a scratch `.site-src/` with one rewritten `../` link, write the derived config (settings loaded from a draft `zensical.toml`, `docs_dir` swapped), and confirm `uv run zensical build --strict --config-file <derived>` is green; if red, stop and adopt the design's fallback (a committed build config pointing at the staging tree) only after consciously amending the change's `docs_dir` deliverable wording (design D2, Risks)
- [x] 1.3 Commit the dependency pin as `build(docs): pin zensical as a dev dependency (#22)` — `pyproject.toml` plus `uv.lock`; code zone: nothing under `openspec/` uncommitted alongside

## 2. Site build machinery (code zone)

- [x] 2.1 Create `tools/docs_site.py` via the senior-dev subagent — stdlib-only, with a `build` subcommand (load the committed `zensical.toml` with `tomllib`, stage `docs/` into `.site-src/` rewriting every `../`-escaping relative link to `{repo_url}/blob/main/{path}` with `#anchor` fragments preserved, uniformly for all out-of-tree targets, write the derived config with `docs_dir` swapped, invoke `zensical build --strict --config-file`) and a `serve` subcommand (stage, then preview the staged tree) (design D2/D3, ADR-0007)
- [x] 2.2 Extend `.gitignore` with `site/` and `.site-src/` (design D2)
- [x] 2.3 Create `zensical.toml` — `site_name`, `site_url` (the exact Pages URL), `repo_url` as the single repo-URL setting, `docs_dir = "docs"`, `site_dir`, explicit `nav` with config-side titles for all seven pages (Home, Setup, Usage, Governance, HSF Affiliation, Maintainer Guide, Intent Prompt Guidelines), minimal built-in theme, `strict = true` (design D1/D3/D5)
- [x] 2.4 Create `docs/index.md` — the audience-facing landing page per design D5: what hep-metadex is, paths for adopters and evaluators, the GitHub repository link, using the same relative links as every other page
- [x] 2.5 Verify locally: `uv run tools/docs_site.py build` exits green under strict mode; all seven pages appear in navigation; the staged tree shows rewritten out-of-tree links while `git status` shows no docs-source edits beyond `docs/index.md`
- [x] 2.6 Commit as `feat(docs): add the staging build entry point for the docs site (#22)` (`tools/docs_site.py` + `.gitignore`), `docs(site): add zensical.toml with in-place docs_dir, navigation, and theme (#22)`, and `docs(site): add the site landing page (#22)`

## 3. CI publishing workflow (code zone)

- [ ] 3.1 Create `.github/workflows/docs.yml` — triggers on `pull_request` and `push` to `main` (plus `workflow_dispatch` for manual republish from `main`); both paths check out, install uv via `astral-sh/setup-uv` with an explicitly pinned version (closing ADR-0006's deferred pinning question), run `uv sync --locked`, then `uv run tools/docs_site.py build` (the strict gate); the `main` path additionally uploads `site/` via `actions/upload-pages-artifact` and deploys via `actions/deploy-pages` under `permissions: contents: read, pages: write, id-token: write`, the `github-pages` environment, and a deploy concurrency group; no CI caching (design D4); commit as `ci(docs): add the uv-native build-and-publish workflow (#22)`
- [ ] 3.2 Operational, no commit: a repository admin enables GitHub Pages with the GitHub Actions publishing source — the one-time precondition; the publish requirement is untestable until it is done (design D4)

## 4. Governance, bookkeeping, and glossary (code zone)

- [ ] 4.1 Update the Documentation row in `docs/hsf-affiliation.md` — cite the live site URL alongside the README and `docs/` citations, as a factual hosting citation per the `governance-docs` delta (design D6); commit as `docs(governance): cite the live site in the HSF checklist documentation row (#22)`
- [ ] 4.2 Add the divergence-manifest row in `docs/maintainer.md` — `zensical.toml`, `tools/docs_site.py`, `.github/workflows/docs.yml` as repo-local site tooling the template never ships, mirroring the ADR-0006 toolchain row's sync semantics — and one README repository-map row for the same files (design D6, the #21 precedent); commit as `docs(maintainer): record the docs-site tooling divergence and map row (#22)`
- [ ] 4.3 Add the **documentation site** term to `glossary/technical.md` with use-when/avoid guidance per the proposal's glossary companion; commit as `docs(glossary): add the documentation site term (#22)`

## 5. Verification and completion

- [ ] 5.1 Push the apply branch (cut from `main` after the planning merge) and open the implementation PR referencing issue #22; confirm the strict docs gate runs green on the PR and that nothing is published from it (spec: `docs-site`, "A pull request never publishes")
- [ ] 5.2 Run `openspec validate stand-up-zensical-docs-site --type change` and confirm `valid: true` (non-strict per ADR-0003; fenced scenarios are the single source — the CLI 1.16.0 `--strict` flag is the known issue ADR-0003 records)
- [ ] 5.3 Sweep the deliverables against issue #22's rules: a push to `main` builds in CI and publishes to GitHub Pages; the build passes `zensical build --strict` with zero invalid internal links or anchors; `docs/setup.md`, `docs/usage.md`, `docs/governance.md`, `docs/hsf-affiliation.md`, and `docs/intent-prompt-guidelines.md` remain at their current repo paths; the scaffolding copy-list (`.agents/skills/`, `.opencode/`, `openspec/schemas/intent-driven/`, `AGENTS.md`, `.github/workflows/validate.yml`) is untouched; no acceptance-test scaffolding was added (#20 stays open)
- [ ] 5.4 Merge the implementation PR; confirm the first Pages deploy serves the site at the Pages URL with all seven pages navigable, out-of-tree links resolving on GitHub, and anchors working under the project subpath
- [ ] 5.5 Confirm the docs-source invariant: the merged `git diff` shows no docs-source link edits beyond the new `docs/index.md` and the hsf-affiliation Documentation row — every other `../` link is untouched (spec: `docs-site`, "Out-of-tree link resolution")
