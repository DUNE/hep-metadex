# Council Notes: proposal

## Author Summary
- Drafted via adversarial-author subagent: a Why focused on the unrecorded convention and the unrecorded routing rule; seven What Changes bullets covering every issue #23 deliverable; one new capability (`issue-authoring`) and one modified capability (`adopter-onboarding`) per the user's grill-interview decision; Impact enumerating new/modified files and the no-schema-fork, no-new-skill, validate.yml-untouched bounds.

## Reviewer Challenges
- The routing-rule ADR and its two cross-references (docs/maintainer.md Repository Configuration, CONTRIBUTING.md "Where Decisions Live") had no home in the Capabilities contract — the specs phase would have had no delta spec to place them in.
- The host-conditional copy scope was ambiguous about `config.yml` — copying the form without its config leaves blank issues enabled downstream; unclear whether the manifest gets one row or two.
- The `glossary/domain.md` entry was listed in Impact but owned by no capability.
- The Why's universal claims ("recorded nowhere", "the open issues now follow") risked inaccuracy; "ADR-0008" hardcoded; "ADR under adr/" unverified; "durable family architecture" undefined jargon.
- The `issue-authoring` description risked hardcoding GitHub mechanics into a capability that must serve non-GitHub-hosted adopters.
- Open questions: CONTRIBUTING.md ownership overlap with governance-docs; whether new specs are common capabilities automatically; ADR content freezing from proposal text; coordination with #9 (`/metadex-bootstrap`).

## Resolutions
- Accepted: `governance-docs` added as a second modified capability owning the ADR and its cross-references (user confirmed).
- Accepted: the copy-list item and the divergence-manifest row cover `.github/ISSUE_TEMPLATE/` — both files, one item, one row.
- Accepted: the glossary entry is owned by `issue-authoring`, the capability that coins the term.
- Accepted: provisional ADR numbering (next sequence, assigned at the adr stage); plainer Why wording ("reformatted onto", no "family" jargon); capability description leads with the host-neutral convention and names the GitHub form as this repository's implementation; **intent material** bolded at first mention.
- Rejected (verified against the repository): "recorded nowhere" — accurate; `docs/intent-prompt-guidelines.md` covers intent prompts, not issue authoring, and no form, doc, or spec carries the issue template (kept with sharpened wording). "ADR under `adr/`" — verified: ADRs 0001-0007 live at `adr/`. CONTRIBUTING.md ownership overlap — none; governance-docs carries no requirement on the "Every Change Starts as an Issue" section content. Common-capability designation — every spec under `openspec/specs/` is a common capability by construction, injected via the spec index.
- Deferred: #9 coordination (its future bootstrap command must absorb the new host-conditional copy item) — a tasks-stage note; exact form field attributes — design/specs stages.

## Remaining Risks
- ADR sequence collision if a concurrent ADR-bearing change lands first; mitigated by assigning the number at the adr stage.
- The routing-rule enumeration passes from issue #23's exploration settlement into the ADR verbatim; any drift from that exploration is frozen into the ADR at the adr stage.
