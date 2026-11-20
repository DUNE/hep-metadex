# Council Notes: proposal

## Author Summary
The author draft framed the change around the friction asymmetry — a proven but copy-paste agent-assisted bootstrap versus a born-version-aware command now that the Kit release channel (#34) and its discipline (#35) exist — and structured the Capabilities contract as one new capability (`bootstrap-command`, with eight requirement areas) plus two modified capabilities (`kit-releases`: ownership-class granularity and the checksummed command asset; `adopter-onboarding`: command as primary path, prompt as fallback and specification). It encoded all three grill-me resolutions: the command-as-release-asset one-liner, the per-file kit-owned manifest entry with most-specific-path precedence, and the `bootstrap-command` capability name.

## Reviewer Challenges
- The claim "bundle derivation is unchanged in effect" was called a correctness error: the reviewer read the cli-owned class as excluding the directory's files from the bundle, making the per-file entry the thing that adds the command to the bundle.
- Citing `opsx-update.md` as "the existing kit command shape" was called false and self-contradictory (those files are CLI-delivered, not kit-owned).
- Three parts of the issue's "end to end" automation had no requirement area: `openspec init`, the AGENTS.md merge-guidance and kit-file placement behavior, and the greenfield/brownfield MUST (visible only in the config-authoring clause).
- Two version-skew risks were unnamed: fetched-command vs pinned-kit skew, and the documented prompt's hand-pinned CLI (1.16.0) vs the command's release-declared pin.
- Advisory: unverifiable claims (dune-metadex dogfood, the #7 quote, the README pointer); divergence-manifest scope for the release-workflow row; "no kit-release-discipline change needed" called an assumption; `.metadex-kit` missing from the Impact file list for the version bump; attribution of the usage.md ownership bullet; bolding consistency; dropping how-not-what layout detail; a specification-fidelity requirement area.

## Resolutions
- Accepted: reworded the bundle claim precisely (see the rejected factual claim below for the substance) — the final states the command ships via the directory entry, the per-file entry exists for ownership semantics, and defers duplicate-member handling to design.
- Accepted: the command is now framed as "the first kit-owned command" following the shape of the CLI-delivered files in the directory.
- Accepted: added the Initialization requirement area, folded kit-file placement (AGENTS.md merge-guidance, version file as arriving stamp) into Versioned install, and made greenfield/brownfield a cross-cutting property of the capability.
- Accepted: named both version-skew risks — the fetched-command-vs-pinned-kit behavior is a Deferred item and a #39 input; the prompt-pin vs release-pin divergence is an Impact bullet ("Sanctioned divergence").
- Accepted: `.metadex-kit` added to the Impact file list; the usage.md ownership bullet attributed to `kit-releases`' release-consumption documentation requirement; consistent bolding; dropped the frontmatter/section-layout detail (kept the zero-runtime artifact-type claim); added the Specification fidelity requirement area (the issue's own MUST, made testable).
- Rejected: the reviewer's bundle-membership mechanics — the release workflow's `tar` includes every `paths:` entry regardless of ownership class (the class governs the refresh route), so the cli-owned directory entry does carry the command file into the bundle; verified against `release.yml`.
- Rejected: "no kit-release-discipline change needed" as an assumption — verified against the spec: its requirements define kit paths generically as "the paths the KIT-MANIFEST.yaml paths: block lists" and its Single-source requirement explicitly covers "a later change adding a path" reaching all three consumers.
- Rejected: the advisory claim that the dune-metadex dogfood, the #7 "proven steps" quote, and the README quick-start pointer are unverifiable — all three verified in `docs/setup.md`, the #7 archive design, and the README.
- Rejected: trimming the release-workflow divergence row as scope creep — the manifest already tracks the release workflow as a row, and its description becomes inaccurate once the asset publishes; the final updates the existing row rather than adding a second.
- Rejected: dropping the `metadex-*` namespace rationale and the PR-merge boilerplate — the rationale is issue-sourced (Provenance section), and the PR-merge sentence is the #34 proposal's house style.

## Remaining Risks
- The duplicate-member question (per-file entry nested under a directory entry in bundle assembly) is real but deferred to design with the single-source copy-list contract named as the constraint.
- Whether the one-liner itself verifies the fetched command file's checksum is unspecified at proposal level — the asset is SHA256SUMS-covered but the fetch path is not; deferred toward design alongside the #36 signing follow-on.
- The reviewer's challenge 11 concern (specification fidelity split across two capabilities) is resolved by giving each side a home — docs framing in `adopter-onboarding`, command fidelity in `bootstrap-command` — but the specs stage must keep the two deltas from double-speccing the same scenario.
