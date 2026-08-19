# ============================================================================
# FIXTURE: K3 SURFACES — COMPLETE INTERSECTIONS
#
# A smooth complete intersection of type (d_1,...,d_r) in PP^{r+2} is K3 iff
#   sum(d_i) = r + 3  (adjunction: K = (sum d_i - (r+3)) H = 0)
# The complete K3 CI list:
#   (4)     in PP^3   (quartic hypersurface)
#   (2, 3)  in PP^4   (quadric ∩ cubic)
#   (2,2,2) in PP^5   (three quadrics)
# All have: K = 0, p_g = 1, q = 0, chi(O) = 2, chi_top = 24, h^{1,1} = 20.
# ============================================================================


# --- (2,3) complete intersection K3 in PP^4 ---------------------------------
# Adjunction: K = (2+3-5)H = 0.  Degree = 2*3 = 6.

R5.<u0,u1,u2,u3,u4> = PolynomialRing(CC, 5)

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

# Riemann-Roch on K3: chi(nH) = 2 + (nH)^2/2 = 2 + n^2*6/2 = 2 + 3n^2
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

# Riemann-Roch: chi(nH) = 2 + n^2*8/2 = 2 + 4n^2
for n in range(0, 5):
    assert (n * H_K3_222).hirzebruch_riemann_roch() == 2 + 4 * n^2


# --- K3 Picard group (rank 1 base case) --------------------------------------
# A "general" (Picard-number-1) K3 with polarisation H: Pic = ZZ*H,
# with H^2 = 2g-2 for genus g >= 2.  The simplest case: H^2 = 2 (g=2).
# h^0(H) = g = 2 by Riemann-Roch on K3: chi(H) = 2 + H^2/2 = 2 + 1 = 3;
# by Kodaira vanishing h^2(H) = h^0(K-H) = h^0(-H) = 0 and h^1(H) = 0,
# so h^0(H) = 3 for a (2,0)-polarised K3.

# For the quartic K3 S4 (above): H^2 = 4, Pic >= rank 1.
# The hyperplane class satisfies H^2 = 4; by R-R chi(nH) = 2 + 2n^2 as verified.
