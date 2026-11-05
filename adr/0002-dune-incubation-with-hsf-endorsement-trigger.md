# ADR-0002: Incubate the OpenSpec Store in the DUNE organization with HSF endorsement as the affiliation trigger

## Status

Accepted

## Date

2026-11-05

## Context and Problem Statement

hep-metadex is mandated to be usable by experiments beyond DUNE, and the HEP Software Foundation's affiliated-projects process is the chosen legitimacy path. The repository currently lives in the DUNE GitHub organization; hosting there reads as DUNE-owned to other experiments. **HSF affiliation** (Steering Group endorsement after a checklist-based evaluation) is distinct from HSF GitHub-organization hosting, which the HSF describes as optional and mutually agreed.

## Considered Options

- DUNE-org incubation; HSF Steering Group endorsement triggers affiliation; HSF-org hosting as a separate, optional, mutually-agreed follow-on
- Immediate transfer to the HSF organization before the pattern is proven
- Adoption-driven trigger (move when the first non-DUNE experiment joins)

## Decision Outcome

Chosen option: "DUNE incubation with HSF-endorsement trigger", because internal reviews must first greenlight the approach and affiliation requires evidence the checklist can verify; endorsement is the legitimacy event, and because the **OpenSpec Store** id (`hep-metadex`) and all governance text are **org-neutral**, the hosting move — whenever mutually agreed — is a one-repo infrastructure transfer (update git remotes and the advisory `remote:` line in experiment configs; registrations and ids survive).

### Consequences

- Good, because affiliation de-risks the DUNE-ownership perception even if hosting is deferred.
- Good, because a single repository moves; **experiment repositories** never relocate.
- Bad, because endorsement timing is outside this project's control; adoption may precede it — cross-org write access and **org-neutral** governance must operate during incubation regardless.
- Follow-up: informal HSF Steering Group discussion can start during incubation; the affiliation checklist mapping lives in `docs/hsf-affiliation.md`.
