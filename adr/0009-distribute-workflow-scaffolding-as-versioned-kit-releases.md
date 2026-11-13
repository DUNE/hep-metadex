# ADR-0009: Distribute the workflow scaffolding as versioned kit releases

## Status

Accepted

## Date

2026-11-12

## Context and Problem Statement

ADR-0001 established two channels: specs flow read-only through the **OpenSpec Store**; the **workflow scaffolding** replicates by template install with hep-metadex as its source. But the kit has no version identity: adopters copy from an unpinned checkout, installs leave no provenance record in the **experiment repository**, and the documented update path ("re-run the scaffolding install") cannot say what changed since the last install. The tension underneath is structural — the kit wants pinning (stability; drift is ADR-0001's named bad consequence) while channel 1's registered checkout must float on `main` (spec freshness; **write-back** assumes current specs), and both channels flow from the same clone: pinning the clone freezes the specs, and leaving it floating leaves the kit unpinned.

## Considered Options

- Semantically versioned, checksum-verified kit release bundles, decoupled from the store checkout
- A pinned store checkout cloned at a release tag (rejected — pins channel 1's specs together with the kit, breaking spec freshness and write-back currency)
- The status quo: unpinned checkout copies with no provenance (rejected — drift stays invisible, installs are not reproducible, updates are not diffable)
- Release-please-style automated release PRs (rejected — they generate issue-less commits that fight the change lifecycle and the git discipline)

## Decision Outcome

Chosen option: "versioned kit release bundles", because the two channels have opposite versioning natures — continuous freshness for specs, discrete stability for the kit — and only a kit-only release channel gives each channel the discipline that fits it. Versioning is kit-only: the number speaks about the kit copy-list, never about spec content. A root version file (`.metadex-kit`) is the source-side release trigger and the shipped provenance stamp in one, so every install lands pre-stamped. A version-bump merge to `main` cuts the release automatically — tag `vX.Y.Z`, a bundle of exactly the copy-list plus the version file and a machine-readable KIT-MANIFEST, SHA256SUMS, a release body extracted from the changelog section for that version (failing when it is missing), and the required OpenSpec CLI version declared — with the workflow creating tags and releases only, never commits on `main`. Channel 1 is untouched: the registered checkout keeps floating, and store registration, spec consumption, and the doctor fix are unchanged.

### Consequences

- Good, because every install carries provenance, bootstraps are reproducible against a pinned release, and updates become diffable between stamped versions.
- Good, because kit pinning and spec freshness stop fighting — each channel gets the versioning semantics that match its nature, per the kit-pin/spec-freshness decoupling.
- Bad, because the release workflow's first-ever run is triggered by the merge that introduces it — a first-release acceptance focus with a manual re-run fallback.
- Bad, because the changelog heading's date is authored before merge while the release date is only known at merge; the GitHub release timestamp is authoritative and any drift is cosmetic.
- Follow-up: issue #35 mechanizes the bump discipline (a CI reminder plus an archive gate); #9 and #39 consume the release channel; #36 (signing), #37 (spec versioning), and #38 (installer) extend it on their triggers.
