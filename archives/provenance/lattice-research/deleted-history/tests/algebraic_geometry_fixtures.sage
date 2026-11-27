# ============================================================================
# ALGEBRAIC GEOMETRY FIXTURES
#
# Comprehensive standard examples with all classical invariants asserted
# concretely.  Properties follow from adjunction, Riemann-Roch, Noether,
# the degree-genus formula, Hodge theory, and related classical results.
# Full interface vocabulary: smoothness/singularity loci, adjunction as an
# equation, Picard group membership, linear equivalence, divisorial h^0,
# plurigenera, classification predicates, normalization/resolution, ampleness.
#
# Hodge diamond convention (matching variety_interface_spec.sage):
#   Matrix entry (p, q) = h^{p,q},  rows indexed by p from 0 upward.
#
# ============================================================================


t = polygen(QQ, 't')

# ============================================================================
# 1. PROJECTIVE SPACES PP^1, PP^2, PP^3
# ============================================================================

# K_{PP^n} = -(n+1)H  (general adjunction formula for projective space)
# Hodge numbers: h^{p,q}(PP^n) = delta_{p,q}  (only diagonal entries non-zero)
# Pic(PP^n) = ZZ * H  (Lefschetz; rank 1)
# Kodaira dimension: -Infinity  (K anti-ample)
# Hilbert polynomial: P(t) = C(t+n, n) = (t+1)(t+2)...(t+n)/n!

# --- PP^1 -------------------------------------------------------------------

P1 = PP^1(CC)
assert P1.dimension() == 1
assert P1.is_smooth() and P1.is_projective() and P1.is_quasi_projective()
assert not P1.is_affine()
assert P1.smooth_locus() == P1 and P1.singular_locus() == Variety.empty()
assert P1.normalization() == P1
assert P1.resolution().domain() == P1

assert P1.is_rational() and P1.is_unirational()
assert not P1.is_elliptic() and not P1.is_general_type()
assert P1.geometric_genus() == 0 and P1.arithmetic_genus() == 0
assert P1.irregularity() == 0
assert P1.holomorphic_euler_characteristic() == 1
assert P1.kodaira_dimension() == -Infinity

H1 = P1.hyperplane_class()
# K_{PP^1} = -2H
K_P1 = P1.canonical_divisor()
assert K_P1 == -2 * H1
assert K_P1.degree() == -2   # deg K = 2g - 2 = -2 for g=0
assert K_P1.is_linearly_equivalent_to((-2) * H1)
assert K_P1 in P1.picard_group()
assert H1 in P1.picard_group()

assert H1.is_ample() and H1.is_nef() and H1.is_big()
assert K_P1.is_anti_ample()    # K negative => rational

# h^0 of line bundles on PP^1: h^0(O(d)) = max(d+1, 0)
assert (2 * H1).h(0) == 3
assert H1.h(0) == 2
assert P1.picard_group()(0).h(0) == 1    # h^0(O) = 1
assert K_P1.h(0) == 0                     # h^0(K) = 0 for g=0

# Plurigenera: P_n = h^0(nK) = 0 for all n >= 1 (K anti-ample)
assert [P1.plurigenus(n) for n in range(6)] == [1, 0, 0, 0, 0, 0]

# Picard group rank 1; deg K = 2g-2 = -2
# Noether for a curve: deg K_C = 2g - 2  =>  deg(-2H) = -2 = 2*0 - 2 ✓
assert P1.picard_group().rank() == 1
assert H1.self_intersection() == 1

# Hodge diamond for PP^1:
#   p\q  0  1
#    0  [1  0]
#    1  [0  1]
assert P1.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])

assert P1.hilbert_polynomial(t) == t + 1

# Riemann-Roch on PP^1: for D = d*H, chi(O(d)) = d + 1
for d in range(-3, 6):
    assert (d * H1).hirzebruch_riemann_roch() == d + 1


# --- PP^2 -------------------------------------------------------------------

P2 = PP^2(CC)
assert P2.dimension() == 2
assert P2.is_smooth() and P2.is_projective() and P2.is_quasi_projective()
assert P2.smooth_locus() == P2 and P2.singular_locus() == Variety.empty()
assert P2.normalization() == P2
assert P2.is_rational() and P2.is_unirational()
assert P2.geometric_genus() == 0 and P2.irregularity() == 0
assert P2.holomorphic_euler_characteristic() == 1
assert P2.kodaira_dimension() == -Infinity

H2 = P2.hyperplane_class()
K_P2 = P2.canonical_divisor()
assert K_P2 == -3 * H2
assert K_P2 in P2.picard_group() and H2 in P2.picard_group()
assert K_P2.is_linearly_equivalent_to((-3) * H2)
assert K_P2.is_anti_ample()
assert H2.is_ample() and H2.is_nef() and H2.is_big()

# H^2 = 1  (two general lines in PP^2 meet in one point)
assert H2.self_intersection() == 1     # two lines in PP^2 meet in one point
assert K_P2.self_intersection() == 9
assert P2.topological_euler_characteristic() == 3
assert P2.holomorphic_euler_characteristic() == 1
# Noether: K^2 + chi_top = 12*chi(O)  =>  9 + 3 = 12 ✓
assert K_P2.self_intersection() + P2.topological_euler_characteristic() == 12

assert K_P2.h(0) == 0    # h^0(K_{PP^2}) = 0 (anti-ample)
# Pic(PP^2) = ZZ * H
assert P2.picard_group().rank() == 1

# Hodge diamond:
#   p\q  0  1  2
#    0  [1  0  0]
#    1  [0  1  0]
#    2  [0  0  1]
assert P2.hodge_diamond() == Matrix(ZZ, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
assert [P2.plurigenus(n) for n in range(5)] == [1, 0, 0, 0, 0]
# Hilbert polynomial: P(t) = (t+1)(t+2)/2
assert P2.hilbert_polynomial(t) == (t + 1) * (t + 2) / 2

# Riemann-Roch on PP^2: for D = d*H, chi(O_{PP^2}(d)) = (d+1)(d+2)/2
for d in range(0, 5):
    assert (d * H2).hirzebruch_riemann_roch() == (d + 1) * (d + 2) // 2


# --- PP^3 -------------------------------------------------------------------

P3 = PP^3(CC)
assert P3.dimension() == 3
assert P3.is_smooth() and P3.is_projective()
assert P3.smooth_locus() == P3 and P3.singular_locus() == Variety.empty()
assert P3.is_rational()
assert P3.kodaira_dimension() == -Infinity
assert P3.holomorphic_euler_characteristic() == 1

H3 = P3.hyperplane_class()
K_P3 = P3.canonical_divisor()
assert K_P3 == -4 * H3
assert K_P3 in P3.picard_group()
assert K_P3.is_anti_ample() and H3.is_ample()

# Hodge diamond:
#   p\q  0  1  2  3
#    0  [1  0  0  0]
#    1  [0  1  0  0]
#    2  [0  0  1  0]
#    3  [0  0  0  1]
assert P3.hodge_diamond() == Matrix(ZZ, [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
assert P3.picard_group().rank() == 1


# ============================================================================
# 2. SMOOTH PLANE CURVES IN PP^2
# ============================================================================

# For a smooth plane curve C of degree d in PP^2 (adjunction):
#   K_C = (K_{PP^2} + C)|_C = (-3H + dH)|_C = (d-3) H|_C
#   deg K_C = (d-3)*d
#   chi(O_C) = 1 - g
#   genus: g = (d-1)(d-2)/2
#   Kodaira dimension:
#     d <= 2 (g = 0): kappa = -Infinity  (rational)
#     d = 3  (g = 1): kappa = 0          (elliptic)
#     d >= 4 (g >= 3): kappa = 1         (general type)

R3.<x,y,z> = PolynomialRing(CC, 3)

# --- Degree 1: Line V(x) in PP^2 -------------------------------------------
# K_L = (1-3)H|_L = -2H|_L  (same as K_{PP^1}; deg = -2)

L = Variety(x)
assert L.is_projective() and L.is_hypersurface()
assert L.ambient_variety() == PP^2(CC)
assert L.degree() == 1 and L.dimension() == 1
assert L.is_smooth()
assert L.smooth_locus() == L and L.singular_locus() == Variety.empty()
assert L.normalization() == L and L.resolution().domain() == L

assert L.arithmetic_genus() == 0 and L.geometric_genus() == 0
assert L.irregularity() == 0 and L.holomorphic_euler_characteristic() == 1
assert L.is_rational() and L.is_isomorphic_to(PP^1(CC))
assert not L.is_elliptic() and not L.is_general_type()
assert L.kodaira_dimension() == -Infinity
assert L.is_snc()

H_L = L.hyperplane_class()
K_L = L.canonical_divisor()
# Adjunction formula as an equation
L_div = L.as_divisor()    # L viewed as a divisor in PP^2
assert L_div.is_linearly_equivalent_to(1 * H2)
assert K_L == (P2.canonical_divisor() + L_div).restrict_to(L)
assert K_L == -2 * H_L
assert K_L.degree() == -2
assert K_L.is_linearly_equivalent_to((-2) * H_L)
assert K_L in L.picard_group() and H_L in L.picard_group()
assert K_L.is_anti_ample() and H_L.is_ample()

assert K_L.h(0) == 0      # g=0: no global sections of K
assert H_L.h(0) == 2      # h^0(O_L(1)) = deg + 1 - g = 2
assert [L.plurigenus(n) for n in range(5)] == [1, 0, 0, 0, 0]

assert L.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])
assert L.hilbert_polynomial(t) == t + 1


# --- Degree 2: Smooth Conic V(x^2 + y^2 + z^2) ----------------------------
# Smooth conic in PP^2 is isomorphic to PP^1 (rational normal curve of degree 2)
# K = (2-3)H|_conic = -H|_conic, deg = -2

conic = Variety(x^2 + y^2 + z^2)
assert conic.is_projective() and conic.is_hypersurface()
assert conic.ambient_variety() == PP^2(CC)
assert conic.degree() == 2 and conic.dimension() == 1
assert conic.is_smooth()
assert conic.smooth_locus() == conic and conic.singular_locus() == Variety.empty()
assert conic.normalization() == conic and conic.resolution().domain() == conic

assert conic.arithmetic_genus() == 0 and conic.geometric_genus() == 0
assert conic.irregularity() == 0 and conic.holomorphic_euler_characteristic() == 1
assert conic.is_rational() and conic.is_isomorphic_to(PP^1(CC))
assert conic.kodaira_dimension() == -Infinity
assert conic.is_snc()

H_conic = conic.hyperplane_class()
K_conic = conic.canonical_divisor()
conic_div = conic.as_divisor()
assert conic_div.is_linearly_equivalent_to(2 * H2)
assert K_conic == (P2.canonical_divisor() + conic_div).restrict_to(conic)
assert K_conic == -1 * H_conic
assert K_conic.degree() == -2     # (d-3)*d = -2
assert K_conic.is_linearly_equivalent_to((-1) * H_conic)
assert K_conic.is_anti_ample() and H_conic.is_ample()
assert K_conic in conic.picard_group()

assert K_conic.h(0) == 0
assert [conic.plurigenus(n) for n in range(5)] == [1, 0, 0, 0, 0]
assert conic.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])
assert conic.hilbert_polynomial(t) == 2*t + 1


# --- Degree 3: Smooth Elliptic Curve V(x^3 + y^3 + z^3) -------------------
# Smooth plane cubic: g = 1, Calabi-Yau curve, K = 0
# K_C = (3-3)H|_C = 0: trivial canonical bundle
# Hodge diamond for genus-1 curve:
#   p\q  0  1
#    0  [1  1]
#    1  [1  1]

elliptic = Variety(x^3 + y^3 + z^3)
assert elliptic.is_projective() and elliptic.is_hypersurface()
assert elliptic.ambient_variety() == PP^2(CC)
assert elliptic.degree() == 3 and elliptic.dimension() == 1
assert elliptic.is_smooth()
assert elliptic.smooth_locus() == elliptic and elliptic.singular_locus() == Variety.empty()
assert elliptic.normalization() == elliptic and elliptic.resolution().domain() == elliptic

assert elliptic.arithmetic_genus() == 1 and elliptic.geometric_genus() == 1
assert elliptic.irregularity() == 1
assert elliptic.holomorphic_euler_characteristic() == 0   # chi = 1 - 1 = 0
assert elliptic.is_elliptic() and elliptic.is_calabi_yau() and elliptic.is_abelian_variety()
assert not elliptic.is_rational() and not elliptic.is_general_type()
assert elliptic.kodaira_dimension() == 0
assert elliptic.is_snc()

H_ell = elliptic.hyperplane_class()
K_ell = elliptic.canonical_divisor()
ell_div = elliptic.as_divisor()
assert ell_div.is_linearly_equivalent_to(3 * H2)
assert K_ell == (P2.canonical_divisor() + ell_div).restrict_to(elliptic)
assert K_ell == 0                                         # K trivial
assert K_ell.degree() == 0                               # deg K = 2g-2 = 0
assert K_ell.is_linearly_equivalent_to(elliptic.picard_group()(0))
assert K_ell in elliptic.picard_group()
assert K_ell.is_nef() and not K_ell.is_ample() and not K_ell.is_big()

assert K_ell.h(0) == 1    # h^0(K_C) = g = 1
assert H_ell.h(0) == 3    # h^0(O_C(H)) = d + 1 - g = 3 + 1 - 1 = 3
assert [elliptic.plurigenus(n) for n in range(5)] == [1, 1, 1, 1, 1]

assert elliptic.hodge_diamond() == Matrix(ZZ, [[1, 1], [1, 1]])
# Hilbert polynomial: 3*t  (since p_a=1, chi(O_C(t)) = 3t + 1 - 1 = 3t)
assert elliptic.hilbert_polynomial(t) == 3*t

# Riemann-Roch: chi(O_C(dH)) = 3d for any integer d
for d in range(0, 5):
    assert (d * H_ell).hirzebruch_riemann_roch() == 3*d


# --- Degree 4: Smooth Quartic Curve V(x^4 + y^4 + z^4) --------------------
# Smooth plane quartic: g = 3, general type
# K_C = (4-3)H = H, deg K_C = 4
# Hodge diamond for genus-3 curve

quartic_curve = Variety(x^4 + y^4 + z^4)
assert quartic_curve.is_projective() and quartic_curve.is_hypersurface()
assert quartic_curve.degree() == 4 and quartic_curve.dimension() == 1
assert quartic_curve.is_smooth()
assert quartic_curve.smooth_locus() == quartic_curve
assert quartic_curve.singular_locus() == Variety.empty()
assert quartic_curve.normalization() == quartic_curve

assert quartic_curve.arithmetic_genus() == 3 and quartic_curve.geometric_genus() == 3
assert quartic_curve.irregularity() == 3
assert quartic_curve.holomorphic_euler_characteristic() == -2
assert quartic_curve.is_general_type() and quartic_curve.is_hyperbolic()
assert not quartic_curve.is_rational() and not quartic_curve.is_elliptic()
assert quartic_curve.kodaira_dimension() == 1

H_qc = quartic_curve.hyperplane_class()
K_qc = quartic_curve.canonical_divisor()
qc_div = quartic_curve.as_divisor()
assert qc_div.is_linearly_equivalent_to(4 * H2)
assert K_qc == (P2.canonical_divisor() + qc_div).restrict_to(quartic_curve)
assert K_qc == H_qc                                      # K = H|_C
assert K_qc.degree() == 4                               # (d-3)*d = 4
assert K_qc.is_linearly_equivalent_to(H_qc)
assert K_qc.is_ample() and K_qc.is_big()

assert K_qc.h(0) == 3    # h^0(K_C) = g = 3

# Plurigenera: h^0(nK) = (2n-1)(g-1) for n>=2, g>=2  (Riemann-Roch: chi(nK) = (2n-1)(g-1))
# For g=3: P_1=3, P_2=6, P_3=10, P_4=14
assert [quartic_curve.plurigenus(n) for n in range(5)] == [1, 3, 6, 10, 14]

assert quartic_curve.hodge_diamond() == Matrix(ZZ, [[1, 3], [3, 1]])


# --- Degree 5: Smooth Quintic Curve V(x^5 + y^5 + z^5) --------------------
# g = (5-1)(5-2)/2 = 6
# K_C = 2H, deg = 10

quintic_curve = Variety(x^5 + y^5 + z^5)
assert quintic_curve.is_projective() and quintic_curve.is_hypersurface()
assert quintic_curve.degree() == 5 and quintic_curve.dimension() == 1
assert quintic_curve.is_smooth()
assert quintic_curve.singular_locus() == Variety.empty()

g5 = (5-1)*(5-2)//2    # = 6
assert quintic_curve.arithmetic_genus() == g5 and quintic_curve.geometric_genus() == g5
assert quintic_curve.irregularity() == g5
assert quintic_curve.holomorphic_euler_characteristic() == 1 - g5   # = -5
assert quintic_curve.is_general_type() and quintic_curve.is_hyperbolic()
assert quintic_curve.kodaira_dimension() == 1

H_q5c = quintic_curve.hyperplane_class()
K_q5c = quintic_curve.canonical_divisor()
q5_div = quintic_curve.as_divisor()
assert q5_div.is_linearly_equivalent_to(5 * H2)
assert K_q5c == (P2.canonical_divisor() + q5_div).restrict_to(quintic_curve)
assert K_q5c == 2 * H_q5c
assert K_q5c.degree() == 10
assert K_q5c.is_ample() and K_q5c.is_big()

assert K_q5c.h(0) == g5   # h^0(K) = g = 6
assert quintic_curve.hodge_diamond() == Matrix(ZZ, [[1, g5], [g5, 1]])


# --- Degree-genus loop: d = 1..6 (uniform verification) --------------------
# Consolidates the formulas above.  Smooth model is the Fermat curve x^d+y^d+z^d=0.
# Consolidates the formulas above.  Smooth model is the Fermat curve x^d+y^d+z^d=0.

smooth_plane_curves = {
    1: x,
    2: x^2 + y^2 + z^2,
    3: x^3 + y^3 + z^3,
    4: x^4 + y^4 + z^4,
    5: x^5 + y^5 + z^5,
    6: x^6 + y^6 + z^6,
}

for d, f in smooth_plane_curves.items():
    C  = Variety(f)
    g  = (d - 1) * (d - 2) // 2
    HC = C.hyperplane_class()
    C_div = C.as_divisor()

    assert C.is_smooth() and C.is_hypersurface()
    assert C.dimension() == 1 and C.degree() == d
    assert C.smooth_locus() == C and C.singular_locus() == Variety.empty()
    assert C.normalization() == C and C.resolution().domain() == C
    assert C.is_snc()

    assert C.arithmetic_genus() == g and C.geometric_genus() == g
    assert C.irregularity() == g
    assert C.holomorphic_euler_characteristic() == 1 - g
    assert C.ambient_variety() == PP^2(CC)

    # Adjunction formula as an equation
    assert C_div.is_linearly_equivalent_to(d * H2)
    assert C.canonical_divisor() == (P2.canonical_divisor() + C_div).restrict_to(C)
    assert C.canonical_divisor().degree() == (d - 3) * d
    assert C.canonical_divisor() in C.picard_group()

    # h^0(K_C) = g  (Riemann-Roch + Serre duality)
    assert C.canonical_divisor().h(0) == g

    if g == 0:
        assert C.kodaira_dimension() == -Infinity
        assert C.is_rational() and not C.is_elliptic() and not C.is_general_type()
        assert C.canonical_divisor().is_anti_ample()
        assert [C.plurigenus(n) for n in range(5)] == [1, 0, 0, 0, 0]
    elif g == 1:
        assert C.kodaira_dimension() == 0
        assert C.is_elliptic() and C.is_calabi_yau() and C.is_abelian_variety()
        assert C.canonical_divisor().is_linearly_equivalent_to(C.picard_group()(0))
        assert [C.plurigenus(n) for n in range(5)] == [1, 1, 1, 1, 1]
    else:
        assert C.kodaira_dimension() == 1
        assert C.is_general_type() and C.is_hyperbolic()
        assert C.canonical_divisor().is_ample()

    assert C.hodge_diamond() == Matrix(ZZ, [[1, g], [g, 1]])
    assert C.hilbert_polynomial(t) == d * t + (1 - g)

    for k in range(4):
        assert (k * HC).hirzebruch_riemann_roch() == k * d + 1 - g


# ============================================================================
# 3. SINGULAR PLANE CURVES
# ============================================================================

# --- Nodal cubic: y^2*z - x^2*(x - z) = 0 ---------------------------------
# Affine equation y^2 = x^2*(x-1); node at [0:0:1].
# p_a = 1  (from degree),  p_g = p_a - #nodes = 0.
# Normalization: PP^1.  Resolution: blowup at the node.

f_node = y^2*z - x^2*(x - z)
nodal_cubic = Variety(f_node)
p_node = nodal_cubic([0, 0, 1])

assert nodal_cubic.is_projective() and nodal_cubic.is_hypersurface()
assert nodal_cubic.ambient_variety() == PP^2(CC)
assert nodal_cubic.degree() == 3 and nodal_cubic.dimension() == 1
assert nodal_cubic.is_singular() and not nodal_cubic.is_smooth()

N_sing = nodal_cubic.singular_locus()
N_sm   = nodal_cubic.smooth_locus()
assert p_node in N_sing and p_node not in N_sm
assert N_sing.cardinality() == 1
assert N_sing.is_finite() and N_sing.is_closed()
assert N_sm.is_smooth() and not N_sm.is_singular()
assert not N_sing.is_smooth() and N_sing.is_singular()
assert N_sing.union(N_sm) == nodal_cubic
assert nodal_cubic - N_sing == N_sm

assert p_node.is_singular()
assert p_node.singularity_type() == Singularity("A1")
assert p_node.is_node() and p_node.is_ordinary_double_point()
assert not p_node.is_cusp()
assert p_node.milnor_number() == 1

# p_a from degree; p_g = p_a - #nodes
assert nodal_cubic.arithmetic_genus() == 1
assert nodal_cubic.geometric_genus() == 0
assert nodal_cubic.irregularity() == 0
assert nodal_cubic.normalization().is_isomorphic_to(PP^1(CC))
assert nodal_cubic.normalization().is_smooth()

# blowup at node resolves the singularity
f_res = nodal_cubic.blowup(p_node)
assert f_res.domain().is_smooth()

# Hodge diamond uses p_g, q: same as PP^1 (rational normalization)
assert nodal_cubic.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])
assert nodal_cubic.kodaira_dimension() == -Infinity
assert [nodal_cubic.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]


# --- Cuspidal cubic: y^2*z - x^3 = 0 --------------------------------------
# Affine equation y^2 = x^3; cusp at [0:0:1].
# p_a = 1,  p_g = 0.  Normalization: PP^1.  Resolution: two blowups (A2 singularity).
# p_a = 1, p_g = 0.  Normalization: PP^1.

f_cusp = y^2*z - x^3
cuspidal_cubic = Variety(f_cusp)
p_cusp = cuspidal_cubic([0, 0, 1])

assert cuspidal_cubic.is_projective() and cuspidal_cubic.is_hypersurface()
assert cuspidal_cubic.degree() == 3 and cuspidal_cubic.dimension() == 1
assert cuspidal_cubic.is_singular() and not cuspidal_cubic.is_smooth()

P_sing = cuspidal_cubic.singular_locus()
P_sm   = cuspidal_cubic.smooth_locus()
assert p_cusp in P_sing and p_cusp not in P_sm
assert P_sing.cardinality() == 1
assert P_sing.union(P_sm) == cuspidal_cubic
assert cuspidal_cubic - P_sing == P_sm

assert p_cusp.is_singular()
assert p_cusp.singularity_type() == Singularity("A2")
assert p_cusp.is_cusp() and not p_cusp.is_node()
assert p_cusp.milnor_number() == 2

assert cuspidal_cubic.arithmetic_genus() == 1
assert cuspidal_cubic.geometric_genus() == 0
assert cuspidal_cubic.normalization().is_isomorphic_to(PP^1(CC))

f_res_cusp = cuspidal_cubic.blowup(p_cusp)
assert f_res_cusp.domain().is_singular()  # one blowup does not fully resolve A2

assert cuspidal_cubic.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])
assert cuspidal_cubic.kodaira_dimension() == -Infinity
assert [cuspidal_cubic.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]


# --- Rational sextic with 10 nodes -----------------------------------------
# A degree-6 curve with p_g = 0 must have p_a - p_g = 10 - 0 = 10 nodes.
# (Same curve as in variety_interface_spec, section 7.)
# p_a = (6-1)(6-2)/2 = 10,  p_g = 10 - 10 = 0.

F_sextic = (
    137*x^6
    - 79*x^5*y - 61*x^5*z
    - 244*x^4*y^2 - 423*x^4*y*z - 134*x^4*z^2
    - 438*x^3*y^3 - 585*x^3*y^2*z - 128*x^3*y*z^2 + 19*x^3*z^3
    - 279*x^2*y^4 - 606*x^2*y^3*z - 395*x^2*y^2*z^2 - 61*x^2*y*z^3 + 7*x^2*z^4
    - 137*x*y^5 - 386*x*y^4*z - 550*x*y^3*z^2 - 479*x*y^2*z^3 - 212*x*y*z^4 - 34*x*z^5
    + 9*y^6 - 54*y^5*z - 256*y^4*z^2 - 385*y^3*z^3 - 276*y^2*z^4 - 97*y*z^5 - 13*z^6
)
rational_sextic = Variety(F_sextic)

assert rational_sextic.is_projective() and rational_sextic.is_hypersurface()
assert rational_sextic.degree() == 6 and rational_sextic.dimension() == 1
assert rational_sextic.is_singular() and not rational_sextic.is_smooth()

RS_sing = rational_sextic.singular_locus()
RS_sm   = rational_sextic.smooth_locus()
assert RS_sing.cardinality() == 10
assert RS_sing.is_finite() and RS_sing.is_closed()
assert RS_sing.union(RS_sm) == rational_sextic
assert rational_sextic - RS_sing == RS_sm

assert all(q.is_node() and q.singularity_type() == Singularity("A1") for q in RS_sing)
assert all(q.milnor_number() == 1 for q in RS_sing)

assert rational_sextic.arithmetic_genus() == 10
assert rational_sextic.geometric_genus() == 0
assert rational_sextic.normalization().is_smooth()
assert rational_sextic.normalization().geometric_genus() == 0
assert rational_sextic.normalization().is_isomorphic_to(PP^1(CC))

assert rational_sextic.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])
assert rational_sextic.kodaira_dimension() == -Infinity
assert [rational_sextic.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]


# ============================================================================
# 4. SMOOTH SURFACES IN PP^3
# ============================================================================

# For a smooth degree-d surface S in PP^3 (adjunction):
#   K_S   = (d - 4) H|_S
#   K_S^2 = (d-4)^2 * d   (since H|_S^2 = d)
#   chi_top(S) = d(d^2 - 4d + 6)
#   q = h^{1,0} = 0   (Lefschetz: smooth hypersurface in PP^3 is simply connected)
#   p_g = h^{2,0}:  0 for d<4,  1 for d=4,  C(d-1, 3) for d>=5
#   chi(O_S) = 1 + p_g
#   h^{1,1} = chi_top - 2 - 2*p_g   (from the Hodge decomposition of H^2)
#   Noether: K_S^2 + chi_top = 12*chi(O_S)

R4.<x,y,z,w> = PolynomialRing(CC, 4)

# --- Degree 2: Smooth Quadric Surface in PP^3 --------------------------------
# Q ≅ PP^1 × PP^1 (smooth quadric surface is rational)
# K_Q = -2H, K^2 = 8, chi_top = 4, p_g = 0, chi(O) = 1
# Noether: K^2 + chi_top = 12*chi(O)  =>  8 + 4 = 12 ✓
# Hodge diamond (h^{1,1} = 4 - 2 - 0 = 2):
#   p\q  0  1  2
#    0  [1  0  0]
#    1  [0  2  0]
#    2  [0  0  1]
# Picard group: two rulings l, m with l^2 = 0, m^2 = 0, l*m = 1.
# Gram matrix in (l, m) basis: [[0, 1], [1, 0]]  (hyperbolic lattice H)
# Anti-canonical class -K = 2H is ample; Riemann-Roch: chi(O_Q(nH)) = (n+1)^2

Q = Variety(x^2 + y^2 + z^2 + w^2)
H_Q = Q.hyperplane_class()
Q_div = Q.as_divisor()            # Q as a divisor in PP^3

assert Q.is_projective() and Q.is_hypersurface()
assert Q.ambient_variety() == PP^3(CC)
assert Q.degree() == 2 and Q.dimension() == 2
assert Q.is_smooth() and not Q.is_singular()
assert Q.smooth_locus() == Q and Q.singular_locus() == Variety.empty()
assert Q.normalization() == Q and Q.resolution().domain() == Q

assert Q.is_rational() and Q.is_unirational()
assert not Q.is_k3() and not Q.is_general_type()
assert Q.kodaira_dimension() == -Infinity

assert Q.geometric_genus() == 0 and Q.irregularity() == 0
assert Q.holomorphic_euler_characteristic() == 1
assert Q.topological_euler_characteristic() == 4

K_Q = Q.canonical_divisor()
# Adjunction formula as equation
assert Q_div.is_linearly_equivalent_to(2 * H3)
assert K_Q == (P3.canonical_divisor() + Q_div).restrict_to(Q)
assert K_Q == -2 * H_Q
assert K_Q.self_intersection() == 8    # (d-4)^2 * d = 4*2
assert K_Q.is_anti_ample() and (-K_Q).is_ample()
assert K_Q in Q.picard_group() and H_Q in Q.picard_group()
assert K_Q.is_linearly_equivalent_to((-2) * H_Q)

# h^0(K_Q) = p_g = 0; h^1(K_Q) = q = 0
assert K_Q.h(0) == 0 and K_Q.h(1) == 0
assert H_Q.is_ample() and H_Q.is_nef() and H_Q.is_big()

# Noether: 8 + 4 = 12 ✓
# Noether: K^2 + chi_top = 12*chi(O)  =>  8 + 4 = 12 ✓
assert K_Q.self_intersection() + Q.topological_euler_characteristic() == 12

# Hodge diamond (h^{1,1} = 4 - 2 - 0 = 2):
#   p\q  0  1  2
#    0  [1  0  0]
#    1  [0  2  0]
#    2  [0  0  1]
assert Q.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,2,0],[0,0,1]])
assert [Q.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]

# Picard group: two rulings l, m with l^2 = 0, m^2 = 0, l*m = 1.
# Gram matrix in (l, m) basis: [[0, 1], [1, 0]]  (hyperbolic lattice H)
Pic_Q = Q.picard_group().as_lattice()
assert Pic_Q.rank() == 2
assert Pic_Q.gram_matrix() == Matrix(ZZ, [[0, 1], [1, 0]])

# Anti-canonical class -K = 2H is ample (positive degree); K = -2H is anti-ample
assert (-Q.canonical_divisor()).is_ample()
assert Q.canonical_divisor().is_anti_ample()

# Riemann-Roch: chi(O_Q(nH)) = chi(O_Q) + nH*(nH - K_Q)/2
#   = 1 + n*2*(n+2)/2 = 1 + n(n+2) = (n+1)^2
for n in range(0, 5):
    assert (n * H_Q).hirzebruch_riemann_roch() == (n + 1)^2


# --- Degree 3: Smooth Cubic Surface in PP^3 (del Pezzo dP_3) ----------------
# Isomorphic to Bl_6 PP^2; has exactly 27 lines.
# K_S = -H, K^2 = 3, chi_top = 9, p_g = 0, chi(O) = 1

S3 = Variety(x^3 + y^3 + z^3 + w^3)
H_S3 = S3.hyperplane_class()
S3_div = S3.as_divisor()

assert S3.is_projective() and S3.is_hypersurface()
assert S3.ambient_variety() == PP^3(CC)
assert S3.degree() == 3 and S3.dimension() == 2
assert S3.is_smooth()
assert S3.smooth_locus() == S3 and S3.singular_locus() == Variety.empty()
assert S3.normalization() == S3

assert S3.is_rational() and not S3.is_k3()
assert S3.kodaira_dimension() == -Infinity

assert S3.geometric_genus() == 0 and S3.irregularity() == 0
assert S3.holomorphic_euler_characteristic() == 1
assert S3.topological_euler_characteristic() == 9

K_S3 = S3.canonical_divisor()
assert S3_div.is_linearly_equivalent_to(3 * H3)
assert K_S3 == (P3.canonical_divisor() + S3_div).restrict_to(S3)
assert K_S3 == -1 * H_S3
assert K_S3.self_intersection() == 3
assert K_S3.is_linearly_equivalent_to((-1) * H_S3)
assert K_S3.is_anti_ample() and (-K_S3).is_ample()
assert K_S3 in S3.picard_group()

assert K_S3.h(0) == 0     # p_g = 0
assert K_S3.h(1) == 0     # q = 0
assert (-K_S3).h(0) == 4  # h^0(-K_{S3}) = h^0(O_{S3}(H)) = ... sections of H|_{S3}
# By exact sequence 0->O_{PP^3}(-2)->O_{PP^3}(1)->O_{S3}(1)->0:
# h^0(O_{S3}(1)) = h^0(O_{PP^3}(1)) = 4

# Noether: 3 + 9 = 12 ✓
assert K_S3.self_intersection() + S3.topological_euler_characteristic() == 12

assert S3.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,7,0],[0,0,1]])
assert [S3.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]

# -K = H is ample: cubic surface is a del Pezzo surface of degree 3
assert (-S3.canonical_divisor()).is_ample()

# Riemann-Roch: chi(O_{S3}(nH)) = chi(O) + nH*(nH - K)/2
#   K = -H, so nH - K = (n+1)H.  H^2 = 3 on S3.
#   chi(nH) = 1 + n*(n+1)*3/2  =  (3n^2 + 3n + 2)/2
for n in range(0, 5):
    chi_expected = 1 + n * (n + 1) * 3 // 2    # integer for all n >= 0
    assert (n * H_S3).hirzebruch_riemann_roch() == chi_expected


# --- Degree 4: Fermat Quartic Surface (K3) ----------------------------------
# K_S = 0, K^2 = 0, chi_top = 24, p_g = 1, chi(O) = 2

S4 = Variety(x^4 + y^4 + z^4 + w^4)
H_S4 = S4.hyperplane_class()
S4_div = S4.as_divisor()

assert S4.is_projective() and S4.is_hypersurface()
assert S4.ambient_variety() == PP^3(CC)
assert S4.degree() == 4 and S4.dimension() == 2
assert S4.is_smooth()
assert S4.smooth_locus() == S4 and S4.singular_locus() == Variety.empty()
assert S4.normalization() == S4

assert S4.is_k3() and S4.is_calabi_yau()
assert not S4.is_rational() and not S4.is_general_type()
assert S4.kodaira_dimension() == 0

assert S4.geometric_genus() == 1 and S4.irregularity() == 0
assert S4.holomorphic_euler_characteristic() == 2
assert S4.topological_euler_characteristic() == 24

Pic_S4 = S4.picard_group()
K_S4 = S4.canonical_divisor()
assert S4_div.is_linearly_equivalent_to(4 * H3)
assert K_S4 == (P3.canonical_divisor() + S4_div).restrict_to(S4)
assert K_S4 == 0
assert K_S4.self_intersection() == 0
assert K_S4.is_linearly_equivalent_to(Pic_S4(0))
assert K_S4 in Pic_S4
assert K_S4.is_nef() and not K_S4.is_ample() and not K_S4.is_big()

# K = 0 is nef but not ample; H is ample (embedding in PP^3)
assert K_S4.h(0) == 1    # h^0(K_{S4}) = p_g = 1
assert K_S4.h(1) == 0    # q = 0
assert H_S4.is_ample() and H_S4.is_nef() and H_S4.is_big()

# Linear system: quartic surface itself belongs to |4H| in PP^3
assert S4_div in (4 * H3).linear_system()
assert S4_div.is_linearly_equivalent_to(4 * H3)

# Noether: 0 + 24 = 12*2 ✓
assert K_S4.self_intersection() + S4.topological_euler_characteristic() == 24

# K3 Hodge diamond (h^{1,1} = 24 - 2 - 2 = 20):
#   p\q  0   1  2
#    0  [1   0  1]
#    1  [0  20  0]
#    2  [1   0  1]
assert S4.hodge_diamond() == Matrix(ZZ, [[1,0,1],[0,20,0],[1,0,1]])
# For a K3 surface P_n = 1 for all n >= 0 (K trivial)
assert [S4.plurigenus(n) for n in range(5)] == [1, 1, 1, 1, 1]

# Riemann-Roch: chi(O_{S4}(nH)) = chi(O) + (nH)^2/2  (since K = 0)
#   = 2 + n^2*4/2 = 2 + 2n^2
for n in range(0, 5):
    assert (n * H_S4).hirzebruch_riemann_roch() == 2 + 2 * n^2


# --- Degree 5: Smooth Quintic Surface in PP^3 (general type) ---------------
# K_S = H, K^2 = 5, chi_top = 55, p_g = 4, chi(O) = 5
# Hodge diamond (h^{1,1} = 55 - 2 - 8 = 45):
#   p\q  0   1  2
#    0  [1   0  4]
#    1  [0  45  0]
#    2  [4   0  1]
# Riemann-Roch: chi(O_{S5}(nH)) = 5 + 5*n*(n-1)/2

S5 = Variety(x^5 + y^5 + z^5 + w^5)
H_S5 = S5.hyperplane_class()
S5_div = S5.as_divisor()

assert S5.is_projective() and S5.is_hypersurface()
assert S5.ambient_variety() == PP^3(CC)
assert S5.degree() == 5 and S5.dimension() == 2
assert S5.is_smooth()
assert S5.smooth_locus() == S5 and S5.singular_locus() == Variety.empty()

assert S5.is_general_type() and not S5.is_rational() and not S5.is_k3()
assert S5.kodaira_dimension() == 2

assert S5.geometric_genus() == 4 and S5.irregularity() == 0
assert S5.holomorphic_euler_characteristic() == 5
assert S5.topological_euler_characteristic() == 55

K_S5 = S5.canonical_divisor()
assert S5_div.is_linearly_equivalent_to(5 * H3)
assert K_S5 == (P3.canonical_divisor() + S5_div).restrict_to(S5)
assert K_S5 == H_S5
assert K_S5.self_intersection() == 5
assert K_S5.is_linearly_equivalent_to(H_S5)
assert K_S5.is_ample() and K_S5.is_big()
assert K_S5 in S5.picard_group()

assert K_S5.h(0) == 4    # h^0(K_{S5}) = p_g = 4
assert K_S5.h(1) == 0    # q = 0

# Noether: 5 + 55 = 60 = 12*5 ✓
assert K_S5.self_intersection() + S5.topological_euler_characteristic() == 60

assert S5.hodge_diamond() == Matrix(ZZ, [[1,0,4],[0,45,0],[4,0,1]])
assert [S5.plurigenus(n) for n in range(4)] == [1, 4, 10, 20]  # P_n = chi(nK)
# P_1=p_g=4; P_2=chi(2K_{S5})=5+5*2*1//2=10; P_3=5+5*3*2//2=20; yes.

for n in range(0, 5):
    assert (n * H_S5).hirzebruch_riemann_roch() == 5 + 5 * n * (n - 1) // 2


# --- Noether loop for d = 2..5 (uniform verification) ----------------------

def _pg(d):
    if d < 4:
        return 0
    elif d == 4:
        return 1
    else:
        return binomial(d - 1, 3)

surfaces_in_PP3 = {
    2: x^2 + y^2 + z^2 + w^2,
    3: x^3 + y^3 + z^3 + w^3,
    4: x^4 + y^4 + z^4 + w^4,
    5: x^5 + y^5 + z^5 + w^5,
}

for d, f in surfaces_in_PP3.items():
    S   = Variety(f)
    pg  = _pg(d)
    chi_top = d * (d^2 - 4*d + 6)
    K2  = (d - 4)^2 * d
    chi_O = 1 + pg

    assert S.is_smooth() and S.is_hypersurface()
    assert S.dimension() == 2 and S.degree() == d
    assert S.smooth_locus() == S and S.singular_locus() == Variety.empty()
    assert S.normalization() == S
    assert S.ambient_variety() == PP^3(CC)

    assert S.geometric_genus() == pg and S.irregularity() == 0
    assert S.holomorphic_euler_characteristic() == chi_O
    assert S.topological_euler_characteristic() == chi_top

    S_div = S.as_divisor()
    K_S = S.canonical_divisor()

    assert S_div.is_linearly_equivalent_to(d * H3)
    assert K_S == (P3.canonical_divisor() + S_div).restrict_to(S)
    assert K_S == (d - 4) * S.hyperplane_class()
    assert K_S.self_intersection() == K2
    assert K_S.h(0) == pg and K_S.h(1) == 0
    assert K_S in S.picard_group()

    assert K2 + chi_top == 12 * chi_O    # Noether

    assert S.hodge_diamond() == Matrix(ZZ, [[1, 0, pg], [0, chi_top - 2 - 2*pg, 0], [pg, 0, 1]])


# ============================================================================
# 5. BLOWUPS OF PP^2
# ============================================================================

# For a blowup pi: Bl_k PP^2 -> PP^2 at k smooth points p_1,...,p_k:
#   Pic(Bl_k PP^2) = ZZ*Hp + ZZ*E_1 + ... + ZZ*E_k
#   Gram matrix: diag(1, -1, ..., -1)  (the lattice I_{1,k})
#   K_{Bl_k PP^2} = -3*Hp + E_1 + ... + E_k
#   K^2 = 9 - k
#   chi_top(Bl_k PP^2) = chi(PP^2) + k = 3 + k
#   p_g = q = 0, chi(O) = 1  (rational surface)

# --- Blowup at one point: Bl_1 PP^2  (del Pezzo dP_8) ----------------------
# Pic(Bl_1 PP^2): Gram matrix diag(1, -1) in basis (Hp1, E1)
# K = -3*Hp + E,  K^2 = 9 - 1 = 8
# Noether: 8 + 4 = 12*1 ✓
# Hodge diamond: h^{1,1} = 4 - 2 = 2
# -K = 3Hp - E is ample (del Pezzo of degree 8); E is not nef: E^2 = -1 < 0

p0 = PP^2(CC).point([0, 0, 1])
pi1 = PP^2(CC).blowup(p0)
S_dP8 = pi1.domain()

assert S_dP8.is_smooth() and S_dP8.is_rational() and S_dP8.dimension() == 2
assert S_dP8.smooth_locus() == S_dP8 and S_dP8.singular_locus() == Variety.empty()
assert S_dP8.geometric_genus() == 0 and S_dP8.irregularity() == 0
assert S_dP8.holomorphic_euler_characteristic() == 1
assert S_dP8.topological_euler_characteristic() == 4
assert pi1.is_birational()

E1 = pi1.exceptional_divisor()
Hp1 = pi1.pullback(PP^2(CC).hyperplane_class())

assert E1.is_isomorphic_to(PP^1(CC))
assert E1.is_smooth() and E1.dimension() == 1
assert E1.self_intersection() == -1

assert pi1.exceptional_locus().cardinality() == 1
assert pi1.exceptional_locus().is_smooth()
assert pi1(E1) == p0     # E1 maps to the blown-up point

# E1 is in the Picard group; Hp1 and E1 generate Pic with gram diag(1,-1)
assert E1.as_divisor() in S_dP8.picard_group()
assert Hp1 in S_dP8.picard_group()
Pic_dP8 = S_dP8.picard_group().as_lattice()
assert Pic_dP8.rank() == 2
assert Pic_dP8.gram_matrix() == Matrix(ZZ, [[1, 0], [0, -1]])

K_dP8 = S_dP8.canonical_divisor()
assert K_dP8 == -3 * Hp1 + E1.as_divisor()
assert K_dP8.self_intersection() == 8
assert K_dP8 in S_dP8.picard_group()
assert K_dP8.is_linearly_equivalent_to(-3 * Hp1 + E1.as_divisor())

assert K_dP8.h(0) == 0 and K_dP8.h(1) == 0   # p_g = q = 0

# -K = 3Hp - E is ample on Bl_1 PP^2 (del Pezzo of degree 8).
# (-K)·E = (3Hp-E)·E = 3*0 - (-1) = 1 > 0, and there are no (-2)-curves
# (one blowup at a generic point introduces none), so -K passes the Nakai
# criterion and is ample.
assert (-K_dP8).is_ample() and (-K_dP8).is_nef() and (-K_dP8).is_big()

# E is not nef: E^2 = -1 < 0
assert not E1.as_divisor().is_nef()

# Noether: 8 + 4 = 12 ✓
assert K_dP8.self_intersection() + S_dP8.topological_euler_characteristic() == 12
assert S_dP8.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,2,0],[0,0,1]])
assert [S_dP8.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]

# Riemann-Roch: chi(O(D)) = chi(O) + D*(D-K)/2
# For D = Hp: D^2 = 1, D*K = -3; D*(D-K)/2 = (1+3)/2 = 2; chi = 1 + 2 = 3
assert Hp1.hirzebruch_riemann_roch() == 3
# For D = -K = 3Hp-E: D^2 = 8, D*K = -8; D*(D-K)/2 = (8+8)/2 = 8; chi = 9
assert (-K_dP8).hirzebruch_riemann_roch() == 9
# For D = E: D^2 = -1, D*K = E*(-3Hp+E) = -3*0 + (-1) = -1
#   D*(D-K)/2 = (-1-(-1))/2 = 0; chi = 1
assert E1.as_divisor().hirzebruch_riemann_roch() == 1


# --- Blowup at six points: Bl_6 PP^2  (isomorphic to a cubic surface) ------
# Pic = ZZ*Hp + ZZ*E_1 + ... + ZZ*E_6, gram matrix diag(1,-1,...,-1) = I_{1,6}
# K = -3*Hp + E_1 + ... + E_6,  K^2 = 9 - 6 = 3
# Noether: 3 + 9 = 12*1 ✓

pts6 = [PP^2(CC).point(p) for p in [
    [1,0,0], [0,1,0], [0,0,1], [1,1,0], [1,0,1], [0,1,1]
]]
pi6 = PP^2(CC).blowup(pts6)
S_dP3 = pi6.domain()

assert S_dP3.is_smooth() and S_dP3.is_rational() and S_dP3.dimension() == 2
assert S_dP3.smooth_locus() == S_dP3 and S_dP3.singular_locus() == Variety.empty()
assert S_dP3.holomorphic_euler_characteristic() == 1
assert S_dP3.topological_euler_characteristic() == 9
assert pi6.is_birational()

Eis6 = pi6.exceptional_locus()
assert Eis6.cardinality() == 6
assert Eis6.is_smooth()
assert all(Ei.self_intersection() == -1 for Ei in Eis6)
assert all(Ei.is_isomorphic_to(PP^1(CC)) for Ei in Eis6)
assert all(Ei.as_divisor() in S_dP3.picard_group() for Ei in Eis6)

Hp6 = pi6.pullback(PP^2(CC).hyperplane_class())
Pic_dP3 = S_dP3.picard_group().as_lattice()
assert Pic_dP3.rank() == 7
assert Pic_dP3.is_isometric_to(Lattice.I(1, 6))

K_dP3 = S_dP3.canonical_divisor()
assert K_dP3 == -3 * Hp6 + sum(Ei.as_divisor() for Ei in Eis6)
assert K_dP3.self_intersection() == 3
assert K_dP3.is_linearly_equivalent_to(-3 * Hp6 + sum(Ei.as_divisor() for Ei in Eis6))
assert K_dP3 in S_dP3.picard_group()
assert K_dP3.h(0) == 0 and K_dP3.h(1) == 0

assert (-K_dP3).is_ample()
assert K_dP3.self_intersection() + S_dP3.topological_euler_characteristic() == 12
assert S_dP3.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,7,0],[0,0,1]])
assert [S_dP3.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]


# --- Blowup loop: K^2 and chi_top decrease by 1 per blown-up point ----------
# Bl_k PP^2: K^2 = 9-k, chi_top = 3+k, Pic rank = k+1, Picard lattice I_{1,k}

PP2 = PP^2(CC)
for k in range(1, 9):
    pts_k = [PP2.point([Integer(i), Integer(i^2 % 7), 1]) for i in range(k)]
    pi_k  = PP2.blowup(pts_k)
    Sk    = pi_k.domain()

    assert Sk.is_smooth() and Sk.is_rational()
    assert Sk.smooth_locus() == Sk and Sk.singular_locus() == Variety.empty()
    assert pi_k.is_birational()

    assert Sk.topological_euler_characteristic() == 3 + k
    assert Sk.holomorphic_euler_characteristic() == 1
    assert Sk.geometric_genus() == 0 and Sk.irregularity() == 0

    Eks  = pi_k.exceptional_locus()
    assert Eks.cardinality() == k
    assert Eks.is_smooth()
    assert all(Ei.self_intersection() == -1 for Ei in Eks)

    Hp_k = pi_k.pullback(PP2.hyperplane_class())
    K_k  = Sk.canonical_divisor()

    assert K_k == -3 * Hp_k + sum(Ei.as_divisor() for Ei in Eks)
    assert K_k.self_intersection() == 9 - k
    assert K_k.h(0) == 0 and K_k.h(1) == 0
    assert K_k in Sk.picard_group()
    assert K_k.self_intersection() + Sk.topological_euler_characteristic() == 12

    # h^{1,1} = k+1 for Bl_k PP^2 (rational surface: p_g = q = 0)
    assert Sk.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,k+1,0],[0,0,1]])
    assert [Sk.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]

    Pic_k = Sk.picard_group().as_lattice()
    assert Pic_k.rank() == k + 1
    assert Pic_k.is_isometric_to(Lattice.I(1, k))


# ============================================================================
# 6. K3 SURFACES: COMPLETE INTERSECTIONS
# ============================================================================

# A smooth complete intersection of type (d_1,...,d_r) in PP^{r+2} is K3 iff
#   sum(d_i) = r + 3  (adjunction: K = (sum d_i - (r+3)) H = 0)
# The complete K3 list:
#   (4)     in PP^3   (quartic hypersurface)
#   (2, 3)  in PP^4   (quadric ∩ cubic)
#   (2,2,2) in PP^5   (three quadrics)
# All have: K = 0, p_g = 1, q = 0, chi(O) = 2, chi_top = 24, h^{1,1} = 20.

R5.<u0,u1,u2,u3,u4> = PolynomialRing(CC, 5)

# --- (2,3) complete intersection K3 in PP^4 ---------------------------------
# Adjunction: K = (2+3-5)H = 0.  Degree = 2*3 = 6.

K3_23 = Variety([u0^2 + u1^2 + u2^2 + u3^2 + u4^2,
                 u0^3 + u1^3 + u2^3 + u3^3 + u4^3])

assert K3_23.is_projective() and K3_23.dimension() == 2
assert K3_23.is_smooth()
assert K3_23.smooth_locus() == K3_23 and K3_23.singular_locus() == Variety.empty()
assert K3_23.normalization() == K3_23

assert K3_23.is_k3() and K3_23.is_calabi_yau()
assert not K3_23.is_rational() and not K3_23.is_general_type()
assert K3_23.kodaira_dimension() == 0
assert K3_23.degree() == 6 and K3_23.dimension() == 2

assert K3_23.geometric_genus() == 1 and K3_23.irregularity() == 0
assert K3_23.holomorphic_euler_characteristic() == 2
assert K3_23.topological_euler_characteristic() == 24

Pic_K3_23 = K3_23.picard_group()
K_K3_23 = K3_23.canonical_divisor()
assert K_K3_23 == 0
assert K_K3_23.is_linearly_equivalent_to(Pic_K3_23(0))
assert K_K3_23 in Pic_K3_23
assert K_K3_23.is_nef() and not K_K3_23.is_ample() and not K_K3_23.is_big()

assert K_K3_23.h(0) == 1   # p_g = 1
assert K_K3_23.h(1) == 0   # q = 0
assert [K3_23.plurigenus(n) for n in range(5)] == [1, 1, 1, 1, 1]

# Noether: 0 + 24 = 12*2 ✓
assert K_K3_23.self_intersection() + K3_23.topological_euler_characteristic() == 24

assert K3_23.hodge_diamond() == Matrix(ZZ, [[1,0,1],[0,20,0],[1,0,1]])

H_K3_23 = K3_23.hyperplane_class()
assert H_K3_23.is_ample() and H_K3_23.is_nef() and H_K3_23.is_big()
assert H_K3_23 in Pic_K3_23

for n in range(0, 5):
    assert (n * H_K3_23).hirzebruch_riemann_roch() == 2 + 3 * n^2


# --- (2,2,2) complete intersection K3 in PP^5 --------------------------------
# Adjunction: K = (2+2+2-6)H = 0.  Degree = 2^3 = 8.

R6.<v0,v1,v2,v3,v4,v5> = PolynomialRing(CC, 6)

K3_222 = Variety([
    v0^2 + v1^2 + v2^2 + v3^2 + v4^2 + v5^2,
    v0^2 + 2*v1^2 + 3*v2^2 + 4*v3^2 + 5*v4^2 + 6*v5^2,
    v0^2 + 4*v1^2 + 9*v2^2 + 16*v3^2 + 25*v4^2 + 36*v5^2,
])

assert K3_222.is_projective() and K3_222.dimension() == 2
assert K3_222.is_smooth()
assert K3_222.smooth_locus() == K3_222 and K3_222.singular_locus() == Variety.empty()

assert K3_222.is_k3() and K3_222.is_calabi_yau()
assert K3_222.kodaira_dimension() == 0
assert K3_222.degree() == 8

assert K3_222.geometric_genus() == 1 and K3_222.irregularity() == 0
assert K3_222.holomorphic_euler_characteristic() == 2
assert K3_222.topological_euler_characteristic() == 24

Pic_K3_222 = K3_222.picard_group()
K_K3_222 = K3_222.canonical_divisor()
assert K_K3_222 == 0
assert K_K3_222.is_linearly_equivalent_to(Pic_K3_222(0))
assert K_K3_222.h(0) == 1 and K_K3_222.h(1) == 0
assert [K3_222.plurigenus(n) for n in range(5)] == [1, 1, 1, 1, 1]

assert K_K3_222.self_intersection() + K3_222.topological_euler_characteristic() == 24
assert K3_222.hodge_diamond() == Matrix(ZZ, [[1,0,1],[0,20,0],[1,0,1]])

H_K3_222 = K3_222.hyperplane_class()
assert H_K3_222.is_ample() and H_K3_222 in Pic_K3_222

for n in range(0, 5):
    assert (n * H_K3_222).hirzebruch_riemann_roch() == 2 + 4 * n^2
# Riemann-Roch: chi(nH) = 2 + n^2*8/2 = 2 + 4n^2  ✓


# --- K3 Picard group (rank 1 base case) --------------------------------------
# A "general" (Picard-number-1) K3 with polarisation H: Pic = ZZ*H,
# with H^2 = 2g-2 for genus g >= 2.  The simplest case: H^2 = 2 (g=2).
# h^0(H) = g = 2 by Riemann-Roch on K3: chi(H) = 2 + H^2/2 = 2 + 1 = 3;
# by Kodaira vanishing h^2(H) = h^0(K-H) = h^0(-H) = 0 and h^1(H) = 0,
# so h^0(H) = 3 for a (2,0)-polarised K3.

# For the quartic K3 S4 (above): H^2 = 4, Pic ≥ rank 1.
# The hyperplane class satisfies H^2 = 4; by R-R chi(nH) = 2 + 2n^2 as verified.


# ============================================================================
# 7. ENRIQUES SURFACES
# ============================================================================

# An Enriques surface Y has:
#   K_Y ≠ 0 but 2*K_Y = 0  (torsion canonical class of order 2)
#   p_g = 0, q = 0, chi(O_Y) = 1
#   chi_top = 12, K^2 = 0
#   Kodaira dimension: 0
#   Universal K3 cover: the unramified double cover pi: X -> Y with X a K3 surface
#   Hodge diamond:
#     p\q  0  1  2
#      0  [1  0  0]
#      1  [0 10  0]
#      2  [0  0  1]
#
# An EnriquesSurface object carries the universal K3 cover; the Enriques
# involution iota is the deck transformation of pi.

Y = EnriquesSurface(...)

assert Y.is_projective() and Y.dimension() == 2
assert Y.is_smooth()
assert Y.smooth_locus() == Y and Y.singular_locus() == Variety.empty()
assert Y.normalization() == Y

assert Y.is_enriques() and Y.is_calabi_yau() == False
assert not Y.is_rational() and not Y.is_k3() and not Y.is_general_type()
assert Y.kodaira_dimension() == 0

assert Y.geometric_genus() == 0 and Y.irregularity() == 0
assert Y.holomorphic_euler_characteristic() == 1
assert Y.topological_euler_characteristic() == 12
assert [Y.plurigenus(n) for n in range(5)] == [1, 0, 1, 0, 1]  # P_n = 1 if n even, 0 if odd

K_Y = Y.canonical_divisor()
# Canonical class: torsion of order 2 (2K_Y ~ 0 but K_Y ≁ 0)
assert K_Y in Y.picard_group()
assert not K_Y.is_linearly_equivalent_to(Y.picard_group()(0))   # K_Y ≠ 0
assert (2 * K_Y).is_linearly_equivalent_to(Y.picard_group()(0)) # 2*K_Y = 0
assert K_Y.order_in_picard_group() == 2
assert K_Y.self_intersection() == 0
assert K_Y.is_nef() and not K_Y.is_ample() and not K_Y.is_big()
assert K_Y.h(0) == 0    # p_g = 0
assert K_Y.h(1) == 0    # q = 0

# Noether: K^2 + chi_top = 0 + 12 = 12*1 ✓
assert K_Y.self_intersection() + Y.topological_euler_characteristic() == 12

# Hodge diamond (h^{1,1} = 12 - 2 - 0 = 10):
assert Y.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,10,0],[0,0,1]])

# Unramified K3 double cover
f_k3 = Y.k3_cover()
X_k3 = f_k3.domain()
assert f_k3.codomain() == Y
assert f_k3.degree() == 2
assert f_k3.branch_divisor() == Variety.empty()    # unramified
assert X_k3.is_k3()

# Deck transformation = Enriques involution iota
iota = Y.enriques_involution()
assert iota.order() == 2
assert iota in X_k3.Aut()
assert iota.fixed_locus() == Variety.empty()        # free action
assert X_k3.quotient(iota) == Y


# ============================================================================
# 8. AMPLENESS, NEF-NESS, BIG-NESS
# ============================================================================

# Ample <=> Kodaira embedding theorem (positive curvature)
# Nef   <=> D·C >= 0 for all effective curves C
# Big   <=> h^0(nD) grows like n^dim

# Ample => Nef, Ample => Big.  Nef + Big does NOT imply Ample.

# H on PP^n: ample, nef, big
H3_amp = P3.hyperplane_class()
assert H3_amp.is_ample() and H3_amp.is_nef() and H3_amp.is_big()
assert (-H3_amp).is_anti_ample() and not (-H3_amp).is_nef()

# K3 surface (S4): K = 0 is nef but not ample, not big; H|_{S4} is the ample polarisation
assert S4.canonical_divisor().is_nef()
assert not S4.canonical_divisor().is_ample() and not S4.canonical_divisor().is_big()
assert H_S4.is_ample() and H_S4.is_nef() and H_S4.is_big()

# Quintic (S5): K=H ample
assert S5.canonical_divisor().is_ample() and S5.canonical_divisor().is_big()

# Cubic surface (S3): K anti-ample; -K ample
assert S3.canonical_divisor().is_anti_ample()
assert (-S3.canonical_divisor()).is_ample() and (-S3.canonical_divisor()).is_nef()

# Quadric (Q): K = -2H anti-ample
assert Q.canonical_divisor().is_anti_ample()
assert (-Q.canonical_divisor()).is_ample()

# Blowup Bl_1 PP^2: E not nef; -K ample
assert not E1.as_divisor().is_nef()
assert (-K_dP8).is_ample() and (-K_dP8).is_nef() and (-K_dP8).is_big()

# Enriques surface: K nef but not ample, not big
assert K_Y.is_nef() and not K_Y.is_ample() and not K_Y.is_big()


# ============================================================================
# 9. RATIONALITY AND UNIRATIONALITY
# ============================================================================

# Rationality:
# Rational:    birational to PP^n
# Unirational: dominant rational map PP^n --> X
# Rational => Unirational
# Curves: rational iff genus 0
# Surfaces: classical rationality results
assert P1.is_rational() and P1.is_unirational()
assert conic.is_rational() and conic.is_unirational()
assert not elliptic.is_rational() and not elliptic.is_unirational()   # g=1
assert not quartic_curve.is_rational() and not quartic_curve.is_unirational()  # g=3

# Surfaces: classical rationality results
assert Q.is_rational() and Q.is_unirational()    # smooth quadric ≅ PP^1 × PP^1
assert S3.is_rational() and S3.is_unirational()  # smooth cubic surface (Cayley-Salmon)
assert not S4.is_rational()   # K3 surface (Kodaira dim 0, non-trivial 2-form)
assert not S5.is_rational() and not S5.is_unirational()  # general type
assert not Y.is_rational()    # Enriques surface
assert not S5.is_rational() and not S5.is_unirational()
assert not Y.is_rational()
