# Coxeter-Dynkin Diagrams Classification

**Source**: https://en.wikipedia.org/wiki/Coxeter%E2%80%93Dynkin_diagram **Retrieved**: 2025-07-26 **Citation Key**: `wikipedia_coxeter_dynkin_2025` **Revision**: oldid 1290398091 (last edited 14 May 2025), permanent link https://en.wikipedia.org/w/index.php?title=Coxeter%E2%80%93Dynkin_diagram&oldid=1290398091

**Cited by**: `tests/coxeter_tdd_specs/system/test_classification_examples.py`.

**Correction applied on capture**: the determinant rows below were captured without their rank restriction.
`det C` is the product of the eigenvalues, so its sign determines the type only in rank ≤ 2; `det C = 0` detects a radical in any rank.
In rank 4 a Schläfli form of signature (2,2) has `det C > 0` and is indefinite.
The source article states the determinant criterion for rank 2 explicitly and tags the general statement as unverified.

All statements here are in the literature convention `C_ij = -2 cos(π/M_ij)`; this project's Gram matrix is `B = -C` (`literature/PROJECT_CONVENTIONS.md`), which reverses every sign.

## Complete Classification by Type

### Finite Coxeter Groups (Elliptical)

- **Characterization**: Schläfli matrix positive definite (`det C > 0` decides this in rank ≤ 2)

- **Geometric Realization**: Spherical geometry

- **Examples**:

  - I₂(2): Two disconnected nodes (reducible)

  - I₂(3): Triangle diagram

  - I₂(4): Square diagram

  - I₂(5): Pentagonal diagram

  - I₂(6): Hexagonal diagram

  - Classical series: Aₙ, Bₙ, Dₙ

  - Exceptional: E₆, E₇, E₈, F₄, H₃, H₄, G₂

### Affine Coxeter Groups (Parabolic)

- **Characterization**: Schläfli matrix positive semidefinite with nontrivial radical; `det C = 0` in every rank

- **Geometric Realization**: Euclidean geometry

- **Key Example**: I₂(∞) representing parallel mirrors

- **Structure**: Extended Dynkin diagrams from finite types

- **Properties**: Infinite groups with finite quotients

### Hyperbolic Coxeter Groups

- **Characterization**: Schläfli matrix of Lorentzian signature (n-1, 1) — exactly one negative eigenvalue, none zero.
  In rank 2 this is `det C < 0`.

- **Geometric Realization**: Hyperbolic geometry

- **Subdivision**:

  1. **Compact**: All proper subgroups are finite

  2. **Paracompact**: Proper subgroups are finite or affine

- **Alternative Name**: Lannér groups (after F. Lannér's enumeration)

## Diagram Notation Conventions

### Node Representation

- **Nodes**: Represent mirrors/generators of reflections

- **Number of nodes**: Rank of the Coxeter group

### Edge Labeling

- **Unlabeled edges**: Order 3 relation (default)

- **Labeled edges**: Specific order relations

- **Order 2**: Can be omitted (generators commute)

- **Order ∞**: Dashed line (no finite relation)

### Mathematical Relationship

- **Coxeter Matrix M**: Encodes edge orders

- **Schläfli Matrix C**: C_ij = -2 cos(π/M_ij)

- **Classification**: Determined by the signature of C

## Applications

### Polytope Construction

- Coxeter-Dynkin diagrams generate uniform polytopes

- Finite types → spherical polytopes

- Affine types → Euclidean tilings

- Hyperbolic types → hyperbolic tilings

### Group Theory

- Diagrams encode presentation of Coxeter groups

- Subdiagrams correspond to parabolic subgroups

- Connected components give irreducible factors

## Key Theorems

### Classification Completeness

- **Finite types**: Completely classified (classical + exceptional)

- **Affine types**: Systematic extension of finite types

- **Hyperbolic types**: Enumerated but infinite in number

### Determinant Classification (rank 2 only, except the zero case)

1. det(C) > 0 ⟺ Finite type

2. det(C) = 0 ⟺ Affine type (valid in every rank: the radical is nontrivial)

3. det(C) < 0 ⟺ Hyperbolic type

Beyond rank 2 the classification is by the signature of C, not by the sign of its determinant.
