---
id: TASK-INTEGRATE-FAMILIES-OF-VARIETIES-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn:
- '[[TASK-INTEGRATE-SCHEMES-CATEGORY]]'
- '[[TASK-INTEGRATE-VARIETIES-CATEGORY]]'
title: Research category integration for families of varieties
status: complete
priority: high
description: Research and prepare the category-spec integration path for families of varieties.
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
# Research category integration for families of varieties

## Summary

Research and prepare the category-spec integration path for families of varieties.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating families of varieties.

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Acceptance Criteria

- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Dependencies And Boundaries

This is a research/planning card, not an implementation card. Do not write category code or specs until the vocabulary, ownership boundaries, and dependencies are clear or an approved plan delegates that work.

## Research Result

Status: needs review. Families of varieties are source-grounded as morphisms whose
fibers satisfy variety hypotheses, with flat/proper/finite-presentation/polarized
families routed to stricter morphism refinements. This card does not authorize
implementation.

## Mathematical Definition

Source evidence:

- Stacks Project, Schemes, Definition 26.9.1, https://stacks.math.columbia.edu/tag/01II: schemes are the ambient category in which relative objects and morphisms live.
- Stacks Project, Varieties, Definition 33.3.1, https://stacks.math.columbia.edu/tag/020C: varieties over a field are integral separated finite-type schemes over that field.
- Stacks Project, Morphisms, Definition 29.25.1, https://stacks.math.columbia.edu/tag/01U2: flatness is a property of a morphism `f: X -> S` and its structure sheaf; flatness is stable under base change.
- Stacks Project, Morphisms, Definition 29.41.1 and Lemma 29.41.5, https://stacks.math.columbia.edu/tag/01W0: proper morphisms are separated, finite type, and universally closed, and properness is stable under base change.
- Stacks Project, Quot and Hilbert Spaces, Situation 99.14.1, https://stacks.math.columbia.edu/tag/0D1L: polarized proper schemes are pairs `(X -> S, L)` with `X -> S` proper, flat, finite presentation and `L` relatively ample; morphisms are cartesian base changes plus compatible line bundles.
- `TASK-INTEGRATE-SCHEMES-CATEGORY` records `Schemes().Over(S)`, `base_scheme()`, `structure_morphism()`, and scheme morphism vocabulary.
- `TASK-INTEGRATE-VARIETIES-CATEGORY` records the project convention for `Varieties(k)`.

Project vocabulary:

- `FamiliesOfVarieties()` should be a refinement of scheme morphisms `f: X -> S`, not a separate object universe.
- The minimally meaningful family object has `total_space = X`, `base = S`, and `structure_morphism = f`.
- A fiber over a point `s -> S` is the base change `X_s = X x_S Spec(k(s))`; it is a variety only after the fiber satisfies the variety hypotheses over `k(s)`.
- `FlatFamiliesOfVarieties()`, `ProperFamiliesOfVarieties()`, `ProjectiveFamiliesOfVarieties()`, `SmoothFamiliesOfVarieties()`, and `PolarizedFamiliesOfVarieties()` are morphism refinements, not unrelated subclasses.
- A one-parameter hypersurface family is a presented-family refinement with base a curve or affine line and a hypersurface presentation; it is not the definition of a family.

Boundary decisions:

- Do not model a family as a list of fibers, a parameterized polynomial alone, or a hidden mutable object with a current parameter. The public mathematical object is the morphism plus any admitted extra data.
- `specialization()`, `generic_fiber()`, and `fiber(s)` are fiber/base-change constructions. Their codomain is a scheme first; variety, curve, surface, smooth, proper, or projective codomains require inherited hypotheses.
- Flatness, properness, smoothness, finite presentation, and relative ampleness are morphism properties. Do not move them to the fiber category or infer them from a backend class name.
- Monodromy, Picard-Fuchs operators, and variation-of-Hodge-structure outputs require stricter smooth/proper or punctured-base hypotheses and typed result objects. They are not methods on arbitrary families of varieties.
- Constant Hilbert polynomial, cohomology-and-base-change behavior, and related invariants belong behind flat/projective/polarized hypotheses; do not expose them on arbitrary families.

## Sage Surface Survey

Source evidence:

- Sage scheme documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/scheme.html, exposes `base_scheme()`, `base_morphism()`, and `base_extend(...)` surfaces. These are direct evidence for treating relative geometry through schemes over bases and base change.
- Sage scheme morphism documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/morphism.html, exposes `Hom(...)`, scheme morphisms between affine/projective schemes, and `change_ring(...)` examples.
- Existing geometry cards record that curve-family and surface-family monodromy must use family vocabulary rather than raw polynomial parameter lists.

Inference:

Sage provides useful scheme and morphism plumbing, but it does not by itself supply a complete public `FamilyOfVarieties` category. Project specs should define families as morphism refinements and then route presented/hypersurface/monodromy adapters through explicit hypotheses.

## Backend Survey

Source evidence:

- `.agents/memories/theory/backends/abstract-to-external-mapping.md` lists `FamilyOfVarieties.specialization()` and `FamilyOfVarieties.monodromy()` as abstract surfaces with Sage candidate backends.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` records family `specialization()` and `monodromy()` as candidate rows needing codomain decisions.
- `SPEC-HISTORICAL-FAMILY-MONODROMY-BACKEND-SURFACE.md` requires a family object with explicit base, total space, and fiber operation; one-parameter hypersurface helpers are valid only under explicit hypersurface and base-curve hypotheses.
- `TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES` records downstream Picard-Fuchs and monodromy backend research for curve and surface families.

Inference:

Backend evidence is thin and currently candidate-level. Specialization can likely be built from scheme base change once representations exist. Monodromy/Picard-Fuchs requires separate exact-backend research and should remain outside this source-admission card.

## Local Category-Spec Dependencies

Source evidence:

- `TASK-INTEGRATE-SCHEMES-CATEGORY` supplies morphism, base-scheme, and fiber-product vocabulary.
- `TASK-INTEGRATE-VARIETIES-CATEGORY` supplies the fiber variety convention.
- `TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY`, `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-CURVES-CATEGORY`, and `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY` route complex, curve, and surface refinements through this family vocabulary.
- `TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES` and `SPEC-HISTORICAL-FAMILY-MONODROMY-BACKEND-SURFACE` own backend-specific monodromy/Picard-Fuchs research.

Inference:

The family card should stabilize the morphism owner and keep downstream monodromy, Picard-Fuchs, Coble, and K3 uses from treating parameterized equations as a substitute for a typed family.

## Method Ownership Guidance

Admit these as family-level or family-refinement surfaces when downstream specs are written:

- `total_space()`, `base_scheme()` / `base()`, and `structure_morphism()`: structural surfaces of a family as a morphism `X -> S`.
- `fiber(s)`: base-change construction `X x_S Spec(k(s))`; codomain is first a scheme, with variety/curve/surface refinements only under hypotheses.
- `generic_fiber()` and `special_fiber(s)`: owned by families over an integral or pointed base with the relevant point/generic-point data.
- `base_change(S_prime -> S)`: morphism-level construction returning the pulled-back family `X x_S S' -> S'`; flat/proper/refinement properties are inherited only when theorems apply.
- `is_flat()`, `is_proper()`, `is_smooth()`, `is_projective()`, `is_finite_presentation()`: morphism-property predicates or refinements, not fiber methods.
- `polarization()` / `relatively_ample_line_bundle()`: owned by polarized/projective family refinements.
- `hilbert_polynomial()`: owned by polarized/projective flat families or presented fibers with a chosen polarization; do not expose on arbitrary families.
- `specialization()`: public spelling should be either a fiber/base-change alias or a typed specialization morphism after a decision; it should not return an untyped backend artifact.
- `monodromy()` and `picard_fuchs_operator()`: owned by smooth/proper family plus local-system or hypersurface-family refinements with typed result objects and backend provenance.

## Downstream Work Unblocked Or Routed

This card gives source-grounded input to these sibling cards and downstream specs:

- Curve and surface family monodromy cards must use `total_space`, `base`, and `fiber` vocabulary before backend computation.
- Coble/K3 family and degeneration work must state whether it has a flat/proper/smooth/polarized family, a one-parameter degeneration, or only a presented hypersurface equation.
- Complex manifold and analytic bridge cards can refer to smooth proper complex algebraic families only through a bridge, not by replacing algebraic families with analytic ones.
- Backend-method inventory can keep `specialization()` and `monodromy()` as candidate rows, with codomain decisions deferred to spec work.

## Follow-Up Routing

No new card is needed from this family source-admission pass.

- Monodromy and Picard-Fuchs backend evidence remains in `TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES` and historical backend recovery specs.
- A later spec card should decide the public spelling and codomain for `specialization()` versus `fiber(s)`.
- Hypersurface-family helpers belong to presented-family refinements after scheme/variety and polynomial-ring presentation specs exist.

## Acceptance Evidence

- Mathematical convention recorded from Stacks scheme, variety, flat morphism, proper morphism, and polarized proper scheme sources.
- Sage surfaces surveyed for scheme base morphisms, base extension, and scheme morphisms.
- Backend surfaces surveyed for candidate specialization and monodromy rows.
- Local dependencies and downstream cards listed explicitly.
- Follow-up routing records that no new card is needed because existing monodromy/Picard-Fuchs and historical backend cards own specialization.

## Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** None
**Outcome:** complete

#### Evidence

**Gate 1 — Definition Grounding:** Stacks sources for scheme, variety, flat/proper/polarized morphism definitions. Sage backend docs for scheme morphisms.
**Gate 2 — Acceptance Criteria:** Convention recorded from Stacks; Sage/backend surfaces surveyed; dependencies listed; follow-up routing to monodromy/Picard-Fuchs cards.
**Gate 3-6:** No issues. Research card documenting family = morphism with fiber-by-base-change definition. Correct distinction between family morphism, fiber, and specialization.

---

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for families of varieties, recording family objects as morphism refinements with fibers defined by base change and monodromy/Picard-Fuchs routed to stricter downstream backend cards.
- 2026-05-06: Added explicit DAG prerequisite edges for source-admission substrate dependencies. These are sequencing edges, not blockers; the card should wait until the prerequisite source cards are accepted.
