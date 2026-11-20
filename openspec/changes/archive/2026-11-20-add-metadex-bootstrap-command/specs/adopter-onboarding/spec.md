# Adopter Onboarding

## ADDED Requirements

### Requirement: Agent-assisted bootstrap command as the primary path
The agent-assisted bootstrap section of `docs/setup.md` SHALL present the `/hep-metadex-bootstrap` command as the primary agent-assisted bootstrap path — for greenfield and brownfield **experiment repositories** alike — with the documented prompt remaining the fallback and the specification the command automates, and SHALL document the one-liner that fetches the command file from the latest kit release and hands it to the agent.

#### Scenario: A reader finds the command as the primary path

```gherkin
Given the agent-assisted bootstrap section of docs/setup.md
When an adopter wants an agent-assisted bootstrap
Then the section presents the /hep-metadex-bootstrap command as the primary path
And the documented prompt remains as the fallback and the specification the command automates
```

#### Scenario: A reader finds the one-liner

```gherkin
Given the agent-assisted bootstrap section of docs/setup.md
When an adopter starts from an uninitialized repository
Then the section documents the one-liner that fetches the command file from the latest kit release
And hands it to the agent
```

#### Scenario: The documented prompt's procedure is unchanged

```gherkin
Given the documented agent-assisted bootstrap prompt
When the bootstrap command ships as the primary path
Then the prompt's steps are unchanged
And the prompt is framed as the fallback and the specification the command automates
```

### Requirement: Divergence manifest frames the bootstrap command as kit scaffolding
The divergence-manifest entry for `.opencode/commands/hep-metadex-bootstrap.md` SHALL present the command as a component of **workflow scaffolding** — the kit's first kit-owned command, shipped inside the cli-owned commands directory — while remaining recorded as an intentional divergence from the intent-driven template, which ships no kit commands.

#### Scenario: An adopter reads the command's manifest entry

```gherkin
Given the divergence manifest in the maintainer guide
When an adopter reads the entry for the bootstrap command
Then it presents the command as kit scaffolding installed from the kit release bundle
And a maintainer syncing from the template preserves it as an intentional divergence
```
