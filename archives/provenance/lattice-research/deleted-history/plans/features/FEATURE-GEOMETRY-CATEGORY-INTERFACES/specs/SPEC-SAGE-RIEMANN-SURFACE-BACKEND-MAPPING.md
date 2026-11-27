---
id: SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING
trackerStatus:
  type: spec
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE]]'
title: Map Sage RiemannSurface as an analytic curve backend, not a raw wrapper target
status: complete
priority: medium
requirement: Record how Sage `RiemannSurface` functionality should inform future curve,
  Jacobian, Abel-Jacobi, period, and monodromy category specs before any public wrapper
  or backend bridge is implemented.
acceptanceCriteria:
- Constructor and method surfaces cite Sage documentation and installed source paths.
- Public project owners are stated as mathematical nouns rather than Sage helper names.
- Numerical/certified-homotopy limitations are explicit.
- Implementation work remains blocked until curve/Jacobian/family ownership is specified
  in a later geometry category spec.
complexity: 45
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Sage RiemannSurface Backend Mapping

## Source Scope

- Sage documentation: <https://doc.sagemath.org/html/en/reference/curves/sage/schemes/riemann_surfaces/riemann_surface.html>.
- Installed Sage source: `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/riemann_surfaces/riemann_surface.py`.
- Installed curve entry points:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/affine_curve.py`
  and
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/projective_curve.py`.
- Local backend memory: `theory-graph-monodromy-hodge-methods`, which records that
  Sage Riemann-surface chaining is a candidate route for one-parameter curve-family
  monodromy.

## Backend Boundary

Sage `RiemannSurface(f, prec=53, certification=True, differentials=None,
integration_method='rigorous')` models the compact analytic Riemann surface determined
by a bivariate plane-curve equation `f(z,w)=0` over a subfield of the complex numbers.
The surface is interpreted as a covering of the coordinate plane in the first variable.
The constructor is therefore not a general project constructor for all curves or all
schemes. It is a backend route for plane-curve analytic data after the project has a
curve object, a chosen plane model/projection, and a complex embedding.

The public project noun should be an analytic curve/Riemann-surface refinement attached
to a curve, not a raw `RiemannSurface` wrapper. The existing Sage entry points
`AffineCurve.riemann_surface(**kwargs)` and `ProjectivePlaneCurve.riemann_surface(**kwargs)`
are source evidence for a future method such as `C.analytic_riemann_surface(...)` on
the appropriate complex curve category. The exact method name and owner should be
settled with the future geometry category spec.

## Candidate Surface Mapping

| Sage surface | Project owner candidate | Public meaning | Admission status |
| --- | --- | --- | --- |
| `RiemannSurface(f, prec, certification, differentials, integration_method)` | backend constructor behind a curve method | Analytic surface of a plane algebraic curve with projection to the first coordinate | Backend evidence only; not public API. |
| `C.riemann_surface(**kwargs)` | complex plane curve or smooth projective curve refinement | Construct analytic Riemann-surface data from a curve model | Candidate future method after curve-category ownership exists. |
| `monodromy_group()` | branched cover or plane-curve projection data | Local monodromy permutations around finite branch points and infinity | Backend evidence for curve-cover monodromy, not fundamental-group output. |
| `homology_basis()` | topological homology of compact Riemann surface | Homology cycles represented by lifted graph paths | Candidate backend for `H_1(X, ZZ)` once homology objects exist. |
| `cohomology_basis()` | holomorphic differentials on a smooth curve | Basis of regular differentials represented by `g/(df/dw) dz`; uses Singular unless user supplies differentials | Candidate backend for `H^0(X, Omega^1)` with explicit backend caveat. |
| `period_matrix()` / `riemann_matrix()` | Jacobian or period-lattice surface | Numerical period/Riemann matrices from a symplectic homology basis | Candidate backend for Jacobian/period data; not exact proof data by itself. |
| `endomorphism_basis()` / `homomorphism_basis()` | Jacobian/period-lattice morphisms | Numerical integer near-solutions for endomorphism or homomorphism lattices | Research evidence only until exactness/proof criteria are specified. |
| `symplectic_isomorphisms()` / `symplectic_automorphism_group()` | Jacobian isomorphism or automorphism surface | Numerical symplectic isomorphisms between Jacobians/period lattices | Research evidence only; requires proof/audit policy before use. |
| `abel_jacobi(...)`, `divisor_to_divisor_list(...)`, `reduce_over_period_lattice(...)` | Abel-Jacobi map from divisors to a Jacobian/period torus | Numerical Abel-Jacobi representatives modulo the period lattice | Candidate backend after divisor and Jacobian categories exist. |
| `downstairs_graph()`, `upstairs_graph()`, `edge_permutations()` | backend graph/interoperability data | Voronoi and lifted graph data used to compute homology and monodromy | Interop evidence; not public geometry vocabulary. |

## Limitations And Audit Requirements

- The backend is numerical. The documentation and source describe certified homotopy
  continuation and rigorous integration options, but period matrices, endomorphism
  bases, homomorphism bases, and Abel-Jacobi values are still numerical artifacts that
  need explicit certification or proof-audit criteria before being used as exact
  mathematical evidence.
- `cohomology_basis()` currently calls Singular `adjointIdeal` for regular
  differentials unless `differentials` are supplied. The source notes that user-supplied
  differentials make the computation independent from Singular and are required in
  examples over number fields with complex embeddings.
- `monodromy_group()` returns permutations for the chosen plane projection and branch
  locus. It should not be confused with the fundamental group of a curve complement or
  with global family monodromy on cohomology.
- Wrapper work is premature until geometry specs define curve, analytic surface,
  divisor, Jacobian, period lattice, homology, and family-monodromy owners.

## Follow-Up Consequence

The next durable work is tracked as
`[[SPEC-CURVE-JACOBIAN-PERIOD-LATTICE-OWNERSHIP]]`. That later spec can consume
this mapping and decide whether
`C.analytic_riemann_surface(...)`, `C.period_matrix(...)`,
`C.jacobian().period_lattice(...)`, or a different public surface best expresses the
mathematics.

## Non-Admission Finding

- Searched: Sage documentation page linked above; installed source file
  `sage/schemes/riemann_surfaces/riemann_surface.py`; installed curve entry points
  `sage/schemes/curves/affine_curve.py` and
  `sage/schemes/curves/projective_curve.py`; local memory
  `theory-graph-monodromy-hodge-methods`.
- Found: Sage exposes a rich numerical analytic backend, but the checked sources do
  not define the project-level owners for curve analytic refinements, Jacobians,
  period lattices, Abel-Jacobi maps, homology objects, or family monodromy.
- Conclusion: inference based on the checked sources: no implementation card is
  admitted from this pass; wrapper implementation should wait for those geometry
  owner specs rather than exposing raw Sage helper names.
- Confidence: High for this source-admission card's scope.
- Gaps: broader geometry category specs, Sage Jacobian docs, and family-monodromy
  backend cards remain to be researched separately.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Hermes Agent — delegated 6-gate spec card review)

**Gates passed:** G1, G2, G3, G4, G5, G6
**Gates failed:** None
**Outcome:** PASS — the spec is source-grounded, mathematically correct, and properly
routes all ambiguity to tracked follow-up cards. No gate failures. Two advisory
findings noted under G2.

---

#### G1 — Source Grounding

PASS.

Every source citation in the spec was verified on disk:

| Reference | Actual path | Exists |
| --- | --- | --- |
| Sage RiemannSurface documentation | `https://doc.sagemath.org/html/en/reference/curves/sage/schemes/riemann_surfaces/riemann_surface.html` | YES (public URL) |
| Installed Sage source | `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/riemann_surfaces/riemann_surface.py` | YES (4115 lines) |
| Installed curve entry point (affine) | `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/affine_curve.py` | YES (2927 lines) |
| Installed curve entry point (projective) | `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/projective_curve.py` | YES (3024 lines) |
| Local backend memory | `/home/dzack/research/.agents/memories/theory-graph-monodromy-hodge-methods.md` | YES (43 lines) |
| Parent feature | `/home/dzack/research/plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/FEATURE-GEOMETRY-CATEGORY-INTERFACES.md` | YES |
| Dependency card | `/home/dzack/research/plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS/PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH/tasks/TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE.md` | YES |
| Follow-up spec | `/home/dzack/research/plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/specs/SPEC-CURVE-JACOBIAN-PERIOD-LATTICE-OWNERSHIP.md` | YES |

Frontmatter validation:
- `id: SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING` matches filename stem ✓
- `parents` correctly lists `FEATURE-GEOMETRY-CATEGORY-INTERFACES` ✓
- `dependsOn` correctly lists `TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE` ✓
- The dependency task's work log confirms this spec was created as its output ✓

Sage source verification:
- Constructor signature `RiemannSurface(f, prec=53, certification=True, differentials=None, integration_method='rigorous')` confirmed at line 624-631 of `riemann_surface.py` ✓
- `AffineCurve.riemann_surface(**kwargs)` confirmed at line 1931 of `affine_curve.py` ✓
- `ProjectivePlaneCurve.riemann_surface(**kwargs)` confirmed at line 1895 of `projective_curve.py` ✓

No orphan references, dead links, or missing source paths detected.

#### G2 — Sage Surface Completeness

PASS with two advisory findings.

The spec's surface mapping table (lines 58-69) inventories 10 surface rows covering all
major mathematical surfaces of the Sage `RiemannSurface` class. Source-method audit:

| Sage method | Source line | Spec table coverage |
| --- | --- | --- |
| `RiemannSurface(f, prec, certification, differentials, integration_method)` | L624 | Row 1 (constructor) ✓ |
| `C.riemann_surface(**kwargs)` | affine L1931, projective L1895 | Row 2 (curve method) ✓ |
| `monodromy_group()` | L1416 | Row 3 ✓ |
| `homology_basis()` | L1513 | Row 4 ✓ |
| `cohomology_basis(option=1)` | L1841 | Row 5 ✓ |
| `period_matrix()` | L2357 | Row 6 ✓ |
| `riemann_matrix()` | L2396 | Row 6 ✓ |
| `endomorphism_basis(b, r)` | L2515 | Row 7 ✓ |
| `homomorphism_basis(other, b, r)` | L2557 | Row 7 ✓ |
| `symplectic_isomorphisms(other, hom_basis, b, r)` | L2757 | Row 8 ✓ |
| `symplectic_automorphism_group(endo_basis, b, r)` | L2835 | Row 8 ✓ |
| `abel_jacobi(divisor, verbose)` | L3475 | Row 9 ✓ |
| `divisor_to_divisor_list(divisor, eps)` | L3807 | Row 9 ✓ |
| `reduce_over_period_lattice(vector, method)` | L3524 | Row 9 ✓ |
| `downstairs_graph()` | L854 | Row 10 ✓ |
| `upstairs_graph()` | L877 | Row 10 ✓ |
| `edge_permutations()` | L1371 | Row 10 ✓ |

**G2 Finding 1 (advisory):** `places_at_branch_locus()` (source line 3673) is a
publicly documented method returning function-field places above the branch locus.
It is mathematically relevant for divisor construction and feeds into
`divisor_to_divisor_list()`. The spec could add a row or note under the Abel-Jacobi
row mentioning this method. Not a gate failure — the spec's existing mapping already
covers the divisor-to-Jacobian pipeline at a high level.

**G2 Finding 2 (advisory):** The endomorphism row (row 7) covers `endomorphism_basis()`
and `homomorphism_basis()` but does not mention the associated methods
`tangent_representation_numerical()` (L2596), `tangent_representation_algebraic()`
(L2646), or `rosati_involution()` (L2721). These are endomorphism-adjacent and could
be noted as backend sub-evidence under the same row. Not a gate failure — the row's
"Research evidence only" status already defers exactness criteria to future specs.

Methods correctly excluded from the table (non-mathematical or low-level helpers):
`plot_paths()` (L2426), `plot_paths3d()` (L2462), `make_zw_interpolator()` (L1688),
`simple_vector_line_integral()` (L1780), `rigorous_line_integral()` (L2035),
`matrix_of_integral_values()` (L2263), `w_values()` (L767), `downstairs_edges()`
(L800), `upstairs_edges()` (L1273), `homotopy_continuation()` (L1005),
`strong_approximation()` (L3717), and `curve()` (L3651). These are either
visualization methods, internal graph helpers, integration plumbing, or basic
attribute accessors — their exclusion from a high-level mathematical mapping is
acceptable.

#### G3 — Mathematical Correctness

PASS.

Every mathematical claim in the spec was cross-checked against the Sage source at
`/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/riemann_surfaces/riemann_surface.py`:

- **"models the compact analytic Riemann surface determined by a bivariate plane-curve equation f(z,w)=0 over a subfield of the complex numbers"** — verified against module docstring lines 2-7 and constructor line 647 (`only bivariate polynomials supported`) ✓
- **"interpreted as a covering of the coordinate plane in the first variable"** — consistent with the downstairs/upstairs graph construction (L854, L877) and branch locus computation (L687-692) ✓
- **"not a general project constructor for all curves or all schemes"** — correct; requires bivariate polynomial, rejects degree ≤ 1 (L649-650) ✓
- **`monodromy_group()` returns local monodromy permutations around finite branch points and infinity"** — source L1416-1511 confirms permutation group on sheets ✓
- **`homology_basis()` returns homology cycles represented by lifted graph paths"** — source L1513-1686 confirms graph-path cycle construction ✓
- **`cohomology_basis()` uses Singular `adjointIdeal` unless differentials are supplied"** — source L1847-1851 confirms Singular `adjointIdeal` call; L659-661 confirms user-supplied differential path ✓
- **`period_matrix()` / `riemann_matrix()` produce numerical period/Riemann matrices"** — source L2357-2424 confirms numerical computation via `matrix_of_integral_values` ✓
- **`endomorphism_basis()` / `homomorphism_basis()` produce numerical integer near-solutions"** — source L2515-2594 confirms LLL-based integer relation finding ✓
- **`symplectic_isomorphisms()` / `symplectic_automorphism_group()` produce numerical symplectic isomorphisms"** — source L2757-2874 confirms period-matrix comparison with symplectic condition ✓
- **`abel_jacobi()` produces numerical Abel-Jacobi representatives modulo the period lattice"** — source L3475-3649 confirms numerical integration with `reduce_over_period_lattice` ✓
- **`downstairs_graph()`, `upstairs_graph()`, `edge_permutations()` provide Voronoi and lifted graph data"** — source L854-913, L877-913, L1371-1414 confirms Voronoi-based graph construction ✓

Limitations section verification:
- **"period matrices, endomorphism bases, homomorphism bases, and Abel-Jacobi values are still numerical artifacts"** — correct; all use floating-point complex numbers via `ComplexField(prec)` and LLL-based integer recognition, not exact algebraic computation ✓
- **"cohomology_basis() currently calls Singular adjointIdeal"** — confirmed at L1882-1885 with `sage.libs.singular.function_factory.lib("paraplanecurves.lib")` and `adjointIdeal = ...` ✓
- **"monodromy_group() should not be confused with the fundamental group of a curve complement"** — correct; the method returns sheet permutations of the branched cover, not a finitely presented fundamental group ✓
- **"Wrapper work is premature until geometry specs define curve, analytic surface, divisor, Jacobian, period lattice, homology, and family-monodromy owners"** — this is a correct architectural assessment consistent with the spec's non-admission finding ✓

No mathematical errors, mischaracterizations, or unsupported claims detected.

#### G4 — Nonmathematical Rejection

PASS.

The spec correctly identifies and rejects non-mathematical surfaces:

- Raw `RiemannSurface` constructor is classified as "Backend evidence only; not public API" — correct; the Sage class should not be exposed as a public project wrapper ✓
- `downstairs_graph()`, `upstairs_graph()`, `edge_permutations()` classified as "Interop evidence; not public geometry vocabulary" — correct; these are internal Voronoi graph helpers, not mathematical geometry objects ✓
- The Non-Admission Finding section (lines 98-112) explicitly states "no implementation card is admitted from this pass; wrapper implementation should wait for those geometry owner specs" — correctly blocks premature implementation ✓
- The five-field negative-finding format (Searched, Found, Conclusion, Confidence, Gaps) is properly followed ✓
- Sage method names are mapped through candidate project owners rather than adopted as-is — consistent with the rejection of raw Sage helper names as public vocabulary ✓

The spec does not leak implementation intent, does not propose wrapper code, and does
not treat Sage internal names as project mathematical nouns.

#### G5 — Ambiguity Routing

PASS.

Unresolved questions are explicitly routed to tracked follow-up cards:

- **Method naming ambiguity:** "The exact method name and owner should be settled with the future geometry category spec" (line 53-54) — correctly defers naming to the ownership spec ✓
- **Owner ambiguity:** Table rows 3-10 all use "Candidate backend for X once Y objects exist" or "Candidate future method after Z ownership exists" — explicit about what is missing ✓
- **Follow-up tracked:** `SPEC-CURVE-JACOBIAN-PERIOD-LATTICE-OWNERSHIP` (lines 91-95) is a concrete tracked spec card that lists the specific owner questions ✓
- **Admission status column:** Each table row has an explicit status (Backend evidence only, Candidate future method, Candidate backend, Research evidence only, Interop evidence) — no ambiguous or hand-wavy statuses ✓
- **Boundary distinctions:** `monodromy_group()` is clearly distinguished from complement fundamental groups and family monodromy on cohomology (lines 82-84) — prevents category confusion ✓
- **Numerical vs. exact boundary:** Limitations section (lines 73-80) explicitly states numerical outputs need certification/proof-audit criteria before use as exact mathematical evidence ✓

No ambiguity is left as unresolved prose; every open question has a routing path.

#### G6 — Obligation Preservation

PASS.

- `dependsOn: [[TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE]]` — the research task that authorized this spec is correctly declared ✓
- The research task's work log (line 61-62) confirms this spec was created from it: "Created `[[SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING]]` to record constructor and method mapping" ✓
- Follow-up consequence (lines 90-95) links to the concrete tracked spec `SPEC-CURVE-JACOBIAN-PERIOD-LATTICE-OWNERSHIP` ✓
- The follow-up spec's `dependsOn` correctly lists this spec: `dependsOn: [[SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING]]` ✓
- Acceptance criteria (lines 16-21) are concrete and checkable:
  1. "Constructor and method surfaces cite Sage documentation and installed source paths" — CHECKABLE against this review's G2 audit ✓
  2. "Public project owners are stated as mathematical nouns rather than Sage helper names" — CHECKABLE; the Candidate Surface Mapping table names complex curve, homology object, holomorphic differential space, Jacobian, etc. ✓
  3. "Numerical/certified-homotopy limitations are explicit" — CHECKABLE; Limitations section (lines 73-86) ✓
  4. "Implementation work remains blocked until curve/Jacobian/family ownership is specified" — CHECKABLE; Non-Admission Finding confirms blocking ✓
- The Non-Admission Finding preserves the five-field format obligation and explicitly records confidence level and remaining gaps ✓

No broken dependency chains, orphaned obligations, or unmet acceptance criteria detected.

---

**Overall verdict:** The spec passes all six gates. It is a well-grounded,
mathematically accurate mapping of Sage RiemannSurface functionality into the
project's category-spec vocabulary, with proper non-admission boundaries and
clear ambiguity routing to the follow-up ownership spec. The two G2 advisory
findings do not block acceptance.
