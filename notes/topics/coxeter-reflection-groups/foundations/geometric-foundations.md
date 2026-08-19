<!--
Origin: gitclones/Coxeter/research/foundations/geometric-foundations.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is RESEARCH PROSE from the Coxeter working trees: a mathematical
account written for this project. Errors the audit found in it are listed in
the README.md of this directory.
-->

# Geometric Foundations: Hyperbolic Geometry and Coxeter Groups

This document establishes the geometric foundations underlying Coxeter systems, focusing on the hyperbolic geometry that governs infinite Coxeter groups and their fundamental domains.

## Geometric Context

### From Algebra to Geometry

The classification of Coxeter systems as elliptic, parabolic, or hyperbolic has deep geometric significance:

- **Elliptic (Finite)**: Group acts on spherical geometry
- **Parabolic (Affine)**: Group acts on Euclidean geometry  
- **Hyperbolic**: Group acts on hyperbolic geometry

This connection transforms algebraic questions about quadratic forms into geometric questions about group actions on curved spaces.

## Hyperbolic Space and Coxeter Groups

### Mathematical Setup

**Hyperbolic Space**: For signature (1, n-1, 0), we work in hyperbolic space ℍⁿ⁻¹, realized as:
- **Hyperboloid Model**: {x ∈ ℝⁿ : ⟨x,x⟩ = -1, x₀ > 0}
- **Ball Model**: Unit ball in ℝⁿ⁻¹ with hyperbolic metric
- **Half-Space Model**: Upper half-space {(x₁,...,xₙ₋₁,xₙ) : xₙ > 0}

**Isometry Group**: O(1, n-1) acts as isometries of hyperbolic space.

### Reflection Geometry

**Hyperbolic Reflections**: For a simple root α with ⟨α,α⟩ = -2, the reflection s_α acts as:
```
s_α(x) = x - 2⟨x,α⟩/⟨α,α⟩ · α = x + ⟨x,α⟩ · α
```

**Reflection Hyperplanes**: Each reflection is across a hyperplane:
```
H_α = {x ∈ ℍⁿ⁻¹ : ⟨x,α⟩ = 0}
```

**Fundamental Domain**: The intersection of half-spaces:
```
D = {x ∈ ℍⁿ⁻¹ : ⟨x,αᵢ⟩ ≥ 0 for all simple roots αᵢ}
```

### Geometric Invariants

#### Volume and Covolume

**Volume Formula**: For hyperbolic Coxeter groups, Vinberg's formula relates:
- Volume of fundamental domain
- Gram determinant  
- Field discriminant (for non-crystallographic types)

**Covolume**: The volume of the quotient orbifold ℍⁿ⁻¹/Γ where Γ is the Coxeter group.

#### Cusp Structure

**Parabolic Elements**: Elements of infinite order fixing a point at infinity.

**Cusp Correspondence**: Each maximal parabolic subdiagram corresponds to:
- A conjugacy class of maximal parabolic subgroups
- A cusp in the quotient orbifold ℍⁿ⁻¹/Γ
- A limit point of the group action on the boundary sphere

## Vinberg's Theory

### Volume Finiteness

**Main Theorem**: A hyperbolic Coxeter group has finite covolume if and only if all maximal parabolic subdiagrams are affine type.

**Geometric Interpretation**:
- **Affine maximal parabolics**: Create cusps of finite volume
- **Hyperbolic maximal parabolics**: Create cusps of infinite volume
- **Finite covolume**: Sum of cusp volumes is finite

### Geometric Classification

#### Compact Groups (Lannér Condition)
- **Condition**: No parabolic subdiagrams exist
- **Geometry**: Fundamental domain is compact
- **Examples**: Finite list of 9 groups in dimension 3, 5 in dimension 4

#### Non-Compact Finite Volume
- **Condition**: All maximal parabolic subdiagrams are affine
- **Geometry**: Fundamental domain has finite volume with cusps
- **Examples**: Include many arithmetic hyperbolic manifolds

#### Infinite Volume
- **Condition**: At least one maximal parabolic subdiagram is hyperbolic
- **Geometry**: Fundamental domain has infinite volume
- **Examples**: Most hyperbolic Coxeter groups

### Arithmetic vs Non-Arithmetic Groups

**Arithmetic Groups**: Defined by rational structures, often have finite covolume.

**Non-Arithmetic Groups**: More general, can have infinite covolume.

**Research Question**: Characterize which finite covolume hyperbolic Coxeter groups are arithmetic.

## Geometric Algorithms

### Fundamental Domain Construction

**Goal**: Compute explicit description of fundamental domain D.

**Method**:
1. Start with half-space for each simple root
2. Intersect to get convex polytope
3. Check if polytope has finite volume

**Challenges**:
- Infinite-sided polytopes
- Numerical precision for hyperbolic geometry
- Coordinate system choice

### Distance and Angle Computations

**Hyperbolic Distance**: Between points x, y in ℍⁿ⁻¹:
```
d(x,y) = arccosh(-⟨x,y⟩)
```

**Dihedral Angles**: Between reflection hyperplanes:
```
angle(H_α, H_β) = arccos(⟨α,β⟩/√(⟨α,α⟩⟨β,β⟩))
```

**Implementation**: Use exact arithmetic in appropriate field extensions.

### Orbit and Stabilizer Computations

**Orbit Enumeration**: Generate group orbit of a point:
- Start with fundamental domain point
- Apply generators systematically
- Use geometric constraints to terminate

**Stabilizer Structure**: For maximal parabolic subgroups:
- Identify parabolic elements (infinite order)
- Compute action on boundary sphere
- Relate to cusp structure

## Crystallographic vs Non-Crystallographic Geometry

### Crystallographic Cases

**Integral Structures**: Simple roots span integral lattices.

**Reflection Hyperplanes**: Have rational normal vectors.

**Fundamental Domains**: Often have rational vertex coordinates.

**Arithmetic Properties**: Natural connection to algebraic number theory.

### Non-Crystallographic Cases

**Field Extensions**: Require ℚ(φ), ℚ(2cos(π/5)), etc.

**Galois Actions**: Fundamental domains come in Galois conjugate families.

**Example H₃**: Icosahedral symmetry requires golden ratio:
- Dihedral angles involve π/5
- Vertices at fifth roots of unity
- Volume involves φ-dependence

**Geometric Complexity**: 
- More complex algebraic coordinates
- Galois conjugate fundamental domains
- Field discriminant in volume formulas

## Connections to Other Geometries

### Spherical and Euclidean Cases

**Elliptic (Spherical)**:
- Finite reflection groups
- Fundamental domain is spherical simplex
- All angles acute (< π/2)

**Parabolic (Euclidean)**:
- Affine Weyl groups
- Fundamental domain is Euclidean simplex
- Some angles equal π/2

**Hyperbolic**:
- Infinite reflection groups  
- Fundamental domain is hyperbolic simplex
- Some angles obtuse (> π/2)

### Moduli Spaces

**Deformation Theory**: Hyperbolic Coxeter groups form families parameterized by:
- Coxeter matrix entries
- Subject to hyperbolicity constraints
- Natural compactification at boundary

**Example**: For triangle groups (3 reflections):
- Parameterized by three angles (α, β, γ)
- Constraint: α + β + γ < π (hyperbolic)
- Moduli space is open triangle

## Computational Geometric Methods

### Exact Hyperbolic Arithmetic

**Challenge**: Hyperbolic computations involve transcendental functions.

**Solution Approaches**:
1. **Algebraic coordinates**: Work in appropriate field extensions
2. **Symbolic computation**: Use exact symbolic expressions
3. **Interval arithmetic**: For verified numerical results

### Visualization and Graphics

**Hyperbolic Models**: Different models for different purposes:
- **Hyperboloid**: Natural for inner product computations
- **Poincaré disk**: Good for visualization
- **Half-space**: Convenient for certain algorithms

**Fundamental Domain Plots**:
- Project to 2D or 3D for visualization
- Show reflection hyperplanes and their intersections
- Highlight parabolic cusps and their geometry

### Precision and Accuracy

**Exact Methods**: Maintain mathematical exactness throughout.

**Validation**: Cross-check geometric results with:
- Known volume formulas
- Symmetry properties
- Literature values for standard examples

## Advanced Geometric Topics

### Geometric Structures on Quotients

**Orbifolds**: Quotient spaces ℍⁿ⁻¹/Γ with singularities.

**Cone Points**: Correspond to finite order elements.

**Cusp Neighborhoods**: Parameterized by maximal parabolic subgroups.

### Geometric Group Theory

**Word Metrics**: Distance in Cayley graph vs geometric distance.

**Growth Functions**: Relate algebraic and geometric properties.

**Boundary Theory**: Action on sphere at infinity encodes group structure.

### Rigidity Phenomena

**Mostow Rigidity**: Hyperbolic manifolds of dimension ≥ 3 are determined by fundamental group.

**Coxeter Case**: Rigidity properties for Coxeter groups and their quotients.

**Deformation Spaces**: When can Coxeter groups be continuously deformed?

---

**Research Perspective**: The geometric foundations provide essential intuition for understanding Coxeter systems beyond pure algebra. The interplay between quadratic form properties and hyperbolic geometry reveals deep mathematical structures that guide both theoretical understanding and computational implementation.

**Implementation Impact**: Geometric considerations inform:
- Choice of coordinate systems and representations
- Numerical precision requirements
- Validation methods using geometric invariants
- Connections to broader mathematical literature