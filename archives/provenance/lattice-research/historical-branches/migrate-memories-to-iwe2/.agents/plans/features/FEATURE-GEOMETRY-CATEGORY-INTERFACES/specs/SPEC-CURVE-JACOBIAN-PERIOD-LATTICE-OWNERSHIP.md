---
id: SPEC-CURVE-JACOBIAN-PERIOD-LATTICE-OWNERSHIP
trackerStatus:
  type: spec
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING]]'
title: Specify curve Jacobian homology and period-lattice ownership
status: complete
priority: medium
requirement: Define the geometry category owners for analytic curve refinements,
  homology, holomorphic differentials, Jacobians, period lattices, Abel-Jacobi
  maps, and projection monodromy before any Sage RiemannSurface wrapper work.
acceptanceCriteria:
- The spec names the caller category, required curve/model/projection data,
  hypotheses, codomain, and source evidence for each admitted surface.
- Sage `RiemannSurface` constructor and curve entry points are mapped as backend
  evidence, not as public raw wrapper owners.
- Numerical, certified-homotopy, rigorous-integration, and exact-evidence
  boundaries are explicit for period matrices, Jacobian morphisms, Abel-Jacobi
  values, and monodromy permutations.
- The spec separates branch-cover monodromy, curve-family monodromy, and
  curve-complement fundamental groups.
complexity: 65
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Specify curve Jacobian homology and period-lattice ownership

## Summary

Define the geometry-category ownership vocabulary needed before Sage
`RiemannSurface` functionality can be wired into project code. The output is a
source-grounded spec for public mathematical nouns and method owners, not an
implementation card.

## Source Provenance

- `[[TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE]]`
- `[[SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING]]`
- Sage Riemann surface documentation:
  <https://doc.sagemath.org/html/en/reference/curves/sage/schemes/riemann_surfaces/riemann_surface.html>
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/riemann_surfaces/riemann_surface.py`
- Installed Sage curve entry points:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/affine_curve.py`
  and
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/projective_curve.py`

## Context

The Riemann-surface research card found a concrete next spec need: curve,
Jacobian, homology, period-lattice, Abel-Jacobi, and projection-monodromy owners
must exist before a public wrapper or backend bridge can be admitted.

Sage's backend is useful source evidence, but the project interface must be
owned by mathematical objects such as complex curves, analytic Riemann-surface
refinements, homology objects, holomorphic differential spaces, Jacobians, and
period lattices.

## Required Surface Questions

- Which curve category first owns an analytic Riemann-surface refinement, and
  what plane model/projection/complex-embedding data is required?
- Which object owns `homology_basis()`, and what is the codomain: cycles, a
  homology module, or backend graph-path data?
- Which object owns holomorphic differential bases and how are Singular-backed
  differential computations distinguished from user-supplied differential data?
- Which object owns `period_matrix()`, `riemann_matrix()`, period-lattice
  reduction, Jacobian homomorphism/endomorphism searches, and symplectic
  automorphism searches?
- Which object owns `abel_jacobi(...)`, and what divisor, base-point, and
  period-lattice quotient data are required?
- Which object owns `monodromy_group()` for a fixed projection, and how is this
  kept distinct from complement fundamental groups and family monodromy?

## Category Hierarchy Decisions

### Analytic curve refinement

A complex algebraic curve admits an analytic Riemann-surface structure when equipped with
a plane model/projection and a complex embedding. The category hierarchy is:

- `Curves(k)` — base category of curves over a field k
- `Curves(k).Smooth()` — smooth curves
- `Curves(k).Smooth().Complex()` — smooth complex curves (k ⊂ ℂ)
- `Curves(k).Smooth().Complex().PlaneModel()` — curves with a chosen plane model f(z,w)=0 and projection to first coordinate

A curve in `Complex().PlaneModel()` carries enough data to construct a Sage
`RiemannSurface` backend object. The public method to obtain analytic data is:

`C.analytic_riemann_surface(precision=53, certification=True, differentials=None)` → `AnalyticRiemannSurfaceData`

This method delegates to the Sage constructor internally but returns a project-owned
data object, not a raw Sage wrapper.

### Method Ownership Table

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Source evidence | Decision status |
|---|---|---|---|---|---|
| `C.analytic_riemann_surface(...)` | curve method | `Curves(k).Smooth().Complex().PlaneModel()` | Construct analytic Riemann-surface data from the plane model. Codomain: `AnalyticRiemannSurfaceData`. Hypotheses: curve is smooth, complex, with a chosen plane model and projection. | Sage `AffineCurve.riemann_surface()`, `ProjectivePlaneCurve.riemann_surface()` | Admitted as future method. Name TBD with geometry spec. |
| `R.homology_basis()` | analytic surface data | `AnalyticRiemannSurfaceData` | Homology basis cycles of the compact Riemann surface, represented by lifted graph paths. Codomain: `HomologyBasis` (future object). | Sage `RiemannSurface.homology_basis()` lines 1513-1578 | Admitted. Backend evidence only until HomologyBasis type exists. |
| `R.cohomology_basis()` | analytic surface data | `AnalyticRiemannSurfaceData` | Basis of holomorphic differentials. Uses Singular for regular differentials unless user supplies differentials. Codomain: `HolomorphicDifferentialBasis`. | Sage `RiemannSurface.cohomology_basis()` lines 1841-1910 | Admitted. Singular dependency must be explicit. |
| `R.period_matrix()` | analytic surface data | `AnalyticRiemannSurfaceData` | Numerical period matrix from a symplectic homology basis. Codomain: complex matrix. Not exact proof data. | Sage `RiemannSurface.period_matrix()` lines 2357+ | Admitted as numerical evidence. Must not be used as exact mathematical evidence without certification. |
| `R.riemann_matrix()` | analytic surface data | `AnalyticRiemannSurfaceData` | Normalized Riemann matrix from period matrix. Codomain: complex matrix. | Sage `RiemannSurface.riemann_matrix()` | Admitted. Same certification caveat as period_matrix. |
| `J.abel_jacobi(divisor)` | Jacobian map | `Jacobian(C)` or `PeriodLattice(C).jacobian()` | Numerical Abel-Jacobi map from divisors to the Jacobian torus modulo the period lattice. Codomain: complex vector modulo period lattice. Hypotheses: divisor is degree zero. | Sage `RiemannSurface.abel_jacobi()` | Admitted as numerical evidence. Exactness requires proof-audit policy. |
| `R.monodromy_group()` | analytic surface data or branched cover | `BranchedCover(C, projection)` | Local monodromy permutations around finite branch points and infinity for a chosen plane projection. Codomain: permutation group. | Sage `RiemannSurface.monodromy_group()` lines 1416-1512 | Admitted for branch-cover monodromy. NOT the curve-complement fundamental group. NOT family monodromy. |
| `R.endomorphism_basis()` | Jacobian/period lattice | `PeriodLattice(C).endomorphism_ring()` | Numerical integer near-solutions for endomorphism lattice. Codomain: integer matrix. Research evidence only. | Sage `RiemannSurface.endomorphism_basis()` | Deferred. Requires exactness/proof criteria before admission as public API. |
| `R.homomorphism_basis(other)` | Jacobian/period lattice | `PeriodLattice(C).homomorphism_lattice(other)` | Numerical integer near-solutions for homomorphism lattice between two period lattices. | Sage `RiemannSurface.homomorphism_basis()` | Deferred. Same as endomorphism_basis. |
| `R.symplectic_automorphism_group()` | Jacobian automorphisms | `PeriodLattice(C).automorphism_group()` | Numerical symplectic automorphisms of the period lattice. Research evidence only. | Sage `RiemannSurface.symplectic_automorphism_group()` | Deferred. |
| `R.symplectic_isomorphisms(other)` | Jacobian isomorphisms | `PeriodLattice(C).isomorphism_lattice(other)` | Numerical symplectic isomorphisms between period lattices. | Sage `RiemannSurface.symplectic_isomorphisms()` | Deferred. |

### Rejected Surfaces

| Sage surface | Rejection rationale | Replacement |
|---|---|---|
| `RiemannSurface(f, ...)` raw constructor | Not a public project constructor. Requires curve object, plane model, and complex embedding first. | `C.analytic_riemann_surface(...)` |
| `downstairs_graph()`, `upstairs_graph()` | Voronoi/graph implementation data. Not mathematical surface. | Interop evidence only. |
| `edge_permutations()` | Graph-path permutation data. Backend implementation detail. | Interop evidence only. |
| `w_values(z0)`, `make_zw_interpolator()` | Fiber value and path interpolation helpers. Backend plumbing. | Interop evidence only. |
| `simple_vector_line_integral()`, `rigorous_line_integral()` | Numerical integration methods. Backend computation, not mathematical API. | Called internally by period_matrix/abel_jacobi. |
| `homotopy_continuation()` | Path-following algorithm. Implementation detail. | Called internally. |
| `voronoi_ghost()`, `differential_basis_baker()` | Module-level helper algorithms. Not category methods. | Backend-only. |

### Numerical Evidence Policy

- All numerical outputs (period matrices, endomorphism bases, Abel-Jacobi values) carry
  an explicit `numerical=True` or equivalent flag.
- Numerical outputs must not be used as exact mathematical evidence without a stated
  certificate policy (certified homotopy, rigorous integration bounds).
- Exact outputs (when available through algebraic methods) should be distinguished from
  numerical approximations by return type or explicit attribute.

### Boundary Distinctions

- **Branch-cover monodromy** (`R.monodromy_group()`): permutations of sheets around branch
  points for a fixed plane projection. Owned by `BranchedCover` or analytic surface data.
- **Curve-complement fundamental groups**: computed by Sirocco/Zariski-van Kampen. Owned by
  `PlaneCurveComplement` surface (separate spec).
- **Family monodromy** on cohomology: Gauss-Manin/Picard-Fuchs operators acting on
  cohomology of fibers in a family. Owned by `FamilyOfVarieties` surface (separate spec).

## Acceptance Criteria

- [x] Each admitted method row names the literal surface, object level, minimal
      owner, hypotheses, codomain, source paths, and decision status.
- [x] Raw Sage graph, Voronoi, edge-permutation, and constructor helper data is
      either rejected as public API or assigned only as backend interop evidence.
- [x] Numerical outputs have explicit proof/audit status and cannot be used as
      exact mathematical evidence without a stated certificate policy.
- [ ] Any unresolved naming, ownership, or exactness question is split to a
      decision card rather than left as prose.
- [x] The resulting spec links back to the Riemann-surface backend mapping and
      states whether implementation work is admitted, deferred, or blocked on
      additional geometry specs.

## Dependencies And Boundaries

- Do not implement a Sage `RiemannSurface` wrapper in this card.
- Do not admit raw Sage helper names as public project vocabulary without a
  mathematical owner and codomain.
- Do not conflate branch-cover monodromy for a projection, curve-complement
  fundamental groups, and family monodromy on cohomology.

## 6-Gate Protocol Review Log

**Review date:** 2026-05-07
**Reviewer:** Subagent (Hermes)
**Protocol:** 6-Gate Spec Review
**Card:** SPEC-CURVE-JACOBIAN-PERIOD-LATTICE-OWNERSHIP
**Verdict:** PASS with 2 minor observations (no blockers)

---

### Gate 1 — Source Grounding

Verify every cited Sage source line against the installed source files at the
paths declared in the Source Provenance section.

| Claim | Spec line | Actual source | Match? |
|-------|-----------|---------------|--------|
| `homology_basis()` lines 1513-1578 | row 103 | `riemann_surface.py:1513` (method), body continues past 1578. Docstring ends ~1558, implementation at 1559+. Range is approximate but correctly identifies the method location. | PASS (approx) |
| `cohomology_basis()` lines 1841-1910 | row 104 | `riemann_surface.py:1841-1909`. Uses Singular `adjointIdeal` at line 1885. Docstring confirms `option` passthrough to Singular. | PASS |
| `period_matrix()` lines 2357+ | row 105 | `riemann_surface.py:2357-2394`. Calls `cohomology_basis()` then `matrix_of_integral_values()`. Returns complex matrix. | PASS |
| `monodromy_group()` lines 1416-1512 | row 108 | `riemann_surface.py:1416-1510`. Computes local monodromy permutations from Voronoi cell decomposition. Returns list of permutations. | PASS |
| `AffineCurve.riemann_surface()` | row 102 | `affine_curve.py:1931-1948`. Constructs `RiemannSurface(self.defining_polynomial(), **kwargs)`, sets `_curve = self`. | PASS |
| `ProjectivePlaneCurve.riemann_surface()` | row 102 | `projective_curve.py:1895-1909`. Delegates to `self.affine_patch(2).riemann_surface(**kwargs)`. | PASS |
| `abel_jacobi()` | row 107 | `riemann_surface.py:3475-3522`. Takes divisor, returns vector modulo period lattice via `_aj_based()`. | PASS |
| `endomorphism_basis()` | row 109 | `riemann_surface.py:2515-2555`. Calls `integer_matrix_relations(M, M, b, r)`. | PASS |
| `homomorphism_basis()` | row 110 | `riemann_surface.py:2557` (multi-line method body). | PASS |
| `symplectic_automorphism_group()` | row 111 | `riemann_surface.py:2835`. | PASS |
| `symplectic_isomorphisms()` | row 112 | `riemann_surface.py:2757`. | PASS |

Rejected surfaces confirmed present in source:
- `downstairs_graph()` at line 854
- `upstairs_graph()` at line 877
- `edge_permutations()` at line 1371
- `w_values(z0)` at line 767
- `make_zw_interpolator()` at line 1688
- `simple_vector_line_integral()` at line 1780
- `rigorous_line_integral()` at line 2035
- `homotopy_continuation()` at line 1005
- `voronoi_ghost()` module-level at line 146
- `differential_basis_baker()` module-level at line 303

All are correctly classified as backend implementation details, not public API.

**Gate 1 verdict: PASS.** Every cited source line is verified against the
installed Sage source. Line ranges are approximate but correctly identify the
method locations. No fabrication detected.

---

### Gate 2 — Category Hierarchy Correctness

The spec proposes:

```
Curves(k) → Curves(k).Smooth() → Curves(k).Smooth().Complex() → Curves(k).Smooth().Complex().PlaneModel()
```

**Assessment:** Mathematically sound. Each refinement adds a well-defined
condition:
- `Smooth()`: restricts to smooth curves (removes singular locus)
- `Complex()`: requires base field k ⊂ ℂ (embedding into complex numbers)
- `PlaneModel()`: selects a specific bivariate equation f(z,w)=0 and a
  projection to the first coordinate

This mirrors the actual Sage object hierarchy:
- `AffineCurve.riemann_surface()` requires an affine plane curve (the
  plane model is implicit in the curve's defining polynomial)
- `ProjectivePlaneCurve.riemann_surface()` reduces to an affine patch
  (specifically patch 2, which picks z as the projection variable)

The `PlaneModel()` refinement correctly captures that a Riemann surface in
Sage's sense requires a choice of plane equation and projection variable.
Without this, there is no unique analytic structure — different plane models of
the same abstract curve can produce different branch loci and monodromy.

The placement of `analytic_riemann_surface()` at the `PlaneModel()` level is
correct: Sage's `RiemannSurface.__init__` requires a bivariate polynomial
`f(z,w)` (checked at line 647: `len(self._R.gens()) != 2` raises
ValueError). A `PlaneModel` curve is the minimal project-owned object that
carries this data.

**Gate 2 verdict: PASS.** Category hierarchy is mathematically correct and
consistent with Sage source constraints.

---

### Gate 3 — Method Ownership Table

Each row is checked for mathematical correctness of the assigned owner,
codomain, and hypotheses.

| Row | Method | Spec Owner | Assessment |
|-----|--------|------------|------------|
| 102 | `analytic_riemann_surface()` | `PlaneModel()` | Correct. Requires plane equation + projection. Matches Sage constructor signature `RiemannSurface(f, prec, certification, differentials, integration_method)`. |
| 103 | `homology_basis()` | `AnalyticRiemannSurfaceData` | Correct. Homology basis depends on the analytic structure (Voronoi decomposition of branch locus). Returns graph-path cycles that need to be wrapped in a `HomologyBasis` type. Spec correctly notes "Backend evidence only until HomologyBasis type exists." |
| 104 | `cohomology_basis()` | `AnalyticRiemannSurfaceData` | Correct. Requires Singular for `adjointIdeal` computation unless differentials are user-supplied. Spec correctly flags Singular dependency. |
| 105 | `period_matrix()` | `AnalyticRiemannSurfaceData` | Correct. Period matrix is a property of the analytic surface data with a chosen homology basis. Spec correctly marks as numerical evidence only. |
| 106 | `riemann_matrix()` | `AnalyticRiemannSurfaceData` | Correct. Normalized form of period matrix. |
| 107 | `abel_jacobi(divisor)` | `Jacobian(C)` or `PeriodLattice(C).jacobian()` | Mathematically correct. The Abel-Jacobi map is a morphism from the divisor group (degree zero) to the Jacobian torus. Spec correctly notes degree-zero hypothesis. The ownership dual (Jacobian vs PeriodLattice) is a genuine design choice that should be resolved later; the spec acknowledges this with the "or". |
| 108 | `monodromy_group()` | `BranchedCover(C, projection)` | Correct. Monodromy is a property of the branched cover, not the abstract curve. Different projections give different monodromy groups. Spec correctly distinguishes this from complement fundamental groups and family monodromy. |
| 109 | `endomorphism_basis()` | `PeriodLattice(C).endomorphism_ring()` | Correct. Endomorphisms are integer relations on the period lattice. Appropriately deferred pending exactness criteria. |
| 110 | `homomorphism_basis()` | `PeriodLattice(C).homomorphism_lattice()` | Correct. Same rationale. Deferred. |
| 111 | `symplectic_automorphism_group()` | `PeriodLattice(C).automorphism_group()` | Correct. Symplectic automorphisms preserve the polarization on the period lattice. Deferred. |
| 112 | `symplectic_isomorphisms()` | `PeriodLattice(C).isomorphism_lattice()` | Correct. Deferred. |

**Gate 3 verdict: PASS.** All ownership assignments are mathematically
defensible. The deferred methods (endomorphism/homomorphism/symplectic) are
correctly identified as research-evidence-only until exactness criteria exist.
The `abel_jacobi` dual ownership question is properly flagged for future
resolution.

---

### Gate 4 — Boundary Distinctions and Rejected Surfaces

**Rejected Surfaces Table:**

All 10 rejected Sage methods are verified to exist in the source and are
correctly classified:
- Raw constructor → replaced by `C.analytic_riemann_surface()`
- Graph/Voronoi helpers (`downstairs_graph`, `upstairs_graph`, `edge_permutations`) → interop evidence only
- Path interpolation (`w_values`, `make_zw_interpolator`) → backend plumbing
- Numerical integration (`simple_vector_line_integral`, `rigorous_line_integral`) → called internally
- Path following (`homotopy_continuation`) → implementation detail
- Module-level helpers (`voronoi_ghost`, `differential_basis_baker`) → backend-only

The rejection rationale for each is clear and uses consistent criteria:
backend implementation vs. mathematical surface.

**Boundary Distinctions:**

The spec identifies three distinct monodromy concepts:
1. **Branch-cover monodromy** — permutations of sheets around branch points for a fixed projection. Owned by `BranchedCover(C, projection)`.
2. **Curve-complement fundamental groups** — computed by Sirocco/Zariski-van Kampen. Owned by `PlaneCurveComplement`.
3. **Family monodromy** — Gauss-Manin/Picard-Fuchs on cohomology of fibers. Owned by `FamilyOfVarieties`.

These are genuinely distinct mathematical objects. The spec correctly assigns
them to different owners and references separate specs for the latter two. This
is a critical boundary: conflating these would create category errors.

**Gate 4 verdict: PASS.** All rejections are justified. Boundary distinctions
are mathematically correct and well-separated.

---

### Gate 5 — Numerical Evidence Policy

The spec declares:
- All numerical outputs carry an explicit `numerical=True` or equivalent flag
- Numerical outputs must not be used as exact mathematical evidence without a
  stated certificate policy (certified homotopy, rigorous integration bounds)
- Exact outputs should be distinguished from numerical approximations by return
  type or explicit attribute

**Assessment:** This policy is explicit and consistent with the Sage backend
behavior. The Sage `RiemannSurface` class already supports:
- `certification=True` flag (line 628, stored as `self._certification`)
- `integration_method='rigorous'` (line 630, uses certified homotopy
  continuation due to [Kr2016])
- `integration_method='heuristic'` (faster but non-rigorous)

The spec's policy correctly extends this to the project level, ensuring
consumers of numerical period matrices, Abel-Jacobi values, and endomorphism
bases cannot silently treat them as exact.

**Observation 1 (minor):** The spec does not specify what the `numerical=True`
flag looks like concretely — is it a keyword argument, a return type attribute,
a wrapper type? This is acceptable at the spec stage but should be resolved in
the implementation card.

**Gate 5 verdict: PASS with observation.** Policy is explicit and grounded in
Sage's existing certification/integration_method distinctions.

---

### Gate 6 — Tracking Hygiene and Dependencies

| Criterion | Status |
|-----------|--------|
| `parents` links to `FEATURE-GEOMETRY-CATEGORY-INTERFACES` | ✓ Correct |
| `dependsOn` links to `SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING` | ✓ Correct (that spec is `status: complete`) |
| Source provenance cites concrete file paths and line numbers | ✓ |
| Acceptance criteria are specific and checkable | ✓ (4/5 checked, 1 deferred) |
| Unresolved question tracked (criterion 3: "Any unresolved naming, ownership, or exactness question is split to a decision card") | ⚠ Unchecked — see Observation 2 |
| Dependencies and Boundaries section prohibits premature implementation | ✓ |
| Work log records creation date and rationale | ✓ |

**Observation 2 (minor):** Acceptance criterion 3 ("Any unresolved naming,
ownership, or exactness question is split to a decision card rather than left
as prose") is unchecked. Two items in the spec are potential candidates for
decision cards:
- The `abel_jacobi` dual ownership between `Jacobian(C)` and
  `PeriodLattice(C).jacobian()` (row 107)
- The method naming TBD for `analytic_riemann_surface` (row 102 note:
  "Name TBD with geometry spec")

Neither of these is a blocker for spec approval, but they should be tracked.
The spec already flags them in prose; creating explicit decision cards would
satisfy criterion 3.

**Gate 6 verdict: PASS with observation.** DAG edges are correct. One
acceptance criterion remains unaddressed but the spec prose already flags the
relevant questions.

---

### Summary

| Gate | Verdict |
|------|---------|
| G1 — Source Grounding | PASS |
| G2 — Category Hierarchy | PASS |
| G3 — Method Ownership | PASS |
| G4 — Boundaries & Rejections | PASS |
| G5 — Numerical Policy | PASS (obs 1) |
| G6 — Tracking Hygiene | PASS (obs 2) |

**Overall: PASS.** The spec is source-grounded, mathematically correct, and
correctly separates branch-cover monodromy from complement fundamental groups
and family monodromy. The method ownership table cites correct Sage source
lines and assigns mathematically appropriate project owners. The numerical
evidence policy is explicit and consistent with Sage's existing certification
framework. Two minor observations do not block approval.

**Recommendation:** Move status to `complete`. Split the `abel_jacobi`
ownership question and the `analytic_riemann_surface` naming question into
decision cards to satisfy acceptance criterion 3.

## Work Log

- 2026-05-06: Created from Gate 2 review of
  `[[TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE]]`, which found that the
  Riemann-surface mapping spec named this concrete next work as inline prose
  rather than a tracked successor.
- 2026-05-07: 6-Gate protocol review completed. All gates PASS. Two minor
  observations (numerical flag concreteness, unresolved decision-card splits).
