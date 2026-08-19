# TODO: the semantics here are as intended, but need mathematical checks.

##### Coble geometry contract

# The Coble rank-11 lattice should be obtained from the geometry:
#   rational sextic C with 10 A_1 nodes
#   -> Coble surface S = Bl_nodes(P^2)
#   -> Pic(S)
#   -> K3 cover X -> S
#   -> pull back Pic(S) to H^2(X, ZZ)
# The discriminant group is then computed from that pullback lattice.  The
# orthogonal-complement/transcendental lattice is a second computation, not a
# constructor axiom.

sextic = rational_nodal_sextic
S = CobleSurface.from_sextic(sextic)
PicS = S.picard_group().as_lattice()
assert PicS.rank() == 11
assert PicS.signature_pair() == (1, 10)

cover = S.k3_cover()
pullback = cover.pullback_lattice(PicS)
assert pullback.rank() == 11
assert pullback.gram_matrix() == diagonal_matrix(ZZ, [2] + [-2] * 10)
assert pullback.discriminant_group().is_p_elementary(2)
assert pullback.discriminant_group().p_rank(2) == 11

T_Co = cover.orthogonal_complement_of_pullback_lattice()
assert T_Co.rank() == 11
assert T_Co.signature_pair() == (2, 9)
assert T_Co.discriminant_group().is_p_elementary(2)
assert T_Co.discriminant_group().p_rank(2) == 11

U = Lattice.U()
e,f = U.gens()

# Unimodular => isometric to dual
iota_U = U.dual().inclusion_morphism()
assert iota_U in U.hom(U.dual())
assert iota_U.is_isometry()

# Dual elements are functionals
e_star, f_star = U.dual().gens()
assert e_star in U.hom(Lattice.Z())
assert f_star in U.hom(Lattice.Z())

# Dual basis: e_i^*(e_j) = \delta_{ij}
assert e_star(e) == 1 and e_star(f) == 0
assert f_star(e) == 0 and f_star(f) == 1

# \iota_L sends v -> \beta(v, \cdot)
e_functional = U.hom(Lattice.Z()).from_dict({e: U.b(e, e), f: U.b(e,f)})
assert iota_U(e) == e_functional
f_functional = U.hom(Lattice.Z()).from_dict({e: U.b(e,f), f: U.b(f,f)})
assert iota_U(f) == f_functional

# Under the isometry U^* -> U, e^* -> f and f^* -> e
assert iota_U^(-1)(e_star) == f
assert iota_U^(-1)(f_star) == e
assert iota_U(e) == f_star
assert iota_U(f) == e_star
# Why: e^*(e) = 1 and e^*(f) = 0 => e^* = \beta(f, \cdot)
# and f^*(e) = 0 and f^*(f) = 1 => f^* = \beta(e, \cdot)

# Isometry between L and L^* for unimodular L
assert U.dual().is_isometric_to(U)
# But the isometry is not the identity -- it swaps the factors.
assert U.dual() != U

##### Twists

U2 = U.twist(2)
ep, fp = U2.gens()

# multiplication is not twisting:
assert not (2*U).is_isometric(U2)
# Instead, c*L := {c*v | v in L}, so generally c*L is isometric to L.twist(c^2).
e2, f2 = (2*U).gens()
assert e2 == 2*e # Automatically regard n*v as an element of L \cap nL
assert f2 == 2*f
assert e2*f2 == (2*e)*(2*f)
assert U.twist(2).gram_matrix() == 2*(U.gram_matrix())

# Can construct a sublattice of L from a sequence of elements [v_1, ...., v_n]
# by constructing the Gram matrix G_ij := \beta_L(v_i, v_j)
assert 2*U == U.sublattice_from_gens([2*e_i for e_i in U.gens()])
isom, witness = (2*U).is_isometric(U.twist(4), witness = True)
assert isom and witness.to_matrix() == diagonal_matrix(ZZ, [2,2])
assert U.index_of(sublattice(2*U)) == 2

# Need to monkey-patch sage internals significantly to make this syntax work:
C_2_2 = BilinearModule( (ZZ / (2*ZZ)), matrix(ZZ, 2, [0,1,1,0]))
assert C_2_2 in BilinearModules and C_2_2 in TorsionBilinearModules # Category containment
b_2_2 = C_2_2.bilinear_form()
# L/nL, when L is integral, inherits a ZZ/nZZ-valued bilinear form.
assert b_2_2.domain() == C_2_2 and b_2_2.codomain() == ZZ / (2*ZZ)
assert (U / (2*U)).is_isometric_to(C_2_2) # As torsion bilinear modules

iota_U2 = U2.dual().inclusion_morphism()
ep_star, fp_star = U2.dual().gens()

# Algebraic dual basis
assert ep_star(ep) == 1 and ep_star(fp) == 0
assert fp_star(ep) == 0 and fp_star(fp) == 1

# \iota_L sends v -> \beta(v, \cdot)
ep_functional = U2.hom(Lattice.Z()).from_dict({
	ep: U2.b(ep,ep), 
	fp: U2.b(ep,fp)
})
assert iota_U2(ep) == ep_functional
fp_functional = U2.hom(Lattice.Z()).from_dict({
	ep: U2.b(ep,fp), 
	fp: U2.b(fp,fp)
})
assert iota_U2(fp) == fp_functional

# Under the isometry U(2)^* -> (1/2)*U, ep^* -> (1/2)*f and f^* -> (1/2)*e
is_isometric, f_iso = U2.dual().is_isometric_to( (1/2)*U, witness=True)
assert is_isometric and f_iso.is_isometry()

half_e, half_f = ((1/2)*U).gens()

# Naturally regard (p/q)*v as an element of L_QQ  
assert (1/2)*e == half_e and (1/2)*f == half_f

assert f_iso(ep_star) == half_f
assert f_iso(fp_star) == half_e
assert f_iso.inverse()(half_f) == ep_star
assert f_iso.inverse()(half_e) == fp_star
