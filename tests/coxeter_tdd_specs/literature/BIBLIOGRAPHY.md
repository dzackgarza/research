# Project Bibliography

## Authoritative References for Coxeter Groups Theory

### Primary Sources (Canonical Textbooks)

#### [Humphreys1990]
- **Title**: Reflection Groups and Coxeter Groups
- **Author**: James E. Humphreys
- **Year**: 1990
- **Publisher**: Cambridge University Press
- **Series**: Cambridge Studies in Advanced Mathematics, Volume 29
- **ISBN**: 978-0521436137
- **Status**: Primary algebraic reference - most cited standard for core theory
- **Coverage**: Algebraic theory, classification, connections to Lie theory

#### [Davis2008]
- **Title**: The Geometry and Topology of Coxeter Groups
- **Author**: Michael W. Davis
- **Year**: 2008
- **Publisher**: Princeton University Press
- **ISBN**: 978-0691131382
- **Status**: Primary geometric reference - modern standard for geometric aspects
- **Coverage**: Group actions, Davis complex, hyperbolic geometry, polytope connections

#### [Bourbaki2002]
- **Title**: Lie Groups and Lie Algebras, Chapters 4-6
- **Author**: Nicolas Bourbaki
- **Year**: 2002
- **Publisher**: Springer-Verlag
- **ISBN**: 978-3540691716
- **Status**: Ultimate formal authority - for definitional disputes and maximum rigor
- **Coverage**: Abstract foundations, root systems, formal definitions

#### [BjornerBrenti2005]
- **Title**: Combinatorics of Coxeter Groups
- **Authors**: Anders Björner & Francesco Brenti
- **Year**: 2005
- **Publisher**: Springer-Verlag
- **ISBN**: 978-3540442387
- **Status**: Primary combinatorial reference
- **Coverage**: Bruhat order, reduced words, combinatorial invariants

### Foundational Mathematical References

#### [PerronFrobenius1907-1912]
- **Title**: Perron-Frobenius Theorem
- **Authors**: Oskar Perron (1907), Georg Frobenius (1912)
- **Status**: Fundamental theorem in matrix theory - foundation for eigenvalue analysis
- **Coverage**: Spectral properties of non-negative matrices, spectral radius
- **Application**: Used for classification of Coxeter groups by eigenvalue signature

### Secondary Sources (Research Papers)

#### [BogachevKolpakov2024]
- **Title**: Thin Hyperbolic Reflection Groups
- **Authors**: Nikolay Bogachev, Alexander Kolpakov
- **Year**: 2024
- **Identifier**: arXiv:2112.14642v4 [math.GR]
- **Status**: Recent research on hyperbolic groups and Zariski density
- **Coverage**: Thin groups, Vinberg algorithm, classification by eigenvalues

### Supporting References

#### [ConwayBurgiel2008]
- **Title**: The Symmetries of Things
- **Authors**: John H. Conway, Heidi Burgiel, Chaim Goodman-Strauss
- **Year**: 2008
- **Publisher**: A K Peters/CRC Press
- **ISBN**: 978-1568812205
- **Status**: Geometric intuition and visual examples
- **Coverage**: Lower-dimensional groups, symmetry, visual representations

## Citation Floor (No Citation Required)

### Level 0: Basic Mathematics
- Elementary arithmetic operations
- Properties of real numbers
- Basic set theory

### Level 1: Standard Undergraduate Linear Algebra
**Reference**: Any standard undergraduate text (e.g., Axler "Linear Algebra Done Right")
- Matrix operations: det(AB) = det(A)det(B)
- Properties of symmetric matrices
- Eigenvalue existence for real symmetric matrices
- Basic properties of positive definite matrices

### Level 2: Standard Undergraduate Group Theory
**Reference**: Any standard abstract algebra text (e.g., Dummit & Foote)
- Definition of groups, subgroups, homomorphisms
- Lagrange's theorem
- Basic properties of finite groups

## Citation Required (Level 3+)

### All Domain-Specific Knowledge
- **All facts about Coxeter groups**: Must cite [Humphreys1990] or equivalent
- **Advanced matrix theory**: Perron-Frobenius theorem applications
- **Geometric properties**: Polytope theory, hyperbolic geometry
- **Algorithmic correctness**: Vinberg algorithm, Todd-Coxeter
- **Classification results**: Finite/affine/hyperbolic characterization

## Citation Format

### Standard Format
```python
# CITATION: [BibKey] Chapter X, Section Y, Theorem Z
# CATEGORY: Brief description of mathematical truth
def test_name():
    """Test description."""
```

### Categories
- **THEOREM**: Major named results or cornerstone theorems
- **DEFINITION**: Formal mathematical definitions
- **ALGORITHM**: Algorithmic correctness assertions
- **CLASSIFICATION**: Type classification results
- **CONVENTION**: Standard mathematical conventions
- **EXAMPLE**: Specific computational examples from literature

### Examples
```python
# CITATION: [Humphreys1990] Chapter 5, Section 4, Theorem 1
# THEOREM: A Coxeter group is finite iff the bilinear form is positive definite
def test_finiteness_via_bilinear_form():

# CITATION: [Davis2008] Chapter 6, Section 3, Definition 6.3.1
# DEFINITION: Hyperbolic Coxeter group classification by matrix signature
def test_hyperbolic_classification():

# CITATION: [BogachevKolpakov2024] Section 2, Example 1
# EXAMPLE: Non-reflective Lorentzian lattice with specific Gram matrix
def test_bogachev_kolpakov_example():
```

## Quality Control

### Pre-Commit Checks
Mathematical keywords requiring citation verification:
- `eigenvalue`, `hyperbolic`, `finite`, `affine`
- `order`, `root`, `crystallographic`, `classification`
- `determinant`, `signature`, `definite`, `polytope`

### Review Checklist
1. Are new mathematical assertions properly cited?
2. Do citations point to approved sources in this bibliography?
3. Are citation keys and theorem numbers accurate?
4. Is the assertion above the established "citation floor"?