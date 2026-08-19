<!--
Origin: gitclones/Coxeter-v2/docs/authority/GEOMETRIC_THEORY.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is RESEARCH PROSE from the Coxeter working trees: a mathematical
account written for this project. Errors the audit found in it are listed in
the README.md of this directory.
-->

# Geometric Theory Authority Document

This document defines the geometric theories, conjectures, and exploratory directions for the Coxeter project. It consolidates literal extractions from research notes and exploratory archives.

## 1. Topological Methods

The project utilizes topological invariants associated with Coxeter diagrams to characterize their structure.

- **Simplicial & Cell Complexes**: Association of a simplicial complex (specifically the order complex of the parabolic subdiagram poset) to each Coxeter diagram.
- **Topological Invariants**: Investigation into the relationship between diagram connectivity and the homology of the associated complexes.
- **Cohomological Methods**: Application of group cohomology and building cohomology to study the subspace of the Tits cone where the group acts properly discontinuously.

## 2. Geometric Perspectives and Realizations

### Hyperbolic Geometry & Fundamental Domains
Classification of hyperbolic Coxeter groups is fundamentally linked to the properties of their fundamental domains in $\mathbb{H}^n$.
- **Finite Covolume Criterion**: A hyperbolic Coxeter group has finite covolume if and only if all its maximal parabolic subdiagrams are of affine (parabolic) type.
- **Volume Formulas**: Computation of exact volumes of fundamental domains using Schläfli's volume differential formula and specialized polylogarithmic values.

### The Tits Cone and Proper Actions
- **Fundamental Domain**: $C = \{ v \in V \mid \langle v, \alpha_i \rangle \leq 0 \text{ for all } i \}$.
- **Tits Cone**: $U = \bigcup_{w \in W} w(C)$.
- **Action boundaries**: The group $W$ acts properly discontinuously on the interior of $U$.

## 3. Advanced Conjectures & Open Questions

### Galois Theory of Classification
For non-crystallographic types requiring field extensions $\mathbb{Q}(\phi, \cos(2\pi/p))$, the interaction with Galois automorphisms is a primary research node.
- **Conjecture**: The number of maximal parabolic subdiagrams is Galois-invariant for all non-crystallographic Coxeter types.
- **Galois Action**: Systematic study of how $\sigma \in Gal(K/\mathbb{Q})$ permutes the set of maximal parabolic subdiagrams.

### Motivic Homotopy Theory Connections
- **Research Node**: Exploration of motivic aspects of quadratic forms and $A^1$-homotopy theory over various fields in the context of Coxeter groups.
- **Arithmetic Properties**: Connection between the discriminants of the Gram matrix over number fields and the arithmeticity of the resulting hyperbolic groups.

## 4. Experimental Investigations

### Regularized Theta Series
Investigation into the modular properties of theta series associated with indefinite hyperbolic lattices.
- **Regularization Method**: Implementation of regularization techniques (e.g., Borcherds products or Siegel-Weil variants) to handle the divergence of indefinite theta series.
- **Modular Forms**: Potential mapping of hyperbolic lattice invariants to specific spaces of modular forms.

### Higher-Dimensional Asymptotics
- **Node**: Investigation into the growth rate of maximal parabolic subdiagram counts as the rank $n \to \infty$.
- **Growth Pattern**: Comparison between worst-case exponential growth and typical growth for "random" Coxeter diagrams.
