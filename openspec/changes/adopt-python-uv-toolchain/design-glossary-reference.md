# Glossary Reference

| Term | Source Glossary | Context |
| --- | --- | --- |
| Maintainer toolchain | `glossary/technical.md` | The change's core concept: the Python + uv tooling this design establishes as repo-local, outside both ADR-0001 channels. |
| Workflow scaffolding | `glossary/technical.md` | The outbound kit; the design scopes it as untouched and contrasts its template-install channel with the toolchain's non-channel boundary. |
| OpenSpec Store | `glossary/technical.md` | hep-metadex in its store role; the read-only spec channel the design leaves unchanged. |
| Store reference | `glossary/technical.md` | Named in the diagram as the read-only spec-index edge to experiment repositories. |
| Experiment repository | `glossary/domain.md` | Adopting repositories, which the design explicitly constrains nothing for. |
| Common capability | `glossary/domain.md` | The store-owned specs in the Context paragraph; unchanged by this design. |
| Org-neutral | `glossary/domain.md` | Property the hsf-affiliation rewrite must preserve, per ADR-0002 (D5). |
