# Changelog

All notable changes to the hep-metadex workflow scaffolding (the kit) are
documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and the kit adheres to [Semantic
Versioning](https://semver.org/spec/v2.0.0.html); every entry references its
change issue. The version number speaks about the kit only — changes
confined to specs, changes, non-kit docs, or repo-local tooling never drive
a release
([ADR-0009](adr/0009-distribute-workflow-scaffolding-as-versioned-kit-releases.md)).
There is no Unreleased section: a kit-altering change bumps the version and
lands its changelog entry in the same change, and the release cuts when
that change merges to `main`.

## [1.1.0] - 2026-11-20

### Added
- The `/hep-metadex-bootstrap` command — the kit's first kit-owned command, automating the documented agent-assisted bootstrap prompt end to end: prerequisites check against the release's declared CLI pin, `openspec init`, checksum-verified kit install from a versioned release (latest by default, pin-able), host-conditional GitHub files, config authoring with the store reference, doctor to green (#9).
- The bootstrap one-liner: each release now publishes the command file as a standalone, checksummed asset (`hep-metadex-bootstrap.md`) covered by `SHA256SUMS`, fetched pre-scaffolding from `releases/latest` and handed to the agent (#9).
- A per-file `KIT-MANIFEST.yaml` entry marking the command kit-owned inside the CLI-owned commands directory, with most-specific-matching-path precedence; bundle assembly derives from the manifest and drops entries nested inside another entry (#9).

## [1.0.1] - 2026-11-19

### Fixed
- Unified the `actions/checkout` pin at `@v7` across the repository's workflows: the kit-shipped spec-validation workflow (`validate.yml`) moves `@v4` → `@v7`, matching `docs.yml` and `kit-reminder.yml` — the same coordinated move the repo-local `release.yml` carries source-side (#44).

## [1.0.0] - 2026-11-12

### Added
- Versioned kit releases: the kit publishes as a semantically versioned, checksum-verified bundle per release, with `SHA256SUMS` and the required OpenSpec CLI version declared (#34).
- `.metadex-kit`: the kit version file — source-side release trigger, shipped verbatim in the bundle as each install's provenance stamp (#34).
- `KIT-MANIFEST.yaml`: the kit's per-path bill of materials with ownership classes (cli-owned, kit-owned, merge-guidance, never-touch) (#34).
- A repo-local release workflow that tags `vX.Y.Z` on a version bump, assembles the kit bundle, and sources each GitHub release body from this changelog (#34).
- Kit release consumption documentation with manual checksum verification (#34).

[1.0.0]: https://github.com/DUNE/hep-metadex/releases/tag/v1.0.0
[1.0.1]: https://github.com/DUNE/hep-metadex/releases/tag/v1.0.1
[1.1.0]: https://github.com/DUNE/hep-metadex/releases/tag/v1.1.0
