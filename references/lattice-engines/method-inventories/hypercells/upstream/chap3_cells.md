# Chapter 3 — Triangle-Group Cells

> Source: https://www.hypercells.net/HyperCells/doc/chap3_mj.html

## 3.1 Cells

A triangle-group cell is defined by the quotient group of Δ by a torsion-free normal subgroup Γ ◁ Δ⁺. Implemented as `TGCellObj` with components:

- `GetProperTriangleGroup` (3.2-1): the proper triangle group Δ⁺
- `CellRelators` (3.2-2): relators defining Δ⁺/Γ
- `TGCellTranslationGroup` (3.2-3): the translation group Γ
- `TGCellPointGroup` (3.2-4): the point group G⁺ ≅ Δ⁺/Γ
- `TGCellMSWPs` (3.2-6): maximally symmetric Wyckoff positions

Printed as: `TGCell( ProperTriangleGroup(r, q, p), rels )`

### 3.1-1 TGCell( tg, quotient [, GAMgens [, TDGAM [, TGGw ]]] )
Constructs a cell from triangle group and quotient.

### 3.1-2 TGCellSymmetric( tg, quotient, center )
Constructs a symmetric cell centered at a given vertex type.

## 3.2 Cell Properties

### 3.2-1 GetProperTriangleGroup( cell )
### 3.2-2 CellRelators( cell )
### 3.2-3 TGCellTranslationGroup( cell )
### 3.2-4 TGCellPointGroup( cell )
### 3.2-5 HasTGCellMSWPs( cell )
### 3.2-6 TGCellMSWPs( cell )

## 3.3 Schwarz Triangle Representative

### 3.3-1 TGCellSchwarzTriangleRep( cell )

## 3.4 Cell Translation Group

### 3.4-1 AsTGSubgroup( Gamma )
### 3.4-2 Generators( Gamma )
### 3.4-3 FpGroup( Gamma )
Returns as finitely presented group with generators `g1`, `g2`, ....
### 3.4-4 FpIsomorphism( Gamma )

## 3.5 Cell Point Group

### 3.5-1 AsQuotientGroup( G )
### 3.5-2 AsQuotient( G )
### 3.5-3 GetRightTransversal( G )
### 3.5-4 QuotientHomomorphism( G )

## 3.6 Maximally Symmetric Wyckoff Positions

### 3.6-1 AsQuotient( obj )
Returns the three quotients G⁺/G_w⁺ for w = x, y, z.

### 3.6-2 GetRightTransversal( obj )
### 3.6-3 GetKernel( obj )

## 3.7 Cell Graphs

Given a triangle-group quotient and a choice of center, the cell graph defines a maximally symmetric triangular tessellation of the compactified translation unit cell. Implemented as `TGCellGraph`.

Components:
- `GetTGCell` (3.7-12): associated `TGCell`
- `CellCenter` (3.7-4): center of cell graph
- `CellVertices` (3.7-5): vertices
- `CellEdges` (3.7-7): edges with translations
- `CellFaces` (3.7-9): oriented faces
- `CellBoundary` (3.7-11): boundary identifications

Printed as:
```
TGCellGraph( cell,
  center = w,
  vertices = [ [ w1, gi1 ], ... ],
  edges = [ [ v1, v2, s, gam ], ... ],
  faces = [ [ [ e1, o1 ], ... ], ... ],
  boundary = [ [ d1, d2, e, b, m, gam ], ... ]
)
```

### 3.7-1 TGCellGraph( tg, quotient, center [, GAMgens [, TDGAM [, TGGw ]]] )
Constructs a cell graph. `center` is integer 1–3 corresponding to vertices x, y, z of the Schwarz triangle.

### 3.7-2 GetProperTriangleGroup( cellgraph )
### 3.7-3 CellRelators( cellgraph )
### 3.7-4 CellCenter( cellgraph )
### 3.7-5 CellVertices( cellgraph )
Each vertex: `[ w, gi ]` with w = vertex type (1–3), gi = transversal index.

### 3.7-6 CellVertexPositions( cellgraph )
Vertex positions as elements of Δ⁺.

### 3.7-7 CellEdges( cellgraph )
Each edge: `[ v1, v2, s, gam ]`.

### 3.7-8 CellEdgeTranslations( cellgraph )
### 3.7-9 CellFaces( cellgraph )
Each face: ordered list of `[ edge, orientation ]` tuples.

### 3.7-10 CellFacesWithCenter( cellgraph )
Three lists of faces centered at x, y, z vertices.

### 3.7-11 CellBoundary( cellgraph )
Each boundary: `[ d1, d2, e, b, m, gam ]`.

### 3.7-12 GetTGCell( cellgraph )

### 3.7-13 Exporting TGCellGraph Objects
- `Export( cellgraph, output-stream )`
- `Export( cellgraph, path )`
- `ExportString( cellgraph )`

### 3.7-14 Importing TGCellGraph Objects
- `ImportTGCellGraph( input-stream [, tg ] )`
- `ImportTGCellGraphFromFile( path [, tg ] )`
- `ImportTGCellGraphFromString( string [, tg ] )`
