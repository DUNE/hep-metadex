# ADR-0004: Adopt Apache-2.0, diverging from the template's MIT

## Status

Accepted

## Date

2026-11-05

## Context and Problem Statement

**HSF affiliation** requires an open-source license. The intent-driven template this repository was installed from ships MIT; the README divergence manifest records that `LICENSE.md` was deliberately not installed, deferring the decision. hep-metadex is a cross-institution standards artifact serving multiple experiments and, eventually, the HEP Software Foundation.

## Considered Options

- Apache-2.0 (explicit patent grant, defined contribution terms)
- MIT (template default; no explicit patent grant)
- Defer the choice to apply, with HSF Licensing activity input

## Decision Outcome

Chosen option: "Apache-2.0", because a cross-institution standards repository benefits from the explicit patent grant and defined contribution terms; the divergence from the template's MIT is recorded in the README divergence manifest rather than silently replacing the template file.

### Consequences

- Good, because the HSF checklist license item closes with a robust, permissive license.
- Bad, because the divergence manifest gains an entry that template syncs must preserve.
- Follow-up: the divergence-manifest entry and the HSF checklist mapping in `docs/hsf-affiliation.md` both reference this license.
