# ============================================================================
# FIXTURE: DEL PEZZO AND FANO SURFACES
#
# A del Pezzo surface is a smooth projective surface with ample anticanonical
# class -K.  Its degree is d = (-K)^2 = K^2.
#
# A weak del Pezzo surface has -K nef and big ((-K)^2 > 0) but possibly not
# ample; it may carry (-2)-curves on which -K has degree 0.
#
# Every smooth del Pezzo surface is one of:
#   PP^2                     degree 9
#   PP^1 x PP^1              degree 8  (the other dP8)
#   Bl_n PP^2  (n=1..8)      degree 9-n  (points in general position)
#
# Fano: -K_X is ample.  For smooth surfaces this coincides with del Pezzo.
# In higher dimensions Fano is the standard term; for surfaces both are used.
#
# is_del_pezzo()      -- -K is ample
# del_pezzo_degree()  -- (-K)^2  (only meaningful when del Pezzo)
# is_fano()           -- -K is ample  (same predicate, Fano vocabulary)
# is_weak_del_pezzo() -- -K is nef and (-K)^2 > 0
#
# References:
#   Demazure, "Surfaces de del Pezzo" in SGA 7
#   Manin, "Cubic Forms" ch. IV
# ============================================================================

P2 = PP^2(CC)
H2 = P2.hyperplane_class()


# ============================================================================
# Section 1: PP^2 — degree-9 del Pezzo
# ============================================================================
# K_{PP^2} = -3H, so -K = 3H is ample and (-K)^2 = 9.

assert P2.is_del_pezzo()
assert P2.del_pezzo_degree() == 9
assert P2.is_fano()
assert P2.is_weak_del_pezzo()   # del Pezzo => weak del Pezzo

# -K coincides with the anticanonical class 3H
K_P2 = P2.canonical_divisor()
assert (-K_P2).is_ample()
assert (-K_P2).self_intersection() == P2.del_pezzo_degree()


# ============================================================================
# Section 2: PP^1 x PP^1 — degree-8 del Pezzo (the other dP8)
# ============================================================================
# K_{PP^1 x PP^1} = -2f1 - 2f2 where f1,f2 are fibre classes;
# (-K)^2 = (2f1+2f2)^2 = 8.  Pic is rank 2, gram [[0,1],[1,0]].

P1xP1 = PP^1(CC) * PP^1(CC)
f1 = P1xP1.fibre_class(0)
f2 = P1xP1.fibre_class(1)

assert P1xP1.is_del_pezzo()
assert P1xP1.del_pezzo_degree() == 8
assert P1xP1.is_fano()
assert P1xP1.is_weak_del_pezzo()

K_P1xP1 = P1xP1.canonical_divisor()
assert (-K_P1xP1).is_ample()
assert (-K_P1xP1).self_intersection() == 8
assert K_P1xP1 == -2 * f1 - 2 * f2


# ============================================================================
# Section 3: Bl_n PP^2 (general position) — del Pezzo of degree 9-n, n=1..8
# ============================================================================
# In general position:  -K = 3Hp - E_1 - ... - E_n is ample iff n <= 8.
# At n = 9 the degree drops to 0 and -K is no longer big, hence not ample.
#
# "General position" here means:
#   * no 3 of the n points are collinear
#   * no 6 lie on a conic
#   * no 8 lie on a cubic with one of them being a double point
# The Weil group W(E_n) acts on Pic for n=3..8.

blowup_points_general = {
    1: [[0, 0, 1]],
    2: [[1, 0, 0], [0, 1, 0]],
    3: [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    4: [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]],
    5: [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1], [1, 2, 3]],
    6: [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1]],
    7: [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1],
        [1, 2, 3]],
    8: [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1],
        [1, 2, 3], [2, 3, 5]],
}

for n in range(1, 9):
    pts   = [P2.point(p) for p in blowup_points_general[n]]
    pi_n  = P2.blowup(pts)
    Sn    = pi_n.domain()
    K_n   = Sn.canonical_divisor()
    mK_n  = -K_n

    assert Sn.is_del_pezzo(),        f"Bl_{n} PP^2 should be del Pezzo"
    assert Sn.del_pezzo_degree() == 9 - n, \
        f"Bl_{n} PP^2: expected degree {9-n}, got {Sn.del_pezzo_degree()}"
    assert Sn.is_fano(),             f"Bl_{n} PP^2 should be Fano"
    assert Sn.is_weak_del_pezzo(),   f"Bl_{n} PP^2 should be weak del Pezzo"

    # Sanity: predicates agree with divisor-level assertions
    assert mK_n.is_ample()
    assert mK_n.is_nef()
    assert mK_n.is_big()
    assert mK_n.self_intersection() == 9 - n
    assert mK_n.self_intersection() == Sn.del_pezzo_degree()

    # Anticanonical linear system embeds Sn in PP^{9-n} for n <= 6
    # (for n=7,8 the embedding is a bit different but -K still ample)
    if n <= 6:
        phi = Sn.anticanonical_map()
        assert phi.is_birational_onto_image()
        assert phi.target().dimension() == 9 - n - 1  # PP^{d-1} in PP^{d}

    # Degree-1 del Pezzo: base locus of |-K| is a single point
    if n == 8:
        assert mK_n.h(0) == 1    # dim |-K| = 0  (single section up to scalar)

# del Pezzo for n=3..8 carries a root system in K_perp <= Pic:
root_systems = {3: 'A1xA2', 4: 'A4', 5: 'D5', 6: 'E6', 7: 'E7', 8: 'E8'}
for n, rsys in root_systems.items():
    pts  = [P2.point(p) for p in blowup_points_general[n]]
    pi_n = P2.blowup(pts)
    Sn   = pi_n.domain()
    # The (-2)-curve-free lattice K_{n}^perp in Pic is the root lattice E_{n-2}
    assert Sn.picard_group().as_lattice().root_system() == RootSystem(rsys)


# ============================================================================
# Section 4: Bl_9 PP^2 — NOT del Pezzo, NOT weak del Pezzo
# ============================================================================
# After blowing up 9 general points: (-K)^2 = 0, so -K cannot be big.
# Neither del Pezzo nor weak del Pezzo.

pts9  = [P2.point([Integer(i), Integer((i*i + 1) % 11), 1]) for i in range(9)]
pi9   = P2.blowup(pts9)
S9    = pi9.domain()
K_9   = S9.canonical_divisor()

assert not S9.is_del_pezzo()
assert not S9.is_fano()
assert not S9.is_weak_del_pezzo()
assert (-K_9).self_intersection() == 0    # degree 0: -K not big
assert not (-K_9).is_ample()
assert not (-K_9).is_big()


# ============================================================================
# Section 5: Weak del Pezzo — Bl_2 with collinear points
# ============================================================================
# If two of the n points are collinear with a third base point, the proper
# transform of the line through them becomes a (-2)-curve L with -K·L = 0.
# This makes -K nef but not ample: is_weak_del_pezzo() but not is_del_pezzo().
#
# Concretely: blow up [1:0:0] and [0:1:0] in PP^2, then the line z=0 has
# proper transform with (-K)·transform = 0.  Here we simulate this by using
# a non-general-position blowup where a (-2)-curve arises.

p_A = P2.point([1, 0, 0])
p_B = P2.point([0, 1, 0])
pi_w = P2.blowup([p_A, p_B])
Sw   = pi_w.domain()
assert Sw.del_pezzo_degree() == 7

# Sw is WEAK del Pezzo of degree 7 because the proper transform of the
# line through p_A and p_B is a (-2)-curve (if the two points are in special
# relative position imposing a (-2)-curve in the intersection configuration).
# In this particular standard blowup the (-2)-curve situation is:
#   proper transform of z=0 line: self-intersection = 1 - 2 = -1  (generic case)
# To get a genuine weak-but-not-del Pezzo we need an explicit (-2)-curve.
# We construct it via a second blowup at an infinitely near point:

pi_near = P2.blowup_infinitely_near(p_A, tangent_direction=[1, 0])
S_wdP   = pi_near.domain()
K_w     = S_wdP.canonical_divisor()

assert S_wdP.is_weak_del_pezzo()
assert not S_wdP.is_del_pezzo()
assert not S_wdP.is_fano()

mK_w = -K_w
assert mK_w.is_nef()
assert mK_w.is_big()
assert not mK_w.is_ample()    # vanishes on the (-2)-curve

# The (-2)-curve: self-intersection -2, intersection with -K equals 0
neg2 = S_wdP.minus_two_curves()
assert all(C.self_intersection() == -2 for C in neg2)
assert all(mK_w.intersection_number(C) == 0 for C in neg2)


# ============================================================================
# Section 6: Non-del Pezzo surfaces for contrast
# ============================================================================

R4.<x,y,z,w> = PolynomialRing(CC, 4)
P3 = PP^3(CC)

# K3 quartic surface: Kodaira dimension 0, K ~ 0, not del Pezzo
S4 = Variety(x^4 + y^4 + z^4 + w^4)    # smooth quartic in PP^3
assert not S4.is_del_pezzo()
assert not S4.is_fano()
assert not S4.is_weak_del_pezzo()
assert S4.canonical_divisor().is_linearly_equivalent_to(Variety.empty().divisor())  # K ~ 0

# Enriques surface: K^2 = 0, 2K ~ 0
Y = EnriquesSurface(...)
assert not Y.is_del_pezzo()
assert not Y.is_fano()
assert not Y.is_weak_del_pezzo()

# Quintic (general type): K ample, not del Pezzo
S5 = Variety(x^5 + y^5 + z^5 + w^5)
assert not S5.is_del_pezzo()
assert not S5.is_fano()
assert not S5.is_weak_del_pezzo()
assert S5.canonical_divisor().is_ample()  # K ample for general type
