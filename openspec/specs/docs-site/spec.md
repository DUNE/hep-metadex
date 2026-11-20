# Docs Site Specification

## Purpose

Defines the repository's **documentation site** — Zensical building `docs/` in place for HSF evaluators and adopter maintainers, the strict link-validation gate that CI enforces on every pull request and push, publishing to GitHub Pages from `main` only, and out-of-tree links rewritten to absolute GitHub URLs while the docs sources keep their relative, **org-neutral** links.

## Requirements

### Requirement: In-place site build
The repository SHALL build the **documentation site** from `docs/` in place: `zensical.toml` at the repository root configures Zensical with `docs_dir` pointing at `docs/`, explicit sectioned navigation, and a `[project.theme]` section carrying the site's theme settings, and Zensical SHALL be a dev dependency of the **maintainer toolchain** with a version floor of 0.1.2 in `pyproject.toml` and the resolved pin recorded in `uv.lock`.

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
Then Zensical is installed as a dev dependency at the version recorded in uv.lock
And the installed version is at least 0.1.2
```

### Requirement: Three-way color palette toggle
The site SHALL offer a three-way color palette toggle — the system preference (`prefers-color-scheme`), light, and dark — and SHALL render every page in the reader's chosen palette, persisting that choice across pages.

#### Scenario: A reader follows the system color scheme

```gherkin
Given a reader whose system requests a dark color scheme
When the reader opens any page of the site
Then the page renders in the dark palette
```

#### Scenario: A reader overrides the system preference

```gherkin
Given a reader whose system requests a dark color scheme
When the reader switches the palette toggle to light
Then the page renders in the light palette
```

#### Scenario: The reader's choice persists across pages

```gherkin
Given a reader who has chosen the dark palette
When the reader opens another page of the site
Then that page renders in the dark palette
```

### Requirement: Site branding from the DUNE organization avatar
The site SHALL use the DUNE organization avatar `https://avatars.githubusercontent.com/u/7131646?s=200&v=4` as both its favicon and its header logo, referenced by that URL in `zensical.toml` rather than vendored into the repository.

#### Scenario: A reader sees the project's branding

```gherkin
Given the published site
When a reader opens any page
Then the browser tab shows the DUNE organization avatar as the favicon
And the header shows the same avatar as the logo
```

#### Scenario: The branding moves with the configuration

```gherkin
Given the site branded through the avatar URL in zensical.toml
When the avatar URL setting is changed
Then the favicon and logo follow the new URL
And no branding image file is added to the repository
```

### Requirement: Reader-experience theme features
The site's theme SHALL enable the reader-experience features: navigation footer (previous/next), instant navigation, instant prefetching, reading-progress indicator, automatic previews, anchor tracking, navigation sections, navigation-path breadcrumbs, navigation expansion, navigation pruning, TOC anchor following, and the back-to-top button.

#### Scenario: Every feature survives the strict build

```gherkin
Given zensical.toml with [project.theme] enabling every listed feature
When the site is built through the staging wrapper with zensical build --strict
Then the build succeeds with zero invalid links and zero invalid anchors
And every feature's component renders in the built output
```

#### Scenario: A reader navigates without full page loads

```gherkin
Given a reader viewing any page of the built site
When the reader follows an in-site link
Then the destination page renders without a full page reload
And the link was prefetched before the reader followed it
```

#### Scenario: A reader keeps their bearings while reading

```gherkin
Given a reader viewing a page within a navigation section
When the reader scrolls through the page
Then the reading-progress indicator tracks their position
And the table of contents follows the current anchor
And navigation-path breadcrumbs show the page's position
And previous and next links offer the adjacent pages
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
Then updating repo_url, site_url, and the avatar URL in zensical.toml repoints every out-of-tree link and the site's branding
And no docs source needs editing
```

### Requirement: Site landing page and full navigation
The site SHALL provide `docs/index.md` as the audience-facing landing page for HSF evaluators and adopter maintainers, and explicit navigation in `zensical.toml` SHALL organize the landing page and every existing docs page into audience-oriented sections. All section and page titles SHALL live in configuration, so no existing docs page requires front-matter.

#### Scenario: An evaluator lands on the site

```gherkin
Given the published documentation site
When an evaluator opens the site root
Then the landing page presents what hep-metadex is and where to start
And the navigation reaches the landing page and every existing docs page
```

#### Scenario: Navigation groups the pages by audience

```gherkin
Given the six pre-existing docs pages and docs/index.md
When the site build completes
Then the navigation presents audience-oriented sections grouping the pages
And the landing page stays reachable as a top-level navigation entry
```

#### Scenario: No docs page is dropped from navigation

```gherkin
Given the six pre-existing docs pages and docs/index.md
When the site build completes
Then each of the seven pages appears in the sectioned navigation
```

#### Scenario: Navigation titles stay in configuration

```gherkin
Given the sectioned navigation defined in zensical.toml
When the docs sources are examined after the build
Then every section and page title in the navigation comes from configuration
And no docs page gains front-matter for navigation
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
