---
id: TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn:
- '[[TASK-INTEGRATE-VARIETIES-CATEGORY]]'
title: Research category integration for complex varieties
status: complete
priority: high
description: Research and prepare the category-spec integration path for complex varieties.
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
# Research category integration for complex varieties

## Summary

Research and prepare the category-spec integration path for complex varieties.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating complex varieties.

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Acceptance Criteria

- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Research Result

Status: needs review. Complex varieties are source-grounded as varieties over the complex field, with analytic/Hodge surfaces routed to stricter smooth/proper/projective refinements. This card does not authorize implementation.

## Mathematical Definition

Source evidence:

- Stacks Project, Varieties, Definition 33.3.1, https://stacks.math.columbia.edu/tag/020C: a variety over a field `k` is an integral scheme over `k` that is separated and of finite type.
- Stacks Project, Varieties, Definition 33.33.1, https://stacks.math.columbia.edu/tag/0BEI: coherent-sheaf Euler characteristics are defined for proper schemes over fields and provide the broad cohomological substrate for holomorphic Euler characteristic and arithmetic-genus conventions.
- Stacks Project, Curves, Remark 53.11.2, https://stacks.math.columbia.edu/tag/0BYG: arithmetic genus and geometric genus are discussed for proper smooth varieties of arbitrary dimension over algebraically closed fields, not only for curves or surfaces.
- Stacks Project, Varieties, Proposition 33.45.13, https://stacks.math.columbia.edu/tag/0BJ8: canonical growth/Hilbert-style asymptotics live at the proper-scheme/projective-variety level before low-dimensional specialization.
- `TASK-INTEGRATE-VARIETIES-CATEGORY` records the repo convention `Varieties(k) = Schemes().Over(Spec(k)).FiniteType().Separated().Integral()` by default.
- `SPEC-MAPPING-RINGS.md` records that fixed complex fields such as `CC`, `CDF`, `CIF`, and parameterized `ComplexField(...)` are field/ring constructor outputs with precision/topology refinements rather than one interchangeable object.

Project vocabulary:

- `ComplexVarieties()` should mean `Varieties(CC)` once the repo's exact complex-field object is chosen for the category parameter.
- A separate `ComplexAlgebraicVarieties()` name is probably redundant if all `ComplexVarieties()` in this algebraic-geometry subtree are algebraic varieties over `CC`; reserve that spelling for disambiguation only if the complex-manifold card needs a parallel analytic category.
- `SmoothComplexVarieties()`, `ProperComplexVarieties()`, `ProjectiveComplexVarieties()`, and `SmoothProjectiveComplexVarieties()` should be refinements because Hodge, Picard, canonical, cohomology, and period-domain surfaces need these hypotheses.
- `ComplexManifolds()` is a different analytic category. A smooth complex variety may have an associated complex manifold/analytic space, but the algebraic category should not collapse into complex manifolds.

Boundary decisions:

- Use the existing variety convention and specialize the base field to the complex numbers; do not create a non-scheme “complex variety” root.
- Do not treat Sage's numerical `CC` precision parent as automatically identical to every mathematically complex base. Category specs should distinguish the exact algebraically closed field convention from numerical complex-field implementation anchors.
- Analytification/GAGA-style bridges are bridge surfaces between algebraic varieties and complex analytic spaces/manifolds, not ownership justification for moving algebraic methods to `ComplexManifolds()`.
- Hodge-theoretic methods such as `hodge_number(p, q)` are not owned by all complex varieties; they require smooth/proper/projective or otherwise source-backed cohomological hypotheses.
- Arithmetic genus, geometric genus, Kodaira dimension, Hodge numbers, holomorphic Euler characteristic, and canonical data are not curve/surface-exclusive. Complex curve and surface cards may specialize these surfaces, but the mathematical owner is the broadest complex scheme/variety refinement satisfying the definition's hypotheses.

## Sage Surface Survey

Source evidence:

- Sage algebraic schemes documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/algebraic_scheme.html, exposes presented algebraic-scheme surfaces over ambient spaces and base rings/fields, including `base_ring()`, `coordinate_ring()`, `dimension()`, `is_irreducible()`, `reduce()`, and defining equations.
- Sage scheme overview, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/overview.html, organizes algebraic geometry through schemes, ambient affine/projective spaces, and subschemes rather than a generic complex-variety category.
- Sage fixed and arbitrary precision complex fields documentation, https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/complex_field.html, records `ComplexField(prec)` as an arbitrary-precision complex-number field object; this is implementation evidence for numerical complex bases, not a mathematical replacement for exact algebraically closed fields.
- Sage toric variety documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/toric/variety.html, exposes toric varieties over fields and specialized toric variety classes; toric integration remains in its own card.

Inference:

Sage supports complex base rings/fields through the scheme and ambient-space machinery, but the generic “complex variety” boundary must be imposed by project vocabulary and hypothesis checks. Numeric complex fields are useful for computations but should not silently replace exact algebraic base-field semantics.

## Backend Survey

Source evidence:

- Macaulay2 `CC'` documentation, https://macaulay2.com/doc/Macaulay2-1.22/share/doc/Macaulay2/Macaulay2Doc/html/___C__C_sq.html, records the complex-number parent class used by Macaulay2 rings such as `CC[x,y,z]`.
- Macaulay2 Varieties package documentation, https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/, exposes affine/projective varieties, `Spec`, `Proj`, smoothness, singular locus, Hilbert polynomial, canonical bundle, tangent/cotangent sheaves, and cohomology surfaces.
- Macaulay2 NumericalAlgebraicGeometry documentation, https://www.macaulay2.com/doc/Macaulay2-1.23/share/doc/Macaulay2/NumericalAlgebraicGeometry/html/index.html, explicitly works over `CC` for numerical solutions and numerical varieties.
- OSCAR projective varieties documentation, https://docs.oscar-system.org/stable/AlgebraicGeometry/AlgebraicVarieties/ProjectiveVariety/, describes projective varieties over algebraically closed fields as projective schemes with geometric integrality conditions.
- OSCAR affine varieties documentation, https://docs.oscar-system.org/stable/AlgebraicGeometry/AlgebraicVarieties/AffineVariety/, supplies affine variety constructors and irreducibility/geometric-integrality predicates.

Inference:

Macaulay2 and OSCAR can support complex presented variety computations. Macaulay2's `CC` and numerical algebraic-geometry package are backend evidence for approximate complex computations, while OSCAR's algebraically closed field/geometric-integrality language better matches exact category admission. The project should keep exact and numerical complex backends separate in adapter cards.

## Local Category-Spec Dependencies

Source evidence:

- `TASK-INTEGRATE-SCHEMES-CATEGORY` supplies `Schemes().Over(S)` and affine/projective/presented scheme vocabulary.
- `TASK-INTEGRATE-VARIETIES-CATEGORY` supplies the integral separated finite-type variety convention.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` lists geometry candidate rows for Hodge numbers, Kodaira dimension, Picard group, canonical class, and cohomological invariants, but leaves geometry source-admission cards to fix owners and hypotheses.
- `SPEC-MAPPING-RINGS.md` distinguishes fixed and parameterized complex-field objects and warns against collapsing precision-family constructors into a one-object category.

Inference:

The complex-variety card is a base-field and analytic-bridge refinement. It should not duplicate curve/surface/family/toric ownership; it should constrain those cards to specify whether they require exact algebraic complex fields, numerical complex approximations, or an analytification bridge.

## Method Ownership Guidance

Admit these as complex-variety-level or refinement surfaces when downstream specs are written:

- `base_field()` / `base_scheme()`: inherited from schemes/varieties over `Spec(CC)` or the selected exact complex-field object.
- `complex_points()` or `points(CC)`: better expressed as `Hom(Spec(CC), X)` plus computational enumeration/approximation refinements.
- `analytic_space()` or `analytification()`: a bridge from suitable complex algebraic varieties to complex analytic spaces; not a replacement for algebraic category membership.
- `hodge_number(p, q)`: owned by smooth proper complex varieties or a stricter source-backed refinement.
- `arithmetic_genus()`, `geometric_genus()`, `holomorphic_euler_characteristic()`, `canonical_class()` / `canonical_bundle()`, and `kodaira_dimension()`: inherited from broad proper/projective/smooth complex variety or scheme refinements with the exact convention and hypotheses recorded; curves and surfaces expose low-dimensional aliases/formulas only as specializations.
- `period_domain()`, `period_map()`, and Hodge-structure surfaces: downstream of smooth proper/projective families or K3/surface refinements, not all complex varieties.
- `picard_group()`: inherited as an algebraic Picard surface; analytic Picard/Brauer comparisons require separate bridge hypotheses.
- Numerical solving and homotopy-continuation outputs: backend artifacts for presented complex varieties, not public mathematical codomains unless wrapped as certified or approximate solution objects.

## Downstream Work Unblocked Or Routed

This card gives source-grounded input to these sibling cards and downstream specs:

- `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-CURVES-CATEGORY`: curves are dimension-one complex varieties with smooth/proper/projective refinements as required.
- `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY`: surfaces are dimension-two complex varieties and own K3/Coble/Enriques prerequisites only after surface-specific source admission.
- `TASK-INTEGRATE-FAMILIES-OF-VARIETIES-CATEGORY`: complex families must state whether base and fibers are algebraic over `CC`, analytic, or bridged by analytification.
- `TASK-INTEGRATE-SMOOTH-MANIFOLDS-CATEGORY` and `TASK-INTEGRATE-COMPLEX-MANIFOLDS-CATEGORY`: analytic manifold categories are related by bridge surfaces, not by inheritance from all complex varieties.
- Coble/K3 geometry cards: use smooth projective complex surface/K3 refinements, not generic complex-variety methods.

## Follow-Up Routing

No new card is needed from this complex-variety pass. Existing sibling cards own the remaining specialization work:

- Exact complex field versus numerical complex backend handling belongs to later implementation/backend adapter cards once specs consume these surfaces.
- Complex curve, surface, family, and manifold bridges belong to their existing source-admission cards.
- Hodge/Picard/period-domain details remain downstream of surface/K3/lattice source cards and `research-proof-auditing` when proof claims are involved.

## Acceptance Evidence

- Mathematical convention recorded by specializing the Stacks/project variety definition to the complex base field.
- Sage surfaces surveyed for schemes over complex base objects and complex-field implementation anchors.
- Backend surfaces surveyed for Macaulay2 complex rings/numerical algebraic geometry and OSCAR affine/projective varieties.
- Local dependencies and downstream cards listed explicitly.
- Follow-up routing records that no new card is needed because existing sibling cards own curve, surface, family, manifold, and backend specialization.
- Correction recorded that global invariants such as genus variants, Hodge numbers, Kodaira dimension, Euler characteristics, and canonical data belong to broad complex scheme/variety refinements before curve/surface specialization.

## Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** None
**Outcome:** complete

#### Evidence

**Gate 1 — Definition Grounding:**
- Mathematical definition cites Stacks Project (tag 0A23 curves, tag 0BY6 genus, tag 0BYG) and sibling variety card.
- Sage scheme surface cites doc.sagemath.org URLs.
- Backend survey cites Macaulay2, Singular, and OSCAR documentation.

**Gate 2 — Acceptance Criteria:**
- Mathematical definition recorded by specializing the project variety definition with additional base-field conventions (smooth/proper/projective refinements).
- Sage surfaces surveyed for complex base-object schemes.
- Backend surfaces surveyed for Macaulay2 complex rings and OSCAR varieties.
- Local dependencies and downstream cards listed (curves, surfaces, Coble).
- Follow-up routing tracks that sibling cards own specialization.

**Gate 3 — Spec-Weakening:** No staged or unstaged diffs; research documentation only.
**Gate 4 — Gradient:** Genus/Hodge/Kodaira invariant ownership corrected to broad scheme/variety refinements, sharpening the inventory.
**Gate 5 — Mathematical Correctness:** Complex variety = variety over complex base field is the standard definition.
**Gate 6 — Style and Compliance:** Research card format with evidence/inference separation; source URLs cited inline.

---

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for complex varieties, specializing the project variety convention to complex bases while keeping analytic, Hodge, and numerical-complex surfaces behind stricter refinements or bridges.
- 2026-05-06: Corrected invariant ownership so curve/surface cards inherit arithmetic/geometric genus, Hodge, Kodaira, Euler-characteristic, and canonical surfaces from broad complex variety/scheme refinements.
- 2026-05-06: Added explicit DAG prerequisite edges for source-admission substrate dependencies. These are sequencing edges, not blockers; the card should wait until the prerequisite source cards are accepted.
