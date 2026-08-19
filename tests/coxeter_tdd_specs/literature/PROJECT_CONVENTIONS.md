# Project-Specific Mathematical Conventions

## Critical Convention: Gram Matrix Definition

### Our Formula
**B_ij = 2 × cos(π/M_ij)**

This differs from standard literature in two ways:
1. **Factor of 2**: Standard geometric Gram matrices use -cos(π/M_ij)
2. **Sign**: We get positive off-diagonal entries instead of negative

### Relationship to Standard Literature
```
Our_Matrix = -2 × Standard_Geometric_Gram_Matrix
```

### Consequences for Classification

Because our Gram matrix is a **negative multiple** of the standard matrix, all definiteness criteria are **inverted**:

| Group Type | Standard Literature | Our Convention |
|------------|-------------------|----------------|
| **Finite** | Positive definite (all λ > 0) | **Negative definite (all λ < 0)** |
| **Affine** | Positive semidefinite (one λ = 0, others > 0) | **Negative semidefinite (one λ = 0, others < 0)** |
| **Hyperbolic** | Indefinite (mixed signs) | **Indefinite (mixed signs)** |

### Examples

#### A₂ Triangle Group
- **Coxeter Matrix**: M = [[1,3],[3,1]]
- **Our Gram Matrix**: B = [[-2, 1], [1, -2]]
- **Eigenvalues**: [-3, -1] (both negative → finite type)
- **Standard Literature**: Would have eigenvalues [+3, +1] (both positive → finite type)

#### Verification of Formula
- B₁₁ = 2 × cos(π/1) = 2 × (-1) = -2 ✓
- B₁₂ = 2 × cos(π/3) = 2 × (1/2) = 1 ✓

### Why This Convention?

This convention aligns with:
1. **Negative diagonal requirement** stated in CLAUDE.md
2. **Integral lattice theory** where the Gram matrix represents inner products
3. **Consistency with our project's focus on indefinite lattices**

### Citation Requirements

**ALL tests using eigenvalue classification MUST cite both:**
1. **[Humphreys1990]** or **[Davis2008]** for the underlying mathematical theorem
2. **[PROJECT_CONVENTIONS.md]** for our specific matrix definition that inverts the criteria

### Template Citation
```python
# CITATION: [Humphreys1990] Theorem 2.7.1, [PROJECT_CONVENTIONS.md]
# THEOREM: Finite iff standard Gram matrix is positive definite
# CONVENTION: Our Gram matrix = -2 × standard, so finite iff negative definite
def test_finite_classification():
    # Check all eigenvalues < 0 for finite type
```

## Other Project Conventions

### Matrix Storage
- All matrices stored as Sage `IntegralLattice` objects
- Never use `IntegerLattice` (requires positive definite)
- Work in exact arithmetic (ZZ, QQ, number fields)

### Index Conventions  
- Follow Sage's 1-based labeling internally
- Present 0-based indexing to users when appropriate
- Document any index translation in interfaces

### Field Requirements
- Minimize field extensions for each Coxeter type
- Scale matrices to have integral entries when possible
- Use exact arithmetic for all mathematical computations

This document provides the mathematical foundation that distinguishes our project's approach from standard textbook presentations.