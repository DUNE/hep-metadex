# Writing Intent Prompts

Contributor reference for crafting the intent given to `/opsx-new` or
`/opsx-propose`.

The "user" in BDD-style scenarios is not necessarily an end user. It is the
**actor who receives value** from the capability. Platform engineers,
developers, architects, on-call engineers, and CI pipelines are all valid
actors. Gherkin does not care who the actor is — it needs a system boundary
with observable behaviour.

## Template

```text
/opsx-new Allow <actor> to <capability>.

Actor: <who they are and what boundary they operate at>
Deliverables: <artifacts, if not code>
Rules:
- <observable invariants, SHALL/MUST phrasing>
Out of scope: <what the agent must NOT build>
```

Every part is load-bearing:

- **Intent sentence** — capability + actor + verb. Swap the actor freely.
- **Actor** — names who receives the value and steers scenarios away from
  UI-style defaults.
- **Rules** — observable invariants. This is what determines whether Gherkin
  scenarios and acceptance tests work, regardless of actor.
- **Deliverables / Out of scope** — stop the pipeline from generating
  implementation work you did not ask for.

The `context` block in [openspec/config.yaml](../openspec/config.yaml)
carries global project background; actor-specific context belongs in the
prompt body.

The proposal stage runs `grill-me`, `adversarial-authoring`, and `glossary`.
A prompt that already names actor, deliverables, rules, and out-of-scope
gives those skills better material — a vague intent gets interrogated into
these sections anyway, so front-load them.

## Choosing the actor: redefine the boundary

For non-end-user actors, the mental move is to **redefine the system
boundary, and let the actor follow**:

| Actor | System boundary |
|-------|-----------------|
| End user | The application — UI, API responses |
| Platform engineer | The infrastructure module — chart, manifests, cluster |
| Architect | The documentation set (content rubric), or the architecture itself via invariant-checking tools |

Pick the actor whose outcome you can actually observe, because the
acceptance test must verify it from that boundary. Sometimes the truest
actor is the consuming team ("Allow developer teams to spin up a staging
environment with one command") rather than the operator.

A `Then` step must describe an outcome visible to a user **or an external
system**. For infrastructure, the external system is the cluster,
`kubectl`, or CI — that is the observer.

## Worked examples

### End user

The familiar case, from the
[intent-driven.dev BDD walkthrough](https://intent-driven.dev/blog/2026/07/17/behavior-driven-development-sdd-openspec/):

```text
/opsx-new Allow users to vote for a poll that already exists.

Rules:
- A vote cannot be modified once it is cast.
- A duplicate vote cannot be cast for the same email ID —
  email ID is the unique identifier.
```

### Platform engineer (infrastructure code)

Infrastructure code has real, observable, automatable behaviour — it
renders, validates, becomes ready, and scales. Only the actor and boundary
change:

```text
/opsx-new Allow platform engineers to provision the metadata catalog API
on Kubernetes with autoscaling.

Actor: platform engineer — the operator deploying and running the service.
Rules:
- The deployment MUST become ready within 60 seconds of a clean apply
  on a 3-node cluster.
- Autoscaling keeps CPU utilization between 40-70%; minimum 2 replicas,
  maximum 6.
- Every container declares CPU and memory requests and limits.
- Credentials are mounted from Kubernetes Secrets; values files never
  contain them inline.
```

The rules become scenarios at the infrastructure boundary:

```gherkin
Feature: Metadata catalog deployment
  Rule: The service deploys cleanly and autoscales under load

    Scenario: Deployment becomes ready on a fresh cluster
      Given a 3-node cluster with the metrics server running
      When the platform engineer applies the catalog chart with default values
      Then the catalog deployment reports ready within 60 seconds
      And 2 replicas are serving traffic
```

If running a cluster in CI is too heavy, validate at the static boundary
instead — the chart renders and manifests pass policy checks. Still
Gherkin, still automated, just a different harness.

### Architect (design artifacts, no implementation)

Design and ADR artifacts are first-class stages in this schema. Declare the
deliverable and scope out implementation explicitly, or the pipeline will
generate an implementation task list:

```text
/opsx-new Allow the system architect to record and communicate the
metadata storage architecture decision.

Deliverables: design.md plus a repository ADR under adr/.
This is a design-only change — no implementation code.

Rules:
- The ADR MUST compare at least PostgreSQL, MongoDB, and a
  registry-on-object-store approach against query patterns, relational
  integrity, and operational cost.
- The ADR MUST state consequences and a review trigger
  (e.g., catalog exceeds 10 TB).
- Tasks are limited to artifact authoring and review.

Out of scope: schema definitions, client code, migration tooling.
```

For design-only intents, the generated scenarios act as a **content
rubric** for the writing agent ("When a reader opens the ADR, Then it lists
three alternatives with consequences") — a deterministic definition of done
for the artifact, but not a behavioural test of a running system. See the
docs-only note below before proposing one.

## When Gherkin acceptance tests fit

| Situation | Approach |
|-----------|----------|
| Observable behaviour at a boundary — infra code, CLIs, CI pipelines, APIs | Full Gherkin scenarios with automated acceptance tests. The deterministic "done" signal matters *more* here, not less |
| Prose deliverable content (ADR reasoning, design narrative) | Gherkin as review rubric; human review carries acceptance |
| Doc-set meta-gates (template compliance, index links, supersession graph validity) | Automatable doc-lint scenarios |
| Tool-enforceable architecture invariants (dependency boundaries, API lint) | True behavioural Gherkin backed by checker steps (dependency-cruiser and similar) |

Pending or undefined steps are acceptable initially: scenarios can land as
specification before automation is wired.

## Repo-specific notes

- **Acceptance stack selection.** `acceptance-test-authoring` (CLI 1.16.0)
  is stack-agnostic: it reads a `stack:` key in `openspec/config.yaml`
  (`javascript` → cucumber-js, `python` → behave) and asks when none is
  recorded — it never scaffolds a runner on a guess. Record `stack:` when
  the tech stack decision lands; the suite's hooks boot the application,
  so the runner follows the application stack. The bindings remain
  application/UI-oriented (page objects, an HTTP-client World);
  infra-boundary changes adapt step definitions to wrap CLI tools
  (`helm template`, `helm lint`, `kubectl apply --dry-run=server`,
  `conftest`) or a throwaway kind/k3d cluster.
- **Docs-only changes are a poor fit for this schema.** The
  [intent-driven schema README](../openspec/schemas/intent-driven/README.md)
  lists docs-only changes as not a good fit. Record design work inside a
  real change (design and ADR are first-class stages) with implementation
  explicitly deferred to follow-up changes, or start with
  `/opsx-explore` for design exploration that has not committed to a
  change.
- **Spec format is owned by the specs stage.** Prompt authoring supplies
  actor, rules, and scope; the specs stage decides the wrapping (OpenSpec
  markdown delta headers, Gherkin fencing, acceptance-test extraction).
