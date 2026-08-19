# GAP NConvex Lattice-Oriented Reference
## Polyhedral cone/fan/polyhedron/polytope workflows and integer-solve surfaces

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PKG]` | Provided by GAP package `NConvex` |
| `[POLY]` | Polyhedral/cone/polytope computation workflow |
| `[CONE]` | Cone-specific surface |
| `[FAN]` | Fan-specific surface |
| `[POLYH]` | Polyhedron-specific surface |
| `[POLYTOPE]` | Polytope-specific surface |
| `[LP]` | Linear programming/projection workflow |
| `[INT]` | Integer-system solving workflow |
| `[SRC]` | Declared in package source but not listed in current manual index |

---

## 1. Scope

`NConvex` is an in-scope GAP package for polyhedral computations in the homalg ecosystem.
The lattice-relevant surface here is the integer/rational polyhedral API:

- cones and fans,
- polyhedra and polytopes,
- lattice-point and Hilbert-basis attributes,
- linear-programming and Fourier-projection operations,
- integer equalities/inequalities solving via zsolve-style decomposition.

---

## 2. Manual-Indexed API Surface

The following runtime names are listed in the current NConvex manual index (`chapInd_mj.html`).

### 2.1 Shared convex-object API

| Function | Description | Tags |
|----------|-------------|------|
| `AmbientSpaceDimension(obj)` | Ambient-space dimension attribute for convex objects. | `[PKG, POLY]` |
| `Dimension(obj)` | Intrinsic dimension attribute for convex objects. | `[PKG, POLY]` |
| `IsFullDimensional(obj)` | Predicate for full-dimensionality. | `[PKG, POLY]` |
| `InteriorPoint(obj)` | Interior-point attribute on convex objects. | `[PKG, POLY]` |

### 2.2 Cone API

| Function | Description | Tags |
|----------|-------------|------|
| `ConeByInequalities(L)` | Construct cone from inequality rows. | `[PKG, POLY, CONE]` |
| `ConeByEqualitiesAndInequalities(Eq, Ineq)` | Construct cone from equality and inequality systems. | `[PKG, POLY, CONE]` |
| `Cone(L)` / `Cone(cdd_cone)` | Cone constructors from rays/list or CddInterface object. | `[PKG, POLY, CONE]` |
| `DefiningInequalities(C)` / `EqualitiesOfCone(C)` | Defining inequality/equality data of cone `C`. | `[PKG, POLY, CONE]` |
| `DualCone(C)` | Dual-cone construction. | `[PKG, POLY, CONE]` |
| `FacesOfCone(C)` / `Facets(C)` | Face/facet extraction for cone `C`. | `[PKG, POLY, CONE]` |
| `FVector(C)` | Face-count vector (`f`-vector) attribute. | `[PKG, POLY, CONE]` |
| `RelativeInteriorRay(C)` | Relative interior ray/point witness. | `[PKG, POLY, CONE]` |
| `HilbertBasis(C)` / `HilbertBasisOfDualCone(C)` | Hilbert-basis computations for cone and dual cone. | `[PKG, POLY, CONE]` |
| `LinealitySpaceGenerators(C)` | Basis for lineality space of `C`. | `[PKG, POLY, CONE]` |
| `ExternalCddCone(C)` / `ExternalNmzCone(C)` | Convert to CddInterface/NormalizInterface external objects. | `[PKG, POLY, CONE]` |
| `LatticePointsGenerators(C)` | Generator decomposition for lattice points in cone context. | `[PKG, POLY, CONE]` |
| `GridGeneratedByCone(C)` / `GridGeneratedByOrthogonalCone(C)` | Homalg `Z`-module grid surfaces from cone data. | `[PKG, POLY, CONE]` |
| `FactorGrid(C)` / `FactorGridMorphism(C)` | Factor-grid module and morphism attributes. | `[PKG, POLY, CONE]` |
| `IsRegularCone(C)` / `IsRay(C)` / `IsZero(C)` | Core cone predicates. | `[PKG, POLY, CONE]` |
| `FourierProjection(C, m)` | Coordinate-elimination projection in cone setting. | `[PKG, POLY, CONE, LP]` |
| `IntersectionOfCones(C1, C2)` / `IntersectionOfCones(L)` | Binary/list cone intersections. | `[PKG, POLY, CONE]` |
| `Contains(C1, C2)` | Cone containment predicate. | `[PKG, POLY, CONE]` |
| `IsRelativeInteriorRay(L, C)` | Predicate for point/ray in relative interior of `C`. | `[PKG, POLY, CONE]` |
| `*(n, C)` / `*(A, C)` | Cone scaling and matrix-action overloads. | `[PKG, POLY, CONE]` |
| `NonReducedInequalities(C)` | Non-reduced inequality list for cone `C`. | `[PKG, POLY, CONE]` |

### 2.3 Fan API

| Function | Description | Tags |
|----------|-------------|------|
| `Fan(F)` / `Fan(C)` / `Fan(R, C)` | Fan constructors from fan/list/rays-plus-cones data. | `[PKG, POLY, FAN]` |
| `FansFromTriangulation(R)` / `FanFromTriangulation(R)` | Triangulation-derived fan construction from ray generators. | `[PKG, POLY, FAN]` |
| `RayGenerators(F)` / `GivenRayGenerators(F)` | Ray-generator attribute surfaces. | `[PKG, POLY, FAN]` |
| `RaysInMaximalCones(F)` / `MaximalCones(F)` | Maximal-cone incidence and maximal-cone extraction. | `[PKG, POLY, FAN]` |
| `FVector(F)` | Fan face-count vector attribute. | `[PKG, POLY, FAN]` |
| `IsWellDefinedFan(F)` / `IsComplete(F)` / `IsPointed(F)` | Fan validity/completeness/pointedness predicates. | `[PKG, POLY, FAN]` |
| `IsSmooth(F)` / `IsSimplicial(F)` | Smoothness/simpliciality predicates. | `[PKG, POLY, FAN]` |
| `IsNormalFan(F)` / `IsRegularFan(F)` / `IsFanoFan(F)` | Normal/regular/fano fan predicates. | `[PKG, POLY, FAN]` |

### 2.4 Polyhedron and integer-solve API

| Function | Description | Tags |
|----------|-------------|------|
| `PolyhedronByInequalities(L)` | Construct polyhedron from affine inequalities. | `[PKG, POLY, POLYH]` |
| `Polyhedron(P, C)` / `Polyhedron(L, C)` / `Polyhedron(P, L)` / `Polyhedron(P_vertices, C_rays)` | Polyhedron constructions via Minkowski-sum style polytope/cone data. | `[PKG, POLY, POLYH]` |
| `ExternalCddPolyhedron(P)` / `ExternalNmzPolyhedron(P)` | Convert polyhedron to Cdd/Normaliz external objects. | `[PKG, POLY, POLYH]` |
| `DefiningInequalities(P)` | Defining inequalities of polyhedron `P`. | `[PKG, POLY, POLYH]` |
| `MainRatPolytope(P)` / `MainPolytope(P)` | Main rational/integral polytope attributes. | `[PKG, POLY, POLYH]` |
| `VerticesOfMainRatPolytope(P)` / `VerticesOfMainPolytope(P)` | Vertex extraction from main polytope components. | `[PKG, POLY, POLYH]` |
| `TailCone(P)` / `RayGeneratorsOfTailCone(P)` | Tail-cone attributes for polyhedra. | `[PKG, POLY, POLYH]` |
| `LatticePointsGenerators(P)` | Generator decomposition for integral points in polyhedron. | `[PKG, POLY, POLYH]` |
| `BasisOfLinealitySpace(P)` | Basis of polyhedron lineality space. | `[PKG, POLY, POLYH]` |
| `FVector(P)` | Face-vector attribute for polyhedron. | `[PKG, POLY, POLYH]` |
| `IsBounded(P)` / `IsPointed(P)` | Boundedness and pointed-tail predicates. | `[PKG, POLY, POLYH]` |
| `SolveLinearProgram(P, max_or_min, target_func)` | LP over polyhedron/polytope returning solution and objective or `fail`. | `[PKG, POLY, POLYH, LP]` |
| `SolveEqualitiesAndInequalitiesOverIntergers(eqs, eqs_rhs, ineqs, ineqs_rhs[, signs])` | Integer-system solving into polytope+cone+free-part decomposition data. | `[PKG, POLY, INT]` |

### 2.5 Polytope API

| Function | Description | Tags |
|----------|-------------|------|
| `PolytopeByInequalities(L)` / `Polytope(L)` | Polytope constructors from inequalities or vertices. | `[PKG, POLY, POLYTOPE]` |
| `ExternalCddPolytope(P)` | Convert polytope to CddInterface object. | `[PKG, POLY, POLYTOPE]` |
| `LatticePoints(P)` / `RelativeInteriorLatticePoints(P)` | Lattice-point extraction (all / relative interior). | `[PKG, POLY, POLYTOPE]` |
| `VerticesOfPolytope(P)` / `Vertices(P)` | Vertex extraction operations. | `[PKG, POLY, POLYTOPE]` |
| `DefiningInequalities(P)` / `EqualitiesOfPolytope(P)` / `FacetInequalities(P)` | Defining/facet inequality surfaces. | `[PKG, POLY, POLYTOPE]` |
| `VerticesInFacets(P)` | Vertex-facet incidence data. | `[PKG, POLY, POLYTOPE]` |
| `NormalFan(P)` / `FaceFan(P)` | Normal-fan and face-fan constructions. | `[PKG, POLY, POLYTOPE]` |
| `AffineCone(P)` | Affine-cone lift of polytope. | `[PKG, POLY, POLYTOPE]` |
| `PolarPolytope(P)` / `DualPolytope(P)` | Polar/dual polytope constructions. | `[PKG, POLY, POLYTOPE]` |
| `IsEmpty(P)` / `IsLatticePolytope(P)` / `IsVeryAmple(P)` / `IsNormalPolytope(P)` | Core polytope predicates. | `[PKG, POLY, POLYTOPE]` |
| `IsSimplicial(P)` / `IsSimplexPolytope(P)` / `IsSimplePolytope(P)` / `IsReflexive(P)` | Structure/reflexivity predicates. | `[PKG, POLY, POLYTOPE]` |
| `IsFanoPolytope(P)` / `IsCanonicalFanoPolytope(P)` / `IsTerminalFanoPolytope(P)` / `IsSmoothFanoPolytope(P)` | Fano-family predicates. | `[PKG, POLY, POLYTOPE]` |
| `+(P1, P2)` / `*(n, P)` / `IntersectionOfPolytopes(P1, P2)` | Minkowski/scale/intersection operations. | `[PKG, POLY, POLYTOPE]` |
| `RandomInteriorPoint(P)` / `IsInteriorPoint(M, P)` | Interior-point witness/predicate operations. | `[PKG, POLY, POLYTOPE]` |

---

## 3. Source-Only Declared Surfaces (`[SRC]`)

These methods are declared in upstream `gap/*.gd` source but are not currently listed in the published manual index.

| Function | Declared source location | Notes | Tags |
|----------|--------------------------|-------|------|
| `ConeByGenerators(L)` | `gap/Cone.gd` | Additional cone constructor from generating rays. | `[PKG, POLY, CONE, SRC]` |
| `FactorConeEmbedding(C)` | `gap/Cone.gd` | Cone embedding helper attribute. | `[PKG, POLY, CONE, SRC]` |
| `RaysInFacets(C)` / `RaysInFaces(C)` | `gap/Cone.gd` | Cone incidence attributes. | `[PKG, POLY, CONE, SRC]` |
| `LinearSubspaceGenerators(C)` | `gap/Cone.gd` | Cone-associated linear-subspace generators. | `[PKG, POLY, CONE, SRC]` |
| `HasConvexSupport(C)` | `gap/Cone.gd` | Cone predicate not currently indexed in manual. | `[PKG, POLY, CONE, SRC]` |
| `SuperFan(C)` | `gap/Cone.gd` | Marked in source comments as internal-use helper. | `[PKG, POLY, CONE, SRC]` |
| `StarSubdivisionOfIthMaximalCone(F, i)` / `StarFan(C)` / `StarFan(C, F)` | `gap/Cone.gd` | Star-subdivision / star-fan operations. | `[PKG, POLY, CONE, FAN, SRC]` |
| `FanWithFixedRays(R, C)` / `DeriveFansFromTriangulation(R, require_regular)` | `gap/Fan.gd` | Additional fan-constructor surfaces. | `[PKG, POLY, FAN, SRC]` |
| `RaysInAllCones(F)` / `RaysInTheGivenMaximalCones(F)` / `GivenMaximalCones(F)` / `AllCones(F)` / `Rays(F)` / `PrimitiveCollections(F)` | `gap/Fan.gd` | Additional fan attributes not indexed. | `[PKG, POLY, FAN, SRC]` |
| `*(F1, F2)` / `ToricStarFan(F1, F2)` / `CanonicalizeFan(F)` / `MaximalCones(F, d)` | `gap/Fan.gd` | Fan operations including binary operator overload. | `[PKG, POLY, FAN, SRC]` |
| `FirstLessTheSecond(L1, L2)` / `OneMaximalConeInList(L)` / `ListOfMaximalConesInList(L)` | `gap/Fan.gd` | List-level fan helper operations. | `[PKG, POLY, FAN, SRC]` |
| `ContainingGrid(obj)` | `gap/ConvexObject.gd` | Shared convex-object attribute not manual-indexed. | `[PKG, POLY, SRC]` |
| `HomogeneousPointsOfPolyhedron(P)` / `IsNotEmpty(P)` | `gap/Polyhedron.gd` | Polyhedron surfaces declared but not indexed. | `[PKG, POLY, POLYH, SRC]` |
| `LatticePointsGenerators(P)` / `HasVertices(P)` / `BabyPolytope(P)` / `GaleTransform(M)` / `IsNotEmpty(P)` | `gap/Polytope.gd` | Polytope declarations absent from manual index. | `[PKG, POLY, POLYTOPE, SRC]` |
| `*(P1, P2)` / `*(P, n)` / `FreeSumOfPolytopes(P1, P2)` / `Points(L1, L2)` / `FourierProjection(P, m)` | `gap/Polytope.gd` | Additional overloaded/auxiliary polytope operations. | `[PKG, POLY, POLYTOPE, SRC]` |
| `SolutionPostIntMat(...)` / `AddIfPossible(...)` / `IfNotReducedReduceOnce(...)` / `ReduceTheBase(...)` | `gap/Cone.gd` | Global helper functions declared in source; not manual-indexed. | `[PKG, POLY, SRC]` |

---

## 4. Contract and Constraint Notes

- `FansFromTriangulation` and `FanFromTriangulation` are documented as available only when `TopcomInterface` is available.
- `SolveLinearProgram` is documented with `max_or_min` in `{"max", "min"}` and returns either a solution/objective pair or `fail`.
- `SolveEqualitiesAndInequalitiesOverIntergers` returns three matrices representing polytope points, Hilbert-basis cone part, and free part; optional `signs` is a 0/1 list matching variable count.
- NConvex is a polyhedral geometry package and does not encode arithmetic-lattice signature/genus/isometry contracts.

---

## 5. Sources

Canonical package/manually generated docs:

- NConvex package page: `https://homalg-project.github.io/NConvex/`
- NConvex manual contents: `https://homalg-project.github.io/NConvex/doc/chap0_mj.html`
- NConvex manual index: `https://homalg-project.github.io/NConvex/doc/chapInd_mj.html`
- NConvex manual chapter 3: `https://homalg-project.github.io/NConvex/doc/chap3_mj.html`
- NConvex manual chapter 4: `https://homalg-project.github.io/NConvex/doc/chap4_mj.html`
- NConvex manual chapter 5: `https://homalg-project.github.io/NConvex/doc/chap5_mj.html`
- NConvex manual chapter 6: `https://homalg-project.github.io/NConvex/doc/chap6_mj.html`
- NConvex manual chapter 7: `https://homalg-project.github.io/NConvex/doc/chap7_mj.html`

Source declarations used for source-only surfaces:

- `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/ConvexObject.gd`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Cone.gd`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Fan.gd`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Polyhedron.gd`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Polytope.gd`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/ZSolve.gd`
