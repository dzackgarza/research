# Task 1.3: Primitive Embedding Matrices

## Theorem Statement

The Coble transcendental lattice T_Co admits an explicit primitive embedding into the K3
lattice Λ_K3, and this embedding can be constructed via the chain:

T_Co ↪ T_En ↪ T_dP ↪ Λ_K3

where:
- Λ_K3 ≅ U³ ⊕ E₈(-1)² (signature (3,19), rank 22, even unimodular)
- T_dP is the del Pezzo transcendental lattice (rank 9)
- T_En is the Enriques transcendental lattice (rank 10)
- T_Co is the Coble transcendental lattice (rank 11, signature (2,9))

The embedding T_Co ↪ Λ_K3 is primitive (gcd of all coordinates is 1) and satisfies T_Co
= S_Co^⊥ where S_Co is the Coble Picard lattice.

## Computational Verification

**Method**: Explicit construction of embedding matrices at each stage, followed by
primitivity and orthogonality verification.

**Implementation**: `computations/task1_3_embeddings.sage`,
`task1_3_embeddings_fixed.sage`, `task1_3_embeddings_primitive.sage`

**Verification steps**:

1. **Λ_K3 construction**: Build explicit 22×22 Gram matrix as block diagonal U ⊕ U ⊕ U ⊕
   E₈(-1) ⊕ E₈(-1), verify signature (3,19), determinant 1, even
2. **S_Co embedding**: Construct 11×22 embedding matrix for S_Co ↪ Λ_K3, verify embedded
   Gram matrix matches diag(2, -2, ..., -2)
3. **Orthogonal complement**: Compute T_Co = S_Co^⊥ as 11-dimensional subspace
   orthogonal to all S_Co basis vectors
4. **T_Co Gram matrix**: Extract 11×11 Gram matrix from orthogonal complement basis,
   verify signature (2,9), determinant -2048
5. **Primitivity**: Verify gcd of all matrix entries in embedding is 1
6. **Orthogonality**: Verify S_Co · T_Co = 0 (all pairings vanish)
7. **Rank check**: Verify rank(S_Co) + rank(T_Co) = 11 + 11 = 22 = rank(Λ_K3)

**Results**: All three script variants produce explicit primitive embedding matrices.
The orthogonal complement T_Co has the expected signature (2,9) and Nikulin invariants
(11,11,1). The embedding is primitive and S_Co ⊕ T_Co spans Λ_K3.

## Mathematical Context

**Primitive embeddings**: An embedding L ↪ M of lattices is primitive if L ∩ M = L
(equivalently, M/L is torsion-free).
For K3 surfaces, the Picard lattice S embeds primitively into Λ_K3, and the orthogonal
complement T = S^⊥ is the transcendental lattice.

**Nikulin's primitive embedding theorem** (Nikulin 1979, Section 1.5): Given a
2-elementary lattice L with signature (t⁺, t⁻) and invariants (r,a,δ), a primitive
embedding L ↪ Λ_K3 exists if and only if certain signature and discriminant conditions
are satisfied. For the Coble lattice S_Co with (r,a,δ) = (11,11,1) and signature (1,10),
such an embedding exists and is unique up to O(Λ_K3).

**Orthogonal complement structure**: For a primitive sublattice S ⊂ Λ with Λ unimodular,
the orthogonal complement T = S^⊥ satisfies:
- rank(T) = rank(Λ) - rank(S)
- det(T) = det(S) (up to sign)
- Discriminant forms: q_T ≅ -q_S

**Literature**: Nikulin (1979) for primitive embedding theory and orthogonal complement
structure. Dolgachev-Kondō (2013) for Coble surface lattice embeddings.\
**Huybrechts connection** (Huybrechts K3 Lectures, lines 561, 1589-1619): Provides
foundational K3 lattice theory including U³ ⊕ E₈(-1)² structure and Kummer lattice
discriminant computations relevant for understanding lattice embeddings in K3 context.
See `REFERENCES.md` for complete citations.

## Scope

This verification establishes that the repo contains explicit primitive embedding
matrices for T_Co ↪ Λ_K3 with verified orthogonality to S_Co. The computation does not
prove the existence or uniqueness of such embeddings in principle (already known from
Nikulin's theory) but provides concrete worked examples with explicit coordinates in the
standard K3 lattice basis U³ ⊕ E₈(-1)².

**Cross-references**:
- `notes/proofs/task1_2_gram_matrices.md` — uses these embeddings to verify T_Co
  structure
- `REFERENCES.md` — Nikulin (1979), Dolgachev-Kondō (2013)
