# ============================================================================
# SPEC: STABILITY AND MARKED CURVES
#
# Deligne-Mumford (DM69) stability conditions for curves and pointed curves.
# A curve C is:
#   - stable:     ω_C is ample AND Aut(C) is finite
#   - semistable: ω_C is nef AND Aut(C) is reductive
#
# Equivalently (DM69 combinatorial criterion):
#   stable:     every rational component E meets the rest in ≥ 3 points
#   semistable: every rational component E meets the rest in ≥ 2 points
#
# For pointed curves (C; p_1,...,p_n):
#   stable:     every rational component has (nodes + marked points) ≥ 3
#   semistable: every rational component has (nodes + marked points) ≥ 2
#
# GIT stability for plane curves also tested below.
# ============================================================================

P2 = PP^2(CC)
R3.<x_s, y_s, z_s> = PolynomialRing(CC, 3)
R1.<x_a>            = PolynomialRing(CC)


# ============================================================================
# Section 1: Stable curves
# ============================================================================

# A stable curve must have ω_C ample and Aut(C) finite.
# Smooth curves of genus ≥ 2 are stable.
# Smooth curve of genus 2: Fermat quartic restricted to a line meets at 4 pts...
# Use a smooth plane quartic (genus = (4-1)(4-2)/2 = 3).

f_quartic_plane = x_s^4 + y_s^4 + z_s^4
C_g3 = Variety(f_quartic_plane)
assert C_g3.genus() == 3
assert C_g3.is_smooth()
assert C_g3.is_stable()
assert C_g3.canonical_sheaf().is_ample()
assert C_g3.Aut().is_finite()

# A nodal rational curve with at least 3 nodal connections to other components
# is stable if and only if each rational component meets the rest in ≥ 3 points.

# Triangle: three PP^1s meeting pairwise in 3 nodes
f_triangle = x_s * y_s * z_s
C_tri = Variety(f_triangle)
comps_tri = list(C_tri.irreducible_components())
for comp in comps_tri:
    assert comp.genus() == 0   # each component is rational (PP^1)
    # each component meets the other two in exactly 2 nodes
    other_comps = [c for c in comps_tri if c != comp]
    intersection_count = sum(
        comp.intersection_number(other) for other in other_comps
    )
    assert intersection_count == 2
# Triangle: each rational component meets the rest in 2 points → semistable but NOT stable
assert C_tri.is_semistable()
assert not C_tri.is_stable()

# Fan of three rational tails attached to an elliptic component:
# Construct: one elliptic curve E and three PP^1 tails, each meeting E in 1 node.
# Each tail meets only E; the tails meet each other in 0 nodes.
# Rational tails have 1 meeting point → not semistable.
C_fan = VarietyCurve.fan(base_genus=1, num_tails=3, base_field=CC)
comps_fan = list(C_fan.irreducible_components())
rational_comps = [c for c in comps_fan if c.genus() == 0]
for comp in rational_comps:
    # Each rational tail meets the rest in exactly 1 point → not semistable
    other_nodes_count = sum(
        comp.intersection_number(other)
        for other in comps_fan if other != comp
    )
    assert other_nodes_count == 1
assert not C_fan.is_semistable()
assert not C_fan.is_stable()

# A connected nodal curve of arithmetic genus ≥ 2 with a rational component
# meeting the rest in ≥ 3 points IS stable.
# Example: nodal union of a smooth genus-2 curve and a PP^1 meeting it in 3 nodes.
C_mixed = VarietyCurve.from_components(
    components=[("genus2", CC), ("rational", CC)],
    gluings=[(("rational", i), ("genus2", i)) for i in range(3)]
)
rational_comp = C_mixed.component("rational")
genus2_comp   = C_mixed.component("genus2")
assert rational_comp.genus() == 0
assert genus2_comp.genus() == 2
other_count = sum(
    rational_comp.intersection_number(other)
    for other in C_mixed.irreducible_components() if other != rational_comp
)
assert other_count == 3       # meets 3 points → rational component contributes no instability
assert C_mixed.is_stable()
assert C_mixed.canonical_sheaf().is_ample()
assert C_mixed.Aut().is_finite()


# ============================================================================
# Section 2: Semistable curves (Deligne-Mumford, 1969)
# ============================================================================

# A semistable curve: ω_C nef and Aut(C) reductive.
# DM69 criterion: each rational component meets the rest in ≥ 2 points.

# Triangle of PP^1s (Ã_2 cycle): each rational comp meets 2 others in 1 node each
C_tri2 = Variety(x_s * y_s * z_s)
assert C_tri2.is_semistable()
assert not C_tri2.is_stable()
assert C_tri2.canonical_sheaf().is_nef()
assert C_tri2.Aut().is_reductive()   # reductive but infinite (the torus (CC*)^2)

# Banana (Ã_1): two PP^1s meeting in 2 nodes
C_ban2 = VarietyCurve.banana(CC)
assert C_ban2.is_semistable()
assert not C_ban2.is_stable()
assert C_ban2.canonical_sheaf().is_nef()

# A PP^1 meeting a smooth elliptic curve in 2 nodes: semistable (2 intersections)
C_tail2 = VarietyCurve.from_components(
    components=[("genus1", CC), ("rational", CC)],
    gluings=[(("rational", 0), ("genus1", 0)), (("rational", 1), ("genus1", 1))]
)
rat2 = C_tail2.component("rational")
other_count2 = sum(
    rat2.intersection_number(other)
    for other in C_tail2.irreducible_components() if other != rat2
)
assert other_count2 == 2
assert C_tail2.is_semistable()
assert not C_tail2.is_stable()

# A PP^1 meeting a smooth elliptic curve in 1 node: NOT semistable (1 intersection)
C_tail1 = VarietyCurve.from_components(
    components=[("genus1", CC), ("rational", CC)],
    gluings=[(("rational", 0), ("genus1", 0))]
)
rat1 = C_tail1.component("rational")
other_count1 = sum(
    rat1.intersection_number(other)
    for other in C_tail1.irreducible_components() if other != rat1
)
assert other_count1 == 1
assert not C_tail1.is_semistable()


# ============================================================================
# Section 3: Marked (pointed) curves and stability
# ============================================================================
# A pointed curve (C; p_1,...,p_n) is stable when every rational component
# has (number of nodes) + (number of marked points on it) ≥ 3.

# Smooth PP^1 with no marked points: not stable (Aut = PGL(2), infinite)
C_P1 = PP^1(CC)
assert not C_P1.is_stable()
assert C_P1.Aut().dimension() == 3   # PGL(2) is 3-dimensional

# Smooth PP^1 with 1 marked point: (PP^1; p).  Each rational comp has 0 nodes + 1 marked = 1 < 3.
C_P1_1 = PP^1(CC).with_marked_points([PP^1(CC).point([0, 1])])
assert C_P1_1.marked_points().cardinality() == 1
assert not C_P1_1.is_stable()

# Smooth PP^1 with 2 marked points: 0 nodes + 2 marked = 2 < 3 → not stable.
# But Aut that fixes 2 points is (CC*): semistable but not stable.
C_P1_2 = PP^1(CC).with_marked_points([PP^1(CC).point([0,1]), PP^1(CC).point([1,0])])
assert not C_P1_2.is_stable()
assert C_P1_2.is_semistable()   # fixes 2 pts → Aut = CC* (reductive but not finite)

# Smooth PP^1 with 3 marked points: 0 nodes + 3 marked = 3 ≥ 3 → stable!
pts_3 = [PP^1(CC).point([0,1]), PP^1(CC).point([1,0]), PP^1(CC).point([1,1])]
C_P1_3 = PP^1(CC).with_marked_points(pts_3)
assert C_P1_3.marked_points().cardinality() == 3
assert C_P1_3.is_stable()
assert C_P1_3.Aut().is_finite()   # Aut = trivial (PGL(2) has no nonidentity element fixing 3 distinct points)

# Smooth genus-1 curve (elliptic curve) with no marked points: semistable but not stable
# (Aut(E) contains the translation subgroup — reductive but infinite).
# With 1 marked point: Aut(E, p) = {n-torsion points that fix p as a group} — finite.
E = PP^2(CC).elliptic_curve_from_weierstrass(a=0, b=-1)  # y^2 = x^3 - 1
assert E.genus() == 1
assert not E.is_stable()    # Aut(E) is infinite (translations)
assert E.is_semistable()    # ω_E is trivial (nef), and Aut is reductive (abelian)

p_origin = E.origin()    # the identity element / flex point
E_ptd = E.with_marked_points([p_origin])
assert E_ptd.is_stable()
assert E_ptd.Aut().is_finite()

# Elliptic curves naturally have one distinguished marked point (the origin)
assert E.canonical_marked_point() == p_origin
E_auto_ptd = E.as_pointed_curve()
assert E_auto_ptd.marked_points().cardinality() == 1
assert E_auto_ptd.is_stable()


# ============================================================================
# Section 4: Hilbert polynomial of a stable curve
# ============================================================================
# For a stable curve (C; ω_C^n) embedded by ω_C^{\otimes 3}:
#   Hilbert polynomial: P(m) = (6m-1)(g-1)   (for g ≥ 2)
#   by Riemann-Roch on C.

# Smooth plane quartic (genus 3):
t_hilb = polygen(QQ, 't')
C_g3_hilb = Variety(x_s^4 + y_s^4 + z_s^4)
assert C_g3_hilb.genus() == 3
assert C_g3_hilb.hilbert_polynomial(t_hilb) == (6*t_hilb - 1) * (3 - 1)  # 2*(6t-1)

# Smooth curve of genus 2: hyperelliptic y^2 = x^6 + 1 (not a plane curve)
# Use abstract curve via genus-2 hyperelliptic model
C_g2 = HyperellipticCurve(x_a^6 + 1)
assert C_g2.genus() == 2
assert C_g2.is_stable()
assert C_g2.hilbert_polynomial(t_hilb) == (6*t_hilb - 1) * (2 - 1)  # 6t - 1
