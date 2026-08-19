<!--
Origin: gitclones/Coxeter/research/foundations/classification-theory.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is RESEARCH PROSE from the Coxeter working trees: a mathematical
account written for this project. Errors the audit found in it are listed in
the README.md of this directory.
-->

# Classification Theory: Definiteness-Based Framework

This document provides the theoretical foundation for the definiteness-based classification system used throughout the Coxeter maximal parabolic project.

## Philosophical Foundation

### Mathematics vs Computation

**Core Principle**: Classification is a **mathematical property**, not a **computational algorithm**.

The fundamental error in many implementations is confusing mathematical definitions with computational methods:
- **Definition**: "Parabolic type means -G is positive semidefinite with rank n-1"
- **Algorithm**: "Count eigenvalues equal to zero" is one way to *verify* this property

This distinction is crucial for mathematical rigor and algorithmic correctness.

## Definiteness-Based Classification

### Mathematical Definitions

For a Coxeter system with Gram matrix G, we classify based on the definiteness properties of the **negative** Gram matrix -G:

#### 1. Elliptic (Finite) Type
**Mathematical Definition**: -G is positive definite
- **Signature of G**: (0, n, 0)
- **Eigenvalue Property**: All eigenvalues of G are negative
- **Geometric Interpretation**: Finite reflection group acting on sphere

#### 2. Parabolic (Affine) Type  
**Mathematical Definition**: -G is positive semidefinite with exactly one zero eigenvalue
- **Signature of G**: (0, n-1, 1)
- **Eigenvalue Property**: One zero eigenvalue, all others negative
- **Geometric Interpretation**: Affine Weyl group acting on Euclidean space

#### 3. Hyperbolic Type
**Mathematical Definition**: -G is indefinite with exactly one positive eigenvalue
- **Signature of G**: (1, n-1, 0)  
- **Eigenvalue Property**: One positive eigenvalue, all others negative
- **Geometric Interpretation**: Infinite group acting on hyperbolic space

#### 4. General Indefinite Type
**Mathematical Definition**: -G has multiple positive eigenvalues
- **Signature of G**: (p, q, r) with p ≥ 2
- **Eigenvalue Property**: Multiple positive eigenvalues
- **Geometric Interpretation**: Infinite covolume groups

### Why Negative Gram Matrix?

**Convention Explanation**: Our Gram matrix uses G_{ii} = -2 (negative diagonal), so:
- Finite types have G with all negative eigenvalues
- To apply standard positive definiteness tests, we examine -G
- This makes finite types correspond to "-G is positive definite"

**Alternative Approach**: We could define G with positive diagonal and test G directly, but our convention aligns with certain geometric traditions.

## Signature Theory

### Mathematical Foundation

**Sylvester's Law of Inertia**: The signature (p, q, r) of a real symmetric matrix is invariant under congruence transformations.

**Consequence**: Signature is a well-defined invariant of the quadratic form, independent of basis choice.

### Signature Computation Methods

#### Method 1: Eigenvalue Analysis
```
signature(G) = (#{λ > 0}, #{λ < 0}, #{λ = 0})
```

#### Method 2: Sylvester's Criterion  
Examine signs of leading principal minors:
- All positive → positive definite
- Alternating sign pattern → negative definite
- Mixed patterns → indefinite

#### Method 3: Cholesky-Based Methods
For positive definiteness testing (most efficient for large matrices).

### Signature Inheritance

**Theorem**: For principal submatrices, signatures can only "weaken":
- (0, n, 0) → (0, n', 0) or (0, n'-1, 1) (elliptic → elliptic or parabolic)
- (0, n-1, 1) → (0, n'-1, 1) or (p, q, r) (parabolic → parabolic or indefinite)
- (1, n-1, 0) → (1, n'-1, 0) or (p, q, r) (hyperbolic → hyperbolic or indefinite)

**Proof Idea**: Eigenvalue interlacing theorems (Cauchy, Poincaré).

## Maximal Parabolic Theory

### Mathematical Definition

A **maximal parabolic subdiagram** is a parabolic subdiagram that is not properly contained in any larger parabolic subdiagram.

**Formal Definition**: An element of the set:
```
Max({I ⊆ {1,...,n} : subdiagram I is parabolic})
```
where Max denotes maximal elements under inclusion.

### Poset-Theoretic Approach

**Step 1**: Enumerate all parabolic subdiagrams
```
Parabolic = {I ⊆ {1,...,n} : signature(G[I,I]) = (0, |I|-1, 1)}
```

**Step 2**: Find maximal elements
```
MaxParabolic = {I ∈ Parabolic : ∀J ∈ Parabolic, I ⊆ J ⟹ I = J}
```

### Common Implementation Errors

#### ❌ Wrong Approach: Single-Vertex Extension
```python
# INCORRECT: Only checks immediate supersets
def find_maximal_parabolic(parabolic_diagram):
    for v in remaining_vertices:
        if extended_diagram(v).is_parabolic():
            return False  # Not maximal
    return True  # Maximal
```

**Problem**: Misses maximal elements that can be extended by multiple vertices simultaneously.

#### ✅ Correct Approach: Poset Maximality
```python
# CORRECT: Checks all possible extensions
def find_maximal_parabolic(all_parabolic_subdiagrams):
    maximal = []
    for diagram in all_parabolic_subdiagrams:
        is_maximal = True
        for other in all_parabolic_subdiagrams:
            if diagram < other:  # Proper subset
                is_maximal = False
                break
        if is_maximal:
            maximal.append(diagram)
    return maximal
```

## Vinberg's Volume Theory

### Volume Finiteness Criterion

**Theorem (Vinberg)**: A hyperbolic Coxeter group has finite covolume if and only if all maximal parabolic subdiagrams are affine (not hyperbolic).

**Proof Idea**: 
- Each maximal parabolic corresponds to a cusp at infinity
- Hyperbolic maximal parabolics create "infinitely deep" cusps
- Only affine maximal parabolics give finite volume cusps

### Cusp Correspondence

**Mathematical Description**: 
- Each maximal parabolic subdiagram stabilizes a null vector at infinity
- The orbit closure of this null vector defines a cusp
- The number of cusps equals the number of maximal parabolic subdiagrams

**Volume Classification**:
1. **Compact**: No parabolic subdiagrams → no cusps → compact orbifold
2. **Finite volume**: All maximal parabolics affine → finite volume cusps
3. **Infinite volume**: Some maximal parabolic hyperbolic → infinite volume cusps

## Field Theory in Classification

### Crystallographic vs Non-Crystallographic

**Crystallographic Types**: 
- Coxeter entries from {2, 3, 4, 6}
- All computations over ℤ or ℚ
- Examples: A_n, D_n, E_n, B_n, C_n, F_4, G_2

**Non-Crystallographic Types**:
- Coxeter entries include 5 (order 5 rotations)  
- Require field extensions
- Examples: H_3, H_4, I_2(5), I_2(7), I_2(p) for p ≠ 2,3,4,6

### Field Extensions for Non-Crystallographic Types

#### H_3 (Icosahedral)
- **Field**: ℚ(φ) where φ = (1+√5)/2
- **Minimal polynomial**: x² - x - 1 = 0
- **Gram matrix entries**: Involve φ and powers

#### H_4 (600-cell)  
- **Field**: ℚ(τ) where τ = 2cos(π/5)
- **Minimal polynomial**: x² - x - 1 = 0 (same as φ+φ⁻¹)
- **Relation**: τ = φ + φ⁻¹ = 2φ - 1

#### I_2(p) (Dihedral)
- **Field**: ℚ(2cos(π/p))
- **Minimal polynomial**: Chebyshev polynomial of degree φ(p)/2
- **Galois group**: Cyclic or dihedral

### Galois Actions on Classifications

**Key Insight**: Galois automorphisms preserve mathematical structure.

**Consequence**: Classification results are invariant under field automorphisms:
- If a subdiagram is parabolic over ℚ(α), it remains parabolic under σ(α)
- Galois orbits of eigenvalues have the same multiplicities
- Signature is preserved under Galois actions

## Implementation Principles

### Correctness Requirements

1. **Use definiteness as primary method**:
   ```python
   def is_parabolic(gram_matrix):
       neg_gram = -gram_matrix
       return (neg_gram.is_positive_semidefinite() and 
               neg_gram.rank() == gram_matrix.nrows() - 1)
   ```

2. **Never use floating-point comparisons**:
   ```python
   # ❌ WRONG
   if abs(eigenvalue) < 1e-10:  # "zero"
   
   # ✅ CORRECT  
   if eigenvalue == 0:  # exact zero
   ```

3. **Implement poset-based maximality**:
   ```python
   def maximal_elements(poset):
       return [x for x in poset if not any(x < y for y in poset)]
   ```

### Mathematical Validation

**Cross-Check Methods**: Every classification result should be verifiable by multiple approaches:
- Definiteness testing (-G properties)
- Eigenvalue analysis (signature computation)
- Sylvester criterion (leading principal minors)
- Literature comparison (known results)

**Field Consistency**: For non-crystallographic types:
- Verify Galois invariance of results
- Check minimal polynomial relationships
- Validate field extension degrees

---

**Summary**: This classification framework provides the mathematical foundation for rigorous, exact computation of Coxeter system types. By emphasizing definiteness properties over computational algorithms, we ensure mathematical correctness and algorithmic reliability.