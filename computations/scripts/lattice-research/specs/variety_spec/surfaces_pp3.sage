# ============================================================================
# FIXTURE: SMOOTH SURFACES IN PP^3
#
# For a smooth degree-d surface S in PP^3 (adjunction):
#   K_S   = (d - 4) H|_S
#   K_S^2 = (d-4)^2 * d   (since H|_S^2 = d)
#   chi_top(S) = d(d^2 - 4d + 6)
#   q = h^{1,0} = 0   (Lefschetz: smooth hypersurface in PP^3 simply connected)
#   p_g = h^{2,0}:  0 for d<4, 1 for d=4, C(d-1,3) for d>=5
#   chi(O_S) = 1 + p_g
#   h^{1,1} = chi_top - 2 - 2*p_g   (Hodge decomposition of H^2)
#   Noether: K_S^2 + chi_top = 12*chi(O_S)
# ============================================================================

t = polygen(QQ, 't')

R4.<x,y,z,w> = PolynomialRing(CC, 4)
P3 = PP^3(CC)
H3 = P3.hyperplane_class()


# --- Degree 2: Smooth Quadric Surface ----------------------------------------
# Q ≅ PP^1 × PP^1 (smooth quadric surface is rational)
# K_Q = -2H, K^2 = 8, chi_top = 4, p_g = 0, chi(O) = 1
# Noether: K^2 + chi_top = 12*chi(O)  =>  8 + 4 = 12 ✓
# Hodge diamond (h^{1,1} = 4 - 2 - 0 = 2):
#   p\q  0  1  2
#    0  [1  0  0]
#    1  [0  2  0]
#    2  [0  0  1]
# Picard group: two rulings l, m with l^2 = m^2 = 0, l*m = 1.
# Gram matrix in (l, m) basis: [[0, 1], [1, 0]]  (hyperbolic lattice H)

Q = Variety(x^2 + y^2 + z^2 + w^2)
H_Q = Q.hyperplane_class()
Q_div = Q.as_divisor()

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
assert Q_div.is_linearly_equivalent_to(2 * H3)
assert K_Q == (P3.canonical_divisor() + Q_div).restrict_to(Q)
assert K_Q == -2 * H_Q
assert K_Q.self_intersection() == 8    # (d-4)^2 * d = 4*2
assert K_Q.is_anti_ample() and (-K_Q).is_ample()
assert K_Q in Q.picard_group() and H_Q in Q.picard_group()
assert K_Q.is_linearly_equivalent_to((-2) * H_Q)

assert K_Q.h(0) == 0 and K_Q.h(1) == 0
assert H_Q.is_ample() and H_Q.is_nef() and H_Q.is_big()

# Noether: 8 + 4 = 12 ✓
assert K_Q.self_intersection() + Q.topological_euler_characteristic() == 12

assert Q.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,2,0],[0,0,1]])
assert [Q.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]

# Picard group: two rulings l, m; gram matrix [[0,1],[1,0]] (hyperbolic plane H)
Pic_Q = Q.picard_group().as_lattice()
assert Pic_Q.rank() == 2
assert Pic_Q.gram_matrix() == Matrix(ZZ, [[0, 1], [1, 0]])

assert (-Q.canonical_divisor()).is_ample()
assert Q.canonical_divisor().is_anti_ample()

# Riemann-Roch: chi(O_Q(nH)) = (n+1)^2
for n in range(0, 5):
    assert (n * H_Q).hirzebruch_riemann_roch() == (n + 1)^2


# --- Degree 3: Smooth Cubic Surface (del Pezzo dP_3) -------------------------
# Isomorphic to Bl_6 PP^2; has exactly 27 lines.
# K_S = -H, K^2 = 3, chi_top = 9, p_g = 0, chi(O) = 1
# Hodge diamond (h^{1,1} = 9 - 2 = 7):
#   p\q  0  1  2
#    0  [1  0  0]
#    1  [0  7  0]
#    2  [0  0  1]

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
# By exact sequence 0->O_{PP^3}(-2)->O_{PP^3}(1)->O_{S3}(1)->0:
# h^0(O_{S3}(1)) = h^0(O_{PP^3}(1)) = 4
assert (-K_S3).h(0) == 4

# Noether: 3 + 9 = 12 ✓
assert K_S3.self_intersection() + S3.topological_euler_characteristic() == 12

assert S3.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,7,0],[0,0,1]])
assert [S3.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]

assert (-S3.canonical_divisor()).is_ample()

# Riemann-Roch: chi(O_{S3}(nH)) = 1 + n*(n+1)*3/2 = (3n^2+3n+2)/2
for n in range(0, 5):
    chi_expected = 1 + n * (n + 1) * 3 // 2
    assert (n * H_S3).hirzebruch_riemann_roch() == chi_expected


# --- Degree 4: Fermat Quartic Surface (K3) -----------------------------------
# K_S = 0, K^2 = 0, chi_top = 24, p_g = 1, chi(O) = 2
# Noether: 0 + 24 = 12*2 ✓
# K3 Hodge diamond (h^{1,1} = 24 - 2 - 2 = 20):
#   p\q  0   1  2
#    0  [1   0  1]
#    1  [0  20  0]
#    2  [1   0  1]

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

assert K_S4.h(0) == 1    # h^0(K_{S4}) = p_g = 1
assert K_S4.h(1) == 0    # q = 0
assert H_S4.is_ample() and H_S4.is_nef() and H_S4.is_big()

# Linear system: quartic surface belongs to |4H| in PP^3
assert S4_div in (4 * H3).linear_system()
assert S4_div.is_linearly_equivalent_to(4 * H3)

# Noether: 0 + 24 = 12*2 ✓
assert K_S4.self_intersection() + S4.topological_euler_characteristic() == 24

assert S4.hodge_diamond() == Matrix(ZZ, [[1,0,1],[0,20,0],[1,0,1]])
assert [S4.plurigenus(n) for n in range(5)] == [1, 1, 1, 1, 1]

# Riemann-Roch: chi(O_{S4}(nH)) = 2 + 2n^2
for n in range(0, 5):
    assert (n * H_S4).hirzebruch_riemann_roch() == 2 + 2 * n^2


# --- Degree 5: Smooth Quintic Surface (general type) -------------------------
# K_S = H, K^2 = 5, chi_top = 55, p_g = 4, chi(O) = 5
# Hodge diamond (h^{1,1} = 55 - 2 - 8 = 45):
#   p\q  0   1  2
#    0  [1   0  4]
#    1  [0  45  0]
#    2  [4   0  1]

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

assert K_S5.h(0) == 4    # p_g = 4
assert K_S5.h(1) == 0    # q = 0

# Noether: 5 + 55 = 60 = 12*5 ✓
assert K_S5.self_intersection() + S5.topological_euler_characteristic() == 60

assert S5.hodge_diamond() == Matrix(ZZ, [[1,0,4],[0,45,0],[4,0,1]])
# P_1=p_g=4; P_2=chi(2K)=5+5*2*1//2=10; P_3=5+5*3*2//2=20
assert [S5.plurigenus(n) for n in range(4)] == [1, 4, 10, 20]

for n in range(0, 5):
    assert (n * H_S5).hirzebruch_riemann_roch() == 5 + 5 * n * (n - 1) // 2


# --- Noether loop for d = 2..5 (uniform verification) -----------------------

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
