# Mapping of Abstract Methods to External Tools

This file maps abstract methods defined in `src/coble_geometry_varieties.py` to external
tool functionalities documented in `theory/backends/comprehensive-tool-docs`.

## Variety Methods

| Abstract Method | External Tool(s) | Implementation Strategy |
| --- | --- | --- |
| `Variety.blowup(center)` | Macaulay2: Schubert2 `blowup(i)` | Use Macaulay2's Schubert2 package |
| `Variety.resolve_singularities()` | Singular: `resbin.lib` (minimal resolution) | Use Singular's resolution algorithms |
| `Variety.picard_group()` | Sage: `PicardGroup`, Oscar.jl: integer lattices | Use Sage or Oscar to compute Pic |
| `Variety.kodaira_dimension()` | Macaulay2 + Sage: compute h^0(nK_X), then Sage `R.lagrange_polynomial(points)` | **Verified**: For proper X of dimension d, by Asymptotic Riemann-Roch (Stacks Tag 0BJ8), if κ ≥ 0 then h^0(nK_X) = P(n) for a polynomial of degree κ. Compute h^0(nK_X) for n = 1,...,d+2 via Macaulay2. In Sage: `R = PolynomialRing(QQ, 'x'); points = [(n, h0(n)) for n in 1..d+2]; P = R.lagrange_polynomial(points); κ = P.degree()`. If all h^0 = 0, then κ = -∞. Reference: https://stacks.math.columbia.edu/tag/0BJ8 |
| `Variety.hilbert_polynomial()` | Macaulay2: `hilbertPolynomial` | Use Macaulay2's Hilbert series (verified in docs) |
| `Variety.hodge_number(p,q)` | Macaulay2: `HH^i(cotangentSheaf(p, X))` | Use Macaulay2's sheaf cohomology (verified in docs) |
| `Variety.holomorphic_euler_characteristic()` | Macaulay2: via sheaf cohomology | Formula (definition): χ(O_X) = Σ(-1)^i h^i(O_X). For surfaces: χ = 1 - q + p_g. Compute each h^i(O_X) via Macaulay2's `dim HH^i(O_X)`. Reference: Standard definition (no additional theorem needed). |
| `Variety.canonical_class()` | Macaulay2: `canonicalDivisor(X)` | Verified: https://macaulay2.com/doc/Macaulay2-1.22/share/doc/Macaulay2/Divisor/html/_canonical__Divisor.html |

## Curve Methods

| Abstract Method | External Tool(s) | Implementation Strategy |
| --- | --- | --- |
| `Curve.genus()` | Singular: `brnoeth.lib: Adj_div`, Macaulay2: `geometricGenus` | Use Singular's `Adj_div` or Macaulay2 |
| `Curve.arithmetic_genus()` | Singular: `brnoeth.lib: Adj_div` | Use Singular |
| `Curve.normalization()` | Sage: `normalize()`, Singular: `normalize` | Use Sage or Singular |

## Plane Curve Methods

| Abstract Method | External Tool(s) | Implementation Strategy |
| --- | --- | --- |
| `PlaneCurve.equation()` | Sage: defining polynomial | Direct access |
| `PlaneCurve.dual_curve()` | Sage: `dual` | Use Sage |
| `RationalSextic.is_nodal()` | Singular: solve.lib (find singularities) | Solve partial derivatives and check nodes |
| `RationalSextic.nodes()` | Singular: solve.lib | Solve for singular points |
| `RationalSextic.normalization()` | Sage: `normalize()` | Use Sage |

## Surface Methods

| Abstract Method | External Tool(s) | Implementation Strategy |
| --- | --- | --- |
| `Surface.birational_involution()` | Sage: for Enriques surfaces | Use Sage's built-in |
| `Blowup.exceptional_divisor()` | Macaulay2: Schubert2 `exceptionalDivisor` | Use Macaulay2 |
| `CobleSurface.from_singular_sextic()` | Singular: find nodes, then Sage blowup | Use Singular to find nodes, Sage for blowup |
| `CobleSurface.coble_lattice()` | Oscar.jl: integer lattices | Use Oscar to build lattice |

## Divisor Methods

| Abstract Method | External Tool(s) | Implementation Strategy |
| --- | --- | --- |
| `Divisor.riemann_roch_space_dimension()` | Singular: `brnoeth.lib: BrillNoether`, Macaulay2 | Use Singular or Macaulay2 for RR spaces |
| `Divisor.is_ample()` | Macaulay2: `isVeryAmple` or test via Nakai-Moishezon | Use Macaulay2 |
| `Divisor.is_nef()` | Test via intersection with all curves | Use intersection theory |
| `Divisor.self_intersection()` | Macaulay2: intersection theory | Use Macaulay2 |
| `Divisor.intersection(other)` | Macaulay2: intersection theory | Use Macaulay2 |

## Picard/Lattice Methods

| Abstract Method | External Tool(s) | Implementation Strategy |
| --- | --- | --- |
| `PicardGroup.intersection_matrix()` | Oscar.jl: gram_matrix | Use Oscar |
| `PicardeLattice.underlying_picard_group()` | Direct mapping | Use Oscar |

## Branched Cover Methods

| Abstract Method | External Tool(s) | Implementation Strategy |
| --- | --- | --- |
| `DoubleCover.total_space()` | Sage: weighted projective space | Construct in Sage |
| `K3DoubleCover.cover_surface()` | Sage: K3 surface constructor | Use Sage |
| `EnriquesQuotient.k3_cover()` | Sage: Enriques surface K3 cover | Use Sage |

## Coherent Sheaf Methods

| Abstract Method | External Tool(s) | Implementation Strategy |
| --- | --- | --- |
| `CoherentSheaf.h0()` | Macaulay2: `dim HH^0(F)` | Use Macaulay2 |
| `CoherentSheaf.h1()` | Macaulay2: `dim HH^1(F)` | Use Macaulay2 |
| `CoherentSheaf.euler_characteristic()` | Macaulay2: `chi(F)` | Use Macaulay2 |
| `CoherentSheaf.rank()` | Macaulay2: `rank(F)` | Use Macaulay2 |

## Family Methods

| Abstract Method | External Tool(s) | Implementation Strategy |
| --- | --- | --- |
| `FamilyOfVarieties.specialization()` | Sage: degeneration | Use Sage's degeneration handling |
| `FamilyOfVarieties.monodromy()` | Sage: monodromy | Use Sage |

## Lattice-Theoretic Methods (from coble_geometry_foundation.py)

| Abstract Method | External Tool(s) | Implementation Strategy |
| --- | --- | --- |
| `Lattice.discriminant_group()` | Oscar.jl: `discriminant_group(L)` | Use Oscar |
| `Lattice.primitive_embedding()` | Oscar.jl: `primitive_embeddings(L, M)` | Use Oscar |
| `Lattice.automorphism_group()` | CARAT: `Aut_grp`, Indefinite.jl: `automorphism_group` | Use CARAT (definite) or Indefinite.jl (indefinite) |
| `Lattice.isometry_test()` | Indefinite.jl: `test_equivalence` | Use Indefinite.jl |
| `Lattice.orbit_representatives()` | Indefinite.jl: `get_orbit_representative` | Use Indefinite.jl |
| `Lattice.vinberg_sh姚()` | Vinberg algorithm (Oscar.jl or custom) | Use Oscar or custom implementation |

## Key Tool Selection

- **Oscar.jl**: Lattices, primitive embeddings, discriminant groups, genera, involutions
- **Singular**: Curve singularities, Brill-Noether, resolution, polynomial solving
- **Macaulay2**: Sheaf cohomology, blowups, intersection theory, Hilbert polynomials
- **GAP/GRAPE/Digraphs**: Automorphism groups (combinatorial)
- **CARAT**: Positive-definite lattice automorphism groups
- **Indefinite.jl**: Indefinite lattice automorphism groups and orbits
- **Sage**: General purpose, bridges to all above
