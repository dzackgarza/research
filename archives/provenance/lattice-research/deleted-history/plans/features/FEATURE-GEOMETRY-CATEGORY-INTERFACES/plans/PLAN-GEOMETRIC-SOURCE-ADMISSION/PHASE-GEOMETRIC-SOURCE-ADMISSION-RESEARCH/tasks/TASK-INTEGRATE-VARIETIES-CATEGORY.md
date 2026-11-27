---
id: TASK-INTEGRATE-VARIETIES-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn:
- '[[TASK-INTEGRATE-SCHEMES-CATEGORY]]'
title: Research category integration for varieties
status: needs-review
priority: high
description: Research and prepare the category-spec integration path for varieties.
successCriteria:
- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut
  surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed
  to proceed.
complexity: 65
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-GEOMETRIC-SOURCE-ADMISSION
- PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH
---
# Research category integration for varieties

## Summary

Research and prepare the category-spec integration path for varieties.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating varieties.

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Acceptance Criteria

- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Research Result

Status: needs review. The variety category has a source-grounded convention and backend surface map sufficient for downstream geometry cards. This card does not authorize implementation.

## Mathematical Definition

Source evidence:

- Stacks Project, Varieties, Definition 33.3.1, https://stacks.math.columbia.edu/tag/020C: a variety over a field `k` is an integral scheme over `k` that is separated and of finite type.
- Stacks Project, Schemes, Definition 26.9.1, https://stacks.math.columbia.edu/tag/01II: schemes are locally ringed spaces locally affine, so varieties should be represented as scheme refinements rather than as a separate non-scheme universe.
- Stacks Project, Varieties, Definition 33.33.1, https://stacks.math.columbia.edu/tag/0BEI: for a proper scheme over a field, the Euler characteristic of a coherent sheaf is a finite alternating sum of cohomology dimensions. This is broad scheme/variety infrastructure, not a curve/surface-only invariant.
- Stacks Project, Curves, Remark 53.11.2, https://stacks.math.columbia.edu/tag/0BYG: for a proper smooth variety of dimension `d` over an algebraically closed field, the arithmetic genus and geometric genus are often defined using `chi(O_X)` and top-degree differentials. The remark explicitly compares higher-dimensional varieties, so genus variants must not be owned only by curves.
- Stacks Project, Varieties, Proposition 33.45.13, https://stacks.math.columbia.edu/tag/0BJ8: asymptotic Riemann-Roch is stated for proper schemes over fields with an ample invertible sheaf, giving a broad source for Hilbert/canonical-growth style invariants before low-dimensional specialization.
- `TASK-INTEGRATE-SCHEMES-CATEGORY` records the repo's source-admitted scheme substrate: `Schemes()`, `Schemes().Over(S)`, `AffineSchemes()`, `ProjectiveSchemes()`, and presented algebraic-scheme refinements.

Project vocabulary:

- `Varieties(k)` should mean `Schemes().Over(Spec(k)).FiniteType().Separated().Integral()` by default.
- `AffineVarieties(k)` and `ProjectiveVarieties(k)` are affine/projective refinements of `Varieties(k)`, not alternatives to schemes.
- `SmoothVarieties(k)`, `ProperVarieties(k)`, `NormalVarieties(k)`, `GeometricallyIntegralVarieties(k)`, and similar refinements should be admitted only when a method needs the hypothesis.
- Reducible or nonreduced algebraic sets should live under `AlgebraicSchemes()`, `PresentedSchemes()`, `ReducedPresentedSchemes()`, or explicitly named reducible/presented refinements, not under bare `Varieties(k)` unless a later human decision changes the convention.

Boundary decisions:

- Use the Stacks integral convention for `Varieties(k)` now. This avoids silently importing software conventions where “variety” may include reducible algebraic sets.
- Geometric integrality is a stricter refinement, not the default, because Stacks highlights that products and base change over non-algebraically closed fields can fail to preserve integrality without geometric integrality hypotheses.
- The phrase “complex variety” should be handled by `TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY` as a base-field/base-analytic refinement over this variety convention.
- Do not map every Sage `AlgebraicScheme_subscheme` or Macaulay2/Oscar `variety(...)` object to `Varieties(k)` until integral, separated, finite-type, and base-field hypotheses are established.
- Do not assign arithmetic genus, geometric genus, Hodge numbers, Kodaira dimension, Euler characteristics, canonical classes, or similar global invariants to curve or surface categories merely because software exposes common low-dimensional methods. Their owners are the broadest scheme/variety refinements satisfying the definition's hypotheses; curves and surfaces inherit or specialize them.

## Sage Surface Survey

Source evidence:

- Sage algebraic schemes documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/algebraic_scheme.html, exposes polynomial-equation subscheme surfaces such as `ambient_space()`, `coordinate_ring()`, `dimension()`, `affine_patch()`, `embedding_morphism()`, `defining_ideal()`, `defining_polynomials()`, `Jacobian()`, `irreducible_components()`, `is_irreducible()`, and `reduce()`.
- Sage scheme overview, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/overview.html, presents affine/projective ambient spaces, algebraic subschemes, and generic schemes as the organizational substrate.
- Sage toric variety documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/toric/variety.html, exposes `ToricVariety`, `ToricVariety_field`, `AffineToricVariety`, and `AffineToricVariety(...).Spec()` surfaces.

Inference:

Sage is mostly scheme-first for generic algebraic geometry. Its algebraic-subscheme methods are strong implementation evidence for presented affine/projective varieties once the project verifies the integral/separated/finite-type hypotheses. Sage toric variety classes are evidence for a toric-variety refinement, but that work remains under `TASK-INTEGRATE-TORIC-VARIETIES-WITH-LATTICE-CATEGORY`.

## Backend Survey

Source evidence:

- Macaulay2 Varieties package documentation, https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/, exports `Variety`, `AffineVariety`, `ProjectiveVariety`, `Spec`, `Proj`, `isSmooth`, `singularLocus`, `hilbertPolynomial`, `canonicalBundle`, `tangentSheaf`, `cotangentSheaf`, and `HH` surfaces.
- Macaulay2 `Variety` class documentation, https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/___Variety.html, treats `Variety` as the common class for affine and projective varieties.
- OSCAR affine varieties documentation, https://docs.oscar-system.org/stable/AlgebraicGeometry/AlgebraicVarieties/AffineVariety/, documents absolute affine varieties, constructors from ideals/rings, irreducibility and geometric-integrality predicates, and affine coordinate-ring surfaces.
- OSCAR projective varieties documentation, https://docs.oscar-system.org/stable/AlgebraicGeometry/AlgebraicVarieties/ProjectiveVariety/, documents projective varieties, constructors from homogeneous ideals/graded rings, and projective invariants including sectional genus and canonical bundle surfaces.

Inference:

Macaulay2 and OSCAR are suitable backend candidates for finitely presented affine/projective variety computations, especially Hilbert polynomials, singular loci, smoothness, canonical bundles/classes, tangent/cotangent sheaves, and cohomology-driven invariants. Their naming is broader than the repo's `Varieties(k)` convention; adapter code must check or route hypotheses instead of trusting backend class names.

## Local Category-Spec Dependencies

Source evidence:

- `TASK-INTEGRATE-SCHEMES-CATEGORY` supplies the immediate scheme substrate and says varieties are downstream scheme refinements.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` lists geometry candidate rows for `blowup(center)`, `resolve_singularities()`, `picard_group()`, `kodaira_dimension()`, `hilbert_polynomial()`, `hodge_number(p,q)`, `holomorphic_euler_characteristic()`, `canonical_class()`, curve/surface/divisor/sheaf/family methods, and backend routes.
- `SPEC-MAPPING-TOPOLOGICAL-SPACES.md` records that varieties have extra algebraic-geometric structure beyond bare topology and should map to their own mathematical subtree.

Inference:

The variety card should stabilize the owner convention for algebraic-geometry methods that are not merely scheme-level. It does not decide curve, surface, divisor, sheaf, family, complex, or toric details, but it constrains those cards to inherit the integral separated finite-type scheme convention unless they explicitly choose a different named refinement.

## Method Ownership Guidance

Admit these as variety-level or variety-refinement surfaces when downstream specs are written:

- `dimension()`: first available on finite-type schemes/varieties where dimension is computationally meaningful; backend implementations may be presented-only.
- `is_smooth()`, `singular_locus()`, and `resolve_singularities()`: owned by variety or finite-type scheme refinements with characteristic and presentation hypotheses made explicit; resolution must record characteristic restrictions.
- `hilbert_polynomial()`: owned by projective varieties or graded/projective presented schemes, not arbitrary varieties.
- `canonical_class()` or `canonical_bundle()`: owned by normal/smooth/proper/projective refinements as the selected divisor/sheaf model requires.
- `kodaira_dimension()`: owned by proper variety refinements where the canonical powers and sentinel convention are fixed.
- `hodge_number(p, q)`: owned by smooth proper varieties over fields supporting Hodge theory; complex-specific interpretation belongs to the complex variety card.
- `euler_characteristic(F)` and `holomorphic_euler_characteristic()`: owned by proper schemes/varieties with coherent sheaf or structure-sheaf hypotheses; low-dimensional formulas are specializations.
- `arithmetic_genus()` and `geometric_genus()`: owned by proper/projective smooth or otherwise source-backed scheme/variety refinements with the exact convention recorded. Curve and surface cards may admit aliases or formulas only as inherited special cases.
- `picard_group()`: owned by a variety/scheme Picard surface; Picard lattice remains a separate bridge requiring surface/intersection-form hypotheses.
- `blowup(center)`: after the schemes card, prefer a scheme-level or noetherian/presented-scheme owner with closed-subscheme center; variety-preserving blowups are refinements when the result remains in `Varieties(k)`.
- `rational_points(K)`: treat as `Hom(Spec(K), X)` plus computational enumeration refinements, not a raw list method on all varieties.
- `defining_ideal()` and `defining_polynomials()`: owned by embedded/presented affine/projective varieties, not all varieties.

## Downstream Work Unblocked Or Routed

This card gives source-grounded input to these sibling cards and downstream specs:

- `TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY`: add `k = CC` or analytic/complex-geometry structure over the integral finite-type separated variety convention.
- `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-CURVES-CATEGORY` and `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY`: inherit curves/surfaces as dimension refinements of varieties with extra smooth/proper/projective hypotheses as needed.
- `TASK-INTEGRATE-FAMILIES-OF-VARIETIES-CATEGORY`: model a family as a morphism whose fibers are varieties under hypotheses, not as a list of equations over parameters.
- `TASK-INTEGRATE-TORIC-VARIETIES-WITH-LATTICE-CATEGORY`: toric varieties are variety refinements depending on fan/lattice vocabulary.
- Coble/K3 geometry and Picard-lattice cards: remain downstream of variety, surface, divisor, Picard-group, and lattice conventions.

## Follow-Up Routing

No new card is needed from this variety pass. Existing sibling cards own the remaining specialization work:

- Complex/base-field conventions belong to `TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY`.
- Curve, surface, family, and toric method ownership belongs to their existing source-admission cards.
- The Picard group versus Picard lattice bridge remains governed by the existing category-method inventory decision path.
- Backend-method inventory reconciliation remains in `TASK-CATEGORY-METHOD-INVENTORY-BACKEND-MAPPING` and its source-admission consumers.

## Acceptance Evidence

- Mathematical convention recorded from Stacks Project definition of variety over a field.
- Sage surfaces surveyed for algebraic schemes/subschemes and toric varieties.
- Backend surfaces surveyed for Macaulay2 `Varieties` and OSCAR affine/projective varieties.
- Local dependencies and downstream cards listed explicitly.
- Follow-up routing records that no new card is needed because existing sibling and backend-mapping cards own specialization and reconciliation.
- Correction recorded that global invariants such as arithmetic/geometric genus, Hodge numbers, Kodaira dimension, Euler characteristics, and canonical data must be owned by the broadest source-backed scheme/variety refinements, not by curve/surface categories by default.

## Review Log

### Review 2026-05-06 (Independent Reviewer)

**Gates passed:** none.
**Gates failed:** Gate 1 Definition Grounding.
**Outcome:** revision-required, fixed by DAG edge.

#### Gate 1 Finding: Scheme Dependency

- This card treats `TASK-INTEGRATE-SCHEMES-CATEGORY` as the source-admitted scheme
  substrate for `Varieties(k)` and related method-owner guidance, but the schemes card
  is still `needs-review` rather than human-accepted.
- The card therefore must not be reviewed as independent of schemes; it needs a
  `dependsOn` edge to `TASK-INTEGRATE-SCHEMES-CATEGORY` so the DAG prevents premature
  review or execution.

#### Rework

- Added `[[TASK-INTEGRATE-SCHEMES-CATEGORY]]` to `dependsOn`.
- Did not mark the card blocked. This is ordinary DAG sequencing: the card should wait
  until the schemes source-admission card is accepted.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for varieties, chose the Stacks integral separated finite-type convention for `Varieties(k)`, recorded backend evidence, and routed broader software usage to presented scheme/variety refinements.
- 2026-05-06: Corrected invariant ownership after source review: genus variants, Hodge numbers, Kodaira dimension, Euler characteristics, and canonical data are broad scheme/variety-refinement surfaces before curve/surface specialization.
- 2026-05-06: Added the missing DAG dependency on the schemes source-admission card
  after independent review caught that this card relies on an unaccepted scheme
  substrate. The card remains `needs-review`, but the DAG should treat it as
  dependency-waiting until schemes is accepted.
- 2026-05-09: Reclassified from human input to agent-executable review. The Stacks
  convention recorded here, a variety over `k` as an integral separated finite-type
  scheme over `k`, is the repo's source-grounded scheme-theoretic convention rather
  than a pending user choice. Backend naming drift remains an adapter warning.
