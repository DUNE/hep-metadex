# Glossary: Technical Terms

| Term | Definition | Use When | Avoid |
| --- | --- | --- | --- |
| Store | A standalone OpenSpec repository, registered per machine, whose specs and changes are shared by multiple code repositories. | Referring to hep-metadex in its store role. | Using for a data store or any persistence layer. |
| Reference | A read-only declaration in a project's openspec/config.yaml that injects a store's spec index into artifact workflows. | Describing how an experiment repository connects to the store. | Confusing with the write-routing `store:` config line. |
| Scaffolding | The replicable workflow kit installed into each experiment repository: schema, skills, commands, subagents, and agent guidance files. | Referring to what flows by template install rather than through the store. | Using for specs or changes, which flow through the store. |
