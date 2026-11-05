# ADR-0003: Gate spec validation on valid with fenced Gherkin as the single scenario source

## Status

Accepted

## Date

2026-11-05

## Context and Problem Statement

The project's configured spec-as-source practice requires scenarios as fenced Gherkin — structure in Markdown headings, steps in column-0 ```` ```gherkin ```` fences — so the acceptance extractor can synthesize `.feature` files. The OpenSpec CLI 1.16.0 validator recognizes only bullet-style `- **WHEN**`/`- **THEN**` steps: fenced specs validate as `valid: true` (exit 0), but `--strict` promotes the validator's step-detection warnings to failure (exit 1). Both formats cannot pass strict without writing every scenario twice.

## Considered Options

- Fenced Gherkin only; gate CI and pre-archive checks on `valid: true` (non-strict)
- Hybrid: bullet steps mirroring each fence (strict passes; extraction blanks the bullets)
- Bullet-only scenarios (abandons spec-as-source; the acceptance extractor has nothing to run)

## Decision Outcome

Chosen option: "fenced Gherkin with valid-gated validation", because scenarios must have exactly one authoritative representation; the acceptance toolchain enforces the same properties the validator's warnings approximate — and more strongly: extraction hard-errors on a scenario without steps, the runner fails on pending or undefined steps, and gherkin-lint runs on the extracted features.

### Consequences

- Good, because single-source scenarios eliminate drift between representations.
- Good, because CI still fails on every structural error (`valid: false`).
- Bad, because `--strict` is unusable for fenced specs on CLI 1.16.0; contributors who see the warnings need the known-issue note.
- Follow-up: revisit when an OpenSpec CLI release recognizes fenced scenarios; CLI version pinning and upgrade guidance live in the adopter documentation.
