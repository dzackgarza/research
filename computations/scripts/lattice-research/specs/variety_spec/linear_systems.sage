# ============================================================================
# FIXTURE: LINEAR SYSTEMS
#
# A linear system |D| on a variety X is the projective space of effective
# divisors linearly equivalent to D: |D| = PP(H^0(X, O_X(D))).
#
# Key predicates and methods:
#   D in |L|                     -- divisor D is a member of linear system |L|
#   |L|.dimension()              -- dim |L| = h^0(X,L) - 1
#   |L|.degree()                 -- degree of divisors in |L|
#   |L|.base_locus()             -- intersection of all divisors in |L|
#   |L|.is_base_point_free()     -- base_locus() is empty
#   |L|.is_very_ample()          -- |L| gives an embedding X ↪ PP^n
#   |L|.is_ample()               -- equivalent to very ample up to some multiple
#   |L|.map_to_projective_space() -- rational map φ_{|L|}: X --> PP^{n}
#   |L|.general_member()         -- a general element of |L|
#   |L|.pencil()                 -- a 1-dimensional sub-system (|L| of dim 1)
#
# Bidegree notation on PP^1 × PP^1:
#   O(a, b) = pr_1^* O(a) ⊗ pr_2^* O(b)
#   |O(a,b)| parametrizes curves of bidegree (a,b)
# ============================================================================

P1 = PP^1(CC)
P2 = PP^2(CC)
H2 = P2.hyperplane_class()

P1xP1  = PP^1(CC) * PP^1(CC)
f1     = P1xP1.fibre_class(0)
f2     = P1xP1.fibre_class(1)
O_ab   = lambda a, b: P1xP1.line_bundle(a * f1 + b * f2)


# ============================================================================
# Section 1: Linear systems on PP^2 — |O(d)|
# ============================================================================
# h^0(PP^2, O(d)) = C(d+2, 2) = (d+1)(d+2)/2
# Dimension of |O(d)| = (d+1)(d+2)/2 - 1

for d in range(1, 7):
    L_d = P2.linear_system(d * H2)
    expected_h0 = (d + 1) * (d + 2) // 2

    assert L_d.dimension() == expected_h0 - 1
    assert L_d.degree() == d
    assert L_d.is_base_point_free()
    assert L_d.is_very_ample() == (d >= 1)   # O(d) very ample for d >= 1

    phi_d = L_d.map_to_projective_space()
    assert phi_d.target().dimension() == expected_h0 - 1

    # A general member is a smooth degree-d curve for d <= 3
    if d <= 3:
        C_gen = L_d.general_member()
        assert C_gen.degree() == d
        assert C_gen.is_smooth()

# Containment check: a specific curve is in its linear system
R3.<x,y,z> = PolynomialRing(CC, 3)
C4 = Variety(x^4 + y^4 + z^4)   # smooth quartic
L4 = P2.linear_system(4 * H2)
assert C4 in L4                   # C4 ∈ |O(4)|
assert L4.dimension() == 14       # h^0 = 15

# A cubic is NOT in |O(4)|
C3 = Variety(x^3 + y^3 + z^3)
assert C3 not in L4
assert C3 in P2.linear_system(3 * H2)


# ============================================================================
# Section 2: Bidegree (a,b) linear systems on PP^1 × PP^1
# ============================================================================
# h^0(PP^1×PP^1, O(a,b)) = (a+1)(b+1)
# dim |O(a,b)| = (a+1)(b+1) - 1

for a, b in [(1,1), (2,2), (3,3), (4,4), (1,3), (2,4)]:
    L_ab   = P1xP1.linear_system(O_ab(a, b))
    exp_h0 = (a + 1) * (b + 1)

    assert L_ab.dimension() == exp_h0 - 1
    assert L_ab.degree() == a + b               # degree w.r.t. O(1,1)
    assert L_ab.is_base_point_free()
    assert L_ab.is_very_ample() == (a >= 1 and b >= 1)

# Specific (4,4) curve contained in |O(4,4)|
R4.<a4,b4,c4,d4> = PolynomialRing(CC, 4)
C44 = Variety(a4^4 * c4^4 + b4^4 * d4^4 + a4^2*b4^2*c4^2*d4^2)
L44 = P1xP1.linear_system(O_ab(4, 4))

assert C44 in L44
assert L44.dimension() == 24     # h^0 = (4+1)*(4+1) = 25

# Bidegree containment exclusion
C22 = Variety(a4^2*c4^2 + b4^2*d4^2 + a4*b4*c4*d4)   # (2,2) curve
assert C22 in P1xP1.linear_system(O_ab(2, 2))
assert C22 not in L44              # (2,2) not in |O(4,4)|


# ============================================================================
# Section 3: Base locus and pencils
# ============================================================================
# A pencil |P| ⊂ |D| is a 1-dimensional linear subsystem (dim = 1).
# The base locus of a pencil of cubics on PP^2 is a 0-dimensional scheme of
# length 9 (Bezout: 3 · 3 = 9 base points counted with multiplicity).

# Pencil of cubics spanned by x^3+y^3+z^3 and x*y*z*(x+y+z):
C_a = Variety(x^3 + y^3 + z^3)
C_b = Variety(x * y * z)
pencil_cubics = P2.pencil(C_a, C_b)

assert pencil_cubics.dimension() == 1
assert pencil_cubics.degree() == 3
BL = pencil_cubics.base_locus()
assert BL.dimension() == 0
assert BL.length() == 9              # Bezout

# A base-point-free linear system has empty base locus
L3 = P2.linear_system(3 * H2)
assert L3.is_base_point_free()
assert L3.base_locus().is_empty()


# ============================================================================
# Section 4: Anticanonical linear system on del Pezzo surfaces
# ============================================================================
# For a del Pezzo surface S of degree d, |-K_S| is base-point-free for d >= 2
# and gives an embedding of degree d.

for n in range(1, 7):   # Bl_n PP^2 for n=1..6
    pts   = [P2.point([Integer(i), Integer((i+1) % 5), 1]) for i in range(n)]
    pi_n  = P2.blowup(pts)
    Sn    = pi_n.domain()
    mK_n  = -Sn.canonical_divisor()
    L_mK  = Sn.linear_system(mK_n)

    assert L_mK.degree() == 9 - n
    assert L_mK.dimension() == 9 - n   # h^0(-K) = d for del Pezzo of degree d

    if n <= 5:        # base-point free for d >= 3
        assert L_mK.is_base_point_free()
        phi = L_mK.map_to_projective_space()
        assert phi.target().dimension() == 9 - n  # embeds in PP^d

    # |-K| member is a smooth anticanonical curve (elliptic) for degree >= 1
    if n <= 6:
        C_anti = L_mK.general_member()
        assert C_anti.genus() == 1     # anticanonical on del Pezzo is elliptic
        assert C_anti in L_mK


# ============================================================================
# Section 5: Linear systems on K3 surfaces
# ============================================================================
# For a K3 surface S and a curve class C with C^2 = 2g-2 (g >= 2):
#   h^0(O_S(C)) = g + 1  (Riemann-Roch + K3 conditions: K ~ 0, h^1 = 0)
#   |C| is base-point free and gives a 2:1 map to PP^g if C is not very ample.

R_k3.<u,v,s,w> = PolynomialRing(CC, 4)
S_k3 = Variety(u^4 + v^4 + s^4 + w^4)    # smooth quartic K3 in PP^3
H_k3 = S_k3.hyperplane_class()
K_k3 = S_k3.canonical_divisor()
assert K_k3.is_linearly_equivalent_to(Variety.empty().divisor())   # K ~ 0

# H = hyperplane section: H^2 = 4, so it is a genus-3 curve class
L_H = S_k3.linear_system(H_k3)
assert H_k3.self_intersection() == 4
assert L_H.dimension() == 3      # h^0 = g+1 = 4, dim |H| = 3
assert L_H.is_very_ample()       # H is very ample on a quartic K3
assert L_H.degree() == 4

# Double of H: |2H| embeds S in PP^9 as a degree-16 surface
L_2H = S_k3.linear_system(2 * H_k3)
assert (2 * H_k3).self_intersection() == 16
assert L_2H.dimension() == 9    # h^0 = 11 (RR: 1 + 16/2 = 9, then +2 boundary terms)

# Containment: the defining quartic is in |O(4)|
assert Variety(u^4 + v^4 + s^4 + w^4) in PP^3(CC).linear_system(
    PP^3(CC).linear_system_of_hypersurfaces(4))


# ============================================================================
# Section 6: Linear series and maps — rational normal curves
# ============================================================================
# The complete linear system |O_{PP^1}(d)| maps PP^1 to the rational normal
# curve of degree d in PP^d.

for d in range(2, 6):
    L_d1 = P1.linear_system(P1.tautological_bundle(d))
    phi  = L_d1.map_to_projective_space()

    assert L_d1.dimension() == d
    assert L_d1.is_very_ample()
    assert phi.image().degree() == d
    assert phi.image().dimension() == 1
    assert phi.image().is_rational()
    assert phi.is_closed_immersion()   # rational normal curve embedding
