# Upstream Gating Protocols

This file defines the gate protocols for features, specs, and plans — the cards
that are developed synchronously (human + agent) before autonomous task execution.
These gates operate upstream of the task review kernel (`review-kernel.md`).

## Development Sequence

```
Feature (sync) → Spec (sync) → Plan (sync) → Tasks (autonomous)
```

Each card must be complete enough at its level to unambiguously drive the next.
A feature that leaves the spec author guessing about scope produces a bad spec.
A spec that leaves the plan author guessing about behavior produces a bad plan.
A plan that leaves task executors guessing about what to do produces confabulated
work — the agent fills in plausible text because the plan didn't specify real work.

## Language Convention

Use RFC 2119 normative language:

| Term | Meaning |
|------|---------|
| MUST | Non-negotiable requirement. Failure is a gate failure. |
| MUST NOT | Non-negotiable prohibition. Violation is a gate failure. |
| SHOULD | Strong recommendation. Omission requires an explicit justification. |
| SHOULD NOT | Strong discouragement. Inclusion requires an explicit justification. |
| MAY | Optional. No justification needed either way. |

---

# Feature Gate

A feature is the highest-level planning unit. It captures the problem, scope,
vocabulary, and success criteria at a level that unambiguously drives spec
authorship.

## Feature Gating Checklist

Apply these gates in order. Stop at the first failure.

### Gate F1: Problem Statement

The feature MUST state:

- **What problem it solves.** Not "build X" — "users can't do Y, this feature
  enables Y by building X."
- **Who the users are.** A feature that serves no identifiable user is a
  solution looking for a problem.
- **Why now.** What changed that makes this feature feasible or urgent now, as
  opposed to six months ago or six months from now?

The problem statement SHOULD be 2-4 paragraphs. A one-sentence problem
statement is usually underspecified. A ten-paragraph problem statement is
usually unprioritized brainstorming.

### Gate F2: Scope Boundaries

The feature MUST define what is in scope and what is explicitly out of scope.

- In-scope: what the feature delivers. Concrete nouns and verbs, not
  abstractions like "improve the developer experience."
- Out-of-scope: things that are related, tempting, adjacent, or common
  follow-up work, but NOT part of this feature.

A feature without explicit non-goals invites scope creep during spec
authorship. The spec author will include "nice to have" behaviors because
the feature didn't say not to.

### Gate F3: Key Vocabulary

The feature MUST identify the key mathematical or technical nouns that
the feature introduces or depends on. This is not the full domain model
(that belongs in the spec). It is the vocabulary list that tells the spec
author: "you will need to define these things precisely."

For each key noun, state:

- **What it is** (one sentence — the spec will define it properly)
- **Whether it already exists in the project** or is new
- **What it depends on** (other nouns, features, or external systems)

### Gate F4: Success Criteria

The feature MUST define success criteria that are:

- **Observable**: someone can look at the deliverable and determine whether
  the criterion is met without asking the feature author.
- **Falsifiable**: it is possible to fail. "The system is correct" is not
  falsifiable. "All 47 spec methods pass their respective category-obligation
  examples" is.
- **Feature-level**: criteria describe the completed feature, not individual
  tasks within it.

Success criteria MUST NOT be acceptance criteria for individual tasks or
specs. Those belong at lower levels.

### Gate F5: Dependencies and Blockers

The feature MUST declare:

- **Depends on**: other features, external systems, upstream work, or
  prerequisite decisions that must be complete before this feature can
  start or complete.
- **Blocks**: features or work that depend on this feature. Knowing what
  is waiting helps prioritize.

### Gate F6: Link to Specs

The feature MUST list the specs it will produce. At minimum, each planned
spec should have a provisional title and a one-line description of its scope.

If the feature does not yet know what specs it needs, the feature is not
ready for spec authorship — it needs more problem analysis.

## Feature Gate Outcomes

| Outcome | Meaning |
|---------|---------|
| **Pass** | Feature is ready to begin spec authorship. Proceed to spec gate. |
| **Revision required** | Feature fails one or more gates. Rework and re-gate. |
| **Blocked** | Feature cannot proceed because an external dependency is unresolved. Create the dependency card. |

---

# Spec Gate

A spec is the detailed behavioral contract. It defines input→output behaviors,
E2E workflows, error conditions, invariants, and the domain model at a level
that unambiguously drives plan authoring.

The canonical reference for spec quality is the [Symphony SPEC.md](https://github.com/openai/symphony/blob/main/SPEC.md).
Not every spec needs that level of detail, but every spec should aspire to the
same structural clarity: problem statement, goals/non-goals, domain model,
component contracts, state machines, invariants, and edge cases.

## Spec Gating Checklist

### Gate S1: Domain Model

The spec MUST define the key entities with enough precision that a plan
author can determine what needs to be built.

For each entity:

- **Name and type**: is it a class, a function, a category, a data structure,
  a configuration value?
- **Fields/properties**: what data does it carry? What are the types?
- **Relationships**: how does it connect to other entities?
- **Lifecycle**: how is it created, modified, and destroyed?

### Gate S2: Behavioral Contracts

The spec MUST define input→output contracts for every significant behavior.
These are the spec's "API" — the contracts that implementation must satisfy
and tests must verify.

For each behavior:

- **Inputs**: types, preconditions, required data
- **Outputs**: types, postconditions, guarantees
- **Error conditions**: what happens when inputs violate preconditions?
- **Side effects**: what state changes, file writes, network calls?

A spec with fewer than 5 explicit behavioral contracts is usually
underspecified. A spec where every contract is "TBD" is not a spec.

### Gate S3: E2E Workflows

If the feature involves sequences of operations (not just isolated function
calls), the spec MUST describe at least one representative end-to-end
workflow from start to finish.

The workflow MUST cover:

- How the user initiates the workflow
- Each step the system takes
- The expected outcome
- What happens if any step fails

This is how the plan author understands what orchestration is needed.
Without E2E workflows, the plan will decompose into isolated tasks that
don't compose.

### Gate S4: Invariants and Guarantees

The spec MUST state what properties the system guarantees at all times,
and what properties it guarantees at specific points (pre/post conditions).

Invariants are the spec's strongest claims. They tell the plan author:
"whatever you build, it must preserve these properties." They tell the
task executor: "whatever you implement, these assertions must hold."

### Gate S5: Edge Cases and Error Handling

The spec SHOULD address common edge cases:

- Empty inputs, null inputs, boundary values
- Concurrent or overlapping operations
- Resource exhaustion (memory, disk, network)
- Version skew or incompatible data

A spec that addresses zero edge cases is not necessarily a gate failure,
but it shifts risk downstream: the plan author will have to guess, and
the implementer will have to guess again. Address edge cases at the
earliest practical level.

### Gate S6: Non-Goals

The spec MUST explicitly state what it does NOT cover, parallel to the
feature's non-goals but at a more granular behavioral level. This prevents
the plan author from including work that the spec intentionally excludes.

### Gate S7: Acceptance Criteria

The spec MUST define acceptance criteria that are falsifiable and
observable. These are the criteria against which the completed
implementation will be judged.

## Spec Gate Outcomes

| Outcome | Meaning |
|---------|---------|
| **Pass** | Spec is ready to begin plan authoring. Proceed to plan gate. |
| **Revision required** | Spec fails one or more gates. Rework and re-gate. |
| **Blocked** | Spec requires a decision or external input before it can proceed. |

---

# Plan Gate

A plan decomposes a spec into executable phases and tasks. It is the final
human+agent artifact before autonomous execution. Once a plan is approved,
task cards are created and executed by agents without further human input.

**The critical invariant**: a plan MUST contain zero "unresolved," "TBD,"
"decide later," or "needs investigation" language. Every question the plan
raises must be answered within the plan. If a question cannot be answered,
it must be extracted into a decision card or prerequisite research task
BEFORE the plan is approved.

## Plan Gating Checklist

### Gate P1: Phase Structure

The plan MUST decompose the spec into named phases. Each phase MUST have:

- A title that describes what the phase accomplishes
- A one-paragraph summary of the phase's scope
- A list of tasks (see Gate P2)
- Explicit success criteria (see Gate P3)
- Declared dependencies on other phases or external work

Phases SHOULD be ordered to respect dependencies. A plan with all phases
marked as parallel independent work is either trivially decomposable or
avoiding hard dependency analysis.

### Gate P2: Task Decomposition

Each phase MUST list its constituent tasks. A task is the unit of autonomous
execution. It should be:

- **Atomic enough** that one agent can complete it in one session
- **Scoped enough** that the task card can include a concrete acceptance
  criteria checklist
- **Described enough** that the task card author (who may be a different
  agent) can write the card without reading the spec

The plan MUST NOT describe each task in full detail. That is the task card's
job. The plan describes the task's purpose and boundaries; the task card
provides the execution contract.

For each task in the plan, provide:

- **Title**: what the task does (one line)
- **Scope**: what the task covers and DOES NOT cover (2-4 sentences)
- **Dependencies**: which other tasks or phases must complete first

### Gate P3: Phase Success Criteria

Each phase MUST have success criteria that are:

- **Observable**: a reviewer can check them after phase completion
- **Phase-scoped**: they describe the completed phase, not individual tasks
- **Cumulative**: later phases build on earlier success; criteria should
  not be redundant across phases unless the later phase genuinely re-verifies

### Gate P4: No Unresolved Language

The plan MUST NOT contain any of the following:

- "TBD," "to be determined," "to be decided"
- "Needs investigation," "requires research," "needs more thought"
- "Option A or Option B" without a resolution
- "We will figure this out during implementation"
- "The implementer should decide..."

If a question genuinely cannot be resolved during planning, it MUST be
extracted into:

- A **decision card** (if the question requires a human choice between
  alternatives), OR
- A **research task** (if the question requires looking something up,
  running an experiment, or consulting a source)

The decision card or research task becomes a dependency of the phase
that needs the answer. The plan is not approved until all such cards
are resolved or accepted as unstarted blockers.

### Gate P5: Dependencies Declared

The plan MUST declare dependencies at every level:

- Phase-to-phase dependencies
- Task-to-task dependencies within a phase
- External dependencies (other plans, features, decisions, spec work)

A dependency is not the same as narrative ordering. "Phase 2 logically
follows Phase 1" is not a dependency. "Phase 2 requires the output of
Task 1.3 from Phase 1" is a dependency.

### Gate P6: Plan Acceptance Criteria

The plan itself MUST define acceptance criteria that describe when the
plan is complete (all phases finished). These are not the phase criteria
repeated — they are the plan-level criteria: what observable outcomes
indicate that the plan's objective was achieved.

### Gate P7: Autonomy Audit

Before approving the plan, conduct an autonomy audit: read through every
task description and ask:

**Could an agent with no prior context execute this task from the task
card alone?**

If the answer is no — if the task card author would need to ask clarifying
questions, read the spec, or make design decisions — then the plan is not
detailed enough. Add the necessary context to the plan or restructure the
tasks.

The test is not "could an agent produce correct output" but "could an agent
produce output that is a good-faith attempt at the right thing, without
needing to stop and ask questions."

**Declarative over imperative.** Task cards SHOULD specify success criteria
and constraints, not implementation prescriptions. "Don't tell it what to do,
give it success criteria and watch it go." An agent given a checklist of
implementation steps will follow them literally — it cannot discover a
better approach because the task card pre-empted discovery. An agent given
clear success criteria and constraints will loop until the criteria are met,
potentially finding approaches the task author did not anticipate.

The distinction:
- **Imperative** (wastes the agent): "Step 1: parse the YAML. Step 2: extract
  all category names. Step 3: find their methods. Step 4: build a dict..."
- **Declarative** (leverages the agent): "Produce a Mermaid diagram of the
  category hierarchy where each node shows the category name and the number
  of methods it introduces. Omit categories with zero methods. Output to
  `.agents/plans/visuals/category-tree-{name}.mmd`."

The imperative version assumes a specific implementation; the declarative
version gives the agent room to discover the best path. If the agent finds
a better way to gather method counts than parsing YAML, it can — and should.

**Ambiguity surfacing.** Task cards MUST resolve ambiguities explicitly.
An agent will not ask clarifying questions — it will silently guess and
produce plausible output. If a requirement could be interpreted multiple
ways, the task card must state the intended interpretation. The autonomy
audit should flag any task description where a reasonable person could
interpret the requirement differently than intended.

### Gate P8: Wrap-Up Task

Every phase MUST include a wrap-up task as its final task. The wrap-up task
covers:

- Card status audit (all cards in the phase have accurate statuses)
- Meta-review scan (`research-planning-cleanup`) on completed cards
- Skill and IWE memory updates
- Git milestone organization

The final phase of a feature additionally covers:

- Versioned release tagging
- Feature tree archival to `.agents/plans/features/completed/`
- Feature branch creation for the next feature (if applicable)

The wrap-up task depends on all other tasks in the phase and runs last.

## Plan Gate Outcomes

| Outcome | Meaning |
|---------|---------|
| **Pass** | Plan is ready for autonomous task card authoring and execution. |
| **Revision required** | Plan fails one or more gates. Rework and re-gate. |
| **Blocked** | Plan requires an external decision, research result, or prerequisite before it can proceed. |

---

# Gate Protocol for Cards Without Phases

Some plans are standalone — they don't decompose into phases. These plans
are effectively their own phase and task combined. For such plans:

- The plan body MUST satisfy the Plan Gate requirements (especially P4:
  no unresolved language)
- The plan MUST include a wrap-up section covering the standard wrap-up
  responsibilities (card audit, meta-review, skill/memory updates, git
  organization)
- If the plan is the final item in a feature, the wrap-up MUST include
  feature release steps

---

# Cross-References

- **Task-level review**: `review-kernel.md` — the six ordered gates for
  individual task cards.
- **Execution state machine**: `execution-kernel.md` — the full plan-to-
  execution lifecycle.
- **Planning cleanup**: `research-planning-cleanup` — the meta-review
  protocol for post-hoc scanning of completed cards.
- **Jerry-behaviour**: `jerry-behaviour` — detection of self-referential
  validation, checklist theater, and paraphrase-as-review in agent outputs.
