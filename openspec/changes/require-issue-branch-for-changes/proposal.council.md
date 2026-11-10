# Council Notes: proposal.md

## Author Summary
The author draft framed the change as codifying existing practice: practice and `docs/usage.md` already follow the issue-number-first slug, so the amendment aligns the `openspec-git-discipline` skill gates and `CONTRIBUTING.md` with them. Deliverables covered all four issue items plus the confirmed `AGENTS.md` pointer, a new `change-branching` capability, and an out-of-scope bullet naming the repo-level-ADR exclusion. Impact followed the archived uv-toolchain precedent (affected files, process, downstream).

## Reviewer Challenges
- MAJOR: the new glossary term's definition ("the only way the change's commits reach `main`") contradicted the preserved archive-phase direct commit on `main`.
- MAJOR: the no-auto-commit preservation claim covered commits but not branch creation — the gate's actual new action — leaving the refusal path undefined and risking a spec that encodes an unconditional auto-cut.
- MAJOR: the capability abstract omitted the divergence-manifest row and the maintainer hand-merge/re-apply obligation (issue rule 5), so that MUST would have had no spec coverage.
- MINOR: unverified factual asides (#21 branch name, zero-runtime, "org-neutral upstream"); ambiguity between the new naming rule and the documented `<issue>-apply-<change>` implementation pattern; bolding hygiene (repeat bolds, misapplied terms).

## Resolutions
- Accepted: scoped the **issue branch** definition to planning and implementation commits, explicitly leaving the archive metadata commit direct on `main`.
- Accepted: the gate is ask-first under the skill's no-auto-git rule (which covers branches, not just commits); a decline keeps today's "warn and ask whether to continue intentionally" escape hatch, with refusal semantics delegated to design.
- Accepted: extended the `change-branching` abstract to include the divergence-manifest row and the maintainer hand-merge/re-apply obligation, so issue rule 5 gets spec requirements (precedent: the CI change spec'd its divergence-manifest row).
- Accepted: dropped the "org-neutral upstream" misapplication ("org-neutral" describes hep-metadex's identifiers, not the template); unbolded repeat uses; replaced the misapplied glossary term **change-time work** (defined as experiment-repository development) with the issue's own phrase "change work"; added the clarifying clause that the `<issue>-apply-<change>` implementation pattern is unchanged.
- Rejected: removing the glossary-term deliverable. `glossary/technical.md` exists at the repository root and is project content, distinct from the vendored skill at `.agents/skills/glossary/` (the fork the manifest records), so the edit does not deepen the skill fork or need drift-impact coverage. CONTRIBUTING's glossary discipline mandates recording terms introduced in specs, no existing glossary term covers the concept, and the uv-change precedent shipped a term alongside its change.
- Rejected: softening the #21 branch claim (verified in the archived uv proposal's Impact line) and the zero-runtime posture (verified in `openspec/config.yaml` context).

## Remaining Risks
- Refusal semantics (what an agent does when the user declines the branch) are asserted to preserve today's escape hatch but their exact wording is settled only at design time; the spec must encode consent-aware requirements, not an auto-cut.
- Adopters inherit the amended gates only on their next scaffolding sync; the proposal records this but no adopter-notification mechanism exists yet.
