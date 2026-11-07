# Council Notes: proposal

## Author Summary

The author draft framed the gap — a bootstrapped **experiment repository** installs the agent-facing pieces of **workflow scaffolding** but no validation gate, while the divergence manifest records the workflow as a local-only divergence — and proposed four What Changes bullets (dune-metadex CI, host-conditional bootstrap step, scaffolding reframe of the manifest entry, dogfooded README quick start) plus an out-of-scope bullet; a single modified capability `adopter-onboarding` with no new capabilities; and Impact bullets covering repositories, no breaking changes, tool dependency, process, and downstream effects.

## Reviewer Challenges

- Impact claimed hep-metadex changes "documentation only" with "no stored spec content changes," contradicting the Modified Capabilities section — the `adopter-onboarding` delta is spec content, synced into `openspec/specs/` at archive.
- **org-neutral** was misused to justify name-only non-GitHub coverage; the term concerns naming no GitHub organization, not CI-host coverage.
- House style: the capability entry used an em dash instead of the colon format from the issue #7 proposal.
- The quotation "the template ships no CI" was flagged as unverified against the provided facts.
- "Tracked here as a deliverable" was ambiguous about which artifact tracks the dune-metadex work.
- The glossary-extension timing was unstated, so the Why read as using a sense the glossary does not yet carry.
- Downstream overclaimed that "divergence bookkeeping shrinks" — the manifest entry remains, reworded.
- Terminology nits: "worked scenario" (scenario is loaded by ADR-0003's fenced Gherkin), and the bootstrap install list under-described what is actually installed.
- Open questions: whether maintainer-facing edits belong in the delta spec as adopter-observable requirements; whether dune-metadex's PR installs the same file the bootstrap step tells adopters to copy; cross-repo merge-gating mechanics if the dune-metadex PR stalls.

## Resolutions

- Accepted: rewrote Impact→Repositories to name the `adopter-onboarding` spec delta and its archive-time sync, keeping only the true point (the **Store reference** channel is unchanged); deleted the **org-neutral** clause (name-only non-GitHub coverage is justified by the out-of-scope rule); switched the capability entry to colon format; "tracked as a deliverable in this change's tasks.md"; added "(definition updated at apply time)" to the scaffolding reframe; reworded Downstream (the entry remains but describes distributed **workflow scaffolding**); replaced "worked scenario" with "worked example"; listed the real bootstrap install set in the Why; added the dogfood-equivalence clause (dune-metadex gains the same workflow file future adopters will copy).
- Rejected: re-attaching **org-neutral** as "the bootstrap docs name no organization" — inaccurate, the docs' clone URLs name the DUNE organization, and the term's avoid-guidance warns against stretched uses; removing the "the template ships no CI" quotation — verified verbatim in docs/maintainer.md's divergence table during primary-agent exploration (the reviewer's fact sheet omitted it); unbolding **common capability** — it is a glossary term (glossary/domain.md).
- Deferred: whether the manifest reframe and glossary extension surface as adopter-observable requirements in the delta spec or stay in design/tasks — decided at the specs stage; cross-repo merge mechanics (one held hep-metadex PR vs. split merges, and the contingency if the dune-metadex PR stalls) — for design/tasks.

## Remaining Risks

- The single-PR vs. split-merge sequencing, and the stall contingency for dune-metadex's PR, must be answered in tasks.md or this change's archive could block on another repository.
- The delta spec must keep its requirements adopter-observable; otherwise maintainer bookkeeping becomes untestable spec requirements.
- Pre-existing and out of scope: the `governance-docs` spec's "strict validation" scenario wording diverges from ADR-0003's non-strict `valid: true` gate — a candidate for a separate small change.
