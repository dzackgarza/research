# ============================================================================
# FIXTURE: SMOOTH PLANE CURVES IN PP^2
#
# For a smooth plane curve C of degree d in PP^2 (adjunction):
#   K_C = (K_{PP^2} + C)|_C = (-3H + dH)|_C = (d-3) H|_C
#   deg K_C = (d-3)*d,  genus g = (d-1)(d-2)/2
#   Kodaira dimension:
#     d <= 2 (g=0): kappa = -Infinity  (rational)
#     d = 3  (g=1): kappa = 0          (elliptic / Calabi-Yau)
#     d >= 4 (g>=3): kappa = 1         (general type)
# ============================================================================

t = polygen(QQ, 't')

R3.<x,y,z> = PolynomialRing(CC, 3)
P2 = PP^2(CC)
H2 = P2.hyperplane_class()


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
# Hodge diamond for genus-3 curve:
#   p\q  0  1
#    0  [1  3]
#    1  [3  1]

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

# Plurigenera: P_n = h^0(nK) = (2n-1)(g-1) for n>=2, g>=2
# For g=3: P_1=3, P_2=6, P_3=10, P_4=14
assert [quartic_curve.plurigenus(n) for n in range(5)] == [1, 3, 6, 10, 14]

assert quartic_curve.hodge_diamond() == Matrix(ZZ, [[1, 3], [3, 1]])


# --- Degree 5: Smooth Quintic Curve V(x^5 + y^5 + z^5) --------------------
# g = (5-1)(5-2)/2 = 6, K_C = 2H, deg = 10

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
# Smooth Fermat curve x^d + y^d + z^d = 0 consolidates all of the above.

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
