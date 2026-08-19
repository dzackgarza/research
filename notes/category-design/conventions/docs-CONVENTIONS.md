<!--
Origin: gitclones/Coxeter/tmp_restore/docs/CONVENTIONS.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Project Conventions

This document establishes comprehensive conventions for the Coxeter maximal parabolic project, consolidating all scattered convention documents into a single authoritative source.

## 1. Construction Conventions

### 1.1 Graph-Based Construction Only
- **ALWAYS** construct Coxeter systems through their graphs during testing
- **NEVER** guess or manually write Gram matrices
- Use Sage's `CoxeterMatrix` or `DynkinDiagram` to generate graphs
- Build Gram matrices by extracting from Sage objects

### 1.2 No Hard-Coded Data
- **NEVER** hard-code matrices or graphs
- **ALWAYS** fetch data structures from Sage objects
- Use canonical construction methods from Sage
- Example:
  ```python
  # WRONG
  gram = matrix([[-2, 1], [1, -2]])
  
  # RIGHT
  R = RootSystem("A_2")  # LaTeX notation
  gram = compute_gram_from_roots(R.ambient_space().simple_roots())
  ```

### 1.3 Coxeter Type Notation
- **ALWAYS** use LaTeX string notation for Coxeter types
- **NEVER** use SageMath's list notation `['A', 2]`
- **Standard notation**:

#### Finite Types
```python
# Crystallographic finite types
"A_n"    # A_1, A_2, A_3, A_4, ...
"B_n"    # B_2, B_3, B_4, B_5, ...  
"C_n"    # C_2, C_3, C_4, C_5, ...
"D_n"    # D_4, D_5, D_6, D_7, ...
"E_n"    # E_6, E_7, E_8
"F_4"    # F_4
"G_2"    # G_2

# Non-crystallographic finite types  
"H_n"    # H_3, H_4
"I_2(p)" # I_2(5), I_2(6), I_2(7), ... (dihedral groups)
```

#### Affine Types
```python
# Extended finite types (both forms accepted)
"A_n^{(1)}"  # A_1^{(1)}, A_2^{(1)}, ...
"A_n~"       # Alternative tilde notation: A_1~, A_2~, ...
```

## 2. Critical Convention: Gram Matrix Definition

### 2.1 Our Formula
**B_ij = 2 × cos(π/M_ij)**

This differs from standard literature in two ways:
1. **Factor of 2**: Standard geometric Gram matrices use -cos(π/M_ij)
2. **Sign**: We get positive off-diagonal entries instead of negative

### 2.2 Relationship to Standard Literature
```
Our_Matrix = -2 × Standard_Geometric_Gram_Matrix
```

### 2.3 Consequences for Classification

Because our Gram matrix is a **negative multiple** of the standard matrix, all definiteness criteria are **inverted**:

| Group Type | Standard Literature | Our Convention |
|------------|-------------------|----------------|
| **Finite** | Positive definite (all λ > 0) | **Negative definite (all λ < 0)** |
| **Affine** | Positive semidefinite (one λ = 0, others > 0) | **Negative semidefinite (one λ = 0, others < 0)** |
| **Hyperbolic** | Indefinite (mixed signs) | **Indefinite (mixed signs)** |

### 2.4 Root Labeling and Ordering

- Simple roots are labeled 1, 2, ..., n (not 0-based)
- In extended diagrams, the affine node is labeled 0
- Internal arrays use 0-based indexing with appropriate conversion

### 2.5 Examples

#### A₂ Triangle Group
- **Coxeter Matrix**: M = [[1,3],[3,1]]
- **Our Gram Matrix**: B = [[-2, 1], [1, -2]]
- **Eigenvalues**: [-3, -1] (both negative → finite type)
- **Standard Literature**: Would have eigenvalues [+3, +1] (both positive → finite type)

#### Verification of Formula
- B₁₁ = 2 × cos(π/1) = 2 × (-1) = -2 ✓
- B₁₂ = 2 × cos(π/3) = 2 × (1/2) = 1 ✓

## 3. SageMath Integration Conventions

### 3.1 Prefer SageMath Objects
- **ALWAYS** use SageMath's canonical objects when available
- **NEVER** bypass SageMath's mathematical infrastructure
- Start from SageMath's `RootSystem`, `CoxeterMatrix`, `DynkinDiagram`

### 3.2 LaTeX Notation Preference
```python
# PREFERRED - matches mathematical literature
R = RootSystem("A_2")  # LaTeX notation
C = CoxeterMatrix("B_3")
D = DynkinDiagram("E_6")

# AVOID - internal implementation details
R = RootSystem(['A', 2])  # SageMath list form
```

### 3.3 Root System Construction Pipeline
1. Start with Coxeter type string
2. Get Sage object (`RootSystem`, `CoxeterMatrix`)
3. Extract canonical data (roots, matrix entries)
4. Apply our negative diagonal convention
5. Build our project objects

### 3.4 Never Reinvent the Wheel
- Don't implement root system theory from scratch
- Use Sage's validated mathematical infrastructure
- Build on top of, don't replace Sage components

## 4. Mathematical Object Hierarchy

### 4.1 Data Source Hierarchy (Most Trusted → Least)
1. **Literature theorems** (Humphreys, Davis, Bourbaki)
2. **Sage canonical objects** (RootSystem, CoxeterMatrix)
3. **Validated external tools** (CoxIter, GAP)
4. **Our implementations** (must validate against above)

### 4.2 Construction Priority
- Loop through Cartan types systematically
- Extract data from Sage canonical constructions
- Apply project-specific conventions (negative diagonal)
- Validate against literature when possible

## 5. Lattice and Vector Space Conventions

### 5.1 Root Systems are Never Isolated
- Root systems are **NEVER** in isolation - they are attached to their integral lattice
- Example:
  ```python
  # WRONG - isolated root data
  roots = [(1,-1,0), (0,1,-1)]
  
  # RIGHT - roots know their parent lattice
  L = RootSystem(['A', 2]).root_lattice()
  roots = L.simple_roots()
  # roots know their parent lattice
  ```

### 5.2 Lattice vs Vector Space Distinction
- **Lattices**: ZZ-modules with definite structure
- **Vector spaces**: QQ/RR-modules, more general
- Always specify which context you're working in
- Example:
  ```python
  L1 = RootSystem(['A', 2]).root_lattice()
  L2 = RootSystem(['A', 2]).weight_lattice()
  # These are different mathematical objects!
  ```

### 5.3 Conversion Between Lattices
- Choose source and target bases explicitly
- **NEVER** assume automatic coercion
- Document all lattice embeddings and morphisms

## 6. Field Theory and Number Systems

### 6.1 Exact Arithmetic Requirements
- **NEVER** use floating point (RDF, CDF)
- **ALWAYS** work in exact fields
- Use algebraic number fields when necessary

### 6.2 Field Extensions by Type
- **Crystallographic types (A,B,C,D,E,F,G)**: Work over ℤ after scaling
- **H₃**: Work over ℤ[φ] where φ = (1+√5)/2 (golden ratio)
- **H₄**: Work over ℤ[τ] where τ = 2cos(π/5)  
- **I₂(p)**: Work over ℤ[2cos(π/p)]

### 6.3 Galois Theory Considerations
- When working in field extensions, eigenvalues come in Galois orbits
- Example:
  ```python
  # If λ is an eigenvalue in QQ(√2), then so is -λ (the conjugate)
  # Count Galois orbits, not individual eigenvalues
  ```

## 7. Matrix Operations Conventions

### 7.1 No Loops for Linear Algebra
- **NEVER** use loops for linear algebra operations
- Use SageMath's built-in matrix operations
- Express operations as matrix multiplications

### 7.2 Examples

#### Wrong: Loop-based Gram matrix construction
```python
# WRONG - computing inner products via loops
for i in range(n):
    for j in range(n):
        gram[i][j] = roots[i].inner_product(roots[j])
```

#### Right: Matrix-based construction
```python
root_matrix = matrix([r.vector() for r in roots]).transpose()
gram = root_matrix.transpose() * root_matrix
```

### 7.3 Coordinate Extraction
- Express coordinate extraction as matrix solve
- Avoid loops for coordinate computations

#### Wrong: Loop-based coordinates
```python
def get_coords(v, basis):
    coords = []
    for b in basis:
        coeff = solve_for_coefficient(v, b)
        coords.append(coeff)
    return coords
```

#### Right: Matrix solve
```python
coords = basis_matrix.solve_right(v.vector())
```

## 8. Algorithm and Performance Conventions

### 8.1 Caching Strategy
- Cache expensive computations (eigenvalues, signatures)
- Use SageMath's caching decorators where appropriate
- Document what's cached and why

### 8.2 Enumeration Strategies
- For exhaustive enumeration, follow established mathematical algorithms
- Prefer algorithmic enumeration over brute force when possible
- Document algorithmic complexity

## 9. Lattice Classification Conventions

### 9.1 Signature-Based Classification
- Positive definite lattices: signature (n, 0, 0)
- Negative definite lattices: signature (0, n, 0)  
- Hyperbolic lattices: signature (p, q) with p ≥ 1
- Parabolic/degenerate lattices: signature includes zeros

### 9.2 Examples
```python
# Signature (1, 1) - one positive, one negative eigenvalue
# This is a hyperbolic lattice
```

## 10. Testing and Verification Conventions

### 10.1 Ground Truth Validation
- **CoxIter**: Primary reference for maximal parabolic enumeration
- **SageMath**: Reference for root systems and standard constructions
- **Literature**: Final authority for mathematical correctness

### 10.2 Never Use Mock Data
- Use real mathematical objects from Sage/CoxIter
- Test our logic, not the correctness of established libraries

### 10.3 Test Categories
- **Unit tests**: Test our code with real Sage data (minimal mocking)
- **Integration tests**: Full workflow with real external dependencies  
- **System tests**: End-to-end verification against literature examples

## 11. Documentation and Citation Conventions

### 11.1 Mathematical References
- **ALL tests using eigenvalue classification MUST cite both:**
  1. **[Humphreys1990]** or **[Davis2008]** for the underlying mathematical theorem
  2. **[PROJECT_CONVENTIONS.md]** for our specific matrix definition that inverts the criteria

### 11.2 Code Documentation
- Explain mathematical context, not just implementation
- Include literature references for algorithms
- Document our convention differences from standard literature

## 12. Type-Specific Conventions

### 12.1 Finite Types
- **Elliptic type**: Negative definite (all eigenvalues < 0)
- Use for classification, enumeration, and verification

### 12.2 Affine Types  
- **Parabolic type**: Negative semidefinite with rank n-1 (all eigenvalues ≤ 0, exactly one = 0)
- Null root δ = α_0 + θ where θ is highest root
- Height: ht(α) = sum of simple root coefficients

### 12.3 Hyperbolic Types
- **Hyperbolic type**: Indefinite with signature (1, n-1, 0) (one eigenvalue > 0, rest < 0)
- Maximal parabolic subgroups correspond to cusps
- Corresponds to cusp at infinity in hyperbolic space

## 13. Implementation Strategy

### 13.1 Build on SageMath Foundation
- Use SageMath's category infrastructure
- Respect SageMath's mathematical conventions where possible
- Extend, don't replace SageMath functionality

### 13.2 Mathematical Rigor
- All implementations must recover known literature results  
- Use exact arithmetic throughout
- Validate against multiple sources when possible

### 13.3 Performance and Scalability
- Design for research-scale problems
- Cache expensive operations
- Use efficient enumeration algorithms

This document serves as the authoritative reference for all project conventions. When in doubt, refer to this document and the mathematical literature.