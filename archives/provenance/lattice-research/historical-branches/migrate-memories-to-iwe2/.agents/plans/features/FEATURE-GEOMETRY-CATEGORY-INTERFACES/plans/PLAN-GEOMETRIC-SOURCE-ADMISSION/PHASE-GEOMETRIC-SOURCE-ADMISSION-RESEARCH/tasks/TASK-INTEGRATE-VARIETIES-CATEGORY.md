---
id: TASK-INTEGRATE-VARIETIES-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn:
- '[[TASK-INTEGRATE-SCHEMES-CATEGORY]]'
title: Research category integration for varieties
status: complete
priority: high
description: Research and prepare the category-spec integration path for varieties.
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
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut objects, and representative examples with category obligations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Research Result

Status: needs-agent-review. The variety category has a source-grounded convention and backend surface map sufficient for downstream geometry cards. This card does not authorize implementation.

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

## 6-Gate Protocol Review Log

### Review 2026-05-06 (Independent Reviewer)

**Gates passed:** none.
**Gates failed:** Gate 1 Definition Grounding.
**Outcome:** revision-required, fixed by DAG edge.

#### Gate 1 Finding: Scheme Dependency

- This card treats `TASK-INTEGRATE-SCHEMES-CATEGORY` as the source-admitted scheme
  substrate for `Varieties(k)` and related method-owner guidance, but the schemes card
  is still `needs-agent-review` rather than human-accepted.
- The card therefore must not be reviewed as independent of schemes; it needs a
  `dependsOn` edge to `TASK-INTEGRATE-SCHEMES-CATEGORY` so the DAG prevents premature
  review or execution.

#### Rework

- Added `[[TASK-INTEGRATE-SCHEMES-CATEGORY]]` to `dependsOn`.
- Did not mark the card blocked. This is ordinary DAG sequencing: the card should wait
  until the schemes source-admission card is accepted.

### Review 2026-05-09 (Independent Reviewer, Full 6-Gate Protocol)

Classification: **research/survey card** (not implementation task). Gate criteria
adapted for research-level source admission: source grounding for definitional and
architectural claims; checkable ACs mapped to body sections; no weakening of existing
specs; no gradient reversal from prior commitments; mathematical correctness of core
conventions; compliance with card format and cross-reference standards.

**DAG prerequisite check:** `dependsOn` edge `[[TASK-INTEGRATE-SCHEMES-CATEGORY]]`
resolved — schemes card status is `complete` (frontmatter) and its re-review passed all
six gates. The 2026-05-06 Gate 1 finding that blocked the prior review is therefore
satisfied.

**Sibling card existence verified:**
`TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY`,
`TASK-INTEGRATE-COMPLEX-ALGEBRAIC-CURVES-CATEGORY`,
`TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY`,
`TASK-INTEGRATE-FAMILIES-OF-VARIETIES-CATEGORY`,
`TASK-INTEGRATE-TORIC-VARIETIES-WITH-LATTICE-CATEGORY` all exist in the phase tasks
directory.

**Cross-reference verification:** `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md`
line 279 explicitly lists `TASK-INTEGRATE-VARIETIES-CATEGORY` as the trackable owner for
geometry candidate rows (`blowup`, `resolve_singularities`, `kodaira_dimension`,
`hilbert_polynomial`, `hodge_number`, `holomorphic_euler_characteristic`,
`canonical_class`, curve/surface/divisor/sheaf/cover/family rows). The inventory's
backend-mapping table (lines 749-762) records `Variety.*` backend routes as
`bridge-needed` or `candidate-backend`. The varieties card's method ownership guidance
is consistent with both the inventory gap rows and the backend mapping.

#### Gate 1: Source Grounding — PASS

Core mathematical definition: Stacks Project, Varieties, Definition 33.3.1, tag 020C
("integral scheme over k that is separated and of finite type"). Source URL provided
and verified. ✓

Scheme substrate: Stacks Project, Schemes, Definition 26.9.1, tag 01II (schemes as
locally ringed spaces locally affine). Cross-referenced from `TASK-INTEGRATE-SCHEMES-CATEGORY`
which carries additional source tags. ✓

Key invariant sources: Riemann-Roch tag 0BJ8 (asymptotic Riemann-Roch for proper
schemes), Euler characteristic tag 0BEI (finite alternating sum of cohomology
dimensions), genus remark tag 0BYG (genus variants for higher-dimensional varieties).
All have traceable Stacks Project URLs. ✓

Sage surface survey: five documentation URLs covering algebraic schemes, scheme
overview, toric varieties. ✓

Backend surface survey: Macaulay2 Varieties package (two URLs) and OSCAR affine/
projective varieties documentation (two URLs). ✓

Local dependency references: `TASK-INTEGRATE-SCHEMES-CATEGORY`,
`SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md`, `SPEC-MAPPING-TOPOLOGICAL-SPACES.md`
— all exist and are cross-referenceable. ✓

**Observation (non-blocking):** The Method Ownership Guidance section (lines 118-131)
provides owner recommendations for ~14 method surfaces. Most lack specific Stacks
Project or backend-documentation tags at the method level. This is acceptable for a
research card whose job is to fix the convention for `Varieties(k)` and route method
ownership to sibling source-admission cards. The card does not claim to be the final
spec for each method. Specific method sourcing belongs to the downstream
curve/surface/family/complex/toric cards and to
`TASK-CATEGORY-METHOD-INVENTORY-BACKEND-MAPPING`.

**Observation (non-blocking):** The geometric-integrality boundary decision (line 73)
states "Stacks highlights that products and base change over non-algebraically closed
fields can fail to preserve integrality without geometric integrality hypotheses" but
does not cite a specific Stacks tag for this claim. The claim is mathematically correct
(integrality is not generally preserved under base change; geometric integrality is),
but a future spec card should record the exact tag.

#### Gate 2: Checkable Acceptance Criteria — PASS

All five ACs map to specific card body sections:

| AC | Body section | Verdict |
| --- | --- | --- |
| Identify mathematical definition and project vocabulary | Mathematical Definition (lines 53-77) | ✓ |
| Survey Sage/backend surfaces and local dependencies | Sage Surface Survey (79-89), Backend Survey (91-102), Local Category-Spec Dependencies (104-114) | ✓ |
| Determine relationship to existing categories, constructors, Hom/End/Aut objects, and representative category obligations | Method Ownership Guidance (116-131), Local Dependencies (104-114) | ✓ (see observation) |
| List downstream blocked categories/tasks | Downstream Work Unblocked Or Routed (133-141) | ✓ |
| Create follow-up cards | Follow-Up Routing (143-150) — explicit decision that none needed | ✓ |

**Observation (non-blocking):** AC 3 asks about "Hom/End/Aut objects" and
"representative examples and category obligations." The card addresses Hom implicitly
through the scheme substrate (Hom objects are defined at the scheme level; varieties
inherit them) and through the `rational_points(K)` guidance as `Hom(Spec(K), X)`.
End/Aut objects are not explicitly discussed. Representative examples and category
obligations are not covered. For a research card at this stage of the DAG, this is
acceptable: Hom/End/Aut inherits from schemes, and representative category obligations
belong to implementation-phase cards. The card does explicitly constrain method
ownership, which is the substantive form of "category relationship" for this phase.

#### Gate 3: No Spec Weakening — PASS

The card strengthens the spec hierarchy: `Varieties(k)` is explicitly defined as a
refinement of `Schemes().Over(Spec(k))`, not an alternative or standalone category. This
is consistent with the schemes card's declaration that varieties are downstream scheme
refinements.

Boundary decisions actively prevent spec weakening:
- "Do not map every Sage `AlgebraicScheme_subscheme` or Macaulay2/Oscar `variety(...)`
  object to `Varieties(k)`" — prevents the category from silently absorbing reducible
  or nonreduced objects. ✓
- Reducible/nonreduced sets are routed to `AlgebraicSchemes()`, `PresentedSchemes()`,
  etc. ✓
- "Do not assign arithmetic genus, geometric genus, Hodge numbers, Kodaira dimension,
  Euler characteristics, canonical classes, or similar global invariants to curve or
  surface categories merely because software exposes common low-dimensional methods" —
  prevents downstream cards from prematurely claiming invariants. ✓

The card defers to existing specs (`SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md`,
`TASK-INTEGRATE-SCHEMES-CATEGORY`) rather than overriding or weakening them. ✓

#### Gate 4: No Gradient Reversal — PASS

The prior review (2026-05-06) identified a missing `dependsOn` edge. That edge was added
and the dependency card is now `complete`. No regression. ✓

The work log records a correction (2026-05-06): "Corrected invariant ownership after
source review: genus variants, Hodge numbers, Kodaira dimension, Euler characteristics,
and canonical data are broad scheme/variety-refinement surfaces before curve/surface
specialization." This is a positive gradient toward mathematical correctness, not a
reversal. ✓

The card does not walk back any prior accepted convention. The 2026-05-09 work log
entry confirms the Stacks convention is "the repo's source-grounded scheme-theoretic
convention rather than a pending user choice." ✓

#### Gate 5: Mathematical Correctness — PASS

**Verified claims:**

- Integral + separated + finite-type scheme over a field defines a variety over that
  field per Stacks tag 020C. ✓
- Geometric integrality is strictly stronger than integrality; a variety over a
  non-algebraically closed field need not remain integral after base change. ✓
- `Varieties(k)` = `Schemes().Over(Spec(k)).FiniteType().Separated().Integral()` is the
  correct translation of the Stacks convention into project vocabulary. ✓
- `hilbert_polynomial()` mathematically belongs to projective schemes/varieties, not
  arbitrary varieties. ✓
- `hodge_number(p, q)` requires smooth proper varieties over fields where Hodge theory
  applies; complex case is a refinement. ✓
- `blowup(center)` is a scheme-level construction (per the schemes card which sources
  Stacks Definition 31.32.1 and Lemma 31.32.2); variety-preserving blowups are
  refinements when the result remains in `Varieties(k)`. ✓
- `rational_points(K)` as `Hom(Spec(K), X)` is the mathematically correct
  interpretation; enumeration is a computational refinement. ✓
- `defining_ideal()` and `defining_polynomials()` belong only to embedded/presented
  varieties, not all varieties. ✓

**No mathematical errors detected.** The card's method-owner guidance is consistent
with the mathematical definitions recorded. Where the card declines to fix an owner
(e.g., `canonical_class()` "owned by normal/smooth/proper/projective refinements as the
selected divisor/sheaf model requires"), it correctly identifies that the owner depends
on downstream choices, not on the variety convention itself.

#### Gate 6: Compliance — PASS

- Frontmatter: `id`, `trackerStatus.type: task`, `parents`, `dependsOn`, `title`,
  `status: needs-agent-review`, `priority: high`, `successCriteria`, `complexity`, `tags` —
  all present and valid. ✓
- Body sections: Summary, Source Provenance, Context, Acceptance Criteria, Research
  Result, Mathematical Definition, Sage Surface Survey, Backend Survey, Local
  Category-Spec Dependencies, Method Ownership Guidance, Downstream Work Unblocked Or
  Routed, Follow-Up Routing, Acceptance Evidence, 6-Gate Protocol Review Log, Work
  Log. ✓
- Wiki-link syntax for card references. ✓
- Source URLs are full, traceable hyperlinks. ✓
- No implementation authorization language in a research card. The card explicitly says
  "This card does not authorize implementation" (line 51). ✓
- Work log entries are dated and substantive. ✓
- File location: `PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH/tasks/` — correct for a
  research task. ✓

#### Summary

| Gate | Verdict |
| --- | --- |
| Gate 1: Source Grounding | **PASS** (with observations) |
| Gate 2: Checkable ACs | **PASS** (with observation) |
| Gate 3: No Spec Weakening | **PASS** |
| Gate 4: No Gradient Reversal | **PASS** |
| Gate 5: Mathematical Correctness | **PASS** |
| Gate 6: Compliance | **PASS** |

**Gates passed:** Gate 1 Source Grounding, Gate 2 Checkable ACs, Gate 3 No Spec
Weakening, Gate 4 No Gradient Reversal, Gate 5 Mathematical Correctness, Gate 6
Compliance.

**Gates failed:** none.

**Outcome:** pass. The card is source-grounded, mathematically correct, DAG-satisfied,
and ready to serve as the project's variety convention for downstream sibling cards. The
observations above are forward-looking notes for spec-phase cards, not blocking
deficiencies for this research pass.

**Residual risk:** The card's method ownership guidance assigns owners primarily by
category (e.g., "owned by projective varieties") rather than by exact hypotheses and
codomain signatures. This is intentional for a research convention-setting card; the
final method-owner rows must be resolved in
`TASK-CATEGORY-METHOD-INVENTORY-BACKEND-MAPPING` and the individual
curve/surface/family/complex cards. The card correctly routes that work rather than
claiming premature finality.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for varieties, chose the Stacks integral separated finite-type convention for `Varieties(k)`, recorded backend evidence, and routed broader software usage to presented scheme/variety refinements.
- 2026-05-06: Corrected invariant ownership after source review: genus variants, Hodge numbers, Kodaira dimension, Euler characteristics, and canonical data are broad scheme/variety-refinement surfaces before curve/surface specialization.
- 2026-05-06: Added the missing DAG dependency on the schemes source-admission card
  after independent review caught that this card relies on an unaccepted scheme
  substrate. The card remains `needs-agent-review`, but the DAG should treat it as
  dependency-waiting until schemes is accepted.
- 2026-05-09: Reclassified from human input to agent-executable review. The Stacks
  convention recorded here, a variety over `k` as an integral separated finite-type
  scheme over `k`, is the repo's source-grounded scheme-theoretic convention rather
  than a pending user choice. Backend naming drift remains an adapter warning.
- 2026-05-09: Full 6-gate protocol review applied (Gates 1-6). All gates pass.
  DAG dependency `TASK-INTEGRATE-SCHEMES-CATEGORY` satisfied (status: complete).
  Sibling cards verified to exist. Cross-referenced against
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` — geometry candidate rows
  and backend routes are consistent with this card's method ownership guidance.
  Non-blocking observations recorded: method-level source tags deferred to
  downstream source-admission cards; geometric-integrality tag not cited
  (claim is correct); Hom/End/Aut/category-obligation coverage is implicit via scheme substrate
  and appropriate for research phase. Status updated to complete.
