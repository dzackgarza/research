<!--
Origin: gitclones/Coxeter/research/explorations/open-questions.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is RESEARCH PROSE from the Coxeter working trees: a mathematical
account written for this project. Errors the audit found in it are listed in
the README.md of this directory.
-->

# Open Questions: Unsolved Problems and Research Directions

This document catalogs open questions, conjectures, and unsolved problems related to Coxeter groups, maximal parabolic subdiagrams, and the broader mathematical framework of this project.

## Computational Complexity Questions

### Question 1: Fundamental Complexity of Maximal Parabolic Enumeration

**Problem Statement**: What is the computational complexity of determining the number of maximal parabolic subdiagrams of a given Coxeter diagram?

**Current Status**:
- **Upper Bound**: O(2^n) by naive enumeration
- **Practical Performance**: Significantly better with eigenvalue monotonicity pruning
- **Lower Bound**: Unknown

**Specific Open Questions**:
1. Is the problem NP-hard?
2. Is there a polynomial-time approximation scheme?
3. Can quantum algorithms provide exponential speedup?
4. What is the average-case complexity for random Coxeter diagrams?

**Research Approach**:
```
Conjecture: Maximal parabolic enumeration is #P-complete.
Approach: Reduction from other counting problems.
Alternative: Show polynomial-time algorithm for special cases.
```

### Question 2: Optimal Pruning Strategies

**Problem Statement**: What is the optimal pruning strategy for exhaustive enumeration of subdiagrams?

**Current Methods**:
- Eigenvalue monotonicity (eigenvalue interlacing)
- Signature inheritance constraints
- Graph connectivity requirements

**Open Questions**:
1. Can machine learning improve pruning efficiency?
2. Are there combinatorial constraints that provide stronger pruning?
3. What is the theoretical limit of pruning effectiveness?

**Research Directions**:
- **Spectral graph theory**: Use graph eigenvalues for pruning
- **Semidefinite programming**: Formulate as optimization problem
- **Probabilistic methods**: Use random sampling for large instances

## Mathematical Theory Questions

### Question 3: Galois Actions on Classification Results

**Problem Statement**: How do Galois automorphisms act on the set of maximal parabolic subdiagrams for non-crystallographic types?

**Context**: Non-crystallographic types (H₃, H₄, I₂(p) with p ∉ {2,3,4,6}) require field extensions.

**Specific Questions**:
1. Is the number of maximal parabolic subdiagrams Galois-invariant?
2. How does the Galois group permute individual maximal parabolic subdiagrams?
3. Can Galois symmetry reduce computational complexity?

**Research Program**:
```python
def galois_action_conjecture(diagram, field_extension):
    """
    Conjecture: Number of maximal parabolics is Galois-invariant.
    
    Test: For each σ in Galois group, apply σ to Gram matrix
          and verify same maximal parabolic count.
    """
    base_count = len(enumerate_maximal_parabolics(diagram))
    
    for sigma in field_extension.galois_group():
        transformed_diagram = apply_galois_automorphism(diagram, sigma)
        transformed_count = len(enumerate_maximal_parabolics(transformed_diagram))
        assert base_count == transformed_count  # Conjecture
```

### Question 4: Higher-Dimensional Asymptotics

**Problem Statement**: How do maximal parabolic counts grow as the rank (dimension) increases?

**Current Knowledge**:
- Exponential growth in worst case
- Significant variation between diagram types
- Limited data for high dimensions

**Specific Questions**:
1. What is the asymptotic growth rate for specific infinite families?
2. Are there universal bounds independent of specific diagram structure?
3. How does the finite covolume condition affect growth rates?

**Research Approach**:
- **Systematic enumeration**: Generate data for ranks 10-20
- **Asymptotic analysis**: Study growth patterns
- **Probabilistic models**: Random Coxeter diagrams

### Question 5: Arithmetic vs Non-Arithmetic Groups

**Problem Statement**: Which finite covolume hyperbolic Coxeter groups are arithmetic?

**Background**: Arithmetic groups have special number-theoretic properties and are often easier to study.

**Current Status**:
- Many examples known to be arithmetic
- Some known to be non-arithmetic
- No general classification criterion

**Research Questions**:
1. Is there an effective algorithm to determine if a given finite covolume hyperbolic Coxeter group is arithmetic?
2. What proportion of finite covolume groups are arithmetic?
3. How do arithmetic properties relate to maximal parabolic structure?

### Question 6: Volume Formulas and Exact Computation

**Problem Statement**: Can we compute exact volumes of hyperbolic Coxeter fundamental domains?

**Challenges**:
- Volumes involve transcendental functions
- Field extensions complicate exact computation
- High-dimensional cases are particularly difficult

**Specific Questions**:
1. Are there closed-form volume formulas for specific families?
2. Can volumes be expressed in terms of special functions (polylogarithms, etc.)?
3. What is the relationship between volume and maximal parabolic structure?

## Algorithmic and Implementation Questions

### Question 7: Exact Arithmetic Optimization

**Problem Statement**: What are the most efficient algorithms for exact arithmetic over number fields required for non-crystallographic types?

**Current Bottlenecks**:
- Cyclotomic field arithmetic
- Minimal polynomial computations
- Memory usage for large algebraic numbers

**Research Directions**:
1. **Optimized representations**: More efficient storage of algebraic numbers
2. **Specialized algorithms**: Faster arithmetic in specific cyclotomic fields
3. **Hybrid methods**: Combine exact and numerical computation with rigorous error bounds

### Question 8: Parallel Algorithm Design

**Problem Statement**: How can maximal parabolic enumeration be efficiently parallelized?

**Challenges**:
- Irregular tree structure from pruning
- Load balancing with data dependencies
- Communication overhead

**Open Questions**:
1. What is the optimal parallelization strategy for shared-memory systems?
2. Can distributed computing approaches handle very large instances?
3. How do GPU architectures apply to this problem?

### Question 9: Numerical Verification and Certification

**Problem Statement**: How can we develop certified algorithms that provide rigorous guarantees about correctness?

**Approach**: Use interval arithmetic and computer-assisted proofs.

**Specific Questions**:
1. Can we certify eigenvalue computations over number fields?
2. What precision is required for reliable numerical verification?
3. How do we handle the interaction between symbolic and numerical computation?

## Connections to Other Mathematical Areas

### Question 10: Homotopy Theory and Bilinear Modules

**Problem Statement**: Can we develop a stable homotopy theory for bilinear modules that provides new computational tools?

**Research Program**:
1. Define suspension functor on bilinear modules
2. Construct stable ∞-category of bilinear module spectra
3. Relate to classical homological algebra
4. Develop computational applications

**Open Questions**:
1. What are the homotopy groups of bilinear module spectra?
2. How do spectral sequences arise naturally in this context?
3. Are there connections to algebraic K-theory and L-theory?

### Question 11: Modular Forms and Theta Series

**Problem Statement**: What modular properties do theta series of indefinite lattices possess?

**Challenges**:
- Indefinite theta series typically diverge
- Regularization methods needed
- Connection to Eisenstein series unclear

**Research Questions**:
1. Can we define convergent regularized theta series?
2. What modular transformation properties do they satisfy?
3. How do they relate to classical theory for positive definite lattices?

### Question 12: Motivic Homotopy Theory Connections

**Problem Statement**: Are there connections between Coxeter group theory and motivic homotopy theory?

**Speculative Research**:
- Motivic aspects of quadratic forms
- Arithmetic properties of hyperbolic manifolds
- A¹-homotopy theory over various fields

**Open Questions**:
1. Do Coxeter groups provide interesting examples in motivic homotopy theory?
2. How do field extensions interact with motivic structures?
3. Are there motivic interpretations of classification results?

## Experimental and Empirical Questions

### Question 13: Statistical Properties of Random Coxeter Diagrams

**Problem Statement**: What are the statistical properties of maximal parabolic counts for random Coxeter diagrams?

**Research Approach**:
- Generate large samples of random diagrams
- Study distribution of maximal parabolic counts
- Look for universal statistical patterns

**Questions**:
1. What is the typical number of maximal parabolic subdiagrams?
2. Are there phase transitions as parameters vary?
3. How do different randomness models affect results?

### Question 14: Exceptional Cases and Sporadic Examples

**Problem Statement**: Are there exceptional Coxeter diagrams with unusual maximal parabolic structure?

**Approach**: Systematic search for outliers in enumeration data.

**Questions**:
1. Which diagrams have unexpectedly many or few maximal parabolics?
2. Are there structural explanations for exceptional behavior?
3. Do sporadic examples suggest general patterns?

### Question 15: Computational Limits and Feasibility

**Problem Statement**: What are the practical limits of current computational approaches?

**Current Status**:
- Systematic enumeration feasible up to rank ~10
- Individual cases computed up to rank ~15
- Memory and time constraints limit larger cases

**Questions**:
1. Can algorithmic improvements extend feasible range?
2. What problems become tractable with next-generation computing?
3. Are there fundamental barriers to large-scale computation?

## Meta-Mathematical Questions

### Question 16: Formalization and Computer-Assisted Proof

**Problem Statement**: Can major theorems in Coxeter group theory be fully formalized in proof assistants?

**Examples**:
- Vinberg's volume finiteness criterion
- Classification of finite and affine types
- Eigenvalue monotonicity theorems

**Benefits**:
- Increased confidence in results
- Machine-checkable proofs
- Computer-assisted discovery

### Question 17: Mathematical Software Integration

**Problem Statement**: How can specialized Coxeter group computations be integrated into general mathematical software ecosystems?

**Challenges**:
- Interface design for non-expert users
- Integration with existing computer algebra systems
- Balancing generality with performance

**Research Directions**:
- SageMath module development
- GAP package creation
- Web-based computational interfaces

## Research Methodology Questions

### Question 18: Reproducibility and Open Science

**Problem Statement**: How can large-scale computational mathematics research be made fully reproducible?

**Challenges**:
- Long computation times
- Large datasets
- Software dependency management
- Version control for mathematical results

**Best Practices**:
- Containerized computational environments
- Persistent computational infrastructure
- Open data repositories
- Detailed computational documentation

### Question 19: Collaboration Models for Computational Mathematics

**Problem Statement**: What are effective collaboration models for projects combining theoretical mathematics with intensive computation?

**Considerations**:
- Division of theoretical vs computational work
- Code review processes for mathematical software
- Validation of computational results
- Credit attribution for algorithmic vs theoretical contributions

---

**Research Strategy**: These open questions provide a roadmap for future research, balancing fundamental theoretical questions with practical computational challenges. The interdisciplinary nature of the problems reflects the rich connections between Coxeter group theory and other areas of mathematics.

**Priority Assessment**: Questions are organized roughly by immediacy and computational tractability, with near-term algorithmic improvements balanced against longer-term theoretical developments.

**Collaboration Potential**: Many of these questions would benefit from interdisciplinary collaboration, combining expertise in geometric group theory, computational algebra, number theory, and high-performance computing.