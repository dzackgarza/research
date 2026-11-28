# Lattice Construction Standards

## Critical Issue

Agents have been constructing lattices inconsistently, leading to disagreements over
Gram matrices and verification failures.
This document specifies what MUST be centralized in shared code.

## Required Canonical Constructors

All lattices must be constructed via direct sums of these canonical pieces:

### Standard Building Blocks

1. **Rank-1 lattices**: ⟨n⟩ for any n ∈ ℤ
   - Gram matrix: [n]

2. **Hyperbolic plane**: U
   - Gram matrix: [[0,1],[1,0]]

3. **E8 root lattice**: E8 or E8(-1)
   - Gram matrix: Cartan matrix (optionally negated)

### Project Lattices (Direct Sum Form)

**CRITICAL**: These must be constructed via direct sums, NOT ad-hoc diagonal matrices.

1. **K3 lattice**: Λ_K3 = U³ ⊕ E8(-1)²
   - Signature: (3, 19)
   - Determinant: -1 (unimodular)

2. **Coble Picard lattice**: S_Co = ⟨2⟩ ⊕ ⟨-2⟩¹⁰
   - Signature: (1, 10)
   - Determinant: 2¹¹ = 2048

3. **Coble transcendental lattice**: T_Co = ⟨2⟩ ⊕ U ⊕ E8(-1)
   - Signature: (2, 9)
   - Determinant: -2¹¹ = -2048

4. **Enriques transcendental lattice**: T_En = ⟨2⟩² ⊕ ⟨-2⟩⁸
   - Signature: (2, 8)
   - Determinant: -2¹⁰ = -1024

## Required Standard Operations

All agents MUST use these standard methods (no custom implementations):

### Basic Invariants

- `L.signature()` → (p, n) where p = # positive, n = # negative
- `L.rank()` → rank
- `L.determinant()` → determinant
- `L.gram_matrix()` → Gram matrix (basis-dependent!)

### Discriminant Group

- `L.discriminant_group()` → A_L = L*/L
- `A_L.cardinality()` → |A_L|
- `A_L.invariants()` → elementary divisors
- Check 2-elementary: all invariants equal 2

### Discriminant Form

- `A_L.quadratic_form(v)` → q_L(v) ∈ ℚ/2ℤ
- Check isotropic: q_L(v) = 0

### Nikulin Invariants

For 2-elementary lattices: (r, a, δ) where
- r = rank
- a = rank of discriminant group
- δ = (r - a) mod 2 (coparity)

### Primitive Embeddings

- Check if sublattice M is primitive in L (L/M torsion-free)
- Use Smith normal form: primitive iff all diagonal entries ±1

### Orthogonal Complements

- Compute M^⊥ in L
- Solve orthogonality conditions

## Critical Rules

### Lattice Equality

**NEVER compare Gram matrices directly**. Lattices are equal up to isometry, not matrix
equality.

To check isometry:
- Compare signature
- Compare determinant
- Compare discriminant group invariants
- For 2-elementary lattices: compare discriminant forms

**WARNING**: Signature + determinant + discriminant form does NOT always determine
isometry class for indefinite lattices.
Nikulin's classification is more subtle.

### Assertion-First Coding

Every print must be preceded by assertion:
```python
# BAD
print(f"Signature: {L.signature()}")

# GOOD
sig = L.signature()
assert sig == (2, 9), f"Expected (2,9), got {sig}"
print(f"Signature: {sig}")
```

## Implementation Requirements

1. All canonical constructors must be in `coble_geometry.sage`
2. All scripts must use these constructors (no ad-hoc constructions)
3. Gram matrices may differ (basis change) but invariants must match
4. Any custom construction requires explicit justification

## Delegation

Subagents should implement these specifications in `coble_geometry.sage` and update all
scripts to use them.
