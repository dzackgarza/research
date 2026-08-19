# HyperCells Lattice Methods Reference
## GAP package methods for triangle-group cells, supercells, and periodic cell-complex workflows

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PKG]` | HyperCells package method |
| `[CELL]` | Cell/supercell object construction and manipulation |
| `[GRAPH]` | Model-graph or cell-graph workflow |
| `[ENUM]` | Enumeration/classification/database extraction |
| `[GROUP]` | Group/point-group/isomorphism surface |
| `[EXPORT]` | Display/export surface |
| `[EUCLID]` | Euclidean regime |
| `[HYP]` | Hyperbolic regime |

---

## 1. Scope

HyperCells is a GAP package for unit-cell and periodic-cell-complex workflows driven by triangle groups,
with both Euclidean and hyperbolic surfaces. The package provides:

- constructors for cell, model-graph, and supercell objects,
- isomorphism and equivalence workflows over translation/point-group actions,
- enumeration/classification APIs (Q-class, Z-class, family/genus surfaces),
- database extraction helpers and 3D-structure export methods.

This package is lattice-related via translation-group and point-group cell-complex methods; it is not a standalone arithmetic genus/discriminant-form classification package.

---

## 2. Core Constructor Signatures (manual-backed)

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `TGCell(tg, quotient[, GAMgens[, TDGAM[, TGGw]]])` | `tg`: `ProperTriangleGroup` object; `quotient`: `TGQuotient` object; `GAMgens`: list (optional); `TDGAM`: (optional); `TGGw`: (optional) | `TGCell` object | Construct a primitive triangle-group cell from a proper triangle group and quotient. Optional arguments allow specifying generators, normal subgroup, and Wyckoff data. | `[PKG, CELL]` |
| `TGCellSymmetric(tg, quotient, center)` | `tg`: `ProperTriangleGroup`; `quotient`: `TGQuotient`; `center`: integer (1, 2, or 3 for Schwarz triangle vertices x, y, z) | `TGCell` object | Construct a symmetric triangle-group cell centered at a given vertex type. | `[PKG, CELL]` |
| `TGCellGraph(tg, quotient, center[, GAMgens[, TDGAM[, TGGw]]])` | `tg`: `ProperTriangleGroup`; `quotient`: `TGQuotient`; `center`: integer (1–3); `GAMgens`: list (optional); `TDGAM`: (optional); `TGGw`: (optional) | `TGCellGraph` object | Construct a cell graph (triangular tessellation of the translation unit cell) centered at a given vertex type. | `[PKG, CELL, GRAPH]` |
| `TGCellModelGraph(cellgraph, vfs, efs, ffs)` | `cellgraph`: `TGCellGraph`; `vfs`: list of vertex type indices (sites); `efs`: list of edge type indices (hoppings); `ffs`: list of face type indices (plaquettes) | `TGCellModelGraph` object | Construct a tight-binding model graph from a cell graph and vertex/edge/face specifications. | `[PKG, GRAPH]` |
| `TGSuperCellModelGraph(model, sc)` | `model`: `TGCellModelGraph`; `sc`: `TGCell` (supercell obtained from a quotient sequence) | `TGSuperCellModelGraph` object | Construct a symmetric, connected supercell model graph extending the primitive model to the supercell. | `[PKG, CELL, GRAPH]` |

Constructor notes from upstream docs (chap1, chap4):
- `simplify` and `simplifyMethod` are GAP keyword options (passed after `:` in GAP syntax), not positional arguments; they apply to `TGCellGraph`, `TGCellModelGraph`, `TGSuperCellModelGraph` and related constructors.
- `simplifyMethod` values: `"BruteForce"` (default) or `"KnuthBendix"` (requires optional package `kbmag`).
- `simplify` (non-negative integer): controls word-rewriting length; defaults to twice the number of generators if smaller.

---

## 3. Method Families and Contracts

### 3.1 Object attributes and predicates

Representative methods:

- predicates: `IsTGCell`, `IsTGSuperCell`, `IsHyperCell`, `IsTGSuperCellModelGraph`, `IsCellGraph`, `IsSymmetricCellGraph`, `IsPrimitiveCellGraph`, `IsCenteredCellGraph`, `IsCell`, `IsSymmetricCell`, `IsPrimitiveCell`, `IsCenteredCell`,
- attributes: `Dimension`, `Center`, `Vertices`, `NumberOfVertices`, `Faces`, `NumberOfFaces`, `IsCompact`, `Position`, `DelaneySymbol`,
- display: `ViewObj`, `ViewString`, `DisplayString`, `Draw`.

### 3.2 Group and isomorphism surfaces

Representative methods:

- group structure: `Group`, `GroupHomomorphism`, `MatrixGroup`, `PointGroup`, `TranslationBasis`, `TorsionFreeSubgroup`,
- conversion/isomorphism: `IsomorphicTorsionFreeSubgroup`, `PointGroupRepresentatives`, `IsomorphismFpGroup`, `IsomorphismPcpGroup`, `IsomorphismMatrixGroup`, `IsomorphismAffineCrystGroup`, `IsomorphismPcpGroupToAffineCrystGroup`, `IsomorphismFpGroupToAffineCrystGroup`,
- P1/isosurface conversion family: `Isosurface`, `PointGroupAsP1`, `FundamentalFamily`, `IsomorphismFpGroupToP1Group`, `IsomorphismP1GroupToFpGroup`, `IsomorphismPcpGroupToP1Group`, `IsomorphismP1GroupToPcpGroup`, `IsomorphismP1GroupToMatrixGroup`, `IsomorphismP1GroupToPointGroup`, `IsomorphismP1GroupToAffineCrystGroup`.

### 3.3 Supercell, graph, and invariants

Representative methods:

- primitive/supercell reductions: `PrimitiveCell`, `PrimitiveSuperCell`, `PrimitiveTranslationBasis`,
- action/equivalence: `TranslationAction`, `PointGroupAction`, `IsomorphicTransformation`, `IsEquivalentCell`, `IsIsomorphicCell`, `IsomorphicCell`, `IsomorphicCellGraph`, `IsomorphicSuperCellModelGraph`,
- invariants and boundaries: `CellInvariants`, `CellBoundary`, `CommensuratorPointGroup`,
- model graph and cell graph geometry: `ReducedTranslationGroup`, `CoverOfQuotientSequence`, `IsIsomorphicQuotientSequence`, `IsoclinicSubspace`, `Stabilizer`, `ShiftVector`, `CellGraphCoordinates`, `CellGraphInvariant`, `PrimitiveCellGraph`, `PrimitiveCellGraphCoordinates`.

### 3.4 Enumeration, database, and classification surfaces

Representative method families:

- Q-class and Z-class APIs for supercells:
  - `TGSuperCellModelGraphQClass*`, `TGSuperCellQClass*`, `TGSuperCellModelGraphZClass*`, `TGSuperCellZClass*`, plus `Number*` counters,
- database selectors:
  - `TGCellMSNFsByType*`, `TGCellModelGraphsByType*`, `TGCellGraphsByType*`, `TGCellSymmetriesByType*`, `TGCellByTypeAndSpeciesAndGenusAndLength`,
- point-group classes/families/genera:
  - `TGCellPointGroupReps*`, `TGCellPointGroupQClass*`, `TGCellPointGroupZClass*`, `TGCellPointGroupFamily*`, `TGCellPointGroupGenus*`, `TGCellPointGroupByFamilyAndGenus`.

### 3.5 Export surfaces

- `TGCellModelGraphDisplay`, `TGCellDisplay`, `TGCellGraphDisplay`,
- `CellTo3DStructure`, `CellGraphTo3DStructure`, `CellGraphToPDBStructure`.

---

## 4. Complete Method Index (from manual contents)

### 4.1 Chapter 2: HyperCells base types and interfaces

`TGCell`, `TGSuperCellModelGraph`, `TGSuperCell`, `HyperCell`, `ViewObj`, `ViewString`, `DisplayString`, `IsTGCell`, `IsTGSuperCell`, `IsHyperCell`, `IsTGSuperCellModelGraph`, `UnderlyingGroup`, `IsInternallyConsistent`, `Dimension`, `Center`, `Vertices`, `NumberOfVertices`, `Faces`, `NumberOfFaces`, `IsCompact`, `Position`, `DelaneySymbol`, `DelaneySymbolToDrawingCommands`, `Draw`, `Group`, `GroupHomomorphism`, `MatrixGroup`, `PointGroup`, `TranslationBasis`, `TorsionFreeSubgroup`, `IsomorphicTorsionFreeSubgroup`, `PointGroupRepresentatives`, `IsomorphismFpGroup`, `IsomorphismPcpGroup`, `IsomorphismMatrixGroup`, `Isosurface`, `PointGroupAsP1`, `FundamentalFamily`, `IsomorphismFpGroupToP1Group`, `IsomorphismP1GroupToFpGroup`, `IsomorphismPcpGroupToP1Group`, `IsomorphismP1GroupToPcpGroup`, `IsomorphismP1GroupToMatrixGroup`, `IsomorphismP1GroupToPointGroup`, `IsomorphismP1GroupToAffineCrystGroup`, `CellRelators`, `RelatorsAsMatrices`, `RelatorsAsTransformationPairs`

### 4.2 Chapter 3: Triangle-group cells and supercells

`TGCellSymmetric`, `TGCellSNF`, `TGCellMSNF`, `TGCellRat`, `TGQuotientSequence`, `TGCellMSNFs`, `TGSuperCellModelGraphSymmetric`, `TGSuperCellModelGraphSNF`, `TGSuperCellModelGraphMSNF`, `TGSuperCellModelGraphRat`, `AsTGSuperCellModelGraph`, `SymmetricModelGraph`, `IsCellGraph`, `IsSymmetricCellGraph`, `IsPrimitiveCellGraph`, `IsCenteredCellGraph`, `TGSuperCellSymmetric`, `TGSuperCellSNF`, `TGSuperCellMSNF`, `TGSuperCellRat`, `IsCell`, `IsSymmetricCell`, `IsPrimitiveCell`, `IsCenteredCell`, `PrimitiveCell`, `PrimitiveSuperCell`, `PrimitiveTranslationBasis`, `NumberOfCellVertices`, `NumberOfCellFaces`, `NumberOfHoles`, `NumberOfSurfaces`, `NumberOfWires`, `NumberOfSymmetricCells`, `TranslationAction`, `PointGroupAction`, `IsomorphismToStandardSymmetricCell`, `IsomorphismToStandardSuperCellModelGraph`, `IsomorphismToStandardCell`, `IsomorphismToStandardCellGraph`, `IsomorphicTransformation`, `IsEquivalentCell`, `IsIsomorphicCell`, `IsomorphicSuperCellModelGraph`, `IsomorphicCellGraph`, `IsomorphicSymmetricCell`, `IsomorphicCell`, `IsomorphicCellToCenteredCell`, `IsomorphicSymmetricCells`, `IsomorphicCellGraphs`, `IsomorphicCells`, `IsomorphicCellsToCentered`, `CommensuratorPointGroup`, `CellInvariants`, `IsSelfDualPolygon`, `IsDual`, `IsSelfDual`, `ModelGraph`, `CellGraph`, `CellBoundary`, `PrimitiveCellRelators`, `PrimitiveRelatorsAsMatrices`, `PrimitiveRelatorsAsTransformationPairs`, `IsomorphismFpGroup`, `IsomorphismPcpGroup`, `IsomorphismMatrixGroup`, `IsomorphismAffineCrystGroup`, `IsomorphismPcpGroupToAffineCrystGroup`, `IsomorphismFpGroupToAffineCrystGroup`

### 4.3 Chapter 4: Cell-graph model construction

`TGCellModelGraph`, `TGSuperCellModelGraph`, `ReducedTranslationGroup`, `RepresentativesCellGraphVertexOrbits`, `PointGroupRepresentatives`, `CoverOfQuotientSequence`, `IsIsomorphicQuotientSequence`, `IsomorphicQuotientSequence`, `TGCellGraph`, `IsoclinicSubspace`, `Stabilizer`, `ShiftVector`, `VertexBarycentreInCell`, `VertexBarycentreInCellGraph`, `EdgeVector`, `EdgeVectors`, `NumberOfCellGraphVertices`, `NumberOfCellGraphEdges`, `IsConnected`, `ConnectedComponentIndices`, `ConnectedComponents`, `IsStronglyConnected`, `StronglyConnectedComponents`, `IsLocallyStable`, `IsRegular`, `IsUniform`, `IsSemiequivelar`, `IsTileTransitive`, `IsEdgeTransitive`, `IsVertexTransitive`, `IsLoopless`, `HasMultipleEdges`, `IsSimple`, `IsTame`, `CellGraphCoordinates`, `IsomorphicCellGraphs`, `CellGraphInvariant`, `IsomorphismFpGroupToNQClass`, `IsomorphismNQClassToFpGroup`, `PrimitiveTGCellGraph`, `PrimitiveCellGraph`, `PrimitiveCellGraphCoordinates`, `IsomorphismFpGroup`, `IsomorphismPcpGroup`, `IsomorphismAffineCrystGroup`, `IsomorphismPcpGroupToAffineCrystGroup`, `IsomorphismFpGroupToAffineCrystGroup`

### 4.4 Chapter 5: Supercell enumeration

`TGQuotientSequencesFromInvariantLattices`, `TGSuperCells`, `NumberTGSuperCells`, `IsTGSuperCellModelGraphQClass`, `IsTGSuperCellQClass`, `TGSuperCellModelGraphQClass`, `TGSuperCellQClass`, `TGSuperCellModelGraphQClasses`, `TGSuperCellQClasses`, `TGSuperCellModelGraphQClassReps`, `TGSuperCellQClassReps`, `NumberTGSuperCellModelGraphQClasses`, `NumberTGSuperCellQClasses`, `NumberTGSuperCellModelGraphQClassReps`, `NumberTGSuperCellQClassReps`, `IsTGSuperCellModelGraphZClass`, `IsTGSuperCellZClass`, `TGSuperCellModelGraphZClass`, `TGSuperCellZClass`, `TGSuperCellModelGraphZClasses`, `TGSuperCellZClasses`, `TGSuperCellModelGraphZClassReps`, `TGSuperCellZClassReps`, `NumberTGSuperCellModelGraphZClasses`, `NumberTGSuperCellZClasses`, `NumberTGSuperCellModelGraphZClassReps`, `NumberTGSuperCellZClassReps`, `CellQClass`, `CellZClass`, `CellQClassRepresentative`, `CellZClassRepresentative`

### 4.5 Chapter 6: HyperCell database APIs

`TGCellMSNFsByType`, `TGCellMSNFsByTypeAndGenus`, `TGCellMSNFsByTypeAndSpecies`, `TGCellMSNFsByTypeAndSpeciesAndGenus`, `TGCellMSNFsByTypeAndSpeciesAndGenusAndLength`, `IsSparse`, `Dense`, `Sparse`, `TGCellModelGraphsByType`, `TGCellModelGraphsByTypeAndSpecies`, `TGCellModelGraphsByTypeAndSpeciesAndLength`, `TGCellGraphsByType`, `TGCellGraphsByTypeAndSpecies`, `TGCellGraphsByTypeAndSpeciesAndLength`, `TGCellSymmetriesByType`, `TGCellSymmetriesByTypeAndGenus`, `TGCellSymmetriesByTypeAndSpecies`, `TGCellSymmetriesByTypeAndSpeciesAndGenus`, `TGCellByTypeAndSpeciesAndGenusAndLength`, `CellRecord`, `CellModelGraphRecord`, `CellGraphRecord`, `CellSymmetryRecord`, `CellData`, `CellModelGraphData`, `CellGraphData`, `CellSymmetryData`

### 4.6 Chapter 7: Point-group representations

`IsFiniteMatrixGroup`, `PointGroupData`, `PointGroupName`, `IsTGCellPointGroupRep`, `TGCellPointGroupReps`, `NumberTGCellPointGroupReps`, `TGCellPointGroupRepsData`, `IsTGCellPointGroupQClass`, `TGCellPointGroupQClass`, `TGCellPointGroupQClasses`, `NumberTGCellPointGroupQClasses`, `IsTGCellPointGroupZClass`, `TGCellPointGroupZClass`, `TGCellPointGroupZClasses`, `NumberTGCellPointGroupZClasses`, `IsTGCellPointGroupFamily`, `TGCellPointGroupFamily`, `TGCellPointGroupFamilies`, `NumberTGCellPointGroupFamilies`, `IsTGCellPointGroupGenus`, `TGCellPointGroupGenus`, `TGCellPointGroupGenera`, `NumberTGCellPointGroupGenera`, `TGCellPointGroupByFamilyAndGenus`

### 4.7 Chapter 8: Visualization/export

`TGCellModelGraphDisplay`, `TGCellDisplay`, `TGCellGraphDisplay`, `CellTo3DStructure`, `CellGraphTo3DStructure`, `CellGraphToPDBStructure`

---

## 5. Constraints and Assumptions

- `simplifyMethod` option values in constructors/workflows are documented as `"BruteForce"` (default) and `"KnuthBendix"`; `"KnuthBendix"` requires optional package `kbmag`. Source: `docs/hypercells/upstream/TGCellGraph.gd` lines 66-69, `docs/hypercells/upstream/chap3_mj.html` line 443.
- Homepage limitations documented upstream:
  - complete support for compact hyperbolic 3D orbifolds is not yet complete,
  - `TGCellGraph` support for chiral/non-orientable orbifolds in dimensions greater than 3 is not complete,
  - `boundByGenus` support for `TGCellMSNFsByTypeAndSpecies` and `TGCellMSNFsByTypeAndSpeciesAndGenus` is currently implemented only for type values `< 102`.

---

## 6. Sources

- `docs/hypercells/upstream/hypercells_online_provenance_2026-02-17.md`
- HyperCells package page: `https://gap-packages.github.io/HyperCells/`
- HyperCells manual contents: `https://www.hypercells.net/chap0_mj.html`
- HyperCells manual chapter 2: `https://www.hypercells.net/chap2_mj.html`
- HyperCells manual chapter 3: `https://www.hypercells.net/chap3_mj.html`
- HyperCells manual chapter 4: `https://www.hypercells.net/chap4_mj.html`
- HyperCells manual chapter 5: `https://www.hypercells.net/chap5_mj.html`
- HyperCells manual chapter 6: `https://www.hypercells.net/chap6_mj.html`
- HyperCells manual chapter 7: `https://www.hypercells.net/chap7_mj.html`
- HyperCells manual chapter 8: `https://www.hypercells.net/chap8_mj.html`
