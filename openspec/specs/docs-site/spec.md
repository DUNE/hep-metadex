# Docs Site Specification

## Purpose

Defines the repository's **documentation site** — Zensical building `docs/` in place for HSF evaluators and adopter maintainers, the strict link-validation gate that CI enforces on every pull request and push, publishing to GitHub Pages from `main` only, and out-of-tree links rewritten to absolute GitHub URLs while the docs sources keep their relative, **org-neutral** links.

## Requirements

### Requirement: In-place site build
The repository SHALL build the **documentation site** from `docs/` in place: `zensical.toml` at the repository root configures Zensical with `docs_dir` pointing at `docs/`, explicit navigation, and a minimal theme, and Zensical SHALL be pinned as a dev dependency of the **maintainer toolchain** with the pin recorded in `uv.lock`.

#### Scenario: A maintainer builds the site from the repository root

```gherkin
Given the repository with zensical.toml pointing docs_dir at docs/
When a maintainer runs the Zensical build through the maintainer toolchain
Then the site builds from docs/ in place
And no docs page is moved, renamed, or deleted
```

#### Scenario: Zensical arrives pinned with the toolchain

```gherkin
Given the maintainer toolchain's uv project
When a maintainer syncs dependencies with uv
Then Zensical is installed as a dev dependency at the version pinned in uv.lock
```

### Requirement: Strict link validation gate
Every docs build in CI SHALL pass `zensical build --strict` with zero invalid internal links and zero invalid link anchors. The strict build SHALL run on every pull request and every push to `main`.

#### Scenario: A broken link fails the pull request build

```gherkin
Given a pull request whose docs changes introduce a link to a non-existent page or anchor
When continuous integration runs the strict docs build
Then the build fails and reports the invalid link or anchor
```

#### Scenario: A clean repository passes the strict build

```gherkin
Given the repository with every docs link and anchor valid
When continuous integration runs the strict docs build
Then the build succeeds
```

### Requirement: Publish to GitHub Pages on main
A push to `main` SHALL build the site in CI and publish it to GitHub Pages. Pull request builds SHALL NOT publish.

#### Scenario: A push to main publishes the site

```gherkin
Given the repository on main with GitHub Pages enabled to deploy via GitHub Actions
When a push lands on main
Then continuous integration builds the site with zensical build --strict
And the published site serves the pushed documentation
```

#### Scenario: A pull request never publishes

```gherkin
Given an open pull request changing docs
When its continuous integration runs
Then the strict docs build runs on the pull request
And nothing is published to GitHub Pages
```

### Requirement: Out-of-tree link resolution
Links from site pages to repository-root artifacts — README, CONTRIBUTING, LICENSE, `.github/`, `glossary/`, `adr/`, and other root targets such as `openspec/` — SHALL resolve on the published site as absolute GitHub URLs produced by a build-time rewrite of the docs sources' relative links, driven by a single repo-URL setting in `zensical.toml`. The docs sources SHALL keep their relative links.

#### Scenario: An out-of-tree link resolves on the published site

```gherkin
Given a docs page linking relatively to a repository-root artifact
When the site build runs
Then the published page links to that artifact at an absolute GitHub URL derived from the repo-URL setting
And the docs source still carries its relative link
```

#### Scenario: A hosting move needs no docs-source edits

```gherkin
Given the published site and the docs sources with their relative links
When the repository transfers to a different GitHub organization
Then updating the repo-URL setting and site_url in zensical.toml repoints every out-of-tree link
And no docs source needs editing
```

### Requirement: Site landing page and full navigation
The site SHALL provide `docs/index.md` as the audience-facing landing page for HSF evaluators and adopter maintainers, and explicit navigation in `zensical.toml` SHALL cover the landing page and every existing docs page. Navigation titles SHALL live in configuration, so no existing docs page requires front-matter.

#### Scenario: An evaluator lands on the site

```gherkin
Given the published documentation site
When an evaluator opens the site root
Then the landing page presents what hep-metadex is and where to start
And the navigation reaches the landing page and every existing docs page
```

#### Scenario: No docs page is dropped from navigation

```gherkin
Given the six pre-existing docs pages and the new docs/index.md
When the site build completes
Then each of the seven pages appears in the explicit navigation
```

### Requirement: Documentation paths and scaffolding untouched
The spec-required paths `docs/setup.md`, `docs/usage.md`, `docs/governance.md`, and `docs/hsf-affiliation.md`, and the copy-listed `docs/intent-prompt-guidelines.md`, SHALL remain at their current repository paths, and the change MUST NOT modify any component of the **workflow scaffolding** adopters copy from the store.

#### Scenario: Spec-required paths stay in place

```gherkin
Given the repository as delivered by this change
When the docs tree and the adopter copy-list are examined
Then the spec-required docs files and docs/intent-prompt-guidelines.md are found at their current paths
And nothing on the scaffolding copy-list has changed
```
