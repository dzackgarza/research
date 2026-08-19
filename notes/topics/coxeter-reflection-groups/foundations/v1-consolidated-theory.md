<!--
Origin: gitclones/Coxeter/research/archive/2025-01-27-docs-restructure/MATHEMATICAL_THEORY.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is RESEARCH PROSE from the Coxeter working trees: a mathematical
account written for this project. Errors the audit found in it are listed in
the README.md of this directory.
-->

# Mathematical Theory

This document consolidates the mathematical foundations underlying the Coxeter maximal parabolic project.

## Core Mathematical Framework

### Indefinite Quadratic Forms

**Definition**: An indefinite quadratic form is a symmetric bilinear form that takes both positive and negative values.

**Signature**: For a quadratic form with Gram matrix G, the signature is (p,q,r) where:
- p = number of positive eigenvalues  
- q = number of negative eigenvalues
- r = number of zero eigenvalues

**Project Convention**: We use negative diagonal entries: G_{ii} = -2 for simple roots, following the convention that makes elliptic types negative definite.

### Coxeter System Classification

**CRITICAL**: Classifications are based on definiteness properties, not eigenvalue counting.

#### Mathematical Definitions:
1. **Elliptic (Finite)**: -G is positive definite
2. **Parabolic (Affine)**: -G is positive semidefinite with exactly one zero eigenvalue
3. **Hyperbolic**: -G is indefinite with exactly one positive eigenvalue
4. **General Indefinite**: -G has multiple positive eigenvalues

#### Corresponding Signatures:
The definiteness properties have corresponding signatures for the Gram matrix G:
- Elliptic: signature (0,n,0) 
- Parabolic: signature (0,n-1,1)
- Hyperbolic: signature (1,n-1,0)
- General Indefinite: signature (p,q,r) with p ≥ 2

**Note**: The signature is a CONSEQUENCE of the definiteness property, not the definition.

### Fundamental Mathematical Properties

#### Eigenvalue Monotonicity
**Theorem**: If a Coxeter subdiagram is not elliptic, no superdiagram can be elliptic.
- **Consequence**: Enables efficient enumeration by building up from smaller diagrams
- **Proof**: Adding vertices can only make eigenvalues less negative (eigenvalue interlacing)

#### Signature Inheritance  
**Theorem**: Subdiagrams inherit definiteness properties with possible weakening.
- Principal submatrices have signatures (p',q',r') where p' ≤ p, q' ≤ q
- Definiteness can only weaken: negative definite → negative semidefinite → indefinite

#### Volume Finiteness Criteria
**Theorem (Vinberg)**: A hyperbolic Coxeter group has finite covolume if and only if all maximal parabolic subdiagrams are affine (not hyperbolic).

### Gram vs Cartan Matrix Distinction

**CRITICAL**: These are fundamentally different mathematical objects.

#### Gram Matrix G
- **Definition**: G_{ij} = ⟨e_i, e_j⟩ where e_i are basis vectors
- **Properties**: Always symmetric, encodes the actual inner product
- **Our convention**: Negative diagonal entries G_{ii} = -2

#### Cartan Matrix A  
- **Definition**: A_{ij} = 2⟨α_i, α_j⟩/⟨α_j, α_j⟩ for simple roots α_i
- **Properties**: Encodes reflection data, can be non-symmetric
- **Standard convention**: Positive diagonal entries A_{ii} = 2

#### Relationship
- **Simply-laced types (ADE)**: A = -G (since all roots have same length)
- **Multiple root lengths (BCFG)**: A ≠ -G (relationship depends on root length ratios)
- **Example**: For G₂, scaling is required to make the Gram matrix integral

### Subdiagram Theory

#### Principal Submatrices
For a vertex subset I ⊆ {1,...,n}, the subdiagram corresponds to the principal submatrix G[I,I].

#### Maximal Parabolic Subdiagrams
**Definition**: A parabolic subdiagram that is not contained in any larger parabolic subdiagram.

**Geometric Interpretation**: In Vinberg's theory, each maximal parabolic corresponds to a cusp at infinity in the associated hyperbolic orbifold.

**Computational Challenge**: Must check all 2^n possible subsets and test maximality.

### Field Theory Requirements

#### Crystallographic Types
- **A_n, D_n, E_n**: All computations over ℤ
- **B_n, C_n, F_4**: Work over ℤ after appropriate scaling

#### Non-Crystallographic Types  
- **H₃**: Work over ℤ[φ] where φ = (1+√5)/2 (golden ratio)
- **H₄**: Work over ℤ[τ] where τ = 2cos(π/5)  
- **I₂(p)**: Work over ℤ[2cos(π/p)]

### Lattice Structure

#### Integral Lattices
All objects are integral lattices (finitely generated ℤ-modules with symmetric bilinear form) or their rationalizations.

#### Inner Product Convention
- Use the lattice's intrinsic inner product, never assume Euclidean
- For indefinite lattices, inner products can be negative or zero
- Always work with the ambient lattice's Gram matrix

### Mathematical Definitions vs Computational Algorithms

**CRITICAL DISTINCTION**: 
- **Definitions**: Mathematical properties that define the classification
- **Algorithms**: Computational methods to verify these properties

#### Correct Definitions:
- **Parabolic subdiagram**: DEFINED as -G being positive semidefinite with rank n-1
- **Elliptic subdiagram**: DEFINED as -G being positive definite  
- **Hyperbolic subdiagram**: DEFINED as -G being indefinite with one positive eigenvalue

#### Computational Algorithms:
- **Eigenvalue counting**: An ALGORITHM to check definiteness properties
- **Sylvester's criterion**: An ALGORITHM using leading principal minors
- **Cholesky decomposition**: An ALGORITHM for positive definiteness testing

### Algorithmic Implications

#### For Positive Definite Lattices
- Can use standard algorithms: LLL reduction, short vector enumeration
- Eigenvalues have natural ordering and bounds
- Vector enumeration terminates naturally

#### For Indefinite Lattices  
- Standard algorithms often fail or don't apply
- Must use specialized approaches (e.g., PARI's qfsolve for vector enumeration)
- Eigenvalue analysis requires careful handling of mixed signatures
- Some algorithms (like theta series) may not converge

### Known Mathematical Results

#### Classification Theorems
1. **ADE Classification**: Complete list of finite irreducible Coxeter groups
2. **Affine Classification**: Complete list of affine irreducible Coxeter groups  
3. **Lannér Classification**: Complete list of compact hyperbolic Coxeter groups

#### Computational Verification
- **Finite Types**: All have signature (0,n,0)
- **Affine Types**: All have signature (0,n-1,1) and zero maximal parabolic subdiagrams
- **Lannér Types**: Compact hyperbolic groups with no parabolic subdiagrams

### Integration with SageMath Theory

#### Root System Framework
- Use SageMath's RootSystem infrastructure as ground truth
- Extract Gram matrices from simple root inner products
- Respect Bourbaki labeling conventions (simple roots labeled 1,2,...,n)

#### Category Theory
- Work in the category of integral lattices over ℤ
- All morphisms preserve the lattice structure
- Use SageMath's category framework for proper typing and coercion

#### Construction Principles
1. **Always** build from SageMath's canonical constructions
2. **Never** hard-code numerical values
3. **Always** validate against known theoretical results
4. **Never** bypass SageMath's mathematical infrastructure

## Comprehensive Mathematical Definitions

### Core Definitions

#### Gram Matrix
For simple roots α₁, ..., αₙ in a lattice with inner product ⟨·,·⟩, the **Gram matrix** G is the n×n symmetric matrix with entries:
```
G_{ij} = ⟨αᵢ, αⱼ⟩
```

**Convention**: We use the negative diagonal convention where G_{ii} = ⟨αᵢ, αᵢ⟩ = -2 for simple roots.

#### Subdiagram
For a root lattice L with distinguished root system Φ = {α₁, ..., αₙ}, a **subdiagram** corresponding to root subset I ⊆ {1, 2, ..., n} is:
- The Coxeter diagram of the root subsystem generated by {αᵢ : i ∈ I}
- Equivalently: the induced subgraph on nodes corresponding to roots in I
- Gram matrix: The principal submatrix G[I,I] of the Gram matrix of Φ

**Note**: Subdiagrams are only well-defined for root lattices with a distinguished root system.

#### Maximal Parabolic Subdiagram
A **maximal parabolic subdiagram** is a subdiagram that:
1. Has parabolic type (exactly one zero eigenvalue)
2. Is not properly contained in any larger parabolic subdiagram

#### Coxeter Matrix
For a Coxeter system, the **Coxeter matrix** M has entries:
- M_{ii} = 1 (identity reflections)
- M_{ij} = order of the product sᵢsⱼ in the Coxeter group for i ≠ j
- M_{ij} ∈ {2, 3, 4, 5, 6, ∞} (standard values)
- **Relationship to Gram matrix**: G_{ij} = -2cos(π/M_{ij}) for i ≠ j

### Vinberg's Geometric Conventions

#### Parabolic Subgroup vs Parabolic Type
**Important distinction**:

- **Parabolic subgroup** (group theory): Subgroup W_I = ⟨s_i : i ∈ I⟩ generated by a subset of simple reflections
- **Parabolic type** (Vinberg's convention): Coxeter subdiagram with exactly one zero eigenvalue (affine type)

In this project, "parabolic subdiagram" means parabolic type unless otherwise specified.

#### Cusp Correspondence
In Vinberg's theory of hyperbolic Coxeter groups:
- Each maximal parabolic subdiagram corresponds to a **cusp** at infinity
- The cusp is the limit point of the orbit of the stabilizer of a null vector
- The number of cusps equals the number of maximal parabolic subdiagrams

#### Volume Classification
For hyperbolic Coxeter groups:
- **Compact**: No parabolic subdiagrams exist (Lannér condition)
- **Finite volume, non-compact**: All maximal parabolic subdiagrams are affine type
- **Infinite volume**: At least one maximal parabolic subdiagram is hyperbolic type

### Root Lattice Definitions

#### Root Lattice
A **root lattice** is a lattice L such that there exists a set of simple roots Φ in L and a primitive embedding Φ → L of index 1. Thus it is a lattice generated by a set of simple roots.

**Properties**:
- Has well-defined simple roots, Coxeter matrix, and Coxeter diagram
- The lattice is the ℤ-span of its simple roots
- Corresponds to finite (elliptic) or affine (parabolic) Coxeter systems
- General lattices may contain root sublattices but are not themselves root lattices

#### Root Lattice with Distinguished Root System
A **root lattice L with distinguished root system Φ** is a root lattice equipped with a specific choice of root system Φ ⊂ L. This has:
- A canonical Coxeter diagram determined by Φ
- Well-defined subdiagrams (principal submatrices of the Gram matrix of Φ)
- Subdiagram classification and counting depend on this choice of Φ

**Important**: Subdiagrams are not well-defined on general lattices - they depend on the choice of root system.

#### Coxeter System
A **Coxeter system** (W, S) associated with a root lattice L is the complete algebraic and geometric structure comprising:

**Core Components**:
- **Simple roots** Δ = {α₁, ..., αₙ} ⊂ L generating the root lattice
- **Weyl group** W = ⟨s₁, ..., sₙ⟩ ≤ O(L), the reflection subgroup generated by simple reflections
- **Simple reflections** S = {s₁, ..., sₙ} where sᵢ is reflection through hyperplane orthogonal to αᵢ
- **Fundamental polytope/chamber** P, the connected component of ℝⁿ \ (⋃ reflection hyperplanes) containing a generic point

**Subdiagram Structure**:
- **Elliptic subdiagram poset**: All subsets I ⊆ {1,...,n} where G[I,I] is negative definite
- **Parabolic subdiagram poset**: All subsets I where G[I,I] has signature (0, |I|-1, 1)
- **Hyperbolic subdiagram poset**: All subsets I where G[I,I] has signature (1, |I|-1, 0)
- **Maximal elements** of each poset

### Irreducible Affine Types
The complete classification of irreducible affine (parabolic) types:
- **Ã_n** (n ≥ 1): Cycle graph on n+1 vertices
- **B̃_n** (n ≥ 3): Linear chain with one double edge
- **C̃_n** (n ≥ 2): Linear chain with one double edge at different position
- **D̃_n** (n ≥ 4): Y-shaped graph with three branches
- **Ẽ_6, Ẽ_7, Ẽ_8**: Extended exceptional types
- **F̃_4**: With mixed single and double edges
- **G̃_2**: With one triple edge

## Implementation Requirements

### Mathematical Rigor
- Use exact arithmetic (ZZ, QQ, algebraic number fields)
- Never use floating point for eigenvalue computations
- Validate all mathematical invariants

### Correct Implementation Approach

#### Always Use Definiteness-Based Methods:
```python
def is_parabolic(self):
    """Check if subdiagram is parabolic using definiteness."""
    neg_gram = -self.gram_matrix()
    return neg_gram.is_positive_semidefinite() and neg_gram.rank() == self.rank() - 1

def is_elliptic(self):
    """Check if subdiagram is elliptic using definiteness."""
    neg_gram = -self.gram_matrix()
    return neg_gram.is_positive_definite()
```

#### FORBIDDEN Approaches:
- Don't use eigenvalue counting as primary method
- Don't implement `eigenvalues().count(lambda x: x == 0)`
- Don't use epsilon-based floating point comparisons

#### For Maximality Testing:
1. **Correct approach**: Construct poset of ALL parabolic subdiagrams
2. **Find maximal elements**: Use poset maximality, not single-vertex additions
3. **Reference**: "It is MAXIMAL in the sub-poset of all subdiagrams, consisting only of parabolic subdiagram"

### Common Implementation Errors (Based on Previous Mistakes)

#### ❌ WRONG APPROACHES:
- Defining parabolic as "eigenvalue count == 1"  
- Using eigenvalue analysis as the primary definition
- Implementing maximality by single vertex addition
- Using floating-point epsilon comparisons

#### ✅ CORRECT APPROACHES:
- Define parabolic as "-G is positive semidefinite"
- Use definiteness properties as primary method
- Implement poset-based maximality checking
- Use exact arithmetic throughout

### Index Labeling
Following Bourbaki's convention:
- Simple roots labeled α₁, α₂, ..., αₙ (1-based)
- In extended diagrams, the affine node is labeled α₀
- Internal arrays use 0-based indexing

This mathematical foundation ensures all implementations maintain the highest standards of mathematical rigor and recover all known theoretical results.