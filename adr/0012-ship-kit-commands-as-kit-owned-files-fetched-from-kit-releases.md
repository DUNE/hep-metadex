# ADR-0012: Ship kit commands as kit-owned files fetched from kit releases

## Status

Accepted

## Date

2026-11-19

## Context and Problem Statement

ADR-0008 routes procedure automation to the commands layer and names the bootstrap command (#9) as that rule's first application; ADR-0009 gives the **kit** a versioned release channel and a KIT-MANIFEST whose ownership classes map whole paths — and `.opencode/commands/` is cli-owned: "refreshed through the OpenSpec CLI, never overwritten by a kit copy". Two problems follow. First, a kit command has no honest ownership home: shipping it inside the cli-owned directory leaves the machine-readable manifest wrong for the update path (#39 builds its reconciliation on those classes), while relocating it outside `.opencode/commands/` takes it off the harness's command path and gives one file two homes. Second, the bootstrap chicken-and-egg: a fresh **experiment repository** has no scaffolding, so the command that installs the scaffolding cannot itself arrive by scaffolding install — and fetching it from a floating main-branch URL would defeat the pinning nature ADR-0009 gave the kit.

## Considered Options

- Kit-owned command files inside the commands directory under a `hep-metadex-*` namespace, expressed as per-file KIT-MANIFEST entries with most-specific-matching-path precedence; each kit release additionally publishes its command files as standalone checksummed assets, fetched pre-scaffolding by a documented one-liner
- Keep the manifest unchanged and record the exception in the maintainer guide only (rejected — the manifest is the single ownership source #39 consumes; ownership must be resolvable by tools, not prose exceptions)
- Relocate kit commands to a kit-owned directory, copied into `.opencode/commands/` at install time (rejected — an install-time write into a cli-owned directory that `openspec update` could later clobber, and two homes for one file)
- Publish the command from a floating main-branch URL instead of the releases (rejected — it floats like the store checkout, unversioned and unchecksummed, exactly what ADR-0009 moved the kit away from)
- Defer delivery to the update command (#39) and installer (#38) (rejected — the bootstrap friction is now, and the releases-first progression exists precisely so this command is born version-aware rather than retrofitted)

## Decision Outcome

Chosen option: "kit-owned, release-fetched command files", because the commands layer is where ADR-0008 already routes procedure automation and ownership — not location — is what the manifest must express: a per-file entry for `.opencode/commands/hep-metadex-bootstrap.md` (kit-owned) nested inside the cli-owned directory entry lets the most specific matching path win, so the kit owns and refreshes its `hep-metadex-*` command files while CLI-delivered `opsx-*` files stay cli-owned, and bundle membership flows through the covering directory entry unchanged — the manifest gains granularity, not a second source. The release channel extends read-side only, inside its existing discipline: each kit release publishes the kit's command files as standalone assets derived from the same source files the bundle carries and covered by the same SHA256SUMS, so a documented one-liner fetches the bootstrap command from `releases/latest` into an uninitialized repository — the chicken-and-egg resolved inside the kit's pinning and checksum contract, with no new tooling on the adopter's machine.

### Consequences

- Good, because the kit gains a command-delivery pattern that survives #39: the update path reconciles by the manifest's per-file ownership, and future kit commands follow the `hep-metadex-*` namespace by construction.
- Good, because what the one-liner fetches is the released artifact — the same bytes the bundle carries, checksum-covered — not a floating checkout copy.
- Bad, because one directory now carries two ownership classes: the most-specific-path precedence must be stated on every surface the classes live on (the manifest header, usage.md's ownership guidance, the maintainer guide) and honored by #39's reconciliation.
- Bad, because the one-liner's fetch is unverified at fetch time — the command's install step re-fetches and verifies the assets it consumes; signing the fetch path stays #36's scope.
- Bad, because a fetched command file can be newer than the kit version an adopter pins — a usually-cosmetic skew the command warns about and records in its report, and an explicit input #39 must reconcile.
- Follow-up: #39 consumes the per-file precedence as its reconciliation contract and reuses the asset-plus-namespace pattern for its own command; #36 may sign the fetched asset; #38's agent-free installer remains a separate, independent follow-on.
