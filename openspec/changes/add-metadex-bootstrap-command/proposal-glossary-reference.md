# Glossary Reference

| Term | Source Glossary | Context |
| --- | --- | --- |
| Experiment repository | `glossary/domain.md` | The uninitialized greenfield or brownfield repository the command bootstraps; its provenance stamp arrives with the install. |
| Intent material | `glossary/domain.md` | Issue #9's body is the authoritative request this proposal follows. |
| OpenSpec Store | `glossary/technical.md` | Registration is a machine prerequisite the command verifies before bootstrapping. |
| Store reference | `glossary/technical.md` | What the command's config-authoring step writes into `openspec/config.yaml` — the references block, never a `store:` line. |
| Workflow scaffolding | `glossary/technical.md` | The kit channel the command ships in; template install is the delivery mechanism. |
| Kit release | `glossary/technical.md` | The versioned, checksum-verified source the command installs from (latest by default, pin-able) and the one-liner fetches the command file from. |
| Kit version file | `glossary/technical.md` | `.metadex-kit` — bumped to 1.1.0 in this change; arrives with the install as the provenance stamp, never authored by the command. |
| Kit reminder | `glossary/technical.md` | Review-time advisory that sees the new manifest entry by construction via the single-source copy-list. |
| Kit release gate | `glossary/technical.md` | Archive-time containment gate this change dogfoods first (`uv run tools/kit_release_gate.py 9`). |
| Maintainer toolchain | `glossary/technical.md` | The repo-local class the release workflow's asset-publication extension belongs to. |
| Issue branch | `glossary/technical.md` | `9-add-metadex-bootstrap-command`, cut from `main` before the first commit. |
