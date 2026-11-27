---
id: TASK-INTEGRATE-SCHEMES-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn: []
title: Research category integration for schemes
status: complete
priority: high
description: Research and prepare the category-spec integration path for schemes.
successCriteria:
- Identify the mathematical definition and the intended project vocabulary for this
  category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors,
  Hom/End/Aut surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation
  cards needed to proceed.
complexity: 65
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-GEOMETRIC-SOURCE-ADMISSION
- PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH
---
# Research category integration for schemes

## Summary

Research and prepare the category-spec integration path for schemes.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating schemes.

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Acceptance Criteria

- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Research Result

Status: needs review. The scheme category is source-grounded enough to proceed to downstream vocabulary/spec work, but this card itself does not authorize geometry implementation.

## Mathematical Definition

Source evidence:

- Stacks Project, Schemes, Definition 26.9.1, https://stacks.math.columbia.edu/tag/01II: a scheme is a locally ringed space locally modeled by affine schemes; morphisms are morphisms of locally ringed spaces; the category is denoted Sch.
- Stacks Project, Fibre products of schemes, https://stacks.math.columbia.edu/tag/01JO: fiber products are scheme-level constructions defined by their universal property; affine fiber products are computed by tensor products of coordinate rings.
- Stacks Project, Proj of a graded ring, https://stacks.math.columbia.edu/tag/01M3: Proj of a graded ring is constructed as a locally ringed space and is a scheme with standard affine opens.
- Stacks Project, Blowing up, Definition 31.32.1, https://stacks.math.columbia.edu/tag/01OF:
  for a scheme `X` and quasi-coherent ideal sheaf `I <= O_X` with corresponding closed
  subscheme `Z`, the blowup of `X` along `Z` is the morphism
  `Proj_X(⊕_{n >= 0} I^n) -> X`; `Z` is the center and the exceptional divisor is the
  inverse image of `Z`.
- Stacks Project, Blowing up, Lemma 31.32.2, https://stacks.math.columbia.edu/tag/0804:
  on an affine open `U = Spec(A)` with ideal `I <= A`, the blowup restricts to
  `Proj(⊕_{d >= 0} I^d)` and is covered by affine blowup algebras `A[I/a]`.

Project vocabulary:

- `Schemes()` should be the generic category for locally ringed spaces locally affine, with morphisms of locally ringed spaces as the Hom surface.
- `Schemes().Over(S)` or equivalent base-scheme refinement should carry objects equipped with a structure morphism to a base scheme `S`.
- `AffineSchemes()` should own `Spec(R)` for commutative rings and affine-only surfaces such as `coordinate_ring()` as a global object invariant.
- `ProjectiveSchemes()` should own `Proj(S)` for graded commutative rings and projective-specific homogeneous-coordinate surfaces.
- `AlgebraicSchemes()` or a more precise embedded/presented refinement should cover Sage-style polynomial-equation subschemes of affine, projective, product-projective, or toric ambient spaces.
- `NoetherianSchemes()`, `FiniteTypeSchemes()`, `SeparatedSchemes()`, and related refinements should be added only when a source-backed method or invariant needs those hypotheses.

Boundary decisions:

- A scheme is not a raw zero locus, a raw ideal, or a raw coordinate ring. Those are presentations or constructors for particular subcategories.
- A globally defined `coordinate_ring()` is not a method on all schemes; it belongs first on affine schemes and then on explicitly presented algebraic subscheme surfaces where the returned ring is the presentation coordinate ring.
- `fiber_product()` and `base_change()` are scheme-level constructions. Backend support may start with affine or presented cases, but the method owner is `Schemes()` or `Schemes().Over(S)` because the construction is mathematically defined there.
- `blowup(center)` should not be forced down to varieties merely because current
  backend rows mention varieties. The mathematical owner is a scheme-level construction
  with center data given by a closed subscheme `Z -> X` or corresponding quasi-coherent
  ideal sheaf `I <= O_X`; the return data is a morphism `Bl_Z(X) -> X` in `Schemes()/X`
  constructed as relative Proj of the Rees algebra. Practical implementation may
  require noetherian, finite-type, or presented-scheme refinements and may route to
  Macaulay2/Singular/Oscar in those finitely presented cases.
- `rational_points(K)` is better understood as an `S`-valued point/Hom surface `Hom(Spec(K), X)`; enumeration is a computational refinement, not the definition.

## Sage Surface Survey

Source evidence:

- Sage generic schemes documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/scheme.html, has `Scheme` as the base class, `AffineScheme`, base schemes/rings, structure morphisms, Hom construction, points, zeta surfaces, and category examples such as projective space living in schemes over a base.
- Sage Spec documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/spec.html, exposes `Spec(R)` for commutative rings and ring homomorphisms, returning an `AffineScheme`.
- Sage gluing documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/glue.html, exposes `GluedScheme(f, g)` from open immersions and records that open-immersion checking is not implemented.
- Sage algebraic schemes documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/algebraic_scheme.html, distinguishes `AlgebraicScheme_subscheme` as explicit polynomial-equation closed subschemes and notes that general schemes need not be given by equations.
- Sage scheme overview, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/overview.html, explicitly separates generic `Scheme`, polynomial-equation `AlgebraicScheme`, ambient spaces, and affine/projective subscheme presentations.
- Sage scheme morphism documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/morphism.html, says scheme morphisms are created through `hom()` and `Hom()` and points are morphisms from `Spec(K)`.

Inference:

Sage already has enough generic scheme machinery to witness feasibility for `Schemes()`, `AffineSchemes()`, `Schemes().Over(S)`, Hom surfaces, points-as-morphisms, `Spec`, and gluing. Sage's `AlgebraicScheme` surface is narrower than the mathematical category of schemes and must not become the ceiling for the project spec.

## Backend Survey

Source evidence:

- OSCAR General schemes documentation, https://docs.oscar-system.org/stable/AlgebraicGeometry/Schemes/GeneralSchemes/, defines an abstract `Scheme` type over a commutative base ring, `SchemeMor`, irreducible components with reduced structure, and `base_change` returning the changed scheme plus canonical morphism.
- Macaulay2 Varieties overview, https://www.macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_varieties.html, presents `Spec` for affine schemes/varieties, products, `Proj` for projective schemes/varieties, and sheaf motivation.
- Macaulay2 Spec documentation, https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/___Spec.html, exposes `Spec(Ring)` returning the affine variety or scheme formed from a ring.
- Macaulay2 Proj documentation, https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/___Proj.html, exposes `Proj(Ring)` returning the projective variety or scheme formed from a graded ring.

Inference:

OSCAR and Macaulay2 support backend routes for finitely presented affine/projective scheme computations. Singular is still best treated as a lower-level commutative-algebra engine for ideals, Groebner bases, singularities, and elimination; it should not be presented as a complete scheme category unless a later backend card sources that layer.

## Local Category-Spec Dependencies

Source evidence:

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` delegates geometry candidate rows to this geometry source-admission subtree.
- Existing geometry sibling cards cover varieties, complex varieties, algebraic curves, algebraic surfaces, families of varieties, manifolds, polytopes, and toric varieties.
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-TOPOLOGICAL-SPACES.md` records that manifolds, schemes, varieties, polyhedra, and related objects carry extra structure beyond bare topology and should map to their own mathematical subtrees.

Inference:

The scheme card should be the upstream vocabulary source for geometric categories that are algebraic-geometric refinements. It does not replace the variety, surface, curve, family, or toric cards; those cards should state their extra hypotheses over the scheme substrate.

## Method Ownership Guidance

Admit these as scheme-level or scheme-refinement surfaces when downstream specs are written:

- `Hom(X, Y)`, `identity_morphism()`, and morphism composition: owned by `Schemes()`.
- `base_scheme()` and `structure_morphism()`: owned by `Schemes().Over(S)` or the repo's chosen over-category surface.
- `fiber_product(X, Y, over=S)` and `base_change(T -> S)`: owned by `Schemes().Over(S)`; affine formulas are backend specializations.
- `Spec(R)`: constructor for `AffineSchemes()` from commutative rings.
- `Proj(S)`: constructor for projective schemes from suitable graded commutative rings.
- `coordinate_ring()`: first owned by `AffineSchemes()`; presented algebraic subschemes may expose a presentation ring separately.
- `defining_ideal()`, `defining_polynomials()`, `Jacobian()`, and Jacobian-matrix surfaces: owned by embedded/presented algebraic subschemes or smoothness/singularity refinements, not all schemes.
- `point_homset(S)` and `rational_points(K)`: mathematically Hom surfaces from affine test schemes; computational enumeration belongs to finite/presented refinements.
- `glue_along_domains()` or `GluedScheme`: scheme construction from open-immersion data; current Sage checking gaps are implementation limitations.
- `blowup(center)` / `blow_up(center)`: owned first by `Schemes()` or the chosen
  over-category surface when `center` is a closed subscheme or quasi-coherent ideal
  sheaf datum on the source; the codomain is a scheme `Bl_Z(X)` equipped with its
  structural morphism to `X`. Affine Rees-algebra charts and finite-presentation
  backends are implementation refinements, not the mathematical owner.

## Downstream Work Unblocked Or Routed

This card gives source-grounded input to these sibling cards and downstream specs:

- `TASK-INTEGRATE-VARIETIES-CATEGORY`: define project variety conventions as scheme refinements, including reduced/separated/finite-type/integral hypotheses as needed.
- `TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY`: add complex/base-field hypotheses over the scheme/variety substrate.
- `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-CURVES-CATEGORY` and `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY`: place curve/surface invariants only after their scheme/variety hypotheses are explicit.
- `TASK-INTEGRATE-FAMILIES-OF-VARIETIES-CATEGORY`: use `Schemes().Over(S)` and fiber/base-change vocabulary rather than raw parameter lists.
- `TASK-INTEGRATE-TORIC-VARIETIES-WITH-LATTICE-CATEGORY`: connect toric varieties as scheme refinements with an explicit lattice/fan dependency.
- Coble/K3 geometry cards: remain downstream of scheme, variety, surface, divisor, Picard, and lattice vocabulary.

## Follow-Up Routing

No new card is needed from this scheme pass. Existing sibling cards own the remaining specialization work:

- Variety convention and hypotheses belong to `TASK-INTEGRATE-VARIETIES-CATEGORY`.
- Curve/surface/family method ownership belongs to the existing curve, surface, and family cards.
- Backend-method inventory reconciliation belongs to `TASK-CATEGORY-METHOD-INVENTORY-BACKEND-MAPPING` and the geometry source-admission plan; this card contributes scheme-level owner constraints for that review.

## Negative Finding: Visible Backend Map Path

- Searched: `theory/references/index.md`, `theory/index.md`, `find theory -maxdepth 3`, `rg` for `software-capability-map`, and local geometry/category-spec markdown references.
- Found: no visible `theory/backends/software-capability-map.md` directory/file in this worktree; references to that path exist in cards/specs, and related backend material exists under `.agents/memories/theory/`.
- Conclusion: inference based on the current worktree: visible `theory/backends` is not currently available as source authority, so this card relies on primary upstream docs and local tracked specs rather than that missing path.
- Confidence: High for the current worktree scan.
- Gaps: I did not inspect git history or remote branches for a previously existing visible `theory/backends` tree.

## Acceptance Evidence

- Mathematical definition recorded from Stacks Project scheme definition, fiber-product construction, and Proj construction.
- Sage surfaces surveyed for generic schemes, affine schemes, `Spec`, gluing, algebraic subschemes, and morphisms/points.
- Backend surfaces surveyed for OSCAR general schemes and Macaulay2 `Spec`/`Proj` scheme-variety constructions.
- Local dependencies and downstream cards listed explicitly.
- Follow-up routing records that no new card is needed from this leaf because existing sibling and backend-mapping cards already own the remaining work.
- Blowup owner guidance is now grounded in Stacks Project Definition 31.32.1 and
  Lemma 31.32.2; no separate source-mining card is needed for the basic scheme-level
  owner claim. Backend-specific implementations of finitely presented blowups remain
  downstream of backend-method inventory reconciliation.

## Review Log

### Review 2026-05-06 (Independent Reviewer)

**Gates passed:** none.
**Gates failed:** Gate 1 Definition Grounding.
**Outcome:** revision-required, fixed in-card.

#### Gate 1 Finding: Blowup Ownership

- The card admitted `blowup(center)` ownership while saying the Rees/Proj construction
  still needed sourcing. That violated the Gate 1 requirement that method-owner claims
  record source, definition, owner, hypotheses, codomain/return object, and proof or
  implementation obligations before admission.

#### Rework

- Added Stacks Project Definition 31.32.1 and Lemma 31.32.2 as the source basis.
- Restated the owner claim with explicit hypotheses: source object `X` is a scheme,
  center is a closed subscheme or quasi-coherent ideal sheaf on `X`, and the returned
  object is the blowup scheme with structural morphism to `X`.
- Kept backend implementation limitations as implementation refinements rather than
  owner data.

### Re-Review 2026-05-06 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3
Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and
Compliance.
**Gates failed:** none.
**Outcome:** pass; card remains `needs-review` pending human acceptance.

#### Residual Risk

- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` still contains older candidate
  wording for `blowup(center)`. This research card routes that reconciliation through
  the existing backend/method inventory path rather than editing the inventory in this
  leaf.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for schemes, recorded mathematical owner guidance, backend evidence, downstream routing, and the visible-backend-map negative finding.
- 2026-05-06: Reworked the Gate 1 blowup finding by adding Stacks Project blowup
  sources and making the center/return-object hypotheses explicit. The card remains
  `needs-review` pending re-review; it is not marked complete.
- 2026-05-06: Recorded independent re-review pass. The card remains `needs-review`
  pending human acceptance; it is not marked complete.
