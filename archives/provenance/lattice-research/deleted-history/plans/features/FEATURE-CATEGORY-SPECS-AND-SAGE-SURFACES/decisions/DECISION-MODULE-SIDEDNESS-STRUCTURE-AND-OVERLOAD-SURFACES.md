---
id: DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]'
title: Decide module sidedness structure transport and overload surfaces
status: decided
chosen: Commutative/symmetric-bimodule root surface; reject ambiguous overloads as public API
options:
- name: Commutative-first root module surface
  pros:
  - Matches the current category-spec smoke frontier and most Sage module wrapper evidence.
  - Lets tensor, dual, symmetric, exterior, annihilator, and natural-pairing surfaces
    advance with standard commutative-ring signatures.
  - Keeps noncommutative module sidedness out of the root API until left, right, and
    bimodule owners are explicitly named.
  cons:
  - Requires follow-up decisions before admitting noncommutative tensor products,
    duals, annihilators, and transported module structures.
- name: Add left right and bimodule owners now
  pros:
  - Gives noncommutative tensor, dual, annihilator, and natural-pairing surfaces a
    mathematically precise home.
  - Avoids later migration if Ore and representation-module work needs sided module
    vocabulary soon.
  cons:
  - Broadens the current spec phase and may require restructuring existing module,
    algebra, and Ore mapping cards before implementation can continue.
- name: Reject ambiguous overloads from public module API
  pros:
  - Keeps `__mul__` and unqualified `modify_module_structure` from hiding unrelated
    constructions under Python or mutation-shaped names.
  - Forces named methods such as scalar multiplication, tensor product, restriction
    of scalars, extension of scalars, and twist-by-automorphism.
  cons:
  - Requires explicit migration notes for Sage/Python compatibility spellings.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide module sidedness structure transport and overload surfaces

## Summary

The root module ownership spec admits the standard commutative-ring and
integral-domain module surfaces, but several remaining rows depend on conventions that
must not be guessed during implementation:

- noncommutative left/right/bimodule sidedness for tensor products, duals,
  annihilators, and natural pairings;
- torsion conventions over rings with zero-divisors, where "killed by a nonzero
  scalar" need not define the intended torsion submodule without additional
  hypotheses;
- the public type for scalar-action data returned by `module_structure()`;
- whether `modify_module_structure(...)` is a transport, restriction, extension, or
  twisting construction;
- whether overloaded `__mul__` survives as public API or is only Sage/Python interop.

## Source Provenance

- `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-MODULES.md`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/modules/docs/SAGE_INVENTORY.md`
- `category_specs/modules/__init__.py`
- Sage 10.7 installed source
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/modules.py`
- Sage 10.7 installed source
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/modules/free_module.py`
- Sage 10.7 installed source
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/modules/with_basis/representation.py`

## Decision

Use the current root `Modules(R)` surface only for the commutative or symmetric
`(R,R)`-bimodule convention that Sage already assumes for ordinary module code. This
keeps the current phase executable without pretending that left modules, right modules,
and noncommutative bimodules have already been designed.

Do not add root public methods whose correctness depends on unresolved
noncommutative sidedness. Future noncommutative work must introduce explicit owners
such as left `R`-modules, right `R`-modules, `(R,S)`-bimodules, or a representation
module with action side before tensor, dual, annihilator, natural-pairing, and
structure-transport methods are generalized beyond the current symmetric convention.

The following root surfaces are admitted under the current commutative or symmetric
`(R,R)`-bimodule convention:

- `annihilator()` returns the two-sided ideal `Ann_R(M)` in the commutative/symmetric
  convention. Noncommutative left/right annihilators are not silently identified.
- `tensor(...)` and `tensor_algebra()` use the compatible tensor product supplied by
  the current symmetric/bimodule convention. Arbitrary left-left tensor products over a
  noncommutative ring are not admitted.
- `dual()` returns the Hom-dual object `Hom_R(M, R)` in the active module convention.
  Noncommutative variance and right/left scalar action are future sidedness work.
- `natural_pairing()` is the evaluation pairing `M^* x M -> R` for that Hom-dual
  convention. Any opposite-order spelling is a separate compatibility wrapper or
  swapped form, not a new root convention.

Torsion beyond integral domains is not admitted in this decision. The current admitted
surface remains `Modules(R).OverIntegralDomain().torsion_submodule()`, with
`{m in M : exists 0 != r in R with r m = 0}`. Over rings with zero-divisors, future
work must choose and source a condition such as regular elements, non-zero-divisors,
localization support, or another named torsion theory before adding a public root
method.

`ModuleStructure` is admitted only as scalar-action data, not as an opaque helper type:
it records the unital scalar action defining the module object. In the current
commutative/symmetric convention it may be described as an action map
`R x M -> M` or equivalently as the unital ring morphism from `R` to the endomorphism
object of the underlying additive module. Any implementation type must preserve that
mathematical meaning and must not become a software-shaped option bag.

Reject unqualified `modify_module_structure(...)` as public API. Split it into named
construction surfaces when those surfaces are needed:

- `restrict_scalars(phi)` for a ring morphism `phi: S -> R`, viewing an `R`-module as
  an `S`-module;
- `extend_scalars(phi)` or the existing explicit `base_change(phi: R -> S)` for
  `S tensor_R M`;
- `twist_scalar_action(sigma)` for twisting by a specified ring endomorphism or
  automorphism where the source, target, and action formula are recorded;
- transport along an explicit module isomorphism belongs to the isomorphic-object or
  Hom/isomorphism vocabulary, not to a mutation-shaped root method.

Reject overloaded `__mul__` as public module-object API. Scalar multiplication of
module elements may keep ordinary mathematical operator syntax. Module-object tensor
products use `tensor(...)`; scalar multiples of submodules or modules, if admitted,
need a named method with scalar input and owner. Existing Sage/Python `__mul__`
spellings are interop only and must delegate to an admitted named surface rather than
define a separate method contract.

## Source Findings

Sage `Modules(R)` defines an `R`-module as a left and right module over a commutative
ring and returns `Bimodules(R, R)` as its supercategory. The same source warns that
outside symmetric modules over a commutative ring the category is fuzzy, non-symmetric
module support is not guaranteed, and noncommutative-ring support is not fully
advertised. This is implementation evidence for a commutative/symmetric first pass,
not a source for pretending the noncommutative surface is already settled.

Sage `Modules(R).DualObjects()` states that `dual` means the space of linear
functionals and warns that subcategories with a different notion of dual must use a
different name. That supports the project distinction between Hom duals and metric
dual lattices, and it blocks non-Hom dual overloads from being silently folded into
`dual()`.

Sage `FreeModuleFactory` warns when constructing over a noncommutative ring that Sage
does not have a concept of left, right, and both-sided modules and does not guarantee
the multiplication side. This is explicit source evidence that noncommutative module
sidedness cannot be inferred from current Sage free-module behavior.

Sage representation modules separately record `side` as `left`, `right`, or
`twosided`. This is positive evidence that noncommutative action side is real public
data when the mathematics requires it, but it belongs to a representation/action owner
or future sided-module owner rather than the current root `Modules(R)` pass.

## Acceptance Criteria

- Decide whether the root module spec is commutative-first or whether left, right, and
  bimodule category owners must be added before implementation.
- Decide whether torsion beyond integral domains is admitted, and if so whether it
  uses regular elements, non-zero-divisors, localization support, or another named
  scalar condition.
- Define the public `ModuleStructure` data type or split it into named scalar-action
  constructions.
- Decide whether `modify_module_structure(...)` is rejected, renamed, or split into
  restriction, extension, transport, and twist constructors.
- Decide whether `__mul__` is public module API or only interop spelling for named
  scalar-multiple and tensor-product surfaces.
- Update `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]` before moving or deleting any
  root module abstract method affected by this decision.

All criteria are satisfied by this decision plus the linked spec update. No root
abstract method is deleted here; ambiguous rows are resolved into admitted
commutative/symmetric root surfaces, explicit narrower torsion ownership, or rejected
interop-only overloads.

## Dependencies And Boundaries

This decision blocks only module rows whose meaning depends on sidedness, scalar-action
transport, or overloaded Python spelling. It does not block the admitted commutative
base-ring owners for tensor, symmetric, exterior, dual, annihilator, torsion over
integral domains, quotient construction, span, direct sum, or subobject intersection.
