# Glossary Reference

| Term | Source Glossary | Context |
| --- | --- | --- |
| Kit release | `glossary/technical.md` | Every kit release ships the lagging `@v4` pin; v1.0.1 is cut automatically on merge. |
| Workflow scaffolding | `glossary/technical.md` | The kit whose copy-list includes `validate.yml`, making this change kit-touching. |
| Experiment repository | `glossary/domain.md` | Installed repositories receive `validate.yml` with the unified pin when they update. |
| Kit version file | `glossary/technical.md` | `.metadex-kit`, bumped 1.0.0 → 1.0.1 in this change. |
| Kit reminder | `glossary/technical.md` | Expected to stay silent on this change's PR because the version bump is present. |
| Kit release gate | `glossary/technical.md` | Holds archive until published release v1.0.1 contains the kit-touching commit. |
