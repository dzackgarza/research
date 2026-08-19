# NConvex Method Test Gap Checklist

Tracks GAP `NConvex` package methods documented in `docs/archive/scope_violations/nconvex/lattice/nconvex_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Package Load Surface

- [ ] `LoadPackage("NConvex")`

---

## 2. Shared Convex-Object Surface

- [ ] `AmbientSpaceDimension(obj)`
- [ ] `ContainingGrid(obj)`
- [ ] `Dimension(obj)`
- [ ] `IsFullDimensional(obj)`
- [ ] `InteriorPoint(obj)`

---

## 3. Cones

### 3.1 Constructors

- [ ] `ConeByInequalities(L)`
- [ ] `ConeByEqualitiesAndInequalities(Eq, Ineq)`
- [ ] `ConeByGenerators(L)`
- [ ] `Cone(L)`
- [ ] `Cone(cdd_cone)`

### 3.2 Attributes and predicates

- [ ] `DefiningInequalities(C)`
- [ ] `EqualitiesOfCone(C)`
- [ ] `FactorConeEmbedding(C)`
- [ ] `DualCone(C)`
- [ ] `RaysInFacets(C)`
- [ ] `RaysInFaces(C)`
- [ ] `FacesOfCone(C)`
- [ ] `Facets(C)`
- [ ] `RelativeInteriorRay(C)`
- [ ] `HilbertBasis(C)`
- [ ] `HilbertBasisOfDualCone(C)`
- [ ] `LinearSubspaceGenerators(C)`
- [ ] `LinealitySpaceGenerators(C)`
- [ ] `ExternalCddCone(C)`
- [ ] `ExternalNmzCone(C)`
- [ ] `LatticePointsGenerators(C)`
- [ ] `GridGeneratedByCone(C)`
- [ ] `FactorGrid(C)`
- [ ] `FactorGridMorphism(C)`
- [ ] `GridGeneratedByOrthogonalCone(C)`
- [ ] `IsRegularCone(C)`
- [ ] `HasConvexSupport(C)`
- [ ] `IsRay(C)`
- [ ] `IsZero(C)`
- [ ] `SuperFan(C)`

### 3.3 Operations

- [ ] `FourierProjection(C, m)`
- [ ] `IntersectionOfCones(C1, C2)`
- [ ] `IntersectionOfCones(L)`
- [ ] `Contains(C1, C2)`
- [ ] `IsRelativeInteriorRay(L, C)`
- [ ] `*(n, C)`
- [ ] `*(A, C)`
- [ ] `NonReducedInequalities(C)`
- [ ] `StarSubdivisionOfIthMaximalCone(F, i)`
- [ ] `StarFan(C)`
- [ ] `StarFan(C, F)`

---

## 4. Fans

### 4.1 Constructors

- [ ] `Fan(F)`
- [ ] `Fan(C)`
- [ ] `Fan(R, C)`
- [ ] `FanWithFixedRays(R, C)`
- [ ] `DeriveFansFromTriangulation(R, require_regular)`
- [ ] `FansFromTriangulation(R)`
- [ ] `FanFromTriangulation(R)`

### 4.2 Attributes and predicates

- [ ] `RayGenerators(F)`
- [ ] `GivenRayGenerators(F)`
- [ ] `RaysInMaximalCones(F)`
- [ ] `MaximalCones(F)`
- [ ] `FVector(F)`
- [ ] `RaysInAllCones(F)`
- [ ] `RaysInTheGivenMaximalCones(F)`
- [ ] `GivenMaximalCones(F)`
- [ ] `AllCones(F)`
- [ ] `Rays(F)`
- [ ] `PrimitiveCollections(F)`
- [ ] `IsWellDefinedFan(F)`
- [ ] `IsComplete(F)`
- [ ] `IsPointed(F)`
- [ ] `IsSmooth(F)`
- [ ] `IsSimplicial(F)`
- [ ] `IsNormalFan(F)`
- [ ] `IsRegularFan(F)`
- [ ] `IsFanoFan(F)`

### 4.3 Operations

- [ ] `*(F1, F2)`
- [ ] `ToricStarFan(F1, F2)`
- [ ] `CanonicalizeFan(F)`
- [ ] `MaximalCones(F, d)`
- [ ] `FirstLessTheSecond(L1, L2)`
- [ ] `OneMaximalConeInList(L)`
- [ ] `ListOfMaximalConesInList(L)`

---

## 5. Polyhedra

### 5.1 Constructors

- [ ] `PolyhedronByInequalities(L)`
- [ ] `Polyhedron(P, C)`
- [ ] `Polyhedron(L, C)`
- [ ] `Polyhedron(P, L)`
- [ ] `Polyhedron(P_vertices, C_rays)`

### 5.2 Attributes and predicates

- [ ] `ExternalCddPolyhedron(P)`
- [ ] `ExternalNmzPolyhedron(P)`
- [ ] `DefiningInequalities(P)`
- [ ] `MainRatPolytope(P)`
- [ ] `MainPolytope(P)`
- [ ] `VerticesOfMainRatPolytope(P)`
- [ ] `VerticesOfMainPolytope(P)`
- [ ] `TailCone(P)`
- [ ] `RayGeneratorsOfTailCone(P)`
- [ ] `HomogeneousPointsOfPolyhedron(P)`
- [ ] `LatticePointsGenerators(P)`
- [ ] `BasisOfLinealitySpace(P)`
- [ ] `FVector(P)`
- [ ] `IsBounded(P)`
- [ ] `IsNotEmpty(P)`
- [ ] `IsPointed(P)`

### 5.3 Linear programming

- [ ] `SolveLinearProgram(P, max_or_min, target_func)`

---

## 6. Polytopes

### 6.1 Constructors

- [ ] `PolytopeByInequalities(L)`
- [ ] `Polytope(L)`

### 6.2 Attributes and predicates

- [ ] `ExternalCddPolytope(P)`
- [ ] `LatticePoints(P)`
- [ ] `RelativeInteriorLatticePoints(P)`
- [ ] `LatticePointsGenerators(P)`
- [ ] `VerticesOfPolytope(P)`
- [ ] `Vertices(P)`
- [ ] `HasVertices(P)`
- [ ] `DefiningInequalities(P)`
- [ ] `EqualitiesOfPolytope(P)`
- [ ] `FacetInequalities(P)`
- [ ] `VerticesInFacets(P)`
- [ ] `NormalFan(P)`
- [ ] `FaceFan(P)`
- [ ] `AffineCone(P)`
- [ ] `BabyPolytope(P)`
- [ ] `PolarPolytope(P)`
- [ ] `DualPolytope(P)`
- [ ] `GaleTransform(M)`
- [ ] `FVector(P)`
- [ ] `IsEmpty(P)`
- [ ] `IsNotEmpty(P)`
- [ ] `IsLatticePolytope(P)`
- [ ] `IsVeryAmple(P)`
- [ ] `IsNormalPolytope(P)`
- [ ] `IsSimplicial(P)`
- [ ] `IsSimplexPolytope(P)`
- [ ] `IsSimplePolytope(P)`
- [ ] `IsBounded(P)`
- [ ] `IsReflexive(P)`
- [ ] `IsFanoPolytope(P)`
- [ ] `IsCanonicalFanoPolytope(P)`
- [ ] `IsTerminalFanoPolytope(P)`
- [ ] `IsSmoothFanoPolytope(P)`

### 6.3 Operations

- [ ] `*(P1, P2)`
- [ ] `+(P1, P2)`
- [ ] `*(n, P)`
- [ ] `*(P, n)`
- [ ] `FreeSumOfPolytopes(P1, P2)`
- [ ] `IntersectionOfPolytopes(P1, P2)`
- [ ] `Points(L1, L2)`
- [ ] `FourierProjection(P, m)`
- [ ] `RandomInteriorPoint(P)`
- [ ] `IsInteriorPoint(M, P)`

---

## 7. Integer Solve Surface

- [ ] `SolveEqualitiesAndInequalitiesOverIntergers(eqs, eqs_rhs, ineqs, ineqs_rhs[, signs])`

---

## 8. Source-Only Helper Globals

Declared in `gap/Cone.gd` but not listed in the current manual index.

- [ ] `SolutionPostIntMat(...)`
- [ ] `AddIfPossible(...)`
- [ ] `IfNotReducedReduceOnce(...)`
- [ ] `ReduceTheBase(...)`

---

## Domain Caveats

- `NConvex` is a polyhedral-computation package (`cones`, `fans`, `polyhedra`, `polytopes`), not a quadratic-form signature/genus/isometry classifier API.
- `FansFromTriangulation` and `FanFromTriangulation` are documented as available only when `TopcomInterface` is available.
- `SolveLinearProgram` is documented with `max_or_min` in `{"max", "min"}`.
- `SolveEqualitiesAndInequalitiesOverIntergers` has a documented optional `signs` vector that constrains variable nonnegativity.

---

## References

- `docs/archive/scope_violations/nconvex/lattice/nconvex_lattice_reference.md`
- `docs/archive/scope_violations/nconvex/upstream/nconvex_online_provenance_2026-02-17.md`
- NConvex package page: `https://homalg-project.github.io/NConvex/`
- NConvex manual index: `https://homalg-project.github.io/NConvex/doc/chapInd_mj.html`
- NConvex manual contents: `https://homalg-project.github.io/NConvex/doc/chap0_mj.html`
- NConvex manual chapter 3 (convex-object attributes): `https://homalg-project.github.io/NConvex/doc/chap3_mj.html`
- NConvex manual chapter 4 (cones): `https://homalg-project.github.io/NConvex/doc/chap4_mj.html`
- NConvex manual chapter 5 (fans): `https://homalg-project.github.io/NConvex/doc/chap5_mj.html`
- NConvex manual chapter 6 (polyhedra and zsolve): `https://homalg-project.github.io/NConvex/doc/chap6_mj.html`
- NConvex manual chapter 7 (polytopes): `https://homalg-project.github.io/NConvex/doc/chap7_mj.html`
- NConvex source declarations:
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/ConvexObject.gd`
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Cone.gd`
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Fan.gd`
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Polyhedron.gd`
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Polytope.gd`
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/ZSolve.gd`
