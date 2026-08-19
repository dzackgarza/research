# Chapter 4 — Tight-binding Model Graphs

> Source: https://www.hypercells.net/HyperCells/doc/chap4_mj.html

## 4.1 Cell Model Graphs

Tight-binding models are defined on top of a cell graph. Model graph vertices are a subset of cell graph vertices; edges need not be a subset. Implemented as `TGCellModelGraph`.

Components:
- `GetTGCell` (4.3-4): associated `TGCell`
- `CellCenter` (4.3-3): cell center
- `ModelType` (4.3-5): identifier (tessellation, kagome, Lieb, etc.)
- `CellVertices` (4.3-7): sites of the tight-binding model
- `CellEdges` (4.3-9): hoppings with translations
- `CellFaces` (4.3-11): plaquettes

Edge tags follow the structure: `[ n, root ]` where `root` encodes the origin of the edge in the underlying cell graph.

## 4.2 Constructing Models

Options for all constructors:
- `simplify` (non-negative integer): level of word simplification
- `simplifyMethod` (string): `"BruteForce"` (default) or `"KnuthBendix"` (requires kbmag)

### 4.2-1 TGCellModelGraph( cellgraph, vfs, efs, ffs )
Constructs a model graph from a cell graph and specifications of which vertices define vertices, edges, and faces.

### 4.2-2 TessellationModelGraph( cellgraph [, dual ] )
Constructs a tessellation graph. If `dual` is true, constructs the dual tessellation.

### 4.2-3 AddOrientedNNNEdgesToTessellationModelGraph( model )
Adds oriented next-nearest-neighbor edges to a tessellation model graph.

### 4.2-4 KagomeModelGraph( cellgraph )
Constructs the p-kagome model graph for triangle group (2,3,p).
Model type: `[ "KAGOME", p, [ "VEF", [ [ 1 ], [ 2 ], [ 2, 3 ] ] ] ]`

### 4.2-5 LiebModelGraph( cellgraph [, dual ] )
Constructs a Lieb graph.

## 4.3 Model Properties

### 4.3-1 GetProperTriangleGroup( model )
### 4.3-2 CellRelators( model )
### 4.3-3 CellCenter( model )
Integer 1–3 indicating center vertex type (x, y, z of Schwarz triangle).

### 4.3-4 GetTGCell( model )
### 4.3-5 ModelType( model )
### 4.3-6 ModelName( model )
Friendly names:
- Derived: `"derived-model<[vfs,efs,ffs]>"`
- Tessellation: `"{p,q}-tess"`
- Kagome: `"p-kagome"`
- Lieb: `"{p,q}-Lieb"`

### 4.3-7 CellVertices( model )
Each vertex: `[ w, gi ]`.

### 4.3-8 CellVertexPositions( model )
### 4.3-9 CellEdges( model )
Each edge: `[ v1, v2, tag, gam ]` where `gam` is the translation γ such that g_ũ_{w'} = g_{u_w} γ.

### 4.3-10 CellEdgeTranslations( model )
### 4.3-11 CellFaces( model )

## 4.4 Export and Import

### 4.4-1 Exporting TGCellModelGraph Objects
- `Export( model, output-stream )`
- `Export( model, path )`
- `ExportString( model )`

### 4.4-2 Importing TGCellModelGraph Objects
- `ImportTGCellModelGraph( input-stream [, tg ] )`
- `ImportTGCellModelGraphFromFile( path [, tg ] )`
- `ImportTGCellModelGraphFromString( string [, tg ] )`
