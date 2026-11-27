---
id: SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[SPEC-MAPPING-LATTICES]]'
- '[[PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT]]'
title: Spec discriminant-form isotropic orbit method surfaces
status: complete
priority: medium
requirement: 'The lattice spec lists nikulin_invariants() but the isotropic orbit
  analysis (Tasks 2.1-2.2, FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION) requires the full
  discriminant form and orbit computation in the finite discriminant group. Specify
  the missing method surfaces on DiscriminantGroup that support: (a) the full discriminant
  form q_T: A -> Q/2Z, (b) the orthogonal group O(A,q) and its action on A, (c) orbit
  enumeration of isotropic elements under O(A,q), (d) orbit representatives and their
  lifts to the lattice.'
acceptanceCriteria:
- Every method required by the orbit classification is placed at the correct category
  level (discriminant group, torsion quadratic module, or lattice).
- Sage sources TorsionQuadraticModule, QuadraticForm, and Oscar/Hecke discriminant-form
  APIs are surveyed as implementation evidence.
- The surface does not duplicate methods already specified in SPEC-MAPPING-FORMS or
  Phase 4 discriminant-group tasks.
- The orbit enumeration methods distinguish finite-group orbits (Burnside) from lattice-level
  orbits (spinor norm/Eichler).
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Spec: Discriminant-form isotropic orbit method surfaces

## Relationship to existing specs

Phase 4 (PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT) already specifies
discriminant-group methods: `b(x,y)`, `q(x)`, `invariants()`, `cardinality()`,
`isotropic_elements()`, `elements_of_norm(n)`, `is_isometric_to(other)`,
`isomorphic_as_groups(other)`, `is_p_elementary(p)`, `p_rank(p)`, `value_map()`.

These methods give the quadratic form q: A -> Q/2Z and the set of isotropic elements,
but they do NOT provide:

1. **The orthogonal group O(A, q)** — generators or the full matrix group of
   automorphisms of the finite quadratic form.
2. **Orbits of isotropic elements under O(A, q)** — orbit decomposition, orbit
   representatives, stabilizer sizes.
3. **The spinor norm kernel** — the connecting homomorphism O(T) -> O(A_T, q_T) and its
   image, needed for lifting orbits from the discriminant group to the lattice.

## Method surfaces to add

These methods should be specified on the `DiscriminantGroup` (or `TorsionQuadraticForm`)
object, which is a `ModulesWithForms(R).Quadratic().Torsion().NonDegenerate()` object:

### 1. Discriminant orthogonal group

```
D.orthogonal_group() -> MatrixGroup
    The finite group O(D, q_D) of automorphisms of the discriminant quadratic form.
    Backend: Sage QuadraticForm.automorphism_group() or Oscar/Hecke.
    Returns generators as a matrix group over Z (acting on the invariant-factor basis).
```

### 2. Isotropic orbit decomposition

```
D.isotropic_orbits() -> list[Orbit]
    Orbit decomposition of the set {x in D : q(x) = 0} under O(D, q).
    Each Orbit records a representative element, stabilizer subgroup, and size.
```

### 3. General norm-orbit decomposition

```
D.orbits_of_norm(n) -> list[Orbit]
    Orbit decomposition of {x in D : q(x) = n (mod 2Z)} under O(D, q).
    Specialized for n=0 by isotropic_orbits() when n=0.
```

### 4. Orbit lifting

```
D.lift_orbit_to_lattice(orbit_rep, lattice) -> IsometryClass
    Given an O(q_T)-orbit representative in A_T, produce the set of primitive
    isotropic vectors in T with that discriminant class, up to O*(T).
    Requires: Nikulin surjectivity (or backend), spinor norm computation.
```

## Implementation evidence needed

- Sage: `TorsionQuadraticModule.orthogonal_group()` (or
  `QuadraticForm.automorphism_group()`)
- Sage: `QuadraticForm.automorphism_group()` for computing O(q) on finite forms
- Oscar/Hecke: `orthogonal_group` on discriminant forms, orbit methods
- GAP: `SO`, `GO` on finite quadratic forms, `OrbitsDomain` for group actions

## Non-Goals

- Do not re-specify the discriminant group's bilinear/quadratic form evaluation (Phase 4).
- Do not specify lattice-level isometry backends (Phase 5).
- Do not implement orbit enumeration from first principles before surveying existing
  finite-group orbit methods in GAP/Sage/Oscar.

## 6-Gate Protocol Review Log

### Gate 1 — Scope & Purpose: PASS

The spec has a clearly defined scope: it bridges a gap between Phase 4 discriminant-group
primitives (bilinear/quadratic evaluation, invariants, isotropic element enumeration) and
the orbit-classification work required by Tasks 2.1–2.2 of FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION.
The four method surfaces — `orthogonal_group()`, `isotropic_orbits()`, `orbits_of_norm(n)`,
and `lift_orbit_to_lattice()` — are each motivated by a specific missing capability. No
scope creep: the Non-Goals section explicitly excludes re-specifying Phase 4 primitives,
lattice-level isometry backends (Phase 5), and first-principles orbit enumeration.

*Recommendation:* None. Gate is clean.

### Gate 2 — Dependency Integrity: PASS

Declared `dependsOn` edges are correct:
- `SPEC-MAPPING-LATTICES` — required for understanding how discriminant forms attach to lattices
  and how the invariant-factor basis is defined.
- `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT` — provides the underlying `b(x,y)`,
  `q(x)`, `isotropic_elements()`, `value_map()`, and group structure methods that this spec
  builds on top of.

Parenting under `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` is appropriate; this is a category-level
method surface spec, not an implementation task.

*Issue:* The spec references `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION` in the requirement but
does not declare it as a `dependsOn` or `relatedTo`. This is intentional (this spec *enables*
that feature, not the reverse), but it should be noted as a forward reference.

*Recommendation:* None required. The forward reference is informational only.

### Gate 3 — Implementation Evidence: CONDITIONAL PASS

The spec lists four backend targets: Sage `TorsionQuadraticModule.orthogonal_group()`,
Sage `QuadraticForm.automorphism_group()`, Oscar/Hecke `orthogonal_group` on discriminant forms,
and GAP `OrbitsDomain`. This is a reasonable survey baseline.

*Concerns:*
- Sage's `TorsionQuadraticModule` does not currently have a general `orthogonal_group()` method
  (as of Sage 10.x). The spec acknowledges this by listing `QuadraticForm.automorphism_group()`
  as a fallback, but the mapping between the torsion quadratic module basis and the quadratic
  form basis needs explicit handling.
- Oscar/Hecke discriminant-form orthogonal group support is nascent and may not cover
  non-p-elementary forms.
- The `lift_orbit_to_lattice()` method requires the Nikulin surjectivity result (kernel of
  O(L) → O(A_L, q_L)). This is a nontrivial mathematical prerequisite that the spec notes
  only in passing ("Requires: Nikulin surjectivity (or backend), spinor norm computation").

*Recommendation:* Before a corresponding task is marked `in-progress`, do a focused survey
spike to confirm at least one viable backend path for each of the four method surfaces.
Record results in the task body.

### Gate 4 — Non-Duplication: PASS

The spec's "Relationship to existing specs" section explicitly enumerates the Phase 4 methods
that already exist on `DiscriminantGroup` and clearly demarcates what is *not* provided.
Acceptance criterion 3 ("does not duplicate methods already specified") is satisfied by
construction. The four proposed method surfaces are genuinely additive.

*Recommendation:* None.

### Gate 5 — Acceptance Criteria: PASS (with clarification)

The four acceptance criteria are:
1. Methods placed at correct category level — *measurable by code review of the resulting
   Sage method surfaces.*
2. Backend sources surveyed as implementation evidence — *measurable by checking for
   documentation/survey notes in the implementing task.*
3. No duplication — *measurable by diff against Phase 4 and SPEC-MAPPING-FORMS.*
4. Finite-group vs. lattice-level orbit distinction — *measurable by verifying that
   `isotropic_orbits()` returns O(q_T)-orbits while `lift_orbit_to_lattice()` produces
   O*(T)-classes.*

*Clarification:* Criterion 1 says "placed at the correct category level" but does not define
what those levels are. The spec body implies the methods belong on `DiscriminantGroup`
(`ModulesWithForms(R).Quadratic().Torsion().NonDegenerate()`). This should be made explicit
in the body if it isn't already (the body does state this in the "Method surfaces to add"
preamble, so it is clear enough).

### Gate 6 — Card Integrity: PASS

The card follows the workspace template:
- YAML frontmatter with `id`, `trackerStatus`, `parents`, `dependsOn`, `title`, `status`,
  `priority`, `requirement`, `acceptanceCriteria`, `tags`. All present and well-formed.
- `id` matches filename stem.
- `trackerStatus.type: spec` is correct.
- `status: needs-human-input` is appropriate — the spec requires human review before
  implementation work begins.
- Body has clear sections: Relationship, Method surfaces, Implementation evidence, Non-Goals.
- Review log (this section) is now present.

*Minor note:* The `requirement` field is quite long (wraps multiple lines in YAML). This is
acceptable but may be less searchable. Consider a one-line summary with detail in the body.

### Summary

| Gate | Verdict             |
|------|---------------------|
| 1    | PASS                |
| 2    | PASS                |
| 3    | CONDITIONAL PASS    |
| 4    | PASS                |
| 5    | PASS                |
| 6    | PASS                |

**Overall: APPROVED with one pre-implementation action item.** Before a task deriving from
this spec moves to `in-progress`, conduct a focused backend-survey spike to confirm at least
one viable implementation path for each of the four method surfaces, with particular attention
to `orthogonal_group()` on torsion quadratic modules and the Nikulin-surjectivity
prerequisite for `lift_orbit_to_lattice()`.

*Reviewer: Hermes Agent (automated 6-gate review)*
*Date: 2026-05-07*
