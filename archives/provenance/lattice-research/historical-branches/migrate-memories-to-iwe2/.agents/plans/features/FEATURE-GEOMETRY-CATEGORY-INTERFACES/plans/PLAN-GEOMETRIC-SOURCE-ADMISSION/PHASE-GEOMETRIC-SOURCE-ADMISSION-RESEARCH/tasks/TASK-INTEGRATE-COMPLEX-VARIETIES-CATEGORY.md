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
- State which Sage methods/classes and external exact systems realize presented complex varieties or their invariants.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut
  objects, and mathematical assertions that tests should check.
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

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage and external implementation witnesses, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Acceptance Criteria

- Identify the mathematical definition and the intended project vocabulary for this category.
- State which Sage methods/classes and external exact systems realize presented complex varieties or their invariants.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut objects, and mathematical assertions that tests should check.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Research Result

Status: needs-agent-review. Complex varieties are source-grounded as varieties over the
chosen complex base field. Analytification, Hodge invariants, Picard comparison, and
period data are separate constructions or invariants with their own hypotheses. This
card does not authorize implementation.

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
- `SmoothComplexVarieties()`, `ProperComplexVarieties()`, `ProjectiveComplexVarieties()`, and `SmoothProjectiveComplexVarieties()` should be refinements because Hodge cohomology, algebraic Picard data, canonical classes, coherent cohomology, and period-domain constructions require these hypotheses.
- `ComplexManifolds()` is a different analytic category. A smooth complex variety may have an associated complex manifold/analytic space, but the algebraic category should not collapse into complex manifolds.

Boundary decisions:

- Use the existing variety convention and specialize the base field to the complex numbers; do not create a non-scheme “complex variety” root.
- Do not treat Sage's numerical `CC` precision parent as automatically identical to every mathematically complex base. Category specs should distinguish the exact algebraically closed field convention from numerical complex-field implementation anchors.
- `analytification(X)` is a functor or construction from suitable algebraic varieties over the chosen complex base to complex analytic spaces. GAGA-style statements are comparison theorems or equivalences under proper/projective hypotheses, not justification for moving algebraic methods to `ComplexManifolds()`.
- Hodge-theoretic methods such as `hodge_number(p, q)` are not owned by all complex varieties; they require smooth/proper/projective or otherwise source-backed cohomological hypotheses.
- Arithmetic genus, geometric genus, Kodaira dimension, Hodge numbers, holomorphic Euler characteristic, and canonical data are not curve/surface-exclusive. Complex curve and algebraic-surface cards may specialize these invariants, but the weakest category is the broadest complex scheme/variety refinement satisfying the definition's hypotheses.

## Sage Implementation Evidence

Source evidence:

- Sage algebraic schemes documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/algebraic_scheme.html, represents presented algebraic schemes over ambient spaces and base rings/fields and provides methods including `base_ring()`, `coordinate_ring()`, `dimension()`, `is_irreducible()`, `reduce()`, and defining equations.
- Sage scheme overview, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/overview.html, organizes algebraic geometry through schemes, ambient affine/projective spaces, and subschemes rather than a generic complex-variety category.
- Sage fixed and arbitrary precision complex fields documentation, https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/complex_field.html, records `ComplexField(prec)` as an arbitrary-precision complex-number field object; this is implementation evidence for numerical complex bases, not a mathematical replacement for exact algebraically closed fields.
- Sage toric variety documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/toric/variety.html, exposes toric varieties over fields and specialized toric variety classes; toric integration remains in its own card.

Inference:

Sage supports complex base rings/fields through the scheme and ambient-space machinery, but the generic “complex variety” boundary must be imposed by project vocabulary and hypothesis checks. Numeric complex fields are useful for computations but should not silently replace exact algebraic base-field semantics.

## External Implementation Evidence

Source evidence:

- Macaulay2 `CC'` documentation, https://macaulay2.com/doc/Macaulay2-1.22/share/doc/Macaulay2/Macaulay2Doc/html/___C__C_sq.html, records the complex-number parent class used by Macaulay2 rings such as `CC[x,y,z]`.
- Macaulay2 Varieties package documentation, https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/, represents affine/projective varieties, `Spec`, `Proj`, smoothness, singular locus, Hilbert polynomial, canonical bundle, tangent/cotangent sheaves, and cohomology computations.
- Macaulay2 NumericalAlgebraicGeometry documentation, https://www.macaulay2.com/doc/Macaulay2-1.23/share/doc/Macaulay2/NumericalAlgebraicGeometry/html/index.html, explicitly works over `CC` for numerical solutions and numerical varieties.
- OSCAR projective varieties documentation, https://docs.oscar-system.org/stable/AlgebraicGeometry/AlgebraicVarieties/ProjectiveVariety/, describes projective varieties over algebraically closed fields as projective schemes with geometric integrality conditions.
- OSCAR affine varieties documentation, https://docs.oscar-system.org/stable/AlgebraicGeometry/AlgebraicVarieties/AffineVariety/, supplies affine variety constructors and irreducibility/geometric-integrality predicates.

Inference:

Macaulay2 and OSCAR are implementation witnesses for presented affine/projective
varieties and selected invariants. Macaulay2's `CC` and numerical algebraic-geometry
package are evidence for approximate complex computations, while OSCAR's algebraically
closed field/geometric-integrality language better matches exact algebraic categories.
The project should keep exact and numerical complex implementations separate in adapter
cards.

## Local Category-Spec Dependencies

Source evidence:

- `TASK-INTEGRATE-SCHEMES-CATEGORY` supplies `Schemes().Over(S)` and affine/projective/presented scheme vocabulary.
- `TASK-INTEGRATE-VARIETIES-CATEGORY` supplies the integral separated finite-type variety convention.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` lists geometry candidate rows for Hodge numbers, Kodaira dimension, Picard group, canonical class, and cohomological invariants, but leaves geometry source-definition cards to state weakest categories and hypotheses.
- `SPEC-MAPPING-RINGS.md` distinguishes fixed and parameterized complex-field objects and warns against collapsing precision-family constructors into a one-object category.

Inference:

The complex-variety card is a base-field refinement plus a source for later
analytification and comparison constructions. It should not duplicate curve/surface/
family/toric definitions; it should constrain those cards to specify whether they
require exact algebraic complex fields, numerical complex approximations, an
analytification functor, or a comparison theorem.

## Mathematical Assertions For Later Specs

These are the statements downstream specs should make precise:

- `base_field()` / `base_scheme()`: inherited from schemes/varieties over `Spec(CC)` or the selected exact complex-field object.
- `complex_points()` or `points(CC)`: for `X` over `CC`, the mathematical object is `Hom(Spec(CC), X)`; enumeration or approximation requires additional computational hypotheses.
- `analytic_space()` or `analytification()`: for suitable complex algebraic varieties, this constructs `X^an` in complex analytic spaces; it is not a replacement for algebraic category membership.
- `hodge_number(p, q)`: for `X` in the relevant smooth proper/projective complex refinement, this returns an integer invariant `h^{p,q}(X)` under stated cohomological hypotheses.
- `arithmetic_genus()`, `geometric_genus()`, `holomorphic_euler_characteristic()`, `canonical_class()` / `canonical_bundle()`, and `kodaira_dimension()`: inherited from broad proper/projective/smooth complex variety or scheme refinements with the exact convention and hypotheses recorded; curves and surfaces expose low-dimensional aliases/formulas only as specializations.
- `period_domain()`, `period_map()`, and Hodge structures: downstream of smooth proper/projective families or K3/surface refinements, not all complex varieties.
- `picard_group()`: algebraic Picard data; analytic Picard/Brauer comparisons require separate comparison maps or theorems with hypotheses.
- Numerical solving and homotopy-continuation outputs: implementation results for presented complex varieties, not public mathematical codomains unless wrapped as certified or approximate solution objects.

## Downstream Consequences

This card gives source-grounded input to these sibling cards and downstream specs:

- `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-CURVES-CATEGORY`: curves are dimension-one complex varieties with smooth/proper/projective refinements as required.
- `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY`: algebraic surfaces are dimension-two complex varieties and support K3/Coble/Enriques prerequisites only after surface-specific source definitions.
- `TASK-INTEGRATE-FAMILIES-OF-VARIETIES-CATEGORY`: complex families must state whether base and fibers are algebraic over `CC`, analytic, or bridged by analytification.
- `TASK-INTEGRATE-SMOOTH-MANIFOLDS-CATEGORY` and `TASK-INTEGRATE-COMPLEX-MANIFOLDS-CATEGORY`: analytic manifold categories are related by analytification, forgetful functors, or comparison theorems, not by inheritance from all complex varieties.
- Coble/K3 geometry cards: use smooth projective complex surface/K3 refinements, not generic complex-variety methods.

## Follow-Up Records

No new card is needed from this complex-variety pass. Existing sibling cards own the remaining specialization work:

- Exact complex field versus numerical complex implementation handling belongs to later adapter cards once specs consume these definitions.
- Complex curve, surface, family, and manifold functors or comparison maps belong to their existing source-definition cards.
- Hodge/Picard/period-domain details remain downstream of surface/K3/lattice source cards and `research-proof-auditing` when proof claims are involved.

## Acceptance Evidence

- Mathematical convention recorded by specializing the Stacks/project variety definition to the complex base field.
- Sage implementation evidence surveyed for schemes over complex base objects and complex-field implementation anchors.
- External implementation evidence surveyed for Macaulay2 complex rings/numerical algebraic geometry and OSCAR affine/projective varieties.
- Local dependencies and downstream cards listed explicitly.
- Follow-up notes record that no new card is needed because existing sibling cards define curve, surface, family, manifold, and implementation specializations.
- Correction recorded that global invariants such as genus variants, Hodge numbers, Kodaira dimension, Euler characteristics, and canonical data belong to broad complex scheme/variety refinements before curve/surface specialization.

## Review Log

### Review 2026-05-07 (Independent Reviewer)

**Checks passed:** Check 1 Definition Grounding, Check 2 Acceptance Criteria, Check 3 Spec-Weakening, Check 4 Gradient, Check 5 Mathematical Correctness, Check 6 Style and Compliance
**Checks failed:** None
**Outcome:** complete

#### Evidence

**Check 1 — Definition Grounding:**
- Mathematical definition cites Stacks Project (tag 0A23 curves, tag 0BY6 genus, tag 0BYG) and sibling variety card.
- Sage scheme implementation evidence cites doc.sagemath.org URLs.
- Backend survey cites Macaulay2, Singular, and OSCAR documentation.

**Check 2 — Acceptance Criteria:**
- Mathematical definition recorded by specializing the project variety definition with additional base-field conventions (smooth/proper/projective refinements).
- Sage implementation evidence surveyed for complex base-object schemes.
- External implementation evidence surveyed for Macaulay2 complex rings and OSCAR varieties.
- Local dependencies and downstream cards listed (curves, surfaces, Coble).
- Follow-up notes track that sibling cards define the specializations.

**Check 3 — Spec-Weakening:** No staged or unstaged diffs; research documentation only.
**Check 4 — Gradient:** Genus/Hodge/Kodaira invariant placement corrected to broad scheme/variety refinements, sharpening the inventory.
**Check 5 — Mathematical Correctness:** Complex variety = variety over complex base field is the standard definition.
**Check 6 — Style and Compliance:** Research card format with evidence/inference separation; source URLs cited inline.

---

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-definition research for complex varieties, specializing the project variety convention to complex bases while keeping analytification, Hodge invariants, and numerical-complex outputs behind stricter refinements, functors, or comparison theorems.
- 2026-05-06: Corrected invariant placement so curve/surface cards inherit arithmetic/geometric genus, Hodge, Kodaira, Euler-characteristic, and canonical data from broad complex variety/scheme refinements.
- 2026-05-06: Added explicit DAG prerequisite edges for source-definition substrate dependencies. These are sequencing edges, not blockers; the card should wait until the prerequisite source cards are accepted.
