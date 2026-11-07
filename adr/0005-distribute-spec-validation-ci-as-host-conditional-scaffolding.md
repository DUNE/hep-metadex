# ADR-0005: Distribute the spec-validation workflow as host-conditional workflow scaffolding

## Status

Accepted

## Date

2026-11-07

## Context and Problem Statement

ADR-0001 established two channels: specs flow read-only through the **OpenSpec Store**; **workflow scaffolding** replicates by template install with hep-metadex as its source. The kit as defined — schema, skills, commands, subagents, and agent guidance — carries no validation gate, so a bootstrapped **experiment repository** has no automated check that its specs and changes validate, even though hep-metadex gates itself with `.github/workflows/validate.yml` (`openspec validate --all`, gating on `valid: true` non-strict per ADR-0003, CLI pinned to 1.16.0). The divergence manifest records that workflow as a local-only divergence from the intent-driven template, so adopters never receive it. Hosting also varies across the adopter family: dune-metadex is GitHub-hosted today, but nothing binds future **experiment repositories** to GitHub Actions.

## Considered Options

- Host-conditional scaffolding component: GitHub-hosted adopters copy the provided workflow verbatim; repositories on other hosts get the named equivalent gate, no implementation
- A universal CI configuration for all hosts (rejected — no portable CI format exists; a GitHub Actions workflow runs only on GitHub)
- Per-host implementations shipped now, GitHub plus others (rejected — none is dogfooded; out of scope until a non-GitHub adopter exists to verify one)
- Keep the workflow hep-metadex-local (rejected — leaves adopters without the automated gate the store itself relies on, and the divergence manifest hides the file's distributed role)

## Decision Outcome

Chosen option: "host-conditional scaffolding component", because the gate must reach adopters through the channel that already carries the kit — template install (ADR-0001, channel 2) — and the only coverage promise the project can make honestly is the one it can dogfood: GitHub-hosted adopters receive the same file hep-metadex runs, with identical gate semantics (ADR-0003: `valid: true` non-strict, CLI pinned), while repositories on other hosts wire the named equivalent gate into their own CI. The divergence-manifest entry records the workflow as an intentional divergence with its distributed role stated, and the **workflow scaffolding** glossary term extends to include the CI workflow as a GitHub-host component. dune-metadex, the first adopter, dogfoods the step end to end before the documentation claims it.

### Consequences

- Good, because every GitHub-hosted bootstrap ends with the validation gate in place, making spec drift CI-visible in adopters rather than store-only.
- Good, because the dogfooded instance and the distributed file are one and the same, so the quick start's verified-path claim stays true.
- Bad, because adopters on non-GitHub hosts receive a named gate but no implementation — wiring it is their own work.
- Bad, because copied workflows drift from the source until adopters re-run the scaffolding install; the manifest's drift-impact discipline is the reconciliation.
- Follow-up: per-host implementations remain a deliberate seam; a future host guide extends the kit the same way — dogfooded first.
