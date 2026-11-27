---
id: SPEC-01KQN9J3WVW531PDTHEY094GVG-PRESERVE-ALGEBRA-BASIS-RETURNING-SAGE-HELPERS-AS-OBJECT-RETURNING-PROJEC
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
title: Preserve algebra basis-returning Sage helpers as object-returning project methods
  such as center radical and derivations
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
  failed category assertions remain unrelated frontiers.
- No algebra category initialization or constructor code changed, so the `algebras/category_obligations.sage`
  trigger did not apply in this pass.
- Plain-set `S.algebra(R)` remains routed to `free_module` over `Modules(R)`, not
  to `Algebras(R)`.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Preserve algebra basis-returning Sage helpers as object-returning project methods such as center radical and derivations
## Summary

The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ), a
module hom-category/forms blocker for DualObjects, and constructor admission gaps.

## Source Provenance

- The requested recovery path `git show 8d1c21c^:category_specs/algebras/docs/TRIAGE.md`
  fails because the file still lived under `plans/category_specs/algebras/docs/TRIAGE.md`
  at that parent commit.
- Exact recovered prior content came from
  `git show 8d1c21c^:plans/category_specs/algebras/docs/TRIAGE.md`.
- Original migrated line: `Preserve algebra basis-returning Sage helpers as object-returning project methods such as center radical and derivations from category_specs/algebras/docs/TRIAGE.md`

## Context

- Algebras(ZZ) raises _SageObject__custom_name while Sage resolves subcategory_class during category initialization.
- Algebras(ZZ).DualObjects() fails while Sage/project axiom inference builds modules.homsets._Forms; this is not an algebra constructor issue.
- Free-construction names may appear as abstract spec targets, but callable implementations require Sage-backed routing and refinement.
- Algebra construction is canonicalized to from_multiplication_tensor(multiplication=mu), where mu is a Tensor in T_R(M)[1,2].
- Basis-returning helpers such as center_basis, radical_basis, and derivations_basis should become object-returning methods such as center, radical, and derivations.

## Grounded Spec Contract

Grounding anchors:

- `category_specs/algebras/docs/MAPPING.md` rows for `basis()`, `one_basis()`,
  `algebra_generators()`, `center_basis()`, `radical_basis()`, `derivations_basis()`,
  and `annihilator_basis(...)`.
- `category_specs/algebras/docs/SAGE_INVENTORY.md`, especially the method rows for
  `AlgebrasWithBasis.ParentMethods` and
  `FiniteDimensionalAlgebrasWithBasis.ParentMethods`.

Grounded owner rule for this leaf:

- Sage basis-returning helpers are inventory evidence, not the public project codomain.
  The public owners stay on the algebra parent surface and return the mathematical
  object named by the helper: `center() -> Algebra`, `radical() -> AlgebraIdeal`,
  `derivations() -> RModule`, and `annihilator(...) -> AlgebraIdeal`.
- Basis data remains structure recoverable from the returned object when that object
  lies in `WithBasis()`. The project does not admit separate public surfaces whose only
  codomain is a distinguished basis list or basis-index family.

Required hypotheses and codomains:

- `center_basis()` grounds `center() -> Algebra`, with the center owned as the
  subalgebra spanned by that basis;
- `radical_basis()` grounds `radical() -> AlgebraIdeal`, with the radical owned as the
  ideal spanned by that basis;
- `derivations_basis()` grounds `derivations() -> RModule`, with any chosen basis
  recovered from the derivation object itself;
- `annihilator_basis(...)` grounds `annihilator(...) -> AlgebraIdeal`;
- `one_basis()` does not create a public basis-index API; it grounds `one() -> AlgebraElement`
  and constructor unit data when the unit happens to be a basis vector.

Rejection/retirement condition:

- reject any spec edit that promotes a Sage basis helper itself to the public return
  object when the mapped mathematical object is an algebra, ideal, module, or element.

## Execution Result

The basis-helper migration is already grounded and preserved:

- `category_specs/algebras/docs/MAPPING.md` maps Sage `center_basis()` to
  `center() -> Algebra`, `radical_basis()` to `radical() -> AlgebraIdeal`,
  `derivations_basis()` to `derivations() -> RModule`, and
  `annihilator_basis(...)` to `annihilator(...) -> AlgebraIdeal`.
- `category_specs/algebras/__init__.py` exposes the object-returning abstract methods
  `center`, `radical`, `derivations`, and `annihilator` on the algebra parent surface.
- `AlgebraIdeal` remains the algebra-ideal object in `Algebras(R).Ideals(A)`, backed by
  module-subobject structure rather than by a bare basis list or a ring ideal alias.
- Sage's basis helpers remain inventory evidence for how to build those objects in a
  later implementation pass; they are not public project codomains.

No code change was required in this pass. The historical `Algebras(ZZ)` and
`DualObjects()` failed category assertions are not basis-helper ownership issues.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No new implementation blocker was discovered during this docs/spec pass; recovered failed category assertions remain unrelated frontiers.
- [x] No algebra category initialization or constructor code changed, so the `algebras/category_obligations.sage` trigger did not apply in this pass.
- [x] Plain-set `S.algebra(R)` remains routed to `free_module` over `Modules(R)`, not to `Algebras(R)`.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## 6-Gate Protocol Review Log

*Review conducted 2026-05-07. Evidence gathered from the working tree at
`/home/dzack/research`, installed Sage 10.7 source files at
`/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/`, and git
history at commit `8d1c21c`.*

### Gate 1: Source Grounding — PASS (with one annotation)

**Status: PASS**

**Verified anchors:**

- **Git provenance confirmed.** Commit `8d1c21c` is a valid commit object. The
  TRIAGE.md recovery path `8d1c21c^:plans/category_specs/algebras/docs/TRIAGE.md`
  returns the expected file containing the line: "Sage exposes helpers such as
  `center_basis()`, `radical_basis()`, and `derivations_basis()`. Project methods
  should return the algebraic object spanned by that basis..." This matches the
  "Original migrated line" quoted in the spec's Source Provenance section.

- **SAGE_INVENTORY.md exists** at `category_specs/algebras/docs/SAGE_INVENTORY.md`
  and documents the following relevant Sage method surfaces:
  - Row 51: `AlgebrasWithBasis.ParentMethods` — `basis()`, `one_basis()`, `one()`,
    `algebra_generators()`, `product_on_basis`.
  - Row 55: `FiniteDimensionalAlgebrasWithBasis.ParentMethods` — `radical_basis()`,
    `radical()`, `center_basis()`, `center()`, plus ideal and subalgebra methods.
  - Row 52: `AlgebrasWithBasis.ElementMethods` — `__invert__()` for basis-unit
    scalar multiples (evidence for `one_basis() → one()`).

- **`__init__.py` exists** at `category_specs/algebras/__init__.py` and exposes the
  claimed abstract methods on `_AlgebraParentMethods`:
  - Line 197: `center() -> Algebra`
  - Line 202: `radical() -> AlgebraIdeal`
  - Line 252: `derivations() -> RModule`
  - Line 257: `annihilator(elements) -> AlgebraIdeal`

- **MAPPING.md** at `category_specs/algebras/docs/MAPPING.md` is a redirect stub
  pointing to `SPEC-MAPPING-ALGEBRAS.md`. The actual mapping rows live in that spec:
  - Row 111: `center_basis()` → `center() -> Algebra`
  - Row 110: `radical_basis()` → `radical() -> AlgebraIdeal`
  - Row 105: `derivations_basis()` → `derivations() -> Der(A)`
  - Row 191: `annihilator_basis(...)` → `annihilator(...) -> AlgebraIdeal`

- **Sage source cross-verification:**
  - `derivations_basis()` confirmed at
    `sage/categories/magmatic_algebras.py` line 282
    (MagmaticAlgebras.WithBasis.FiniteDimensional.ParentMethods).
  - `annihilator_basis()` confirmed at
    `sage/categories/finite_dimensional_algebras_with_basis.py` line 367.
  - `center_basis()` and `radical_basis()` confirmed in
    `sage/categories/finite_dimensional_algebras_with_basis.py` (lines 349 and 69
    respectively, per the mapping spec's own review).

**Annotation (non-blocking):** The spec's Grounded Spec Contract section (line
56-61) cites `category_specs/algebras/docs/MAPPING.md` as containing rows for
`basis()`, `one_basis()`, `algebra_generators()`, `center_basis()`,
`radical_basis()`, `derivations_basis()`, and `annihilator_basis(...)`. The actual
MAPPING.md file at that path is a 7-line redirect stub; the substantive rows live
in `SPEC-MAPPING-ALGEBRAS.md`. This is a documentation indirection, not a grounding
failure — the rows exist and are verified. The spec would benefit from citing the
canonical mapping spec path directly.

### Gate 2: Sage Surface Completeness — PASS (with one annotation)

**Status: PASS**

**Surface accounting:**

- `center_basis()` — inventoried in SAGE_INVENTORY.md row 55. Mapped to
  `center() -> Algebra`. Sage also has a separate `center()` method (row 55),
  returning a submodule. The spec correctly identifies that the project surface
  should be `center() -> Algebra` (the center as algebra, not bare submodule).

- `radical_basis()` — inventoried in SAGE_INVENTORY.md row 55. Mapped to
  `radical() -> AlgebraIdeal`. Sage also has a separate `radical()` method (row
  55), returning a submodule with `ambient()` and `basis()`. The spec correctly
  maps to `AlgebraIdeal`, the project's ideal object.

- `derivations_basis()` — **NOT** listed in the main SAGE_INVENTORY.md method
  surface table. It was discovered as an "extra source-only surface" during mapping
  reconciliation (SPEC-MAPPING-ALGEBRAS.md line 74) in
  `sage/categories/magmatic_algebras.py`. The basis-returning spec correctly
  includes it in the mapping set.

- `annihilator_basis(...)` — **NOT** explicitly listed in SAGE_INVENTORY.md's
  method surface table. It appears in Sage source at
  `finite_dimensional_algebras_with_basis.py` line 367. The basis-returning spec
  correctly includes it.

- `one_basis()` — inventoried in SAGE_INVENTORY.md rows 14, 36, 51. Mapped to
  `one() -> AlgebraElement`. Correct.

- `basis()` — inventoried in SAGE_INVENTORY.md rows 14, 51. Cited as grounding
  anchor in the spec but not individually mapped (basis itself isn't a
  "basis-returning helper" of a derived object — it returns the algebra's own
  distinguished basis). Acceptable omission for this leaf spec.

**Annotation (non-blocking):** `derivations_basis` and `annihilator_basis` are
absent from the main SAGE_INVENTORY.md method surface table, appearing only as
extra discoveries in the mapping reconciliation. The SAGE_INVENTORY.md should be
updated to include them under `FiniteDimensionalAlgebrasWithBasis.ParentMethods` or
a new row for `MagmaticAlgebras.WithBasis.FiniteDimensional.ParentMethods`. The
basis-returning spec's surface completeness claim is still valid because the Sage
sources do contain the methods; the gap is in the inventory, not in this spec.

### Gate 3: Mathematical Correctness — PASS

**Status: PASS**

Each basis-helper-to-object mapping is mathematically verified:

1. **`center_basis()` → `center() -> Algebra`**
   - **Definition:** The center `Z(A) = {z ∈ A : za = az for all a ∈ A}` is a
     commutative subalgebra of A.
   - **Sage evidence:** `center_basis()` returns a list of basis vectors spanning
     Z(A). Sage's `center()` already returns the center as a submodule with
     `ambient()`.
   - **Project mapping:** `center() -> Algebra` is correct — the center is an
     algebra in its own right (commutative subalgebra). The basis of the center is
     recoverable from the returned Algebra object when it lies in `WithBasis()`.
   - **Verdict:** Mathematically sound.

2. **`radical_basis()` → `radical() -> AlgebraIdeal`**
   - **Definition:** The Jacobson radical `J(A)` is the intersection of all maximal
     left ideals. For finite-dimensional associative algebras, it is the maximal
     nilpotent ideal.
   - **Sage evidence:** `radical_basis()` returns a basis of J(A). Sage's
     `radical()` returns a submodule with `ambient()` and `basis()`.
   - **Project mapping:** `radical() -> AlgebraIdeal` is correct — the radical is a
     two-sided ideal. `AlgebraIdeal` carries `is_left_ideal()`, `is_right_ideal()`,
     `is_two_sided_ideal()` predicates plus `ambient()`, `ambient_module()`, and
     `inclusion()` from module subobject structure.
   - **Verdict:** Mathematically sound.

3. **`derivations_basis()` → `derivations() -> RModule`**
   - **Definition:** A derivation is an R-linear map `D: A → A` satisfying
     `D(ab) = D(a)b + aD(b)`. Derivations form an R-submodule of `End_R(A)` and a
     Lie algebra under commutator `[D₁, D₂] = D₁∘D₂ - D₂∘D₁`.
   - **Sage evidence:** `derivations_basis()` (magmatic_algebras.py L282) returns a
     list of matrices representing a basis of the derivation space.
   - **Project mapping:** `derivations() -> RModule` captures the module structure.
     The mapping spec notes the richer `Der(A)` type with Lie bracket, but
     `RModule` is the minimal correct type — module structure is always present;
     Lie bracket requires additional category surface. The spec's `__init__.py`
     uses `RModule` (line 252), which is consistent and conservative.
   - **Verdict:** Mathematically sound. The return type is the minimal correct
     structure; Lie algebra enrichment is a future refinement.

4. **`annihilator_basis(...)` → `annihilator(...) -> AlgebraIdeal`**
   - **Definition:** For a subset S ⊆ A, the annihilator `Ann(S) = {a ∈ A : as = 0
     for all s ∈ S}` is a left ideal (right ideal for right annihilator, two-sided
     for `Ann(S) = {a : aS = Sa = 0}`).
   - **Sage evidence:** `annihilator_basis()` returns a basis of the annihilator
     ideal.
   - **Project mapping:** `annihilator(...) -> AlgebraIdeal` is correct.
     `AlgebraIdeal` carries side predicates to distinguish left/right/two-sided
     annihilators.
   - **Verdict:** Mathematically sound.

5. **`one_basis()` → `one() -> AlgebraElement`**
   - **Definition:** The multiplicative identity `1_A ∈ A` satisfying `1_A·a = a·1_A
     = a` for all a ∈ A.
   - **Sage evidence:** `one_basis()` returns the index of the basis vector that
     equals the unit element (when the unit is a basis vector).
   - **Project mapping:** `one() -> AlgebraElement` returns the element itself, not
     its basis index. The basis index is construction/interop data.
   - **Verdict:** Mathematically sound.

**Cross-cutting correctness:** The spec's "Grounded owner rule" (lines 63-71)
correctly states that Sage basis-returning helpers are inventory/implementation
evidence, not the public project codomain. The public surface should return the
mathematical object named by the helper. This is the correct architectural
principle for a category-spec project that aims for a mathematical interface rather
than a Sage wrapper.

### Gate 4: Nonmathematical Rejection — PASS

**Status: PASS**

The spec's rejection condition (lines 85-88) states:

> reject any spec edit that promotes a Sage basis helper itself to the public
> return object when the mapped mathematical object is an algebra, ideal, module,
> or element.

**Assessment:** This is the correct rejection rule. A bare basis list (e.g.,
`center_basis() -> list[AlgebraElement]`) is not a mathematical object — it is a
choice of coordinates for the true mathematical object (the center algebra). The
spec correctly prevents:

- `center_basis()` being exposed as `center_basis() -> list` instead of
  `center() -> Algebra`
- `radical_basis()` being exposed as `radical_basis() -> list` instead of
  `radical() -> AlgebraIdeal`
- `derivations_basis()` being exposed as `derivations_basis() -> list[Matrix]`
  instead of `derivations() -> RModule`
- `annihilator_basis(...)` being exposed as a bare list instead of
  `annihilator(...) -> AlgebraIdeal`
- `one_basis()` being exposed as a basis-index API instead of `one() ->
  AlgebraElement`

**Evidence of correct application:** The Execution Result section (lines 90-106)
confirms that `__init__.py` exposes the object-returning methods (`center`,
`radical`, `derivations`, `annihilator`), not the basis-returning helpers. The spec
gates against regression — future edits must preserve this mapping.

### Gate 5: Ambiguity Routing — PASS

**Status: PASS**

**Resolved ambiguities:**

1. **Basis data recovery from returned objects** (line 69-71):
   > "Basis data remains structure recoverable from the returned object when that
   > object lies in `WithBasis()`."
   - This resolves the concern that hiding `center_basis()` removes useful
     functionality. The center algebra, when it lives in `WithBasis()`, carries its
     own basis. Users call `center().basis()` to recover what Sage's
     `center_basis()` provided. No loss of capability.

2. **`one_basis()` routing** (lines 82-83):
   > "`one_basis()` does not create a public basis-index API; it grounds `one() ->
   > AlgebraElement` and constructor unit data when the unit happens to be a basis
   > vector."
   - Correctly routes the Sage surface to the element-level API while preserving
     the basis index as constructor implementation data.

3. **Plain-set `S.algebra(R)` routing** (acceptance criteria line 24-25):
   > "Plain-set `S.algebra(R)` remains routed to `free_module` over `Modules(R)`,
   > not to `Algebras(R)`."
   - Correctly separates the Sage plain-set algebra construction (which produces a
     free module, not an algebra) from the project's algebra constructors.

4. **`AlgebraIdeal` vs ring ideal** (line 100-101):
   > "`AlgebraIdeal` remains the algebra-ideal object in `Algebras(R).Ideals(A)`,
   > backed by module-subobject structure rather than by a bare basis list or a
   > ring ideal alias."
   - Resolves the ambiguity of what an algebra ideal is: a module subobject with
     multiplicative closure, not a ring ideal.

**Annotation (non-blocking):** The spec maps `derivations_basis()` to
`derivations() -> RModule` (line 79 and `__init__.py` line 252), while the mapping
spec (SPEC-MAPPING-ALGEBRAS.md row 105) maps it to `derivations() -> Der(A)`. This
is a minor type-naming inconsistency between the two specs. `Der(A)` implies Lie
algebra structure (making the object richer than a bare `RModule`), while `RModule`
is the conservative minimal type. Both are correct — `Der(A)` is an `RModule` with
extra Lie structure. The basis-returning spec is slightly more conservative. This
does not block review; implementers should use the richer type when the Lie algebra
category surface is available and fall back to `RModule` otherwise.

### Gate 6: Obligation Preservation — PASS

**Status: PASS**

Every Sage basis helper obligation is elevated to a higher-level mathematical
object. No capability is lost — basis data remains recoverable from the returned
objects.

| Sage surface | Project surface | Obligation status |
| --- | --- | --- |
| `center_basis()` | `center() -> Algebra` | **Preserved and elevated.** The center algebra carries its own basis when in `WithBasis()`. Center structural properties (commutativity, subalgebra inclusion) are now first-class. |
| `radical_basis()` | `radical() -> AlgebraIdeal` | **Preserved and elevated.** The radical ideal carries `ambient()`, `ambient_module()`, `inclusion()`, and side predicates. Basis recoverable from the ideal when it has basis data. |
| `derivations_basis()` | `derivations() -> RModule` | **Preserved and elevated.** The derivation module carries its R-module structure (and Lie bracket when enriched). Matrices representing derivations on a chosen basis are recoverable from the module object. |
| `annihilator_basis(...)` | `annihilator(...) -> AlgebraIdeal` | **Preserved and elevated.** The annihilator ideal carries side predicates (`is_left_ideal()`, etc.) and subobject structure. |
| `one_basis()` | `one() -> AlgebraElement` | **Preserved and elevated.** The unit element is returned as an algebraic object, not a basis index. The basis index is retained as constructor implementation data. |

**No weakening detected.** The spec explicitly gates against regression by
rejecting bare basis-list codomains (Gate 4). The Execution Result section confirms
that the `__init__.py` already exposes the object-returning methods and that Sage's
basis helpers "remain inventory evidence for how to build those objects in a later
implementation pass."

**No obligation dropped.** The spec does not remove any method from the algebra
surface. It clarifies the mathematical owner and return type of each operation
while preserving the underlying Sage capability through the
basis-on-returned-object recovery path.

### Overall Verdict: PASS

The ALGEBRA-BASIS-RETURNING spec is mathematically correct, well-grounded in Sage
source evidence, and correctly gates against bare basis-list codomains. All six
gates pass, with only non-blocking annotations:

1. **G1 annotation:** MAPPING.md is a redirect stub; cite `SPEC-MAPPING-ALGEBRAS.md`
   directly for the actual mapping rows.
2. **G2 annotation:** `derivations_basis` and `annihilator_basis` are missing from
   the main SAGE_INVENTORY.md method table (they were extra discoveries). Update
   the inventory.
3. **G5 annotation:** Minor return-type naming inconsistency between `RModule` (this
   spec) and `Der(A)` (mapping spec) for derivations. Both are correct; `Der(A)`
   should be used when Lie algebra category surface is available.

No blocking deficiencies. The spec is ready to advance past review.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Recovered historical algebra triage from
  `plans/category_specs/algebras/docs/TRIAGE.md`, confirmed the object-returning
  `center`, `radical`, `derivations`, and `annihilator` surfaces in mapping/code, and
  marked the basis-helper preservation leaf ready for review without admitting raw
  basis-list codomains.
- 2026-05-07: 6-Gate Protocol review completed. All gates PASS. Three non-blocking
  annotations recorded (G1: MAPPING.md redirect stub citation; G2: inventory gaps
  for derivations_basis/annihilator_basis; G5: derivations return-type naming
  inconsistency). No blocking deficiencies found.
