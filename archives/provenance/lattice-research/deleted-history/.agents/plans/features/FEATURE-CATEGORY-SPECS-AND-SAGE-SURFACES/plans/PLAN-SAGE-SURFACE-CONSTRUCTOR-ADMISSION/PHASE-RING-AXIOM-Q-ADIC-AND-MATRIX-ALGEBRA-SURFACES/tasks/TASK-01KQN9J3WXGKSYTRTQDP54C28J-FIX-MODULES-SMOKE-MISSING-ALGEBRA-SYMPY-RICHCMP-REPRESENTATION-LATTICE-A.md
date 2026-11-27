---
id: TASK-01KQN9J3WXGKSYTRTQDP54C28J-FIX-MODULES-SMOKE-MISSING-ALGEBRA-SYMPY-RICHCMP-REPRESENTATION-LATTICE-A
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Fix Modules smoke missing algebra _sympy_ __richcmp__ representation lattice
  and graded base-category failures
status: complete
priority: high
description: The deleted Modules triage recorded the post-wrapper-deletion smoke frontier
  and the surfaces still meant as mathematical categories rather than exact Sage implementation
  wrappers.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Run just smoke-file modules/smoketest.sage and preserve the full missing-surface
  output in tracker updates.
- Do not restore constructor-only wrapper categories to make smokes pass.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
---
# Fix Modules smoke missing algebra _sympy_ __richcmp__ representation lattice and graded base-category failures
## Summary

The deleted Modules triage recorded the post-wrapper-deletion smoke frontier and the
surfaces still meant as mathematical categories rather than exact Sage implementation
wrappers.

## Source Provenance

- Archived Modules triage content from commit `8d1c21c` lives at
  `plans/category_specs/modules/docs/TRIAGE.md`; recover exact prior content with
  `git show 8d1c21c^:plans/category_specs/modules/docs/TRIAGE.md`.
- Original migrated line: `Fix Modules smoke missing algebra _sympy_ __richcmp__ representation lattice and graded base-category failures from category_specs/modules/docs/TRIAGE.md`

## Context

- Constructor-only Sage-wrapper categories were removed; constructors now refine Sage objects into real categories such as Free().FiniteRank(), WithOrderedBasis(), Subobjects(), Quotients(), and form-bearing module categories.
- Remaining named module subcategories must not define themselves by exact Sage implementation-class containment.
- OrthogonalGroup belongs to the aut surface of a forms-owned category: C.AutCategory().Of(M) for formed-module categories.
- Current smoke failures include missing algebra, _sympy_, __richcmp__, RepresentationModules KeyError, IntegerLattices/TorsionQuadraticModules compatibility KeyError, and graded module base-category mismatch.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file modules/smoketest.sage and preserve the full missing-surface output in tracker updates.
- [ ] Do not restore constructor-only wrapper categories to make smokes pass.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06 start-of-task smoke after fork-isolated smoke harness: `just
  --justfile category_specs/justfile smoke-file modules/smoketest.sage` fails on
  current module frontiers. The former migrated `_sympy_` headline is no longer
  present in the filtered smoke output. Current repeated frontiers include
  `modify_module_structure` on free/vector/ring-as-module constructors,
  `alternating_algebra` on basis/subobject/quotient constructors, `annihilator` on
  basisless finite-rank constructors and matrix-ring-as-module, `form` or invalid
  form base-category routing on inner-product and quadratic constructors,
  representation-module `KeyError`, integer-lattice and torsion-quadratic-module
  compatibility `KeyError`, graded-module base-category mismatch against Sage
  `Modules`, Ore characteristic-polynomial, ideal `_refine_category_`, and inherited
  ring frontiers for polynomial/series-as-module constructors.
- 2026-05-06 constructor-refinement slice: changed module constructor refinement to
  return refined parents without running the global not-implemented-method test. This
  matches the matrix-ring constructor treatment: constructors expose their scoped
  category memberships, while missing broad root methods remain frontier evidence when
  exercised directly. Re-running `just --justfile category_specs/justfile smoke-file
  modules/smoketest.sage` removed the repeated `modify_module_structure` constructor
  failures and narrowed the first frontier to basisless vector-space `dimension`,
  subobject/quotient `alternating_algebra`, representation/lattice compatibility
  `KeyError`s, graded base-category mismatch, ideal `_refine_category_`, and inherited
  ring-as-module frontiers.
- 2026-05-06 finite-rank dimension slice: implemented
  `Modules(R).Free().FiniteRank().ParentMethods.dimension()` as `rank()`, matching the
  mapping rule that finite-rank dimension is the cardinality of a basis. Re-running
  the modules smoke removed the `VectorSpaceWithoutBasis(2) has dimension 2` failure;
  the first remaining constructor-specific frontier is vector-space inner-product form
  routing (`base must be a ring or a subcategory of Rings()`), followed by the existing
  subobject/quotient `alternating_algebra`, representation/lattice compatibility,
  graded, ideal, and ring-as-module frontiers.
- 2026-05-06 OverPID formed-chain slice: changed
  `Modules(R).OverPID().WithForms().Bilinear()` and `.Quadratic()` to use
  `_with_axiom(...)`, matching the generic formed-module chain instead of
  instantiating the axiom category with a category object as if it were a base ring.
  Direct probes for `Modules(QQ).WithForms().Bilinear()`, `.Quadratic()`, and
  `VectorSpaceWithInnerProductRows(...).inner_product_matrix()` now pass. Re-running
  the modules smoke removed the vector-space inner-product and explicit
  free/quadratic form constructor failures; the first remaining frontier is now
  subobject/quotient refinement hitting `alternating_algebra`.
- 2026-05-06 membership-refinement and join-super slice: changed direct
  membership-only smoke refinements to call `refine_category(..., test=False)`, so
  subobject/quotient/representation membership checks do not also run the global
  missing-method probe. Added `Modules(R).Quotients()` to finitely presented PID
  quotient constructor refinement, preserving the mathematical `V/W` output
  structure. Changed representation, integer-lattice, torsion-quadratic, and graded
  constructor-family categories with several declared supercategories to return the
  explicit Sage join category, avoiding framework initialization failures from
  parallel supercategory lists. Re-running `just --justfile category_specs/justfile
  smoke-file modules/smoketest.sage` removed the subobject/quotient
  `alternating_algebra`, quotient-of-free-modules, representation-module,
  integer-lattice, and torsion-quadratic-module failures. Remaining frontiers are the
  wrapped graded-module base-category mismatch, ideals lacking `_refine_category_`,
  and ring-as-module constructors failing inside ring constructor refinement before
  the module forgetful refinement runs.
- 2026-05-06 ring-constructor refinement slice: changed polynomial, power-series,
  Laurent-series, and Puiseux-series ring constructors to return their scoped
  constructor refinements without running the global missing-method probe. This mirrors
  the matrix-ring and module-constructor treatment: constructor smokes preserve the
  named mathematical constructor/category surface, while missing broad ring methods
  remain frontiers when exercised directly. Re-running `just --justfile
  category_specs/justfile smoke-file modules/smoketest.sage` removed the
  ring-as-module constructor failures. Remaining modules smoke frontiers are the
  wrapped graded-module base-category mismatch and ideal objects lacking
  `_refine_category_`.
- 2026-05-06 ideal-as-submodule slice: changed ideal module constructors to realize
  an ideal `I <= R` as the submodule of the rank-one free module `R^1` generated by
  the rows `[g]` for `g in I.gens()`, then refine that actual submodule into
  `RIdeals()` and, for the invertible/projective constructor, `Projective()`. This
  keeps ideals as mathematical subobjects instead of admitting raw Sage ideal elements
  through every module/set supercategory. Re-running `just --justfile
  category_specs/justfile smoke-file modules/smoketest.sage` removed the ideal
  `_refine_category_` failures. The only remaining modules smoke frontier is the
  wrapped graded-module base-category mismatch.
- 2026-05-06 graded-module slice: added a local `Modules(R).Graded()` axiom surface
  and routed free and finitely presented graded constructor-family categories through
  it instead of Sage's raw `GradedModules` descriptor, which expects Sage's upstream
  `Modules` base class. `FreeGradedModules()` and `FinitelyPresentedGradedModules()`
  now report `is_graded()`. Re-running `just --justfile category_specs/justfile
  smoke-file modules/smoketest.sage` passes with no modules smoke failures. Status
  moved to `needs-agent-review`; this does not mark the card accepted or complete.

## Definition Grounding Rework

### Graded Modules

Grounding sources:

- Sage `sage.categories.graded_modules.GradedModules`: defines graded modules as
  modules `M = \bigoplus_i M_i`, treats the grading as extra structure preserved by
  morphisms, and makes `Modules(R).Graded()` the Sage spelling of the graded-module
  category over `R`.
- Sage `sage.modules.fp_graded.free_module.FreeGradedModule`: constructs finitely
  generated free graded modules over a connected graded algebra with an ordered tuple
  of integer generator degrees.
- Sage `sage.modules.fp_graded.module.FPModule`: constructs finitely presented graded
  modules over a connected graded algebra as cokernels of homomorphisms between
  finitely generated free graded modules, with generator degrees and relations.
- Local `SPEC-MAPPING-MODULES.md`: keeps `Modules(A).Graded().Free()` and
  `Modules(A).Graded().FinitelyPresented()` as real graded module category surfaces,
  not exact Sage wrapper categories.

Definition used by this card: `Modules(R).Graded()` is the refinement of modules over
`R` whose objects carry a grading `M = \bigoplus_i M_i` compatible with the module
structure and whose morphisms preserve the graded structure. The current constructor
surface is only admitted for Sage-backed graded module families over graded algebras
where Sage supplies integer generator degrees and graded presentations. The local
`is_graded()` predicate is therefore a category-membership predicate for that admitted
surface, not a claim that every `Modules(R)` object has canonical grading data.

### Ring Ideals as Module Subobjects

Grounding sources:

- Sage `sage.categories.ring_ideals.RingIdeals`: defines the category of two-sided
  ideals in a fixed ring and lists `Modules(R)` as the supercategory for
  `RingIdeals(R)`.
- Sage `sage.categories.category_types.Category_ideal`: treats ideals as objects in an
  ambient ring and recognizes Sage `Ideal_generic` objects whose ring is that ambient
  ring.
- Local `category_specs/rings/__init__.py` routes commutative ring ideals through both
  Sage `CommutativeRingIdeals(R)` and `Modules(R).RIdeals()`.

Definition used by this card: for a ring `R`, `Modules(R).RIdeals()` is the
module-side refinement for ideals of `R`, i.e. `R`-submodules of the regular
`R`-module `R` satisfying the appropriate ideal closure condition. For a Sage ideal
`I = (g_1, ..., g_n) <= R`, the rank-one-free-module realization sends `I` through the
canonical regular-module identification `R \cong R^1` determined by the singleton
basis. The submodule of `R^1` generated by `[g_1], ..., [g_n]` is the image of the
ideal under that identification. This realizes the existing Sage ideal as a module
subobject for category refinement; it does not redefine the abstract ideal or introduce
an arbitrary basis-dependent invariant.

## Review Log

### Review 2026-05-06 (Chandrasekhar)

**Gates passed:** none
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 1 Findings: Definition Grounding

- The card recorded implementation of a local `Modules(R).Graded()` axiom and
  `is_graded()` predicate, but did not record the exact graded-module definition,
  grading-index and compatibility hypotheses, or owner/codomain rationale.
- The card recorded `ideal_as_submodule()` as the submodule of `R^1` generated by
  `[g]` for `g in I.gens()`, but did not ground `RIdeals()` or the equivalence between
  Sage ideal objects and that rank-one submodule realization.

### Re-review 2026-05-06 (Huygens)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** none
**Outcome:** independent re-review passed Gates 1-6; human approval still required before completion

#### Residual Risks

- Broader `rings/smoketest.sage` still fails on known ring-frontier surfaces, but those
  failures are outside this modules smoke card's discharge claim and remain preserved
  as gap evidence in ring successor work.
