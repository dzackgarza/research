# ============================================================================
# FIXTURE: ENRIQUES SURFACES AND COBLE SURFACE / K3 DOUBLE COVER
#
# Enriques surface Y:
#   K_Y ≠ 0 but 2*K_Y = 0  (torsion canonical class of order 2)
#   p_g = 0, q = 0, chi(O_Y) = 1
#   chi_top = 12, K^2 = 0, kodaira_dimension = 0
#   Hodge diamond h^{1,1} = 10
#   Universal K3 cover: unramified double cover pi: X -> Y
#
# Coble surface S = Bl_{10} PP^2:
#   Constructed from a rational sextic C with 10 nodes (Coble's sextic).
#   K3 double cover via VarietyMorphism.branched_double_cover(branch_divisor).
#   Deck transformation = covering involution; quotient is S.
# ============================================================================

R3.<x,y,z> = PolynomialRing(CC, 3)


# ============================================================================
# 1. ENRIQUES SURFACE
# ============================================================================

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
# P_n = 1 if n even, 0 if odd  (torsion canonical class of order 2)
assert [Y.plurigenus(n) for n in range(5)] == [1, 0, 1, 0, 1]

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
#   p\q  0   1  2
#    0  [1   0  0]
#    1  [0  10  0]
#    2  [0   0  1]
assert Y.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,10,0],[0,0,1]])

# --- Unramified K3 double cover (Enriques involution) -----------------------
# The universal cover is the unramified double cover pi: X -> Y,
# with deck transformation iota = Enriques involution.
# Accessible via Y.k3_cover() or VarietyMorphism.branched_double_cover
# with empty branch divisor.

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
assert X_k3.quotient(iota) == Y                     # method form
assert Y == X_k3 / iota                             # operator form


# ============================================================================
# 2. COBLE SURFACE AND BRANCHED K3 DOUBLE COVER
# ============================================================================

# A rational sextic C ⊂ PP^2 with exactly 10 A1 nodes.
# p_a = (6-1)(6-2)/2 = 10, p_g = p_a - #nodes = 0.

F = (
    137*x^6
    - 79*x^5*y - 61*x^5*z
    - 244*x^4*y^2 - 423*x^4*y*z - 134*x^4*z^2
    - 438*x^3*y^3 - 585*x^3*y^2*z - 128*x^3*y*z^2 + 19*x^3*z^3
    - 279*x^2*y^4 - 606*x^2*y^3*z - 395*x^2*y^2*z^2 - 61*x^2*y*z^3 + 7*x^2*z^4
    - 137*x*y^5 - 386*x*y^4*z - 550*x*y^3*z^2 - 479*x*y^2*z^3 - 212*x*y*z^4 - 34*x*z^5
    + 9*y^6 - 54*y^5*z - 256*y^4*z^2 - 385*y^3*z^3 - 276*y^2*z^4 - 97*y*z^5 - 13*z^6
)

C = Variety(F)
assert C.is_singular()
assert C.ambient_variety() == PP^2(CC)
assert C.degree() == 6

C_sing = C.singular_locus()
assert C_sing.cardinality() == 10
assert all(p.singularity_type() == Singularity("A1") for p in C_sing)

# --- Blowup: Coble surface S = Bl_{10} PP^2 ---------------------------------
f_bl = PP^2(CC).blowup(C_sing)
S = f_bl.domain()                # Coble surface
assert S.is_rational()

# Picard lattice of Bl_{10} PP^2: I_{1,10}
assert S.picard_group().as_lattice().is_isometric_to(Lattice.I(1, 10))

K_S = S.canonical_divisor()
# Coble's defining property: no anti-canonical sections, unique bi-anti-canonical
assert (-K_S).h(0) == 0          # h^0(O_S(-K_S)) = 0
assert (-2 * K_S).h(0) == 1      # h^0(O_S(-2K_S)) = 1

# --- Exceptional divisors ---------------------------------------------------
Eis = f_bl.exceptional_locus()
assert Eis.cardinality() == 10
assert all(Ei.self_intersection() == -1 for Ei in Eis)
assert Variety(f_bl(Ei) for Ei in Eis) == C_sing
assert Variety(f_bl.pullback(pi) for pi in C_sing) == Eis

Hp = f_bl.pullback(PP^2(CC).hyperplane_class())
assert K_S == -3 * Hp + sum(Ei.as_divisor() for Ei in Eis)

# Proper transform of C: class 6H - 2*(E_1 + ... + E_{10}) = -2*K_S
C_tilde = f_bl.proper_transform(C)
assert C_tilde.as_divisor() == 6 * Hp - 2 * sum(Ei.as_divisor() for Ei in Eis)
assert C_tilde.as_divisor() == -2 * K_S    # Coble's defining relation

# --- K3 double cover via VarietyMorphism.branched_double_cover --------------
# Branch divisor B = proper transform C_tilde, which lies in |-2K_S|.
B = C_tilde
assert B in (-2 * K_S).linear_system()
assert B.is_linearly_equivalent_to(-2 * K_S)

# Construct double cover of S branched over B.
f_k3_coble = VarietyMorphism.branched_double_cover(B)
X_coble    = f_k3_coble.domain()             # K3 surface
assert X_coble.is_k3() and f_k3_coble.codomain() == S

# K3 Hodge diamond
assert X_coble.hodge_diamond() == Matrix(ZZ, [[1, 0, 1], [0, 20, 0], [1, 0, 1]])

# Covering involution via deck_transformation()
iota_X = f_k3_coble.deck_transformation()
assert iota_X in X_coble.Aut()
assert iota_X.order() == 2

# Quotient: both notations for X / iota_X ≅ S
assert X_coble.quotient(iota_X) == S         # method form
assert S == X_coble / iota_X                 # operator form

# Branch and ramification
assert f_k3_coble.branch_divisor() == B
R_X = f_k3_coble.ramification_divisor()
assert R_X in X_coble.picard_group()         # Ramification is a Cartier divisor on X_coble
