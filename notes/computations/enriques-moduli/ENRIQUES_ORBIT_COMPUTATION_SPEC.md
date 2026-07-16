# Enriques Surface Orbit Computation: Technical Specification

**Version**: 1.0  
**Date**: 2025-08-06  
**Based on**: Dutour Sikirić & Hulek (2023) "Moduli of polarized Enriques surfaces -- computational aspects" [arXiv:2302.01679v2]

## 1. Executive Summary

This specification defines the requirements for implementing orbit computation algorithms for isotropic vectors in indefinite lattices, specifically targeting moduli spaces of polarized Enriques surfaces. The implementation extracts and modernizes algorithms from the Dutour Sikirić & Hulek paper while avoiding the complex C++ dependency web of their `polyhedral_common` repository.

## 2. Mathematical Background

### 2.1 Core Problem
- **Target**: Compute orbit representatives of isotropic vectors in indefinite quadratic lattices
- **Primary Use Case**: Moduli spaces of polarized Enriques surfaces  
- **Lattice Type**: M(1/2) = U ⊕ 2U ⊕ 2E₈(-1) (signature (2,18))
- **Isotropic Condition**: v^T Q v = 0 for vectors v in lattice

### 2.2 Theoretical Framework
Based on three core algorithms from Section 4 of the paper:

#### Algorithm 1: Matrix Group Intersection
- **Input**: Subgroups G₁, G₂ ⊆ GL_n(ℤ)
- **Output**: Representatives for G₁ ∩ G₂
- **Method**: Approximate models with iterative refinement

#### Algorithm 2: Orbit Representatives  
- **Input**: Indefinite quadratic form Q, target norm c
- **Output**: Representatives for orbits of vectors v with Q(v) = c
- **Method**: Short vectors + orbit enumeration with group actions

#### Algorithm 3: Eichler Transvection Criterion
- **Input**: Indefinite lattice L, element g ∈ O(L)
- **Output**: Check if g is an Eichler transvection
- **Method**: Characteristic polynomial analysis

### 2.3 Enriques Surface Specialization
- **Lattice**: U ⊕ 2U ⊕ 2E₈(-1) where:
  - U = hyperbolic plane [[0,1],[1,0]]
  - E₈ = root lattice (8×8 matrix)  
  - 2E₈(-1) = 2 × (negative definite E₈)
- **Target Vectors**: Norm-0 (isotropic) vectors
- **Applications**: Classification of Enriques surfaces with specific polarizations

## 3. Architecture Requirements

### 3.1 Language and Framework Selection
**Primary Implementation**: Julia/OSCAR.jl
- **Rationale**: Native support for indefinite lattices, built-in automorphism groups
- **Key Packages**: Hecke.jl, Indefinite.jl
- **Performance**: JIT compilation for computational efficiency

**Interface Layer**: Python/SageMath wrapper  
- **Rationale**: Final user accessibility and SageMath ecosystem integration
- **Method**: PyCall.jl for Julia-Python bridge

### 3.2 Modular Design

```
EnriquesOrbits.jl/
├── src/
│   ├── core/
│   │   ├── indefinite_forms.jl      # Core lattice operations
│   │   ├── approximate_models.jl    # Algorithm 1 implementation  
│   │   ├── orbit_computation.jl     # Algorithm 2 implementation
│   │   └── eichler_transvections.jl # Algorithm 3 implementation
│   ├── lattices/
│   │   ├── classical_lattices.jl    # U, E₆, E₇, E₈ definitions
│   │   ├── enriques_lattice.jl      # M(1/2) construction
│   │   └── lattice_utilities.jl     # I/O, conversion utilities
│   ├── interfaces/
│   │   ├── oscar_interface.jl       # OSCAR.jl integration
│   │   └── gap_interface.jl         # GAP system calls (fallback)
│   └── applications/
│       ├── enriques_moduli.jl       # High-level Enriques functions
│       └── examples.jl              # Test cases and examples
├── python_wrapper/
│   ├── enriques_orbits.py           # Python interface
│   └── sagemath_integration.py      # SageMath-specific features
└── tests/
    ├── unit_tests.jl                # Algorithm verification  
    ├── integration_tests.jl         # End-to-end testing
    └── benchmark_tests.jl           # Performance validation
```

## 4. Core Functionality Requirements

### 4.1 Indefinite Lattice Operations
```julia
# Core data structure
struct IndefiniteLattice{T}
    gram_matrix::Matrix{T}
    signature::Tuple{Int, Int}
    automorphism_group::Optional{Group}
end

# Required methods
function automorphism_group(L::IndefiniteLattice)
function is_isotropic(L::IndefiniteLattice, v::Vector) -> Bool
function evaluate_form(L::IndefiniteLattice, v::Vector) -> Number
function short_vectors(L::IndefiniteLattice, bound::Number) -> Vector{Vector}
```

### 4.2 Orbit Computation Interface
```julia
# Primary entry point - Algorithm 2 implementation
function orbit_representatives(
    L::IndefiniteLattice, 
    norm::Number = 0;
    max_iterations::Int = 1000,
    tolerance::Float64 = 1e-10
) -> Vector{Vector{Int}}

# Enriques-specific convenience function  
function enriques_isotropic_orbits(;
    polarization_degree::Int = 2
) -> Vector{Vector{Int}}
```

### 4.3 Classical Lattice Library
```julia
# Standard lattice constructors from paper's GAP code
function hyperbolic_plane() -> IndefiniteLattice     # U
function root_lattice_E8() -> IndefiniteLattice      # E₈  
function root_lattice_E7() -> IndefiniteLattice      # E₇
function root_lattice_E6() -> IndefiniteLattice      # E₆
function root_lattice_An(n::Int) -> IndefiniteLattice # A_n series
function root_lattice_Dn(n::Int) -> IndefiniteLattice # D_n series

# Lattice combination operations  
function direct_sum(lattices::Vector{IndefiniteLattice}) -> IndefiniteLattice
function scaled_lattice(L::IndefiniteLattice, factor::Int) -> IndefiniteLattice
```

### 4.4 Algorithm Implementation Requirements

#### Algorithm 1: Matrix Group Intersection
```julia
function matrix_group_intersection(
    G1::Vector{Matrix{Int}}, 
    G2::Vector{Matrix{Int}},
    approximate_bound::Int = 100
) -> Vector{Matrix{Int}}
```

#### Algorithm 2: Orbit Representatives (Core Function)
```julia  
function compute_orbit_representatives(
    gram_matrix::Matrix{Rational},
    target_norm::Number,
    method::Symbol = :approximate_models
) -> OrbitResult

struct OrbitResult
    representatives::Vector{Vector{Int}}
    orbit_sizes::Vector{Int}
    automorphism_generators::Vector{Matrix{Int}}
    computation_metadata::Dict{String, Any}
end
```

#### Algorithm 3: Eichler Transvections
```julia
function is_eichler_transvection(
    L::IndefiniteLattice, 
    g::Matrix{Int}
) -> Bool
```

## 5. Performance Requirements

### 5.1 Computational Targets
- **Enriques Lattice Dimension**: 20×20 matrices
- **Expected Orbit Count**: 10-100 representatives for typical cases
- **Target Runtime**: < 5 minutes for standard Enriques computation
- **Memory Usage**: < 2GB for typical cases

### 5.2 Scalability Requirements
- **Matrix Size**: Support up to 50×50 indefinite forms
- **Arithmetic**: Exact rational arithmetic throughout
- **Precision**: No floating-point approximations in final results
- **Parallelization**: Support for multi-threaded orbit computation

## 6. Interface Requirements

### 6.1 Julia/OSCAR Interface
```julia
# Integration with OSCAR's lattice types
function from_oscar_lattice(L::Oscar.ZZLat) -> IndefiniteLattice
function to_oscar_lattice(L::IndefiniteLattice) -> Oscar.ZZLat

# Use OSCAR's automorphism group computations where possible
function oscar_automorphism_group(L::IndefiniteLattice) -> Oscar.Group
```

### 6.2 Python/SageMath Wrapper
```python
# Primary user interface
class EnriquesOrbitComputation:
    def __init__(self, lattice_specification=["U", "2U", "2E8"]):
        """Initialize from lattice specification list"""
        
    def compute_orbits(self, norm=0, method="approximate"):
        """Main computation function"""
        return OrbitResult(representatives, metadata)
    
    def to_sagemath_lattice(self):
        """Convert to SageMath IntegralLattice"""
        
# Convenience functions
def enriques_surface_orbits(degree=2):
    """One-line interface for Enriques computation"""
    
def classical_lattice(name: str):  
    """Get standard lattices: 'U', 'E8', 'E7', 'E6', 'A5', 'D4', etc."""
```

### 6.3 I/O Requirements
- **Input Formats**: 
  - Matrix files (compatible with Dutour Sikirić format)
  - SageMath matrix objects
  - OSCAR lattice objects
  - String specifications (["U", "2U", "2E8"])
- **Output Formats**:
  - JSON for programmatic use
  - Human-readable text summaries
  - SageMath/OSCAR native objects

## 7. Testing and Validation Requirements

### 7.1 Correctness Validation
- **Algorithm Verification**: Compare against known results from the paper
- **Enriques Test Case**: Reproduce paper's results for U ⊕ 2U ⊕ 2E₈(-1)
- **Orbit Verification**: Check that computed representatives are inequivalent
- **Automorphism Verification**: Validate group actions preserve the quadratic form

### 7.2 Test Cases
```julia
# From paper's GAP test code (AllTests.g)
test_cases = [
    (["U", "2U"], 2),           # Basic hyperbolic
    (["U", "2U", "A2"], 2),     # With root lattice
    (["U", "2U", "A3"], 2),     # Larger root lattice
    (["U", "2U", "A2", "A2"], 2), # Multiple components
    (["U", "U", "E7"], 2),      # E7 case
    (["U", "2U", "2E8"], 2)     # Enriques case (main target)
]
```

### 7.3 Performance Benchmarks
- **Baseline**: Compare against Dutour Sikirić C++ implementation (if buildable)
- **Regression Testing**: Ensure performance doesn't degrade across versions
- **Memory Profiling**: Track memory usage for large lattices

## 8. Dependencies and External Libraries

### 8.1 Julia Dependencies
- **OSCAR.jl**: Primary mathematical framework
- **Hecke.jl**: Lattice and quadratic form support  
- **Indefinite.jl**: Specialized indefinite form operations
- **LinearAlgebra.jl**: Matrix operations (standard library)
- **PyCall.jl**: Python interface layer

### 8.2 Python Dependencies  
- **SageMath**: Target integration platform
- **NumPy**: Numerical arrays
- **julia**: Python-Julia interface

### 8.3 System Requirements
- **Julia Version**: ≥ 1.9.0
- **Python Version**: ≥ 3.8  
- **RAM**: 4GB minimum, 8GB recommended
- **OS**: Linux, macOS, Windows with WSL

## 9. Documentation Requirements

### 9.1 Mathematical Documentation
- **Algorithm Description**: Detailed explanation of the three core algorithms
- **Theoretical Background**: Indefinite lattice theory primer
- **Enriques Applications**: Connection to algebraic geometry

### 9.2 Technical Documentation  
- **API Reference**: Complete function documentation
- **Installation Guide**: Step-by-step setup instructions
- **Tutorial Notebooks**: Jupyter notebooks with examples
- **Performance Guide**: Optimization tips for large computations

### 9.3 Research Documentation
- **Validation Report**: Comparison with paper's results
- **Benchmark Results**: Performance analysis
- **Extension Guide**: How to add new lattice types or algorithms

## 10. Delivery and Timeline

### 10.1 Development Phases
1. **Phase 1 (2-3 weeks)**: Core Julia implementation
   - Algorithm 2 (orbit computation)
   - Basic indefinite lattice operations
   - Classical lattice library

2. **Phase 2 (1-2 weeks)**: OSCAR integration
   - Interface with OSCAR's lattice types
   - Leverage existing automorphism group computations
   - Performance optimization

3. **Phase 3 (1-2 weeks)**: Python wrapper and validation
   - SageMath integration layer
   - Comprehensive testing against paper's results
   - Documentation and examples

### 10.2 Success Criteria
- **Functional**: Successfully computes orbit representatives for Enriques lattice
- **Performance**: Completes standard cases within target runtime
- **Accuracy**: Results match theoretical expectations and paper's examples
- **Usability**: Simple one-line interface for common use cases
- **Integration**: Seamless operation within SageMath environment

### 10.3 Risk Mitigation
- **Complexity Risk**: Start with Algorithm 2 only, add others incrementally
- **Performance Risk**: Benchmark early, optimize hotspots with C extensions if needed
- **Integration Risk**: Maintain fallback to pure SageMath implementation
- **Mathematical Risk**: Validate against multiple test cases from different sources

---

**Document Prepared By**: Research Analysis Team  
**Review Required**: Mathematical correctness, implementation feasibility  
**Next Steps**: Approve specification → Begin Phase 1 implementation