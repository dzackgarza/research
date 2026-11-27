---
id: TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn:
- '[[TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY]]'
title: Research category integration for complex algebraic surfaces
status: complete
priority: high
description: Research and prepare the category-spec integration path for complex algebraic
  surfaces.
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
# Research category integration for complex algebraic surfaces

## Summary

Research and prepare the category-spec integration path for complex algebraic surfaces.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating complex algebraic surfaces.

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Acceptance Criteria

- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Research Result

Status: needs review. Complex algebraic surfaces are source-grounded as dimension-two complex varieties, with surface-specific divisor, Picard, Hodge, K3, Enriques, Coble, and period surfaces routed to stricter refinements. This card does not authorize implementation.

## Mathematical Definition

Source evidence:

- Stacks Project, Varieties, Definition 33.3.1, https://stacks.math.columbia.edu/tag/020C: varieties over a field are integral separated finite-type schemes over that field.
- Stacks Project, Varieties, Definition 33.33.1, https://stacks.math.columbia.edu/tag/0BEI: coherent-sheaf Euler characteristics are defined for proper schemes over fields, hence holomorphic Euler characteristic and arithmetic-genus conventions are not intrinsically surface-only.
- Stacks Project, Curves, Remark 53.11.2, https://stacks.math.columbia.edu/tag/0BYG: arithmetic genus and geometric genus are discussed for proper smooth varieties of arbitrary dimension, with surfaces appearing as an example where these invariants differ.
- Stacks Project, Varieties, Proposition 33.45.13, https://stacks.math.columbia.edu/tag/0BJ8: asymptotic Riemann-Roch is a proper-scheme statement with an ample invertible sheaf, not a surface-only construction.
- `TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY` records complex varieties as varieties over the selected complex base field.
- OSCAR adjunction-process documentation, https://docs.oscar-system.org/stable/AlgebraicGeometry/Surfaces/AdjunctionProcess/, states its surface section works with smooth projective surfaces over `C`.
- `theory/foundations/reflective-two-elementary-lattices.md` records local K3 and Enriques surface definitions and Picard lattice vocabulary for downstream Coble/K3 work.
- `theory/foundations/coble-task-background.md` records Coble-specific blowup, Picard lattice, K3-cover, and period-domain source material as downstream Coble theory.

Project vocabulary:

- `ComplexAlgebraicSurfaces()` should mean `ComplexVarieties().Dimension(2)` or the repo's equivalent dimension-two refinement.
- `SmoothProjectiveComplexSurfaces()` should specialize broad smooth/proper/projective variety invariants such as Hodge numbers, canonical divisor/class surfaces, Euler characteristics, arithmetic/geometric genus, and Kodaira dimension. It does not own these names merely because surface theory uses them heavily.
- Surface-owned vocabulary should be dimension-two structure: divisor intersection forms on surfaces, Picard-to-lattice bridges after an admitted pairing, surface birational geometry refinements, and named K3/Enriques/Coble/Rational surface refinements.
- `K3Surfaces()`, `EnriquesSurfaces()`, `CobleSurfaces()`, `RationalSurfaces()`, `BlowupsOfSurfaces()`, and `DoubleCoversOfSurfaces()` are stricter refinements, not methods on all surfaces.
- Surface divisor, sheaf, Picard, and lattice objects should be first-class categories/objects rather than raw matrices or lists attached to the surface.

Boundary decisions:

- A complex algebraic surface is not merely a polynomial in three variables or a presented subscheme of projective space; that is a presentation.
- `PicardGroup` and `PicardLattice` must remain distinct. A Picard lattice requires a surface plus an admitted intersection pairing/lattice realization; it is not the generic codomain of `picard_group()`.
- K3, Enriques, and Coble surfaces are downstream named refinements with their own source requirements; do not place K3-cover, Coble-lattice, or period-domain methods on all complex surfaces.
- Divisor intersection surfaces need divisor category admission and surface smooth/proper/projective hypotheses; do not represent them as untyped matrices.
- Arithmetic genus, geometric genus, Hodge numbers, Kodaira dimension, Euler characteristics, and canonical data are broad scheme/variety-refinement invariants. Surface cards own dimension-two formulas, classification uses, and backend routes only after inheriting the broad owner.

## Sage Surface Survey

Source evidence:

- Sage algebraic schemes documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/algebraic_scheme.html, supplies presented subscheme surfaces such as dimension, defining equations, irreducibility, reduction, and coordinate rings.
- Sage scheme overview, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/overview.html, organizes surfaces as schemes/subschemes in affine/projective ambient spaces rather than a generic surface class.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` lists backend candidates for surface-adjacent methods including birational involution, double covers, K3 covers, Picard-group/lattice bridges, divisor intersections, and coherent-sheaf cohomology.

Inference:

Sage gives implementation evidence for presented schemes, double-cover/K3-related rows, and some Enriques/K3 workflows, but it does not by itself define a complete surface category. Surface specs must name the mathematical refinement and codomain first, then select Sage or another backend.

## Backend Survey

Source evidence:

- OSCAR adjunction-process documentation, https://docs.oscar-system.org/stable/AlgebraicGeometry/Surfaces/AdjunctionProcess/, provides smooth projective surface tooling over `C`.
- OSCAR rational-surface parametrization documentation, https://docs.oscar-system.org/v1/AlgebraicGeometry/Surfaces/ParametrizationSurfaces/, supports rational parametrization for smooth rational surfaces under embedding/adjunction hypotheses.
- Macaulay2 Divisor package documentation, https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Divisor/html/_canonical__Divisor.html, includes canonical-divisor computation for rings with grading caveats.
- Macaulay2 Varieties package documentation, https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/, exposes smoothness, singular loci, Hilbert polynomial, canonical bundle, tangent/cotangent sheaves, and cohomology surfaces.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` routes divisor intersection, sheaf cohomology, Picard-lattice bridge, double-cover, K3-cover, Enriques quotient, and Coble-lattice methods to Macaulay2, Sage, OSCAR, and exact lattice backends.

Inference:

Surface backends are available but fragmented by presentation and hypothesis: OSCAR for smooth projective/rational surfaces, Macaulay2 for divisor/sheaf/canonical surfaces, Sage for selected K3/cover routes, and lattice software for Picard-lattice outputs. Adapter cards must route by exact mathematical object, not by a generic `Surface` catch-all.

## Local Category-Spec Dependencies

Source evidence:

- `TASK-INTEGRATE-SCHEMES-CATEGORY`, `TASK-INTEGRATE-VARIETIES-CATEGORY`, and `TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY` supply the scheme/variety/complex base layers.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` delegates unresolved geometry rows to this geometry source-admission subtree.
- `theory/references/index.md` lists Coble, K3, Enriques, Nikulin, Huybrechts, Sterk, Scattone, Alexeev, and Pieroni sources for downstream surface and lattice claims.
- `theory/foundations/coble-task-background.md` and `theory/moduli/moduli-dimension-claim.md` record Coble/K3 period-domain and blowup/Picard-lattice facts as source material, not generic surface API.

Inference:

The complex-surface card should stabilize the dimension-two owner and protect downstream Coble/K3/Picard-lattice work from leaking into generic surface specs. It does not replace K3, Coble, divisor, sheaf, Picard, or lattice cards.

## Method Ownership Guidance

Admit these as surface-level or surface-refinement surfaces when downstream specs are written:

- `dimension() == 2`: defining refinement from complex varieties to complex algebraic surfaces.
- `canonical_class()` / `canonical_bundle()`, `kodaira_dimension()`, `hodge_number(p, q)`, `arithmetic_genus()`, `geometric_genus()`, and `holomorphic_euler_characteristic()`: inherited from broad smooth/proper/projective variety or scheme refinements with exact hypotheses recorded. Surface specs may add dimension-two formulas, classification terminology, and backend routes.
- `picard_group()`: inherited from variety/scheme Picard surfaces; codomain is a Picard group object.
- `picard_lattice()` or `intersection_matrix()` on algebraic classes: owned only after a surface has an admitted intersection pairing and lattice realization, e.g. smooth projective K3/Coble/Enriques refinements.
- `blowup(center)`: scheme-level construction with a surface-preserving refinement when the center and result satisfy surface hypotheses.
- `exceptional_divisor()`: owned by blowup objects, not all surfaces.
- `birational_involution()`: owned by birational self-map/automorphism refinements of surfaces.
- `k3_cover()`, `cover_surface()`, and Coble/K3 double-cover surfaces: owned by Enriques/Coble/double-cover refinements, not generic surfaces.

## Downstream Work Unblocked Or Routed

This card gives source-grounded input to these sibling cards and downstream specs:

- Coble/K3 geometry specs: use named surface refinements plus Picard/lattice bridge surfaces, not generic complex-surface methods.
- Historical Coble/K3 recovery specs: consume this as the surface boundary but must still cite their own Coble/K3 sources before implementation.
- `TASK-INTEGRATE-FAMILIES-OF-VARIETIES-CATEGORY`: surface families must be morphisms with dimension-two fibers under hypotheses.
- `TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES`: surface-family monodromy/Picard-Fuchs work needs family and smooth/proper surface hypotheses.
- Divisor/sheaf/Picard-lattice backend rows remain under category-method inventory and future category specs.

## Follow-Up Routing

No new card is needed from this surface pass. Existing cards own the remaining specialization work:

- K3/Coble/Enriques recovery and lattice bridge specs already exist under historical and Coble feature buckets.
- Divisor, sheaf, Picard, and lattice bridge details remain in category-method inventory and downstream source-admission/spec cards.
- Families and monodromy work remains in the families and curve-complement backend plans.

## Acceptance Evidence

- Mathematical convention recorded by specializing complex varieties to dimension two.
- Corrected invariant ownership so genus variants, Hodge numbers, Kodaira dimension, Euler characteristics, and canonical data are inherited from broad scheme/variety refinements, with surfaces owning only dimension-two specializations and bridge structures.
- Sage surfaces surveyed through algebraic-scheme/presented-subscheme and local backend-inventory evidence.
- Backend surfaces surveyed for OSCAR surface tooling and Macaulay2 divisor/variety tooling.
- Local K3/Coble/Picard-lattice source dependencies listed explicitly.
- Follow-up routing records that no new card is needed because existing Coble/K3, divisor, sheaf, Picard, lattice, family, and backend cards own specialization.

## Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** None
**Outcome:** complete

#### Evidence

**Gate 1 — Definition Grounding:** Stacks/sibling card citations for dimension-two complex variety definition. Sage and OSCAR/Macaulay2 backend URLs.
**Gate 2 — Acceptance Criteria:** Mathematical convention recorded, invariant ownership corrected, Sage/backend surfaces surveyed, K3/Coble/Picard-lattice dependencies listed.
**Gate 3-6:** No spec-weakening or gradient issues; research documentation only. Standard definitions followed. Evidence/inference separation maintained.

---

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for complex algebraic surfaces, recording the dimension-two complex-variety convention and routing K3, Coble, Enriques, divisor, Picard, lattice, and period surfaces to stricter refinements.
- 2026-05-06: Corrected over-narrow invariant ownership: Hodge, Kodaira, genus, Euler-characteristic, and canonical surfaces are broad scheme/variety-refinement invariants before surface specialization.
- 2026-05-06: Added explicit DAG prerequisite edges for source-admission substrate dependencies. These are sequencing edges, not blockers; the card should wait until the prerequisite source cards are accepted.
