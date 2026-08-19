# ============================================================================
# FIXTURE: RIEMANN-HURWITZ FORMULA FOR BRANCHED COVERS
#
# For a finite morphism f: X → Y of smooth projective varieties of dimension n
# there is a ramification divisor R_f satisfying K_X = f^* K_Y + R_f.
#
# CURVES (dimension 1)
# For f: C → D of degree d:
#
#   χ(C) = d · χ(D) − deg R_f
#   2g(C) − 2 = d(2g(D) − 2) + deg R_f
#   deg R_f = Σ_p (e_p − 1)  (sum over all p ∈ C, e_p = ramification index)
#
# For a simple branch point (e_p = 2 at a single point over q ∈ D):
#   that point contributes 1 to deg R_f.
# A totally ramified point above q (e_p = d): contributes d−1.
#
# SURFACES (dimension 2)
# For f: S → T a double cover branched over smooth B ⊂ T:
#   R_f = f^* B / 2  (Weil divisor, the preimage at multiplicity 1)
#   K_S = f^* K_T + f^* (B/2)
#   χ_top(S) = 2 · χ_top(T) − χ_top(B)
#   χ(O_S) = 2 · χ(O_T) + (1/2) · (K_T · B + B^2) / 2    [from HRR]
#
# Topological formula for étale d-cover:
#   χ_top(C) = d · χ_top(D)   (no ramification)
# ============================================================================

P1 = PP^1(CC)
P2 = PP^2(CC)
P3 = PP^3(CC)


# ============================================================================
# Section 1: Power maps PP^1 → PP^1 of degree d
# ============================================================================
# z ↦ z^d: totally ramified at 0 and ∞ (e = d at each).
# deg R = 2(d − 1).  Both source and target PP^1 have g = 0.
# RH: 2(0)−2 = d(2·0−2) + 2(d−1) → −2 = −2d + 2d − 2 = −2 ✓

for d in range(2, 8):
    f = CurveMap.power_map(PP^1(CC), d)   # [s:t] ↦ [s^d : t^d]

    assert f.is_finite() and f.degree() == d
    assert f.domain().genus() == 0
    assert f.codomain().genus() == 0

    R_f = f.ramification_divisor()
    assert R_f.degree() == 2 * (d - 1)

    # Branch locus: {0, ∞} ⊂ PP^1, each with a single preimage of index d
    B_f = f.branch_locus()
    assert B_f.cardinality() == 2
    preimages = [f.fiber(q) for q in B_f]
    assert all(pt.ramification_index() == d for fiber in preimages for pt in fiber)

    # Riemann-Hurwitz identity as method
    assert f.riemann_hurwitz_degree() == 2 * (d - 1)

    # genus formula
    g_C = f.domain().genus()
    g_D = f.codomain().genus()
    assert 2 * g_C - 2 == d * (2 * g_D - 2) + R_f.degree()


# ============================================================================
# Section 2: Hyperelliptic covers y^2 = f_2g+2(x), genus g → PP^1
# ============================================================================
# y^2 = f(x) of degree 2g+2: double cover of PP^1 branched at 2g+2 points,
# each simple (e_p = 2, so e_p − 1 = 1).
# RH: 2g−2 = 2(−2) + (2g+2) → 2g−2 = 2g−2 ✓

R1.<x> = PolynomialRing(CC, 1)

for g in range(1, 6):
    # Hyperelliptic curve of genus g over PP^1 via 2g+2 branch points
    branch_pts = [CC(i) for i in range(2 * g + 2)]
    C_hyp = HyperellipticCurve.from_branch_points(branch_pts)
    f_hyp = C_hyp.hyperelliptic_map()    # the degree-2 projection C → PP^1

    assert f_hyp.degree() == 2
    assert C_hyp.genus() == g
    assert f_hyp.codomain().genus() == 0

    R_f = f_hyp.ramification_divisor()
    assert R_f.degree() == 2 * g + 2

    B_f = f_hyp.branch_locus()
    assert B_f.cardinality() == 2 * g + 2
    assert all(q.ramification_index() == 2
               for q in f_hyp.ramified_points())

    # RH identity
    assert 2 * g - 2 == 2 * (2 * 0 - 2) + R_f.degree()
    assert f_hyp.riemann_hurwitz_degree() == 2 * g + 2


# ============================================================================
# Section 3: Cyclic Kummer covers z^n = f(x), C → PP^1
# ============================================================================
# Totally ramified Z/nZ-cover of PP^1 at r points:
# each contributes e_p − 1 = n − 1, so deg R = r(n − 1).
# RH:  2g(C) − 2 = n(−2) + r(n−1)
#      g(C) = 1 + (n/2)(r − 2) − r/2  (Kummer genus formula)
#
# Simple case: z^n = x(x-1)…(x-(r-1)), r points fully ramified, n | ?

for n in [2, 3, 4]:
    for r in [2, 4, 6]:
        branch_pts = [CC(i) for i in range(r)]
        f_kum = KummerCover.cyclic(P1, n, branch_pts)

        assert f_kum.degree() == n
        assert f_kum.codomain().genus() == 0

        R_f = f_kum.ramification_divisor()
        assert R_f.degree() == r * (n - 1)

        g_C = f_kum.domain().genus()
        assert 2 * g_C - 2 == n * (2 * 0 - 2) + r * (n - 1)

        # Kummer genus formula
        g_expected = 1 + n * (r - 2) // 2 - r // 2
        assert g_C == g_expected


# ============================================================================
# Section 4: Étale covers — no ramification
# ============================================================================
# Unramified degree-d cover f: C → D:
#   g(C) − 1 = d(g(D) − 1)  [since deg R = 0]
#   χ_top(C) = d · χ_top(D)

# Étale double cover of an elliptic curve (g=1) → elliptic curve (g=1):
# 2(1)−2 = 2(2(1)−2) + 0 → 0 = 0 ✓
E = EllipticCurve([0, -1, 0, 0, 1])      # y^2 = x^3 − x, g=1
f_etale = E.etale_double_cover()          # unramified degree-2 cover E' → E

assert f_etale.degree() == 2
assert f_etale.domain().genus() == 1   # source is also elliptic
assert f_etale.ramification_divisor().degree() == 0
assert f_etale.branch_locus().is_empty()
assert f_etale.riemann_hurwitz_degree() == 0

# Étale 3-cover of genus-2 curve → genus-2 curve
# RH: 2(g_C)−2 = 3(2·2−2) + 0 → g_C = 4
C2 = HyperellipticCurve.from_branch_points([CC(i) for i in range(6)])  # g=2
f_3 = C2.etale_cyclic_cover(3)

assert f_3.degree() == 3
assert f_3.domain().genus() == 4
assert f_3.ramification_divisor().degree() == 0
assert 2 * f_3.domain().genus() - 2 == 3 * (2 * 2 - 2) + 0

# General loop: étale d-cover of genus-g_D curve has genus g_C = d(g_D-1)+1
for g_D in [1, 2, 3]:
    for d in [2, 3]:
        C_D = Curve.of_genus(g_D)
        f_d = C_D.etale_cyclic_cover(d)
        g_C = f_d.domain().genus()
        assert g_C == d * (g_D - 1) + 1
        assert f_d.riemann_hurwitz_degree() == 0


# ============================================================================
# Section 5: Hurwitz existence and monodromy
# ============================================================================
# A branched cover f: C → PP^1 of degree d with prescribed ramification
# (partition type over each branch point) exists iff the Hurwitz condition
# holds: the product of local monodromies in S_d is the identity.

# Degree 3 cover PP^1 → PP^1 fully ramified at 3 points (3+3+3 ramification):
# R = 3·(3-1) = 6; RH: 2g-2 = 3(-2)+6 = 0 → g = 1 (elliptic curve!)
f_hurwitz = BranchedCover.from_monodromy(
    target=P1,
    degree=3,
    branch_data={
        P1.point([0, 1]):   Permutation([2, 3, 1]),   # (123)
        P1.point([1, 0]):   Permutation([1, 3, 2]),   # (23)
        P1.point([1, 1]):   Permutation([3, 2, 1]),   # (13)
    }
)
assert f_hurwitz.domain().genus() == 1
R_h = f_hurwitz.ramification_divisor()
assert R_h.degree() == 6
assert 2 * 1 - 2 == 3 * (2 * 0 - 2) + 6


# ============================================================================
# Section 6: Surface double covers (topological Riemann-Hurwitz)
# ============================================================================
# For f: S → T a double cover branched over smooth B ⊂ T:
#   χ_top(S) = 2 · χ_top(T) − χ_top(B)

# 6a. K3 surface as double cover of PP^2 branched over a smooth plane sextic B6.
# χ_top(PP^2) = 3,  B6 smooth plane sextic: g(B6) = 10, χ_top(B6) = 2-2·10 = -18.
# χ_top(S) = 2·3 − (−18) = 6 + 18 = 24 ✓  (K3 has χ_top = 24)

R_P2.<x2,y2,z2> = PolynomialRing(CC, 3)
B6    = Variety(x2^6 + y2^6 + z2^6)               # smooth Fermat sextic
f_k3  = VarietyMorphism.branched_double_cover(B6)
S_k3  = f_k3.domain()

assert S_k3.topological_euler_characteristic() == 24
assert S_k3.is_k3()

chi_T = P2.topological_euler_characteristic()      # 3
chi_B = B6.topological_euler_characteristic()      # 2 - 2*10 = -18
assert chi_B == -18
assert S_k3.topological_euler_characteristic() == 2 * chi_T - chi_B

R_f  = f_k3.ramification_divisor()
assert R_f == f_k3.pullback(B6.as_divisor()) / 2  # R_f = (1/2) f^* B6

# K_S = f^* K_T + R_f
K_S  = S_k3.canonical_divisor()
K_T  = P2.canonical_divisor()
assert K_S.is_linearly_equivalent_to(f_k3.pullback(K_T) + R_f)
assert K_S.is_linearly_equivalent_to(Variety.empty().divisor())   # K3: K ~ 0


# 6b. K3 surface as double cover of PP^1 × PP^1 branched over a smooth (4,4) curve.
# χ_top(PP^1 × PP^1) = 4.  Smooth (4,4) curve: g = 9, χ = 2-2·9 = -16.
# χ_top(S) = 2·4 − (−16) = 8 + 16 = 24 ✓

P1xP1 = PP^1(CC) * PP^1(CC)
f1, f2 = P1xP1.fibre_class(0), P1xP1.fibre_class(1)

R_P1P1.<a,b,c,d> = PolynomialRing(CC, 4)
B44   = Variety((a^4 + b^4) * (c^4 + d^4) + a*b*c*d)  # smooth (4,4) in PP^1×PP^1
f_k3b = VarietyMorphism.branched_double_cover(B44)
S_k3b = f_k3b.domain()

assert S_k3b.topological_euler_characteristic() == 24
assert S_k3b.is_k3()

chi_T2 = P1xP1.topological_euler_characteristic()    # 4
chi_B2 = B44.topological_euler_characteristic()       # -16
assert chi_B2 == -16
assert S_k3b.topological_euler_characteristic() == 2 * chi_T2 - chi_B2


# 6c. Enriques surface: étale Z/2Z cover by K3.
# f: K3 → Enriques, degree 2, unramified.
# χ_top(K3) = 2 · χ_top(Enriques): 24 = 2 · 12 ✓

Y    = EnriquesSurface(...)
f_en = Y.k3_cover()
X    = f_en.domain()

assert f_en.degree() == 2
assert f_en.ramification_divisor().degree() == 0     # étale
assert f_en.branch_locus().is_empty()
assert X.topological_euler_characteristic() == 2 * Y.topological_euler_characteristic()
assert X.topological_euler_characteristic() == 24
assert Y.topological_euler_characteristic() == 12

# K_X = f^* K_Y  (no ramification term)
K_X  = X.canonical_divisor()
K_Y  = Y.canonical_divisor()
assert K_X.is_linearly_equivalent_to(f_en.pullback(K_Y))


# 6d. Double cover of PP^2 branched over a smooth quartic — del Pezzo dP2 → PP^2.
# B4: smooth quartic, g=3, χ_top(B4) = 2-6 = -4.
# χ_top(S) = 2·3 − (−4) = 6 + 4 = 10. (dP2: χ = 3+7 = 10 ✓ since Bl_7 PP^2)
# Actually a double cover of PP^2 branched over a quartic is not del Pezzo;
# let us check it gives a surface with the expected topology.
# K_S^2 = 2(K_{PP^2} + B4/2)^2 = 2(-3H + 2H)^2 = 2H^2 = 2.  This is indeed dP7.

R_P2b.<u,v,w> = PolynomialRing(CC, 3)
B4 = Variety(u^4 + v^4 + w^4)                           # smooth quartic
f_dp2 = VarietyMorphism.branched_double_cover(B4)
S_dp2 = f_dp2.domain()

chi_B4 = B4.topological_euler_characteristic()           # 2 - 2*3 = -4
assert chi_B4 == -4
assert S_dp2.topological_euler_characteristic() == 2 * 3 - (-4)   # 10

K_dp2 = S_dp2.canonical_divisor()
R_dp2 = f_dp2.ramification_divisor()
K_P2  = P2.canonical_divisor()
assert K_dp2.is_linearly_equivalent_to(f_dp2.pullback(K_P2) + R_dp2)


# ============================================================================
# Section 7: Degree formula consistency loop
# ============================================================================
# For any branched cover f: C → D of smooth projective curves, the formula
#   2g(C) − 2 = d(2g(D) − 2) + deg R_f
# can be checked from the ramification data alone.
#
# We check it holds universally for every cover constructed above.

for (f_obj, g_C_expected, g_D_expected, d_expected, deg_R_expected) in [
    # (morphism, g_source, g_target, degree, deg_R)
    (CurveMap.power_map(P1, 3), 0, 0, 3, 4),    # z^3
    (CurveMap.power_map(P1, 5), 0, 0, 5, 8),    # z^5
    (HyperellipticCurve.from_branch_points([CC(i) for i in range(4)]).hyperelliptic_map(),
     1, 0, 2, 4),    # g=1 hyperelliptic
    (HyperellipticCurve.from_branch_points([CC(i) for i in range(8)]).hyperelliptic_map(),
     3, 0, 2, 8),    # g=3 hyperelliptic
]:
    g_C = f_obj.domain().genus()
    g_D = f_obj.codomain().genus()
    d   = f_obj.degree()
    R   = f_obj.ramification_divisor()

    assert g_C == g_C_expected
    assert g_D == g_D_expected
    assert d   == d_expected
    assert R.degree() == deg_R_expected
    assert 2 * g_C - 2 == d * (2 * g_D - 2) + R.degree()
    assert f_obj.riemann_hurwitz_degree() == R.degree()
