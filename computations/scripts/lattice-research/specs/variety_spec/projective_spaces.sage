# ============================================================================
# FIXTURE: PROJECTIVE SPACES PP^1, PP^2, PP^3
#
# Classical invariants of projective space asserted concretely.
# K_{PP^n} = -(n+1)H  (adjunction)
# Hodge numbers: h^{p,q}(PP^n) = delta_{p,q}  (only diagonal non-zero)
# Pic(PP^n) = ZZ * H  (Lefschetz; rank 1)
# Kodaira dimension: -Infinity  (K anti-ample)
# Hilbert polynomial: P(t) = (t+1)...(t+n)/n!
# ============================================================================

t = polygen(QQ, "t")


# --- PP^1 -------------------------------------------------------------------

P1 = PP ^ 1(CC)
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
assert K_P1.degree() == -2  # deg K = 2g - 2 = -2 for g=0
assert K_P1.is_linearly_equivalent_to((-2) * H1)
assert K_P1 in P1.picard_group()
assert H1 in P1.picard_group()

assert H1.is_ample() and H1.is_nef() and H1.is_big()
assert K_P1.is_anti_ample()  # K negative => rational

# h^0 of line bundles on PP^1: h^0(O(d)) = max(d+1, 0)
assert (2 * H1).h(0) == 3
assert H1.h(0) == 2
assert P1.picard_group()(0).h(0) == 1  # h^0(O) = 1
assert K_P1.h(0) == 0  # h^0(K) = 0 for g=0

# Plurigenera: P_n = h^0(nK) = 0 for all n >= 1 (K anti-ample)
assert [P1.plurigenus(n) for n in range(6)] == [1, 0, 0, 0, 0, 0]

# Pic(PP^1) = ZZ * H, H^2 = 1
assert P1.picard_group().rank() == 1
assert H1.self_intersection() == 1

# Hodge diamond for PP^1:
#   p\q  0  1
#    0  [1  0]
#    1  [0  1]
assert P1.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])

assert P1.hilbert_polynomial(t) == t + 1

# Riemann-Roch on PP^1: chi(O(d)) = d + 1
for d in range(-3, 6):
    assert (d * H1).hirzebruch_riemann_roch() == d + 1


# --- PP^2 -------------------------------------------------------------------

P2 = PP ^ 2(CC)
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
assert H2.self_intersection() == 1
assert K_P2.self_intersection() == 9
assert P2.topological_euler_characteristic() == 3
assert P2.holomorphic_euler_characteristic() == 1

# Noether: K^2 + chi_top = 12*chi(O)  =>  9 + 3 = 12 ✓
assert K_P2.self_intersection() + P2.topological_euler_characteristic() == 12

assert K_P2.h(0) == 0  # h^0(K_{PP^2}) = 0 (anti-ample)
assert P2.picard_group().rank() == 1

# Hodge diamond:
#   p\q  0  1  2
#    0  [1  0  0]
#    1  [0  1  0]
#    2  [0  0  1]
assert P2.hodge_diamond() == Matrix(ZZ, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
assert [P2.plurigenus(n) for n in range(5)] == [1, 0, 0, 0, 0]
assert P2.hilbert_polynomial(t) == (t + 1) * (t + 2) / 2

# Riemann-Roch on PP^2: chi(O_{PP^2}(d)) = (d+1)(d+2)/2
for d in range(0, 5):
    assert (d * H2).hirzebruch_riemann_roch() == (d + 1) * (d + 2) // 2


# --- PP^3 -------------------------------------------------------------------

P3 = PP ^ 3(CC)
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
assert P3.hodge_diamond() == Matrix(ZZ, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
assert P3.picard_group().rank() == 1
