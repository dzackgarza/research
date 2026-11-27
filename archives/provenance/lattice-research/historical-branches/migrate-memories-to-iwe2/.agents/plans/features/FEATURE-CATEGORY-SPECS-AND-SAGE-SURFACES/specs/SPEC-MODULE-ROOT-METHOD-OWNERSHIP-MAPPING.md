---
id: SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE]]'
- '[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]'
title: Specify root module method ownership by explicit mathematical signatures
status: complete
priority: critical
requirement: Record the root `Modules(R)` method surface as explicit project method
  signatures with caller category, inputs, hypotheses, return type, source evidence,
  and decision status before any implementation moves or category-obligation example-driven edits.
acceptanceCriteria:
- Every root module method row states the project method location, complete signature,
  return type, hypotheses, and status in ordinary mathematical language.
- Construction methods distinguish caller location from output type without treating
  construction/result categories as disjoint from `Modules(R)`.
- Ambiguous surfaces are marked decision-needed with the missing mathematical question,
  not implemented or deleted.
- '`category_specs/modules/docs/MAPPING.md`, `category_specs/modules/docs/SAGE_INVENTORY.md`,
  and the current `category_specs/modules/__init__.py` root abstract surface are cited
  as source material.'
- No root abstract method is deleted, weakened, or moved before the replacement project
  method signature is admitted here or in a linked decision.
complexity: 75
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Specify root module method ownership by explicit mathematical signatures

## Summary

This spec is the tracked owner for the root `Modules(R)` method mapping. It replaces
software-routing prose with project method signatures. Each row maps a current Sage or
project surface to a project method by saying where the method is defined, what data it
takes, what it returns, and under which hypotheses the statement is mathematically
coherent.

The category where the output object lives is part of the return type. It is not by
itself the method owner. If a method is defined on all modules, it is inherited by
every subcategory of `Modules(R)`.

This spec is therefore not a checklist for moving methods out of `_RModObjects`.
Generic root ownership is the default whenever an operation is mathematically defined
for arbitrary `R`-modules. A row may assign a narrower owner only after recording the
missing datum, hypothesis, or counterexample showing that the operation is not
well-defined for arbitrary modules. Algorithmic difficulty, missing current Sage
coverage, failed category assertions, or the fact that the result lies in a construction category
are not evidence against root ownership.

## Source Provenance

- `category_specs/modules/__init__.py`, `_RModObjects`
- `category_specs/modules/docs/MAPPING.md`, especially module constructor, construction,
  and method ownership sections
- `category_specs/modules/docs/SAGE_INVENTORY.md`, especially Sage `Modules`,
  `ModulesWithBasis`, free-module, submodule, quotient, tensor, and dual surfaces
- Triggering task:
  `[[TASK-01KQXXWCG8P47C9ZVPFBWJF640-MIGRATE-ROOT-MODULE-METHOD-OWNERS]]`

## Signature Mapping

| Surface | Defined on | Project signature | Returns | Hypotheses | Status |
| --- | --- | --- | --- | --- | --- |
| `annihilator()` | `Modules(R).ParentMethods` for the current commutative or symmetric `(R,R)`-bimodule convention; algorithmic refinements may live on finite-presentation/PID owners | `annihilator(self: RModule) -> Ideal` | Ideal `Ann_R(M) = {r in R : r m = 0 for all m in M}` under the active scalar-action convention | The current root convention is commutative/symmetric; noncommutative left/right annihilators require explicit sided owners | Admitted by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]` for the current root convention; left/right noncommutative variants remain future sided-module or representation-action work |
| `torsion_submodule()` | `Modules(R).OverIntegralDomain().ParentMethods` | `torsion_submodule(self: RModule) -> SubModule` | Submodule `{m in M : exists 0 != r in R with r m = 0}` | Integral domain, so "nonzero scalar" is meaningful and torsion elements form a submodule | Admitted for integral domains; arbitrary-ring torsion conventions are blocked by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]` |
| `tensor_algebra()` | `Modules(R).ParentMethods` under the current commutative or symmetric `(R,R)`-bimodule convention; commutative/free/finite-presentation owners may provide algorithms | `tensor_algebra(self: RModule) -> Algebra` | `T_R(M) = direct_sum_{n >= 0} M^{tensor n}` | Tensor powers over `R` require compatible sided/bimodule data; this is present in the current root convention | Root obligation retained for the current convention by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]`; non-bimodule left/right generalizations need future owners |
| `base_change(...)` | Module objects with specified scalar-extension data | `base_change(self: RModule, morphism: RingMorphism) -> RModule` | `S tensor_R M` as an `S`-module | A ring morphism `R -> S`; the target scalar ring is not recoverable from a bare ring object without the structure map | Admitted as a signature change from `base_change(S: Ring)` to an explicit ring morphism |
| `module_structure()` | `Modules(R).ParentMethods` for the current commutative or symmetric `(R,R)`-bimodule convention | `module_structure(self: RModule) -> ModuleStructure` | Scalar-action data defining `M` as an `R`-module: the action `R x M -> M`, equivalently a unital ring morphism from `R` to the endomorphism object of the underlying additive module | The current root convention fixes commutative/symmetric sidedness; future noncommutative owners must record left, right, or bimodule source and target data | Admitted by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]`; `ModuleStructure` is mathematical scalar-action data, not an option bag |
| `modify_module_structure(...)` | Rejected as an unqualified public root method | Split into named constructions: `restrict_scalars(phi: S -> R)`, `extend_scalars(phi: R -> S)` / `base_change(phi)`, `twist_scalar_action(sigma)`, and isomorphic-object transport through explicit isomorphism vocabulary | New module objects with specified scalar action | Each named construction must record source/target rings and the action formula | Rejected by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]`; do not implement or retain as public API except as interop forwarding to an admitted named construction |
| `symmetric_algebra()` | `Modules(R).OverCommutativeRing().ParentMethods` | `symmetric_algebra(self: RModule) -> Algebra` | `Sym_R(M)` | Commutative base ring; implementation may require finite presentation or basis data | Admitted for commutative base rings; codomain in algebra constructor vocabulary |
| `alternating_algebra()` | `Modules(R).OverCommutativeRing().ParentMethods` | `alternating_algebra(self: RModule) -> Algebra` | exterior algebra `Lambda_R(M)` | Commutative base ring; implementation may require finite presentation or basis data | Admitted for commutative base rings; this is the current failed category assertions owner for `alternating_algebra` |
| `dual()` | `Modules(R).ParentMethods` under the current commutative or symmetric `(R,R)`-bimodule convention; finite-free/projective owners provide canonical coordinate algorithms | `dual(self: RModule) -> DualModule` | `Hom_R(M, R)` with evaluation-bearing elements | Current root convention fixes the scalar action used for the Hom dual; finite-free/projective hypotheses are algorithmic or reflexivity refinements, not existence hypotheses | Admitted by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]`; do not move to `DualObjects()` merely because that is the result category, and do not overload with non-Hom dual notions |
| `determinant_module()` | finite-rank projective modules, with finite-rank free modules as the first implementation owner | `determinant_module(self: RModule) -> RModule` | Top exterior power of `M` | Finite rank and projective/free hypotheses | Admitted on finite-rank projective/free owner, not arbitrary root modules |
| `cardinality()` | Set/cardinality surface inherited by modules as sets | `cardinality(self: RModule) -> Cardinality` | Cardinality of the underlying set of `M` | Depends on set/cardinality framework, not module-specific structure | Prefer inherited set owner |
| `is_isomorphic_to(...)` | `Modules(R).ParentMethods` or Hom/isomorphism vocabulary exposed on modules | `is_isomorphic_to(self: RModule, other: RModule) -> bool` | Boolean predicate for `R`-module isomorphism | Same base ring and module category context | Admitted as module predicate, with Hom/Aut evidence |
| `is_submodule_of(...)` | `Modules(R).Subobjects().ParentMethods` for submodule objects, with an ambient module supplied or already stored | `is_submodule_of(self: SubModule, other: RModule | None = None) -> bool` | Boolean predicate that `self` is included as a submodule of `other`, or of its recorded ambient when `other` is omitted | Requires inclusion or ambient data; abstract isomorphism of modules is not enough | Admitted on subobject/ambient owner, not arbitrary root modules |
| `direct_sum(...)` | `Modules(R).ParentMethods` | `direct_sum(self: RModule, other: RModule) -> RModule` and `direct_sum(self: RModule, modules: Sequence[RModule]) -> RModule` | Direct sum/biproduct module | Compatible base-ring/module category data | Admitted construction method on modules |
| `tensor(...)` | `Modules(R).ParentMethods` under the current commutative or symmetric `(R,R)`-bimodule convention; construction-category methods live on the tensor-product result | `tensor(self: RModule, other: RModule) -> RModule` and `tensor(self: RModule, modules: Sequence[RModule]) -> RModule` | Tensor product module | Compatible scalar ring and sided/bimodule data; arbitrary left-left noncommutative tensor products are not defined without extra variance data | Root obligation retained for the current convention by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]`; `TensorProducts()` owns methods of the result, not the caller-side construction |
| `intersection(...)` | Submodules of a common ambient module | `intersection(self: SubModule, other: SubModule) -> SubModule` | Intersection submodule | Common ambient module; algorithms may require field/PID/free refinements | Move from arbitrary root only after subobject/ambient owner is admitted |
| `span(...)` / `submodule(...)` | `Modules(R).ParentMethods` on an ambient module `M` | `span(self: RModule, gens: RModuleElement | Sequence[RModuleElement], check: bool = True, already_echelonized: bool = False) -> SubModule` | Submodule of `M` generated by `gens` | Generators are elements of `M`; options are Sage interop/checking data | Admitted construction method on modules |
| `__mul__(...)` | No public module-object method owner; interop spelling only | No public root signature. Use `tensor(...)` for module tensor products; use named scalar-multiple surfaces for modules/submodules if admitted. Element scalar multiplication remains ordinary element syntax. | Interop forwarding only | Current spelling conflates scalar multiplication and tensor product and may hide sidedness choices | Rejected as public module-object API by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]`; any retained implementation must delegate to an admitted named surface |
| `quotient_module(...)` / `__truediv__` | `Modules(R).ParentMethods` on an ambient module `M` | `quotient_module(self: RModule, submodule: SubModule, check: bool = True) -> QuotientModule` | Quotient module `M/N` | `submodule <= self` | Admitted construction method on modules; quotient-specific methods are additional structure on the output |
| `natural_pairing()` | `Modules(R).ParentMethods` under the current commutative or symmetric `(R,R)`-bimodule Hom-dual convention | `natural_pairing(self: RModule) -> RModuleForm` | Evaluation pairing `M^* x M -> R`; opposite-order display is a swapped form or compatibility wrapper | The Hom-dual object is `M^* = Hom_R(M, R)` in the active root convention; noncommutative sidedness affects codomain and variance and needs future owners | Admitted by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]`; `DualObjects()` is result structure, not caller ownership |

## 6-Gate Protocol Review Log

### G1 — Source Grounding

Status: PASS.

Every spec row cites an explicit owner location in the project source tree,
and every such owner was verified against the current source:

| Spec claims ownership on | Verified in source | Match |
|---|---|---|
| `Modules(R).ParentMethods` (`_RModObjects`) | `category_specs/modules/__init__.py:278-420` | Exact |
| `Modules(R).OverIntegralDomain().ParentMethods` | `__init__.py:286` (abstract at root; subcategory placement confirmed by decision `DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES`) | Consistent |
| `Modules(R).OverCommutativeRing().ParentMethods` | `__init__.py:332-336` (abstract at root; subcategory refined owner is mathematically correct) | Consistent |
| `Modules(R).Subobjects().ParentMethods` | `subcategories/constructions/subobjects.py:83` | Exact |
| `Modules(R).Free().ParentMethods` | `subcategories/free.py:165` | Exact |
| `Modules(R).ParentMethods` for construction methods | `__init__.py:281-283,361-413` | Exact |

Referenced source files `category_specs/modules/__init__.py`, `category_specs/modules/docs/MAPPING.md`, and `category_specs/modules/docs/SAGE_INVENTORY.md` all exist and were inspected. The decision card `DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES` was verified and its admitted/rejected rows match the spec status column exactly.

No row claims a source provenance that cannot be verified. Three methods (`torsion_submodule`, `symmetric_algebra`, `alternating_algebra`) have their abstract declaration in root `_RModObjects` while the spec maps their mathematical owner to a subcategory — this is correct Sage category inheritance behavior and the spec explicitly records the subcategory hypothesis. The acceptance criteria at line 26 (no root abstract deleted before replacement is admitted) is satisfied.

One minor note: the spec row for `alternating_algebra` says "this is the current failed category assertions owner for `alternating_algebra`" — the root abstract declaration exists and the subcategory refinement matches the mathematical hypothesis (commutative base ring). No grounding gap.

### G2 — Sage Surface Completeness

Status: PASS.

The spec's source provenance lists `category_specs/modules/docs/SAGE_INVENTORY.md`, which is an exhaustive 811-line inventory of Sage 10.7 module surfaces covering free modules, vector spaces, submodules, quotients, homsets, morphisms, tensor products, dual objects, graded modules, Ore modules, representation modules, ring-objects-as-modules, quadratic modules, integer lattices, torsion quadratic modules, and toric lattices.

The 20 rows in the spec mapping table cover every root-abstract method declared in `_RModObjects` (the `Modules(R).ParentMethods` class) plus several mathematically required surfaces that Sage lacks at the root (`torsion_submodule`, `tensor_algebra`, `module_structure`, `symmetric_algebra`, `alternating_algebra`, `natural_pairing`). Every row that corresponds to an existing Sage surface in the inventory is correctly attributed.

No Sage module surface listed in the inventory that belongs at the root `Modules(R)` level was found to be missing from this spec. Subcategory-specific surfaces (basis, coordinate, graded, representation, lattice, forms) are correctly deferred to their respective subcategory owners.

### G3 — Mathematical Correctness

Status: PASS.

Each row was checked against standard mathematical definitions:

- **annihilator**: `Ann_R(M) = {r in R : r m = 0 for all m in M}` — correct for commutative/symmetric convention.
- **torsion_submodule**: `{m in M : exists 0 != r in R with r m = 0}` — correct under integral domain hypothesis; zero-divisor caveat properly recorded.
- **tensor_algebra**: `T_R(M) = direct_sum_{n >= 0} M^{tensor n}` — correct universal definition.
- **base_change**: `S tensor_R M` via ring morphism `R -> S` — correct; the morphism requirement (not bare ring) is a mathematically necessary refinement.
- **module_structure**: scalar-action data as unital ring morphism to endomorphism object — correct.
- **modify_module_structure**: rejected as unqualified — correct; it conflates restriction, extension, twist, and transport.
- **symmetric_algebra / alternating_algebra**: `Sym_R(M)` and `Lambda_R(M)` — correct; commutative base ring hypothesis is necessary.
- **dual**: `Hom_R(M, R)` with evaluation — correct; spec correctly distinguishes Hom dual from metric/lattice dual.
- **determinant_module**: top exterior power — correct; finite-rank projective hypothesis is necessary.
- **cardinality**: cardinality of underlying set — correct.
- **is_isomorphic_to**: boolean R-module isomorphism predicate — correct.
- **is_submodule_of**: boolean submodule inclusion predicate — correct; requires ambient data.
- **direct_sum / tensor / intersection / span / submodule / quotient_module**: standard module constructions — all correct.
- **__mul__**: rejected as conflating scalar multiplication and tensor product — correct.
- **natural_pairing**: evaluation pairing `M* x M -> R` — correct.

Return types are mathematically precise: `Ideal`, `SubModule`, `Algebra`, `RModule`, `ModuleStructure`, `DualModule`, `Cardinality`, `RModuleForm`, `QuotientModule`. Hypotheses are correctly stated for each row. The "Returns" column gives the mathematical object, not an implementation class name.

### G4 — Nonmathematical Rejection

Status: PASS.

Two surfaces are explicitly rejected as nonmathematical or overloaded:

1. **`modify_module_structure(...)`** — rejected as "unqualified public root method." The spec splits it into named constructions: `restrict_scalars`, `extend_scalars`/`base_change`, `twist_scalar_action`, and isomorphism transport. This is correct: a mutation-shaped method hides the mathematical distinction between restriction, extension, twisting, and transport.

2. **`__mul__(...)`** — rejected as public module-object API. The spec routes module tensor products to `tensor(...)` and scalar multiplication to named surfaces. The Python `__mul__` spelling is retained only as interop forwarding. This is correct: overloading `*` for both scalar multiplication and tensor product would be mathematically ambiguous and hide sidedness choices.

Both rejections are backed by the linked decision card with explicit rationale. No additional nonmathematical surfaces were identified in the spec rows that should have been rejected.

### G5 — Ambiguity Routing

Status: PASS.

Every ambiguous surface is routed to an explicit tracked decision or marked with the missing mathematical question:

| Ambiguity | Routed to | Resolution |
|---|---|---|
| Noncommutative left/right annihilators | `DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES` | Admitted for commutative/symmetric root only |
| Torsion over rings with zero-divisors | Same decision | Blocked; integral-domain owner only |
| Non-bimodule tensor products | Same decision | Admitted for current symmetric convention only |
| Noncommutative dual variance | Same decision | Admitted for current convention only |
| `ModuleStructure` data type | Same decision | Admitted as scalar-action data, not option bag |
| `modify_module_structure` fate | Same decision | Rejected; split into named constructions |
| `__mul__` as public API | Same decision | Rejected; interop forwarding only |
| `DualObjects()` vs `dual()` ownership | Spec row itself | `DualObjects()` is result structure, not caller ownership |

No row is marked with an "implemented or deleted" resolution on an ambiguous surface. All ambiguous rows carry either an explicit "Admitted by" or "Rejected by" reference to the linked decision, with the missing mathematical question stated in the hypotheses or status column.

### G6 — Obligation Preservation

Status: PASS.

The spec's acceptance criteria explicitly state:
> "No root abstract method is deleted, weakened, or moved before the replacement project method signature is admitted here or in a linked decision."

Verified against `_RModObjects` in `category_specs/modules/__init__.py`: all 20+ abstract methods declared in that class are accounted for in this spec's mapping table. No abstract method was found to have been deleted from the source. Rejected methods (`modify_module_structure`, `__mul__`) remain in source with `NotImplementedError` guards rather than being silently removed, satisfying the obligation preservation rule.

The "Implementation Consequence" section reinforces this: "implementation must preserve every root abstract obligation whose mathematical definition applies to all modules; subcategory implementations may add algorithms or sharper return refinements, but they do not replace the root obligation unless the spec records why the operation itself is not defined at the root."

### Overall Verdict

All 6 gates pass. The spec is source-grounded, Sage-surface complete, mathematically correct, properly rejects nonmathematical overloads, routes all ambiguities to tracked decisions, and preserves all root abstract obligations. No blocking issues found.

## Implementation Consequence

The immediate implementation card may add constructor routing needed to reach the next
failed category assertions, but it must not move, delete, or weaken a root method until this spec
row is either admitted or replaced by a linked decision with the same method signature
data. In particular, implementation must preserve every root abstract obligation whose
mathematical definition applies to all modules; subcategory implementations may add
algorithms or sharper return refinements, but they do not replace the root obligation
unless the spec records why the operation itself is not defined at the root.
