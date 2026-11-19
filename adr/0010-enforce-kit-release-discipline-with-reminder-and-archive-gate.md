# ADR-0010: Enforce kit release discipline with an advisory reminder and an archive gate

## Status

Accepted

## Date

2026-11-18

## Context and Problem Statement

ADR-0009 gave the kit a versioned release channel: a version bump merging to `main` cuts a release automatically, and the bump-in-the-same-change rule carries the discipline. But the rule is convention with two unenforced seams: a change can alter kit files and forget the bump — nothing surfaces the miss at review time — and a change could complete its lifecycle with kit changes that no published release contains. Enforcement must not fight the channels: kit files ship to every adopter (ADR-0001, channel 2), so enforcement living in kit-owned files would push hep-metadex's release discipline into **experiment repositories**, where no kit release is ever cut. And the review-time check must not block merges: the maintainer loop is small, a forgotten bump is cheap to fix, and a hard review-time gate buys no more enforcement than the archive phase already can.

## Considered Options

- Reminder plus archive gate: an advisory CI reminder catches a forgotten bump at review time (never blocking, never rendering a failing status); a repo-local gate script, wired into the archive phase through `openspec/config.yaml`'s archive guidance (ADR-0008's config-rules layer), refuses to archive a kit-touching change until a published release contains its changes — both, with the release workflow, reading the kit copy-list from one definition, the KIT-MANIFEST `paths:` block
- Reminder only (rejected — the review-time miss is caught, but the lifecycle seam stays open: a change could still archive with kit changes no release contains, and an advisory is ignorable by design)
- Merge-blocking required status checks (rejected — hard review-time gating adds merge friction while buying nothing the archive gate does not already guarantee; the archive phase is the honest place for hardness)
- Wiring the gate into the kit-owned `openspec-git-discipline` skill (rejected — kit-owned: the gate would ship to every adopter with no releases to consult, and the enforcement change would itself become kit-touching, self-dogfooding its own gate and contradicting the planned #9 dogfood)
- A CI check the archive phase consults (rejected — asynchronous and CI-dependent where a local **maintainer toolchain** script performs the identical check deterministically)

## Decision Outcome

Chosen option: "reminder plus archive gate", because the two seams have different costs: the forgotten bump is cheapest to fix at review time, where an advisory suffices — it must never block or visually fail — while the lifecycle seam is only enforceable at archive time, where the remedy is mechanical (bump the **kit version file**, merge, and the release cuts). Both mechanisms are repo-local maintainer automation: the reminder a `.github/` workflow (ADR-0008's host-automation layer), the gate a **maintainer toolchain** script (ADR-0006) run by the archive phase through config guidance — nothing ships in the kit, and no adopter sees enforcement it cannot use. Both mechanisms and the release workflow read the kit copy-list from one definition — the KIT-MANIFEST `paths:` block — so a copy-list change reaches every consumer by construction and the release bundle stays byte-identical.

### Consequences

- Good, because the forgotten bump surfaces at review time as a cheap advisory, and the archive gate guarantees no kit-touching change completes its lifecycle unreleased, printing a pasteable fix per diagnosed cause (bump for a forgotten bump; workflow re-run for a misfire — never a second bump, which would scope the release wrong).
- Good, because enforcement rides the layers ADR-0008 already routes — config rules, `.github/`, and the **maintainer toolchain** — and extends ADR-0009 read-side only: the manifest becomes the copy-list's normative home without changing the release contract.
- Bad, because the gate is process discipline, not mechanical prevention: an archive that skips the gate violates the spec'd process, and nothing but the process stops it.
- Bad, because the release workflow — the repository's most critical automation — is edited to derive its bundle list, concentrating release-channel risk inside an enforcement change (mitigated by bundle-equivalence verification).
- Follow-up: #9 (add-metadex-bootstrap-command) is the first kit-touching change under the mechanisms and dogfoods both end to end; promoting the reminder to a required check stays parked unless misses recur; the update command (#39) consumes the same single-sourced copy-list.
