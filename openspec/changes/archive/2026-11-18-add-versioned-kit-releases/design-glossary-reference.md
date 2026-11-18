# Glossary Reference

| Term | Source Glossary | Context |
| --- | --- | --- |
| OpenSpec Store | `glossary/technical.md` | hep-metadex's store role; its checkout keeps floating on `main` while the kit pins to releases. |
| Workflow scaffolding | `glossary/technical.md` | The kit — what the version file versions, the bundle carries, and adopters install. |
| Store reference | `glossary/technical.md` | Channel-1 connection; the design leaves it and its doctor fix untouched. |
| Spec index | `glossary/technical.md` | Channel-1 injection flowing from the floating checkout, unchanged. |
| Maintainer toolchain | `glossary/technical.md` | The repo-local class the release workflow joins; the workflow itself needs none of it (bash + git + gh). |
| Documentation site | `glossary/technical.md` | Reaches the changelog through rewritten out-of-tree links only (D4). |
| Experiment repository | `glossary/domain.md` | The adopter receiving the pre-stamped, checksum-verified kit; dune-metadex is the dogfood target. |
| Intent material | `glossary/domain.md` | Issue #34's body — the delegated decisions this design resolves (D1–D4). |
