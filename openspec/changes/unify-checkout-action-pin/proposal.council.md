# Council Notes: proposal

## Author Summary
The author draft framed the drift problem (two workflows on `@v7`, two stranded on `@v4`, with `@v4` a floating tag that already moved), unified the pin at `@v7` across all four workflows with only `release.yml` and `validate.yml` edited, carried the kit release discipline (PATCH bump 1.0.0 → 1.0.1 plus `## [1.0.1]` changelog section in the same change), proposed the new capability `workflow-action-pinning`, and predicted the kit pipeline effects (silent reminder, gate holding archive until v1.0.1 publishes).

## Reviewer Challenges
- The capability description directed change-scoped constraints ("unification is behavior-neutral, including the CLI pin") into a durable spec, where they would freeze the CLI pin and all workflow evolution.
- "Every workflow pins checkout" overreaches (future workflows may have no checkout step) and hardcoding the four filenames goes stale on a fifth workflow.
- The capability name promises general pinning policy while the description delivers only the checkout pin; two of the issue's five out-of-scope items (enforcement mechanisms, DUNE policy re-evaluation) were silently dropped.
- "Its only breaking change" is an unestablished exhaustiveness claim — v4→v7 also crosses v5's node24 runtime requirement, which bears on self-hosted adopter runners; "Nothing is breaking" leaned on it.
- Internal inconsistency: "no documentation edits" vs a new ADR; the divergence-manifest non-change claim needed substantiation.
- Minor: compress the @v7-safety detail (belongs in design/ADR), imprecise "split widens passively", repeated bolding, "archive gate" vs the glossary term "Kit release gate", missing spec/ADR files in Impact, and no adopter-safety rationale.

## Resolutions
- Accepted: capability description rewritten as durable, universal invariants ("every workflow that uses `actions/checkout`", GitHub-created constraint, four files as conforming set not definition, future tightening is a modification); "OPENSPEC_VERSION untouched" kept change-scoped in What Changes; missing out-of-scope items restored; documentation claim scoped (no existing docs change; the ADR is new); safety detail compressed with evidence deferred to design.md and ADR 0011; ADR bullet made file-oriented; first-use-only bolding; glossary term "Kit release gate" used; `specs/workflow-action-pinning/spec.md` and `adr/0011-*.md` listed in Impact; adopter-safety clause added (shipped triggers exclude the event types v7's change touches).
- Partially accepted: "only breaking change" dropped as an exhaustiveness claim — the fork-PR-refusal mechanism and ubuntu-latest greenness are established investigation facts and stay, but the node24 runtime question is now explicitly deferred to design.md and ADR 0011 rather than waved away.
- Rejected: none.
- Deferred: self-hosted adopter runner currency (design.md + ADR 0011); first real `@v7` exercise of `validate.yml`/`release.yml` on this change's own PR runs (tasks verification step).

## Remaining Risks
- The unified pin remains a floating major tag; movement under it continues, now coordinated across four files instead of reviewed per-file.
- A self-hosted adopter runner below the node24-capable runner version would receive a runtime requirement through a PATCH kit release; design.md and ADR 0011 must record this consequence and its mitigation.
- Reminder and gate behavior is predicted from their source as read today; both are #35-owned mechanisms and should be confirmed behaving as predicted when this change's PR runs.
