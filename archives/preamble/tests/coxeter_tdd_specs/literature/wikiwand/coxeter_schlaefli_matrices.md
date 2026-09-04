# Coxeter and Schläfli Matrices - Wikiwand

**Source**: https://www.wikiwand.com/en/articles/Coxeter_group **Retrieved**: 2025-07-26 **Citation Key**: `wikiwand_coxeter_schlaefli_2025`

**Cited by**: `tests/coxeter_tdd_specs/unit/test_gram_matrices.py` (symmetry validation, A2 triangle example), `tests/coxeter_tdd_specs/system/test_classification_examples.py` (Schläfli matrix examples), `literature/citations/CITATION_INDEX.md`.

**Correction applied on capture** (see the A_2 example below): the capture as originally written negated every entry of the A_2 Schläfli matrix and every eigenvalue, and then read the negated spectrum through the un-negated classification rule stated three sections above it.
The entries and eigenvalues below are recomputed from the capture's own definition `C_ij = -2 cos(π/M_ij)`. The negated matrix is this project's Gram matrix `B = -C`, which is recorded in `literature/PROJECT_CONVENTIONS.md`, not the literature's Schläfli matrix.

## Matrix Definitions

### Coxeter Matrix M

- **Type**: n × n symmetric matrix

- **Diagonal entries**: Exclusively 1

- **Off-diagonal entries**: Values in {2, 3, 4, ...} ∪ {∞}

- **Interpretation**: M_ij encodes relation order between generators s_i and s_j

- **Special values**:

  - M_ij = 2: generators commute (s_i s_j = s_j s_i)

  - M_ij = 3: basic braid relation (s_i s_j s_i = s_j s_i s_j)

  - M_ij = ∞: no relation (infinite order)

### Schläfli Matrix C

- **Definition**: C_ij = -2 cos(π/M_ij)

- **Type**: Symmetric real matrix

- **Geometric interpretation**: Inner products of reflection normals, scaled by 2

- **Classification by eigenvalues**:

  - **All positive**: Finite Coxeter group

  - **All non-negative (≥1 zero)**: Affine Coxeter group

  - **Some negative**: Indefinite Coxeter group; hyperbolic (Lorentzian) exactly when one eigenvalue is negative and the rest positive

## Mathematical Relationship

The fundamental relationship connecting combinatorial and geometric aspects:

**Formula**: C_ij = -2 cos(π/M_ij)

This transforms:

- Combinatorial data (orders of relations) → Geometric data (angles)

- Discrete Coxeter matrix → Continuous Schläfli matrix

- Group presentation → Geometric realization

## Classification Theorem

**Eigenvalue Classification**:

1. **λ_i > 0 for all i**: Finite reflection group

2. **λ_i ≥ 0 for all i, ∃j: λ_j = 0**: Affine reflection group

3. **∃i: λ_i < 0**: Indefinite reflection group; Lorentzian (hyperbolic) when exactly one λ_i is negative and no λ_i is zero

## Examples

### A_2 (Triangular case)

- Coxeter matrix: M = [[1, 3], [3, 1]]

- Schläfli matrix: C = [[-2 cos(π/1), -2 cos(π/3)], [-2 cos(π/3), -2 cos(π/1)]]

- Simplifies to: C = [[2, -1], [-1, 2]]

- Eigenvalues: 1, 3 (both positive, so finite type)

- Determinant: 3

- **This project's Gram matrix**: B = 2 cos(π/M_ij) = -C = [[-2, 1], [1, -2]], eigenvalues -1 and -3, determinant 3. Finite type is negative definiteness of B. See `literature/PROJECT_CONVENTIONS.md`.

### Applications

- Determines geometric realization in Euclidean, affine, or hyperbolic space

- Fundamental for polytope theory and crystallography

- Key tool in Lie theory and algebraic geometry
