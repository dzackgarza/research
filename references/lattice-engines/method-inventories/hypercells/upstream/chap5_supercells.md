# Chapter 5 — Supercells

> Source: https://www.hypercells.net/HyperCells/doc/chap5_mj.html

## 5.1 Supercell Model Graphs

Supercell model graphs describe the extension of a cell model graph to a supercell (Γ_pc/Γ_sc). Implemented as `TGSuperCellModelGraph`.

Components:
- `GetTGPrimitiveCell` (5.3-5): `TGCell` for primitive cell
- `GetTGSuperCell` (5.3-6): `TGCell` for supercell
- `CellCenter` (5.3-4): cell center
- `CellEmbedding` (5.3-14): embedding as `TGCellEmbedding`
- `ModelType` (5.3-8): model type identifier
- `CellVertices` (5.3-9): sites
- `CellVertexPositions` (5.3-10): positions as Δ⁺ elements
- `CellEdges` (5.3-11): hoppings with translations
- `CellFaces` (5.3-13): plaquettes

## 5.2 Constructing Supercell Models

### 5.2-1 TGSuperCellModelGraph( model, sc )
Constructs supercell model graph from model (`TGCellModelGraph`) and supercell (`TGCell`). The result is symmetric and connected.

### 5.2-2 RandomTGSuperCellModelGraph( model, scquotient [, GAMgens [, TDGAM [, TGAMs ]]] )
Constructs a random (potentially asymmetric) supercell model graph.

## 5.3 Supercell Model Properties

### 5.3-1 GetProperTriangleGroup( model )
### 5.3-2 PrimitiveCellRelators( model )
### 5.3-3 SuperCellRelators( model )
### 5.3-4 CellCenter( model )
### 5.3-5 GetTGPrimitiveCell( model )
### 5.3-6 GetTGSuperCell( model )
### 5.3-7 GetTGCell( model )
Alias for `GetTGSuperCell`.

### 5.3-8 ModelType( model )
### 5.3-9 CellVertices( model )
Each vertex: `[ w, gi, ti ]` where `ti` is the transversal index in Γ_pc/Γ_sc.

### 5.3-10 CellVertexPositions( model )
### 5.3-11 CellEdges( model )
Each edge: `[ v1, v2, tag, gam ]`. The tag is `[ v1pc, v2pc, tagpc ]` specifying the edge in the primitive cell.

### 5.3-12 CellEdgeTranslations( model )
### 5.3-13 CellFaces( model )
### 5.3-14 CellEmbedding( supercell-model )
Returns `TGCellEmbedding` object.

## 5.4 Embedding of the Primitive Cell in the Supercell

### 5.4-1 PrimitiveCellTranslationGroup( cellembed )
### 5.4-2 SuperCellTranslationGroup( cellembed )
### 5.4-3 AsQuotient( cellembed )
### 5.4-4 GetRightTransversal( cellembed )
### 5.4-5 TranslationGroupEmbedding( supercell-model )

## 5.5 Export and Import

### 5.5-1 Exporting TGSuperCellModelGraph Objects
- `Export( model, output-stream )`
- `Export( model, path )`
- `ExportString( model )`

### 5.5-2 Importing TGSuperCellModelGraph Objects
- `ImportTGSuperCellModelGraph( input-stream [, tg ] )`
- `ImportTGSuperCellModelGraphFromFile( path [, tg ] )`
- `ImportTGSuperCellModelGraphFromString( string [, tg ] )`
