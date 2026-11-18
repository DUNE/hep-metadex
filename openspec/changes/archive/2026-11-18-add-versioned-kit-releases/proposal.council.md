# Council Notes: proposal

## Author Summary
The author draft covered all eight issue-#34 deliverables and every rule under the template's four headings: one new capability (`kit-releases`), one modified (`adopter-onboarding`), the four delegated design decisions left open, house-style Impact bullets, and the dogfood sequenced as bump-on-merge plus post-merge dune-metadex re-install. It flagged two verification points (docs-site delta need, governance-docs ADR enumeration) and made the sequencing assumption that "cut v1.0.0 in this change" means "on merge."

## Reviewer Challenges
- **Glossary misuse:** "Change-time work" used for the kit-bump discipline in hep-metadex — the term's use-when is experiment-side development against shared specs (two occurrences).
- **Semver contradiction:** calling the version file and KIT-MANIFEST "MINOR-class" additions inside v1.0.0, which is an initial identity with no prior release to increment.
- **Unverified facts:** the `adr/` path and "zero-runtime" characterization were not among the evidence given to the author.
- **Checksum gap:** "checksum-verified" only holds for adopters if the documented manual path carries the SHA256SUMS check; nothing in the draft said so.
- **Dogfood overconfidence:** the workflow's first-ever run is triggered by its own introducing merge — stated as a certainty rather than an acceptance focus.
- **Unsupported addition:** "commands link to" the changelog in the out-of-scope rationale; only docs-page links are mandated by the issue.
- **Capability density:** ~six requirement areas packed into one `kit-releases` sentence.
- **Risks:** first-release bootstrap mechanics (trigger-on-introducing-merge, tag/release token permissions, bump-detection treating the version file's introduction as a bump); the changelog date-stamp knot (authored pre-merge, date known only at merge, workflow barred from backfilling by the never-commit rule); CLI-owned vs copy-list semantics (bundle membership vs install-time overwrite); the dune-metadex re-install being the first over-install of unstamped, possibly diverged files, post-merge and pre-#35; divergence-manifest row placement (adopter-onboarding vs kit-releases).

## Resolutions
- Accepted: removed both "Change-time work" uses; rephrased with the issue's own language (bump plus changelog entry in the same change, mirroring the CLI-pin discipline).
- Accepted: v1.0.0 is the baseline kit — version file and KIT-MANIFEST are part of the initial composition; MINOR governs post-1.0.0 additions.
- Verified and kept: `adr/` exists at the repository root (ADR-0001 through ADR-0008); "zero-runtime" comes from the project's own context configuration. The reviewer lacked session evidence for both.
- Accepted (trimmed): removed the "Org-neutral" claim about the kit — not verified kit-wide; noted as a design consideration instead (see Remaining Risks).
- Accepted: usage.md's release consumption now explicitly includes the manual SHA256SUMS verification step.
- Accepted: the dogfood bullet reframes first-release success as an explicit acceptance focus with a manual workflow re-run fallback, and tracks the dune-metadex re-install as the change's final task.
- Accepted: out-of-scope rationale trimmed to documentation-set links; command-side changelog consumption attributed to #39.
- Accepted: the `kit-releases` capability description now names its distinct requirement areas so the spec stage can make each independently testable.
- Placement decision: divergence-manifest rows stay under `adopter-onboarding` — its existing requirements already frame the validate.yml and ISSUE_TEMPLATE manifest entries; the spec stage may relocate the repo-local release-workflow row if the fit is better there.

## Remaining Risks
- First-release bootstrap: the workflow's first run fires on its own introducing merge; bump-detection must treat the version file's introduction as a bump; tag/release permissions must exist. Design and tasks must carry a first-release acceptance path (hence the manual re-run fallback in the proposal).
- Changelog date-stamp knot: the 1.0.0 section is authored pre-merge, the release date is known only at merge, and the workflow cannot backfill it (never commits on `main`) — the delegated date-stamping decision is constrained by a rule the proposal already states.
- CLI-owned vs copy-list: the bundle includes CLI-owned paths (a bootstrap needs the full kit) while an update must never overwrite them — design must define whether ownership classes govern bundle membership, install-time overwrite behavior, or both, without contradicting "bundle = exactly copy-list + version file + KIT-MANIFEST."
- Version-file org-neutrality: any release URL inside the shipped version file is a factual hosting citation (permitted to name the current organization, updated on a hosting move) — a design consideration surfaced during reconciliation, not an issue requirement.
- dune-metadex re-install is the first over-install of unstamped, possibly diverged kit files, occurring post-merge and before #35's gate exists — tracked as the change's final task rather than an automated gate.
