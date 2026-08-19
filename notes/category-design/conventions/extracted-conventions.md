<!--
Origin: gitclones/Coxeter/tmp_restore/extracted-conventions.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Extracted Mathematical Conventions - Agent-Critical Reference

**Purpose**: Preserve critical mathematical distinctions that agents frequently get wrong during implementation.

**Sources**: 
- `docs/api-planning/BILINEAR_FORMS_MATHEMATICAL_NOTES.md`
- `docs/MATHEMATICAL_THEORY.md`
- `docs/REQUIREMENTS.md`
- `docs/CONVENTIONS.md`

## 1. Agent-Critical Distinctions

### 1.1 Bilinear Forms vs Inner Products
**Source**: `BILINEAR_FORMS_MATHEMATICAL_NOTES.md`

**Bilinear Form**: A function B: V × V → K that is linear in both arguments.

**Inner Product**: A positive-definite, symmetric bilinear form. Specifically requires:
1. Symmetry: B(x,y) = B(y,x)
2. Positive definiteness: B(x,x) > 0 for all x ≠ 0
3. Non-degeneracy: B(x,y) = 0 for all y implies x = 0

**CRITICAL**: DO NOT use "inner product" for general bilinear forms! Use:
- "bilinear form" (general case)
- "bilinear pairing" (emphasizes the pairing aspect)
- "quadratic form" (when discussing B(x,x))

**Examples of what is NOT an inner product**:
- Indefinite forms (signature (p,q) with q > 0)
- Skew-symmetric forms
- Degenerate forms
- Complex Hermitian forms (these are sesquilinear, not bilinear)

### 1.2 Gram vs Cartan Matrix Distinction
**Source**: `MATHEMATICAL_THEORY.md`

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

### 1.3 Orthogonality in Different Bilinear Forms
**Source**: `BILINEAR_FORMS_MATHEMATICAL_NOTES.md`

For a bilinear form `B(x,y)` on a module M:

#### 1. For symmetric forms: `B(x,y) = B(y,x)`
- Orthogonality is symmetric: if `B(x,y) = 0` then `B(y,x) = 0`
- Orthogonal complements are well-defined
- The orthogonal complement of v is `{w ∈ M : B(v,w) = 0}`

#### 2. For skew-symmetric forms: `B(x,y) = -B(y,x)`
- If `B(x,y) = 0` then `B(y,x) = 0` (still symmetric relation)
- Orthogonal complements are well-defined
- BUT: Every element is orthogonal to itself: `B(v,v) = 0` for all v
- No notion of "norm" or "length"

#### 3. For general (non-symmetric) forms: `B(x,y) ≠ B(y,x)` in general
- Need to distinguish left and right orthogonality:
  - Left orthogonal: `{w : B(w,v) = 0}`
  - Right orthogonal: `{w : B(v,w) = 0}`
- These can be different sets!
- No well-defined single "orthogonal complement"

### 1.4 Signature-Based Classification (Inverted Convention)
**Source**: `MATHEMATICAL_THEORY.md`, `CONVENTIONS.md`

**Our Gram Matrix Formula**: B_ij = 2 × cos(π/M_ij)

**CRITICAL**: Because our Gram matrix is a **negative multiple** of standard literature, all definiteness criteria are **inverted**:

| Group Type | Standard Literature | Our Convention |
|------------|-------------------|----------------|
| **Finite** | Positive definite (all λ > 0) | **Negative definite (all λ < 0)** |
| **Affine** | Positive semidefinite (one λ = 0, others > 0) | **Negative semidefinite (one λ = 0, others < 0)** |
| **Hyperbolic** | Indefinite (mixed signs) | **Indefinite (mixed signs)** |

#### Mathematical Definitions:
1. **Elliptic (Finite)**: -G is positive definite
2. **Parabolic (Affine)**: -G is positive semidefinite with exactly one zero eigenvalue
3. **Hyperbolic**: -G is indefinite with exactly one positive eigenvalue
4. **General Indefinite**: -G has multiple positive eigenvalues

## 2. Precise Definitions

### 2.1 Exact Arithmetic Requirements
**Source**: `REQUIREMENTS.md`

- All computations over ℤ, ℚ, number fields, or exact rings
- No floating point approximation (`abs(x - y) < ε` forbidden)
- Eigenvalues computed as algebraic numbers
- Numerical evaluation only for final visualization

### 2.2 Field Extension Requirements
**Source**: `REQUIREMENTS.md`, `MATHEMATICAL_THEORY.md`

**Crystallographic types**: ℤ, ℚ computations
**Non-crystallographic types**:
- H₃: ℤ[φ] where φ² - φ - 1 = 0 (golden ratio)
- H₄: ℤ[τ] where τ = 2cos(π/5)
- I₂(p): ℤ[2cos(π/p)] ⊆ cyclotomic fields
- Minimal field detection: automatic determination of smallest field containing all entries
- Galois orbit handling: eigenvalues/invariants come in conjugate sets

### 2.3 Coxeter System Components
**Source**: `MATHEMATICAL_THEORY.md`

A **Coxeter system** (W, S) associated with a root lattice L comprises:

**Core Components**:
- **Simple roots** Δ = {α₁, ..., αₙ} ⊂ L generating the root lattice
- **Weyl group** W = ⟨s₁, ..., sₙ⟩ ≤ O(L), the reflection subgroup generated by simple reflections
- **Simple reflections** S = {s₁, ..., sₙ} where sᵢ is reflection through hyperplane orthogonal to αᵢ
- **Fundamental polytope/chamber** P, the connected component of ℝⁿ \ (⋃ reflection hyperplanes) containing a generic point

### 2.4 Maximal Parabolic Subdiagram Definition
**Source**: `MATHEMATICAL_THEORY.md`

A **maximal parabolic subdiagram** is a subdiagram that:
1. Has parabolic type (exactly one zero eigenvalue)
2. Is not properly contained in any larger parabolic subdiagram

**Geometric Interpretation**: In Vinberg's theory, each maximal parabolic corresponds to a cusp at infinity in the associated hyperbolic orbifold.

## 3. Common Errors

### 3.1 Using "Inner Product" for General Bilinear Forms
**Source**: `BILINEAR_FORMS_MATHEMATICAL_NOTES.md`

**Wrong**: Calling indefinite or degenerate bilinear forms "inner products"
**Correct**: Use "bilinear form", "bilinear pairing", or "quadratic form" as appropriate

### 3.2 Eigenvalue-Based Primary Definitions
**Source**: `MATHEMATICAL_THEORY.md`

**Wrong Approaches**:
- Defining parabolic as "eigenvalue count == 1"  
- Using eigenvalue analysis as the primary definition
- Implementing maximality by single vertex addition
- Using floating-point epsilon comparisons

**Correct Approaches**:
- Define parabolic as "-G is positive semidefinite"
- Use definiteness properties as primary method
- Implement poset-based maximality checking
- Use exact arithmetic throughout

### 3.3 Confusing Mathematical Definitions with Computational Algorithms
**Source**: `MATHEMATICAL_THEORY.md`

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

### 3.4 Orthogonal Complement Confusion
**Source**: `BILINEAR_FORMS_MATHEMATICAL_NOTES.md`

**Error**: Assuming orthogonal complements exist for all bilinear forms
**Truth**: Only well-defined for symmetric and skew-symmetric forms

For general bilinear forms, must distinguish:
- Left orthogonal: `{w : B(w,v) = 0}`
- Right orthogonal: `{w : B(v,w) = 0}`

### 3.5 Indefinite Lattice Algorithm Misuse
**Source**: `REQUIREMENTS.md`

**Critical distinction**: Many standard algorithms only work for positive definite lattices.

**Vector enumeration**:
- Positive definite: `IntegerLattice.vectors_of_length()`
- Indefinite: `QuadraticForm.find_reps()` via PARI/GP

**Automorphism groups**:
- Positive definite: `IntegerLattice.automorphism_group()`
- Indefinite: Custom implementation required (no standard Sage method)

## 4. Forbidden Approaches

### 4.1 From API Design
**Source**: `BILINEAR_FORMS_MATHEMATICAL_NOTES.md`

FreeBilinearModules (Base Category) should NOT include:
- `orthogonal_complement()` - not well-defined in general
- `norm_squared()` - only makes sense for symmetric forms
- `reflection()` - requires symmetry

### 4.2 From Implementation
**Source**: `REQUIREMENTS.md`, `CONVENTIONS.md`

- No hard-coded matrices (violates graph-first construction)
- Never use IntegerLattice for indefinite forms (use IntegralLattice)
- No floating point approximations
- No eigenvalue counting as primary classification method
- No loops for linear algebra operations

### 4.3 From Construction
**Source**: `CONVENTIONS.md`

- **NEVER** guess or manually write Gram matrices
- **NEVER** hard-code matrices or graphs
- **NEVER** use SageMath's list notation `['A', 2]` (use LaTeX "A_2")
- **NEVER** bypass SageMath's mathematical infrastructure

## 5. Mandatory Implementation Patterns

### 5.1 Correct Classification Implementation
**Source**: `MATHEMATICAL_THEORY.md`

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

### 5.2 Graph-Based Construction Pipeline
**Source**: `CONVENTIONS.md`

1. Start with Coxeter type string
2. Get Sage object (`RootSystem`, `CoxeterMatrix`)
3. Extract canonical data (roots, matrix entries)
4. Apply our negative diagonal convention
5. Build our project objects

### 5.3 Maximality Testing Approach
**Source**: `MATHEMATICAL_THEORY.md`

1. **Correct approach**: Construct poset of ALL parabolic subdiagrams
2. **Find maximal elements**: Use poset maximality, not single-vertex additions
3. **Reference**: "It is MAXIMAL in the sub-poset of all subdiagrams, consisting only of parabolic subdiagram"

---

**This document preserves the exact mathematical content from source files to prevent agent implementation errors. All mathematical definitions and distinctions must be preserved exactly as specified.**