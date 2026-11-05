# Glossary: Domain Terms

| Term | Definition | Use When | Avoid |
| --- | --- | --- | --- |
| Experiment repository | A code repository, such as dune-metadex, holding one experiment's domain-specific specs, changes, and implementation. | Referring to a consuming repository like dune-metadex, eic-metadex, or sphenix-metadex. | Using for the hep-metadex reference repository itself. |
| Common capability | A capability specification owned by the hep-metadex store describing behavior shared across experiments. | Referring to specifications that experiment repositories cite and specialize. | Using for experiment-specific capabilities that live in an experiment repository. |
| Org-neutral | Property of identifiers and documents that name no specific GitHub organization, so hosting can move without renames. | Describing the store id, governance documents, or contribution policy. | Using to imply the repository is hosted neutrally while it lives in the DUNE organization. |
| HSF affiliation | Endorsement by the HEP Software Foundation Steering Group under its affiliated-projects process, valid for five years. | Referring to the legitimacy trigger and its evaluation checklist. | Confusing with hosting in the HSF GitHub organization, which is a separate, mutually agreed follow-on. |
