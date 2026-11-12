# Issue Authoring Specification

## Purpose

Defines the **intent material** template for change issues — the GitHub issue form carrying its six required sections with the blank-issue path disabled, the Writing Issues guidance in the intent-prompt guidelines doc, the contributor and agent pointers that route authors to the template, and the **intent material** glossary term.

## Requirements

### Requirement: Issue form carries the intent-material sections
The GitHub issue form `.github/ISSUE_TEMPLATE/change.yml` SHALL carry the **intent material** sections as required fields in issue-body order — Context, Suggested change name, Actor, Deliverables, Rules, Out of scope — and SHALL offer one optional free-form field for the labeled optional sections (Gate, Trigger, Decisions inside the change, Provenance, References). The form's copy MUST remain **org-neutral**, naming no organization-specific process.

#### Scenario: A contributor opens a change issue

```gherkin
Given a contributor with a change to propose in this repository
When they open a new issue through the change form
Then the form presents the six required sections in issue-body order: Context, Suggested change name, Actor, Deliverables, Rules, Out of scope
And offers one optional field for the labeled optional sections
```

#### Scenario: An issue carries an optional labeled section

```gherkin
Given a change gated on a precondition the author records as a Gate section
When the author fills the optional field with that Gate section
Then the submitted issue body carries the Gate section alongside the required intent material sections
```

### Requirement: Blank issues disabled
`.github/ISSUE_TEMPLATE/config.yml` SHALL disable GitHub's blank-issue path (`blank_issues_enabled: false`), making the change form the single entry point for new issues.

#### Scenario: The issue chooser offers no blank issue

```gherkin
Given the repository's issue templates as delivered by this change
When a contributor opens the issue chooser
Then the change form is the only offered entry point
And no blank-issue option is offered
```

### Requirement: Writing Issues guidance in the intent-prompt guidelines
`docs/intent-prompt-guidelines.md` SHALL define the **intent material** template in a "Writing Issues" section — the six required sections, and the optional labeled sections (Gate, Trigger, Decisions inside the change, Provenance, References) as available additions — and the document SHALL remain at its current path.

#### Scenario: A reader finds the template definition

```gherkin
Given docs/intent-prompt-guidelines.md as delivered by this change
When a reader opens its Writing Issues section
Then it defines the six required sections and documents the optional labeled sections as available additions
And the document is found at its pre-change path
```

### Requirement: Contributor and agent pointers to the template
CONTRIBUTING.md's "Every Change Starts as an Issue" section SHALL point to the issue form and the Writing Issues guidance, and `AGENTS.md` SHALL extend its `docs/intent-prompt-guidelines.md` pointer so agent-authored issues follow the template. The change MUST NOT add a new authoring skill; agent guidance flows through the existing AGENTS.md → guidelines-doc pointer.

#### Scenario: A contributor finds the template from the contribution policy

```gherkin
Given the Every Change Starts as an Issue section of CONTRIBUTING.md
When a contributor prepares to open a change issue
Then the section points them to the issue form and the Writing Issues guidance
```

#### Scenario: An agent session follows the convention without a new skill

```gherkin
Given an agent session that has read AGENTS.md
When the session authors a new issue
Then AGENTS.md directs it to follow the intent-material template through the guidelines doc
And no authoring skill beyond the existing kit is involved
```

### Requirement: Intent material glossed
`glossary/domain.md` SHALL carry an **intent material** entry defining the structured issue body the change workflows consume, with definition, use-when, and avoid guidance.

#### Scenario: A reader finds the term glossed

```gherkin
Given the glossary as delivered by this change
When a reader encounters intent material in the issue form or the guidelines doc
Then glossary/domain.md defines the term with use-when and avoid guidance
```
