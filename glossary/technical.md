# Glossary: Technical Terms

| Term | Definition | Use When | Avoid |
| --- | --- | --- | --- |
| OpenSpec Store | A standalone OpenSpec repository, registered per machine, whose specs and changes are shared by multiple code repositories. | Referring to hep-metadex in its store role, or to the OpenSpec Stores feature. | Using bare "store" in prose where a data store or persistence layer could be meant — this project's domain is metadata storage. |
| Store reference | A read-only declaration in a project's `openspec/config.yaml` (`references:` block) that injects an OpenSpec Store's spec index into artifact workflows. | Describing how an experiment repository connects to the OpenSpec Store. | Confusing with the write-routing `store:` config line, citation references, or calibration reference data. |
| Workflow scaffolding | The replicable workflow kit installed into each experiment repository: schema, skills, commands, subagents, and agent guidance files. | Referring to what flows by template install rather than through the OpenSpec Store. | Using for code-generation scaffolding, or for specs and changes, which flow through the OpenSpec Store. |
| Spec index | The list of an OpenSpec Store's common capability specs — one-line summaries plus fetch commands — injected into the artifact workflows of connected repositories. | Describing what a store reference injects at change time. | Using for spec listings produced by other tooling. |
