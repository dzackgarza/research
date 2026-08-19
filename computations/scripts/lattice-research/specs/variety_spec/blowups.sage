# ============================================================================
# FIXTURE: BLOWUPS OF PP^2 AND DEL PEZZO SURFACES
#
# For pi: Bl_k PP^2 -> PP^2 at k smooth points p_1,...,p_k:
#   Pic(Bl_k PP^2) = ZZ*Hp + ZZ*E_1 + ... + ZZ*E_k
#   Gram matrix: diag(1, -1, ..., -1)  (the lattice I_{1,k})
#   K_{Bl_k PP^2} = -3*Hp + E_1 + ... + E_k
#   K^2 = 9 - k,  chi_top = 3 + k,  p_g = q = 0,  chi(O) = 1
# ============================================================================

P2 = PP^2(CC)
H2 = P2.hyperplane_class()


# --- Blowup at one point: Bl_1 PP^2  (del Pezzo dP_8) ----------------------
# Pic(Bl_1 PP^2): Gram matrix diag(1, -1) in basis (Hp1, E1)
# K = -3*Hp + E,  K^2 = 8
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

# E1 and Hp1 generate Pic; gram matrix diag(1,-1)
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

# -K = 3Hp - E is ample on Bl_1 PP^2 (del Pezzo of degree 8)
assert (-K_dP8).is_ample() and (-K_dP8).is_nef() and (-K_dP8).is_big()

# E is not nef: E^2 = -1 < 0
assert not E1.as_divisor().is_nef()

# Noether: 8 + 4 = 12 ✓
assert K_dP8.self_intersection() + S_dP8.topological_euler_characteristic() == 12
assert S_dP8.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,2,0],[0,0,1]])
assert [S_dP8.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]

# Riemann-Roch spot checks
# D = Hp: D^2 = 1, D*K = -3; D*(D-K)/2 = (1+3)/2 = 2; chi = 1 + 2 = 3
assert Hp1.hirzebruch_riemann_roch() == 3
# D = -K = 3Hp-E: D^2 = 8, D*K = -8; chi = 1 + (8+8)/2 = 9
assert (-K_dP8).hirzebruch_riemann_roch() == 9
# D = E: D^2 = -1, D*K = -1; D*(D-K)/2 = 0; chi = 1
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

for k in range(1, 9):
    pts_k = [P2.point([Integer(i), Integer(i^2 % 7), 1]) for i in range(k)]
    pi_k  = P2.blowup(pts_k)
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

    Hp_k = pi_k.pullback(P2.hyperplane_class())
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
# EXPLICIT BLOWUP EQUATIONS
# ============================================================================
# The blowup of AA^2 at the origin is the subvariety of AA^2 × PP^1 defined by
# the equation  x*v = y*u  in coordinates (x,y) × [u:v].
# In the chart v=1: the blowup in chart is {(x, y, u) : x = y*u} → AA^2.
# In the chart u=1: {(x, y, v) : x*v = y} → AA^2.
#
# For the affine blowup: Spec CC[x,y,u]/(xu-y) — the chart v=1.

# Blowup of AA^2 at origin:  cover by two affine charts
Bl_AA2 = AA^2(CC).blowup(AA^2(CC).origin())

assert Bl_AA2.domain().is_smooth()
assert Bl_AA2.domain().dimension() == 2

# The blowup has exactly one exceptional divisor E ≅ PP^1 with E^2 = -1
E_orig = Bl_AA2.exceptional_divisor()
assert E_orig.is_isomorphic_to(PP^1(CC))
assert E_orig.self_intersection() == -1
assert E_orig.dimension() == 1

# Affine chart equations: in chart v=1, the blowup locus is x = y*u
Ra.<x_b, y_b, u_b> = PolynomialRing(CC, 3)
chart1_eqn = x_b - y_b * u_b
chart1 = Bl_AA2.affine_chart(index=0)
assert chart1.defining_ideal() == Ra.ideal(chart1_eqn)

# In chart u=1: x*v = y, blowup locus x*v - y = 0
Rb.<x_b2, y_b2, v_b> = PolynomialRing(CC, 3)
chart2_eqn = x_b2 * v_b - y_b2
chart2 = Bl_AA2.affine_chart(index=1)
assert chart2.defining_ideal() == Rb.ideal(chart2_eqn)

# The charts glue: in the overlap, u_b = 1/v_b and x_b = x_b2, y_b = y_b2
assert Bl_AA2.domain().is_covered_by([chart1, chart2])

# Blowup of the node of V(y^2 - x^3 + x^2):
# In chart v=1: substitute x = t*u, y = t; equation becomes t^2 - t^3*u^3 + t^2*u^2 = 0.
# Factor out t^2: 1 - t*u^3 + u^2 = 0.  Strict transform: 1 + u^2 - t*u^3 = 0.

C_node2 = Variety(y2^2 - x2^3 + x2^2)    # node at (0,0), smooth for x≠0
p_node2  = C_node2((0, 0))
assert p_node2.is_node()

bl_node  = C_node2.blowup(p_node2)
C_strict = bl_node.strict_transform()
assert C_strict.is_smooth()
assert C_strict.is_irreducible()

# The strict transform meets E in exactly 2 points (two branches of the node)
E_bl = bl_node.exceptional_divisor()
intersection_pts = C_strict.intersection_with(E_bl)
assert intersection_pts.cardinality() == 2
assert all(pt.is_smooth_on(C_strict) for pt in intersection_pts)

# Blowup of V(y^2 - x^3) (cusp) at the cusp:
# First blowup: chart v=1, t ↦ (t*u, t); equation t^2 - t^3*u^3 = t^2*(1-t*u^3).
# Strict transform: 1 - t*u^3 = 0.  Still singular? Check at t=u=0: not on curve.
# The strict transform after first blowup is smooth: the cusp is resolved in one step.
# (Actually A_2 = cusp needs 2 blowups; first blowup gives an A_1 singularity on strict transform.)

bl_cusp1 = cuspidal_cubic.blowup(p_cusp)
C_strict1 = bl_cusp1.strict_transform()
# First blowup: strict transform still singular (one remaining node)
assert not C_strict1.is_smooth()
assert C_strict1.singular_locus().cardinality() == 1
p_cusp2 = C_strict1.singular_locus().points()[0]
assert p_cusp2.is_node()   # after first blowup: A_2 → A_1

# Second blowup: now the strict transform is smooth
bl_cusp2 = C_strict1.blowup(p_cusp2)
C_strict2 = bl_cusp2.strict_transform()
assert C_strict2.is_smooth()

# Minimal resolution requires exactly 2 blowups for A_2 (cusp)
res_cusp = cuspidal_cubic.resolution()
assert res_cusp.number_of_blowups() == 2
