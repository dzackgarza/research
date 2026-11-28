# Auto-Research State Machine for Mathematical Agents

## Constitutional layer

The previous draft had too much process surface.
This section states the hard invariants that prevent agents from satisfying procedure
while evading the mathematical burden.
The state machine is subordinate to these invariants.
If any procedural rule conflicts with them, the procedural rule loses.

### C1. No procedural act has mathematical force

No review, audit, signoff, checklist, bundle assembly, archive step, or status
transition can by itself increase epistemic status.
Only the underlying mathematical objects matter: theorem statement, proof, exact
computation, certificate, counterexample, dependency ledger, and replayable artifacts.

### C2. Closure is only by goal discharge

A `GOAL.md` item is not completed because tasks were executed or because local subtasks
were all closed. It is completed only if one of the following exists and is tied
explicitly to that goal item:

* a rigorous proof of the target statement,
* a rigorous proof of a strictly stronger statement,
* an explicit refutation / counterexample,
* an explicitly labeled conjectural package whose status is non-theorem and whose
  relation to the goal is stated exactly.

### C3. No post hoc narrowing of the claim

The claim under attack must be fixed before implementation.
An agent may not fail on the original claim and then silently restate a weaker claim
that happens to be true.
Any weakening, strengthening, or reformulation creates a new task or a formally revised
task contract, with the delta recorded.

### C4. Hidden major work invalidates the task boundary

If a task contains an undeclared major theorem, algorithm, classification,
infrastructure build, or convention choice, then the task boundary was invalid.
The work must return to planning.
The agent may not treat that hidden major work as an implementation detail.

### C5. Exact computation has no inferential surplus

Exact computational evidence proves only the exact finite statement it directly
computes, plus whatever rigorous reduction theorem already exists.
It does not by itself justify a universal theorem, a classification statement, or a
structural explanation.

### C6. Failed proof attempts do not automatically become conjectures

A failed theorem attempt is discarded unless there is an independently meaningful
conjectural claim, already tied to `GOAL.md` or to an explicit extension, for which the
retained exact evidence is genuinely relevant.
Conjecture status is not a salvage bucket.

### C7. Independence must be semantic, not organizational

Two agents are not independent merely because they are different runs or different
roles. If they share the same hidden premise, same unaudited code path, same invented
construction, or same copied proof skeleton, the confirmation is not independent.

### C8. The trusted base must be explicit

Any code, lemma, convention, reduction theorem, classification theorem, or standard
construction used by a task belongs either:

* to the explicit trusted base, or
* to the current task's own proof burden.
  There is no third category called "obvious background" that agents may freely invent.

### C9. Unresolved obligations are terminally blocking

A single unresolved theorem-level obligation blocks theorem acceptance.
It is not diluted by the number of discharged obligations, the length of the derivation,
or the amount of computational evidence.

### C10. Adversarial review must target the strongest claimed result

The central audit question is not "is something here correct?"
but "is the strongest claim actually made justified exactly as stated?"
Any mismatch between claimed result and established result is a failure at the stronger
claim.

### C11. Reuse requires exact provenance

No artifact may be reused downstream unless its exact statement, assumptions, versioned
dependencies, and status are all explicit.
Archived ambiguity is contamination.

### C12. Drift is failure

Work that does not discharge a `GOAL.md` item, a declared prerequisite, or a declared
extension is drift, even if the mathematics is correct.

## Institutional layer

The state machine below is merely one possible institution for enforcing the
constitutional layer above.
The institution should be kept thin.
Its only role is to force explicit claim-fixing, isolate work, demand adversarial
attack, and prevent unaudited reuse.

## Structural loopholes and mandatory repairs

The main remaining attack surfaces are the ones where an adversarial agent can control
semantics while complying with artifact process.
The machine must therefore add the following mandatory controls.

### R1. Parent-sufficiency map

Every `task.md` must include a formal sufficiency map to its parent `GOAL.md` item or
parent task. This map must state exactly what portion of the parent burden is discharged
if the task succeeds, and what obligations remain.
A task with no compelling sufficiency map is invalid.

### R2. Independent obligation extraction

The obligation ledger for a theorem-level claim may not be author-controlled.
An independent extractor or auditor must generate, or at minimum independently check,
the set of claim-critical obligations directly from the theorem statement and proof
artifact. Completeness is measured against the theorem, not just against the author's
ledger.

### R3. Trusted-base admission is a separate high-burden process

`trusted_references.md`, `accepted_algorithms.md`, conventions files, and shared helper
code may not be extended by ordinary task execution.
Admission of a new trusted-base item requires its own artifact stating:

* exact admitted item,
* exact scope of what future tasks may assume from it,
* justification for trust,
* limits of validity,
* affected downstream tasks.

### R4. Claim-surface alignment

The strongest claim effectively made anywhere must be treated as the claim under review.
Theorem statement, task title, prose summary, filenames, archive tags, dependency
labels, and downstream use must all agree.
Any stronger implication on any surface counts as the operative claim.

### R5. Reduction ledger

Whenever exact computation supports a broader conclusion, there must be a reduction
ledger stating exactly which rigorous theorem lifts the computed finite statement to the
broader claim.
Without such a ledger, the computation has no inferential force beyond the
finite statement directly checked.

### R6. Verifier diversity, not replay alone

Replay is only reproducibility of one pipeline.
For high-risk tasks, theorem-level acceptance requires verifier diversity: independent
proof extraction, independent certificate checking, or independent computational
cross-checks whose failure modes are not shared by construction.

### R7. No proof-burden laundering by task type

A theorem-level burden may not be decomposed into a chain of computation-only,
infrastructure-only, or documentation-only tasks unless an explicit reduction ledger
shows how those tasks, together with already-proved reductions, discharge the original
theorem-level claim.

### R8. Final composed-goal audit

A `GOAL.md` item may not be marked discharged by composing archived local results
without a final composed-goal audit.
That audit must check whether the exact target statement follows from the exact archived
dependencies with all assumptions and statuses preserved.

### R9. Hidden-major-work test must be externalized

A task boundary is invalid if it hides a missing theorem, missing algorithm, missing
classification, missing convention choice, or missing infrastructure of comparable
difficulty to the nominal task.
The classification of such work as "major" may not be left to the implementing agent
alone; it must be part of pre-audit.

### R10. Replan monotonicity

Repeated `REPLAN_REQUIRED` transitions are acceptable only if they produce a measurable
reduction of the original burden: clarified claim, split hidden major work into explicit
tasks, fixed trusted-base scope, or discharged a parent prerequisite.
Replan churn without burden reduction is failure.

### R11. Base-insufficiency escalation is mandatory

If faithful execution of a task reveals that the shared semantic base is insufficient,
the task boundary was invalid. This is not an implementation detail and may not be
patched locally inside the task.

The insufficiency is real if any of the following occurs:

* the task needs a new shared noun, method, morphism, coercion, or interop bridge in
  order to express its mathematics cleanly;
* the task is forced into repeated raw matrix/vector/quadratic-module manipulation
  because the semantic base cannot state the operation at the right mathematical level;
* the agent is tempted to add a free function whose primary argument is a lattice,
  lattice element, discriminant group, or morphism, and the correct design would attach
  that verb to the noun instead;
* the same foundational convention or exact operation is being reinvented across tasks
  rather than admitted once into the trusted base;
* most of the work has become redesign of foundations rather than discharge of the
  stated task burden.

When this happens, the implementing subagent must:

* stop implementation immediately and surface the insufficiency as blocking;
* mark the current task `REPLAN_REQUIRED` rather than continuing with local helpers or
  wrappers;
* split the hidden work into at least:
  * a trusted-base task that freezes the exact new noun/method/convention/interop
    burden, and
  * a redesigned dependent task that states exactly how it will use the repaired base;
* refuse to resume the dependent task until the base task has its own exact contract,
  replay route, and acceptance surface.

A subagent may not hide base insufficiency by:

* adding ad hoc helper functions in the task worktree,
* laundering new fundamentals through "just this task" glue,
* silently broadening the shared base during implementation, or
* pushing foundational redesign into audit or cleanup work after code already exists.

## Objective

Given a user-provided `GOAL.md` containing high-level research goals, maintain a
zero-trust research pipeline whose only acceptable outputs are:

1. fully rigorous mathematical proofs, or
2. explicitly labeled conjectures supported by substantial, numerically exact,
   reproducible computational evidence,

answering the questions in `GOAL.md` or tightly justified extensions of them.

The pipeline must reject confabulation, fabricated algorithms, partial proofs presented
as proofs, heuristic computation presented as exact computation, ill-defined tasks, and
any unaudited dependency being silently treated as trusted.

* * *

## Core principles

### 1. Zero-trust by default

Every mathematical assertion, algorithmic claim, computed value, classification result,
reduction step, and proof dependency is treated as untrusted until independently
attacked and its specific obligations are discharged by explicit evidence.

### 2. No stamp-of-approval state

There is no terminal notion of approval by label alone: not `validated`, not `audited`,
not `reviewed`, not `checked`.

An audit report is only an attack artifact.
It never certifies success by itself.

A task may advance only by producing a concrete acceptance bundle whose required
components are fully present.
For a theorem-level result, that means a theorem bundle.
For conjectural work, that means a conjecture-evidence bundle.
A bare statement such as "audit passed" has no state-transition force.

### 3. No partial-credit completion

Incomplete, partial, or incorrect attempts do not transition to success.
They transition to one of:

* `REPLAN_REQUIRED`
* `REJECTED`
* `QUARANTINED`
* `CONJECTURE_TRIAGE`

### 4. Exactness requirement for computation

Computational evidence must be numerically exact, reproducible, and mathematically
interpretable.
No floating approximations unless the task explicitly permits them and the
interpretation is formally controlled.
No bounded search may be presented as proof of a universal statement.

### 5. Scope discipline

A task must not smuggle in an unplanned research program.
If a task statement hides a major algorithmic problem, missing infrastructure, missing
conventions, or undefined objects, it is kicked back to planning.

### 6. Local grounding requirement

All task definitions must be grounded in locally available material: `GOAL.md`, project
notes, local source documents, audited library code, established conventions files, and
explicit dependencies.
Agents may not invent missing definitions, constructions, algorithms, or conventions.

### 7. Isolation of work

Every implementation attempt occurs in an isolated branch or worktree with a bounded
file scope. Collateral edits outside the approved scope are audited as possible
contamination.

### 8. Independence where possible

Critical code, tests, derivations, and audits should be independently produced by
distinct agents or distinct runs.
Single-path confirmation is insufficient for high-risk steps.

* * *

## Artifact model

Each task has a directory with immutable records.

```text
research/
  GOAL.md
  conventions/
    objects.md
    notation.md
    accepted_algorithms.md
    trusted_references.md
  tasks/
    T-XXXX/
      task.md
      provenance.md
      scope.yml
      assumptions.md
      dependencies.md
      plan.md
      implementation/
      proofs/
      computations/
      audit/
      outcomes/
      archive/
```

### Required artifacts per task

* `task.md`: precise statement, origin in `GOAL.md`, target deliverable, acceptance
  criteria.
* `scope.yml`: allowed files, allowed modules, allowed outputs, required isolation
  strategy.
* `assumptions.md`: all mathematical assumptions, conventions, and ambient objects.
* `dependencies.md`: prerequisite lemmas, algorithms, code modules, references.
* `plan.md`: decomposition into auditable subtasks.
* `implementation/`: code and derivations produced during execution.
* `proofs/`: formal proof text or proof skeletons with exact dependency references.
* `computations/`: exact scripts, logs, certificates, raw outputs, reproducibility
  instructions.
* `audit/`: pre-audit reports, adversarial audit reports, fraud findings, replay checks.
* `outcomes/`: theorem, conjecture, rejection, quarantine record.
* `archive/`: finalized bundle with hashes and provenance.

* * *

## State machine overview

```text
GOAL_INGEST
  -> GOAL_EXPANSION
  -> TASK_SELECTION
  -> TASK_SPECIFICATION
  -> PRE_AUDIT
      -> IMPLEMENT
      -> REPLAN_REQUIRED
      -> REJECTED
  IMPLEMENT
      -> SELF_CHECK
      -> REPLAN_REQUIRED
      -> QUARANTINED
  SELF_CHECK
      -> ADVERSARIAL_AUDIT
      -> REPLAN_REQUIRED
      -> QUARANTINED
  ADVERSARIAL_AUDIT
      -> ACCEPTANCE_BUNDLE_ASSEMBLY
      -> CONJECTURE_TRIAGE
      -> REPLAN_REQUIRED
      -> REJECTED
      -> QUARANTINED
  CONJECTURE_TRIAGE
      -> ACCEPTANCE_BUNDLE_ASSEMBLY
      -> IMPLEMENT
      -> REJECTED
  ACCEPTANCE_BUNDLE_ASSEMBLY
      -> THEOREM_ACCEPT
      -> CONJECTURE_ACCEPT
      -> REPLAN_REQUIRED
      -> REJECTED
      -> QUARANTINED
  THEOREM_ACCEPT
      -> DOCUMENT
      -> ARCHIVE
  CONJECTURE_ACCEPT
      -> DOCUMENT
      -> ARCHIVE
  DOCUMENT
      -> ARCHIVE
  ARCHIVE
      -> TASK_SELECTION
```

A task may move backward multiple times.
Planning and implementation are allowed to oscillate.
No forward transition bypasses adversarial audit.
Audit itself is not an approval state.

* * *

## 0. `GOAL_INGEST`

### Purpose

Parse `GOAL.md` into explicit research targets.

### Inputs

* `GOAL.md`
* trusted conventions / references already present locally

### Outputs

* list of candidate goal items with IDs
* dependency graph at coarse granularity
* list of ambiguous or underspecified goals requiring expansion

### Entry conditions

* `GOAL.md` exists

### Exit conditions

* every sentence in `GOAL.md` is classified as one of:

  * theorem/proof goal
  * classification/computation goal
  * conjecture/evidence goal
  * exposition/documentation goal
  * future/optional extension
  * ambiguous/needs expansion

### Failure transitions

* if a goal cannot be parsed into a mathematical target, mark it `AMBIGUOUS_GOAL` and
  send to `GOAL_EXPANSION`

* * *

## 1. `GOAL_EXPANSION`

### Purpose

Expand high-level goal items into long-term task trees across four mandatory tiers.

### Task tier taxonomy

Every goal expansion must classify candidate tasks into one of four numbered tiers.
The tier prefix is part of the task ID: `T-0XXX`, `T-1XXX`, `T-2XXX`, `T-3XXX`.

#### Tier 0 — Tool construction (`T-0XXX`)

These tasks centralize and formalize all nontrivial algorithms that higher-tier tasks
depend on into shared functions, classes, wrappers, and reusable modules.
They do **not** solve any mathematical problem.
They build the toolkit that T-3 tasks will apply and combine.
Each T-0 task must specify:

* the exact algorithm or mathematical operation being wrapped,
* the input/output contract (types, exactness requirements, edge cases),
* which T-3 tasks will consume this tool,
* the isolation strategy so tool code does not become entangled with task-specific logic.

Examples: `is_primitive()`, discriminant form evaluators, lattice embedding constructors,
orbit enumeration engines, Gram matrix builders, involution matrix generators.

#### Tier 1 — Fixture discovery (`T-1XXX`)

These tasks search the existing repo-local literature, references, and known results for
concrete fixtures with pre-computed invariants that can serve as sanity-check data for
tool correctness.
They do **not** verify correctness themselves.
They assemble the reference data that T-2 assertion gates will check against.
Each T-1 task must specify:

* the source (paper, theorem, known example) providing the fixture,
* the exact invariant values or structural properties expected,
* which T-0 tools the fixture is intended to test,
* provenance chain back to the original reference.

Examples: known $(r,a,\delta)$ invariants for specific lattices, published Gram matrices,
verified orbit counts, established embedding indices.

#### Tier 2 — Assertion gates (`T-2XXX`)

These tasks write assertion functions, test harnesses, and validation gates that T-3
tasks **must** pass before their results are accepted.
They rely on T-0 shared tools and T-1 fixture data.
They do **not** solve mathematical problems.
They define the correctness criteria that T-3 outputs must satisfy.
Each T-2 task must specify:

* the exact property being asserted (e.g., primitivity, signature match, orbit count),
* which T-0 tool implements the check,
* which T-1 fixtures provide the expected values,
* the failure mode (what happens when a T-3 task fails the gate).

Examples: `assert_primitive()`, `assert_signature()`, `assert_orbit_count()`,
`assert_discriminant_form()`, replay-and-compare harnesses.

#### Tier 3 — Mathematical application (`T-3XXX`)

These tasks apply and combine existing T-0 tools, validated by T-2 gates, against
T-1 fixtures and new mathematical targets to produce proofs, computations, or
conjectural evidence answering `GOAL.md` items.
They are the only tier that may produce mathematical results.
Each T-3 task must specify:

* which T-0 tools it uses,
* which T-2 gates it must pass,
* which T-1 fixtures it validates against (if any),
* the exact mathematical claim or computation target.

### Required actions

* map each goal item to explicit mathematical questions
* distinguish proof targets from computational infrastructure targets
* identify latent research programs hidden inside single lines
* extract prerequisite objects, algorithms, references, and conventions
* separate core goals from natural extensions
* **classify every candidate into its correct tier before specification**
* **identify every algorithm that a T-3 task depends on and promote it to a T-0 task**
* **identify every known fixture that can validate a tool and promote it to a T-1 task**
* **identify every correctness gate a T-3 result must pass and promote it to a T-2 task**

### Output

A backlog of task candidates, each with:

* exact objective
* tier label (0 / 1 / 2 / 3)
* justification from `GOAL.md`
* dependencies (including cross-tier dependencies)
* risk level
* expected deliverable type: theorem / exact computation / conjecture evidence /
  documentation / shared tool / fixture data / assertion gate

### Rejection rule

A task candidate is invalid if it cannot be tied either:

* directly to `GOAL.md`, or
* to a necessary prerequisite of a `GOAL.md` item, or
* to a natural extension explicitly justified in writing

### Tier integrity rules

* A T-3 task may **not** implement an algorithm that should be a T-0 shared tool.
  Any nontrivial algorithm discovered during T-3 planning must be split into a T-0 task.
* A T-0 task may **not** attempt to solve a mathematical problem.
  Its deliverable is a reusable function, class, or module — not a theorem or computation.
* A T-2 task may **not** be skipped for any T-3 task.
  Every T-3 task must have at least one T-2 gate it must pass.
* A T-3 task may not advance to IMPLEMENT until its required T-0 tools and T-2 gates
  are at minimum in PRE_AUDIT, and its T-1 fixtures are identified.

### Tier integrity rules

* A T-3 task may **not** implement an algorithm that should be a T-0 shared tool.
  Any nontrivial algorithm discovered during T-3 planning must be split into a T-0 task.
* A T-0 task may **not** attempt to solve a mathematical problem.
  Its deliverable is a reusable function, class, or module — not a theorem or computation.
* A T-2 task may **not** be skipped for any T-3 task.
  Every T-3 task must have at least one T-2 gate it must pass.
* A T-3 task may not advance to IMPLEMENT until its required T-0 tools and T-2 gates
  are at minimum in PRE_AUDIT, and its T-1 fixtures are identified.

* * *

## 2. `TASK_SELECTION`

### Purpose

Choose a subset of task candidates to activate and enforce tier execution order.

### Tier execution order

Tasks must be activated in tier order.
A task in tier N may not enter IMPLEMENT until the prerequisite tasks in tiers 0..N-1
that it depends on have passed their own gates.

* **T-0 (Tools)**: activated first. No tier dependencies.
* **T-1 (Fixtures)**: activated in parallel with T-0. No tier dependencies.
* **T-2 (Gates)**: activated after required T-0 tools exist and T-1 fixtures are identified.
* **T-3 (Math)**: activated only after required T-0 tools, T-1 fixtures, and T-2 gates
  are at minimum specified and in PRE_AUDIT.

### Selection criteria

* prerequisite readiness
* availability of trusted algorithms and local source material
* isolation feasibility
* auditability of output
* dependency pressure from higher-priority goals
* **tier readiness**: no T-3 task selected before its T-0/T-1/T-2 dependencies are ready

### Output

Activated tasks `T-NXXX` where N is the tier digit (0, 1, 2, or 3).

### Constraint

A selected task must be small enough to have unambiguous acceptance criteria, but not so
small that it reduces to meaningless clerical motion.

* * *

## 3. `TASK_SPECIFICATION`

### Purpose

Convert an activated task into an executable, auditable contract.

### `task.md` must contain

1. **Origin**: exact lines or items from `GOAL.md`.

2. **Objective**: formal statement of what is to be established or computed.

3. **Deliverable type**:

   * rigorous proof,
   * exact computation with certificate,
   * conjecture with exact evidence,
   * infrastructure prerequisite.

4. **Acceptance criteria**.

5. **Non-goals**.

6. **Allowed dependencies**.

7. **Required conventions and object definitions**.

8. **Failure conditions**.

### Example acceptance criteria for a proof task

* theorem statement is formal and unambiguous;
* every nontrivial step is proved or cited from locally trusted references;
* no proof step relies on bounded search for universal statements;
* all computations used in proof are exact and replayable;
* all referenced code is pinned and auditable.

### Example acceptance criteria for an exact computation task

* object to compute is formally defined;
* algorithm is specified or already available in trusted code;
* output is exact;
* reproduction from clean environment yields identical result;
* certificate or independent cross-check exists.

* * *

## 4. `PRE_AUDIT`

### Purpose

Determine whether the task is well-defined, scoped correctly, and executable using
trusted local resources.

This is the gate that prevents an agent from being asked to solve an ill-posed or
hidden-major-problem task.

### Questions the pre-audit must answer

1. Is the task mathematically well-defined?
2. Are all objects, conventions, and ambient assumptions fixed?
3. Is the task specifically tied to `GOAL.md` or an explicit prerequisite?
4. Are acceptance criteria objective and unambiguous?
5. Does the task hide a major undeclared algorithmic problem?
6. Are the necessary algorithms already available and audited, or is creating them
   itself a separate task?
7. Are all dependencies local and available?
8. Is the task file scope bounded and isolation feasible?
9. Is there a plausible exact verification path?

### Automatic kickback conditions

Return to `REPLAN_REQUIRED` if any of the following hold:

* undefined objects or conventions;
* task statement contains compressed research problems disguised as substeps;
* required algorithms are unavailable, unaudited, or only vaguely described;
* acceptance criteria are subjective;
* the task depends on invented facts or unstated standard constructions;
* the task cannot be checked exactly;
* the task is not actually connected to a `GOAL.md` objective.

### Automatic rejection conditions

Transition to `REJECTED` if:

* the task is mathematically incoherent,
* the task duplicates a completed archived result without justified extension,
* the task asks for a proof of a claim already known locally to be false.

### Output

A signed pre-audit report containing:

* precise pass/fail findings,
* missing prerequisites,
* split suggestions if the task was hiding multiple research problems,
* scope fixes,
* audit plan for the implementation state.

* * *

## 5. `IMPLEMENT`

### Purpose

Carry out the task in isolated workspaces using subagents.

### Required execution rules

1. Implementation happens only after pre-audit pass.

2. Every worker runs in an isolated branch or worktree.

3. Every worker receives:

   * exact task contract,
   * allowed file set,
   * dependencies,
   * conventions,
   * explicit prohibitions.

4. No worker may modify unaudited shared core code unless the task explicitly covers it.

5. No produced code becomes an input to later tasks until it passes the later gates.

6. No claim may be elevated from computation to theorem unless a theorem bundle is
   eventually assembled.

### Delegation pattern

A task may be split into subagents such as:

* proof search / derivation agent,
* exact computation agent,
* code implementation agent,
* reference extraction agent,
* test / certificate generation agent,
* red-team falsification agent.

### Required prohibitions

Workers must not:

* claim proof by finite sampling or partial enumeration;
* replace a derived quantity by a constant or asserted equality;
* rely on numerics where exact arithmetic is required;
* use undefined invariants or false classification statements;
* silently broaden scope;
* silently change conventions;
* edit files outside `scope.yml`.

### Required intermediate products

* derivation notes with dependency citations;
* code with exact arithmetic where required;
* raw logs;
* certificates / witness objects;
* explicit unresolved blockers.

### Transition rules

* If new hidden prerequisites are discovered, go to `REPLAN_REQUIRED`.
* If suspected fraud, confabulation, or collateral damage appears, go to `QUARANTINED`.
* Otherwise continue to `SELF_CHECK`.

* * *

## 6. `SELF_CHECK`

### Purpose

A non-author agent performs a first-pass consistency and completeness check before
adversarial audit.

### Required checks

* deliverable matches task contract;
* all files modified are within scope;
* all claimed results are present in artifacts;
* all referenced lemmas / code / computations exist;
* exact reproducibility was attempted;
* there are no unresolved placeholders, TODOs, mocked constants, or fake
  implementations;
* theorem vs conjecture status is correctly labeled.

### Output

A structured checklist, not a narrative approval.

### Transition rules

* pass -> `ADVERSARIAL_AUDIT`
* missing prerequisites or missing artifacts -> `REPLAN_REQUIRED`
* fraud indicators -> `QUARANTINED`

* * *

## 7. `ADVERSARIAL_AUDIT`

### Purpose

Try to break the result.

This state is not a formality.
Its job is to falsify, narrow, or downgrade the claimed result unless the claim survives
hostile examination.

### Important restriction

`ADVERSARIAL_AUDIT` does **not** output a certificate of correctness.
It outputs only attack records, replay results, counterexample attempts, failed
obligations, and any surviving unresolved issues.
It is a destructive filter, not a positive approval state.

### Audit dimensions

#### A. Mathematical soundness

* Are all definitions fixed?
* Is each inference justified?
* Are there hidden appeals to unproved claims?
* Does the claimed theorem exceed what was actually established?
* Was any universal statement inferred from bounded search?
* Are edge cases treated?
* Are algebraic invariants used correctly?
* Are classification theorems stated with the right hypotheses?

#### B. Computational soundness

* Does the code compute the defined object?
* Is arithmetic exact where required?
* Can independent reimplementation or cross-check reproduce the result?
* Are certificates independently checked?
* Is there dead code, branch poisoning, constant substitution, or assertion abuse?

#### C. Scope and provenance

* Is the result actually tied to `GOAL.md`?
* Were conventions changed midstream?
* Did the agent modify unrelated files?
* Does the artifact rely on unaudited shared code?

#### D. Fraud and confabulation signals

* invented citations or references,
* invented algorithms,
* appeals to standard facts not locally grounded,
* proof text inconsistent with code,
* code returning constants or tautologies,
* proofs with missing quantified steps disguised as prose,
* placeholders presented as completion.

### Required audit methods

* replay from clean checkout,
* differential review of branch/worktree,
* exact output comparison,
* independent symbolic or algebraic spot checks,
* attempt explicit counterexamples,
* independent proof outline reconstruction,
* dependency graph audit,
* hash audit of trusted code inputs.

### Output

An adversarial audit produces an **attack bundle**, not a pass/fail stamp.
The bundle must contain:

* list of claims under review,
* list of obligations attacked,
* concrete attack attempts,
* replay transcript,
* counterexample search transcript,
* dependency-integrity findings,
* fraud findings,
* unresolved issues list.

### Outcomes

1. `ACCEPTANCE_BUNDLE_ASSEMBLY`
2. `CONJECTURE_TRIAGE`
3. `REPLAN_REQUIRED`
4. `REJECTED`
5. `QUARANTINED`

The transition to `ACCEPTANCE_BUNDLE_ASSEMBLY` is allowed only when the attack bundle
leaves no unresolved theorem-level defect and the required evidence objects already
exist or can be assembled mechanically from existing artifacts.

* * *

## 8. `CONJECTURE_TRIAGE`

### Purpose

Handle cases where the output does not meet proof standard but may still be worth
retaining as conjectural evidence.

### Entry condition

The adversarial audit concluded:

* theorem claim failed, or was never attained,
* but exact evidence may still be substantial and non-fraudulent.

### Questions

1. Is the evidence exact and reproducible?
2. Is the claim clearly labeled conjectural everywhere?
3. Does retaining the artifact help future planning?
4. Did failure arise from missing proof steps, or from evidence that is too weak /
   irrelevant?
5. Would retrying immediately be rational, or is the artifact mainly archival evidence?

### Outcomes

* `ACCEPTANCE_BUNDLE_ASSEMBLY` if exact evidence is substantial, relevant, and properly
  labeled.
* `IMPLEMENT` if the missing gap appears locally repairable.
* `REJECTED` if the evidence is weak, irrelevant, non-exact, or misleading.

### Rule

No conjectural artifact may be cited later as if it were a theorem.
The archive format must enforce this distinction.

* * *

## 9. `ACCEPTANCE_BUNDLE_ASSEMBLY`

### Purpose

Assemble the concrete objects required for downstream trust.
This replaces any notion of a bare approval state.

### Rule

Nothing is accepted because an auditor says "looks correct".
Acceptance exists only if the relevant bundle is complete.

### Theorem bundle requirements

A theorem-level result must contain all of:

1. exact theorem statement;
2. explicit assumptions and conventions ledger;
3. proof artifact with every dependency cited or discharged locally;
4. obligation ledger listing each nontrivial step and where it is discharged;
5. exact computation certificates for any computational subclaims;
6. replay transcript from clean environment;
7. independent attack bundle from adversarial audit;
8. independent cross-check object if required by task risk policy;
9. empty unresolved-issues list.

### Conjecture-evidence bundle requirements

A conjectural result must contain all of:

1. exact conjecture statement;
2. explicit statement that theorem status was not obtained;
3. exact domain of tested/computed evidence;
4. exact scripts and certificates;
5. replay transcript;
6. adversarial audit bundle;
7. explicit non-proof boundary;
8. empty unresolved-issues list relative to the narrower conjectural claim.

### Outcomes

* `THEOREM_ACCEPT`
* `CONJECTURE_ACCEPT`
* `REPLAN_REQUIRED`
* `REJECTED`
* `QUARANTINED`

* * *

## 10. `THEOREM_ACCEPT`

### Purpose

Promote a completed theorem bundle to theorem status.

### Required conditions

* the theorem bundle is complete;
* no unresolved issues remain;
* any required independent cross-checks are present;
* the claim under acceptance matches the proved claim exactly.

### Output

* theorem statement,
* proof document,
* obligation ledger,
* dependency index,
* reproducibility bundle,
* provenance record.

* * *

## 11. `CONJECTURE_ACCEPT`

### Purpose

Promote exact computational evidence to a conjectural research result.

### Required conditions

* theorem status explicitly denied;
* evidence exact and reproducible;
* domain of evidence precisely bounded;
* any observed patterns stated without overclaim;
* the conjecture-evidence bundle is complete.

### Output

* conjecture statement,
* exact evidence summary,
* scripts and certificates,
* explicit non-proof disclaimer.

* * *

## 12. `DOCUMENT`

### Purpose

Convert accepted outputs into research notes and internal documentation.

### Requirements

* separate theorem/proof from conjecture/evidence;
* document exact dependency chain;
* record rejected approaches only if they carry future planning value;
* state scope of validity precisely;
* include replay instructions and hashes.

### Constraint

Documentation is downstream of acceptance.
Draft expository prose is not itself evidence of correctness.

* * *

## 13. `ARCHIVE`

### Purpose

Freeze accepted or rejected task outcomes with provenance.

### Archive bundle must contain

* final task contract,
* all audit reports,
* final proof/evidence artifacts,
* code hashes,
* branch/worktree diff summary,
* dependency versions,
* outcome label.

### Outcome labels

* `ARCHIVED_THEOREM`
* `ARCHIVED_CONJECTURE`
* `ARCHIVED_REJECTED`
* `ARCHIVED_QUARANTINED`

Only theorem and conjecture archives may feed future planning, and conjectures must
remain tagged as non-theorems.

* * *

## 14. `REPLAN_REQUIRED`

### Purpose

Return a task to planning when the issue is structural rather than fraudulent.

### Typical causes

* hidden prerequisite discovered,
* task scope too large,
* task depends on unaudited algorithm,
* acceptance criteria incomplete,
* conventions not fixed,
* decomposition needs refinement.

### Required output

A delta against the current plan:

* which assumption failed,
* what prerequisite task must be added,
* whether the original task should be split, deferred, or rewritten.

* * *

## 15. `REJECTED`

### Purpose

Terminate a task attempt that does not produce a retainable result.

### Causes

* proof incorrect,
* evidence insufficient,
* task incoherent,
* scope mismatch with `GOAL.md`,
* deliverable failed essential gates.

### Rule

Rejected work does not feed downstream execution as trusted input.

* * *

## 16. `QUARANTINED`

### Purpose

Isolate contaminated work.

### Triggers

* fabricated citation/reference,
* fabricated computation,
* constant substitution for derived value,
* assertion abuse,
* unaudited shared-code dependency slipped into proof path,
* collateral edits outside scope,
* silent convention drift,
* result text inconsistent with executable artifacts.

### Required actions

* freeze branch/worktree,
* block merge / reuse,
* generate incident report,
* mark derived artifacts tainted,
* audit downstream tasks that consumed the artifact.

### Rule

Quarantined artifacts are never used as dependencies until a separate decontamination
audit clears them.

* * *

## Transition table

| From | To | Guard |
| --- | --- | --- |
| `GOAL_INGEST` | `GOAL_EXPANSION` | goal items extracted |
| `GOAL_EXPANSION` | `TASK_SELECTION` | candidate tasks available |
| `TASK_SELECTION` | `TASK_SPECIFICATION` | task activated |
| `TASK_SPECIFICATION` | `PRE_AUDIT` | task contract complete |
| `PRE_AUDIT` | `IMPLEMENT` | task well-defined, scoped, grounded |
| `PRE_AUDIT` | `REPLAN_REQUIRED` | hidden prerequisite / ambiguity / missing algorithm |
| `PRE_AUDIT` | `REJECTED` | incoherent or impossible task |
| `IMPLEMENT` | `SELF_CHECK` | execution artifacts complete |
| `IMPLEMENT` | `REPLAN_REQUIRED` | new prerequisite discovered |
| `IMPLEMENT` | `QUARANTINED` | fraud/confabulation/collateral damage indicator |
| `SELF_CHECK` | `ADVERSARIAL_AUDIT` | checklist complete |
| `SELF_CHECK` | `REPLAN_REQUIRED` | missing artifacts / unresolved blockers |
| `SELF_CHECK` | `QUARANTINED` | taint indicator |
| `ADVERSARIAL_AUDIT` | `ACCEPTANCE_BUNDLE_ASSEMBLY` | attack bundle leaves no unresolved defect and evidence objects exist |
| `ADVERSARIAL_AUDIT` | `CONJECTURE_TRIAGE` | theorem claim fails but exact evidence remains |
| `ADVERSARIAL_AUDIT` | `REPLAN_REQUIRED` | fixable structural gap |
| `ADVERSARIAL_AUDIT` | `REJECTED` | not salvageable |
| `ADVERSARIAL_AUDIT` | `QUARANTINED` | contamination/fraud |
| `CONJECTURE_TRIAGE` | `ACCEPTANCE_BUNDLE_ASSEMBLY` | retainable conjecture-evidence bundle can be assembled |
| `CONJECTURE_TRIAGE` | `IMPLEMENT` | local repair path exists |
| `CONJECTURE_TRIAGE` | `REJECTED` | evidence not worth retaining |
| `ACCEPTANCE_BUNDLE_ASSEMBLY` | `THEOREM_ACCEPT` | theorem bundle complete |
| `ACCEPTANCE_BUNDLE_ASSEMBLY` | `CONJECTURE_ACCEPT` | conjecture-evidence bundle complete |
| `ACCEPTANCE_BUNDLE_ASSEMBLY` | `REPLAN_REQUIRED` | missing evidence object or unresolved obligation |
| `ACCEPTANCE_BUNDLE_ASSEMBLY` | `REJECTED` | acceptance bundle cannot be completed |
| `ACCEPTANCE_BUNDLE_ASSEMBLY` | `QUARANTINED` | contamination found during assembly |
| `THEOREM_ACCEPT` | `DOCUMENT` | accepted |
| `CONJECTURE_ACCEPT` | `DOCUMENT` | accepted |
| `DOCUMENT` | `ARCHIVE` | artifacts bundled |
| `ARCHIVE` | `TASK_SELECTION` | next task |

* * *

## Pre-audit checklist

A task fails pre-audit unless every item is answered explicitly.

1. What exact statement/object/output is requested?
2. Which lines/items in `GOAL.md` justify the task?
3. Which conventions file fixes notation and ambient assumptions?
4. What exact deliverable type is requested?
5. What are the objective pass/fail criteria?
6. Which prerequisite theorems, algorithms, code modules, and references are required?
7. Are those prerequisites locally available and auditable?
8. Is any hidden major subproblem present?
9. Is exact verification possible?
10. What files may be changed?
11. What independent attack will later be possible?
12. What would count as task failure?

* * *

## Implementation contract for subagents

Each worker instruction should be a strict contract, not an open-ended prompt.

### Required fields

* task ID
* exact objective
* prohibited shortcuts
* allowed sources
* allowed files
* required proof/computation style
* required artifacts to emit
* no-claim zone: what the worker is not allowed to assert
* exit condition

### Example no-claim zone

* Do not claim a universal theorem from tested examples.
* Do not use floating numerics where exact algebra is required.
* Do not cite any theorem not present in trusted local sources.
* Do not modify shared utilities outside scope.
* Do not rename an unproved statement as a lemma.

* * *

## Adversarial audit contract

An audit agent should receive the artifact under the assumption that it is wrong unless
it can expose no surviving defect.
Its output is purely adversarial.

### Audit output schema

* `claims_under_review`
* `obligations_attacked`
* `attack_attempts`
* `mathematical_findings`
* `computational_findings`
* `scope_findings`
* `fraud_signals`
* `replay_result`
* `counterexample_attempts`
* `dependency_integrity`
* `unresolved_issues`
* `required_remediation`

### Mandatory audit behaviors

* attempt to refute the result,
* independently restate the theorem actually proved,
* compare claimed theorem to actually established theorem,
* identify any gap where the output silently switches from exact result to heuristic
  narrative,
* inspect diff for collateral edits,
* inspect code for constant-return paths and assertion abuse.

### Explicit non-power of the audit agent

The audit agent may not emit a terminal statement of the form "accepted", "validated",
"approved", or equivalent.
It can only produce attack findings and note whether unresolved issues remain.
Acceptance is a separate assembly step requiring the full concrete bundle.

* * *

## Shared-code policy

Shared core code is itself a research dependency and cannot be treated as invisible
infrastructure.

### Rules

1. Any task depending on shared code must pin the exact version/hash.

2. Changes to shared code require their own task and later gates unless already in
   scope.

3. Proof artifacts may not depend on fresh helper code that has not itself gone through
   the machine.

4. Analysis must distinguish:

   * correctness of the task-specific logic,
   * correctness of shared infrastructure,
   * correctness of external dependencies.

* * *

## Testing policy inside the state machine

Testing does not replace proof.
It serves different roles depending on task type.

### For proof tasks

Testing may only support:

* sanity checks,
* discovery of counterexamples,
* verification of exact intermediate computations,
* certificate replay.

### For computation tasks

Testing must include:

* exact replay on known cases,
* independent cross-check or certificate validation,
* negative tests for scope violations,
* checks against silent constant substitution.

### Forbidden misuse

* treating passing tests as proof of theorem,
* treating partial coverage as proof of classification,
* testing compiler/library behavior as if it were the project's mathematical
  contribution.

* * *

## Natural extensions policy

A task not literally present in `GOAL.md` may still be admitted if it is one of:

* a necessary prerequisite,
* a consequence whose proof materially advances the stated goals,
* an exact computation illuminating a stated conjecture,
* a structurally adjacent theorem explicitly justified in writing.

Such tasks must record the justification in `task.md`. Otherwise they are rejected as
drift.

* * *

## Minimal orchestrator algorithm

```text
loop:
  parse GOAL.md backlog
  choose activated tasks whose prerequisites are ready
  for each task:
    write exact task contract
    run PRE_AUDIT
    if fail -> replan or reject
    if pass:
      dispatch isolated subagents
      collect artifacts
      run SELF_CHECK
      run ADVERSARIAL_AUDIT
      if result is theorem-eligible or conjecture-eligible:
        assemble acceptance bundle
      if theorem bundle complete:
        document and archive as theorem
      elif conjecture-evidence bundle complete:
        document and archive as conjecture
      elif replan required:
        insert prerequisite tasks / rewrite task
      elif quarantined:
        freeze artifact and audit downstream contamination
      else:
        archive as rejected
```

* * *

## Recommended hard gates

A task is automatically blocked from downstream use unless all are true:

1. pre-audit passed,
2. implementation occurred in isolated scope,
3. self-check emitted complete artifact checklist,
4. adversarial audit produced a complete attack bundle,
5. the relevant acceptance bundle is complete,
6. code dependencies hash-pinned,
7. no collateral diff outside approved scope,
8. archive bundle complete.

Item 4 is not an approval gate.
It is only the existence of an attack record.
Downstream trust begins only at item 5.

* * *

## Non-negotiable rejection triggers

Immediate rejection or quarantine on detection of any of:

* theorem claim based on finite enumeration of examples,
* exact quantity replaced by hardcoded constant or identity assertion,
* invented lemma, theorem, or classification fact,
* silently changed conventions,
* unexplained use of helper code that has not itself gone through the machine,
* modifications outside file scope,
* unverifiable claims about results not reproducible from artifacts,
* mismatch between claimed deliverable and actual artifact.

* * *

## Suggested extension: confidence is not a state variable

Do not track outputs as low/medium/high confidence.
Confidence labels permit rhetorical inflation.
Track only:

* theorem bundle accepted,
* conjecture-evidence bundle accepted,
* replan required,
* rejected,
* quarantined.

* * *

## Suggested extension: dual-track independence for critical results

For high-value claims, require two independent paths before theorem acceptance:

* proof path A and proof path B, or
* exact computation A and independent exact cross-check B.

Disagreement automatically triggers `QUARANTINED` or `REPLAN_REQUIRED` depending on
whether contamination is suspected.

* * *

## Second-order semantic controls

The remaining attack surface is mostly not procedural but semantic: who defines
sufficiency, how obligation completeness is judged, how trusted-base growth is bounded,
what independence means operationally, and how local artifacts compose into final
theorem discharge.

### S1. Sufficiency edges must themselves be proved

A parent-sufficiency map may not consist of explanatory prose alone.
Each edge in the map must be one of:

* a proved reduction theorem,
* a formally verified implication,
* a cited trusted theorem together with an instance sheet,
* a declared non-discharge edge stating that the child task is preparatory only.

If an edge claims theorem-level discharge, the edge itself carries proof burden.

### S2. Obligation extraction must satisfy a completeness test

Independent obligation extraction is not complete unless it explicitly checks for:

* quantifier dependencies,
* hidden case splits,
* admissibility conditions,
* uses of classification theorems,
* uses of convention-dependent identifications,
* proof obligations buried in notation or imported definitions.

A theorem bundle must therefore include not only an obligation ledger but an
obligation-completeness report stating what completeness criteria were applied.

### S3. Trusted-base growth is globally budgeted

Trusted-base admission is not only separate; it is scarce.
Each admission must declare:

* what theorem burden is being moved out of future tasks,
* why that movement is justified,
* what prior admissions it depends on,
* why the same burden is not being laundered incrementally.

Large theorem-level content may not be transferred into the trusted base by a sequence
of locally modest admissions without a global review of cumulative burden moved.

### S4. Independence requires a diversity matrix

For any claimed independent cross-check, record a diversity matrix covering at least:

* proof source diversity,
* parser / formalization diversity,
* checker diversity,
* algorithmic diversity,
* convention diversity,
* codebase diversity.

If two verifiers share too many rows of the matrix, they do not count as independent.

### S5. Final composed-goal audit includes assumption unification

Before a `GOAL.md` item is discharged, the final composed-goal audit must also check:

* notation compatibility,
* ambient-object compatibility,
* convention equality,
* hypothesis compatibility,
* theorem-status compatibility of all imported artifacts,
* absence of contradictory local assumptions.

Local soundness is insufficient without global assumption unification.

### S6. "Major" requires threshold rules

Hidden work counts as major if it includes any of:

* a new theorem whose failure would block the parent claim,
* a new algorithm not already in the trusted base,
* a new classification or normal-form result,
* a new convention choice that changes the meaning of downstream statements,
* infrastructure whose correctness is itself mathematically nontrivial.

Such work invalidates the task boundary unless made explicit.

### S7. Replan monotonicity must reduce theorem burden, not only paperwork

A replan is progress only if it does at least one of:

* proves a reduction that strictly shrinks the remaining target,
* isolates a hidden major obligation into an explicit child task,
* eliminates an ambiguity that blocked theorem-instance checking,
* discharges a prerequisite theorem,
* removes a trusted-base ambiguity.

Documentary refinement alone does not count as burden reduction.

### S8. Theorem-level proof artifacts may not be skeletons

Proof skeletons are allowed only as planning artifacts.
A theorem bundle may not use a skeleton as the proof artifact unless every leaf
obligation is either:

* formally verified, or
* expanded to leaf-level derivation with exact cited dependencies.

### S9. Certificate schemas must be task-class specific

A certificate is sufficient only relative to a declared schema for the task class.
Each task class must specify:

* what the certificate certifies,
* what checker validates it,
* why the checker is sufficient,
* which failure modes remain outside the certificate.

Replay of opaque exact data is not enough.

### S10. Claim-surface alignment requires a registry

Each task must maintain a claim-surface registry enumerating all places where claim
strength appears:

* theorem statement,
* task title,
* prose summary,
* filenames,
* archive labels,
* dependency labels,
* downstream planning references.

Any stronger phrasing on any registered surface is treated as part of the operative
claim.

### S11. Local grounding does not imply local sufficiency

For every imported theorem, algorithm, or reference used substantively, the task must
include an instance sheet:

* exact imported statement,
* exact local objects to which it is applied,
* exact local hypotheses required,
* check that each hypothesis holds,
* exact conclusion actually imported.

This blocks under-instantiated citations.

### S12. Conjecture retention has admissibility criteria

A conjectural artifact may be retained only if it has:

* exact and reproducible evidence,
* an explicit conjecture statement,
* a bounded evidentiary domain,
* a clear statement of relevance to a `GOAL.md` item or declared extension,
* nontrivial future planning value that is stated concretely.

Exact but rhetorically suggestive debris is not enough.

### S13. Anti-stalling control

The machine must track theorem-level closure pressure.
If prerequisite depth, trusted-base admissions, or replans grow without corresponding
discharge of parent proof burdens, the process enters a blocked state requiring external
intervention rather than permitting indefinite compliant decomposition.

### S14. Every cited reduction theorem needs an instance sheet

A reduction ledger is incomplete unless every cited reduction/classification theorem is
accompanied by a theorem-instance sheet recording:

* exact theorem statement,
* exact local instantiation,
* exact hypothesis verification,
* exact resulting obligation transfer.

This prevents formally present but semantically loose reduction ledgers.

* * *

## Executable kernel

A further simplification is required for ordinary work: the runtime system should
optimize for fast rejection of overscoped tasks and cheap splitting into
one-shot-friendly subtasks, not for prolonged internal agent loops on bad task shapes.

### Runtime principle: reject/split beats looping on a bad task

The key distinction is not one-shot versus looping in the abstract.
It is:

* one-shotting an overscoped task that hides major work, versus
* one-shotting a sequence of smaller tasks whose contracts match real hidden
  obligations.

If a task silently contains algorithm selection, reusable module construction, and
concrete instantiation, then it is not atomic and should be rejected in that shape.

So the ordinary engine should be:

```text
overscoped task
  -> reject or split in preflight
  -> one-shot narrower subtasks
  -> replay/attack each subtask
  -> promote only when a sufficiency edge is actually discharged
```

Looping remains useful, but mainly for machine reruns, adversarial retries, and narrowly
scoped repair attempts.
It should not be the default strategy for forcing progress on a bad oversized task.

### Canonical sources of truth

The day-to-day system should have only four canonical objects:

1. **Machine-readable task spec** A single structured file per active task containing:

   * origin `GOAL.md` item,
   * exact claim or computation target,
   * parent-sufficiency edges,
   * task type,
   * allowed scope,
   * trusted-base dependencies,
   * verification plan,
   * current status.

2. **Trusted-base registry** A versioned registry of admitted lemmas, references,
   algorithms, conventions, helper modules, and certificate schemas, with explicit scope
   and limits.

3. **Artifact directory** Produced objects only: proofs, computations, certificates,
   logs, replay outputs, counterexample attempts, and generated reports.

4. **Git state** Branch/worktree isolation, provenance, diffs, hashes, and merge
   history.

Everything else in the larger design should be generated from these objects or computed
in CI.

### Generated, not handwritten

The following should normally be derived reports, not manually maintained primary
documents:

* dependencies view,
* assumptions view,
* claim-surface registry,
* obligation ledger,
* reduction ledger,
* theorem-instance sheets,
* archive manifests,
* replay summaries,
* scope-diff summaries.

If a view cannot be generated, it should at least be machine-checked against the
canonical task spec and artifact contents.

### Stage model for the executable kernel

Use only four live stages in the ordinary workflow:

1. **Preflight** Machine checks whether the task is atomic enough to run.
   If hidden major work is detected, the task is rejected in its current shape and
   split.
2. **Run one-shot** Agents attempt the atomic task in isolated scope.
3. **Replay/Attack** CI and adversarial checks rerun artifacts, verify certificates,
   test scope, and generate attack reports.
4. **Promote / Reject / Split** Promotion is allowed only if the required generated
   reports show theorem-burden discharge or admissible conjectural evidence.
   Otherwise the result is rejected or the task is split into narrower children.

This is deliberately smaller than an iterative implement/audit loop.
The default for ordinary work is not prolonged looping but one-shot execution on tasks
that already passed the atomicity gate.

### Atomicity gate

Preflight should reject a task as non-atomic if success would require any undeclared
major obligation such as:

* choosing or inventing the core algorithm,
* building reusable exact infrastructure not already in the trusted base,
* proving a new reduction theorem,
* fixing a convention that changes downstream meaning,
* solving a hidden classification or search problem comparable to the nominal task.

When this happens, the system should split the task along the real burden lines.
For example:

* determine or fix the algorithmic approach,
* implement the reusable exact module,
* instantiate the module on the concrete input.

These are legitimate subtasks because they correspond to distinct hidden obligations.
Splitting is invalid only when it replaces the original burden by weaker paperwork tasks
rather than exposing the real mathematical/computational burdens.

### Escalation tiers

Heavy controls should trigger only when theorem-level burden is about to move upward.

#### Tier 0: exploratory / preparatory

* isolated scope,
* canonical task spec,
* trusted-base pinning,
* replayable artifacts.

No theorem-discharge claims allowed.

#### Tier 1: local claim promotion

When a task claims to discharge a parent sufficiency edge:

* generate obligation ledger,
* generate reduction ledger if computation is involved,
* run independent obligation extraction/check,
* run claim-surface alignment checks.

#### Tier 2: `GOAL.md` discharge

When a task claims to discharge a `GOAL.md` item:

* run final composed-goal audit,
* run assumption-unification checks,
* require verifier diversity where applicable,
* require theorem-instance sheets for imported reductions/classifications,
* require anti-laundering checks over prerequisite chain and trusted-base growth.

This keeps theorem-acceptance strict without forcing theorem-level bureaucracy onto all
preparatory work.

### Automation-first enforcement

The live system should push enforcement into tooling rather than prose.

#### Git / worktree layer

* isolate tasks by branch or worktree,
* enforce allowed-path scope,
* block merges on out-of-scope diffs,
* keep provenance and hashes automatically.

#### CI layer

* validate machine-readable task specs,
* regenerate derived reports,
* fail on stale generated views,
* rerun replay/certificate checks,
* run adversarial check suite,
* run promotion gates.

#### Hook / policy layer

* block edits outside declared scope,
* block trusted-base modifications without admission records,
* block promotion if generated reports are stale,
* block theorem promotion from tasks whose type does not permit theorem discharge.

### Single-source anti-drift rule

If the same semantic fact appears in multiple places, exactly one location is canonical
and all others are generated or checked against it.
In particular:

* the exact claim is canonical in the task spec;
* trusted assumptions are canonical in the trusted-base registry plus task spec
  instantiation;
* provenance is canonical in git;
* produced evidence is canonical in artifact outputs.

This is the main way to avoid the drift problem created by many ledgers.

### Operational thresholds should be encoded, not narrated

Terms such as `high-risk`, `critical`, `substantial`, and `external intervention` should
not remain informal prose.
The executable kernel should replace them with trigger predicates, for example:

* theorem-discharge attempted,
* imported reduction theorem used,
* trusted-base admission requested,
* exact computation lifted to a universal claim,
* multiple replans without theorem-burden decrease,
* cross-task composition invoked for `GOAL.md` closure.

These predicates decide which checks run.

### Anti-stalling control in executable form

Track a simple monotone measure attached to each `GOAL.md` item:

* unresolved sufficiency edges,
* unresolved theorem-level obligations,
* undeclared trusted-base admissions pending,
* blocked composed-goal audits.

If this measure does not decrease across repeated replans or prerequisite expansions,
promotion is frozen and the system enters a blocked state.
This prevents endless compliant decomposition.

### Recommended MVP

A practical minimum implementation is:

* one canonical machine-readable task spec per task,
* one canonical trusted-base registry,
* one artifact directory,
* git/worktree isolation,
* CI stages: preflight, run one-shot, replay/attack, promote/reject/split,
* atomicity checks that reject overscoped tasks early,
* generated reports only at promotion boundaries,
* heavy semantic checks triggered only for parent-edge discharge and `GOAL.md` closure.

This captures the anti-fraud core while keeping ordinary research work lightweight
enough to converge.

* * *

## Result

The correct implementation target is not the full document as a literal day-to-day
operating system. It is a slim executable kernel backed by:

* a canonical task spec,
* a canonical trusted-base registry,
* artifact outputs,
* git provenance,
* CI-enforced replay/attack/promotion,
* escalation to heavier checks only when theorem burden is being discharged.

That preserves loophole resistance while reducing operational overhead and moving
enforcement into automation rather than handwritten governance.
