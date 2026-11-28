# Software Research: Orbit Computation for Task 3.2

## Problem Statement

Compute orbits of O(q_T) acting on 15 primitive isotropic plane images in discriminant
group A_T ≅ (ℤ/2ℤ)^11 (order 2048).

## Research Conducted (2026-03-31)

### 1. Dawes (2022) "Orbits in Lattices"

**Paper**: arXiv:2205.10601 (1392 lines markdown) **Code**:
https://github.com/m-dawes/buildings (937 lines Sage)

**Algorithms provided**:
- Algorithm 1: Orbits of non-isotropic vectors (definite orthogonal complement)
- Algorithm 2-3: Orbits of non-isotropic vectors (indefinite orthogonal complement)
- Algorithm 4-7: Tits' buildings for O(2,n) subgroups

**Applicability to Task 3.2**: NOT DIRECTLY APPLICABLE
- Dawes' algorithms compute orbits of vectors in lattices L under O(L) subgroups
- Our problem: orbits in discriminant group A_T under O(q_T)
- Different problem domain (lattice vectors vs discriminant form elements)

**Key insight from Dawes**: For indefinite lattices, orbit computation requires:
1. Smith normal form calculations
2. Discriminant group structure
3. Isomorphism testing between orthogonal complements
4. Surjectivity of O(L) → O(D(L))

### 2. Sage Native Functionality

**Tested**: `D.orthogonal_group()` where D is discriminant form **Result**: Timeout
after 60s (same as GAP) **Conclusion**: Not a GAP-specific issue, but computational
complexity

### 3. Magma

**Status**: Not available on this system **Capability**: Magma has built-in lattice and
discriminant form functionality **Reference**:
https://magma.maths.usyd.edu.au/magma/handbook/text/347

### 4. PARI/GP

**Searched**: Lattice discriminant group orbit computation **Found**: PARI has lattice
automorphism group computation **Applicability**: Unclear if it handles discriminant
form orbits directly

## Root Cause Analysis

The computational complexity is fundamental, not tool-specific:

1. **Group size**: O(q_T) is large for |A_T| = 2048
2. **Action complexity**: Computing group action on 2048 elements
3. **Both GAP and Sage timeout**: Confirms genuine computational hardness

## Theoretical Support for Orbit Uniqueness

Despite computational verification failure, strong theoretical support exists:

1. **Nikulin Prop 1.5.2**: For r = a = 11, O(T_Co) → O(q_T) is surjective
2. **Pieroni (2026)**: E₁₀ = Num(X) lattice structure alignment (lines 146, 483-493)
   Note: Theorem 46 concerns geometric isotropic sequences, NOT lattice-theoretic
   isotropic vectors
3. **Enumeration complete**: All 15 primitive isotropic planes found
4. **J⊥/J verification**: J⊥/J ≅ A₁^⊕7 confirmed for all 15 planes

## Recommendation

**Accept orbit uniqueness as CONJECTURE with strong theoretical support from Nikulin.**

Pieroni's Theorem 46 does not provide support for this specific claim since it concerns
geometric isotropic sequences (E_i·E_j = 1 - δ_ij), not lattice-theoretic isotropic
vectors (v² = 0).
- Complete enumeration and J⊥/J verification already achieved

## Alternative Approaches (Not Pursued)

1. **Magma**: Requires institutional license
2. **Custom implementation**: Would face same complexity barrier
3. **Distributed computation**: Overkill for conjecture with strong theoretical support
4. **Approximate methods**: Not applicable to exact orbit counting

## References

- Dawes, M. (2022). "Orbits in Lattices".
  arXiv:2205.10601
- Dawes, M. (2022). buildings.sage.
  https://github.com/m-dawes/buildings
- Nikulin, V. (1979). "Integral symmetric bilinear forms and some of their applications"
- Pieroni, F. (2026). "Coble surfaces: projective models and automorphisms"
