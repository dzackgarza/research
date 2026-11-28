# Technical Audit Report: Task 5.1 θ Involution Construction

**Date**: 2026-03-27\
**Task**: Construct explicit involution θ on Λ_K3 = U³ ⊕ E₈(-1)² with specified
eigenspaces\
**Status**: FAILED — eigenspaces not orthogonal, θ not an isometry

* * *

## Executive Summary

The Task 5.1 implementation attempted to construct an involution θ on the K3 lattice by
constructing explicit embedding matrices for T_Co and S_Co, then defining θ via a
change-of-basis from the eigenbasis.
This approach failed because **the chosen embeddings M_T_plus and M_S_minus are not
orthogonal to each other**, and consequently the resulting matrix does not preserve the
bilinear form on Λ_K3.

This report provides the mathematically correct criterion for the construction,
distinguishes automatic vs.
non-automatic properties, specifies computational verification conditions, and
identifies the failure mode.

* * *

## (A) Mathematical Criterion for Correct θ Construction

### Theorem (Nikulin, 1979)

Let Λ be an even unimodular lattice of signature (t⁺, t⁻). Let S ⊂ Λ be a primitive
sublattice of signature (s⁺, s⁻) and let T = S^⊥ be its orthogonal complement.
Define an involution θ : Λ ⊗ ℚ → Λ ⊗ ℚ by:

```
θ|_T = +1 (identity)
θ|_S = -1 (negation)
```

Then θ extends to an **isometry** of Λ (i.e., θ ∈ O(Λ)) if and only if:

1. **Orthogonality**: S ⊥ T in Λ — this is automatic from the definition of orthogonal
   complement
2. **Integral action**: θ(Λ) ⊂ Λ — equivalently, Λ is θ-invariant
3. **Self-adjointness**: For the bilinear form B on Λ, B(θv, w) = B(v, θw) for all v, w
   ∈ Λ

### Key Invariants

For the Coble case:
- Λ_K3 has signature (3, 19), rank 22, even, unimodular
- S_Co (coinvariant) has signature (1, 10), rank 11, even, det = 2048 = 2¹¹
- T_Co (fixed) has signature (2, 9), rank 11, even, det = -2048 = -2¹¹

### Discriminant Form Compatibility

The critical condition is the **gluing isomorphism** between discriminant groups:

```
A_S ≅ A_T
q_S ≅ -q_T
```

where (A_S, q_S) and (A_T, q_T) are the discriminant quadratic forms.
This follows from the unimodularity of Λ = S ⊕ T (modulo gluing): since Λ is unimodular,
the discriminant forms must be opposite.

**Verification**:
- |A_S| = |A_T| = 2048 = 2¹¹
- Both discriminant groups are isomorphic to (ℤ/2ℤ)¹¹
- The discriminant form q_S has type (1, 10) and q_T has type (2, 9); they should be
  negatives of each other

### Necessary and Sufficient Conditions

The construction θ = (+1 on T, -1 on S) yields an element of O(Λ_K3) if and only if:

1. **S is a primitive sublattice of Λ_K3** — this guarantees S^⊥ is well-defined as a
   saturated sublattice
2. **S ⊥ T** — automatic from complement construction
3. **θ(Λ) ⊂ Λ** — equivalently, the eigenspaces intersect Λ in full-rank lattices
4. **The discriminant forms satisfy q_S ≅ -q_T** — follows from unimodularity of Λ

* * *

## (B) Automatic vs. Non-Automatic Properties

### Automatic from Primitivity in a Unimodular Lattice

| Property | Status | Explanation |
| --- | --- | --- |
| S^⊥ exists as saturated sublattice | **Automatic** | In a unimodular lattice, the orthogonal complement of a primitive sublattice is primitive (Nikulin, Thm. 1.6.2) |
| rank(S) + rank(T) = rank(Λ) | **Automatic** | Orthogonal complement in non-degenerate lattice |
| Signature decomposition | **Automatic** | Witt decomposition: signature adds componentwise |
| Discriminant group orders multiply to 1 | **Automatic** | det(S) · det(T) = det(Λ) = ±1, so \|A_S\| · \|A_T\| = 1 |
| q_S ≅ -q_T | **Automatic** | Follows from unimodularity: the discriminant form of a direct sum is the orthogonal sum, and Λ has trivial discriminant form |

### NOT Automatic (Must Be Verified or Constructed)

| Property | Status | Explanation |
| --- | --- | --- |
| Orthogonality of S and T in Λ | **Must verify** | The current code used embeddings that are NOT orthogonal |
| Integral eigenspaces: V_± ∩ Λ are full rank | **Must verify** | Requires that θ respects Λ, not just Λ ⊗ ℚ |
| θ ∈ O(Λ) (preserves bilinear form) | **Must verify** | The failed check: θ^T G θ = G |
| Self-adjointness | **Must verify** | Equivalent to orthogonality of eigenspaces for symmetric matrices |

### What Went Wrong in Task 5.1

The code constructed embedding matrices M_T_plus and M_S_minus that:
- Each have rank 11 and correct Gram diagonals
- BUT their column spaces are NOT orthogonal in Λ_K3

This violates condition (2) in the "NOT Automatic" table.
The resulting θ fails the fundamental test θ^T G θ = G.

* * *

## (C) Computational Verification Checklist

The corrected implementation must verify ALL of the following:

### Step 1: Primitive Embedding Verification

```python
# Verify S_Co → Λ_K3 is primitive
def verify_primitive_embedding(M, L_gram):
    """M is n×k integer matrix, L_gram is k×k Gram of ambient lattice."""
    n, k = M.nrows(), M.ncols()
    # Compute saturation: (span_ℚ(M) ∩ Z^n)
    saturation = saturate_embedding(M, L_gram)
    # Check saturation has same rank as M
    return saturation.rank() == k
```

### Step 2: Orthogonal Complement Computation

```python
def compute_orthogonal_complement(M, L_gram):
    """
    Compute basis for {v ∈ L : v ⟂ all columns of M}.
    Returns matrix whose columns span T = S^⊥.
    """
    # Solve M^T * L_gram * x = 0
    # This gives the orthogonal complement in the dual
    G = L_gram
    # Nullspace of M^T * G
    A = M.transpose() * G
    nullbasis = A.kernel().basis_matrix()
    # Convert from dual coordinates back to ambient
    return nullbasis * G
```

### Step 3: Orthogonality Verification

```python
def verify_orthogonality(M_S, M_T, L_gram):
    """Verify column spaces of M_S and M_T are orthogonal in L."""
    cross = M_S.transpose() * L_gram * M_T
    return cross.is_zero()
```

### Step 4: Isometry Verification

```python
def verify_theta_is_isometry(theta, L_gram):
    """Verify θ ∈ O(L): θ^T G θ = G."""
    return (theta.transpose() * L_gram * theta == L_gram)

def verify_self_adjoint(theta, L_gram):
    """Verify θ is self-adjoint: G θ = θ^T G."""
    return (L_gram * theta == theta.transpose() * L_gram)
```

### Step 5: Discriminant Form Compatibility

```python
def verify_discriminant_compatibility(L_plus_gram, L_minus_gram):
    """Verify q_{L_plus} ≅ -q_{L_minus} on discriminant groups."""
    L_plus = IntegralLattice(L_plus_gram)
    L_minus = IntegralLattice(L_minus_gram)

    A_plus = L_plus.discriminant_group()
    A_minus = L_minus.discriminant_group()

    # Check orders match
    assert A_plus.order() == A_minus.order()

    # Compute quadratic forms
    q_plus = A_plus.gram_matrix_quadratic()
    q_minus = A_minus.gram_matrix_quadratic()

    # Check q_plus + q_minus = 0 (mod 1)
    return (q_plus + q_minus).is_zero()
```

### Step 6: Full Verification Suite

```python
def full_theta_verification():
    """Run all verifications for θ construction."""
    results = {}

    # 1. Load lattices
    Lambda_K3 = get_Lambda_K3()
    G = Lambda_K3.gram_matrix()
    T_Co = get_T_Co()
    S_Co = get_S_Co()

    # 2. Find primitive embedding of S_Co → Λ_K3
    # (must be computed, not assumed)
    M_S = find_primitive_embedding(S_Co, Lambda_K3)
    results['S_primitive'] = verify_primitive_embedding(M_S, G)

    # 3. Compute orthogonal complement
    M_T = compute_orthogonal_complement(M_S, G)
    results['T_complement'] = verify_orthogonal_complement(M_T, G)

    # 4. Verify orthogonality
    results['orthogonal'] = verify_orthogonality(M_S, M_T, G)

    # 5. Construct θ
    P = M_T.augment(M_S)
    theta = P * block_diagonal([identity_matrix(11), -identity_matrix(11)]) * P.inverse()
    results['involution'] = (theta^2 == identity_matrix(22))

    # 6. Verify θ ∈ O(Λ_K3)
    results['isometry'] = verify_theta_is_isometry(theta, G)
    results['self_adjoint'] = verify_self_adjoint(theta, G)

    # 7. Verify eigenspace lattices
    V_plus = M_T.column_space()  # +1 eigenspace
    V_minus = M_S.column_space()  # -1 eigenspace

    results['eigenspace_orthogonal'] = V_plus.is_orthogonal(V_minus)
    results['eigenspace_T'] = (V_plus.gram() == T_Co.gram())
    results['eigenspace_S'] = (V_minus.gram() == S_Co.gram())

    return results
```

* * *

## (D) Failure Mode Analysis

### Root Cause

The Task 5.1 code constructed embedding matrices M_T_plus and M_S_minus **by inspection
of the standard basis**, picking specific vectors of the correct norms but **not
verifying or ensuring orthogonality between the two column spaces**.

Specifically:

```python
# Current code (incorrect):
M_T_plus[0, 0] = 1   # t_0 in U_0
M_T_plus[1, 0] = 1
M_T_plus[4, 0] = 1   # s_0 in U_2 (MISTAKE: overlaps with S_Co space)
M_T_plus[5, 0] = 1
```

The cross-term matrix computed in the audit shows non-zero entries at positions (3,4),
(4,5), etc., indicating the chosen basis vectors are not orthogonal.

### Why This Fails

For θ to be an isometry, we need:
- V_+ ⟂ V_- (eigenspaces orthogonal)
- θ^T G θ = G (form preservation)

The current code enforced neither.
It merely ensured:
- dim(V_+) = dim(V_-) = 11 (achieved)
- Each eigenspace has the correct Gram diagonal (achieved)

But without orthogonality, the induced quadratic forms on the eigenspaces are not the
original T_Co and S_Co — they are **twisted** by the non-orthogonal cross-terms.

### Evidence from Audit Output

```
θ^T G θ = G: False
V_+ ⟂ V_-: False

Cross-term matrix V_+ G V_-^T:
[0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 1 0 0 0 0 0 0 0]   # ← non-zero!
[0 0 0 1 1 0 0 0 0 0 0]   # ← non-zero!
...
```

### The Correct Approach

1. **Find a primitive embedding** of S_Co into Λ_K3 — this is a non-trivial
   computational problem requiring lattice reduction or Nikulin's embedding theorem
2. **Compute the orthogonal complement** T_Co = S_Co^⊥ automatically
3. **Verify** S ⊥ T (orthogonality is guaranteed by construction)
4. **Define θ** = +1 on T, -1 on S — this automatically gives θ ∈ O(Λ_K3)

The key insight is that **orthogonality is built into the construction**, not added
afterward.
By computing T as the orthogonal complement of a primitive S, we guarantee V_+
⟂ V_-.

* * *

## Recommendations

### Immediate Fix

1. Implement `find_primitive_embedding(S_Co, Lambda_K3)` using:
   - LLL reduction on candidate vectors
   - Nikulin's criterion for primitive embeddings
   - Exhaustive search for small rank cases

2. Replace the manual embedding construction with:
   ```python
   M_S = find_primitive_embedding(S_Co, Lambda_K3)
   M_T = compute_orthogonal_complement(M_S, Lambda_K3_gram)
   # Verify orthogonality
   assert verify_orthogonality(M_S, M_T, Lambda_K3_gram)
   ```

3. Construct θ from verified orthogonal decomposition

### Long-term Improvements

1. Add unit tests verifying θ ∈ O(Λ_K3) as part of the construction
2. Implement discriminant form computation and compatibility checks
3. Consider using SageMath's `QuadraticForm` and `IntegralLattice` classes more
   extensively rather than raw matrix operations

* * *

## References

- Nikulin, V. V. (1979). Integer symmetric bilinear forms and some of their geometric
  applications. *Math.
  USSR Izvestiya*, 14(1), 103-167.
- Conway, J. H., & Sloane, N. J. A. (1999). *Sphere Packings, Lattices and Groups* (3rd
  ed.). Springer.
- Scattone, F. (1987). On the compactification of moduli spaces for algebraic K3
  surfaces. *Memoirs of the AMS*, 70(374).
