---
id: SPEC-HISTORICAL-DISCRIMINANT-DESCENT-MORPHISM-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE]]'
title: Recover kernels, images, cokernels, and discriminant descent through morphisms
status: complete
priority: high
requirement: Historical morphism operations must be recovered through category-correct
  Hom objects, with cokernels returning the mathematically correct formed-module quotient.
acceptanceCriteria:
- Morphisms are elements of Hom spaces and form preservation is Hom containment.
- Kernel, image, cokernel, lift, injective, surjective, bijective, identity, and primitive
  predicates have mathematically typed return objects.
- The discriminant form arises from the cokernel of the dual inclusion with descended
  coefficient data.
- Lattice promotion from a morphism result happens only when the returned object is
  free, integral, and nondegenerate under explicit hypotheses.
complexity: 80
tags:
- FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY
---
# Recover kernels, images, cokernels, and discriminant descent through morphisms

## Source Provenance

- `src.bak/lattices/morphisms/lattice.py`: image, kernel, cokernel, lift, primitive,
  injective, and promotion hooks.
- `src.bak/lattices/morphisms/discriminant.py`: discriminant-group morphism kernel,
  image, cokernel, injective, surjective, bijective, isomorphism, and identity
  predicates.
- `src.bak/lattices/morphisms/homspaces.py`: Hom-space construction stubs and evidence
  that the old layer was incomplete.
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`: current Hom,
  cokernel, and discriminant descent rules.
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`:
  morphism-owned verbs, Hom-space construction, and rejection of morphism `perp` or
  containment shortcuts.
- `projects/github.com__dzackgarza__lattice-research/context/bilinear-form-category-semantics`: coefficient-module
  cokernel semantics and the discriminant descent diagram using `L -> L^#`.

## Contract

Recovered morphism work must start from Hom objects. A matrix or generator-image table
constructs a candidate morphism only through the parent Hom space, where domain,
codomain, generator conventions, and form-preservation checks are centralized.

Kernel, image, and cokernel return actual category objects with the appropriate
descended form data. For discriminant descent, the quotient is not merely an
underlying-module quotient: the form and coefficient codomain must descend through the
specified morphism under the hypotheses recorded in the with-form category spec.

Primitive embedding and quotient tests are properties of the morphism and its cokernel.
They must not be restated as standalone helper assertions over raw matrices.

## Recovered Hom-Space Surface

Every formed-module morphism is an element of a declared Hom parent:

- `M.Hom(N)` is the parent of morphisms from `M` to `N`.
- `Hom.from_images(images)` constructs the morphism determined by the fixed domain
  generators and the listed codomain elements.
- `Hom.from_dict({g_i: h_i})` constructs a morphism from named generator images.
- `Hom.from_callable(f)` is admitted only as a thin constructor that evaluates `f` on
  the domain generators and delegates to `from_dict`.
- `Hom.from_matrix(A)` constructs a candidate morphism from a matrix relative to the
  selected presentations, then validates it through Hom containment.

The Hom parent owns domain/codomain checks, selected-generator conventions, module
linearity, and form preservation. Matrix equations such as `A^T Q_N A = Q_M` are
localized implementation checks inside Hom containment or Aut containment; they are not
public substitutes for the morphism object.

The old `BilinearModuleHomSpace.__contains__` is recoverable only as the containment
site. It must not be copied as a broad `isinstance`/duck-type pattern. Candidate inputs
must be routed through explicit constructors and real category membership.

## Recovered Morphism Element Surface

A formed-module morphism element owns:

- `domain()` and `codomain()`;
- `__call__(x)` for `x` in the domain, returning a codomain element;
- `images()` as the tuple of images of the domain generators;
- `to_matrix()` as presentation readback after the morphism exists;
- additive operations in the Hom object when the Hom parent has additive module
  structure;
- `inverse()` only when the morphism is an isomorphism, returning an element of the
  reverse Hom parent.

`is_isometry()` is not a freestanding matrix predicate. In a formed Hom parent whose
containment already enforces form preservation, an isomorphism is an isometry. In an
Aut parent, membership is the isometry check.

## Recovered Kernel, Image, And Cokernel Surface

The returned objects must be actual category objects:

- `f.kernel()` is a subobject of `domain(f)` with the restricted form.
- `f.image()` is a subobject of `codomain(f)` with inclusion into the codomain and the
  restricted form.
- `f.cokernel()` is the quotient `codomain(f) / image(f)` with projection morphism,
  lift data where mathematically available, and descended form data when the descent
  hypotheses hold.
- `f.lift(y)` is a partial inverse along the projection/image data, not a raw Sage lift
  escape hatch.

The cokernel descent gate is:

- construct the underlying finitely generated PID-module cokernel;
- compute the coefficient-module quotient needed by the form;
- verify that cross-terms from the image vanish in the quotient codomain;
- construct the descended bilinear or quadratic form on the cokernel;
- promote the result into the richest correct category, such as `Free()`, `Torsion()`,
  `Integral()`, `Rational()`, `NonDegenerate()`, or `DiscriminantGroups()`.

Promotion is therefore a consequence of the constructed object and hypotheses. It must
not be implemented as "if the codomain is a `DualLattice` class, return a
`DiscriminantGroup`".

## Discriminant Descent Contract

For a lattice `L`, discriminant descent is the special case of the generic cokernel
machine applied to the metric inclusion:

```text
i: L -> L^#
A_L := coker(i)
```

The descended bilinear form has codomain `K/R`, and any descended quadratic refinement
has codomain `K/2R`. The resulting object must carry:

- the source lattice `L`;
- the metric dual `L^#`;
- the inclusion `i`;
- the projection `L^# -> A_L`;
- the quotient-valued form data.

The map `L^# -> Hom_R(L,R)` induced by `x |-> beta(x, -)` is separate transport data.
It is not what makes `L^#` a dual object, and it must not replace the metric-cokernel
definition of `A_L`.

## Recovered Predicate Surface

Morphism predicates are derived from the returned objects:

- `f.is_injective()` means `f.kernel()` is the zero object in the domain category.
- `f.is_surjective()` means `f.cokernel()` is the zero object in the codomain category.
- `f.is_bijective()` is injective and surjective.
- `f.is_isomorphism()` is categorical isomorphism, and in a formed Hom parent it is the
  relevant isometry condition when form preservation is already contained.
- `f.is_identity()` requires equal domain/codomain and equality on generators.
- `f.is_primitive()` for an inclusion means the cokernel is torsion-free; this belongs
  to the morphism/inclusion surface, not to a coordinate helper.

## Non-Preservation Boundaries

- Do not preserve `pass`-only homspace subclasses as if the surface were implemented.
- Do not define cokernel as an orthogonal complement.
- Do not promote a quotient to `DiscriminantGroup` by recognizing a particular class
  pair without constructing the actual dual inclusion and quotient map.
- Do not make morphisms own operations such as `perp` or containment; those belong to
  subobjects, Hom spaces, or formed-module parents as appropriate.

## Acceptance Criteria

- [x] Matrix and image constructors route through Hom-space parents.
- [x] Kernels, images, cokernels, and lifts return typed mathematical objects.
- [x] Discriminant descent is specified as a cokernel with descended form data.
- [x] Primitive embedding checks use the morphism/cokernel contract and produce
  reviewable evidence.

---

## 6-Gate Protocol Review Log

**Reviewer**: automated 6-gate spec review
**Date**: 2026-05-07
**Spec ID**: SPEC-HISTORICAL-DISCRIMINANT-DESCENT-MORPHISM-SURFACE
**Spec status before review**: needs-agent-review
**Review status**: PASS (all 6 gates)

---

### G1 — Source Grounding

**Verdict**: PASS

All six cited sources exist in the workspace and contain the described content:

| Source | Path | Status | Evidence |
|--------|------|--------|----------|
| Lattice morphisms | `src.bak/lattices/morphisms/lattice.py` (123 lines) | Confirmed | Contains `image()`, `kernel()`, `cokernel()`, `lift()`, `is_primitive()`, `is_injective()`, `is_surjective()`, `is_bijective()`, `is_isomorphism()`, `is_isometry()`, `inverse()`, `images()`, `to_matrix()`, `_promote_cokernel()` with exact `DualLattice` class-check pattern (lines 65-76) that the spec correctly flags as an anti-pattern. |
| Discriminant morphisms | `src.bak/lattices/morphisms/discriminant.py` (85 lines) | Confirmed | `DiscriminantGroupMorphism` with `kernel()`, `image()`, `cokernel()`, `is_injective()` (cardinality==1), `is_surjective()` (cardinality==1), `is_bijective()`, `is_isomorphism()`, identity predicates. HomSpace with `element_from_images()`. |
| Hom spaces | `src.bak/lattices/morphisms/homspaces.py` (108 lines) | Confirmed | `BilinearModuleHomSpace` with `element_from_images()`, `element_from_matrix()`, `element_from_dict()`, `__contains__()` enforcing `A^T Q_N A = Q_M`. Subclasses `RationalLatticeHomSpace`, `LatticeHomSpace`. |
| Category ABC spec | `.agents/skills/lattice-redesign/references/category-abc-spec.md` (938 lines) | Confirmed | Authoritative `ModulesWithForms(R)` contract, Hom/cokernel/descent rules, Sage category framework integration. |
| Lattice style guide | `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md` (1399 lines) | Confirmed | Morphism-owned verbs, Hom-space construction rules, rejection of morphism `perp`/containment shortcuts (matching spec's Non-Preservation Boundaries). |
| Bilinear semantics | `projects/github.com__dzackgarza__lattice-research/context/bilinear-form-category-semantics` (52 lines) | Confirmed | Coefficient-module cokernel semantics (lines 14-15), discriminant descent diagram `L -> L^# -> A_L` (line 15), explicit `R=ZZ, S_1=S_2=ZZ` construction (line 15), correct cokernel = `L^#/L = A_L`. |

No phantom or missing sources. Every claim in the Source Provenance section is verifiable.

---

### G2 — Sage Surface Completeness

**Verdict**: PASS

The spec defines a complete Sage-compatible surface with seven nested contracts:

1. **Hom-space surface** (lines 59-79): `M.Hom(N)` parent, `from_images`, `from_dict`, `from_callable`, `from_matrix`, containment with matrix equations localized as internal checks. Complete constructor surface for formed-module morphisms.

2. **Morphism element surface** (lines 81-96): `domain()`, `codomain()`, `__call__`, `images()`, `to_matrix()`, additive ops in Hom, `inverse()` for isomorphisms, `is_isometry()` via Hom/Aut containment. Matches Sage `Morphism` + `ElementMethods` conventions.

3. **Kernel/image/cokernel surface** (lines 98-118): Returns actual category objects (subobjects, quotients) with descended form data. Five-step cokernel descent gate: PID-module cokernel, coefficient-module quotient, cross-term vanishing, descended form, category promotion.

4. **Discriminant descent contract** (lines 124-145): `L -> L^# -> A_L = coker(i)` with source lattice, dual, inclusion, projection, and quotient-valued form data. Correctly distinguishes metric dual from Hom dual transport.

5. **Predicate surface** (lines 147-158): `is_injective` (kernel is zero), `is_surjective` (cokernel is zero), `is_bijective`, `is_isomorphism`, `is_identity`, `is_primitive` (cokernel torsion-free). All derived from returned objects, not matrix tests.

6. **Promotion rules** (lines 120-122): Promotion only when free, integral, nondegenerate under explicit hypotheses — not via class-name recognition.

7. **Non-preservation boundaries** (lines 160-167): Explicit rejection of four anti-patterns found in source code.

No surface gaps. Every mathematical operation a user would need for morphism work is specified with return-type contracts.

---

### G3 — Mathematical Correctness

**Verdict**: PASS (no errors found)

Spot-check of key mathematical claims:

- **Hom containment as form preservation**: `A^T Q_N A = Q_M` localized inside Hom containment (line 75). Correct: this is the matrix form of `phi^* beta_N = beta_M`. In category terms, membership in `Hom_WithForm(M,N)` is precisely the form-preservation condition.

- **Cokernel descent pipeline** (lines 111-118): Five-step sequence (PID cokernel, coefficient quotient, cross-term vanishing, descended form, category promotion) matches the general coefficient-module quotient semantics in `bilinear-form-category-semantics.md` lines 13-14. Mathematically sound.

- **Discriminant as cokernel** (lines 129-132): `A_L := coker(i: L -> L^#)`. Standard definition in lattice theory (Nikulin 1979, Miranda-Morrison 2009). The descended form codomain `K/R` for bilinear and `K/2R` for quadratic is correct.

- **Primitive = cokernel torsion-free** (line 157): Correct for inclusions of free modules over PIDs. The source code `lattice.py:82-83` uses `cokernel().is_torsionfree()` — this is the right mathematical property.

- **Promotion rules** (line 120-122): Free + integral + nondegenerate → promote to lattice. Correct: these are the three conditions for a formed module to be an integral lattice. The spec correctly rejects the `isinstance(codomain, DualLattice)` shortcut in source code `lattice.py:65-76`.

- **is_isometry vs is_isomorphism** (lines 94-96, 154-155): The spec correctly distinguishes: in a formed Hom parent where containment enforces form preservation, an isomorphism is already an isometry. In an Aut parent, membership IS the isometry check. This matches source code `lattice.py:94-98`.

- **Metric dual vs Hom dual** (lines 143-145): `L^# -> Hom_R(L,R)` via `x |-> beta(x, -)` is transport data, not the definition. The spec correctly insists `L^#` is defined by the metric, and `A_L` by the metric cokernel — not by the Hom dual.

No mathematical errors detected. Claims align with standard references (Nikulin, Miranda-Morrison) and with the semantics recorded in `bilinear-form-category-semantics.md`.

---

### G4 — Nonmathematical Rejection

**Verdict**: PASS

The spec is purely mathematical. It contains:
- Category-theoretic contracts (Hom objects, containment, subobjects, quotients)
- Module-theoretic operations (kernel, image, cokernel, lift)
- Form theory (descent, discriminant, isometry)
- Explicit boundaries against nonmathematical shortcuts

No UI/UX fluff, no business logic, no implementation-specific details beyond necessary surface contracts. The Non-Preservation Boundaries section (lines 160-167) actively rejects four implementation shortcuts. Clean.

---

### G5 — Ambiguity Routing

**Verdict**: PASS (no blocking ambiguities)

Terms are precise and standard: cokernel (module quotient with descended form), discriminant descent (L → L# → A_L), primitive (torsion-free cokernel), Hom containment (form-preservation membership).

The spec uses concrete anti-patterns to resolve potential ambiguity:
- "Do not define cokernel as an orthogonal complement" (line 163) — unambiguous rejection of the perp shortcut.
- "Do not promote a quotient to DiscriminantGroup by recognizing a particular class pair" (lines 164-165) — directly addresses the `isinstance(codomain, DualLattice)` anti-pattern in source code.
- Promotion conditions are explicit: "free, integral, and nondegenerate under explicit hypotheses" (line 121).

The dependency spec `SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE` exists and its acceptance criteria align (discriminant object records source lattice, dual inclusion, quotient map, descended form data). No circular or broken dependency chains.

---

### G6 — Obligation Preservation

**Verdict**: PASS

- **Feature-level obligations preserved**: The spec satisfies `FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY` requirements for morphism recovery through Hom objects, with cokernels returning correct formed-module quotients (requirement line 12-13).

- **Dependency obligations preserved**: Depends on `SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE` which specifies the discriminant group surface. This spec defines the morphism machinery (cokernel descent) that produces discriminant groups — it builds on, not duplicates, the dependency.

- **Acceptance criteria obligations**: All four acceptance criteria are checked [x], indicating implementation obligations tracked and completed. The criteria correctly reflect the spec's contracts.

- **Source code obligations**: The spec preserves the functional surface from three source files (lattice.py, discriminant.py, homspaces.py) while correctly rejecting four implementation anti-patterns (`pass`-only subclasses, cokernel-as-perp, instanceof promotion, morphism-owned perp/containment).

---

### Summary

| Gate | Description | Verdict | Notes |
|------|-------------|---------|-------|
| G1 | Source Grounding | PASS | All 6 sources exist and contain described content |
| G2 | Sage Surface Completeness | PASS | 7 nested contracts, complete surface |
| G3 | Mathematical Correctness | PASS | No errors; aligns with Nikulin/Miranda-Morrison |
| G4 | Nonmathematical Rejection | PASS | Purely mathematical content |
| G5 | Ambiguity Routing | PASS | Precise terms, concrete anti-patterns |
| G6 | Obligation Preservation | PASS | Feature/dependency/source obligations preserved |

**Recommendation**: Advance status from `needs-agent-review` to `reviewed`. The spec is mathematically sound, well-grounded in sources, and provides a complete Sage surface contract for morphism recovery.
