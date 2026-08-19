<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/TODO.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is an ALGORITHM/REQUIREMENT SURVEY written against SageMath as it
stood in the source tree. Rows now owned by the preamble, and errors the
audit recorded, are listed in the README.md of this directory.
-->

# Mathematical Research TODOs

This document tracks major mathematical research and implementation tasks for future development.

## Algorithmic Research Needed

### 1. Vinberg's Algorithm Implementation
**Status**: Requires mathematical research
**Description**: Currently we only have interface specifications. Need to research and implement:
- Which variant of Vinberg's algorithm to use (classical vs. modern optimizations)
- Convergence guarantees and stopping criteria
- Arithmetic conditions for applicability
- Computational complexity analysis
- Connections to work of Vinberg, Kaplinskaya, Bugaenko, Allcock, etc.

### 2. Field Extension Algorithms  
**Status**: Mathematical foundation needed
**Description**: How to handle lattices over number fields concretely:
- Representation of lattices over ℤ[√d], cyclotomic integers
- Algorithms for base change between different number rings
- Transition between ℤ-lattices and number field lattices
- Integration with Sage's number field machinery

### 3. Discriminant Form Computations
**Status**: Algorithmic specifications needed  
**Description**: Concrete algorithms for:
- Computing quadratic form q_L: A_L → ℚ/ℤ from lattice data
- Genus symbol construction for all primes
- Brown invariant (signature mod 8) calculations
- Classification within genera

## Mathematical Connections for Future Work

### 1. Modular Forms and Theta Series
**Context**: Definite lattices primarily
**Research areas**:
- Theta series associated to positive definite lattices
- Connections to Eisenstein series and cusp forms
- Weight and level computations
- Integration with Sage's modular forms package

### 2. Genus Theory and Class Field Theory
**Context**: Definite and indefinite lattices
**Research areas**:
- Genus representatives and classification
- Mass formulas (Smith-Minkowski-Siegel)
- Connections to class field theory
- Hasse-Minkowski local-global principles

### 3. Coding Theory Applications  
**Context**: Positive definite lattices
**Research areas**:
- Sphere packing bounds and kissing numbers
- Construction of lattices from linear codes
- Decoding algorithms and nearest neighbor problems
- Weight enumerators and MacWilliams identity

### 4. Computational Number Theory Integration
**Context**: All lattice types
**Research areas**:
- LLL and BKZ reduction algorithms
- Short vector problems and lattice basis reduction
- Connections to cryptographic lattice problems
- Integration with computational algebra systems

### 5. Automorphic Forms and L-functions
**Context**: Quadratic forms over number fields
**Research areas**:
- Theta series as automorphic forms
- L-functions associated to quadratic forms
- Special values and periods
- Connections to arithmetic algebraic geometry

## Literature Integration Tasks

### 1. Classical References
**Need**: Cross-references to foundational papers
- Conway-Sloane "Sphere Packings, Lattices and Groups"
- Vinberg's papers on hyperbolic reflection groups
- Serre's "Course in Arithmetic" 
- Cassels "Rational Quadratic Forms"
- O'Meara "Introduction to Quadratic Forms"

### 2. Modern Research Connections
**Need**: Integration with current research
- Connections to work on K3 surfaces and algebraic cycles
- Mirror symmetry and lattice polarizations
- Arithmetic dynamics and rational points
- Geometric representation theory

### 3. Computational References
**Need**: Algorithmic literature
- Computational approaches to Vinberg's algorithm
- Efficient algorithms for quadratic forms
- Computer algebra approaches to lattice problems

## Implementation Architecture for Research

### 1. Extensible Algorithm Framework
**Goal**: Support multiple algorithmic approaches
- Plugin architecture for different Vinberg implementations
- Benchmarking framework for algorithm comparison
- Caching strategies for expensive computations

### 2. Mathematical Verification System
**Goal**: Ensure computational correctness
- Cross-checking against multiple sources/algorithms
- Symbolic computation verification where possible
- Connection to proof assistants (Lean, Coq) for critical results

### 3. Research Data Management
**Goal**: Support large-scale mathematical investigations
- Database of computed examples and counterexamples
- Systematic enumeration tools
- Export to mathematical databases (OEIS, L-functions database)

## Mathematical Examples Database

### 1. Classical Examples Database
**Need**: Complete worked examples
- All irreducible finite Coxeter groups
- Standard indefinite lattices (hyperbolic plane, Lorentzian lattices)
- Classical modular lattices (A_n, D_n, E_6, E_7, E_8)
- Non-crystallographic cases (H_3, H_4, I_2(p))

### 2. Research Examples Database  
**Need**: Examples from active research
- Vinberg's classification results
- K3 surface lattice polarizations
- Hyperbolic Coxeter polytopes with small volume
- 2-elementary lattices from algebraic geometry

### 3. Computational Challenge Problems
**Need**: Benchmark problems for algorithms
- Large-scale Vinberg algorithm computations
- Classification problems in high dimensions
- Optimization problems (shortest vector, etc.)

## Integration with Mathematical Software

### 1. Sage Integration Improvements
**Current**: Basic integration exists
**Future**: Deeper integration with Sage's mathematical libraries
- Number theory packages
- Algebraic geometry tools  
- Modular forms machinery
- Symbolic computation systems

### 2. External Software Connections
**Research need**: Connections to specialized tools
- GAP for group theory computations
- Magma for number theory and algebraic geometry
- Singular for computational commutative algebra
- Export formats for visualization (polymake, etc.)

### 3. Mathematical Database Integration
**Research need**: Connections to mathematical databases
- OEIS for sequence recognition
- LMFDB for L-functions and modular forms
- Online lattice catalogs and repositories

---

*This TODO list represents long-term research goals. Many items require significant mathematical research and are not immediate implementation tasks.*