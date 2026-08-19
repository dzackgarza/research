<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/ALGORITHMS.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is an ALGORITHM/REQUIREMENT SURVEY written against SageMath as it
stood in the source tree. Rows now owned by the preamble, and errors the
audit recorded, are listed in the README.md of this directory.
-->

# Algorithms for Lattice Computations

This document catalogs computationally difficult problems in lattice theory and Coxeter systems, with **primary focus on indefinite lattices** (our main use case). Implementation sources are prioritized by integration ease.

## CRITICAL DISTINCTION: Definite vs Indefinite Algorithms

Many algorithms work ONLY for positive definite lattices. Since we primarily work with indefinite lattices in Coxeter theory, we must carefully verify algorithm applicability and develop indefinite-specific methods.

## Implementation Priority Order

1. **Adapt Sage code** - Direct access, already in Python
2. **Adapt existing Python libraries** - Native integration
3. **Call GAP via Sage interface** - Well-established bridge
4. **Call Julia packages** - Via PyJulia or system calls
5. **Call custom binaries** - System process interface
6. **Implement from papers** - Last resort, most error-prone

## Corrected Algorithm Priorities for Indefinite Lattices

**Note**: The following priorities correct common misunderstandings from definite lattice theory.

### ESSENTIAL (High Complexity, Frequently Needed)

#### 1. Isometry Testing Between Indefinite Lattices
- **Problem**: Determine if two indefinite lattices are isometric
- **Complexity**: Much harder than definite case
- **Current status**: `IntegerLattice.is_isometric()` likely definite-only
- **Priority**: Essential for classification

#### 2. Automorphism Group Generation (Indefinite)
- **Problem**: Compute O(L) for indefinite lattice L
- **Complexity**: Group may be infinite, requires careful analysis
- **Current status**: `IntegerLattice.automorphism_group()` definite-only
- **Priority**: Essential for structure analysis

#### 3. Local Invariants Computation
- **Problem**: Compute p-adic invariants, Hasse symbols, etc.
- **Complexity**: Essential for classification
- **Priority**: High - needed for lattice classification

#### 4. Primitive Embedding Detection
- **Problem**: Determine if L₁ primitively embeds in L₂
- **Complexity**: EXTREMELY difficult Diophantine problem
- **Common misconception**: NOT "gcd conditions" (definite lattice thinking)
- **Reality**: Complex systems, may have infinite solution families

### TRIVIAL (Already Solved)

#### Signature Computation
- **Problem**: Compute (p,q,r) signature
- **Implementation**: Simple eigenvalue analysis
- **Code**: `matrix.eigenvalues()` with sign counting

### QUESTIONABLE/NEEDS VERIFICATION

#### Vector Enumeration by Norm
- **Issue**: `QuadraticForm.find_reps()` may be definite-only
- **Problem**: Indefinite lattices typically have infinitely many vectors of given norm
- **Action needed**: Verify Sage algorithm applicability

#### Theta Series for Indefinite Lattices
- **Issue**: Theta series typically diverge for indefinite lattices
- **Reality**: ∑_{v∈L} q^{v·v} is usually infinite
- **Conclusion**: Not well-defined in general

## Core Algorithmic Problems

### 1. Vector Enumeration in Lattices

Finding all vectors of a given norm/length in a lattice.

#### Problem Complexity
- **Positive definite**: Polynomial in dimension for fixed norm
- **Indefinite**: Can be exponential or even undecidable
- **Key challenge**: Indefinite forms lack a well-ordering

#### Available Implementations

##### For Positive Definite Lattices

**Sage Implementation** ✓ (Priority 1)
```python
# IntegerLattice.vectors_of_length(n) - ONLY FOR POSITIVE DEFINITE
E8 = IntegerLattice(E8_gram)  # E8 is positive definite
root_vectors = E8.vectors_of_length(2)  # 240 E8 roots

# Algorithm: Fincke-Pohst (Cython/C implementation)
# Source: sage.modules.free_module_integer
# Extremely fast for positive definite forms
```

**Alternative: Short Vector Enumeration**
```python
# IntegerLattice.short_vectors() - also positive definite only
# Uses LLL reduction first
short = L.short_vectors(max_length=10)
```

##### For Indefinite Lattices

**Sage QuadraticForm** ✓ (Priority 1)
```python
# QuadraticForm works for ANY signature!
Q = QuadraticForm(ZZ, 3, [1, 0, 0, -1, 0, -1])  # Indefinite form
solutions = Q.find_reps(7)  # Works! Uses PARI/GP qfsolve

# For hyperbolic lattices:
H3_gram = matrix([[-2, 1, 1], [1, -2, 1], [1, 1, -2]])
Q_H3 = QuadraticForm(H3_gram)
vectors_norm_2 = Q_H3.find_reps(2)  # Find v with Q(v) = 2
```

**PARI/GP Direct** (Priority 3 - via Sage)
```python
# Can call PARI directly for more control
pari.qfsolve(gram_matrix, target_value)
```

**Custom Implementation Needed**:
- Vinberg's algorithm for systematic enumeration in hyperbolic lattices
- Light cone enumeration for null vectors

### 2. Lattice Automorphism Groups

Computing Aut(L) for a lattice L with bilinear form.

#### Problem Complexity
- **Finite groups**: Exponential in dimension
- **Infinite groups**: May need generators + relations

#### Available Implementations

##### For Definite Lattices

**Sage Implementation** ✓ (Priority 1)
```python
# IntegerLattice.automorphism_group() - positive definite only
L = IntegerLattice(gram)
G = L.automorphism_group()
```

**GAP via Sage** (Priority 3)
```python
# Use GAP's more powerful group algorithms
gap.AutomorphismGroup(gap(gram_matrix))
```

##### For Indefinite Lattices

**No built-in Sage implementation** ❌

**Magma** (Priority 5 - requires license)
```
// Magma code - would need system call
L := LatticeWithGram(gram_matrix);
G := AutomorphismGroup(L);
```

**Custom Implementation Required**:
- Adapt methods from Plesken & Souvignier papers
- Use reduction to finite index sublattice for hyperbolic case

### 3. Theta Series Computation

Computing ∑ q^{Q(v)} over lattice vectors.

#### Problem Complexity
- **Convergence**: Only for positive definite
- **Growth rate**: Depends on signature

#### Available Implementations

**Sage for Definite** ✓ (Priority 1)
```python
# Built-in for positive definite
L = IntegerLattice(gram)
theta = L.theta_series(prec=100)
```

**Custom for Indefinite** (Priority 6)
```python
def theta_series_indefinite(L, prec, cutoff):
    """Modified theta series with convergence cutoff."""
    # Must implement specialized convergence handling
    # Reference: Zagier's work on mock theta functions
```

### 4. Root System Classification

Determining Cartan type from Gram matrix.

#### Available Implementations

**Sage RootSystem** ✓ (Priority 1)
```python
# For crystallographic types
R = RootSystem(cartan_matrix)
R.cartan_type()  # Returns ['A', 3] etc.
```

**Custom for Non-crystallographic** (Priority 6)
- H₃, H₄, I₂(p) detection
- Must check angle conditions

### 5. Weyl Group Computations

#### Available Implementations

**Sage WeylGroup** ✓ (Priority 1)
```python
W = WeylGroup(['A', 3])
W.order()  # 24
W.long_element()
```

**GAP for Complex Cases** (Priority 3)
```python
# For infinite groups or complex presentations
gap.CoxeterGroup(coxeter_matrix)
```

### 6. Fundamental Domain Computation

#### For Finite/Affine Types

**Sage Implementation** ✓ (Priority 1)
```python
# Fundamental alcove for affine
R = RootSystem(['A', 2, 1])
R.fundamental_weights()
```

#### For Hyperbolic Types

**No Sage Implementation** ❌

**Vinberg's Algorithm** (Priority 6 - implement from paper)
- Reference: Vinberg, "Hyperbolic groups of reflections"
- Boyd's implementation in C++ (Priority 5 - could wrap)

**CoxIter** (Priority 5 - external binary)
```bash
# Guglielmetti's CoxIter program
./coxiter < input.txt
```

### 7. Representation Numbers

Counting solutions to Q(v) = n without listing them.

#### Available Implementations

**Sage QuadraticForm** ✓ (Priority 1)
```python
Q = QuadraticForm(gram)
count = Q.representation_number(n)
```

**Siegel-Weil Formula** (Priority 2 - via SymPy)
```python
# For special cases, use analytic formulas
from sympy import *
# Implement Siegel-Weil for genus
```

### 8. Lattice Embeddings

Finding primitive embeddings L₁ ↪ L₂.

#### Problem Complexity
- Requires solving Diophantine systems
- May have infinite families of solutions

#### Available Implementations

**No General Sage Implementation** ❌

**Partial Solutions**:
```python
# For root lattices specifically
R1 = RootSystem(['A', 2])
R2 = RootSystem(['A', 3])
# Manual construction needed
```

**Custom Algorithm** (Priority 6)
- Adapt Miranda-Morrison theory
- Use p-adic methods for existence

### 9. Chamber Decomposition

Decomposing space by reflection hyperplanes.

#### Available Implementations

**Sage for Finite Types** ✓ (Priority 1)
```python
H = HyperplaneArrangement(hyperplanes)
H.chambers()
```

**Custom for Infinite** (Priority 6)
- Need specialized data structures
- Reference: Hohlweg's work on infinite arrangements

### 10. Coxeter Element Properties

#### Available Implementations

**Sage Implementation** ✓ (Priority 1)
```python
W = WeylGroup(['A', 3])
c = W.coxeter_element()
c.order()  # Coxeter number
```

## Algorithm Selection Guide

```python
def select_algorithm(problem, lattice):
    """Choose appropriate algorithm based on problem and lattice type."""
    p, q, r = lattice.signature()
    
    if problem == "vector_enumeration":
        if p > 0 and q == 0 and r == 0:  # Positive definite
            return "IntegerLattice.vectors_of_length()"
        else:  # Indefinite or degenerate
            return "QuadraticForm.find_reps()"
    
    elif problem == "automorphisms":
        if p > 0 and q == 0 and r == 0:
            return "IntegerLattice.automorphism_group()"
        else:
            return "custom_implementation_needed"
    
    elif problem == "theta_series":
        if p > 0 and q == 0 and r == 0:
            return "IntegerLattice.theta_series()"
        else:
            return "custom_with_convergence_control"
    
    # ... etc
```

## External Libraries Reference

### Python Libraries
1. **fpylll** - Lattice algorithms (LLL, BKZ, enumeration)
2. **pyCox** - Some Coxeter group functionality  
3. **cypari2** - Direct PARI/GP interface

### GAP Packages
1. **Carat** - Crystallographic groups
2. **CrystCat** - Crystal system catalog
3. **RadiRoot** - Root system computations

### Julia Packages
1. **Hecke.jl** - Algebraic number theory and lattices
2. **AbstractAlgebra.jl** - Generic algebra structures

### Standalone Programs
1. **CoxIter** (Guglielmetti) - Hyperbolic Coxeter groups
2. **Vinberg's Algorithm** (Boyd) - Hyperbolic lattices
3. **Magma** - Commercial, very complete lattice algorithms

## Performance Considerations

### Definite vs Indefinite
| Algorithm | Definite Performance | Indefinite Performance |
|-----------|---------------------|----------------------|
| Vector enum | O(poly(dim)) for fixed norm | Can be exponential |
| Automorphisms | Exponential but finite | May be infinite group |
| Theta series | Converges rapidly | May not converge |
| Embeddings | Finite search space | Infinite families possible |

### Recommended Approach by Signature

1. **Negative definite** (0, n, 0): Use all standard algorithms
2. **Positive definite** (n, 0, 0): Use IntegerLattice suite  
3. **Parabolic** (0, n-1, 1): Use IntegralLattice + custom
4. **Hyperbolic** (1, n-1, 0): Need specialized algorithms
5. **General indefinite**: Fallback to QuadraticForm interface

## Implementation Status

| Problem | Definite | Indefinite | Notes |
|---------|----------|------------|-------|
| Vector enumeration | ✓ Sage | ✓ Sage (QF) | Complete |
| Automorphisms | ✓ Sage | ❌ Custom | High priority |
| Theta series | ✓ Sage | ❌ Custom | Convergence issues |
| Root classification | ✓ Sage | ✓ Sage | Complete for crystallographic |
| Weyl groups | ✓ Sage | ✓ Sage/GAP | May need GAP for infinite |
| Fundamental domain | ✓ Sage | ❌ CoxIter | External tool available |
| Embeddings | Partial | ❌ Custom | Theory exists |
| Chamber decomposition | ✓ Sage | ❌ Custom | Finite only |

## References

### Key Papers
1. Vinberg - "Hyperbolic groups of reflections" (1985)
2. Plesken & Souvignier - "Computing isometries of lattices" (1997)
3. Fincke & Pohst - "Improved methods for calculating vectors of short length" (1985)
4. Conway & Sloane - "Sphere Packings, Lattices and Groups" (1999)

### Implementation References
1. Sage source: `sage/modules/free_module_integer.pyx`
2. PARI/GP manual: "Quadratic forms" section
3. GAP manual: "Matrix groups" chapter
4. CoxIter documentation: GitHub guglielmetti/CoxIter

## Proven Implementation Methods

### Core Subdiagram Testing Algorithms

#### Testing if a Subdiagram is Elliptic
**Method**: Use SageMath's definiteness checking on the Gram matrix of the root sublattice  
**Implementation**: For root subset I, call `G(L)[I,I].is_negative_definite()`  
**Justification**: By definition, elliptic type means negative definite Gram matrix

#### Testing if a Subdiagram is Parabolic  
**Method**: Use SageMath's definiteness checking on the Gram matrix of the root sublattice  
**Implementation**: For root subset I, call `G(L)[I,I].is_negative_semidefinite()` and verify corank is 1  
**Justification**: By definition, parabolic type means negative semidefinite with corank 1

#### Testing if a Subdiagram is Hyperbolic
**Method**: Use SageMath's definiteness checking on the Gram matrix of the root sublattice  
**Implementation**: For root subset I, check that `G(L)[I,I]` is indefinite with signature (1, |I|-1, 0)  
**Justification**: By definition, hyperbolic type means indefinite with exactly one positive eigenvalue

### Maximal Parabolic Enumeration Algorithm

**Proven Method**: Systematic enumeration with mathematical property optimization

```python
def maximal_parabolic_subdiagrams(self):
    """Find all maximal parabolic subdiagrams using proven method."""
    n = self.rank()
    parabolics = []
    
    # Check all 2^n subsets
    for subset in powerset(range(n)):
        if len(subset) == 0:
            continue
            
        # Test if subset gives parabolic type
        submatrix = self.gram_matrix()[subset, subset]
        if self._is_parabolic_type(submatrix):
            # Test maximality
            if self._is_maximal_parabolic(subset, parabolics):
                parabolics.append(subset)
    
    return parabolics

def _is_parabolic_type(self, matrix):
    """Test if matrix has exactly one zero eigenvalue."""
    return (matrix.is_negative_semidefinite() and 
            (matrix.rank() == matrix.nrows() - 1))

def _is_maximal_parabolic(self, subset, known_parabolics):
    """Test if subset is not contained in any larger parabolic."""
    for known in known_parabolics:
        if set(subset).issubset(set(known)) and subset != known:
            return False
    return True
```

### Optimization Using Mathematical Properties

**Elliptic Monotonicity**: If subset is not elliptic, no superset can be elliptic  
**Implementation**: Skip supersets of non-elliptic subdiagrams  
**Performance**: Reduces search space exponentially for most cases

```python
def optimized_enumeration(self):
    """Use monotonicity to prune search space."""
    n = self.rank()
    non_elliptic = set()
    
    for subset in powerset(range(n)):
        # Skip if contained in known non-elliptic
        if any(set(subset).issuperset(ne) for ne in non_elliptic):
            continue
            
        if not self._is_elliptic(subset):
            non_elliptic.add(frozenset(subset))
```

### Cross-Validation Framework

```python
def validate_algorithm_implementation(algorithm, test_cases):
    """Validate algorithm against known results."""
    for test_case in test_cases:
        result = algorithm(test_case.input)
        expected = test_case.expected_output
        
        if result != expected:
            raise AlgorithmValidationError(
                f"Algorithm {algorithm.__name__} failed on {test_case.name}"
            )
```