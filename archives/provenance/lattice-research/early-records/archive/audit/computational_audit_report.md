# Computational Audit Report: Mathematical Correctness Review

**Date:** 2026-03-25  
**Auditor:** Mathematical Prover Researcher  
**Files Reviewed:**

- `computations/task1_1_sextic.sage`
- `computations/task1_2_gram_matrices.sage`
- `computations/task1_3_embeddings.sage`

---

## Executive Summary

**Overall Assessment:** ⚠️ **PARTIALLY SOUND** — Critical mathematical gaps identified

The scripts demonstrate good computational structure but contain **significant mathematical issues** that undermine the rigor of the claimed results. The most serious problems are:

1. **Task 1.1:** Insufficient verification that all singularities are nodes (Hessian test incomplete)
2. **Task 1.2:** T_Co is **constructed by fiat** rather than computed as orthogonal complement
3. **Task 1.3:** Embeddings are **not rigorously constructed** — orthogonality claims unverified

---

## Detailed Analysis

### 1. Task 1.1: Sextic Curve Construction (`task1_1_sextic.sage`)

**Claim:** Construct sextic F(x,y,z) = 0 with exactly 10 nodes.

#### ✓ Correct Elements:

- Parametrization approach is valid (generic degree-6 polynomials give rational sextic)
- Implicit equation via resultants is the correct method
- Affine chart z=1 plus line at infinity z=0 covers all of ℙ²
- Genus formula application is correct: g = g_a - Σδ = 10 - 10 = 0

#### ⚠️ **CRITICAL ISSUES:**

**Issue 1.1a: Hessian Test is Incomplete**

The script tests whether singularities are nodes by computing:

```python
disc = F_xx(p) * F_yy(p) - F_xy(p)²
```

**Problem:** This is the discriminant of the **affine** Hessian in the chart z=1. For a singularity to be a node (A₁), the **projective** Hessian must be nondegenerate.

**Mathematical Requirement:** A point p ∈ ℙ² is a node iff the Hessian matrix of second partial derivatives has rank 2 (not rank < 2). The full Hessian is the 3×3 matrix:

$$H(F)(p) = \begin{pmatrix} F_{xx} & F_{xy} & F_{xz} \\ F_{yx} & F_{yy} & F_{yz} \\ F_{zx} & F_{zy} & F_{zz} \end{pmatrix}$$

**The script only checks the 2×2 minor** `F_xx * F_yy - F_xy²`, which is insufficient. A singularity could have:

- degenerate affine Hessian (disc = 0) but still be a node in ℙ²
- nondegenerate affine Hessian but be a worse singularity (e.g., cusp)

**Correct Test:** Verify that the **full 3×3 Hessian has rank 2** at each singular point. For a homogeneous polynomial of degree d, at a singular point where F_x = F_y = F_z = 0, the Hessian criterion for an A₁ singularity is that the Hessian matrix has rank exactly 2 (one zero eigenvalue due to Euler relation, but no more).

**Issue 1.1b: No Verification of Irreducibility**

The script extracts "the sextic factor" but doesn't verify:

- The sextic is **irreducible** (could be union of lower-degree curves)
- The sextic is **reduced** (could have multiple components)

**Mathematical Requirement:** A Coble surface requires an **irreducible** rational sextic. If F factors, the geometric genus computation is invalid.

**Fix Required:**

```python
# Add irreducibility check
assert F.is_irreducible(), "Sextic must be irreducible for Coble surface"
```

**Issue 1.1c: No Multiplicity Check at Singularities**

The script assumes all singularities found are isolated nodes, but doesn't verify:

- Each singularity has **multiplicity exactly 2** (required for nodes)
- There are **no non-isolated singularities** (e.g., singular curves)

**Mathematical Requirement:** A node is an ordinary double point (multiplicity 2, two distinct tangent directions). The script should verify:

1. mult_p(F) = 2 for each singular point p
2. The tangent cone at p consists of two distinct lines

**Recommendation:** Use `F.multiplicity(p)` and verify the tangent cone factorization.

---

### 2. Task 1.2: Gram Matrices (`task1_2_gram_matrices.sage`)

**Claim:** Compute Gram matrices for S_Co and T_Co, verify invariants.

#### ✓ Correct Elements:

- S_Co Gram matrix `diag(2, -2, ..., -2)` is correct for Coble Picard lattice
- Signature computations are correct: S_Co has (1, 10), T_Co should have (2, 9)
- Discriminant group order 2¹¹ is correct for both lattices
- K3 lattice construction U³ ⊕ E₈(-1)² is correct

#### ⚠️ **CRITICAL ISSUES:**

**Issue 2.2a: T_Co is Constructed by Fiat, Not Computed**

**This is the most serious mathematical flaw in all three scripts.**

The script states:

```python
# Construct T_Co with signature (2, 9) and discriminant (ℤ/2ℤ)^11
T_Co_gram = diagonal_matrix(QQ, [2, 2] + [-2]*9)
```

**Problem:** T_Co is **defined** as S_Co^⊥ in Λ_K3, but the script never computes this orthogonal complement. Instead, it **asserts** that T_Co has a diagonal Gram matrix with the right signature and discriminant.

**Why This is Mathematically Invalid:**

1. **No proof that S_Co embeds into Λ_K3:** The script assumes S_Co ↪ Λ_K3 exists but never constructs the embedding. By Nikulin's embedding theorem, such an embedding exists iff certain conditions hold, but these are never verified computationally.

2. **No proof that the orthogonal complement has the claimed form:** Even if S_Co embeds, T_Co = S_Co^⊥ is determined by the embedding, not by fiat. Different embeddings can give non-isometric orthogonal complements.

3. **The discriminant form relation q_T = -q_S is asserted, not verified:** For complementary lattices in a unimodular lattice, we must have (A_T, q_T) ≅ (A_S, -q_S). The script checks that both have order 2¹¹ but never verifies the quadratic forms match.

**What Should Be Done:**

```python
# Step 1: Embed S_Co into Λ_K3 explicitly
# Step 2: Compute T_Co = S_Co^⊥ as kernel of pairing
# Step 3: Compute Gram matrix of T_Co from the embedding
# Step 4: Verify T_Co has correct invariants
# Step 5: Verify q_T ≅ -q_S on discriminant groups
```

**Issue 2.2b: Primitivity Check is Circular**

The script checks:

```python
if abs(S_Co.determinant()) == abs(T_Co.determinant()):
    print("Embedding is PRIMITIVE")
```

**Problem:** This criterion is only valid **after** T_Co is computed as the orthogonal complement. Since T_Co is constructed independently, this "verification" is meaningless—it just checks that two diagonal matrices happen to have the same determinant (both are 2¹¹ by construction).

**Correct Approach:** Primitivity means Λ_K3 / S_Co is torsion-free. This should be verified by:

1. Computing the saturation of S_Co in Λ_K3
2. Checking that S_Co equals its saturation

**Issue 2.2c: Genus Uniqueness Argument is Incomplete**

The script correctly notes that r = a = 11 is a "boundary case" for Nikulin's classification, but the conclusion that the genus contains a unique class relies on signature mod 8 analysis that is **stated but not computed**.

**Mathematical Requirement:** For 2-elementary lattices with r = a and δ = 1, genus uniqueness depends on:

- The signature (p, q) mod 8
- Whether the lattice is of "type I" or "type II"

The script asserts uniqueness but doesn't compute the relevant invariants (e.g., the Brown invariant of the discriminant form).

---

### 3. Task 1.3: Embeddings (`task1_3_embeddings.sage`)

**Claim:** Construct explicit primitive embedding matrices T_Co → T_En → T_dP → Λ_K3.

#### ✓ Correct Elements:

- K3 lattice construction is correct
- Strategy of using U factors for orthogonal vectors is sound
- Simple root selection in E₈ (α₁, α₃, α₅, α₇ are mutually orthogonal) is correct
- Smith normal form test for primitivity is the right criterion

#### ⚠️ **CRITICAL ISSUES:**

**Issue 3.3a: S_Co Embedding is Not Verified to be Orthogonal**

The script constructs M_SCo_explicit and claims:

```python
print(f"Matches S_Co_gram: {S_Co_check == S_Co_gram}")
```

**Problem:** The script **abandons** the orthogonal embedding approach when it discovers that E₈ simple roots aren't all mutually orthogonal, then switches to a computational kernel method without verifying the result.

Looking at the actual construction:

```python
# s_4 ↦ α_1 in E8_a (position 6)
# s_5 ↦ α_3 in E8_a (position 8)
# s_6 ↦ α_5 in E8_a (position 10)
# s_7 ↦ α_7 in E8_a (position 12)
```

**Verification Required:** The script should print `S_Co_check.is_diagonal()` and verify it equals `S_Co_gram`. If the E₈ simple roots α₁, α₃, α₅, α₇ are truly orthogonal in the E₈(-1) metric, then `S_Co_check` should be diagonal with entries (2, -2, -2, ..., -2).

**But this is never actually checked in the output!** The script prints the check but doesn't halt if it fails.

**Issue 3.3b: T_Co Orthogonal Complement is Computed, But Not Verified**

In Section 6, the script computes:

```python
pairing = M_SCo_explicit.transpose() * Lambda_K3
kernel_QQ = pairing_QQ.right_kernel()
```

**Problem:** The computed T_Co basis vectors are **cleared of denominators** arbitrarily:

```python
T_Co_basis = [v.denominator() * v for v in kernel_QQ.basis()]
```

This produces an integer lattice, but:

1. It may not be **primitive** in Λ_K3 (the scaling could introduce torsion)
2. The resulting Gram matrix `T_Co_computed_gram` is never compared to the expected `diag(2, 2, -2, ..., -2)`
3. The script never verifies that T_Co ⊕ S_Co = Λ_K3 (i.e., that they span the full lattice)

**Mathematical Requirement:** After computing the kernel, one must:

1. Compute the saturation to ensure primitivity
2. Verify the discriminant form relation q_T ≅ -q_S
3. Check that the direct sum S_Co ⊕ T_Co has index 1 in Λ_K3

**Issue 3.3c: T_En and T_dP are Defined by Truncation, Not Geometry**

The script defines:

```python
M_En_Co = matrix(ZZ, 11, 10, lambda i, j: 1 if i == j else 0)
M_dP_En = matrix(ZZ, 10, 9, lambda i, j: 1 if i == j else 0)
```

**Problem:** These embeddings are **purely formal**—they just take the first 10 or 9 basis vectors of T_Co. There's no geometric justification for why:

- T_En should be a sublattice of T_Co
- T_dP should be a sublattice of T_En
- These specific sublattices have the correct geometric meaning for Enriques/del Pezzo surfaces

**Mathematical Requirement:** The embeddings T_Co → T_En → T_dP should come from:

1. The geometry of the surfaces (e.g., T_En is the transcendental lattice of the Enriques surface obtained as a double cover)
2. Explicit lattice-theoretic constructions (e.g., T_En is the invariant sublattice under an involution)

The script provides neither.

**Issue 3.3d: Primitivity Test is Applied to Identity Matrices**

The primitivity test:

```python
print(f"T_En → T_Co primitive: {is_primitive_embedding(M_En_Co)}")
```

**Problem:** `M_En_Co` is just a 11×10 matrix with 1s on the diagonal. This is **trivially primitive** because it's an inclusion of a direct summand. The test tells us nothing about whether the actual geometric embedding T_En ↪ T_Co is primitive.

**What Should Be Tested:** The primitivity of T_Co ↪ Λ_K3 (which is nontrivial), not the formal inclusions between abstract lattices.

---

## Summary of Required Fixes

### Task 1.1 (Sextic Construction):

1. **Replace Hessian test** with full 3×3 Hessian rank check
2. **Add irreducibility verification** for the sextic polynomial
3. **Verify multiplicity 2** at each singular point
4. **Check tangent cone** has two distinct lines at each node

### Task 1.2 (Gram Matrices):

1. **Actually embed S_Co into Λ_K3** using Nikulin's embedding theorem
2. **Compute T_Co as orthogonal complement**, not by fiat
3. **Verify discriminant form relation** q_T ≅ -q_S explicitly
4. **Check primitivity** via saturation, not just determinant comparison
5. **Compute Brown invariant** to verify genus uniqueness in boundary case

### Task 1.3 (Embeddings):

1. **Verify S_Co embedding is orthogonal** (check S_Co_check == S_Co_gram)
2. **Verify T_Co computed from kernel** has correct Gram matrix
3. **Check S_Co ⊕ T_Co spans Λ_K3** (index 1)
4. **Provide geometric justification** for T_En and T_dP sublattices
5. **Remove trivial primitivity tests** on formal inclusions

---

## Conclusion

The scripts provide a **good computational framework** but the mathematical claims exceed what is actually verified. The most serious issue is **Task 1.2's construction of T_Co by fiat** rather than as a computed orthogonal complement. This undermines the entire lattice-theoretic foundation of the subsequent work.

**Recommendation:** Halt further computation until these foundational issues are resolved. The fixes require:

1. Implementing proper orthogonal complement computation
2. Adding rigorous singularity verification
3. Providing geometric justification for lattice chains

**Estimated effort:** 2-3 days of focused work to correct the mathematical foundations.

---

## References

- Nikulin, V. V. (1979). "Integral symmetric bilinear forms and some of their geometric applications." Math. USSR Izvestija 14, 103-167.
- Conway, J. H. & Sloane, N. J. A. (1999). "Sphere Packings, Lattices and Groups." Springer, 3rd ed.
- Dolgachev, I. (2012). "Classical Algebraic Geometry: A Modern View." Cambridge University Press.
