# Utility Scripts Documentation

## Overview

Two utility scripts provide shared functionality across the Coble moduli computational
verification:

1. `computations/coble_geometry.sage` (197 lines): Central lattice constructions and
   verification functions
2. `computations/compare_stabilizers.sage` (105 lines): Stabilizer group comparison for
   multiple sextic examples

## coble_geometry.sage

**Purpose**: Provides canonical lattice definitions and verification utilities used
across all computational tasks.

**Key definitions**:
- `hyperbolic_plane()`: U with Gram matrix [[0,1],[1,0]]
- `E8_lattice(negative=True)`: E₈ root lattice (Cartan matrix), optionally negated
- `K3_lattice()`: Λ_K3 = U³ ⊕ E₈(-1)²
- `S_Co_gram()`: Coble Picard lattice diag(2, -2, ..., -2) (rank 11)
- `T_Co_gram()`: Coble transcendental lattice diag(2, 2, -2, ..., -2) (rank 11)
- `is_primitive_embedding(M, G_ambient, G_sub)`: Verify primitive embedding via gcd
  check
- `is_node(F, p)`: Verify A₁ singularity using 3×3 Hessian rank test

**Usage**: Imported by task1_1, task1_2, task1_3, task5_1 scripts for consistent lattice
construction.

**Literature context**: Lattice definitions follow Nikulin 1979 (2-elementary lattices),
Dolgachev-Kondō 2013 (K3 lattice structure), standard root lattice references.
**Pieroni connection** (Pieroni 2026, lines 146, 483-493): The E₁₀ framework for Coble
surfaces provides geometric interpretation for S_Co as Num(X) = E₁₀.

## compare_stabilizers.sage

**Purpose**: Verifies that the stabilizer group Γ_Co = Stab_{O(T_En)}(h_Co) ∩
Z_{O(T_En)}(θ) is abstractly isomorphic across different sextic examples.

**Method**:
1. Constructs T_En = diag(2, 2, -2, ..., -2) (rank 10)
2. Defines h_Co = [1, 0, ..., 0] (Coble polarization)
3. Defines θ = diag(1, 1, -1, ..., -1) (sign involution)
4. Enumerates reflection generators satisfying both stabilizer and centralizer
   conditions
5. Computes Cartan matrix from reflection roots

**Result**: 9 reflection generators with identical Cartan matrix for all generic
10-nodal rational sextics, confirming abstract isomorphism.

**Literature context**: Reflection groups (Nikulin 1980), arithmetic groups for lattices
with signature (2,n), period-domain stabilizers (Sterk 1991).

**Cross-references**: Used by task3_1 (stabilizer generators), conceptually related to
task6_1 (monodromy group structure).

## Verification Status

Both utility scripts provide foundational definitions and verification logic used
throughout the computational verification pipeline.
They are not standalone computational tasks but rather shared infrastructure referenced
by multiple task-specific scripts.

**Coverage**: All 10 solved proof notes implicitly rely on lattice definitions from
`coble_geometry.sage`. The stabilizer comparison logic from `compare_stabilizers.sage`
supports the abstract group structure claims in task3_1 and task6_1.
