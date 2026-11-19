# Glossary Reference

| Term | Source Glossary | Context |
| --- | --- | --- |
| Intent material | `glossary/domain.md` | Issue #44's structured body is the authoritative request the design implements. |
| Experiment repository | `glossary/domain.md` | Adopters receive the unified pin through `validate.yml` in the v1.0.1 bundle. |
| Workflow scaffolding | `glossary/technical.md` | The kit whose copy-list makes this change kit-touching. |
| Kit release | `glossary/technical.md` | v1.0.1 cuts automatically on merge, carrying the updated `validate.yml`. |
| Kit release gate | `glossary/technical.md` | Holds archive until v1.0.1 contains this change's kit-touching commit. |
| Kit version file | `glossary/technical.md` | `.metadex-kit`, bumped 1.0.0 → 1.0.1 (PATCH) in the same change. |
| Kit reminder | `glossary/technical.md` | Expected to stay silent on this change's PR because the bump is present. |
| Issue branch | `glossary/domain.md` | `44-unify-checkout-action-pin`, cut from `main` before the change's first commit. |
