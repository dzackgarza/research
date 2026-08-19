<!--
Origin: gitclones/Coxeter/research/archive/2025-01-27-docs-restructure/IMPLEMENTATION_GUIDE.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of this
corpus.
-->

# Implementation Guide

This document provides practical guidance for implementing the Coxeter lattice framework.

## Getting Started

### Prerequisites
- **SageMath 9.0+**: Core mathematical infrastructure
- **Python 3.8+**: For type annotations and modern language features
- **Pydantic**: For data validation and type safety

### Development Setup
```bash
# Clone repository
git clone [repository-url]
cd Coxeter

# Review conventions
cat CONVENTIONS.md

# Examine existing API structure  
ls docs/api/interfaces/
```

## Core Implementation Strategy

### 1. Algebraic Lattice Foundation

The central innovation is a minimal lattice class supporting natural mathematical notation:

```python
class AlgebraicLattice(FreeModule_generic):
    """
    Lattice with symbolic basis supporting natural algebraic notation.
    
    EXAMPLES::
    
        sage: U = AlgebraicLattice(['e', 'f'], 
        ....:                      bilinear_form={('e','f'): 1, ('f','e'): 1})
        sage: e, f = U.e, U.f
        sage: v = 2*e + 3*f
        sage: v * v  # Bilinear form evaluation
        12
    """
```

**Design Rationale**: 
- Inherits from `FreeModule_generic` for ~100 lines vs thousands from `CombinatorialFreeModule`
- Full control over implementation for indefinite lattice optimization
- Natural mathematical syntax: `v * w` for bilinear form evaluation

### 2. Implementation Priorities

#### Phase 1: Core Classes (Week 1-2)
1. **AlgebraicLattice**: Basic class with symbolic basis access
2. **Element Operations**: Bilinear form evaluation, arithmetic operations
3. **Factory Functions**: Convenient constructors from various inputs
4. **Basic Properties**: Signature computation, type classification

#### Phase 2: Mathematical Operations (Week 3-4)  
1. **Subdiagram Enumeration**: Efficient algorithms for maximal parabolic finding
2. **Morphism Integration**: Proper categorical morphisms between lattices
3. **Algorithm Selection**: Automatic choice between definite/indefinite algorithms
4. **Validation Framework**: Cross-checking against known results

#### Phase 3: SageMath Integration (Week 5-6)
1. **Category Framework**: Proper integration with SageMath's category system
2. **Coercion System**: Principled coercion along canonical morphisms
3. **Documentation**: Complete docstring and example system
4. **Testing**: Comprehensive test coverage including edge cases

## Key Implementation Patterns

### Construction from Sage Objects

**ALWAYS** construct from SageMath's canonical objects:

```python
# RIGHT - construct from Sage
def from_coxeter_type(cls, coxeter_type):
    R = RootSystem(coxeter_type)
    roots = R.root_lattice().simple_roots()
    gram = compute_gram_from_roots(roots)
    return cls.from_gram_matrix(gram)

# WRONG - hard-code matrices  
def from_a3_wrong():
    gram = matrix([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])  # VIOLATES conventions!
    return cls.from_gram_matrix(gram)
```

### Algorithm Selection by Signature

Automatically choose appropriate algorithms based on lattice signature:

```python
def vectors_of_norm(self, n):
    """Find vectors with given norm using appropriate algorithm."""
    p, q, r = self.signature()
    
    if q == 0 and r == 0:  # Positive definite
        # Use fast IntegerLattice methods
        IL = IntegerLattice(self.gram_matrix())
        return [self(v) for v in IL.vectors_of_length(n)]
    else:  # Indefinite
        # Use QuadraticForm for general case
        QF = QuadraticForm(self.gram_matrix())
        return [self.from_vector(v) for v in QF.find_reps(n)]
```

### Bilinear Form Implementation

The core innovation is overloading `*` for bilinear form evaluation:

```python
class Element(FreeModule_generic.Element):
    def __mul__(self, other):
        """v * w evaluates bilinear form, otherwise scalar multiplication."""
        if hasattr(other, 'parent') and other.parent() is self.parent():
            # Bilinear form evaluation
            result = self.parent().base_ring().zero()
            form = self.parent()._bilinear_form_dict
            
            for key1, coeff1 in self._monomial_coefficients.items():
                for key2, coeff2 in other._monomial_coefficients.items():
                    if (key1, key2) in form:
                        result += coeff1 * coeff2 * form[(key1, key2)]
            return result
        else:
            # Scalar multiplication
            return FreeModule_generic.Element.__mul__(self, other)
```

## Algorithm Implementation Guidelines

### For Indefinite Lattices

#### Vector Enumeration
- **Positive Definite**: Use `IntegerLattice.vectors_of_length()`
- **Indefinite**: Use `QuadraticForm.find_reps()` via PARI/GP

#### Automorphism Groups  
- **Positive Definite**: Use `IntegerLattice.automorphism_group()`
- **Indefinite**: Custom implementation required (no standard Sage method)

#### Signature Analysis
- **All Types**: Simple eigenvalue counting with exact arithmetic
- **Implementation**: `matrix.eigenvalues()` over exact fields

### Mathematical Validation

Every algorithm must be validated against known results:

```python
def test_finite_types():
    """Validate against all known finite Coxeter types."""
    for coxeter_type in ["A_1", "A_2", "A_3", "B_2", "B_3", "C_2", "C_3", "D_4", "D_5", 
                         "E_6", "E_7", "E_8", "F_4", "G_2", "H_3", "H_4"]:
        L = AlgebraicLattice.from_coxeter_type(coxeter_type)
        assert L.is_finite()  # Must be elliptic
        assert len(L.maximal_parabolic_subdiagrams()) == 0
```

## Common Implementation Pitfalls

### 1. Gram vs Cartan Confusion
```python
# WRONG - assuming relationship holds generally
def gram_from_cartan_wrong(cartan_matrix):
    return -cartan_matrix  # Only works for ADE!

# RIGHT - compute from actual inner products  
def gram_from_cartan_correct(cartan_type):
    R = RootSystem(cartan_type)
    roots = R.root_lattice().simple_roots()
    return compute_gram_matrix(roots)
```

### 2. Definite vs Indefinite Algorithm Confusion
```python
# WRONG - assuming positive definite methods work
def bad_vector_enumeration(lattice, norm):
    return lattice.vectors_of_length(norm)  # May not exist!

# RIGHT - check signature first
def good_vector_enumeration(lattice, norm):
    if lattice.is_positive_definite():
        return lattice.vectors_of_length(norm)
    else:
        return lattice._indefinite_vector_enumeration(norm)
```

### 3. Floating Point in Exact Computation
```python
# WRONG - floating point for exact computations
def bad_eigenvalue_check(matrix):
    evs = matrix.eigenvalues(RDF)  # Approximate!
    return any(abs(ev) < 1e-10 for ev in evs)

# RIGHT - exact computation
def good_eigenvalue_check(matrix):
    evs = matrix.eigenvalues(QQ)  # Exact
    return any(ev == 0 for ev in evs)
```

## Testing Strategy

### Unit Tests
- **Mathematical Properties**: Verify all known theorems
- **Edge Cases**: Test boundary conditions and degenerate cases
- **Algorithm Correctness**: Cross-check against multiple methods

### Integration Tests  
- **SageMath Compatibility**: Ensure proper integration
- **Performance**: Verify acceptable performance on realistic examples
- **Regression**: Prevent performance degradation

### Validation Tests
- **Literature Verification**: Check against published results
- **Cross-Platform**: Verify behavior across different systems
- **Mathematical Consistency**: Ensure internal consistency

## Performance Considerations

### Caching Strategy
```python
@cached_method
def signature(self):
    """Cache expensive eigenvalue computations."""
    evs = self.gram_matrix().eigenvalues()
    # ... signature computation
```

### Algorithm Optimization
- **Eigenvalue Caching**: Store eigenvalues for repeated submatrix queries
- **Monotonicity Pruning**: Use mathematical properties to avoid computation
- **Parallel Processing**: Independent subdiagram analysis can be parallelized

### Memory Management
- **Lazy Evaluation**: Compute properties only when needed
- **Efficient Storage**: Use sparse representations when appropriate
- **Cache Invalidation**: Clear caches when underlying data changes

## Documentation Standards

### Docstring Format
```python
def maximal_parabolic_subdiagrams(self):
    """
    Return all maximal parabolic subdiagrams.
    
    A parabolic subdiagram is defined as -G being positive semidefinite (affine type).
    Maximal means not contained in any larger parabolic subdiagram.
    
    OUTPUT:
    List of vertex subsets corresponding to maximal parabolic subdiagrams.
    
    EXAMPLES::
    
        sage: L = AlgebraicLattice.from_coxeter_type("A_3")
        sage: L.maximal_parabolic_subdiagrams()
        []  # Finite types have no parabolic subdiagrams
        
    ALGORITHM:
    Uses eigenvalue analysis with elliptic monotonicity pruning.
    See ALGORITHMS.md for detailed complexity analysis.
    """
```

### Mathematical References
- Include relevant theorem statements and proofs references
- Link to external mathematical sources when appropriate
- Explain algorithmic choices and mathematical assumptions

## Testing

For comprehensive testing strategies, framework details, and validation approaches, see **[TESTING.md](TESTING.md)**.

This implementation guide provides the foundation for building a mathematically rigorous and computationally efficient lattice framework.