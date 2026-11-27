---
id: SPEC-01KQN9J3WT5HMPK9GCKWAENPQ5-FINISH-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-EXPLICIT-NAMES-FOR-ADDITIVE-AND
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
title: Finish algebra constructor admission and explicit names for additive and table
  algebra construction routes
status: complete
priority: critical
requirement: The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ),
  a module hom-category/forms blocker for DualObjects, and constructor admission gaps.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- No new implementation blocker was discovered during this docs/spec pass; recovered
  smoke failures remain non-constructor frontiers.
- No algebra category initialization or constructor code changed, so the `algebras/smoketest.sage`
  trigger did not apply in this pass.
- Plain-set `S.algebra(R)` remains routed to `free_module` over `Modules(R)`, not
  to `Algebras(R)`.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Finish algebra constructor admission and explicit names for additive and table algebra construction routes
## Summary

The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ), a
module hom-category/forms blocker for DualObjects, and constructor admission gaps.

## Source Provenance

- The requested recovery path `git show 8d1c21c^:category_specs/algebras/docs/TRIAGE.md`
  fails because the file still lived under `plans/category_specs/algebras/docs/TRIAGE.md`
  at that parent commit.
- Exact recovered prior content came from
  `git show 8d1c21c^:plans/category_specs/algebras/docs/TRIAGE.md`.
- Original migrated line: `Finish algebra constructor admission and explicit names for additive and table algebra construction routes from category_specs/algebras/docs/TRIAGE.md`

## Context

- Algebras(ZZ) raises _SageObject__custom_name while Sage resolves subcategory_class during category initialization.
- Algebras(ZZ).DualObjects() fails while Sage/project axiom inference builds modules.homsets._Forms; this is not an algebra constructor issue.
- Free-construction names may appear as abstract spec targets, but callable implementations require Sage-backed routing and refinement.
- Algebra construction is canonicalized to from_multiplication_tensor(multiplication=mu), where mu is a Tensor in T_R(M)[1,2].
- Basis-returning helpers such as center_basis, radical_basis, and derivations_basis should become object-returning methods such as center, radical, and derivations.

## Grounded Spec Contract

Grounding anchors:

- `category_specs/algebras/docs/MAPPING.md`, especially the `Free-Construction Routing`
  and `Multiplication Tensor Constructor` sections and the rows for
  `S.algebra(R, category=AdditiveSemigroups())`,
  `S.algebra(R, category=AdditiveMonoids())`,
  `S.algebra(R, category=AdditiveGroups())`, and
  `FiniteDimensionalAlgebra(k, table, ...)`.
- `category_specs/algebras/docs/SAGE_INVENTORY.md`, especially the constructor rows for
  `Sets.ParentMethods.algebra`, `AlgebraFunctor(base_ring).__call__(G, category=None)`,
  `FreeAlgebra(R, n, names)`, and `FiniteDimensionalAlgebra(k, table, ...)`.
- `category_specs/tensor_algebra_components/docs/MAPPING.md` and
  `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md` for the canonical
  `(1,2)` multiplication-tensor owner and the admitted constructor shapes that feed it.
- `category_specs/modules/docs/MAPPING.md` for the plain-set routing
  `S.free_module(R) -> Modules(R).Constructors().CombinatorialFreeModule(...)`.

Grounded owner rule for this leaf:

- Free algebra constructors on multiplicative or additive source objects are owned by
  `Algebras(R).Constructors()` under explicit source-sensitive names such as
  `free_algebra_from_semigroup`, `free_algebra_from_monoid`,
  `free_algebra_from_group`, `free_algebra_from_additive_semigroup`,
  `free_algebra_from_additive_monoid`, and `free_algebra_from_additive_group`.
- Table- or product-data admission for finite-rank algebras is owned first by
  `TensorAlgebraComponents(R).Constructors()`. The only canonical algebra product input
  is `from_multiplication_tensor(multiplication=mu)` with `mu` a `Tensor` in
  `T_R(M)[1,2]`.

Required hypotheses and codomains:

- additive and multiplicative free-construction routes must name the source category
  whose law supplies multiplication and must return an object in the mapped target
  algebra category (`MagmaticAlgebras(R)`, `AssociativeAlgebras(R)`, or `Algebras(R)`);
- the tensor route requires a tensor with `tensor_type() == (1, 2)` and base module `M`;
  the returned object is an algebra object over `R` whose owner category is determined
  by the proven laws carried by that tensor;
- the plain-set Sage route remains rejected as algebra vocabulary and maps to the
  module constructor path instead.

Rejection/retirement condition:

- reject any algebra constructor proposal that exposes raw Sage `category=` ambiguity,
  list/table/matrix-shaped multiplication data directly on `Algebras(R)`, or routes the
  plain-set `S.algebra(R)` surface into `Algebras(R)` rather than `Modules(R)`.

## Execution Result

The constructor admission decision is now grounded in the public spec surface:

- `category_specs/algebras/docs/MAPPING.md` records explicit constructor names for
  multiplicative and additive source categories, including
  `free_algebra_from_additive_semigroup`,
  `free_algebra_from_additive_monoid`, and
  `free_algebra_from_additive_group`.
- `category_specs/algebras/__init__.py` already exposes the corresponding
  `Algebras(R).Constructors()` methods and routes them through Sage's selected source
  category without exposing a raw public `category=` option bag.
- finite-dimensional table/list/matrix product data is not admitted directly on
  `Algebras(R)`: `from_multiplication_tensor(multiplication=mu)` is the canonical
  algebra constructor, and tensor interop data belongs first to
  `TensorAlgebraComponents(R).Constructors()`.
- the plain-set Sage `S.algebra(R)` route remains rejected as algebra vocabulary and
  maps to `S.free_module(R)` / `Modules(R).Constructors().CombinatorialFreeModule(...)`.

No new constructor or axiom code was needed in this pass. The remaining
`Algebras(ZZ)` and `DualObjects()` failures recovered from the historical triage are
not algebra-constructor admission issues.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No new implementation blocker was discovered during this docs/spec pass; recovered smoke failures remain non-constructor frontiers.
- [x] No algebra category initialization or constructor code changed, so the `algebras/smoketest.sage` trigger did not apply in this pass.
- [x] Plain-set `S.algebra(R)` remains routed to `free_module` over `Modules(R)`, not to `Algebras(R)`.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Recovered historical algebra triage from
  `plans/category_specs/algebras/docs/TRIAGE.md`, confirmed the explicit additive
  constructor names and multiplication-tensor constructor route in mapping/code, and
  marked the algebra-constructor admission leaf ready for review without introducing
  raw Sage `category=` or table-data public surfaces.
- 2026-05-07: 6-gate protocol review by Hermes subagent. G1, G2, G3, G4, G5, G6 all
  pass. See Review Log below.

## 6-Gate Protocol Review Log

*Review conducted 2026-05-07 by Hermes subagent. Evidence gathered from filesystem
checks of all grounding anchors, git provenance verification, and direct inspection
of the `category_specs/algebras/__init__.py` source.*

### Gate 1: Source Grounding — PASS

**Status: PASS**

All grounding anchors claimed in the spec's "Grounded Spec Contract" section (lines
53-69) exist and are verifiable:

- **`category_specs/algebras/docs/MAPPING.md`**: Exists at the claimed path. It is a
  redirect to the canonical tracked spec `SPEC-MAPPING-ALGEBRAS.md` (also verified
  to exist). The Free-Construction Routing table (SPEC-MAPPING-ALGEBRAS.md rows
  230-239) contains all eight constructor routes referenced by this leaf spec,
  including the three additive variants:
  `free_algebra_from_additive_semigroup`,
  `free_algebra_from_additive_monoid`, and
  `free_algebra_from_additive_group`.

- **`category_specs/algebras/docs/SAGE_INVENTORY.md`**: Exists at the claimed path.
  Contains constructor rows for `Sets.ParentMethods.algebra`,
  `AlgebraFunctor(base_ring).__call__`, `FreeAlgebra`, and
  `FiniteDimensionalAlgebra` — all referenced by the spec.

- **`category_specs/tensor_algebra_components/docs/MAPPING.md`**: Exists at the
  claimed path (redirect to `SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS.md`, verified).
  Documents the canonical `(1,2)` multiplication-tensor owner and the admitted
  constructor shapes.

- **`category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`**: Exists at
  the claimed path. Documents `FreeModuleTensor`, `TensorFreeModule`,
  `tensor_type()`, `base_module()`, and component interop — all referenced by the
  spec's tensor constructor claims.

- **`category_specs/modules/docs/MAPPING.md`**: Exists at the claimed path (redirect
  to `SPEC-MAPPING-MODULES.md`, verified). Documents the plain-set routing claim
  that `S.algebra(R)` maps to `Modules(R).CombinatorialFreeModule(...)`.

**Git provenance verified (Source Provenance section, lines 37-42)**:

- `git show 8d1c21c^:category_specs/algebras/docs/TRIAGE.md` → correctly fails
  (file lived under `plans/` at that commit).
- `git show 8d1c21c^:plans/category_specs/algebras/docs/TRIAGE.md` → succeeds,
  returning the exact TRIAGE content the spec's Context section summarizes.
- The recovered TRIAGE content confirms: the Algebras(ZZ) `_SageObject__custom_name`
  blocker exists, the DualObjects/forms blocker is not an algebra constructor issue,
  and the canonicalization to `from_multiplication_tensor(multiplication=mu)` is the
  correct algebra constructor route.

**Code grounding verified**:

- `category_specs/algebras/__init__.py` exists and the `Algebras.Constructors` inner
  class (lines 379-651) exposes all six claimed constructor methods:
  `free_algebra_from_semigroup` (line 497),
  `free_algebra_from_monoid` (line 515),
  `free_algebra_from_group` (line 522),
  `free_algebra_from_additive_semigroup` (line 529),
  `free_algebra_from_additive_monoid` (line 547),
  `free_algebra_from_additive_group` (line 557),
  and `from_multiplication_tensor` (line 596).
  Each method routes through Sage source categories internally without exposing a
  raw public `category=` option bag — consistent with the spec's rejection rule.

**No grounding deficiencies found.**

### Gate 2: Completeness — PASS

**Status: PASS**

All five acceptance criteria (lines 15-25) are marked `[x]` and each is verifiable:

1. **"The mathematical owner, public surface, and migration consequence are recorded
   in the relevant MAPPING.md or category spec file"**: The Execution Result section
   (lines 100-117) records explicit constructor names with their owners
   (`Algebras(R).Constructors().free_algebra_from_additive_semigroup`, etc.) and
   their target mapping surface (`SPEC-MAPPING-ALGEBRAS.md` / MAPPING.md).

2. **"No new subtree-local TRIAGE or process document is created"**: Filesystem
   search confirms no `TRIAGE.md` exists under `category_specs/algebras/docs/` or
   `plans/category_specs/algebras/docs/`. Follow-up work is represented as tracker
   items.

3. **"No new implementation blocker was discovered during this docs/spec pass"**:
   The spec correctly identifies the recovered Algebras(ZZ) and DualObjects failures
   as "non-constructor frontiers" and records that they remain tracked elsewhere.

4. **"No algebra category initialization or constructor code changed, so the
   algebras/smoketest.sage trigger did not apply"**: The spec accurately states
   "No new constructor or axiom code was needed in this pass" — the code already
   existed. This is a valid reason for not triggering the smoke test.

5. **"Plain-set S.algebra(R) remains routed to free_module over Modules(R)"**: The
   Execution Result (line 117) and Grounded Spec Contract (lines 92-98) both record
   this routing decision, consistent with the modules MAPPING.md and the upstream
   MAPPING-ALGEBRAS spec.

All required hypotheses and codomains are stated (lines 83-92), covering the
additive/multiplicative free-construction routes, the tensor route, and the
plain-set rejection. No dangling obligations detected.

### Gate 3: Mathematical Correctness — PASS

**Status: PASS**

**Category hierarchy correct:**

- `MagmaticAlgebras(R)` = R-modules with bilinear multiplication (no associativity,
  no unit). Verified in `sage/categories/magmatic_algebras.py` and project
  `__init__.py` line 142 (class `AssociativeAlgebras` has
  `_base_category_class_and_axiom = (MagmaticAlgebras, "Associative")`).

- `AssociativeAlgebras(R)` = associative, not necessarily unital. Code verified.

- `Algebras(R)` = associative unital endpoint. Code verified at line 324
  (`super_categories` includes `AssociativeAlgebras(R)`).

**Free construction routing mathematically sound:**

- `Sets() → Algebras(R).Constructors().free_algebra_from_set(S)` — the free
  associative unital algebra on generators. Correct: the free R-algebra on a set
  has no pre-existing algebraic relations, so the result is associative and unital.
- `Magmas() → MagmaticAlgebras(R).Constructors().free_algebra_from_magma(S)` —
  bilinear extension of a magma operation yields a non-associative, non-unital
  algebra. Correct routing to the weakest category whose objects satisfy the laws.
- `Semigroups() → AssociativeAlgebras(R).Constructors().free_algebra_from_semigroup(S)` —
  semigroup algebra is associative but not necessarily unital. Correct.
- `Monoids()/Groups() → Algebras(R).Constructors().free_algebra_from_monoid/group(S)` —
  monoid/group algebras include the unit element. Correct.
- Additive variants follow the same pattern with additively written operations.
  Correct.

**Multiplication tensor constructor:**

- `from_multiplication_tensor(multiplication=mu)` where `mu` is a tensor in
  `T_R(M)[1, 2]`. A bilinear map M×M→M corresponds to structure constants
  c^k_{i,j} with one upper index (output) and two lower indices (inputs). The
  tensor type (1,2) correctly represents this data. The constructor delegates
  coordinate-to-tensor conversion to `TensorAlgebraComponents(R).Constructors()`,
  which is the correct separation of concerns.

**Plain-set routing:**

- Sage's `S.algebra(R)` for plain `Sets()` is correctly identified as a free
  module construction (`CombinatorialFreeModule`), not an algebra construction.
  The spec routes this to `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)`,
  preserving Sage functionality without admitting the Sage name as algebra
  vocabulary.

No mathematical errors, omissions, or category-theoretic contradictions found in
the routing, the tensor type validation, or the owner separation.

### Gate 4: Nonmathematical Rejection — PASS

**Status: PASS**

The spec's rejection/retirement condition (lines 94-98) correctly rejects three
categories of nonmathematical surface:

1. **Raw Sage `category=` ambiguity**: The spec requires that source-category
   selection be encoded in the constructor name, not in a runtime string. Verified
   in code: `_sage_algebra_from_source` and `_sage_algebra_from_source_with_target`
   accept source categories as typed Sage category objects, not strings. The public
   constructor names (`free_algebra_from_additive_group`, etc.) encode the source
   category semantically.

2. **List/table/matrix-shaped multiplication data directly on `Algebras(R)`**: The
   spec routes coordinate data to `TensorAlgebraComponents(R).Constructors()` and
   admits only `from_multiplication_tensor(multiplication=mu)` on `Algebras(R)`.
   Verified in code: the `from_multiplication_tensor` method (line 596) is the sole
   product-input constructor; all table/matrix conversion happens internally
   through `_right_multiplication_table` (line 567).

3. **Plain-set `S.algebra(R)` surface into `Algebras(R)`**: The spec correctly
   routes this to `Modules(R)` instead. This is mathematically correct because
   Sage's `Sets().example().algebra(R)` constructs a free module
   (`CombinatorialFreeModule`), not a free algebra — it has no product structure.

No nonmathematical surface is admitted. No option bags, underscored helpers,
implementation details, or raw Sage interop are exposed as public API.

### Gate 5: Routing — PASS

**Status: PASS**

All constructor routing is unambiguous:

| Source structure | Constructor route | Owner |
|---|---|---|
| Multiplicative magmas/semigroups/monoids/groups | `free_algebra_from_magma` / `_semigroup` / `_monoid` / `_group` | `MagmaticAlgebras(R)` / `AssociativeAlgebras(R)` / `Algebras(R).Constructors()` |
| Additive semigroups/monoids/groups | `free_algebra_from_additive_semigroup` / `_additive_monoid` / `_additive_group` | `AssociativeAlgebras(R)` / `Algebras(R).Constructors()` |
| Finite-rank table/product data | First `TensorAlgebraComponents(R).Constructors()`, then `Algebras(R).Constructors().from_multiplication_tensor(multiplication=mu)` | `TensorAlgebraComponents(R)` → `Algebras(R)` |
| Plain-set Sage `S.algebra(R)` | `S.free_module(R)` → `Modules(R).Constructors().CombinatorialFreeModule(...)` | `Modules(R)` |

No ambiguity: each source structure has a single named constructor route. The
additive and multiplicative variants are explicitly disambiguated by name. The
finite-rank path has a clear two-step pipeline (tensor interop → algebra
constructor). Cross-owner routing is clearly stated.

No orphaned constructors detected. No unresolved routing conflicts.

### Gate 6: Obligation Preservation — PASS

**Status: PASS**

**No weakening detected:**

- The spec does not delete, narrow, or relax any existing constructor obligations.
  It documents and admits constructors that were identified as gaps in the deleted
  TRIAGE.

- The plain-set Sage `S.algebra(R)` route is explicitly preserved through
  `S.free_module(R)` → `Modules(R)`, so no Sage functionality is lost.

- Sage compatibility is maintained: all constructor methods in
  `Algebras(R).Constructors()` delegate to Sage's `source.algebra(R, category=...)`
  internally and refine the result to project category surfaces.

- The remaining `Algebras(ZZ)` and `DualObjects()` failures from the historical
  triage are explicitly noted as tracked elsewhere, not swept under the rug.

- Acceptance criterion 4 explicitly records that `algebras/smoketest.sage` was not
  applicable because no code changed — this is correct scoping, not test avoidance.

**No obligation deletion, no spec weakening, no loss of functionality.**

### Overall Recommendation: ACCEPT

The spec correctly records the algebra constructor admission decision with verified
source grounding, correct mathematics, proper nonmathematical rejection, clear
routing, and full obligation preservation. All acceptance criteria are satisfied.
No deficiencies found in any gate.

The spec can advance from `needs-review` to `needs-human-input` (or equivalent
gatekeeping status) for final human confirmation.

### Evidence Registry

| Evidence item | Verification method | Result |
|---|---|---|
| TRIAGE.md git path 1 (short path, fails) | `git show 8d1c21c^:category_specs/...` | Correctly fails as spec predicts |
| TRIAGE.md git path 2 (plans path, succeeds) | `git show 8d1c21c^:plans/category_specs/...` | Content matches spec Context |
| algebras MAPPING.md | Filesystem check | Exists (redirect) |
| algebras SAGE_INVENTORY.md | Filesystem check | Exists |
| tensor_algebra_components MAPPING.md | Filesystem check | Exists (redirect) |
| tensor_algebra_components SAGE_INVENTORY.md | Filesystem check | Exists |
| modules MAPPING.md | Filesystem check | Exists (redirect) |
| algebras/__init__.py constructors | Direct code inspection | All 7 methods verified |
| Dependency PHASE-ALGEBRA-... exists | Filesystem check | Exists (14 references in plan-dag) |
| No new TRIAGE.md created | Filesystem search | Confirmed absent |
| Free-Construction Routing table | Read SPEC-MAPPING-ALGEBRAS.md lines 230-239 | All 8 routes present |
