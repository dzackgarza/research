# Task 1.1: Explicit Rational Sextic Construction

## Theorem Statement

For each of three explicit parametrizations P¹ → P² given by degree-6 polynomials with
rational coefficients, the image curve C ⊂ P² satisfies:

1. C is defined by an irreducible degree-6 equation F(x,y,z) = 0 over ℚ
2. C has exactly 10 singular points, all ordinary nodes (A₁ singularities)
3. The parametrization is generically injective (birational onto its image)
4. Therefore C is a rational plane sextic with 10 nodes

## Computational Verification

**Method**: Parametric elimination via resultants, followed by singularity
classification and generic fiber analysis.

**Implementation**: `computations/task1_1_sextic.sage`, `task1_1_sextic_example2.sage`,
`task1_1_sextic_example3.sage`

**Verification steps**:

1. **Parametrization**: Define three degree-6 polynomials f₀(s:t), f₁(s:t), f₂(s:t) in
   ℚ[s,t] with generic coefficients
2. **Implicit equation**: Compute resultant of x·f₁ - y·f₀ and x·f₂ - z·f₀ with respect
   to s, extract degree-6 factor F(x,y,z)
3. **Irreducibility**: Verify F is irreducible over ℚ and squarefree
4. **Singular locus**: Solve F = ∂F/∂x = ∂F/∂y = ∂F/∂z = 0 in projective coordinates,
   find exactly 10 points
5. **Node verification**: For each singular point, compute Hessian matrix and verify
   rank 2 (non-degenerate quadratic part)
6. **Generic injectivity**: For generic parameter a ∈ ℚ(a), compute gcd of fiber
   equations in ℚ(a)[u], verify gcd = u - a (fiber degree 1)

**Results**: All three examples produce irreducible rational sextics with exactly 10
nodes. Node coordinates are stored as exact algebraic numbers via
`QQbar.polynomial_root(AA.common_polynomial(minpoly), isolating_interval(...))`.

## Mathematical Context

**Arithmetic genus formula**: For a plane curve of degree d, the arithmetic genus is g_a
= (d-1)(d-2)/2. For d=6, this gives g_a = 10.

**Genus-delta relation**: The geometric genus g of a curve with singularities satisfies
g = g_a - Σ δ_p, where δ_p is the delta-invariant of each singular point.
For an ordinary node (A₁ singularity), δ = 1.

**Rationality**: Ten nodes with δ=1 each give g = 10 - 10 = 0, hence C is rational.
The generic fiber degree 1 condition ensures the parametrization P¹ → C is birational.

**Literature**: The classical Coble surface construction (Coble 1917, 1929) begins with
such a rational 10-nodal sextic.
The blowup of P² at the 10 nodes produces a K3 surface with specific lattice structure.

**Theoretical context** (Pieroni 2026, lines 752-759): For a generic 10-point
configuration in P², no nodal sextic exists because 10 nodes impose 30 independent
linear conditions on the 28-dimensional space H⁰(O_P²(6)). The repo's three examples
represent special configurations where these conditions become dependent, making them
computationally rare instances of the theoretical framework Pieroni describes.

See `REFERENCES.md` for Coble (1917, 1929), Dolgachev-Kondō (2013), Pieroni (2026), and
related sources.

## Scope

This verification establishes that the repo contains explicit worked examples of
rational 10-nodal sextics with exact algebraic coordinates.
It does not prove existence in principle (already known from classical literature) or
classify all such sextics.
The role is to provide concrete computational instances matching the standard Coble
surface setup.

**Cross-references**:
- `notes/task1_1_birationality_note.md` — canonical scope note for what Task 1.1
  establishes
- `notes/task1_1_exact_coordinate_note.md` — exact algebraic coordinate rendering path
- `REFERENCES.md` — Coble (1917, 1929), Dolgachev-Kondō (2013)
