# Task 1.2: Gram Matrices and Nikulin Invariants

## Theorem Statement

The Coble surface lattice S_Co and its orthogonal complement T_Co in the K3 lattice Λ_K3
satisfy:

1. S_Co ≅ ⟨2⟩ ⊕ ⟨-2⟩^10 with Gram matrix diag(2, -2, -2, ..., -2), signature (1,10),
   rank 11
2. T_Co has signature (2,9), rank 11, discriminant -2048 = -2^11
3. Both lattices are 2-elementary with discriminant groups A_S ≅ A_T ≅ (ℤ/2ℤ)^11
4. Nikulin invariants: (r,a,δ) = (11,11,1) for both S_Co and T_Co
5. Discriminant forms satisfy q_T ≅ -q_S (mod 2ℤ)
6. The embedding S_Co ↪ Λ_K3 is primitive

## Computational Verification

**Method**: Explicit Gram matrix construction, discriminant group computation, and
Nikulin invariant verification.

**Implementation**: `computations/task1_2_gram_matrices.sage`,
`task1_2_gram_matrices_fixed.sage`, `task1_2b_discriminant_forms.sage`

**Verification steps**:

1. **S_Co construction**: Define 11×11 diagonal Gram matrix with entries (2, -2, ...,
   -2) corresponding to basis {e₀, e₁, ..., e₁₀} where e₀ is the hyperplane class and
   e_i are exceptional divisors
2. **Signature verification**: Compute signature via quadratic form, verify (1,10)
3. **Discriminant group**: Compute A_S = S_Co*/S_Co, verify cardinality 2^11 = 2048 and
   structure (ℤ/2ℤ)^11
4. **Discriminant form**: Extract q_S gram matrix on Smith form generators, verify
   diagonal entries ±1/2 mod 2ℤ (hence δ=1)
5. **K3 lattice**: Construct Λ_K3 ≅ U³ ⊕ E₈(-1)² with signature (3,19), rank 22,
   determinant 1
6. **Orthogonal complement**: Compute T_Co = S_Co^⊥ in Λ_K3, verify signature (2,9),
   rank 11, determinant -2048
7. **Primitivity**: Verify gcd of all S_Co coordinates in Λ_K3 basis is 1
8. **Discriminant form duality**: Verify q_T ≅ -q_S via Brown invariant check:
   Brown(q_T) + Brown(q_S) ≡ 0 (mod 8)

**Results**: All three script variants confirm S_Co and T_Co have the expected Gram
matrices, signatures, and Nikulin invariants (11,11,1). The embedding is primitive and
discriminant forms are dual.

## Mathematical Context

**Nikulin invariants**: For a 2-elementary lattice L (discriminant group is 2-power
torsion), the triple (r,a,δ) consists of:
- r = rank of L
- a = rank of discriminant group A_L as ℤ/2ℤ-vector space
- δ = 0 if q_L takes values in ℤ/2ℤ, else δ = 1

**Nikulin's classification theorem** (Nikulin 1979, Theorem 1.14.2): A 2-elementary
lattice of signature (t⁺, t⁻) is determined up to isometry by (r,a,δ) and the signature.
For r > a, the genus contains a unique isometry class.

**Coble lattice structure**: The Picard lattice S_Co arises from blowing up P² at 10
nodes of a rational sextic.
The basis element e₀ = π*L has self-intersection 2 (sextic double cover), while
exceptional divisors e_i have self-intersection -2. The orthogonal complement T_Co is
the transcendental lattice.

**Discriminant form duality**: For a primitive sublattice S ⊂ Λ with Λ unimodular, the
discriminant forms of S and T = S^⊥ satisfy q_T ≅ -q_S. This is verified via the Brown
invariant: Brown(q_T) + Brown(q_S) ≡ 0 (mod 8).

**Literature**: Nikulin (1979) for 2-elementary lattice classification and discriminant
form theory. Dolgachev-Kondō (2013) for Coble surface lattice structure.\
**Pieroni connection** (Pieroni 2026, lines 146, 483-493): The lattice E₁₀ = k^⊥ ⊂
ℤ^{1,10} is identified as the numerical class group Num(X) for Coble surfaces, matching
S_Co structure. See `REFERENCES.md` for complete citations.

## Scope

This verification establishes that the repo's explicit Gram matrices for S_Co and T_Co
match the standard Coble surface lattice structure from the literature.
The Nikulin invariants (11,11,1) uniquely determine these lattices up to isometry within
their signature class.
The computation does not prove the existence of such lattices in principle (already
known from Nikulin's classification) but provides explicit worked examples with verified
invariants.

**Cross-references**:
- `notes/proofs/task1_1_sextic.md` — uses this lattice structure for Coble surface setup
- `REFERENCES.md` — Nikulin (1979), Dolgachev-Kondō (2013)
