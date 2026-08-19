# HyperCells Method Test Gap Checklist

Tracks HyperCells package methods documented in `docs/hypercells/lattice/research_readme.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Package Load Surface

- [ ] `LoadPackage("HyperCells")`

---

## 2. Object Constructors and Core Types

### 2.1 Constructors

- [ ] `TGCell(...)`
- [ ] `TGSuperCellModelGraph(...)`
- [ ] `TGSuperCell(...)`
- [ ] `HyperCell(...)`
- [ ] `TGCellSymmetric(...)`
- [ ] `TGCellSNF(...)`
- [ ] `TGCellMSNF(...)`
- [ ] `TGCellRat(...)`
- [ ] `TGSuperCellModelGraphSymmetric(...)`
- [ ] `TGSuperCellModelGraphSNF(...)`
- [ ] `TGSuperCellModelGraphMSNF(...)`
- [ ] `TGSuperCellModelGraphRat(...)`
- [ ] `TGSuperCellSymmetric(...)`
- [ ] `TGSuperCellSNF(...)`
- [ ] `TGSuperCellMSNF(...)`
- [ ] `TGSuperCellRat(...)`
- [ ] `TGCellModelGraph(...)`
- [ ] `TGCellGraph(...)`

### 2.2 Predicates and consistency

- [ ] `IsTGCell(...)`
- [ ] `IsTGSuperCell(...)`
- [ ] `IsHyperCell(...)`
- [ ] `IsTGSuperCellModelGraph(...)`
- [ ] `IsInternallyConsistent(...)`
- [ ] `IsCellGraph(...)`
- [ ] `IsSymmetricCellGraph(...)`
- [ ] `IsPrimitiveCellGraph(...)`
- [ ] `IsCenteredCellGraph(...)`
- [ ] `IsCell(...)`
- [ ] `IsSymmetricCell(...)`
- [ ] `IsPrimitiveCell(...)`
- [ ] `IsCenteredCell(...)`

---

## 3. Structural Attributes and Group Interfaces

### 3.1 Geometric and combinatorial attributes

- [ ] `Dimension(...)`
- [ ] `Center(...)`
- [ ] `Vertices(...)`
- [ ] `NumberOfVertices(...)`
- [ ] `Faces(...)`
- [ ] `NumberOfFaces(...)`
- [ ] `IsCompact(...)`
- [ ] `Position(...)`
- [ ] `DelaneySymbol(...)`
- [ ] `DelaneySymbolToDrawingCommands(...)`
- [ ] `ViewObj(...)`
- [ ] `ViewString(...)`
- [ ] `DisplayString(...)`
- [ ] `Draw(...)`

### 3.2 Group-level interfaces

- [ ] `Group(...)`
- [ ] `UnderlyingGroup(...)`
- [ ] `GroupHomomorphism(...)`
- [ ] `MatrixGroup(...)`
- [ ] `PointGroup(...)`
- [ ] `TranslationBasis(...)`
- [ ] `TorsionFreeSubgroup(...)`
- [ ] `IsomorphicTorsionFreeSubgroup(...)`
- [ ] `PointGroupRepresentatives(...)`
- [ ] `IsomorphismFpGroup(...)`
- [ ] `IsomorphismPcpGroup(...)`
- [ ] `IsomorphismMatrixGroup(...)`
- [ ] `IsomorphismAffineCrystGroup(...)`
- [ ] `IsomorphismPcpGroupToAffineCrystGroup(...)`
- [ ] `IsomorphismFpGroupToAffineCrystGroup(...)`

### 3.3 Quotient and relator surfaces

- [ ] `TGQuotientSequence(...)`
- [ ] `CellRelators(...)`
- [ ] `RelatorsAsMatrices(...)`
- [ ] `RelatorsAsTransformationPairs(...)`
- [ ] `PrimitiveCellRelators(...)`
- [ ] `PrimitiveRelatorsAsMatrices(...)`
- [ ] `PrimitiveRelatorsAsTransformationPairs(...)`

---

## 4. P1 Isosurface and Translation-Action APIs

- [ ] `Isosurface(...)`
- [ ] `PointGroupAsP1(...)`
- [ ] `FundamentalFamily(...)`
- [ ] `IsomorphismFpGroupToP1Group(...)`
- [ ] `IsomorphismP1GroupToFpGroup(...)`
- [ ] `IsomorphismPcpGroupToP1Group(...)`
- [ ] `IsomorphismP1GroupToPcpGroup(...)`
- [ ] `IsomorphismP1GroupToMatrixGroup(...)`
- [ ] `IsomorphismP1GroupToPointGroup(...)`
- [ ] `IsomorphismP1GroupToAffineCrystGroup(...)`

---

## 5. Supercell, Isomorphism, and Invariant Workflows

### 5.1 Primitive conversion and counting

- [ ] `PrimitiveCell(...)`
- [ ] `PrimitiveSuperCell(...)`
- [ ] `PrimitiveTranslationBasis(...)`
- [ ] `NumberOfCellVertices(...)`
- [ ] `NumberOfCellFaces(...)`
- [ ] `NumberOfHoles(...)`
- [ ] `NumberOfSurfaces(...)`
- [ ] `NumberOfWires(...)`
- [ ] `NumberOfSymmetricCells(...)`

### 5.2 Isomorphism and actions

- [ ] `TranslationAction(...)`
- [ ] `PointGroupAction(...)`
- [ ] `IsomorphismToStandardSymmetricCell(...)`
- [ ] `IsomorphismToStandardSuperCellModelGraph(...)`
- [ ] `IsomorphismToStandardCell(...)`
- [ ] `IsomorphismToStandardCellGraph(...)`
- [ ] `IsomorphicTransformation(...)`
- [ ] `IsEquivalentCell(...)`
- [ ] `IsIsomorphicCell(...)`
- [ ] `IsomorphicSuperCellModelGraph(...)`
- [ ] `IsomorphicCellGraph(...)`
- [ ] `IsomorphicSymmetricCell(...)`
- [ ] `IsomorphicCell(...)`
- [ ] `IsomorphicCellToCenteredCell(...)`
- [ ] `IsomorphicSymmetricCells(...)`
- [ ] `IsomorphicCellGraphs(...)`
- [ ] `IsomorphicCells(...)`
- [ ] `IsomorphicCellsToCentered(...)`
- [ ] `CommensuratorPointGroup(...)`

### 5.3 Cell/model graph conversion and invariants

- [ ] `CellInvariants(...)`
- [ ] `IsSelfDualPolygon(...)`
- [ ] `IsDual(...)`
- [ ] `IsSelfDual(...)`
- [ ] `ModelGraph(...)`
- [ ] `CellGraph(...)`
- [ ] `CellBoundary(...)`
- [ ] `AsTGSuperCellModelGraph(...)`
- [ ] `SymmetricModelGraph(...)`
- [ ] `TGCellMSNFs(...)`

---

## 6. Cell-Graph and Quotient-Sequence Utilities

### 6.1 Quotient-sequence and orbit helpers

- [ ] `ReducedTranslationGroup(...)`
- [ ] `RepresentativesCellGraphVertexOrbits(...)`
- [ ] `CoverOfQuotientSequence(...)`
- [ ] `IsIsomorphicQuotientSequence(...)`
- [ ] `IsomorphicQuotientSequence(...)`

### 6.2 Cell-graph geometry/combinatorics

- [ ] `IsoclinicSubspace(...)`
- [ ] `Stabilizer(...)`
- [ ] `ShiftVector(...)`
- [ ] `VertexBarycentreInCell(...)`
- [ ] `VertexBarycentreInCellGraph(...)`
- [ ] `EdgeVector(...)`
- [ ] `EdgeVectors(...)`
- [ ] `NumberOfCellGraphVertices(...)`
- [ ] `NumberOfCellGraphEdges(...)`
- [ ] `IsConnected(...)`
- [ ] `ConnectedComponentIndices(...)`
- [ ] `ConnectedComponents(...)`
- [ ] `IsStronglyConnected(...)`
- [ ] `StronglyConnectedComponents(...)`
- [ ] `IsLocallyStable(...)`
- [ ] `IsRegular(...)`
- [ ] `IsUniform(...)`
- [ ] `IsSemiequivelar(...)`
- [ ] `IsTileTransitive(...)`
- [ ] `IsEdgeTransitive(...)`
- [ ] `IsVertexTransitive(...)`
- [ ] `IsLoopless(...)`
- [ ] `HasMultipleEdges(...)`
- [ ] `IsSimple(...)`
- [ ] `IsTame(...)`

### 6.3 Graph coordinates and primitive cell graphs

- [ ] `CellGraphCoordinates(...)`
- [ ] `CellGraphInvariant(...)`
- [ ] `IsomorphismFpGroupToNQClass(...)`
- [ ] `IsomorphismNQClassToFpGroup(...)`
- [ ] `PrimitiveTGCellGraph(...)`
- [ ] `PrimitiveCellGraph(...)`
- [ ] `PrimitiveCellGraphCoordinates(...)`

---

## 7. Enumeration and Database Interfaces

### 7.1 Q-class and Z-class enumeration

- [ ] `TGQuotientSequencesFromInvariantLattices(...)`
- [ ] `TGSuperCells(...)`
- [ ] `NumberTGSuperCells(...)`
- [ ] `IsTGSuperCellModelGraphQClass(...)`
- [ ] `IsTGSuperCellQClass(...)`
- [ ] `TGSuperCellModelGraphQClass(...)`
- [ ] `TGSuperCellQClass(...)`
- [ ] `TGSuperCellModelGraphQClasses(...)`
- [ ] `TGSuperCellQClasses(...)`
- [ ] `TGSuperCellModelGraphQClassReps(...)`
- [ ] `TGSuperCellQClassReps(...)`
- [ ] `NumberTGSuperCellModelGraphQClasses(...)`
- [ ] `NumberTGSuperCellQClasses(...)`
- [ ] `NumberTGSuperCellModelGraphQClassReps(...)`
- [ ] `NumberTGSuperCellQClassReps(...)`
- [ ] `IsTGSuperCellModelGraphZClass(...)`
- [ ] `IsTGSuperCellZClass(...)`
- [ ] `TGSuperCellModelGraphZClass(...)`
- [ ] `TGSuperCellZClass(...)`
- [ ] `TGSuperCellModelGraphZClasses(...)`
- [ ] `TGSuperCellZClasses(...)`
- [ ] `TGSuperCellModelGraphZClassReps(...)`
- [ ] `TGSuperCellZClassReps(...)`
- [ ] `NumberTGSuperCellModelGraphZClasses(...)`
- [ ] `NumberTGSuperCellZClasses(...)`
- [ ] `NumberTGSuperCellModelGraphZClassReps(...)`
- [ ] `NumberTGSuperCellZClassReps(...)`
- [ ] `CellQClass(...)`
- [ ] `CellZClass(...)`
- [ ] `CellQClassRepresentative(...)`
- [ ] `CellZClassRepresentative(...)`

### 7.2 Database extraction and typed filters

- [ ] `TGCellMSNFsByType(...)`
- [ ] `TGCellMSNFsByTypeAndGenus(...)`
- [ ] `TGCellMSNFsByTypeAndSpecies(...)`
- [ ] `TGCellMSNFsByTypeAndSpeciesAndGenus(...)`
- [ ] `TGCellMSNFsByTypeAndSpeciesAndGenusAndLength(...)`
- [ ] `IsSparse(...)`
- [ ] `Dense(...)`
- [ ] `Sparse(...)`
- [ ] `TGCellModelGraphsByType(...)`
- [ ] `TGCellModelGraphsByTypeAndSpecies(...)`
- [ ] `TGCellModelGraphsByTypeAndSpeciesAndLength(...)`
- [ ] `TGCellGraphsByType(...)`
- [ ] `TGCellGraphsByTypeAndSpecies(...)`
- [ ] `TGCellGraphsByTypeAndSpeciesAndLength(...)`
- [ ] `TGCellSymmetriesByType(...)`
- [ ] `TGCellSymmetriesByTypeAndGenus(...)`
- [ ] `TGCellSymmetriesByTypeAndSpecies(...)`
- [ ] `TGCellSymmetriesByTypeAndSpeciesAndGenus(...)`
- [ ] `TGCellByTypeAndSpeciesAndGenusAndLength(...)`
- [ ] `CellRecord(...)`
- [ ] `CellModelGraphRecord(...)`
- [ ] `CellGraphRecord(...)`
- [ ] `CellSymmetryRecord(...)`
- [ ] `CellData(...)`
- [ ] `CellModelGraphData(...)`
- [ ] `CellGraphData(...)`
- [ ] `CellSymmetryData(...)`

### 7.3 Point-group representation families

- [ ] `IsFiniteMatrixGroup(...)`
- [ ] `PointGroupData(...)`
- [ ] `PointGroupName(...)`
- [ ] `IsTGCellPointGroupRep(...)`
- [ ] `TGCellPointGroupReps(...)`
- [ ] `NumberTGCellPointGroupReps(...)`
- [ ] `TGCellPointGroupRepsData(...)`
- [ ] `IsTGCellPointGroupQClass(...)`
- [ ] `TGCellPointGroupQClass(...)`
- [ ] `TGCellPointGroupQClasses(...)`
- [ ] `NumberTGCellPointGroupQClasses(...)`
- [ ] `IsTGCellPointGroupZClass(...)`
- [ ] `TGCellPointGroupZClass(...)`
- [ ] `TGCellPointGroupZClasses(...)`
- [ ] `NumberTGCellPointGroupZClasses(...)`
- [ ] `IsTGCellPointGroupFamily(...)`
- [ ] `TGCellPointGroupFamily(...)`
- [ ] `TGCellPointGroupFamilies(...)`
- [ ] `NumberTGCellPointGroupFamilies(...)`
- [ ] `IsTGCellPointGroupGenus(...)`
- [ ] `TGCellPointGroupGenus(...)`
- [ ] `TGCellPointGroupGenera(...)`
- [ ] `NumberTGCellPointGroupGenera(...)`
- [ ] `TGCellPointGroupByFamilyAndGenus(...)`

---

## 8. Export and Visualization Surfaces

- [ ] `TGCellModelGraphDisplay(...)`
- [ ] `TGCellDisplay(...)`
- [ ] `TGCellGraphDisplay(...)`
- [ ] `CellTo3DStructure(...)`
- [ ] `CellGraphTo3DStructure(...)`
- [ ] `CellGraphToPDBStructure(...)`

---

## Domain and Constraint Caveats

- HyperCells focuses on periodic cell complexes under translation-group/point-group workflows, including hyperbolic and Euclidean cases; it is not a standalone genus/discriminant-form classifier API.
- The package manual documents `simplifyMethod` options (`MaximalTree` default; `KnuthBendix` requiring optional package `kbmag`) for constructor/workflow calls that expose this option.
- The package homepage documents known current limits:
  - full support for all compact hyperbolic 3D orbifolds is not complete,
  - `TGCellGraph` does not yet support chiral and non-orientable orbifolds in dimensions greater than 3,
  - `boundByGenus` support for `TGCellMSNFsByTypeAndSpecies*` methods is currently restricted to type values less than 102.

---

## References

- `docs/hypercells/lattice/research_readme.md`
- `docs/hypercells/upstream/hypercells_online_provenance_2026-02-17.md`
- HyperCells package page: `https://gap-packages.github.io/HyperCells/`
- HyperCells package manual contents: `https://www.hypercells.net/chap0_mj.html`
- HyperCells package reference chapter 2: `https://www.hypercells.net/chap2_mj.html`
- HyperCells package reference chapter 3: `https://www.hypercells.net/chap3_mj.html`
- HyperCells package reference chapter 4: `https://www.hypercells.net/chap4_mj.html`
- HyperCells package reference chapter 5: `https://www.hypercells.net/chap5_mj.html`
- HyperCells package reference chapter 6: `https://www.hypercells.net/chap6_mj.html`
- HyperCells package reference chapter 7: `https://www.hypercells.net/chap7_mj.html`
- HyperCells package reference chapter 8: `https://www.hypercells.net/chap8_mj.html`
