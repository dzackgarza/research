<!--
Origin: gitclones/Coxeter/implementation/conventions/CONVENTIONS.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Mathematical and Implementation Conventions

## Critical Mathematical Distinctions (AGENTS: READ FIRST)

### Bilinear Forms vs Inner Products

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

### Gram vs Cartan Matrices

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

### Orthogonality Behavior

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

## Signature-Based Classification

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

## Exact Arithmetic Requirements

- All computations over ℤ, ℚ, number fields, or exact rings
- No floating point approximation (`abs(x - y) < ε` forbidden)
- Eigenvalues computed as algebraic numbers
- Numerical evaluation only for final visualization

## Field Extensions for Non-Crystallographic Types

**Crystallographic types**: ℤ, ℚ computations
**Non-crystallographic types**:
- H₃: ℤ[φ] where φ² - φ - 1 = 0 (golden ratio)
- H₄: ℤ[τ] where τ = 2cos(π/5)
- I₂(p): ℤ[2cos(π/p)] ⊆ cyclotomic fields
- Minimal field detection: automatic determination of smallest field containing all entries
- Galois orbit handling: eigenvalues/invariants come in conjugate sets

## Forbidden Implementation Patterns

### Classification Errors
- **DO NOT** use "inner product" for general bilinear forms
- **DO NOT** define parabolic as "eigenvalue count == 1"  
- **DO NOT** use eigenvalue analysis as the primary definition
- **DO NOT** implement maximality by single vertex addition
- **DO NOT** use floating-point epsilon comparisons

### Construction Errors
- **DO NOT** guess or manually write Gram matrices
- **DO NOT** hard-code matrices or graphs
- **DO NOT** use SageMath's list notation `['A', 2]` (use LaTeX "A_2")
- **DO NOT** bypass SageMath's mathematical infrastructure

### Algorithm Misuse
- **DO NOT** use `IntegerLattice` for indefinite forms (use `IntegralLattice`)
- **DO NOT** use `IntegerLattice.vectors_of_length()` for indefinite forms
- **DO NOT** use `IntegerLattice.automorphism_group()` for indefinite forms
- **DO NOT** assume orthogonal complements exist for all bilinear forms

### API Design Errors
FreeBilinearModules (Base Category) should NOT include:
- `orthogonal_complement()` - not well-defined in general
- `norm_squared()` - only makes sense for symmetric forms
- `reflection()` - requires symmetry

## Quick Reference

For detailed mathematical theory, implementation patterns, and API specifications, see:
- `implementation/planning/` - Complete API design documentation and algorithm specifications
- `research/foundations/` - Core theoretical concepts and mathematical foundations
- `research/reference/MATHEMATICAL_FOUNDATIONS.md` - Comprehensive mathematical reference

**Remember**: Mathematical definitions are PRIMARY, computational algorithms are SECONDARY. Always implement based on definiteness properties, not eigenvalue counting.