---
id: TASK-1777748120716-ZUYAHM-MOVE-NONTRIVIAL-ALGEBRA-CONSTRUCTION-OUT-OF-CATEGORY-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
dependsOn: []
title: Move nontrivial algebra construction out of category constructors
status: complete
priority: high
description: Move nontrivial algebra construction out of category constructors
successCriteria:
- The card names the canonical source rows that define the algebra-constructor boundary.
- Public algebra category constructors are limited to admitted lightweight routing and
  refinement surfaces, not raw heavy constructors such as Zmod, CyclotomicField,
  NumberField, or generic Sage option bags.
- Free algebra routes are source-category-selected named methods; Sage's generic
  category= disambiguation is not exposed as project API.
- Finite-dimensional algebra construction from tables, matrices, or module-element
  data is routed through TensorAlgebraComponents before
  Algebras(R).Constructors().from_multiplication_tensor.
- Relevant algebra category-obligation example evidence is recorded without weakening mapping decisions or
  category-obligation example obligations.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING
---
# Move nontrivial algebra construction out of category constructors
Source: pasted backlog 2026-05-02.

Task: move nontrivial algebra construction (Zmod, Cyclotomic, NumberField, etc.) out of category constructors, restrict to lightweight wrapper logic.

## Source Provenance

- Canonical algebra mapping:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-ALGEBRAS.md`.
- Constructor source-category rows in `SPEC-MAPPING-ALGEBRAS` define the admitted public
  routes: `S.free_algebra(R)` for the selected source category routes to named
  constructors such as `free_algebra_from_set`, `free_algebra_from_monoid`,
  `free_algebra_from_group`, and their additive/magma/semigroup variants.
- The same mapping rejects Sage's generic `category=` disambiguation as public project
  API. The source category, not a runtime option bag, chooses the constructor.
- The multiplication tensor section in `SPEC-MAPPING-ALGEBRAS` defines the canonical
  finite-rank algebra constructor:
  `Algebras(R).Constructors().from_multiplication_tensor(multiplication=mu)`, with
  tables, matrices, module-element matrices, and right-multiplication data routed
  first through `TensorAlgebraComponents(R).Constructors()`.
- Implementation surface:
  `category_specs/algebras/__init__.py`, especially the constructor methods on
  `Algebras(R).Constructors()`.

## Grounded Boundary

The executable obligation is not to delete all Sage-backed construction. It is to keep
`Algebras(R).Constructors()` as a category-spec routing/refinement namespace whose
public inputs are mathematically named source objects or canonical tensor objects. Heavy
raw algebra constructors such as `Zmod`, `CyclotomicField`, `NumberField`, generic Sage
option bags, and table/matrix-shaped finite-dimensional algebra calls do not become
public algebra category constructors here. When they are mathematically relevant, they
belong to their own ring/field/source-object owners or to tensor-component interop
before algebra construction.

Admitted algebra constructor routes are therefore:

- true free associative algebra on a finite set of generators, with a recorded
  generator presentation;
- source-category-selected algebra routes from magmas, semigroups, monoids, groups,
  additive semigroups, additive monoids, and additive groups;
- the canonical finite-rank multiplication-tensor route after
  `TensorAlgebraComponents` has converted coordinate/table/matrix data into a tensor
  `mu` with `tensor_type() == (1, 2)`.

## Complexity Justification
- Owner: C77
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Move nontrivial algebra construction out of category constructors
- Why this specific score:
  - This task is high-coupling by design: lifting substantial algebra-construction behavior out of category constructors affects constructor semantics, import layering, and initialization pathways across multiple algebra families (Zmod, Cyclotomic, NumberField).
- Item-specific evidence:
  - The text explicitly calls out nontrivial constructions (`Zmod`, `Cyclotomic`, `NumberField`) and a hard behavior boundary (`lightweight wrapper logic`), which increases migration and compatibility risk.
  - Complexity is validated by expected downstream behavior shifts rather than small typed annotation edits.

## Work Log

- 2026-05-06 implementation review: the current algebra constructor surface does
  not directly construct `Zmod`, cyclotomic fields, number fields, or comparable
  nontrivial algebra parents inside category constructors. It keeps category
  constructors to named routing/refinement logic over Sage-backed objects:
  `FreeAlgebra`, source-category `S.algebra(R, category=...)`, and
  `FiniteDimensionalAlgebra` reached only after tensor-component construction.
  This matches the boundary in `SPEC-MAPPING-ALGEBRAS` that nontrivial raw
  constructor shapes are not public algebra category constructors.
- 2026-05-06 validation: `just --justfile category_specs/justfile category-obligation-file
  algebras/category_obligations.sage` passes. Status moved to `needs-agent-review`; this does
  not mark the card accepted or complete.
- 2026-05-06 Gate 1 rework: after independent review found that the card remained
  backlog-shaped, added source provenance, the grounded algebra-constructor boundary,
  and non-tautological success criteria naming the exact spec rows and owner split.

## Negative Finding

- Searched: `rg -n "Zmod|Cyclotomic|NumberField" category_specs/algebras`;
  `category_specs/algebras/__init__.py`; `SPEC-MAPPING-ALGEBRAS`.
- Found: no direct algebra-constructor implementation route for `Zmod`,
  cyclotomic fields, or number fields in `category_specs/algebras`; the code and
  spec route constructor work through named lightweight Sage-backed routes and
  refinement.
- Conclusion: inference based on the checked algebra subtree and canonical
  mapping spec: the current algebra constructor surface satisfies this card's
  boundary by keeping these heavy constructors out of category constructors.
- Confidence: High.
- Gaps: other subtrees may still mention these constructors for their own module,
  ring, or field surfaces; that is outside this algebra-constructor card.

## Review Log

### Review 2026-05-06 (Beauvoir)

**Gates passed:** none
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 1 Finding: Definition Grounding

- The card body was still grounded only as `Source: pasted backlog 2026-05-02`.
- The success criterion was tautological and did not name the controlling spec rows,
  exact admitted constructor surfaces, or replacement owners for moved behavior.
- The implementation evidence looked directionally consistent with the task intent,
  but Gate 1 failed before later gates mattered.

#### Rework

- Added source provenance for `SPEC-MAPPING-ALGEBRAS`, the source-category constructor
  table, the rejection of Sage `category=` as public API, and the multiplication-tensor
  constructor boundary.
- Replaced the tautological success criterion with concrete acceptance conditions about
  lightweight routing, heavy-constructor exclusion, source-category-selected free
  algebra routes, tensor-component handoff, and non-weakening validation.
- Recorded the grounded executable boundary so future review can check the actual
  implementation against named mathematical owners rather than backlog wording.

### Status correction 2026-05-09

Human feedback clarified that constructor cards must distinguish mathematical owner,
human-facing named-constructor convention, and code-maintenance owner. `Zmod`,
cyclotomic fields, and number fields are conventionally ring/field constructor names,
while aggregate surfaces such as `Cat().Constructors()` may expose the total user
entry point. This card's algebra-subtree finding is agent-reviewable; any broader
named-constructor convention question should be a separate decision, not a reason to
hold this card in `needs-human-input`.

## 6-Gate Protocol Review Log

*Review conducted 2026-05-09. Evidence from current implementation at
`/home/dzack/research/category_specs/algebras/__init__.py` (706 lines),
`/home/dzack/research/category_specs/algebras/category_obligations.sage` (225 lines),
and controlling spec `SPEC-MAPPING-ALGEBRAS.md`.*

### Gate 1: Definition Grounding — PASS

**Status: PASS**

The card body names the exact controlling spec rows and grounded boundary.
No tautological or circular criteria remain. All required source provenance is
present and verifiable:

- **Controlling spec cited**: `SPEC-MAPPING-ALGEBRAS.md` (card lines 36-51,
  "Source Provenance" section). The Free-Construction Routing table at spec
  lines 230-240 names all 8 source-category → constructor-target rows.
  **Filesystem evidence**: `read_file(SPEC-MAPPING-ALGEBRAS.md, offset=230,
  limit=10)` confirms the 8-row table exists at those exact line numbers.

- **Success criteria are concrete and non-tautological** (card lines 12-23):
  each names a specific boundary condition (lightweight routing only, heavy
  constructor exclusion, source-category-selected free algebra routes,
  tensor-component handoff, non-weakening validation). Compare the earlier
  tautological criterion recorded at card lines 127-130 in the 2026-05-06
  review.

- **Grounded executable boundary** (card lines 53-73, "Grounded Boundary"):
  explicitly lists admitted routes and places heavy constructors in their
  proper owners (ring/field/source-object owners or tensor-component interop).

- **Cross-reference to implementation surface**: card line 50-51 cites
  `category_specs/algebras/__init__.py` and specifically
  `Algebras(R).Constructors()`. **Filesystem evidence**: the `Constructors`
  class exists at `__init__.py` line 379.

No definition-grounding deficiencies. All spec references are bidirectional
(the spec rows at lines 230-240 name the same constructor targets as the
implementation at lines 458-651).

### Gate 2: Implementation Consistency — PASS

**Status: PASS**

The implementation fully matches the card's claim that no heavy constructors
(Zmod, CyclotomicField, NumberField) leak through the algebra constructor
surface.

**Evidence — Prohibited constructors absent from algebra subtree:**

```
Command: rg -n "Zmod|CyclotomicField|NumberField" /home/dzack/research/category_specs/algebras
Result: 0 matches (empty output, exit code 1)
```

The same search scoped to the full `category_specs/` tree confirms that Zmod
appears only in its proper owners:
- `category_specs/rings/__init__.py` line 736 (ring constructor)
- `category_specs/rings/subcategories/integer_mod_ring.py` line 26
- `category_specs/modules/category_obligations.sage` lines 142-209 (module tests over Zmod(6))

And CyclotomicField/NumberField appear only in:
- `category_specs/rings/subcategories/number_field.py` lines 1-71 (ring subcategory)
- `category_specs/rings/subcategories/cyclotomic_field.py` (ring subcategory, lazy-imported)
- `category_specs/rings/category_obligations.sage` line 131 (ring constructor category-obligation example)

**Evidence — Constructor surface is lightweight routing/refinement only:**
The `Constructors` class (`__init__.py` lines 379-651) exposes exactly 9 public
methods plus 4 private helpers. Every public method is a named, source-category-
selected constructor:

| Public method | Lines | What it delegates to |
|---|---|---|
| `free_algebra_from_set(generators)` | 458-478 | `FreeAlgebra(R, n, names)` (line 471), then refinement |
| `free_algebra_from_magma(magma)` | 481-494 | `source.algebra(R, category=Magmas())` (line 448), then refinement |
| `free_algebra_from_semigroup(semigroup)` | 497-512 | `source.algebra(R, category=Semigroups())` (line 448), then refinement |
| `free_algebra_from_monoid(monoid)` | 515-519 | `source.algebra(R, category=Monoids())` (line 432), then refinement |
| `free_algebra_from_group(group)` | 522-526 | `source.algebra(R, category=Groups())` (line 432), then refinement |
| `free_algebra_from_additive_semigroup(...)` | 529-544 | `source.algebra(R, category=AdditiveSemigroups())` (line 448), then refinement |
| `free_algebra_from_additive_monoid(...)` | 547-554 | `source.algebra(R, category=AdditiveMonoids())` (line 432), then refinement |
| `free_algebra_from_additive_group(...)` | 557-564 | `source.algebra(R, category=AdditiveGroups())` (line 432), then refinement |
| `from_multiplication_tensor(multiplication)` | 596-651 | `FiniteDimensionalAlgebra(R, table, category=...)` (line 633), then refinement |

No public method constructs `Zmod`, `CyclotomicField`, `NumberField`, or any
other raw Sage parent directly. No option-bag parameter (variadic `**kwargs`,
`*args`) appears in any public constructor signature. The `category=` argument
to Sage internals is used only in private methods (`_sage_algebra_from_source`
line 432, `_sage_algebra_from_source_with_target` line 448,
`from_multiplication_tensor` line 633) and is always programmatically determined
by the named constructor method, never user-exposed.

**Evidence — Category-obligation test passes:**

```
Command: sage /home/dzack/research/category_specs/algebras/category_obligations.sage
Exit code: 0
Output: (none — all assertions pass silently)
```

The category-obligation test (225 lines) contains 0 occurrences of `Zmod`, `CyclotomicField`,
or `NumberField` (`rg` returns 0 matches). It validates all 8 source-category
free algebra routes plus both `from_multiplication_tensor` routes (over QQ and
ZZ). The multiplication tensor test (lines 53-63, 216-221) confirms that the
tensor is first constructed through
`TensorAlgebraComponents(R).Constructors().from_module_element_matrix(...)` before
being passed to `Algebras(R).Constructors().from_multiplication_tensor(...)`.

### Gate 3: Constructor Route Justification — PASS

**Status: PASS**

Every public constructor method is justified against the canonical
`SPEC-MAPPING-ALGEBRAS` Free-Construction Routing table (spec lines 230-240):

| Spec source category | Spec target constructor | Implementation location | Match? |
|---|---|---|---|
| `Sets()` | `free_algebra_from_set(S)` | `__init__.py` lines 458-478 | Yes — uses Sage `FreeAlgebra`, refines to `WithBasis()` |
| `Magmas()` | `free_algebra_from_magma(S)` | `__init__.py` lines 481-494 | Yes — routes to `MagmaticAlgebras(R)` |
| `Semigroups()` | `free_algebra_from_semigroup(S)` | `__init__.py` lines 497-512 | Yes — routes to `AssociativeAlgebras(R)` |
| `Monoids()` | `free_algebra_from_monoid(S)` | `__init__.py` lines 515-519 | Yes — routes to `Algebras(R).WithBasis()` |
| `Groups()` | `free_algebra_from_group(S)` | `__init__.py` lines 522-526 | Yes — routes to `Algebras(R).WithBasis()` |
| `AdditiveSemigroups()` | `free_algebra_from_additive_semigroup(S)` | `__init__.py` lines 529-544 | Yes — routes to `AssociativeAlgebras(R)` |
| `AdditiveMonoids()` | `free_algebra_from_additive_monoid(S)` | `__init__.py` lines 547-554 | Yes — routes to `Algebras(R).WithBasis()` |
| `AdditiveGroups()` | `free_algebra_from_additive_group(S)` | `__init__.py` lines 557-564 | Yes — routes to `Algebras(R).WithBasis()` |

The multiplication-tensor constructor (`__init__.py` lines 596-651) matches
the spec at lines 275-303: validates `mu.tensor_type() == (1, 2)` (line 605),
checks the tensor base ring (line 610), reads `mu.structure_constants()` 
(line 614), converts to Sage's right-multiplication table format (lines 567-593),
and calls `FiniteDimensionalAlgebra` with programmatically determined categories.
The spec's requirement that "callers do not pass a separate basis, table, 
matrix, or right-multiplication data" is enforced: `from_multiplication_tensor`
accepts exactly one parameter, `multiplication: Tensor` (line 596).

Additionally, the spec's rejection of Sage's plain-set `S.algebra(R)` as an
algebra constructor (spec lines 263-273) is consistent with the implementation:
no public `Sets().algebra(R)` route exists in `Algebras(R).Constructors()`.

### Gate 4: Nonmathematical Rejection — PASS

**Status: PASS**

The implementation correctly excludes nonmathematical targets and raw Sage
implementation containers from the public constructor surface:

- **No `has_standard_involution()`** — the spec's Gate 4 finding (spec lines
  474-483) confirms this is quaternion-specific and correctly rejected from
  general `Algebras(R)`. The implementation has no such method.

- **No generic `category=` user-exposed API**: the docstring at `__init__.py`
  lines 382-386 explicitly states: "Sage's generic `S.algebra(R)` compatibility
  method is not the public project API." The only `category=` usages are in
  private helpers (`_sage_algebra_from_source` line 432,
  `_sage_algebra_from_source_with_target` line 448, `from_multiplication_tensor`
  line 633), all programmatically determined.

- **No option bags**: zero occurrences of `*args` or `**kwargs` in public
  constructor signatures. The `_right_multiplication_table` private method
  (lines 567-593) is properly underscore-prefixed.

- **No Sage display/runtime/private interop exposed**: `FreeAlgebra` factory
  internals (`create_key`, `_repr_`, `construction()`) are not surfaced.

- **No `AlgebraModules(A)` admitted as algebra method**: correctly routed to
  modules subtree (per spec line 123).

### Gate 5: Ambiguity Routing — PASS

**Status: PASS**

The card's Negative Finding section (lines 102-115) explicitly acknowledges
the scope boundary and routes out-of-scope concerns:

- **Card line 114**: "Other subtrees may still mention these constructors for
  their own module, ring, or field surfaces; that is outside this
  algebra-constructor card."

This is a clean, explicit routing statement. The search evidence confirms that
`Zmod` lives in `category_specs/rings/` and `category_specs/modules/`, while
`CyclotomicField`/`NumberField` live in `category_specs/rings/`. These are
their correct mathematical owners per the owner split recorded in the card's
Grounded Boundary (lines 60-62): "When they are mathematically relevant, they
belong to their own ring/field/source-object owners or to tensor-component
interop before algebra construction."

No unresolved ambiguity within the algebra-constructor scope. The card does
not need to track decisions about ring/field constructor cards — those are
separate tracked items in their respective subtrees.

### Gate 6: Obligation Preservation — PASS

**Status: PASS**

The card and implementation do not weaken or delete any algebra constructor
obligation. Every admitted route is preserved:

- **Free associative algebra on a set**: preserved as `free_algebra_from_set`
  (lines 458-478), per spec row 254-255. The generator presentation is recorded
  on the returned object (lines 472-475), and the category-obligation test explicitly validates
  this at category_obligations.sage lines 96-103.

- **Source-category-selected free algebra routes**: all 7 magma/semigroup/monoid/
  group/additive-semigroup/additive-monoid/additive-group routes preserved
  (see Gate 3 table above). Each category-obligation example-tested:
  - `free_algebra_from_magma` — category_obligations.sage lines 188-189
  - `free_algebra_from_semigroup` — lines 191-193
  - `free_algebra_from_monoid` — lines 195-197
  - `free_algebra_from_group` — lines 199-201
  - `free_algebra_from_additive_semigroup` — lines 203-205
  - `free_algebra_from_additive_monoid` — lines 207-209
  - `free_algebra_from_additive_group` — lines 211-213

- **Multiplication tensor route**: preserved as `from_multiplication_tensor`
  (lines 596-651), with tensor-component handoff before algebra construction
  validated by category_obligations.sage lines 53-63 and 215-221.

- **Refinement not weakening**: each constructor refines the result into the
  project category hierarchy (via `_refine_constructed_algebra` at line 405
  and `_refine_constructed_magmatic_algebra` at line 413). The refinement
  adds project category structure without removing Sage category information.

- **Heavy constructors not deleted, just not duplicated**: Zmod rings are still
  constructible via `Rings().Constructors().Zmod(n)` at
  `category_specs/rings/__init__.py` line 736. Cyclotomic fields are still
  constructible via their ring constructor. No algebraic capability is lost.

### Overall Verdict: ALL GATES PASS

The current algebra constructor surface satisfies every success criterion:
1. No Zmod, CyclotomicField, or NumberField leaks into `Algebras(R).Constructors()`.
2. Public constructors are lightweight source-category routing/refinement methods.
3. Sage's generic `category=` disambiguation is not exposed as public project API.
4. Finite-dimensional algebra construction routes through
   `TensorAlgebraComponents` before `from_multiplication_tensor`.
5. Category-obligation example evidence is recorded without weakening mapping decisions or obligations.

**Card status set to: complete**
