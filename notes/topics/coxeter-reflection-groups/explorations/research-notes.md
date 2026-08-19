<!--
Origin: gitclones/Coxeter/research/explorations/research-notes.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is RESEARCH PROSE from the Coxeter working trees: a mathematical
account written for this project. Errors the audit found in it are listed in
the README.md of this directory.
-->

# Research Notes: Active Investigations and Ideas

This document contains ongoing research notes, open questions, and preliminary investigations for the Coxeter maximal parabolic project.

## Current Research Questions

### 1. Computational Complexity and Optimization

#### Question: Optimal Pruning Strategies
**Problem**: Can we improve upon eigenvalue monotonicity pruning?

**Current Approach**: Use eigenvalue interlacing to prune non-elliptic branches.

**Research Ideas**:
- **Signature-based pruning**: Use more detailed signature information
- **Combinatorial constraints**: Exploit graph-theoretic properties
- **Machine learning**: Train models to predict classification from partial information

**Experimental Approach**:
```python
def experimental_pruning(partial_diagram):
    # Traditional eigenvalue pruning
    if not eigenvalue_monotonicity_test(partial_diagram):
        return False
    
    # Additional signature-based test
    if not signature_inheritance_test(partial_diagram):
        return False
    
    # Graph-theoretic constraint
    if not combinatorial_feasibility_test(partial_diagram):
        return False
    
    return True
```

**Open Questions**:
- What is the theoretical complexity lower bound?
- Can quantum algorithms provide speedup?
- Are there polynomial-time approximation algorithms?

#### Question: Parallel Algorithm Design
**Problem**: How to efficiently parallelize maximal parabolic enumeration?

**Challenges**:
- Irregular tree structure makes load balancing difficult
- Pruning creates data dependencies
- Communication overhead for shared state

**Proposed Approaches**:
1. **Work-stealing**: Dynamic load balancing with pruning
2. **Domain decomposition**: Partition vertex sets systematically
3. **Speculative computation**: Compute speculatively and discard if pruned

**Research Metrics**: Speedup vs number of cores, memory usage patterns.

### 2. Mathematical Theory Extensions

#### Question: Galois Theory of Classification Results
**Problem**: How do Galois automorphisms act on maximal parabolic enumerations?

**Context**: Non-crystallographic types require field extensions, introducing Galois groups.

**Specific Questions**:
- Do maximal parabolic counts remain invariant under Galois automorphisms?
- How do field automorphisms permute the actual maximal parabolic subdiagrams?
- Can we exploit Galois symmetry to reduce computation?

**Research Approach**:
```python
def study_galois_action(coxeter_type, field_extension):
    """Study how Galois group acts on classification results."""
    base_results = enumerate_maximal_parabolics(coxeter_type)
    
    galois_group = field_extension.galois_group()
    orbit_results = {}
    
    for sigma in galois_group:
        # Apply field automorphism to Gram matrix
        transformed_gram = apply_automorphism(gram_matrix, sigma)
        transformed_results = enumerate_maximal_parabolics(transformed_gram)
        orbit_results[sigma] = transformed_results
    
    return analyze_orbit_structure(orbit_results)
```

**Expected Results**: Galois-equivariant enumeration algorithms.

#### Question: Higher-Dimensional Generalizations
**Problem**: How does the theory extend to higher dimensions?

**Current Status**: Most work focuses on dimensions 3-5 for computational feasibility.

**Research Directions**:
- Asymptotic behavior of maximal parabolic counts
- Dimensional analysis of volume finiteness criteria
- Connections to higher-dimensional topology

#### Question: Arithmetic Properties
**Problem**: Which finite covolume hyperbolic Coxeter groups are arithmetic?

**Context**: Arithmetic groups have special number-theoretic properties.

**Research Strategy**:
- Systematic enumeration of small examples
- Analysis of discriminants and field properties
- Connection to quadratic form theory over number fields

### 3. Connections to Other Mathematical Areas

#### Question: Homotopy-Theoretic Interpretation
**Problem**: Can we develop a stable homotopy theory for bilinear modules?

**Motivation**: Modern algebraic topology uses stable ∞-categories instead of classical derived categories.

**Research Program**:
1. Define suspension functor on bilinear modules
2. Construct stable ∞-category of bilinear module spectra
3. Relate classical Ext/Tor to homotopy groups of spectra
4. Develop computational tools for spectral sequences

**Potential Applications**:
- New computational methods for homological algebra
- Connections to algebraic K-theory and L-theory
- Links to motivic homotopy theory

#### Question: Modular Forms and Theta Series
**Problem**: What modular properties do theta series of indefinite lattices have?

**Context**: Positive definite lattices have well-understood theta series theory.

**Research Challenges**:
- Indefinite theta series typically diverge
- Need regularization methods
- Connection to Eisenstein series

**Experimental Approach**: Study regularized theta series for specific hyperbolic lattices.

### 4. Computational Implementation Questions

#### Question: Exact Arithmetic Over Number Fields
**Problem**: How to efficiently implement exact arithmetic for non-crystallographic types?

**Current Status**: SageMath provides basic support, but optimization needed.

**Research Areas**:
- Optimized algorithms for cyclotomic field arithmetic
- Memory-efficient representation of algebraic numbers
- Fast algorithms for minimal polynomial computation

#### Question: Numerical Verification Methods
**Problem**: How to numerically verify exact symbolic results?

**Approach**: Interval arithmetic and certified computation.

**Implementation Strategy**:
```python
def verify_classification(gram_matrix, classification_result):
    """Verify exact classification using interval arithmetic."""
    # Convert to high-precision interval matrices
    interval_gram = IntervalMatrix(gram_matrix, precision=200)
    
    # Compute eigenvalue bounds
    eigenvalue_bounds = interval_gram.eigenvalue_bounds()
    
    # Verify classification is consistent with bounds
    return verify_consistency(eigenvalue_bounds, classification_result)
```

**Research Goal**: Develop certified algorithms with rigorous error bounds.

## Ongoing Experiments

### Experiment 1: Large-Scale Enumeration

**Goal**: Systematically enumerate maximal parabolics for all irreducible hyperbolic types up to rank 10.

**Current Status**: 
- Completed for ranks 3-5
- In progress for ranks 6-8
- Planning for ranks 9-10

**Data Collection**:
```python
experimental_data = {
    'rank': [],
    'type': [],
    'maximal_parabolic_count': [],
    'computation_time': [],
    'memory_usage': []
}
```

**Analysis Questions**:
- Growth rates of maximal parabolic counts
- Computational complexity patterns
- Outliers and exceptional cases

### Experiment 2: Field Extension Optimization

**Goal**: Optimize computations over cyclotomic fields for dihedral types I₂(p).

**Approach**: Compare different representations of 2cos(π/p).

**Methods**:
1. Standard cyclotomic field representation
2. Minimal polynomial representation  
3. Continued fraction approximation (for verification)

**Metrics**: Computation time, memory usage, numerical accuracy.

### Experiment 3: Geometric Visualization

**Goal**: Develop 3D visualization tools for hyperbolic fundamental domains.

**Current Tools**:
- Poincaré ball model rendering
- Hyperboloid model computations
- Interactive diagram manipulation

**Research Applications**:
- Intuition building for high-dimensional cases
- Verification of computational results
- Educational and presentation purposes

## Open Theoretical Problems

### Problem 1: Maximal Parabolic Enumeration Complexity
**Statement**: What is the computational complexity of enumerating maximal parabolic subdiagrams?

**Known Results**: 
- Naive algorithm is O(2^n)
- Pruning can provide significant speedup in practice
- No proven polynomial-time algorithm

**Research Directions**:
- Prove exponential lower bounds for worst-case inputs
- Identify polynomial-time special cases
- Develop approximation algorithms

### Problem 2: Universal Bounds on Maximal Parabolic Counts
**Statement**: Are there universal upper bounds on the number of maximal parabolic subdiagrams?

**Context**: Each hyperbolic Coxeter diagram has finite covolume iff all maximal parabolics are affine.

**Conjectures**:
- Number of maximal parabolics is bounded by exponential in rank
- Finite covolume condition provides stronger bounds
- Arithmetic cases may have additional constraints

### Problem 3: Algorithmic Classification of Finite Covolume Types
**Statement**: Is there an efficient algorithm to determine if a hyperbolic Coxeter group has finite covolume?

**Current Method**: Enumerate all maximal parabolics and check if all are affine.

**Research Questions**:
- Can we avoid full enumeration?
- Are there local criteria that imply global properties?
- What about approximate/probabilistic algorithms?

## Future Research Directions

### Short-Term (1-2 years)
1. **Complete systematic enumeration** for ranks up to 10
2. **Optimize algorithms** for large-scale computation
3. **Develop visualization tools** for geometric understanding
4. **Implement Galois-equivariant methods** for non-crystallographic types

### Medium-Term (2-5 years)
1. **Extend to higher dimensions** with asymptotic analysis
2. **Develop homotopy-theoretic framework** for bilinear modules
3. **Study arithmetic properties** of finite covolume groups
4. **Create certified computation methods** with rigorous error bounds

### Long-Term (5+ years)
1. **Connect to motivic homotopy theory** and arithmetic geometry
2. **Develop quantum algorithms** for classification problems
3. **Study modular forms** associated to indefinite lattices
4. **Create comprehensive database** of all known results

## Collaboration Opportunities

### Mathematical Areas
- **Geometric group theory**: Connections to CAT(0) spaces and buildings
- **Number theory**: Arithmetic aspects of hyperbolic manifolds
- **Algebraic topology**: Homotopy theory and K-theory connections
- **Computational algebra**: Algorithm development and optimization

### Computational Projects
- **SageMath development**: Contribute to lattice and root system modules
- **Database projects**: Mathematical databases for classification results
- **Visualization software**: 3D geometry and interactive mathematics
- **High-performance computing**: Parallel algorithms and GPU acceleration

## Research Methodology Notes

### Validation Strategies
1. **Multiple independent implementations** of key algorithms
2. **Cross-verification** using different mathematical approaches
3. **Comparison with literature** for known cases
4. **Numerical verification** using interval arithmetic

### Documentation Standards
1. **Mathematical exposition** with full theoretical context
2. **Algorithmic descriptions** with complexity analysis
3. **Implementation details** with reproducible examples
4. **Experimental results** with statistical analysis

### Open Science Principles
1. **Open source software** development
2. **Reproducible research** practices
3. **Data sharing** for large-scale enumerations
4. **Collaborative development** using version control

---

**Research Philosophy**: These notes reflect an active, evolving research program that balances theoretical depth with computational practicality. The emphasis on exact methods, mathematical rigor, and open science principles ensures that our work contributes meaningfully to the mathematical literature while providing reliable tools for the research community.

**Next Steps**: Regular updates to these notes as research progresses, with particular attention to experimental results, new theoretical insights, and computational optimizations.