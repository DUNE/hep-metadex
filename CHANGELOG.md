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

## [1.0.0] - 2026-11-12

### Added
- Versioned kit releases: the kit publishes as a semantically versioned, checksum-verified bundle per release, with `SHA256SUMS` and the required OpenSpec CLI version declared (#34).
- `.metadex-kit`: the kit version file — source-side release trigger, shipped verbatim in the bundle as each install's provenance stamp (#34).
- `KIT-MANIFEST.yaml`: the kit's per-path bill of materials with ownership classes (cli-owned, kit-owned, merge-guidance, never-touch) (#34).
- A repo-local release workflow that tags `vX.Y.Z` on a version bump, assembles the kit bundle, and sources each GitHub release body from this changelog (#34).
- Kit release consumption documentation with manual checksum verification (#34).

[1.0.0]: https://github.com/DUNE/hep-metadex/releases/tag/v1.0.0
