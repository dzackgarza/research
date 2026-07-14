---
name: lattice-theoretic-image-extraction
description: Use when extracting, reconstructing, or validating geometric diagrams governed by lattice geometry, toric geometry, Symington surgeries, or integral-affine structures from images or source figures.
---

# Lattice-Theoretic Geometric Extraction

This document explains the methodology for extracting and reproducing geometric diagrams in contexts governed by discrete lattice geometry (e.g., Toric geometry, Symington surgeries, Integral-Affine theory).

## Methodology

### 1. Lattice Coordinate System
Lattice-theoretic diagrams are defined by their relationship to an underlying discrete grid (usually $\mathbb{Z}^n$).
- **Establish a Frame**: Identify the primitive lattice basis (the unit steps of the grid) from the source image.
- **Pin the Origin**: Select a primary vertex as $(0,0)$ to anchor all subsequent measurements.
- **Vectorize Edges**: Represent all boundary segments as explicit lattice vectors $v_i$.
- **Coordinate Extraction**: Every significant point (vertex, surgery apex, intersection) can be explicitly identified by counting grid steps from the origin.

### 2. Geometric Primitives and Parameters
Decompose the diagram into its constituent mathematical primitives:
- **Identification**: Recognize building blocks such as rectangles, triangles, conics, or curves.
- **Parameter Extraction**: Compute or extract explicit integral parameters for these primitives (e.g., lattice side lengths, slopes of segments, foci of conics).

### 3. Containment and Partition Relationships
Formally map the structural relationships between primitives:
- **Partition**: Enumerate how a larger region is split into sub-regions (e.g., a rectangle partitioned by internal surgery triangles).
- **Containment**: Determine exactly which lattice nodes and primitives are contained within which regions.

### 4. Interpretation of Labels
Labels in these diagrams serve different semantic roles and must be analyzed accordingly:
- **Mathematical Data**: Literal coordinates, vectors, or dimensions to be plotted.
- **Construction Instructions**: Parameters that dictate geometric structure (e.g., surgery weights or multiplicities). 

### 5. Theoretical Inference
Refer to the theory being represented (e.g., Symington theory, Toric geometry) to infer geometric constraints that are mathematically "forced":
- **Constraint Resolution**: For example, a Symington surgery labeled with weight $k$ must be implemented as a union of $k$ basis triangles (each with Lattice Area 1 / Euclidean Area 0.5).
- **Forced Determination**: Use these theoretical constraints to uniquely determine the coordinates of apexes or bases that may not be explicitly labeled but are forced by the lattice geometry.
