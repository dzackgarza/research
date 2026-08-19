# Archived GAP Umbrella Checklist Sections (Out of Active Scope)

Archived from `docs/gap_methods_checklist.md` on 2026-02-18.

These sections are polyhedral/toric/LP-centered surfaces and are out of active bilinear-form lattice scope for this project.

### 2.2 4ti2Interface

- [ ] `LoadPackage("4ti2Interface")`
- [ ] `4ti2Interface_groebner_matrix(...)`
- [ ] `4ti2Interface_groebner_basis(...)`
- [ ] `4ti2Interface_hilbert_inequalities(...)`
- [ ] `4ti2Interface_hilbert_equalities_in_positive_orthant(...)`
- [ ] `4ti2Interface_hilbert_equalities_and_inequalities(...)`
- [ ] `4ti2Interface_zsolve_equalities_and_inequalities(...)`
- [ ] `4ti2Interface_graver_equalities(...)`

### 2.3 NormalizInterface

- [ ] `NmzCone(list)`
- [ ] `NmzCompute(cone[, props])`
- [ ] `NmzConeProperty(cone, property)`
- [ ] `NmzKnownConeProperties(cone)`
- [ ] `NmzHasConeProperty(cone, property)`
- [ ] `NmzGenerators(cone)`
- [ ] `NmzExtremeRays(cone)`
- [ ] `NmzSupportHyperplanes(cone)`
- [ ] `NmzHilbertBasis(cone)`
- [ ] `NmzHilbertSeries(cone)`
- [ ] `NmzHilbertQuasiPolynomial(cone)`
- [ ] `NmzTriangulation(cone)`
- [ ] `NmzTriangulationSize(cone)`
- [ ] `NmzTriangulationDetSum(cone)`
- [ ] `NmzLatticePoints(cone)`
- [ ] `NmzVerticesOfPolyhedron(cone)`

### 2.5 toric

- [ ] `InsideCone(...)`
- [ ] `InDualCone(...)`
- [ ] `PolytopeLatticePoints(...)`
- [ ] `Faces(...)`
- [ ] `ConesOfFan(...)`
- [ ] `NumberOfConesOfFan(...)`
- [ ] `ToricStar(...)`
- [ ] `DualSemigroupGenerators(...)`
- [ ] `EmbeddingAffineToricVariety(...)`
- [ ] `DivisorPolytope(...)`
- [ ] `DivisorPolytopeLatticePoints(...)`
- [ ] `RiemannRochBasis(...)`
- [ ] `EulerCharacteristic(...)`
- [ ] `BettiNumberToric(...)`
- [ ] `CardinalityOfToricVariety(...)`

### 2.6 CddInterface

- [ ] `Cdd_PolyhedronByInequalities(...)`
- [ ] `Cdd_PolyhedronByGenerators(...)`
- [ ] `Cdd_Canonicalize(P)`
- [ ] `Cdd_V_Rep(P)`
- [ ] `Cdd_H_Rep(P)`
- [ ] `Cdd_AmbientSpaceDimension(P)`
- [ ] `Cdd_Dimension(P)`
- [ ] `Cdd_GeneratingVertices(P)`
- [ ] `Cdd_GeneratingRays(P)`
- [ ] `Cdd_Equalities(P)`
- [ ] `Cdd_Inequalities(P)`
- [ ] `Cdd_Faces(P)`
- [ ] `Cdd_FacesWithFixedDimension(P, d)`
- [ ] `Cdd_Facets(P)`
- [ ] `Cdd_InteriorPoint(P)`
- [ ] `Cdd_FacesWithInteriorPoints(P)`
- [ ] `Cdd_FacesWithFixedDimensionAndInteriorPoints(P, d)`
- [ ] `Cdd_ExtendLinearity(P, V)`
- [ ] `Cdd_Lines(P)`
- [ ] `Cdd_Vertices(P)`
- [ ] `Cdd_IsEmpty(P)`
- [ ] `Cdd_IsCone(P)`
- [ ] `Cdd_IsLinSpace(P)`
- [ ] `Cdd_IsPointed(P)`
- [ ] `Cdd_IsContained(P1, P2)`
- [ ] `Cdd_Intersection(P1, P2)`
- [ ] `Cdd_LinearProgram(P, b)`
- [ ] `Cdd_FourierProjection(P, var)`
- [ ] `Cdd_FourierProjection([A, b], var)`
  - Caveat: complete CddInterface inventory and source links are archived in `docs/archive/scope_violations/cddinterface_methods_checklist.md` (out of active bilinear-form lattice scope).

### 2.7 NConvex package (detailed checklist surface)

- [ ] `ConeByInequalities(L)`
- [ ] `ConeByEqualitiesAndInequalities(Eq, Ineq)`
- [ ] `ConeByGenerators(L)`
- [ ] `Cone(L)`
- [ ] `Cone(cdd_cone)`
- [ ] `IntersectionOfCones(C1, C2)`
- [ ] `Contains(C1, C2)`
- [ ] `Fan(R, C)`
- [ ] `FansFromTriangulation(R)`
- [ ] `FanFromTriangulation(R)`
- [ ] `PolyhedronByInequalities(L)`
- [ ] `Polyhedron(P, C)`
- [ ] `SolveLinearProgram(P, max_or_min, target_func)`
- [ ] `PolytopeByInequalities(L)`
- [ ] `Polytope(L)`
- [ ] `LatticePoints(P)`
- [ ] `NormalFan(P)`
- [ ] `IntersectionOfPolytopes(P1, P2)`
- [ ] `SolveEqualitiesAndInequalitiesOverIntergers(eqs, eqs_rhs, ineqs, ineqs_rhs[, signs])`
  - Caveat: complete NConvex inventory (including source-only declarations not listed in current manual index) is maintained in `docs/archive/scope_violations/nconvex_methods_checklist.md`.
