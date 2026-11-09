# hep-metadex

The general-purpose reference for building experiment metadata management
systems across high-energy physics — published as an
[OpenSpec Store](../glossary/technical.md): a standalone, registered OpenSpec
repository whose [common capability](../glossary/domain.md) specifications
any experiment can consume read-only, plus the
[workflow scaffolding](../glossary/technical.md) that experiments install by
template.

This site is the reading front door for evaluators and adopter maintainers.
The [repository](../README.md) remains the adopter entry point with its quick
start; everything readable there is readable here.

## Where to start

- **Adopting an experiment** — [setup.md](setup.md) walks a fresh repository
  to a connected one; [usage.md](usage.md) covers change-time work and
  write-back.
- **Evaluating the project** (HSF or otherwise) — [governance.md](governance.md)
  records decision rights and the review bar;
  [hsf-affiliation.md](hsf-affiliation.md) maps every required HSF
  affiliated-project guideline to the artifact in this repository that
  satisfies it.
- **Maintaining this repository** — [maintainer.md](maintainer.md) holds
  template provenance, the divergence manifest, and update-from-upstream
  guidance.
- **Contributing a change** — see
  [CONTRIBUTING.md](../CONTRIBUTING.md) in the repository; the
  [intent prompt guidelines](intent-prompt-guidelines.md) shape the intents
  that drive every change.

## What flows where

Content reaches an [experiment repository](../glossary/domain.md) through two
independent channels:

1. **Specs flow through the store, read-only.** A
   [Store reference](../glossary/technical.md) declaration injects the
   store's [spec index](../glossary/technical.md) into the experiment's
   artifact workflows.
2. **Workflow scaffolding replicates by template install.** The kit is
   copied from a hep-metadex checkout at bootstrap time; it never flows
   through the store.

[dune-metadex](https://github.com/DUNE/dune-metadex) is the first adopter,
proving the mechanism end to end.
