<!--
Origin: gitclones/Coxeter/research/foundations/mathematical-theory.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is RESEARCH PROSE from the Coxeter working trees: a mathematical
account written for this project. Errors the audit found in it are listed in
the README.md of this directory.
-->

# Mathematical Theory: Enhanced Foundations

This document provides comprehensive mathematical foundations for the Coxeter maximal parabolic project, combining formal mathematical exposition with development context and research intuition.

## Motivation and Context

The study of Coxeter systems and their maximal parabolic subdiagrams lies at the intersection of several deep mathematical areas:

- **Geometric group theory**: Understanding discrete groups acting on hyperbolic space
- **Quadratic form theory**: Classification via signature and definiteness properties  
- **Algebraic topology**: Connections to homotopy theory and stable ∞-categories
- **Number theory**: Field extensions required for non-crystallographic types

This project develops computational tools to systematically enumerate and classify maximal parabolic subdiagrams, bridging abstract mathematical theory with concrete algorithmic implementation.

## Core Mathematical Framework

### Indefinite Quadratic Forms Theory

#### Mathematical Definition
An **indefinite quadratic form** is a symmetric bilinear form B: V × V → K that takes both positive and negative values on non-zero vectors.

**Signature Classification**: For a quadratic form with Gram matrix G, the signature is (p,q,r) where:
- p = number of positive eigenvalues  
- q = number of negative eigenvalues
- r = number of zero eigenvalues

**Critical Theoretical Property**: The signature is invariant under orthogonal transformations and completely determines the isomorphism class of the quadratic form over ℝ.

#### Project Gram Matrix Convention
Our Gram matrix formula: **B_ij = 2 × cos(π/M_ij)**

This differs from standard geometric literature by a factor of -2:
```
Our_Matrix = -2 × Standard_Geometric_Gram_Matrix
```

**Consequence**: All definiteness criteria are inverted from standard literature.

**Mathematical Intuition**: This convention makes elliptic (finite) types correspond to negative definite forms, aligning with the geometric intuition that finite reflection groups act on spheres (where the metric is negative definite in our convention).

#### Fundamental Eigenvalue Properties

**Eigenvalue Monotonicity Theorem**: If a Coxeter subdiagram is not elliptic, no superdiagram can be elliptic.
- **Mathematical Proof**: By eigenvalue interlacing (Cauchy's interlacing theorem)
- **Computational Consequence**: Enables efficient enumeration by building up from smaller diagrams
- **Implementation Impact**: Allows pruning of search trees in classification algorithms

**Research Context**: This theorem is fundamental to the algorithmic approach developed by Vinberg and implemented in tools like CoxIter. It transforms an exponential search problem into a manageable enumeration.

**Signature Inheritance Theorem**: Subdiagrams inherit definiteness properties with possible weakening.
- **Mathematical Statement**: Principal submatrices have signatures (p',q',r') where p' ≤ p, q' ≤ q
- **Definiteness Weakening**: negative definite → negative semidefinite → indefinite
- **Never Strengthening**: Subdiagrams cannot have "better" definiteness properties than parent diagrams

### Coxeter System Classification Framework

#### Mathematical Classifications (Definiteness-Based)

**Critical Mathematical Principle**: Classifications are based on definiteness properties of the negative Gram matrix -G, not on eigenvalue counting algorithms.

**Philosophical Note**: This distinction between *mathematical definitions* and *computational algorithms* is crucial. The classification is an intrinsic mathematical property; eigenvalue counting is merely one algorithm to verify this property.

1. **Elliptic (Finite) Type**: 
   - **Definition**: -G is positive definite
   - **Signature**: (0,n,0)
   - **Mathematical Property**: All eigenvalues of G are negative
   - **Geometric Context**: Corresponds to finite reflection groups acting on spheres
   
2. **Parabolic (Affine) Type**: 
   - **Definition**: -G is positive semidefinite with exactly one zero eigenvalue
   - **Signature**: (0,n-1,1)
   - **Mathematical Property**: One zero eigenvalue, all others negative
   - **Geometric Context**: Corresponds to affine Weyl groups acting on Euclidean space
   
3. **Hyperbolic Type**: 
   - **Definition**: -G is indefinite with exactly one positive eigenvalue
   - **Signature**: (1,n-1,0)
   - **Mathematical Property**: One positive eigenvalue, all others negative
   - **Geometric Context**: Corresponds to infinite groups acting on hyperbolic space
   
4. **General Indefinite Type**: 
   - **Definition**: -G has multiple positive eigenvalues
   - **Signature**: (p,q,r) with p ≥ 2
   - **Mathematical Property**: Multiple positive eigenvalues
   - **Geometric Context**: Corresponds to groups with infinite covolume

**Fundamental Distinction**: These are mathematical **definitions**, not computational **algorithms**.

#### Vinberg's Geometric Theory

**Volume Finiteness Theorem (Vinberg)**: A hyperbolic Coxeter group has finite covolume if and only if all maximal parabolic subdiagrams are affine (not hyperbolic).

**Research Significance**: This theorem provides the theoretical foundation for studying maximal parabolic subdiagrams. It connects the abstract algebraic classification to concrete geometric properties of the associated hyperbolic orbifold.

**Cusp Correspondence**: In Vinberg's theory of hyperbolic Coxeter groups:
- Each maximal parabolic subdiagram corresponds to a **cusp** at infinity
- The cusp is the limit point of the orbit of the stabilizer of a null vector
- The number of cusps equals the number of maximal parabolic subdiagrams

**Volume Classification**:
- **Compact**: No parabolic subdiagrams exist (Lannér condition)
- **Finite volume, non-compact**: All maximal parabolic subdiagrams are affine type
- **Infinite volume**: At least one maximal parabolic subdiagram is hyperbolic type

### Gram vs Cartan Matrix Mathematical Theory

**Critical Mathematical Distinction**: These represent fundamentally different mathematical structures.

**Historical Context**: The confusion between Gram and Cartan matrices has been a persistent source of implementation errors. Understanding their mathematical distinction is essential for correct algorithmic implementation.

#### Gram Matrix G (Inner Product Encoding)
- **Mathematical Definition**: G_{ij} = ⟨e_i, e_j⟩ where e_i are basis vectors
- **Algebraic Properties**: Always symmetric, encodes the actual bilinear form
- **Our Convention**: Negative diagonal entries G_{ii} = -2
- **Geometric Meaning**: Encodes metric structure of the ambient space

#### Cartan Matrix A (Reflection Encoding)  
- **Mathematical Definition**: A_{ij} = 2⟨α_i, α_j⟩/⟨α_j, α_j⟩ for simple roots α_i
- **Algebraic Properties**: Encodes reflection data, can be non-symmetric
- **Standard Convention**: Positive diagonal entries A_{ii} = 2
- **Geometric Meaning**: Encodes angular relationships in the root system

#### Mathematical Relationship
- **Simply-laced types (ADE)**: A = -G (all roots have same length)
- **Multiple root lengths (BCFG)**: A ≠ -G (relationship depends on root length ratios)
- **Example**: For G₂, scaling is required to make the Gram matrix integral

## Field Theory Requirements  

### Crystallographic vs Non-Crystallographic Types

#### Crystallographic Types (Classical Root Systems)
- **A_n, D_n, E_n**: All computations over ℤ
- **B_n, C_n, F_4**: Work over ℤ after appropriate scaling
- **Mathematical Property**: Coxeter matrix entries from {2,3,4,6}

#### Non-Crystallographic Types (Require Field Extensions)

**Research Context**: Non-crystallographic types arise naturally in the classification of finite reflection groups but require sophisticated algebraic machinery for computational implementation.

**H₃ (Icosahedral Symmetry)**:
- **Field**: ℤ[φ] where φ = (1+√5)/2 (golden ratio)
- **Minimal Polynomial**: φ² - φ - 1 = 0
- **Coxeter Matrix Entries**: Order 5 angles, cos(π/5) = φ/2
- **Geometric Context**: Related to the regular icosahedron and dodecahedron

**H₄ (600-Cell Symmetry)**:
- **Field**: ℤ[τ] where τ = 2cos(π/5)  
- **Minimal Polynomial**: τ² - τ - 1 = 0
- **Mathematical Relationship**: τ = φ + φ⁻¹ = 2φ - 1
- **Geometric Context**: Related to the 600-cell, the 4-dimensional regular polytope

**I₂(p) (Dihedral Groups)**:
- **Field**: ℤ[2cos(π/p)] ⊆ cyclotomic fields
- **Galois Theory**: 2cos(π/p) generates cyclotomic field extensions
- **Minimal Polynomials**: Chebyshev polynomials of the first kind

### Galois Theory Considerations

**Eigenvalue Galois Orbits**: When working in field extensions, eigenvalues come in conjugate sets under the Galois group.

**Example for H₃**: If λ is an eigenvalue in ℚ(φ), then φ̄λ is also an eigenvalue where φ̄ = -1/φ is the Galois conjugate.

**Computational Impact**: 
- Count Galois orbits, not individual eigenvalues
- Signature computation must respect Galois symmetry
- Algebraic multiplicities reflect field extension structure

## Advanced Mathematical Theory

### Subdiagram Theory

#### Mathematical Framework
For a root lattice L with distinguished root system Φ = {α₁, ..., αₙ}, a **subdiagram** corresponding to subset I ⊆ {1, 2, ..., n} is:
- The Coxeter diagram of the root subsystem generated by {αᵢ : i ∈ I}
- Equivalently: the induced subgraph on nodes corresponding to roots in I
- **Gram Matrix**: The principal submatrix G[I,I] of the Gram matrix of Φ

**Critical Theoretical Point**: Subdiagrams are only well-defined for root lattices with a distinguished root system.

#### Maximal Parabolic Theory
**Mathematical Definition**: A **maximal parabolic subdiagram** is a subdiagram that:
1. Has parabolic type (exactly one zero eigenvalue)
2. Is not properly contained in any larger parabolic subdiagram

**Poset-Theoretic Characterization**: Maximal elements in the sub-poset of all parabolic subdiagrams under inclusion.

**Computational Challenge**: Must check all 2^n possible subsets and test maximality in the parabolic poset.

**Research Perspective**: This enumeration problem is at the heart of Vinberg's program for classifying hyperbolic Coxeter groups of finite covolume. The computational complexity grows exponentially, making efficient algorithms essential.

### Classification Theorems

#### Complete Classification Results

**ADE Classification**: Complete list of finite irreducible Coxeter groups
- **A_n**: n ≥ 1, corresponds to symmetric groups S_{n+1}
- **D_n**: n ≥ 4, corresponds to hyperoctahedral groups
- **E_6, E_7, E_8**: Exceptional finite groups

**Affine Classification**: Complete list of affine irreducible Coxeter groups  
- **Extended types**: Ã_n, B̃_n, C̃_n, D̃_n, Ẽ_6, Ẽ_7, Ẽ_8, F̃_4, G̃_2
- **Mathematical Property**: Each corresponds to a Euclidean tiling of hyperplane

**Lannér Classification**: Complete list of compact hyperbolic Coxeter groups
- **Finite List**: 9 groups in dimension 3, 5 groups in dimension 4
- **Compactness Condition**: No parabolic subdiagrams exist

#### Irreducible Affine Types (Complete List)
- **Ã_n** (n ≥ 1): Cycle graph on n+1 vertices
- **B̃_n** (n ≥ 3): Linear chain with one double edge
- **C̃_n** (n ≥ 2): Linear chain with one double edge at different position
- **D̃_n** (n ≥ 4): Y-shaped graph with three branches
- **Ẽ_6, Ẽ_7, Ẽ_8**: Extended exceptional types
- **F̃_4**: With mixed single and double edges
- **G̃_2**: With one triple edge

## Algorithm Mathematical Requirements

### Indefinite Lattice Algorithm Theory

**Critical Mathematical Distinction**: Many standard algorithms only work for positive definite lattices.

**Research Context**: The extension of lattice algorithms to indefinite forms is an active area of research in computational algebra. Our project requires careful algorithm selection based on signature properties.

#### Vector Enumeration Algorithms
**Positive Definite Case**:
- **Algorithm**: Systematic enumeration by norm bounds
- **SageMath Method**: `IntegerLattice.vectors_of_length()`
- **Mathematical Property**: Finite number of vectors in any norm ball

**Indefinite Case**:
- **Algorithm**: Quadratic form representation theory
- **SageMath Method**: `QuadraticForm.find_reps()` via PARI/GP
- **Mathematical Property**: May have infinite families of vectors with given norm

#### Automorphism Group Algorithms
**Positive Definite Case**:
- **Algorithm**: Reduction theory + finite search
- **SageMath Method**: `IntegerLattice.automorphism_group()`
- **Mathematical Foundation**: Reduction theory guarantees finite fundamental domain

**Indefinite Case**:
- **Algorithm**: No standard method available
- **Mathematical Difficulty**: Fundamental domains may be non-compact
- **Research Status**: Active area of computational algebra

#### Theta Series and Modular Forms
**Positive Definite Case**:
- **Mathematical Property**: Theta series converge absolutely
- **Modular Properties**: Often modular or quasi-modular forms
- **Applications**: Enumeration of representations

**Indefinite Case**:
- **Mathematical Property**: Theta series typically divergent
- **Regularization**: Require Eisenstein series or other regularization
- **Applications**: Limited, often require sophisticated analytic techniques

### Signature-Based Algorithm Selection

**Fundamental Principle**: Algorithm choice must be based on signature analysis.

```python
def select_algorithm_by_signature(lattice):
    """Algorithm selection based on mathematical properties."""
    sig = lattice.signature()
    
    if sig[0] == 0:  # Positive semidefinite
        return use_positive_definite_algorithms()
    elif sig[1] == 0:  # Negative semidefinite  
        return use_negative_definite_algorithms()
    else:  # Indefinite
        return use_indefinite_algorithms()
```

### Computational Complexity Theory

#### Eigenvalue Computation Complexity
**Exact Computation**: 
- **Crystallographic Types**: Polynomial time in input size
- **Non-Crystallographic Types**: Requires algebraic number field arithmetic
- **Mathematical Foundation**: Galois theory determines minimal field extensions

#### Subdiagram Enumeration Complexity
**Exhaustive Enumeration**: O(2^n) subsets to check
**Pruning Strategies**: 
- **Eigenvalue Monotonicity**: Prune by definiteness inheritance
- **Poset Structure**: Use inclusion relationships to reduce search space

## Connections to Modern Mathematics

### Homotopy Theory and Stable ∞-Categories

**Research Direction**: The category of bilinear modules over a ring admits a natural enhancement to a stable ∞-category, connecting our work to modern homotopy theory.

**Suspension Functor**: The operation M ↦ H ⊕ M ⊕ H (where H is the hyperbolic plane) defines a suspension functor that leads to stabilization.

**Derived Categories**: The classical derived category D(BilR-Mod) can be understood as the homotopy category of a stable ∞-category of spectra.

**Future Research**: This perspective opens connections to:
- Algebraic K-theory of forms
- L-theory and surgery theory
- Motivic homotopy theory

### Arithmetic and Galois Theory

**Deeper Connections**: The field extensions required for non-crystallographic types connect our work to:
- Galois theory of cyclotomic fields
- Arithmetic of quadratic forms
- Class field theory

**Research Questions**: 
- How do Galois automorphisms act on maximal parabolic enumerations?
- What arithmetic information is encoded in the field extensions?

## Literature and References

### Primary Mathematical Sources

**Root System Theory**:
- **[Humphreys1990]**: "Reflection Groups and Coxeter Groups" - Fundamental reference for Coxeter group theory
- **[Bourbaki]**: "Lie Groups and Lie Algebras, Chapters 4-6" - Canonical treatment of root systems
- **[Davis2008]**: "The Geometry and Topology of Coxeter Groups" - Modern geometric perspective

**Hyperbolic Geometry**:
- **[Vinberg1984]**: "Hyperbolic reflection groups" - Foundational work on hyperbolic Coxeter groups
- **[Allcock2006]**: "Completions, branched covers, Coxeter groups and volume" - Volume computations

**Computational Methods**:
- **[Brink-Howlett1993]**: "A finiteness property and an automatic structure for Coxeter groups"
- **[CoxIter]**: Computational tool for maximal parabolic enumeration

### Theoretical Validation Sources

**Classification Verification**:
- **SageMath RootSystem**: Reference implementation for standard constructions
- **CoxIter**: Primary computational reference for maximal parabolic enumeration
- **GAP System**: Group theory computations and verification

**Mathematical Cross-References**:
- **OEIS Sequences**: Integer sequences for various counting problems
- **ArXiv**: Recent research on hyperbolic Coxeter groups and their applications

## Implementation Requirements for Mathematical Rigor

### Exact Arithmetic Mandate
- **Field Requirements**: ℤ, ℚ, number fields, or exact rings only
- **Forbidden**: Floating point approximation (`abs(x - y) < ε` is mathematically invalid)
- **Eigenvalue Computation**: As algebraic numbers in appropriate field extensions
- **Numerical Evaluation**: Only for final visualization, never for classification

### Categorical Framework Requirements
- **Mathematical Context**: Objects live in well-defined categories with proper morphisms
- **Structure Preservation**: Morphisms preserve bilinear form structure
- **Equivalence**: Isomorphisms determine mathematical equivalence, not equality
- **Validation**: Constructor validation enforces categorical correctness

### Basis-Free Mathematical Construction
- **Mathematical Principle**: Objects defined by intrinsic properties
- **Matrix Derivation**: Matrices derived from objects when basis chosen
- **Coordinate Independence**: Different basis choices yield equivalent results
- **Implementation**: Coordinate computations are implementation details, not definitions

---

**Research Context**: This document represents the consolidated mathematical foundation for a project that bridges abstract mathematical theory with concrete computational implementation. The emphasis on exactness, mathematical rigor, and proper categorical structure reflects the deep mathematical content involved in modern Coxeter group theory.

**Development Philosophy**: Mathematical correctness is paramount. Every algorithm must respect the underlying mathematical structure, and every computation must maintain exact precision. This approach ensures that our results contribute meaningfully to the mathematical literature while providing reliable computational tools for researchers.