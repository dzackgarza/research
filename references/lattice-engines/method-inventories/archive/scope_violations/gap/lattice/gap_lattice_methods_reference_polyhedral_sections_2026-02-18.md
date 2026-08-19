# Archived GAP Umbrella Reference Sections (Out of Active Scope)

Archived from `docs/gap/lattice/gap_lattice_methods_reference.md` on 2026-02-18.

These sections are polyhedral/toric/LP-centered surfaces and are out of active bilinear-form lattice scope for this project.

## Package Ecosystem Sections

### 2.1 4ti2Interface

Integer relation, toric ideal, Hilbert basis, and semigroup workflows.

| Function | Description | Tags |
|----------|-------------|------|
| `4ti2Interface_groebner_matrix` | Gröbner/toric ideal matrix-side routine | `[PKG, TORIC]` |
| `4ti2Interface_groebner_basis` | Gröbner basis routine for toric/integer relation systems | `[PKG, TORIC]` |
| `4ti2Interface_hilbert_inequalities` | Hilbert basis from inequality descriptions | `[PKG, POLY, TORIC]` |
| `4ti2Interface_hilbert_equalities_in_positive_orthant` | Hilbert basis under equalities with positive orthant constraints | `[PKG, POLY, TORIC]` |
| `4ti2Interface_hilbert_equalities_and_inequalities` | Hilbert basis from mixed equality/inequality systems | `[PKG, POLY, TORIC]` |
| `4ti2Interface_zsolve_equalities_and_inequalities` | Integer solution enumeration/structure for mixed systems | `[PKG, ZZMOD, TORIC]` |
| `4ti2Interface_graver_equalities` | Graver basis from equality constraints | `[PKG, ZZMOD, TORIC]` |

Definiteness note:
- These are integer-algebraic/polyhedral methods, not real-signature quadratic-form methods.

### 2.2 NormalizInterface

Interface to Normaliz for affine monoids, vector configurations, lattice polytopes, and rational cones.

| Package | Role | Tags |
|---------|------|------|
| `NormalizInterface` | Polyhedral/lattice-point computations in cones/polytopes/monoids | `[PKG, POLY]` |

Representative `NormalizInterface` methods:

| Function | Description | Tags |
|----------|-------------|------|
| `NmzCone(list)` | Construct a Normaliz cone object from typed input matrices | `[PKG, POLY]` |
| `NmzCompute(cone[, props])` | Trigger computation of requested cone properties/options | `[PKG, POLY]` |
| `NmzConeProperty(cone, property)` | Query/compute a specific property by name | `[PKG, POLY]` |
| `NmzKnownConeProperties(cone)` | List already computed properties on a cone object | `[PKG, POLY]` |
| `NmzHasConeProperty(cone, property)` | Check if a property is already available | `[PKG, POLY]` |
| `NmzGenerators(cone)` / `NmzExtremeRays(cone)` / `NmzSupportHyperplanes(cone)` | Core geometric generators/rays/facet-description accessors | `[PKG, POLY]` |
| `NmzHilbertBasis(cone)` / `NmzHilbertSeries(cone)` / `NmzHilbertQuasiPolynomial(cone)` | Hilbert-basis and degreewise counting invariants | `[PKG, POLY]` |
| `NmzTriangulation(cone)` / `NmzTriangulationSize(cone)` / `NmzTriangulationDetSum(cone)` | Triangulation-level combinatorial output | `[PKG, POLY]` |
| `NmzLatticePoints(cone)` / `NmzVerticesOfPolyhedron(cone)` | Lattice-point and vertex extraction in polyhedral regimes | `[PKG, POLY]` |

Definiteness note:
- Not a quadratic-form lattice package; no PD/INDEF signature regime is central.

### 2.4 toric

| Package | Role | Tags |
|---------|------|------|
| `toric` | Toric varieties over fixed lattices/fans/cones; divisor-polytopes and lattice-point operations | `[PKG, TORIC, POLY]` |

Representative `toric` methods:

| Function | Description | Tags |
|----------|-------------|------|
| `InsideCone(...)` | Membership test for a cone | `[PKG, TORIC, POLY]` |
| `InDualCone(...)` | Membership test in dual cone | `[PKG, TORIC, POLY]` |
| `PolytopeLatticePoints(...)` | Lattice points of a polytope | `[PKG, TORIC, POLY]` |
| `Faces(...)` / `ConesOfFan(...)` / `NumberOfConesOfFan(...)` | Face/fan combinatorics | `[PKG, TORIC, POLY]` |
| `ToricStar(...)` | Star construction in fan geometry | `[PKG, TORIC, POLY]` |
| `DualSemigroupGenerators(...)` | Semigroup generators from dual cone data | `[PKG, TORIC, POLY]` |
| `EmbeddingAffineToricVariety(...)` | Construct affine toric variety embedding ideal data | `[PKG, TORIC]` |
| `DivisorPolytope(...)` / `DivisorPolytopeLatticePoints(...)` / `RiemannRochBasis(...)` | Divisor polytope and Riemann-Roch space computations | `[PKG, TORIC, POLY]` |
| `EulerCharacteristic(...)` / `BettiNumberToric(...)` / `CardinalityOfToricVariety(...)` | Topological and finite-field invariants | `[PKG, TORIC]` |

Definiteness note:
- Lattice is combinatorial (`\mathbb{Z}^n` data), not a PD/INDEF bilinear-form lattice object.

### 2.5 Convex/polyhedral interfaces

| Package | Role | Tags |
|---------|------|------|
| `NConvex` | Polyhedra/polyhedral complex support and backend conversions | `[PKG, POLY]` |
| `CddInterface` | Interface to cdd/cddlib for H/V polyhedral conversion workflows | `[PKG, POLY]` |

Representative `CddInterface` methods:

| Function | Description | Tags |
|----------|-------------|------|
| `Cdd_PolyhedronByInequalities(...)` / `Cdd_PolyhedronByGenerators(...)` | Build polyhedra from H-representation or V-representation input | `[PKG, POLY]` |
| `Cdd_Canonicalize(P)` | Remove redundant constraints/generators in representation | `[PKG, POLY]` |
| `Cdd_V_Rep(P)` / `Cdd_H_Rep(P)` | Convert between reduced V- and H-representations | `[PKG, POLY]` |
| `Cdd_AmbientSpaceDimension(P)` / `Cdd_Dimension(P)` | Ambient and intrinsic dimension attributes | `[PKG, POLY]` |
| `Cdd_GeneratingVertices(P)` / `Cdd_GeneratingRays(P)` | Extract vertex/ray generators | `[PKG, POLY]` |
| `Cdd_Equalities(P)` / `Cdd_Inequalities(P)` | Retrieve linear equalities/inequalities | `[PKG, POLY]` |
| `Cdd_Faces(P)` / `Cdd_FacesWithFixedDimension(P, d)` / `Cdd_Facets(P)` | Face lattice and facet-level queries | `[PKG, POLY]` |
| `Cdd_InteriorPoint(P)` / `Cdd_FacesWithInteriorPoints(P)` / `Cdd_FacesWithFixedDimensionAndInteriorPoints(P, d)` | Interior-point-aware face extraction methods | `[PKG, POLY]` |
| `Cdd_ExtendLinearity(P, V)` / `Cdd_Lines(P)` / `Cdd_Vertices(P)` | Lineality/vertex extraction and linearity-extension helpers | `[PKG, POLY]` |
| `Cdd_IsEmpty(P)` / `Cdd_IsCone(P)` / `Cdd_IsLinSpace(P)` / `Cdd_IsPointed(P)` | Basic geometric predicates | `[PKG, POLY]` |
| `Cdd_IsContained(P1, P2)` / `Cdd_Intersection(P1, P2)` | Polyhedral containment/intersection operations | `[PKG, POLY]` |
| `Cdd_LinearProgram(P, b)` / `Cdd_FourierProjection(P, var)` | LP and projection/elimination workflows for polyhedral models | `[PKG, POLY]` |

Representative `NConvex` methods:

| Function | Description | Tags |
|----------|-------------|------|
| `ConeByInequalities(L)` / `ConeByEqualitiesAndInequalities(Eq, Ineq)` / `ConeByGenerators(L)` | Cone constructors from inequality/equality/generator data. | `[PKG, POLY]` |
| `Cone(L)` / `Cone(cdd_cone)` / `DualCone(C)` / `HilbertBasis(C)` | Core cone conversion and Hilbert-basis workflows. | `[PKG, POLY]` |
| `Fan(R, C)` / `FansFromTriangulation(R)` / `FanFromTriangulation(R)` | Fan construction and triangulation-derived fan workflows. | `[PKG, POLY]` |
| `PolyhedronByInequalities(L)` / `Polyhedron(P, C)` / `TailCone(P)` | Polyhedron constructors and tail-cone extraction. | `[PKG, POLY]` |
| `SolveLinearProgram(P, max_or_min, target_func)` | Linear programming on NConvex polyhedra/polytopes. | `[PKG, POLY]` |
| `PolytopeByInequalities(L)` / `Polytope(L)` / `LatticePoints(P)` / `NormalFan(P)` | Polytope construction, lattice-point extraction, and fan conversion. | `[PKG, POLY]` |
| `IntersectionOfCones(...)` / `IntersectionOfPolytopes(P1, P2)` / `FourierProjection(...)` | Intersection and projection operations across cone/polytope surfaces. | `[PKG, POLY]` |
| `SolveEqualitiesAndInequalitiesOverIntergers(...)` | Integer equalities/inequalities solver returning polytope+cone decomposition data. | `[PKG, POLY]` |

Detailed inventory note:

- Full NConvex method-level checklist/reference surfaces are in `docs/archive/scope_violations/nconvex_methods_checklist.md` and `docs/archive/scope_violations/nconvex/lattice/nconvex_lattice_reference.md`.
- Full CddInterface checklist/reference surfaces are archived at `docs/archive/scope_violations/cddinterface_methods_checklist.md` and `docs/archive/scope_violations/cddinterface/lattice/cddinterface_lattice_reference.md` (out of active bilinear-form lattice scope).


## Consolidated Index Sections

### 4.5 4ti2Interface methods

- `4ti2Interface_groebner_basis`
- `4ti2Interface_groebner_matrix`
- `4ti2Interface_graver_equalities`
- `4ti2Interface_hilbert_equalities_and_inequalities`
- `4ti2Interface_hilbert_equalities_in_positive_orthant`
- `4ti2Interface_hilbert_inequalities`
- `4ti2Interface_zsolve_equalities_and_inequalities`

### 4.6 NormalizInterface methods

- `NmzCompute`
- `NmzCone`
- `NmzConeProperty`
- `NmzExtremeRays`
- `NmzGenerators`
- `NmzHasConeProperty`
- `NmzHilbertBasis`
- `NmzHilbertQuasiPolynomial`
- `NmzHilbertSeries`
- `NmzKnownConeProperties`
- `NmzLatticePoints`
- `NmzSupportHyperplanes`
- `NmzTriangulation`
- `NmzTriangulationDetSum`
- `NmzTriangulationSize`
- `NmzVerticesOfPolyhedron`

### 4.7 toric methods

- `BettiNumberToric`
- `CardinalityOfToricVariety`
- `ConesOfFan`
- `DivisorPolytope`
- `DivisorPolytopeLatticePoints`
- `DualSemigroupGenerators`
- `EmbeddingAffineToricVariety`
- `EulerCharacteristic`
- `Faces`
- `InDualCone`
- `InsideCone`
- `NumberOfConesOfFan`
- `PolytopeLatticePoints`
- `RiemannRochBasis`
- `ToricStar`

### 4.8 NConvex methods

- `AmbientSpaceDimension`
- `BasisOfLinealitySpace`
- `Cone`
- `ConeByEqualitiesAndInequalities`
- `ConeByGenerators`
- `ConeByInequalities`
- `Contains`
- `DefiningInequalities`
- `DualCone`
- `EqualitiesOfCone`
- `EqualitiesOfPolytope`
- `ExternalCddCone`
- `ExternalCddPolyhedron`
- `ExternalCddPolytope`
- `ExternalNmzCone`
- `ExternalNmzPolyhedron`
- `FacesOfCone`
- `Fan`
- `FanFromTriangulation`
- `FansFromTriangulation`
- `FourierProjection`
- `GridGeneratedByCone`
- `HilbertBasis`
- `IntersectionOfCones`
- `IntersectionOfPolytopes`
- `IsFullDimensional`
- `IsInteriorPoint`
- `IsLatticePolytope`
- `IsRegularCone`
- `LatticePoints`
- `LatticePointsGenerators`
- `MainPolytope`
- `MainRatPolytope`
- `NormalFan`
- `Polyhedron`
- `PolyhedronByInequalities`
- `Polytope`
- `PolytopeByInequalities`
- `RandomInteriorPoint`
- `SolveEqualitiesAndInequalitiesOverIntergers`
- `SolveLinearProgram`
- `Vertices`
- `VerticesOfPolytope`
- plus source-only declared helper/auxiliary surfaces tracked in `docs/archive/scope_violations/nconvex_methods_checklist.md`.

### 4.9 CddInterface methods

- `Cdd_AmbientSpaceDimension`
- `Cdd_Canonicalize`
- `Cdd_Dimension`
- `Cdd_Equalities`
- `Cdd_ExtendLinearity`
- `Cdd_Faces`
- `Cdd_FacesWithFixedDimensionAndInteriorPoints`
- `Cdd_FacesWithFixedDimension`
- `Cdd_FacesWithInteriorPoints`
- `Cdd_Facets`
- `Cdd_FourierProjection`
- `Cdd_GeneratingRays`
- `Cdd_GeneratingVertices`
- `Cdd_H_Rep`
- `Cdd_InteriorPoint`
- `Cdd_Intersection`
- `Cdd_Inequalities`
- `Cdd_IsCone`
- `Cdd_IsEmpty`
- `Cdd_IsContained`
- `Cdd_IsLinSpace`
- `Cdd_IsPointed`
- `Cdd_LinearProgram`
- `Cdd_Lines`
- `Cdd_PolyhedronByGenerators`
- `Cdd_PolyhedronByInequalities`
- `Cdd_V_Rep`
- `Cdd_Vertices`
