L = Lattice.U().twist(2)
assert L.is_even()

OU = L.O() # Orthogonal group
assert OU in Modules(ZZ)
assert OU.is_finite()
assert OU == ConditionSet(GL(2,ZZ), lambda g: g.T() * L.gram_matrix() * g == L.gram_matrix())
m_id = -1 * identity_matrix(ZZ, 2)
m_flip = matrix(ZZ, 2, [0,1,1,0])
assert OU == MatrixGroup(m_id, m_flip)
Z_2_2.<g1, g2> = (ZZ/2)^2
is_isom, witness = OU.is_isomorphic_to(Z_2_2)
assert is_isom and witness.is_isomorphism()
assert witness in OU.Hom(Z_2_2)
assert is_isom(m_id) == g1 and is_isom(m_flip) == g2

assert L in Lattices(ZZ)

R = Zp(2)
L2 = L.base_change(R)
assert L2 in Lattices(R)

assert L.gram_matrix() == matrix(R, 2, [R(0), R(1), R(1), R(0)])

L.<e, f> = Lattice.U()
assert e.span() == L.span([e])
assert e.span().is_degenerate() and e.span() not in Lattices(ZZ)
assert e.span() in BilinearModule(ZZ)
assert e.is_isotropic() and e.span().is_isotropic() # As a sub-bilinear module

assert e.inclusion().image() == e.span()
assert e.perp() == e.span().perp() # Perps are defined wrt inclusion morphisms, on literaly subobjects.
degen_rank2 = e.span() + f.span() # External direct sum
# Forces off-diagonal entries to be zero, not the same as taking the span of all of the elements!
assert degen_rank2.is_degenerate() and not degen_rank2.is_nondegenerate()
assert not degen_rank2 in Lattices(ZZ) and degen_rank2 in BilinearModules(ZZ)
assert e.span() + f.span() != L.span([e,f])


assert e.perp() == e.span() and f.perp() == f.span()
assert e.perp().is_degenerate() and f.perp().is_degenerate()

L.<e,f,g> = Lattice.U() + Lattice.Z()
assert e.perp() == L.span([e, g])
assert e.perp().is_degenerate()
assert L.span([e,g]) == e.span() + g.span() # Ok because they were already orthogonal
assert f.perp() == L.span([f, g])
assert f.perp().is_degenerate()
assert L.span([f,g]) == f.span() + g.span()
assert e.perp() / e.span() == e.perp().quotient(e.span())
assert e.perp() / e == e.perp() / e.span() # Convenience
assert e.isotropic_reduction() == e.perp() / e # Canonical name
assert L.isotropic_reduction(e) == e.isotropic_reduction() # Convenience
assert e.perp()/e == g.span()
assert f.perp()/f == g.span()
assert e.perp() not in Lattices(ZZ) and e.perp()/e in Lattices(ZZ) # Promotion



L.<e,f> = Lattice.U()
M = (e+f).span() + (e-f).span()
assert M.inclusion().index() == 2 # [L:M]=2


# iota_bad = L.End().element_from_dict({e: e, f: -f}) # Assertion error: not an isometry
iota = L.End().element_from_dict({e: f, f:e}) # Checks isometry, okay.
assert iota.is_involution() and iota.order() == 2 and iota^2 == L.End().identity()
assert iota in L.O()
assert L.O() == L.Aut()
G = L.O().subgroup_from_gens([iota])
assert G == iota.cyclic_subgroup() # Convenience
assert G.is_subgroup_of(L.O())
assert G <= L.O() # Convenience

L_inv, L_coinv = G.invariant_coinvariant_sublattice_pair()
assert L_inv == G.invariant_sublattice()
assert L_coinv == G.coinvariant_sublattice()
assert L_inv.perp() == L_coinv and L_coinv.perp() == L_inv
assert L^G == L_inv # Convenience

assert L_inv == (e+f).span() and L_coinv == (e-f).span()
assert L_inv + L_coinv == M
assert L/M == BilinearModule(ZZ/2, matrix(ZZ, 1, [0]))
assert not M.is_isometric(L)
assert M.base_change(QQ).is_isometric(L.base_change(QQ))

iota_M = M.inclusion()
assert not iota_M.coker().is_torsionfree()
assert not iota_M.is_primitive() # By definition, since cokernel is torsion

id = identity_matrix(ZZ, 2)
m1 = -1 * id
m2 = matrix(ZZ, 2, [0,1,1,0])
G == MatrixGroup(m1, m2)
assert L.O() == G
f1, f2  = L.O().element_from_matrix(m1), L.O().element_from_matrix(m2)
f_id, f1, f2 = list(map(lambda x: L.O()(x), [id, m1, m2]))
assert f1^2 == f_id and f2^2 == f_id
assert (f1*f2).to_matrix() == matrix(ZZ, 2, [0,-1,-1,0])
assert [(f1*f2)(x) for x in [e,f]] == [-f, -e]

assert {F.to_matrix() for F in L.O()} == {id, m1, m2, m1*m2}
assert {F for F in L.O()} == {f_id, f1, f2, f1*f2}
assert {F for F in L.O() if F(e) == e} == {f_id}
assert L.O().stabilizer(e) == f_id.cyclic_subgroup() # Identity
assert {F for F in L.O() if F(f) == f} == {f_id}
assert L.O().stabilizer(f) == f_id.cyclic_subgroup() # Identity

assert [F(e) for F in [id, f1, f2, f1*f2]] == [e, -e, f, -f]
assert [F(f) for F in [id, f1, f2, f1*f2]] == [f, -f, e, -e]
assert [F(e+f) for F in [id, f1, f2, f1*f2]] == [e+f,-(e+f),f+e,-(f+e)]

assert {F for F in L.O() if F(e+f) == e+f} == {f_id, f2}
assert L.O().stabilizer(e+f) == f2.cyclic_subgroup()
assert f2.cyclic_subgroup() == ZZ/2 # Canonical iso

assert {F for F in L.O() if F(e-f) == e-f} == {f_id,f1*f2}
assert L.O().stabilizer(e-f) == (f1*f2).cyclic_subgroup()
assert (f1*f2).cyclic_subgroup() == ZZ/2 # Canonical iso


r = e-f
assert r == -2
s_r = r.reflection() # Defined for any non-isotropic vector, as an element of L.base_change(QQ).O(), i.e. a rational matrix.
var("x")
assert s_r.to_formula(x) == x - ( (r*x)/r^2 )*r # Automatic promotion: elements in W(L) have explicit formulas.
assert s_r in L.O() and s_r in L.W() # Weyl group
assert s_r.to_matrix() in GL(2, ZZ)
assert r in L.roots() # Condition set: s_r is always in GL_n(QQ), checks when s_r in GL_n(ZZ) instead
assert s_r.to_matrix() == matrix(ZZ, 2, [0,1,1,0])

assert L.O_plus() == s_r.cyclic_subgroup() # Stable orthogonal group
assert L.W() == L.O_plus()
iota_Op = L.O_plus().inclusion() # Into O(L)
assert iota_Op in L.O_plus().Hom(L.O()) # As groups 
assert iota_Op.index() == 2 # [O(L):O^+(L)]=2

assert not L.is_root_lattice() # Isometric to its maximal root sublattice 
assert L.root_lattice() == r.span()
assert r.span().is_root_lattice()
assert r.is_isometric_to(Lattice.A(1))

assert r.span() in RootLattices # Category containment, automatic promotion
assert r.span().coxeter_diagram() == CoxeterDiagram.A(1) # Weighted graph with self-loops of weights r^2 and edges of weights derived from r_i*r_j

assert L.is_hyperbolic() and L in HyperbolicLattices # Category promotion
assert L.positive_cone() == ConditionSet(L, lambda v: all(v*gi > 0 for gi in L.gens())) # v = ae+bf with a,b>0
assert L.positive_cone().End() == L.O_plus() # By definition for hyperbolic lattices
assert L.coxeter_diagram() == r.span().coxeter_diagram() # Delegate
assert L.coxeter_diagram().Aut() == Groups().zero_group() # May need to be patched in
assert Groups().zero_group() == 0 # Coerce
assert L.coxeter_diagram().Aut() in Groups # Automorphisms of weighted graphs, here A_1 has no symmetries.
assert L.coxeter_polytope() in Polytopes # May need to define or patch in.
assert L.coxeter_polytope().Aut() == Groups().zero_group()

assert L.hyperbolic_space() == HH^1 # Complex upper-half plane 

assert L.positive_cone() in Cones # Category containment
# TODO: hilbert basis for this cone.
# TODO: assert P = {v | v = a*e+b*f, a,b>0, b-a>=0 }
# TODO: what does this look like in the half-space and disk models?
