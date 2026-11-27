---
id: PLAN-STATIC-CATEGORY-REFINEMENT-ORDER
trackerStatus:
  type: plan
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Static category refinement order and constructor-interception sequence
status: in-progress
priority: critical
owner: Zack
description: 'Define and enforce the static category refinement order (which categories
  sit above which in the hierarchy) and the constructor-interception order (which
  constructors fire before which). Prevents downstream work from depending on
  unstable category graph edges or incorrect interception chains.'
successCriteria:
- Every `super_categories()` return in `category_specs/` is documented in the
  admitted-edges table or has an approved decision card.
- No constructor refines into a category whose status is `unstarted`.
- New categories added to the refinement order require an update to this plan
  and a decision card.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Static category refinement order and constructor-interception sequence

## Objective

Encode the project's category refinement order as a static constraint: every
`super_categories()` return is a documented, justified edge in the category
graph. Constructor interception order is similarly constrained: constructor
routing must not depend on unstable or downstream categories.

## Core principles

### Category refinement order

- Every subcategory's `super_categories()` must be justified by a mathematical
  specialization relationship (e.g. Fields → IntegralDomains → Rings) or a
  structural construction relationship (e.g. Subobjects → Sets).
- No subcategory may list a supercategory that is still under active spec review
  unless the edge is already settled by an approved decision or accepted spec.
- The refinement order is static: it should not change during execution based on
  Sage runtime state, constructor parameters, or coercion outcomes.

### Constructor-interception order

- Constructor routing must call Sage once, refine the returned parent into the
  appropriate project categories, and return the refined object.
- The refinement target categories must be a subset of the categories that the
  constructed parent actually satisfies. Do not refine into a category whose
  supercategory is not yet settled.
- Do not refine into a downstream category whose vocabulary depends on method
  ownership decisions still in review.

### Enforcement

- Before a subcategory is added or changed, verify that its supercategory chain
  does not include categories with unstarted or in-review status for their
  foundational specs.
- Before a constructor refines into a target category, verify that the target
  category's method surface is settled (status is at least needs-review with
  checked acceptance criteria).

## Admitted category refinement edges

The following edges are admitted as settled. Future work may add edges but must
not remove or reorder existing edges without a decision card.

| Subcategory | Supercategories | Justification |
|---|---|---|
| `Algebras(R)` | `Rings(R)`, `Modules(R)` | Algebras are rings with an R-module structure; Sage confirms. Source: category_specs/algebras/docs/MAPPING.md |
| `Algebras(R).WithBasis()` | `Algebras(R)`, `Modules(R).WithBasis()` | Basis-bearing algebras inherit both structures. Source: same. |
| `Modules(R).Free()` | `Modules(R)` | Free modules are modules. |
| `Modules(R).Free().FiniteRank()` | `Modules(R).Free()` | Finite-rank free modules refine free modules. |
| `Posets().Finite()` | `Posets()`, `SageFinitePosets()` | Finite posets refine posets and use Sage's finite poset implementation. |
| `Posets().JoinSemilattice().Finite()` | `Posets().JoinSemilattice()`, `Posets().Finite()` | Finite join-semilattices refine both. |
| `Sets().Partitioned()` | `Sets().Countable()`, `Sets().Subobjects()` | Partition sets are countable subobjects of the powerset. |
| `Sets().Partitioned().FiniteTotallyOrderedBase()` | `Sets().Partitioned()`, `Sets().Countable().Finite()` | Finite totally-ordered base partitions refine both. |
| `TensorAlgebraComponents(R)` | `Modules(R).TensorProducts()`, `Modules(R).Free().FiniteRank()` | Tensor components are tensor products of finite-rank free modules. |
| `_MatrixAlgebras(R, n, n)` | `Algebras(R)`, `Modules(R).Free().FiniteRank()` | Square matrix rings are algebras and finite-rank free modules. |
| `_ImageSets` | `Sets().Subobjects()`, `Sets().Subquotients()` | Image subobjects are both subobjects and subquotients. |

## Constructor interception order

Constructors must refine into target categories in this order of stability:

1. `Sets()` — always stable, always available.
2. `Modules(R)` — stable for PID base rings.
3. `Modules(R).Free()` — stable.
4. `Modules(R).Free().FiniteRank()` — stable.
5. `Algebras(R)` — stable.
6. `Posets()` / `Posets().Finite()` — stable.
7. `Sets().Countable()` / `Sets().Finite()` — stable.
8. `Sets().Subobjects()` / `Sets().Subquotients()` — stable.
9. `Rings()` subcategories — stable for settled rings (ZZ, QQ, finite fields, p-adics).
10. `TensorAlgebraComponents(R)` — stable.
11. `_MatrixAlgebras(R, n, n)` — stable.

Categories that should NOT be used as constructor refinement targets yet
(because their method ownership or supercategory edges are still under review):

- `Modules(R).Graded()` — Sage/project base-category mismatch not resolved.
- `Modules(R).WithForms()` — forms-owned categories pending Phase 02.
- Lattice/discriminant categories — pending FEATURE-MODULES-WITH-FORMS-AND-LATTICES.

## Acceptance Criteria

- [ ] Every `super_categories()` return in `category_specs/` is documented in the admitted-edges table or has an approved decision card.
- [ ] No constructor refines into a category whose status is `unstarted`.
- [ ] New categories added to the refinement order require an update to this plan and a decision card.

## Source corpus

- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `category_specs/*/docs/MAPPING.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-FOUNDATION-KERNEL/PLAN-CATEGORY-FOUNDATION-KERNEL.md`

## Work Log

- 2026-05-07: Created as missing skeleton plan referenced in current-goal-phase.md.
  Sources category refinement edges from existing super_categories() returns in
  the implementation files under category_specs/.
- 2026-05-09: Reclassified from `needs-human-input` to agent-owned remediation.
  `super_categories()` edges are mathematically determined by source-grounded
  specialization or construction relationships; dead links, missing citations,
  incomplete edge inventory, and the `Sets().Partitioned()` contradiction are plan/spec
  cleanup work, not owner decisions.

## 6-Gate Protocol Review Log

Review conducted 2026-05-07 against the card body below this log.  The review
audited `category_specs/` super_categories() returns, checked source references,
and scored each gate.

### G1 — Source Grounding

**Sources cited**: three entries in Source Corpus section.

| Source | Exists? | Notes |
|---|---|---|
| `.agents/skills/lattice-redesign/references/category-abc-spec.md` | **MISSING** | No file at this path; no lattice-redesign skill directory found. This is a dead reference. |
| `category_specs/*/docs/MAPPING.md` | **EXISTS** | 17 MAPPING.md files found. Only 2 of 11 admitted-edges rows cite a specific MAPPING.md. |
| `PLAN-CATEGORY-FOUNDATION-KERNEL.md` | **EXISTS** | Referenced but is a planning artifact, not a mathematical source. Contains migrated source bodies that provide real grounding. |

**Edge grounding quality**: Only rows 1 (Algebras) and 2 (Algebras.WithBasis) cite
a concrete source file. The other 9 rows use brief prose justifications ("Free
modules are modules", "Finite posets refine posets") without file paths, Sage
source references, or canonical theory references. These are tautologies, not
grounding.

**Verdict**: **PARTIAL PASS**.  MAPPING.md corpus exists.  One dead reference
(category-abc-spec.md).  Only 2/11 edges carry traceable source citations; the
rest are justified by self-evident prose.  The card needs source links for every
edge row to satisfy its own success criterion #1 in a reviewable way.

### G2 — Exit Criteria Checkable

Three success criteria defined (frontmatter + body acceptance criteria are
identical):

1. *Every super_categories() return in category_specs/ is documented in the
   admitted-edges table or has an approved decision card.*
   → Checkable but **currently FAILING**.  Audit of `category_specs/` reveals
   ~30+ `super_categories()` calls across 50 files.  Only 11 edges appear in the
   table.  Examples undocumented: `_Fields` returns 8 supercategories,
   `_FinitePosets` returns `[Posets(), SageFinitePosets()]` (documented, ok),
   but `Posets().Finite().JoinSemilattice()`, `Posets().Finite().Lattice()`,
   `_CartesianProducts`, `_Quotients`, `_Subobjects`, `_Subquotients`,
   `RingsOver`, `RingsUnder`, `_TopologicalSpaces`, `Compact`, `Complete`,
   `Connected`, `Metric`, `_ImageSets`, `PartitionedSetsCategory` (returns `[]`
   — empty, contradicting the table row for `Sets().Partitioned()`), and many
   Rings subcategories are absent.  Criterion is falsifiable but currently
   falsified.

2. *No constructor refines into a category whose status is `unstarted`.*
   → Checkable given tracker metadata.  Requires cross-reference with
   constructor-interception implementations.  Not verified in this review but
   structurally checkable.

3. *New categories added to the refinement order require an update to this plan
   and a decision card.*
   → A governance rule, not a binary exit criterion.  It constrains process
   rather than declaring a state to reach.  Cannot be checked as "done" — it
   is either being followed or not.

**Mismatch**: The success criteria and acceptance criteria are duplicates
(identical text).  One of them should be removed or they should be
differentiated.

**Verdict**: **PARTIAL PASS**.  Criteria #1 and #2 are checkable but #1 is
failing against current code.  Criterion #3 is a process constraint, not an
exit gate.  Duplicate criteria between frontmatter and body.

### G3 — Phase Inventory

- **No `phases` field** in frontmatter metadata.
- **No PHASE-* subdirectories** under this plan directory.
- This plan is a **leaf/policy card**, not a container.  Structurally valid.
- However, "enforcement" implies operational work: auditing all current
  `super_categories()` returns, adding missing edges to the table, verifying
  constructor-interception order against actual constructors.  This work is not
  captured in any child phase, phase card, or task list under this plan.
- The plan is referenced as a subplan by `PLAN-CATEGORY-FOUNDATION-KERNEL`
  (line 103 of that card), which is correct containment.

**Verdict**: **PASS with NOTE**.  A leaf policy plan does not require phases.
But the gap between the stated admitted-edges table and the actual codebase
implies enforcement work that should be tracked somewhere (either as a phase
under this plan, tasks under the parent plan, or an explicit follow-up card).

### G4 — Scope

**In-scope** (well-bounded):
- Category refinement edges (admitted-edges table, 11 rows).
- Constructor-interception order (11 stable levels + 3 exclusions).
- Core principles for adding/removing edges and constructors.
- Excluded categories list (Graded, WithForms, Lattice/discriminant).

**Scope gaps**:
1. The admitted-edges table omits the entire Rings subcategory hierarchy
   (Fields, Commutative, Division, Euclidean, IntegralDomain, PID, UFD,
   Dedekind, Noetherian, Reduced, Valued, DVR, etc.) — dozens of
   `super_categories()` returns.
2. Topological spaces (`TopologicalSpaces()`, `Compact()`, `Complete()`,
   `Connected()`, `Metric()`) super_categories are absent.
3. Construction categories (CartesianProducts, Quotients, Subobjects,
   Subquotients, RingsOver, RingsUnder) are absent.
4. PartitionedSetsCategory returns `[]` (empty super_categories) but the
   table claims `Sets().Countable()` and `Sets().Subobjects()` — direct
   contradiction.
5. Scope does not state whether the table is exhaustive (it says "The
   following edges are admitted as settled. Future work may add edges" which
   implies it is NOT exhaustive — but then success criterion #1 demands
   exhaustive coverage).

**Verdict**: **PARTIAL PASS**.  Scope is well-defined at the conceptual level
but the admitted-edges table is a small subset of what exists in code.  The
card must either expand the table to cover all current `super_categories()`
returns or clarify that only a designated subset is in scope, with the rest
explicitly deferred to decision cards.

### G5 — Dependencies

- `dependsOn: []` — declared as having no dependencies.
- **Parent relationship**: Correctly listed under `parents:
  [[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]`.  Also cross-referenced in
  `PLAN-CATEGORY-FOUNDATION-KERNEL` as a subplan.
- **Implicit dependencies**: The card's content depends on `category_specs/`
  being populated (it exists).  For enforcement, it depends on access to
  category status metadata (tracker system) and constructor-interception code.
  None of these are blocking prerequisites in the DAG sense.
- **Missing dependency**: The constructor-interception order references
  `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` implicitly (that's where
  constructors live).  No explicit dependency edge declared.

**Verdict**: **PASS with NOTE**.  `dependsOn: []` is accurate for a policy
card that does not block on prior work.  A soft dependency on
`PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` for enforcement validation would
improve traceability but is not blocking.

### G6 — Preservation

- Card created 2026-05-07 as a new skeleton — no prior content to preserve.
- Structure follows workspace conventions: valid YAML frontmatter, all
  required fields present (id, trackerStatus.type=plan, parents, dependsOn,
  title, status, priority, owner, description, successCriteria, tags).
- Work log has one entry.
- No stale references to deleted files (except the dead source reference
  noted in G1).

**Verdict**: **PASS**.  No preservation issues.  Clean card structure.

---

### Summary

| Gate | Verdict | Critical Issues |
|---|---|---|
| G1 Source Grounding | PARTIAL PASS | Dead source ref; only 2/11 edges have traceable citations |
| G2 Exit Criteria | PARTIAL PASS | Criterion #1 fails against current code; #3 is a process rule, not an exit gate; duplicate criteria |
| G3 Phase Inventory | PASS (note) | No phases needed but enforcement work is untracked |
| G4 Scope | PARTIAL PASS | Admitted-edges table covers ~20% of actual super_categories() returns; PartitionedSets row contradicts code |
| G5 Dependencies | PASS (note) | Soft dep on PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION undeclared |
| G6 Preservation | PASS | Clean |

### Recommendations

1. **Fix dead source reference**: Remove or correct
   `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
2. **Audit all super_categories() returns** in `category_specs/` and add
   missing rows to the admitted-edges table, or create decision cards for
   each undocumented edge.
3. **Fix PartitionedSets row**: `PartitionedSetsCategory.super_categories()`
   returns `[]` but the table claims `Sets().Countable()` and
   `Sets().Subobjects()` — either the code or the table is wrong.
4. **Add source citations** to every admitted-edges row (specific
   MAPPING.md file, Sage source reference, or decision card ID).
5. **Differentiate success criteria from acceptance criteria** — remove
   the duplicate or give them distinct roles.
6. **Clarify scope**: State whether the admitted-edges table is exhaustive
   or whether only certain category subtrees are in scope.
7. **Create enforcement tracking**: Add a phase or task card to close the
   gap between the table and the codebase.
8. **Declare soft dependency** on PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
   if constructor-interception enforcement requires it.
