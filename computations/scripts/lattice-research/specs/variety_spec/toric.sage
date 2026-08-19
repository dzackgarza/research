# ============================================================================
# FIXTURE: TORIC VARIETIES
#
# A toric variety is a normal variety containing a torus T ≅ (CC^*)^n as
# a dense open subset, with an algebraic T-action extending the self-action.
# Equivalently (for smooth projective): defined by a complete smooth fan.
#
#   X.is_toric()             -- True iff X admits a torus action with dense orbit
#   X.torus()                -- the dense torus T ≅ (CC^*)^n
#   X.fan()                  -- the fan Σ defining X (if toric)
#   X.moment_polytope()      -- the moment polytope (for projective toric)
#   X.torus_fixed_points()   -- 0-dimensional T-orbits (vertices of polytope)
#   X.torus_orbits()         -- all T-orbits stratified by cones of Σ
#
# Non-toric examples: smooth curves of genus >= 1, K3 surfaces (generic),
# Enriques surfaces, surfaces of general type.
# ============================================================================

P1 = PP^1(CC)
P2 = PP^2(CC)
P3 = PP^3(CC)


# ============================================================================
# Section 1: Projective spaces — toric via standard fan
# ============================================================================
# PP^n is toric with torus (CC^*)^n, fan = all cones over faces of the
# standard simplex.  Fixed points: the n+1 coordinate points.

for n in range(1, 5):
    Pn = PP^n(CC)
    assert Pn.is_toric()
    T_n = Pn.torus()
    assert T_n.dimension() == n

    fixed = Pn.torus_fixed_points()
    assert fixed.cardinality() == n + 1    # n+1 vertices of simplex

    # Fan has n+1 rays corresponding to coordinate hyperplanes
    Sigma = Pn.fan()
    assert Sigma.rays().cardinality() == n + 1
    assert Sigma.is_complete() and Sigma.is_smooth()

    # Moment polytope is the standard n-simplex
    Delta = Pn.moment_polytope()
    assert Delta.vertices().cardinality() == n + 1
    assert Delta.is_simplex()


# ============================================================================
# Section 2: Products of projective spaces
# ============================================================================
# PP^m × PP^n is toric with torus (CC^*)^{m+n}.

P1xP1 = PP^1(CC) * PP^1(CC)
P1xP2 = PP^1(CC) * PP^2(CC)

assert P1xP1.is_toric()
assert P1xP1.torus().dimension() == 2
assert P1xP1.torus_fixed_points().cardinality() == 4   # 2 × 2

assert P1xP2.is_toric()
assert P1xP2.torus().dimension() == 3
assert P1xP2.torus_fixed_points().cardinality() == 6   # 2 × 3

# Moment polytope of PP^1 × PP^1 is the unit square
Delta_sq = P1xP1.moment_polytope()
assert Delta_sq.vertices().cardinality() == 4
assert Delta_sq.is_isomorphic_to(Polytope.cube(1))   # [0,1]^2


# ============================================================================
# Section 3: Hirzebruch surfaces F_n = PP(O ⊕ O(n)) → PP^1
# ============================================================================
# F_n is toric for all n >= 0.  F_0 = PP^1 × PP^1, F_1 = Bl_1 PP^2.
# Fan: 4 rays, 4 maximal cones.  Fixed points: 4.

for n in range(0, 5):
    Fn = HirzebruchSurface(n)
    assert Fn.is_toric()
    assert Fn.torus().dimension() == 2
    assert Fn.torus_fixed_points().cardinality() == 4

    Sigma_n = Fn.fan()
    assert Sigma_n.rays().cardinality() == 4
    assert Sigma_n.is_complete() and Sigma_n.is_smooth()

    # F_0 ≅ PP^1 × PP^1
    if n == 0:
        assert Fn.is_isomorphic_to(P1xP1)
    # F_1 ≅ Bl_1 PP^2 (del Pezzo dP_8)
    if n == 1:
        assert Fn.is_isomorphic_to(P2.blowup(P2.point([0, 0, 1])).domain())


# ============================================================================
# Section 4: Blowups of toric surfaces remain toric (star subdivision)
# ============================================================================
# Blowing up a torus-fixed point of a toric variety is a star subdivision
# of the fan and yields another toric variety.

p0 = P2.torus_fixed_points().points()[0]
Bl_P2 = P2.blowup(p0).domain()
assert Bl_P2.is_toric()
assert Bl_P2.torus_fixed_points().cardinality() == 4  # was 3, gained one new

# Bl_n PP^2 for n = 1..4 (each blow-up of a torus-fixed point)
Sn = P2
for n in range(1, 5):
    p_fix = Sn.torus_fixed_points().points()[0]
    Sn    = Sn.blowup(p_fix).domain()
    assert Sn.is_toric()
    assert Sn.torus_fixed_points().cardinality() == n + 3


# ============================================================================
# Section 5: Weighted projective spaces
# ============================================================================
# WPP(w_0,...,w_n) = (AA^{n+1}\{0}) / CC^* with weights (w_0,...,w_n).
# Toric iff all quotient singularities are cyclic (always true by construction).

WP112 = WeightedProjectiveSpace([1, 1, 2])
WP124 = WeightedProjectiveSpace([1, 2, 4])

assert WP112.is_toric()
assert WP124.is_toric()
assert WP112.torus().dimension() == 2
assert WP112.torus_orbits().cardinality() == 4   # 3 vertices + open stratum

# WPP(1,1,2): singularity at [0:0:1] of type 1/2(1,1)
sing = WP112.singular_locus()
assert sing.cardinality() == 1
assert sing.points()[0].singularity_type() == SingularityType.cyclic_quotient(2, 1)


# ============================================================================
# Section 6: Non-toric varieties
# ============================================================================
# A smooth curve of genus >= 1 is NOT toric: a one-dimensional toric variety
# must be PP^1 or AA^1 (or CC^*), all of genus 0.

R.<x,y,z> = PolynomialRing(CC, 3)
E  = Variety(x^3 + y^3 + z^3)      # elliptic curve, g=1
C2 = Variety(x^5 + y^5 + z^5)      # genus 6 curve

assert not E.is_toric()
assert not C2.is_toric()

# A K3 surface is NOT toric: a toric surface has χ(O) = 1 and κ = -∞,
# while K3 has χ(O) = 2 and κ = 0.
R4.<u,v,s,w> = PolynomialRing(CC, 4)
S_k3 = Variety(u^4 + v^4 + s^4 + w^4)
assert not S_k3.is_toric()
assert S_k3.holomorphic_euler_characteristic() == 2   # ≠ 1, never toric

# An Enriques surface is NOT toric (κ = 0, not rational)
Y = EnriquesSurface(...)
assert not Y.is_toric()

# A general quintic threefold (Calabi-Yau) is NOT toric
R5.<a,b,c,d,e> = PolynomialRing(CC, 5)
CY3 = Variety(a^5 + b^5 + c^5 + d^5 + e^5)
assert not CY3.is_toric()


# ============================================================================
# Section 7: Toric Riemann-Roch and combinatorics
# ============================================================================
# For a toric variety X = X(Σ) and a T-invariant divisor D = Σ a_ρ V(ρ),
# h^0(X, O(D)) = |{m ∈ M : ⟨m, v_ρ⟩ >= -a_ρ for all rays ρ}|
# i.e., lattice points in the polytope P_D.

# PP^2: O(d) has h^0 = (d+1)(d+2)/2 = |lattice points in d·Δ_2|
for d in range(1, 6):
    L_d = P2.toric_line_bundle(d)
    assert L_d.h0() == (d + 1) * (d + 2) // 2
    assert L_d.polytope().lattice_points().cardinality() == (d + 1) * (d + 2) // 2

# PP^1 × PP^1: O(a,b) has h^0 = (a+1)(b+1) = lattice points in [0,a]×[0,b]
for a, b in [(1,1), (2,3), (4,4)]:
    L_ab = P1xP1.toric_line_bundle(a, b)
    assert L_ab.h0() == (a + 1) * (b + 1)
    assert L_ab.polytope().lattice_points().cardinality() == (a + 1) * (b + 1)
