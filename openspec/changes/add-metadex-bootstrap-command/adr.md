# ADR Review Manifest

- Status: completed
- Review date: 2026-11-19

## Review Summary

ADR review completed for this change. One major durable architectural decision met the bar: the kit's procedure-automation commands ship as kit-owned files inside the cli-owned commands directory — per-file KIT-MANIFEST entries with most-specific-matching-path precedence — and each kit release publishes them as standalone, checksummed assets that a documented one-liner fetches into an uninitialized repository. It extends ADR-0008's layer routing (which names this change as the command layer's first procedure automation) and ADR-0009's release channel (read-side only: one more asset, one more manifest entry) without diverging from any in-force decision; no supersession is warranted.

## In-Force ADRs Reviewed

- ADR-0001 — serve experiments via read-only store references and template-installed scaffolding (both channels preserved; the command automates the channel-2 bootstrap and writes the channel-1 references block)
- ADR-0002 — DUNE incubation with HSF endorsement trigger
- ADR-0003 — fenced Gherkin single-source validation gate (this change's delta specs are authored as fenced Gherkin)
- ADR-0004 — Apache-2.0 license diverging from template MIT
- ADR-0005 — host-conditional validation CI as scaffolding (the command automates the same host-conditional steps; the kit still ships GitHub implementations only)
- ADR-0006 — Python + uv repo-local maintainer toolchain (the command is zero-runtime agent instructions; the release-workflow edit uses none of it)
- ADR-0007 — Zensical docs site published from `docs/` in place (setup.md and usage.md edits publish in place; no site build changes)
- ADR-0008 — kit-layering routing rule (extended, not superseded: the bootstrap command lands procedure automation in the command layer, as the ADR anticipated)
- ADR-0009 — versioned kit releases (extended read-side: the release publishes the command asset, and the manifest gains per-file ownership granularity; the release contract and bump discipline are intact)
- ADR-0010 — kit release discipline via reminder and archive gate (untouched; this change is the gate's first dogfood)
- ADR-0011 — unified actions/checkout pin (the release-workflow edit adds no new Actions and keeps the unified `@v7` pin)

## New Durable ADRs Created

- `adr/0012-ship-kit-commands-as-kit-owned-files-fetched-from-kit-releases.md` — records the kit-command delivery pattern: the `hep-metadex-*` namespace as kit-owned per-file manifest entries with most-specific-path precedence, and command files published as checksummed standalone release assets fetched pre-scaffolding by the documented one-liner.
