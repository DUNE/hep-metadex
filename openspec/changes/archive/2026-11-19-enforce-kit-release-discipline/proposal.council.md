# Council Notes: proposal

## Author Summary
The author draft covered all four issue-#35 deliverables and every rule under the template's four headings: one new capability (`kit-release-discipline`), no modified capabilities, the three grilled decisions carried as settled scope (issue branch; repo-local gate script wired via the config guidance seam; one new capability with the single-source requirement covering release workflow, reminder, and gate), house-style Impact bullets, and the no-bump consequence stated with the #9 dogfood. It flagged the ADR-stage question, the manifest-restructure risk to the zero-kit-paths claim, and the guidance-vs-mechanical enforcement seam as author notes rather than hiding them.

## Reviewer Challenges
- **Divergence-manifest structure:** the draft's "two new rows" contradicted how docs/maintainer.md records `tools/` — the existing row (`zensical.toml`, `tools/`, `.github/workflows/docs.yml`) reads as documentation-site tooling (ADR-0007) and `tools/` scripts get no individual rows; a gate script is not documentation-site tooling.
- **ADR-stage silence:** the schema has an adr stage and house precedent names the expected ADR in the proposal (#34 names ADR-0009); the settled gate mechanism is ADR-grade and the single-source derivation touches ADR-0009-recorded behavior.
- **Pasteable-fix correctness:** the mandated fix text ("bump, merge, release cuts") is wrong advice for the documented misfire failure mode, where the remedy is the `workflow_dispatch` re-run — a second bump would scope the release wrong.
- **Dogfood imprecision:** "the gate's first exercise is #9" is doubly wrong — the gate's literal first run is this change's own archive (the new guidance line is live on `main` then), trivially green; #9 is the first substantive exercise, not "the issue's own dogfood."
- **Detection-semantics gap:** the deferral list named the gate's containment semantics but not the reminder's (what counts as a bump; which paths count as kit paths).
- **Zero-kit-paths verifiability:** the claim verified airtight but did not say why in the artifact.
- **Glossary nit:** bolded plural "Experiment repositories" where the glossary term is singular.
- **Enforcement hardness:** a guidance-wired gate is process discipline, not mechanical prevention; the hardness must live in the spec'd archive process.
- **release.yml refactor risk:** the strong single-source reading concentrates release-channel risk in an enforcement change; a lighter reading exists (mechanisms read the manifest, workflow untouched) and the proposal should name it and why it loses.
- **Never-red trap:** under the org's Actions policy, a nonzero-exit reminder renders a red X even without branch protection — in tension with MUST NOT block merge.
- **Why over-claim:** "the rule has no enforcement" overstated — release.yml's tag-exists gate enforces the adjacent re-release case; the forgotten-bump case is the genuinely silent one.
- **Multi-bump lifecycle:** containment semantics must survive a change that bumps, merges (release cut), then touches kit files again before archive.

## Resolutions
- Accepted: the reminder workflow gets a divergence-manifest row (the release.yml pattern); the gate script's manifest placement is named as an explicit amend-vs-new-row design decision against the existing ADR-0007 tooling row.
- Accepted: added the **ADR-0010** bullet naming the enforcement decision (reminder-plus-archive-gate over the rejected alternatives; the routing rationale; the ADR-0009 touch).
- Accepted: the gate's fix output is per-diagnosed-cause — the issue's text for the forgotten bump, the documented misfire re-run otherwise; added to the gate bullet and the deferral list.
- Accepted: the no-bump bullet now claims the gate's own trivially-green archive run as a free smoke test and names #9 as the first substantive dogfood; the zero-kit-path pass case is surfaced in the capability description for the specs stage.
- Accepted: reminder detection semantics added to the deferral list, symmetric with the gate's containment semantics.
- Accepted: the zero-kit-paths bullet now carries the one-clause verification path (only validate.yml is bundled from `.github/workflows/`; `tools/` and maintainer.md are off the copy-list; config.yaml is never-touch).
- Accepted: singular **Experiment repository** in the out-of-scope bullet.
- Accepted: the gate bullet states the hardness as archive-process discipline — the archive workflow runs the gate and refuses on failure — with the spec stage wording the observable rule.
- Accepted (adjusted): kept the strong single-source reading (the user's capability decision covers the release workflow inside the requirement) and named the lighter alternative with why it loses; equivalence risks carried to design.
- Accepted: the never-red constraint is stated in the reminder bullet and carried on the advisory-surface deferral.
- Accepted: the Why now says the release workflow's gates fire only after a bump and positions the mechanisms as complementing them.
- Accepted: multi-release-spanning changes and the no-prior-release edge are named in the containment-semantics deferral.
- Rejected: none.

## Remaining Risks
- The guidance-wired gate is process enforcement, not mechanical prevention; its hardness exists only insofar as the spec makes "the archive workflow runs the gate and refuses on failure" observable behavior.
- The release.yml derivation concentrates release-channel risk inside an enforcement change; the byte-identical equivalence is load-bearing (tar member ordering, directory handling) and must be verified in design and tasks.
- The zero-kit-paths claim depends on the manifest needing no restructuring for machine parsing; if design finds it must restructure `KIT-MANIFEST.yaml`, the change becomes kit-touching and the no-bump story breaks — the manifest stays unedited.
- The advisory surface must never render red; a wrong surface choice would psychologically block merges and violate the issue's MUST NOT.
- The gate first executes for real at this change's own archive, before any true failure has occurred; its first failure-path exercise is #9's archive, so a gate bug discovered there falls back to the pasteable fix and a manual re-run.
