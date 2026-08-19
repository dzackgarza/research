---
title: ONBOARDING — READ FIRST
included_by: [index]
---
# ONBOARDING — READ BEFORE ANY ACTION

**Do not read other files, run tools, scan plans, or edit anything until you have read
this entire document.** This is the gate.
Every agent session begins here.

## Completion discipline — the core invariant

Start from the mathematical object.
Route by a priori mathematical ownership.
Treat code as a witness.
Treat artifacts as consequences.
Treat hidden compliance as zero evidence.
Completion means a visible theorem, formula, representation split, or missing-category
obligation.

Hidden reasoning is not evidence.
A code edit, mapping label, prose explanation, or passing report that lacks one of those
four visible outputs is not progress.
If the artifact becomes cleaner while the mathematical owner remains unstated, the edit
is theater.

Separate four layers in every action:

1. **The mathematical object** (set, module, morphism, topological space, etc.)
2. **The expression object** (basis, coordinate chart, matrix representative, etc.)
3. **The implementation** (storage, normalization, backend calls, etc.)
4. **The category obligation** (the highest abstract category where the operation
   belongs)

A type error is a diagnostic, not an editing instruction.
A mapping row must name an owner, give a recovery formula, or declare a missing
category/spec obligation — it is never allowed to defer behind labels like "pending",
"abstract", or "rejected".

If the next move is to adjust a decorator, signature, label, section, report, or prose
explanation before the mathematical owner is visible, the frame is wrong.

See `mem:category-spec-epistemic-foundation` for the full completion discipline:
evidentiary rules, visible obligations, frame-rejection triggers, and mapping-document
purpose.

* * *

## What this project is

This is a **mathematical research repo**, not an engineering project.
The engineering exists only to build reliable mathematical language so that future
lattice/Coble work can state claims, define objects, and write proofs that read like
mathematics.

The high-level goal is to build a mathematically semantic, Sage-compatible substrate
for exact lattice and surface computations, then use it to verify the lattice-theoretic
claims needed for the moduli space of terminal Coble surfaces of K3 type. `GOAL.md` is
the staged-program source for that goal.

The current spec phase defines the mathematically natural category/refinement structure
needed by the Coble/K3 lattice research, grounded by Sage/source inventories. The phase
does not restrict the spec to objects Sage already implements, and it does not write an
API detached from realization.

The object-level rule is categorical. Claimed methods follow from the object's stated
category membership, hypotheses, and required witnesses. `Aut(L)` or `O(L)` belongs in
the lattice spec as the automorphism group of a lattice. It lies first in `Groups`.
`gens()` appears only after the same group is also placed in
`FinitelyGeneratedGroups`, a generated matrix-group category,
`FinitelyPresentedGroups`, or an explicitly generated-subgroup category.

The downstream computation must be able to express and check `Pic(S)`,
`f^*Pic(S) <= H^2(X, \mathbb{Z})`, and
`T_Co = (f^*Pic(S))^\perp <= \Lambda_{\mathrm{K3}}`, together with discriminant forms,
primitive embeddings, orthogonal complements, isotropic-orbit calculations,
stabilizers, and involution eigenspaces. The current category-spec phase exists to make
those objects and morphisms typed mathematical objects, not raw matrices, incidental
method calls, or ledger rows.

The test of progress is not completed cards, green checkboxes, or process artifacts.
The test is:

> What mathematical object, operation, claim, interface, or proof path is now closer
> because of this work?

If the answer is only "a card is clearer," "a plan is more detailed," or "handoff
context improved," presume no mathematical progress occurred.
If the user's directive names a broader correction, such as entrypoint guidance or
anti-laundering doctrine, completing the current handoff leaf is not a substitute. The
handoff tells where to resume ordinary work; it does not override the latest user
directive or shrink it to the nearest mapping slice.
Terminology cleanup is not completion unless the rewritten passage states the
mathematical object, operation, category, hypothesis, witness, source evidence, or
implementation gap that the old wording hid.
When asked for a research checkpoint or to touch base with high-level tasks, begin with
the mathematical state, not a route through plans or features. State what definitions,
constructions, category obligations, implementation witnesses, or proof obligations are
established; what exact mathematical claims remain unresolved; which claim is next; what
source or Sage/backend behavior controls it; and what becomes true if it is settled.
If prior work did not change any of those objects, call it paperwork, not mathematical
progress.

The implementation philosophy is minimal reuse at owned boundaries.
Use mature mechanisms for solved non-research problems: Sage for category construction,
Python for abstract-method semantics, and mature mathematical backends for exact
algebra.
Project-owned glue is justified only when it is the smallest bridge needed to compose
those mechanisms and keep ordinary mathematical specs readable.
Quarantine unavoidable Sage/Python internals in the interop layer; do not spread them
through specs, refinement-time satisfaction checks, category-obligation examples, or
local helper systems.

Downstream Coble/lattice goals must NOT be attacked by raw matrix computations.
The repo is in the category-spec phase.
See `mem:repo-purpose-mathematical-research-machine`.

## Current phase

**Category-spec vocabulary.** The current obligations are named mathematical
structures: sets, modules, Hom/End/Aut objects, modules with forms, lattices,
morphisms, coercions, exact-backend bridge points, category refinements, and witness
data. Do not abbreviate this as "the substrate" unless the concrete structures and
obligations have already been named. Downstream lattice/Coble work is blocked until this
vocabulary exists.

Spec work is in scope when it is needed to express later lattice or Coble computations
as typed mathematical constructions, or when Sage investigation shows that omitting it
would force raw matrix/vector/group manipulation at the research layer. It is out of
scope when it only improves general Sage ergonomics, catalogs arbitrary concrete
methods, or places an object in a stronger category without the required proof,
construction, or witness. Geometry vocabulary such as schemes, varieties, surfaces,
divisors, Picard groups, blowups, covers, and families is deferred and recorded until
the lattice substrate exists.

Read `GOAL.md` once, but the phase is tracked in `.agents/current-goal-phase.md`. Do not
attempt downstream Coble research.

## CRITICAL constructor interop rule

Before touching constructors, load
`mem:category-spec-constructor-routes-are-category-owned`.

Constructor work is not constructor redefinition. The workflow is:

- read Sage docs and actual factory/source code;
- enumerate every valid Sage input shape, especially variadic/positional factories;
- record the recovered shapes in mapping docs;
- treat every source-grounded constructor shape recorded in mapping docs as mapped;
  there is no deferred, not-admitted, or blocked constructor state in source material;
- expose only named-parameter category-owned overloads on `Cat().Constructors()`;
- implement each overload by calling the original Sage constructor, refining the
  returned parent, and returning it;
- make category-obligation examples call category constructor methods only.

Any constructor surprise is a red flag that this workflow was skipped. Start auditing
at the mapping docs and overload definitions; do not patch ambient Sage names, widen a
free-floating wrapper, add "constructor redefinitions", or preserve rejected constructor
ideas as evidence artifacts. If Sage source does not establish the constructor shape,
do not mention it in constructor mappings, provenance, category-obligation examples,
decisions, or tasks.
Do not polish a suspect constructor artifact in place. Reconstruct the mapping from
Sage docs/source, then delete or replace the artifact as a consequence of the corrected
mapping.

Refinement targets are single categories. A constructor returning a `Qp` object refines
to the `Qp` implementation-spec category; inherited ring/field/local-field membership
comes from the category hierarchy. Passing several categories to `refine_category`
manually bypasses the hierarchy and is banned.

## CRITICAL property/witness distinction

Before changing module property categories, load
`mem:category-spec-properties-witnesses-and-equipped-structure`.

Property categories are not equipped-object categories.
`FinitelyGenerated` asserts finite generation; `WithFiniteGeneratingSet` or
`WithOrderedGeneratingSet` adds a chosen witness as part of the object.
Property categories should still name abstract witness-producing methods so downstream
consumers can demand evidence for the claim, but the graph edge goes from equipped
witness to property, not from property to equipped witness.

## CRITICAL category-obligation example public API rule

Before editing category-obligation examples or regressions, load
`mem:category-spec-tests-use-category-api-not-private-classes`.

Tests must mirror downstream mathematical use: category objects, category-owned
constructors, refinements, membership, and methods reached through those category
operations.
Tests must not define dummy classes that inherit private spec implementation classes or
nested `ParentMethods` / `ElementMethods` containers.
Those class names are internal engineering, not user-facing mathematical vocabulary.

## Immediate concrete work

Read `mem:current-goal-handoff` for the most recent next action.
The handoff names **concrete, source-grounded fixes** — read the files it names,
understand the problem, and fix it.
Do not run tools, produce reports, or create process artifacts instead.

## The seven most common agent failure modes

Learn these before you act.
Every one of these has happened.
Every one will waste the session if you repeat it.

### 1. Running tools instead of reading code

Error: Producing a mypy report, ledger, structural analysis, or classification before
reading the actual source files that the handoff names.

Rule: Read the code first.
The handoff names specific files and types of errors.
Read those files. If you cannot quote both sides of a conflict from source, you are not
allowed to classify or fix it.
See `mem:analysis-must-be-grounded`.

### 2. Producing process artifacts instead of concrete fixes

Error: Writing strategy documents, issue comments, acceptance criteria, or planning
documents when asked to fix a bug.

Rule: If the handoff says "fix ~25 private-stub annotation bugs," fix the annotations.
Do not write a document about fixing them.
Do not create a card.
Fix the code. See `mem:analysis-must-be-grounded` and
`mem:foundation-serves-research-not-itself`.

### 3. Treating private Sage stubs as types

Error: `_RingObjectMethods`, `_RModObjects`, `_RingHomomorphisms` etc.
appearing in return type annotations.
These are **private method-container stubs** used to organize Sage category definition
files. No object is an instance of `_RingObjectMethods`. No method returns one.

Rule: Any method whose declared return type is a private `_*Methods` or `_*Objects` name
has a **bug in the annotation**. Replace with the public type (`Ring`, `Module`,
`Morphism`, `Set`, etc.). This is mechanical.
No decision, variance analysis, or `# type: ignore` needed.
See `mem:private-stubs-are-not-types`.

### 4. Classifying errors without reading both sides of the conflict

Error: Inventing categories like "variance problem," "Liskov audit," or "interface
design question" before displaying the two conflicting method signatures side by side.

Rule: Before classifying any override/signature error, quote both definitions from the
actual code. The RealSet/topological-space incident involved `is_open(self, U: Subset)`
vs `is_open(self)` — an arity conflict visible in 30 seconds of reading.
An agent spent hours on ledger taxonomy instead.
See `mem:analysis-must-be-grounded` and `mem:mathematics-first-not-engineering-options`.

### 5. Trying to run mypy directly

Error: Running `mypy category_specs/` from the command line instead of through Sage.

Why it's wrong: The code imports Sage — needs `sage -python`. The mypy plugin teaches
mypy about Sage's dynamic category system (`_with_axiom`, dynamic inheritance,
method-container projection).
Running bare mypy fails on every import.

Why the automated structural report recipe is also wrong right now: The plugin CANNOT
produce correct output until the source-level annotation bugs (items 1 and 2 from the
handoff) are fixed. Running the tool before fixing the code is circular.

When to run it: After fixing the source-level errors, use
`just category-specs-mypy-structural-report` which correctly routes through
`sage -python` with the plugin.

### 6. Treating a process problem as a local patch

Error: Finding an embarrassing, fundamental error (e.g., `_QQ` declaring both `_Fields`
and `_NumberFields` as supercategories) and just fixing that one instance.

Rule: The presence of the bug proves the process is broken.
Create inspection tooling so the error is discoverable in the future, then fix the
concrete instance, then add a test that would have caught it.
See `mem:process-before-patches-policy`.

### 7. Redefining constructors instead of recovering Sage constructor shapes

Error: A category assertion fails because raw Sage construction returns an unrefined
object, and the agent patches Sage globals, module attributes, temporary providers, or
a free-floating wrapper so the old syntax secretly returns a project-refined object.

Rule: Public project constructor API lives only on category `Constructors()` methods.
Recover Sage's valid constructor shapes from docs and source, enumerate them in mapping
docs, expose them as named-only overloads on the owning category, call the original Sage
constructor, refine the result, and make category-obligation examples call those
category constructors. See `mem:category-spec-constructor-routes-are-category-owned`.

## How to start

1. Read this document. You are doing that now.
2. Read `mem:current-goal-handoff`.
3. Read the files named in the handoff.
4. Fix the bugs.
5. Update the handoff with what the next session should do.

## Critical follow-up memories

Read these when their situation arises:

| Situation | Memory |
| --- | --- |
| Learning what the repo is for | `mem:repo-purpose-mathematical-research-machine`, `mem:what-category-specs-actually-is`, and `mem:category-spec-repo-model-corrections` |
| Reviewing recent commits, prior agent output, or suspicious category-spec work | `mem:category-spec-rotten-core-indicators` and `mem:mathematical-sanity-check` |
| Before any category operation edit, decorator change, or mapping | `mem:category-spec-epistemic-foundation` |
| Writing, editing, or retrieving a memory | `mem:memory-management-discipline` |
| About to write a return type for a method | `mem:private-stubs-are-not-types` |
| About to classify a mypy override error | `mem:analysis-must-be-grounded` |
| About to produce or polish cards, ledgers, reports, plans, handoffs, or notes | `mem:paperwork-is-a-routing-layer-not-progress` |
| User correction affected repo purpose, architecture, or mathematical claims | `mem:corrections-update-the-model-not-the-artifact` |
| Refinement, object-method resolution, constructor refinement, abstract methods, ABCMeta, or failed category assertions | `mem:category-spec-repo-model-corrections`, `mem:category-spec-refinement-category-declaration`, and `mem:category-spec-methods-are-abstract` |
| Two methods with the same name collide | `mem:mathematics-first-not-engineering-options` |
| Found an embarrassing category-graph bug | `mem:process-before-patches-policy` |
| About to produce a strategy doc instead of code | `mem:foundation-serves-research-not-itself` |
| Unsure about stub vs. plugin vs. internal work | `mem:category-spec-architectural-boundary` |
| Drifting from mathematical purpose | `mem:repo-purpose-mathematical-research-machine` |
| Writing specs or type annotations | `mem:category-spec-style` (skill) |
| Any category-spec workflow, audit, planning, triage, or retirement operation | `mem:skills/category-spec-*` |
| Mathematical proof or computation audit | `mem:skills/research-proof-auditing` |
| Fixture creation or source acquisition | `mem:skills/creating-fixtures` or `mem:skills/research-source-acquisition` |
| Lattice redesign or module boundary work | `mem:skills/lattice-redesign` or `mem:skills/research-math-boundary` |
| Subagent delegation, one-shot workers, or orchestration | `mem:skills/opencode-one-shot-workers` |
| Planning cleanup, meta-review, or completed-card quality scan | `mem:skills/research-planning-cleanup` |
| Scheduling, cadence, or wakeup design | `mem:skills/research-scheduling` |
| Repo structure, cleanup, or file placement | `mem:skills/research-repo-structure` |
| Research intake, workstream setup, or co-mathematician workflow | `mem:skills/research-co-mathematician-workflow` |
| Tracker mechanics and plan decomposition | `mem:skills/research-project-workflow` |
| Vinberg's algorithm | `mem:skills/vinberg-algorithm` |
| Sage category source maps | `mem:skills/sage-category-source-maps` |
| Plannotator CLI workflow | `plannotator-workflow` |

Most former local skills now live under `mem:skills/`. Use `iwe find skills/` to
discover the full tree.
Remaining always-in-context skills are: `research-software-wiring`,
`research-relevance-check`, `handling-corrections`, `research-state-machine`,
`research-orchestration`, `research-code-style`, `category-spec-style`, `task`, and
`track`.

## Do not

- Run mypy, structural reports, or ledgers until the source-level bugs are fixed.
- Create cards, issues, or process documents instead of fixing code.
- Delegate concrete fix work to future agents.
- Produce analysis documents when asked for a fix.
- Classify errors without reading both sides of the conflict.
- Use `# type: ignore` or cast-based silencing.
- Write `NotImplementedError` — banned by pre-commit hook.
- Touch downstream Coble/lattice code.
