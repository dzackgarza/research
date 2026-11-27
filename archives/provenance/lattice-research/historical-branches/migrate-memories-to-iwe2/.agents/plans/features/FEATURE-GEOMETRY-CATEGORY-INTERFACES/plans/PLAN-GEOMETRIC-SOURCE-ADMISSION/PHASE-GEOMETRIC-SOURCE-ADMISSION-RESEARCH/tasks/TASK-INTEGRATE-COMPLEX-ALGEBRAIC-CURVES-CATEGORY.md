---
id: TASK-INTEGRATE-COMPLEX-ALGEBRAIC-CURVES-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn:
- '[[TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY]]'
title: Research category integration for complex algebraic curves
status: complete
priority: high
description: Research and prepare the category-spec integration path for complex algebraic
  curves.
successCriteria:
- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut
  objects, and representative examples with category obligations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed
  to proceed.
complexity: 65
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-GEOMETRIC-SOURCE-ADMISSION
- PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH
---
# Research category integration for complex algebraic curves

## Summary

Research and prepare the category-spec integration path for complex algebraic curves.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating complex algebraic curves.

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Acceptance Criteria

- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut objects, and representative examples with category obligations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Research Result

Status: needs-agent-review. Complex algebraic curves are source-grounded as dimension-one complex varieties, with smooth/proper/projective/Riemann-surface surfaces routed to stricter refinements. This card does not authorize implementation.

## Mathematical Definition

Source evidence:

- Stacks Project, Curves, Definition 33.43.1, https://stacks.math.columbia.edu/tag/0A23: a curve over a field `k` is a variety of dimension `1` over `k`.
- Stacks Project, Curves, Section 53.8, https://stacks.math.columbia.edu/tag/0BY6: the curve genus section gives a dimension-one specialization and notes arithmetic-genus conventions via `chi(O_X)` for proper curves.
- Stacks Project, Curves, Remark 53.11.2, https://stacks.math.columbia.edu/tag/0BYG: arithmetic genus and geometric genus are discussed for proper smooth varieties of arbitrary dimension over algebraically closed fields; curve genus is a low-dimensional specialization, not the global owner of these invariant names.
- `TASK-INTEGRATE-VARIETIES-CATEGORY` records `Varieties(k)` as integral separated finite-type schemes over `k`.
- `TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY` records complex varieties as varieties over the selected complex base field, keeping analytic and numerical-complex surfaces as bridges/backends.

Project vocabulary:

- `ComplexAlgebraicCurves()` should mean `ComplexVarieties().Dimension(1)` or the repo's equivalent dimension-one refinement.
- `SmoothProjectiveComplexCurves()` should be the owner for compact Riemann-surface and Jacobian-style surfaces.
- `PlaneCurves(CC)`, `ProjectivePlaneCurves(CC)`, `AffineCurves(CC)`, `HyperellipticCurves(CC)`, and `RationalSexticCurves(CC)` are presented/refined curve categories, not replacements for generic curves.
- Singular or reducible plane algebraic sets should remain presented scheme/algebraic-set refinements unless the integral dimension-one variety hypotheses are established.

Boundary decisions:

- A complex algebraic curve is not merely a polynomial equation in two variables; that is a presentation of an affine or projective plane curve.
- `RiemannSurface` surfaces are analytic bridges associated to suitable complex algebraic curves, not the base algebraic curve category.
- `genus()` on curves is a dimension-one alias/convention surface, not evidence that arithmetic genus, geometric genus, Hodge numbers, Kodaira dimension, or canonical invariants are curve-owned. Those broader invariants are inherited from proper/projective/smooth variety or scheme refinements when their hypotheses hold.
- Curve specs must distinguish geometric genus, arithmetic genus, and topological genus for associated compact Riemann surfaces where those names appear. Do not collapse these names.
- Normalization returns a normalized curve with a normalization morphism; it is not just a simplified equation or a raw function field.

## Sage Surface Survey

Source evidence:

- Sage curves overview, https://doc.sagemath.org/html/en/reference/curves/index.html, says Sage supports curves in affine and projective ambient spaces, curves over `CC` as Riemann surfaces, and Jacobians of projective curves.
- Sage base curve documentation, https://sagemath.gitlab.io/documentation/html/en/reference/curves/sage/schemes/curves/curve.html, exposes curve surfaces including `genus()` and documents that one genus convention is the genus of the normalization of the projective closure over the algebraic closure of the base field.
- Sage Riemann surface documentation, https://doc.sagemath.org/html/en/reference/curves/sage/schemes/riemann_surfaces/riemann_surface.html, provides a `RiemannSurface` model for plane algebraic curves and period/Riemann-matrix computations.
- Sage curve index lists affine curves, projective curves, plane conics, plane quartics, rational/closed points, Riemann surfaces, and Jacobians as separate surfaces.

Inference:

Sage provides strong implementation evidence for presented affine/projective curves and analytic Riemann-surface bridges, but the project should keep the generic curve category scheme/variety-theoretic. Sage genus naming is especially convention-sensitive and must be translated into explicit project surfaces.

## Backend Survey

Source evidence:

- Macaulay2 Varieties package documentation, https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/, supplies affine/projective variety infrastructure used by curve computations.
- Macaulay2 PlaneCurveLinearSeries documentation, https://www.macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/PlaneCurveLinearSeries/html/, includes plane-curve linear-series surfaces such as `geometricGenus` and normalization/canonical-model related methods.
- OSCAR projective plane curves documentation, https://docs.oscar-system.org/stable/AlgebraicGeometry/Curves/ProjectivePlaneCurves/, models projective plane curves as reduced projective algebraic sets and exposes `ProjectivePlaneCurve`, `defining_equation`, `degree`, and plane-curve-specific methods.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` routes `Curve.genus()`, `Curve.arithmetic_genus()`, `Curve.normalization()`, plane-curve equation/dual-curve methods, and rational-sextic node methods to Sage, Singular, Macaulay2, and OSCAR backend candidates.

Inference:

Macaulay2, Singular, OSCAR, and Sage are all plausible curve backends, but most support is for presented affine/projective/plane curves. Generic curve methods need exact hypotheses and should route to backend adapters only after the representation is known.

## Local Category-Spec Dependencies

Source evidence:

- `TASK-INTEGRATE-SCHEMES-CATEGORY` supplies scheme and morphism vocabulary.
- `TASK-INTEGRATE-VARIETIES-CATEGORY` supplies the integral separated finite-type variety convention.
- `TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY` supplies the complex base-field and analytic-bridge boundary.
- `TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE` separately owns detailed Riemann-surface API mapping.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` already lists candidate curve, plane-curve, divisor, and rational-sextic method rows.

Inference:

The complex algebraic curve card should stabilize the dimension-one owner and route method names by hypotheses. It should not absorb the Riemann-surface backend card, divisor/sheaf cards, or Coble rational-sextic implementation work.

## Method Ownership Guidance

Admit these as curve-level or curve-refinement surfaces when downstream specs are written:

- `dimension() == 1`: defining refinement from varieties to curves.
- `genus()`: a curve-specific public alias only after the exact convention is chosen. For smooth projective complex curves this can agree with Riemann-surface genus and the dimension of `H^1(O_X)`, but the alias must point back to the broad invariant it specializes.
- `arithmetic_genus()` and `geometric_genus()`: inherited from proper/projective/smooth scheme or variety refinements with recorded hypotheses. Curve refinements may provide dimension-one formulas, normalization-backed computations, or backend routes, but they do not own the global invariant names.
- `normalization()`: inherited from broader integral scheme/variety normalization surfaces where available; curve refinements own low-dimensional computation routes and codomain sharpening to a normalized curve with normalization morphism.
- `rational_points(K)` / `complex_points()`: Hom/point surfaces inherited from varieties; enumeration/approximation is backend-specific.
- `riemann_surface()` / `analytic_space()`: bridge from suitable smooth/projective complex curves or presented plane curves to analytic Riemann-surface objects.
- `jacobian()`: owned by smooth projective curves, not arbitrary curves.
- `equation()`, `defining_equation()`, `dual_curve()`: owned by plane-curve refinements.
- `nodes()`, `is_nodal()`: owned by singular plane-curve or rational-sextic refinements with node certificates as finite scheme/point data.

## Downstream Work Unblocked Or Routed

This card gives source-grounded input to these sibling cards and downstream specs:

- `TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE`: detailed Sage Riemann-surface constructor/method mapping remains there.
- `TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES`: curve-family monodromy must use curve/family vocabulary rather than raw polynomial parameter lists.
- `TASK-INTEGRATE-FAMILIES-OF-VARIETIES-CATEGORY`: families of curves are morphisms whose fibers are curves under explicit hypotheses.
- Coble rational-sextic geometry: rational sextic/node/normalization methods are downstream plane-curve refinements, not generic curve methods.

## Follow-Up Routing

No new card is needed from this curve pass. Existing sibling cards own the remaining specialization work:

- Riemann-surface API mapping belongs to `TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE`.
- Family/monodromy/Picard-Fuchs work belongs to the existing curve-complement and families cards.
- Rational sextic and Coble-specific curve methods remain downstream of Coble geometry cards and plane-curve refinements.

## Acceptance Evidence

- Mathematical convention recorded from Stacks curve definition plus the already-recorded variety and complex-variety cards.
- Corrected invariant ownership so `genus()` is only a curve alias/specialization, while arithmetic/geometric genus and similar global invariants are inherited from broad scheme/variety refinements.
- Sage surfaces surveyed for affine/projective curves, curves over `CC` as Riemann surfaces, and Jacobians.
- Backend surfaces surveyed for Macaulay2 plane-curve linear series, OSCAR projective plane curves, and existing Sage/Singular/Macaulay2 routing rows.
- Local dependencies and downstream cards listed explicitly.
- Follow-up routing records that no new card is needed because existing Riemann-surface, family, monodromy, and Coble cards own specialization.

## Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** None
**Outcome:** complete

#### Evidence

**Gate 1 — Definition Grounding:**
- Mathematical definitions cite Stacks Project (tags 0A23, 0BY6, 0BYG) for curve dimension and genus conventions.
- Project vocabulary traces to sibling cards (INTEGRATE-VARIETIES-CATEGORY, INTEGRATE-COMPLEX-VARIETIES-CATEGORY).
- Sage surface claims cite https://doc.sagemath.org/ documentation URLs.
- Backend claims cite Macaulay2 and OSCAR documentation URLs.

**Gate 2 — Acceptance Criteria:**
- [x] Mathematical definition and project vocabulary identified → dimension-one complex variety convention with Stacks backing.
- [x] Sage/backend surfaces surveyed → Sage curves, Macaulay2 PlaneCurveLinearSeries, OSCAR projective plane curves.
- [x] Category relationships determined → schemes → varieties → complex varieties → curves chain, with plane-curve refinements as presentations.
- [x] Downstream work listed → Riemann-surface, families, monodromy, Coble cards.
- [x] Follow-up cards routed → no new cards needed; existing sibling cards own specialization.

**Gate 3 — Spec-Weakening:**
- No staged or unstaged diffs; this is a research card producing documentation only.

**Gate 4 — Gradient:**
- Genus convention corrected: `genus()` is a curve-level alias, not the global owner of arithmetic/geometric genus names. This sharpens the method ownership inventory, not reverses it.

**Gate 5 — Mathematical Correctness:**
- Curve = dimension-one variety is the standard definition (Stacks 0A23, Hartshorne I.6).
- Genus conventions correctly separated (geometric genus, arithmetic genus, topological genus for Riemann surfaces).
- Boundary decisions (normalization returns a morphism, not a simplified equation) are mathematically correct.

**Gate 6 — Style and Compliance:**
- Research card format with clear evidence/inference separation.
- Source URLs cited inline.
- `just plan-validate` passes.

---

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for complex algebraic curves, recording the dimension-one complex-variety convention and routing genus, normalization, Riemann-surface, Jacobian, plane-curve, and node surfaces to proper refinements.
- 2026-05-06: Corrected over-narrow invariant ownership: genus variants, Hodge/Kodaira-style invariants, Euler characteristics, and canonical data are broad scheme/variety-refinement surfaces before curve specialization.
- 2026-05-06: Added explicit DAG prerequisite edges for source-admission substrate dependencies. These are sequencing edges, not blockers; the card should wait until the prerequisite source cards are accepted.
