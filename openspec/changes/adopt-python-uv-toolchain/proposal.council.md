# Council Notes: proposal.md

## Author Summary

Drafted the proposal per the intent-driven template: a two-sentence Why (TBD tech stack → pinned toolchain ahead of #22), eight What Changes bullets (ADR-0006, bare uv scaffolding with the 3.14 pin, config context, hsf-affiliation row, divergence-manifest row, README note, glossary term, out of scope), both Capabilities sections as "None — <reason>" per the verified spec scan, and five Impact bullets (Repositories, No breaking changes, Tool dependency, Process, Downstream) matching the archived add-spec-validation-ci house style.

## Reviewer Challenges

- The scaffolding bullet omitted the grill-me-resolved `[dependency-groups]` while the Downstream bullet presupposed it — internal inconsistency and a requirement-coverage miss.
- Divergence-manifest row granularity was ambiguous (one combined row vs. one row per file), and the "not added during a sync" phrasing read as an invented normative rule.
- Three claims overreached: "the OpenSpec CLI remains the only tool they are asked to install," assertions about #22's CI design ("relies on," "will land in"), and characterization of the hsf-affiliation row's current wording.
- Why leaked an anachronism ("toolchain for the docs engine" — no docs engine exists until #22) and attached "zero-runtime" to the toolchain rather than the repository.
- Glossary-term drift: "maintainer-side tooling"/"maintainer-side toolset" variants instead of the term being defined; plural/singular inconsistency for **experiment repository**.
- "Nothing downstream consumes the new files" (No breaking changes) sat in tension with the Downstream bullet where #22 consumes them.
- Verify-before-final risks: does `.gitignore` belong to the kit (out-of-scope conflict)? Do all bolded glossary terms exist? Does the config context literally read "Tech stack: TBD"?

## Resolutions

- Accepted: `[dependency-groups]` added to the scaffolding bullet (empty in this change, reserved for #22); enabling language for #22 claims ("can land in," "can rely on"); Tool dependency softened to "adopters are asked to install nothing new"; Why rephrased to name #22 as the ahead-work and to keep "zero-runtime" a property of the repository; term usage unified to **maintainer toolchain**; "no adopting repository consumes the new files" qualifier added; the resolved definition's gist included in the glossary bullet.
- Accepted with grounding (verified against the repo, not just softened): the "not added during a sync without a deliberate decision" semantics are the existing `package.json` manifest row's own text (`docs/maintainer.md`), so the new row mirrors established semantics rather than inventing a rule; the hsf-affiliation row literally reads "the tech stack is TBD by design until the first runtime change," so the draft's characterization stands.
- Rejected: one-row-per-file granularity — the existing manifest precedent is a single combined row for `package.json`/`package-lock.json`/`skills-lock.json`, so the Python analogue is likewise one combined row.
- Resolved by verification: `.gitignore` is repo-local (absent from the README step-4 copy list; already a manifest divergence row), so additions do not flow to adopters; all bolded terms exist in `glossary/domain.md` or `glossary/technical.md`; the config context line is verbatim "Tech stack: TBD".

## Remaining Risks

- Exact rewrite wording for the config context and the hsf-affiliation row is apply-time detail; the proposal's claims about their current text are verified, but the replacements are designed later (design.md/tasks.md).
- A minimum-uv-version expectation for lockfile compatibility is unsettled; design.md should decide whether to document one.
