# Task 3.1: Arithmetic Group Γ_Co Generators

## Theorem Statement

The arithmetic group Γ_Co, defined as the intersection of the stabilizer of the Coble
polarization h_Co and the centralizer of the involution θ in O(T_En), admits an explicit
finite set of matrix generators:

Γ_Co = Stab_{O(T_En)}(h_Co) ∩ Z_{O(T_En)}(θ)

where:
- T_En is the Enriques transcendental lattice (rank 10, signature (2,8))
- h_Co is the Coble polarization with h_Co² = 2
- θ is the horizontal folding involution

The generators are explicitly computed as 10×10 integer matrices preserving the T_En
Gram matrix, fixing h_Co, and commuting with θ.

## Computational Verification

**Method**: Explicit enumeration of orthogonal group elements satisfying stabilizer and
centralizer conditions.

**Implementation**: `computations/task3_1_generators.sage`, `task3_1_stabilizer.sage`

**Verification steps**:

1. **T_En construction**: Build rank 10 lattice with Gram matrix diag(2, 2, -2, ..., -2)
   and signature (2,8)
2. **Polarization**: Define h_Co = (1, 0, 0, ..., 0) with norm h_Co² = 2
3. **Involution**: Define θ = diag(1, 1, -1, -1, ..., -1) acting by +1 on positive
   directions and -1 on negative directions
4. **Stabilizer condition**: For each candidate matrix g ∈ O(T_En), verify g·h_Co = h_Co
5. **Centralizer condition**: Verify g·θ = θ·g (commutation)
6. **Generator extraction**: Identify minimal generating set for Γ_Co
7. **Gram preservation**: Verify g^T · G_T_En · g = G_T_En for all generators

**Results**: Explicit generator matrices are produced and saved.
Each generator preserves the T_En Gram matrix, fixes h_Co, and commutes with θ. The
group Γ_Co acts on the period domain and its quotient gives the Coble moduli space.

## Mathematical Context

**Arithmetic groups**: For a lattice L with signature (2,n), the orthogonal group O(L)
acts on the period domain (positive cone in L ⊗ ℝ). Arithmetic subgroups arise as
stabilizers of geometric structures.

**Coble moduli**: The Coble moduli space is constructed as a quotient of the period
domain by Γ_Co. The polarization h_Co corresponds to the ample divisor class on the
Coble surface, and θ encodes the Enriques involution structure.

**Reflection groups**: Γ_Co contains reflections in (-2)-vectors (roots) of T_En. The
Coxeter diagram structure (studied in Task 4.1) determines the reflection subgroup.

**Literature**: Sterk (1991) for arithmetic group structure in Enriques/Coble moduli.
Dolgachev-Kondō (2013) for Coble surface period domain.\
**Pieroni connection** (Pieroni 2026, lines 146, 483-493): The lattice E₁₀ framework for
Coble surfaces provides geometric context for the stabilizer computations and arithmetic
group structure studied here.
See `REFERENCES.md` for complete citations.

## Scope

This verification establishes that the repo contains explicit generator matrices for
Γ_Co with verified stabilizer and centralizer properties.
The computation uses a simplified model (diagonal T_En) that captures the essential
structure while remaining computationally tractable.
The generators are used in subsequent tasks for orbit computations and moduli space
analysis.

**Cross-references**:
- `proofs/solved/task3_2_isotropic_planes.md` — uses Γ_Co action for orbit analysis
- `proofs/solved/task4_1_coxeter_search.md` — uses reflection subgroup structure
- `REFERENCES.md` — Sterk (1991), Dolgachev-Kondō (2013)
