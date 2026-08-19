# ============================================================================
# FIXTURE: FAMILY MACHINERY
#
# A family is a flat morphism π: X → S where S is a parameter space, typically
# a smooth curve or a complex disc Δ = Spec CC[[t]] or the affine line AA^1.
#
#   general_fiber   -- π^{-1}(s) for s ∈ S general (s ≠ 0)
#   special_fiber   -- π^{-1}(0)  (also central_fiber; aliases)
#   central_fiber   -- alias for special_fiber
#   specialize()    -- maps objects on the general fiber to the special fiber
#   is_flat()       -- checks flatness of π
#   is_smooth_over_generic_point() -- smooth away from finitely many s ∈ S
#
# Branched cyclic covers z^n - f = 0:
#   The defining equation of a Z/nZ-cover of a hypersurface V(f) ⊂ PP^N is
#   z^n = f(x_0, ..., x_N) in the total space of O(deg f / n).
#   For a double cover: z^2 - f = 0 in the affine chart.
# ============================================================================

AA1 = AA^1(CC)
t   = AA1.coordinate('t')

P2 = PP^2(CC)
P3 = PP^3(CC)


# ============================================================================
# Section 1: Pencil of plane cubics (Legendre family)
# ============================================================================
# y^2 z = x(x - z)(x - t·z) for t ∈ AA^1 \ {0, 1}.
# The total space is a surface with a map to AA^1.
# General fiber: smooth elliptic curve.
# Special fiber (t=0): nodal rational curve  y^2 z = x^2(x-z).
# Special fiber (t=1): cuspidal rational curve  y^2 z = x^3  (up to coord change).

R.<x,y,z,T> = PolynomialRing(CC, 4)
legendre_eq  = y^2 * z - x * (x - z) * (x - T*z)
X_legendre   = Variety(legendre_eq)              # total space in PP^2 × AA^1
pi_legendre  = X_legendre.projection_to(AA1, variable=T)

assert pi_legendre.is_flat()
assert pi_legendre.is_smooth_over_generic_point()

# General fiber (t = 1/2)
F_gen = pi_legendre.general_fiber()
assert F_gen.genus() == 1
assert F_gen.is_smooth()
assert F_gen.is_irreducible()

# Special fiber at t = 0: nodal cubic
F_0 = pi_legendre.special_fiber()              # t = 0
assert F_0 == pi_legendre.central_fiber()      # alias
assert not F_0.is_smooth()
assert F_0.singular_locus().cardinality() == 1
sing_0 = F_0.singular_locus().points()[0]
assert sing_0.is_nodal()
assert not sing_0.is_cuspidal()
assert F_0.geometric_genus() == 0             # nodal: p_a = 1, p_g = 0

# Special fiber at t = 1: cuspidal cubic
F_1 = pi_legendre.fiber_at(AA1.point([1]))
assert not F_1.is_smooth()
cusp_1 = F_1.singular_locus().points()[0]
assert cusp_1.is_cuspidal()
assert not cusp_1.is_nodal()
assert F_1.geometric_genus() == 0

# Specialize: a section of the total space restricts to a point
sigma = pi_legendre.section([0, 1, 0])          # the point [0:1:0] for all t
assert sigma.is_section()
p_spec = pi_legendre.specialize(sigma, t=0)
assert p_spec in F_0


# ============================================================================
# Section 2: Semistable degeneration of K3 surfaces
# ============================================================================
# A one-parameter family of K3 surfaces degenerating to a singular central fiber.
# π: X → Δ,  Δ = Spec CC[[t]].  General fiber: smooth K3.  Special fiber: union
# of two rational surfaces glued along an elliptic curve (Type II degeneration)
# or a chain of rational surfaces (Type III degeneration).

# Type II: quartic K3 degenerating to two quadrics glued along an elliptic curve
R4.<a,b,c,d,T2> = PolynomialRing(CC, 5)
quartic_family = a^4 + b^4 + c^4 + d^4 + T2 * (a^2*b^2 + c^2*d^2)
X_k3_fam = Variety(quartic_family)             # family in PP^3 × AA^1
pi_k3    = X_k3_fam.projection_to(AA1, variable=T2)

assert pi_k3.is_flat()

F_k3_gen = pi_k3.general_fiber()
assert F_k3_gen.is_k3()
assert F_k3_gen.is_smooth()
assert F_k3_gen.topological_euler_characteristic() == 24
assert F_k3_gen.geometric_genus() == 1
assert F_k3_gen.irregularity() == 0

F_k3_0 = pi_k3.special_fiber()
assert F_k3_0 == pi_k3.central_fiber()
assert not F_k3_0.is_smooth()
assert F_k3_0.is_connected()

# specialize: Hodge number h^{1,1} jumps at the special fiber (monodromy)
mono = pi_k3.monodromy_operator()
assert not mono.is_identity()     # non-trivial monodromy around t=0

# specialize a divisor class from general to special fiber
H_gen = F_k3_gen.hyperplane_class()
H_sp  = pi_k3.specialize(H_gen)
assert H_sp in F_k3_0.picard_group()


# ============================================================================
# Section 3: Pencil of conics (rational fibration)
# ============================================================================
# t·x^2 + y^2 - z^2 for t ∈ AA^1.  At t=0: (y-z)(y+z), a degenerate conic.

R2.<x2,y2,z2,T3> = PolynomialRing(CC, 4)
conic_fam = T3 * x2^2 + y2^2 - z2^2
X_conic   = Variety(conic_fam)
pi_conic  = X_conic.projection_to(AA1, variable=T3)

assert pi_conic.is_flat()
F_c_gen = pi_conic.general_fiber()
assert F_c_gen.genus() == 0 and F_c_gen.is_smooth()

F_c_0 = pi_conic.special_fiber()
assert not F_c_0.is_irreducible()     # splits into two lines at t=0
assert F_c_0.irreducible_components().length() == 2
assert all(L.genus() == 0 for L in F_c_0.irreducible_components())

# is_flat() fails if the family has non-constant fiber dimension
X_bad = Variety(T3 * (x2^2 + y2^2 + z2^2))   # fiber drops dimension at t=0
pi_bad = X_bad.projection_to(AA1, variable=T3)
assert not pi_bad.is_flat()


# ============================================================================
# Section 4: Branched cyclic covers via defining equation z^n - f = 0
# ============================================================================
# A Z/nZ-cover of Y branched over V(f) ⊂ Y is the hypersurface
#   { z^n = f(x_0, ..., x_N) }
# in the total space of the line bundle O(deg f / n) over Y.
#
# For a double cover of PP^2 branched over a degree-2k curve f:
#   z^2 - f = 0  in the total space of O(k) over PP^2.

# Double cover of PP^2 branched over a smooth sextic (k=3): gives a K3 surface
R3.<u,v,w> = PolynomialRing(CC, 3)
f_sex  = u^6 + v^6 + w^6                     # Fermat sextic, degree 6
f_dc   = BranchedCover.cyclic(P2, n=2, branch_equation=f_sex)

assert f_dc.defining_equation() == f_dc.domain_variable()^2 - f_sex
assert f_dc.domain_variable().name() == 'z'
assert f_dc.degree() == 2
assert f_dc.domain().is_k3()
assert f_dc.branch_locus() == Variety(f_sex)
assert f_dc.ramification_divisor() == f_dc.pullback(Variety(f_sex).as_divisor()) / 2

# Triple cover of PP^2 branched over a smooth cubic (k=1): gives a degree-3 surface
f_cub  = u^3 + v^3 + w^3
f_tc   = BranchedCover.cyclic(P2, n=3, branch_equation=f_cub)
assert f_tc.defining_equation() == f_tc.domain_variable()^3 - f_cub
assert f_tc.degree() == 3

# Double cover in a family: z^2 - (f_0 + t·f_1) varies in t
f_fam  = f_sex + T3 * (u^5*v + v^5*w + w^5*u)
f_dc_fam = BranchedCover.cyclic(P2, n=2, branch_equation=f_fam)
pi_dc  = f_dc_fam.total_space_family()

assert pi_dc.is_flat()
assert pi_dc.general_fiber().is_k3()
assert pi_dc.general_fiber().topological_euler_characteristic() == 24

# Defining equation is a global section of O(2k) on the total space
assert f_dc.defining_equation() in f_dc.total_space().sections(f_dc.total_space().tautological_bundle(2))


# ============================================================================
# Section 5: Lefschetz fibration / fibration over PP^1
# ============================================================================
# A Lefschetz fibration π: X → PP^1 has smooth general fiber and finitely many
# nodal fibers.  For a fibration of elliptic curves:
#   χ_top(X) = χ_top(PP^1) · χ_top(F_gen) + Σ (number of vanishing cycles)

R_lef.<x_l,y_l,z_l,s_l,t_l> = PolynomialRing(CC, 5)
# Family of cubics: s*y^2*z = x(x-z)(x-t*z) + t*s*z^3 in PP^2 × PP^1
lef_eq   = s_l * y_l^2 * z_l - x_l * (x_l - z_l) * (x_l - t_l*z_l)
X_lef    = Variety(lef_eq)
pi_lef   = X_lef.projection_to(PP^1(CC), variables=[s_l, t_l])

assert pi_lef.is_flat()
assert pi_lef.is_lefschetz_fibration()

F_lef_gen = pi_lef.general_fiber()
assert F_lef_gen.genus() == 1

nodal_fibers = pi_lef.singular_fibers()
assert all(F.singular_locus().cardinality() == 1 for F in nodal_fibers)
assert all(F.singular_locus().points()[0].is_nodal() for F in nodal_fibers)

# Noether formula for the total space (elliptic surface)
chi_top_X  = X_lef.topological_euler_characteristic()
chi_top_F  = F_lef_gen.topological_euler_characteristic()   # 0 for elliptic
n_nodal    = len(nodal_fibers)
assert chi_top_F == 0
assert chi_top_X == n_nodal * 1    # each nodal fiber contributes +1 to χ


# ============================================================================
# Section 6: Cuspidal degeneration  V(x^3 - y^2 + t)
# ============================================================================
# The family X := V(x^3 - y^2 + t) over AA^1 with parameter t.
# - Central fiber (t=0): V(x^3 - y^2) — the cuspidal cubic (A_2 singularity).
# - General fiber (t ≠ 0): V(x^3 - y^2 + t) — smooth elliptic curve.
#
# This is an affine family; the total space maps to AA^1 by projecting to t.

Ra_cusp.<x_cp, y_cp, t_cp> = PolynomialRing(CC, 3)
f_cusp_fam = x_cp^3 - y_cp^2 + t_cp
X_cusp_fam = Variety(f_cusp_fam)                          # total space in AA^3
pi_cusp    = X_cusp_fam.projection_to(AA^1(CC), variable=t_cp)

assert pi_cusp.is_flat()
assert pi_cusp.is_smooth_over_generic_point()

# General fiber: smooth elliptic curve (t ≠ 0)
F_cusp_gen = pi_cusp.general_fiber()
assert F_cusp_gen.is_smooth()
assert F_cusp_gen.genus() == 1
assert F_cusp_gen.is_elliptic()

# Special fiber (t=0): cuspidal cubic V(x^3 - y^2)
F_cusp_0 = pi_cusp.special_fiber()
assert F_cusp_0 == pi_cusp.central_fiber()
assert not F_cusp_0.is_smooth()
assert F_cusp_0.singular_locus().cardinality() == 1
sing_cusp = F_cusp_0.singular_locus().points()[0]
assert sing_cusp.is_cuspidal()
assert not sing_cusp.is_nodal()
assert sing_cusp.singularity_type() == Singularity("A2")
assert F_cusp_0.geometric_genus() == 0    # cuspidal: p_a = 1, p_g = 0
assert F_cusp_0.arithmetic_genus() == 1   # by degree formula for cubic

# Specialize a point: the identity section [x=0, y=0, t] specializes to the cusp
sec_origin = pi_cusp.section([0, 0])            # section (x,y) = (0,0) for all t
assert sec_origin.is_section()
p_spec = pi_cusp.specialize(sec_origin, t=0)
assert p_spec == sing_cusp                      # specializes to the singular point

# Concrete fiber at a specific t ≠ 0
F_cusp_1 = pi_cusp.fiber_at(AA^1(CC).point([1]))
assert F_cusp_1.is_smooth()
assert F_cusp_1.genus() == 1

# Monodromy: the fundamental group of AA^1 \ {0} acts on H^1(F_gen, ZZ).
# For a cuspidal degeneration the monodromy is unipotent: N^2 = 0 but N ≠ 0.
mono_cusp = pi_cusp.monodromy_operator()
assert not mono_cusp.is_identity()
assert (mono_cusp.matrix() - mono_cusp.identity_matrix()).is_nilpotent()
N_cusp = mono_cusp.matrix() - mono_cusp.identity_matrix()
assert N_cusp^2 == 0 * N_cusp    # N^2 = 0 (cuspidal = Type II degeneration in Kulikov classification)


# ============================================================================
# Section 7: Weierstrass family of elliptic curves
# ============================================================================
# The Weierstrass family y^2 = x^3 + a(t)*x + b(t) over a parameter base.
# Discriminant Δ = -16*(4a^3 + 27b^2).
# Smooth fibers: Δ(t) ≠ 0.
# Nodal fiber:   Δ(t) = 0 and a^3/b^2 ratio is generic (cuspidal or nodal).
#
# Concrete example: y^2 = x*(x-1)*(x-t) = x^3 - (t+1)*x^2 + t*x
# (This is the Legendre family, now written in inhomogeneous affine Weierstrass form.)
# The Weierstrass change of variables X = x - (t+1)/3, Y = y brings it to
# y^2 = X^3 + A(t)*X + B(t) with A, B explicit polynomials.

Ra_W.<x_W, y_W, t_W> = PolynomialRing(CC, 3)

# Hesse pencil: a^3 + b^3 + c^3 - 3*t*a*b*c = 0
# (cubic in PP^2 with parameter t; smooth for t ≠ 1, ω with ω^3=1)
# Simpler explicit Weierstrass family: y^2 = x^3 - t
# At t=0: y^2 = x^3 (cuspidal), p_g = 0; for t≠0: smooth elliptic.

f_W = y_W^2 - (x_W^3 - t_W)
X_W = Variety(f_W)
pi_W = X_W.projection_to(AA^1(CC), variable=t_W)

assert pi_W.is_flat()
assert pi_W.is_smooth_over_generic_point()

F_W_gen = pi_W.general_fiber()
assert F_W_gen.genus() == 1
assert F_W_gen.is_smooth()
assert F_W_gen.is_elliptic()

F_W_0 = pi_W.special_fiber()
assert not F_W_0.is_smooth()
assert F_W_0.singular_locus().cardinality() == 1
assert F_W_0.singular_locus().points()[0].is_cuspidal()

# Weierstrass family with a nodal fiber: y^2 = x^3 - x^2 + t*(x^3 - x)
# At t=0: y^2 = x^3 - x^2 = x^2*(x-1), a node at x=y=0.
f_W_nod = y_W^2 - x_W^2 * (x_W - 1) - t_W * x_W * (x_W^2 - 1)
X_W_nod = Variety(f_W_nod)
pi_W_nod = X_W_nod.projection_to(AA^1(CC), variable=t_W)

assert pi_W_nod.is_flat()

F_W_nod_0 = pi_W_nod.special_fiber()
assert not F_W_nod_0.is_smooth()
assert F_W_nod_0.singular_locus().cardinality() == 1
assert F_W_nod_0.singular_locus().points()[0].is_nodal()

F_W_nod_gen = pi_W_nod.general_fiber()
assert F_W_nod_gen.genus() == 1
assert F_W_nod_gen.is_smooth()

# Discriminant vanishing encodes the singular locus of the family
# For y^2 = x^3 + A*x + B: Δ = -16*(4A^3 + 27B^2)
# The discriminant locus of pi_W (y^2 = x^3 - t) in AA^1_t is {t=0} alone
disc_W = pi_W.discriminant_locus()
assert disc_W == AA^1(CC).point([0])

# j-invariant: for y^2 = x^3 - t (A=0, B=-t), j = 0 (cuspidal degeneration at j→∞)
# For a general smooth fiber t≠0: j(E_t) = 1728 * 4A^3 / (4A^3 + 27B^2) with A=0, B=-t
# gives j = 0 for all t≠0.  This is the equianharmonic family (all fibers j=0).
j_W = pi_W.general_fiber().j_invariant()
assert j_W == 0

# Period map: the period τ(t) → ∞ as t → 0 (degeneration of the lattice)
assert pi_W.period_map().is_holomorphic_on(AA^1(CC).remove_point([0]))
