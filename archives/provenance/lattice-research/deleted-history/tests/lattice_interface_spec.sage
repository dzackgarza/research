r"""
These tests define things that should be possible with the finalized interfaces.
"""

Z = Lattice.()
assert Z.gram_matrix().is_identity()
assert Z.is_integral() and Z.is_nondegenerate()

Z2 = Lattice.ZZ(2)
assert Z2.gram_matrix() == Matrix(ZZ, 1, [2])
assert Z2 == Z.twist(2) == 2*Z

E8 = Lattice.root_lattice("E8")
assert E8 == Lattice.E8()
assert E8.is_integral() and E8.is_nondegenerate()
assert E8.is_negative_definite() and not E8.is_positive_definite() and not E8.is_indefinite()
assert E8.is_unimodular() and E8.discriminant_group().is_trivial()
assert E8.signature == (0, 8) and E8 == Lattice.II(0, 8)
assert E8.rank() == 8 and E8.dual() == E8

E8_2 = E8.twist(2)
assert not E8_2.is_unimodular() and E8_2.dual() == (1/2)*E8_2
# If L is a lattice, then L(2)^* = (1/2)L^* always, 
# and if L is unimodular, L^* = L.
assert E8_2.discriminant_group() == E8_2.dual()/E8_2 == (1/2)E8/E8 == E8 / (2*E8)
# If L is unimodular, then A_{L(2)} = L(2)^*/L(2) = (1/2)L/L = L/2L

assert E8.root_sublattice() == E8
assert E8.orthogonal_group() == E8.weyl_group()
assert E8.weyl_group().cardinality() == 2^(14) * 3^5 * 5^2 * 7
R_E8 = E8.root_system()
assert R_E8.cardinality() == 240
assert R_E8.rank() == 8


U.<e,f> = Lattice.U()
assert U.is_nondegenerate() and U.rank() == 2 and U.signature() == (1,1)
assert abs(U.det()) == 1 and U.is_unimodular() and not U.is_even()
assert e^2 == 0 and f^2 == 0 and e*f == f*e and e*f == 1
assert U.gram_matrix() == Matrix(ZZ, 2, [0,1,1,0])
assert e.is_orthogonal_to(e) and e in e.perp()
assert not e.is_orthogonal_to(f) and e not in f.perp()

assert U.discriminant_group().is_trivial()

assert e^2 == e*e == U.q(e) == U.b(e, e)
assert e.is_isotropic()

span_e = U.span([e]) # Warning: lattice is degenerate
assert span_e == U.span(e) # Convenience, replace e with [e]
assert span_e == e.span()
assert U.is_degenerate()

e_perp = U.perp(span_e)
assert e_perp == e.perp() # e knows it is embedded in U
assert U.perp() == e.span()
assert e in e.perp() and f not in e.perp() # Cache the perp computation internally.

assert e.perp().quotient(e.span()) == f.span()
assert e.perp() / e.span() == e.perp().quotient(e.span()) == e.perp() / e
assert (e.perp() / e).is_nondegenerate()
assert U.isotropic_reduction(e) == e.perp() / e # Convenience method
assert e.isotropic_reduction() == e.perp() / e # Convenience

U2.<ep, fp>= U.twist(2)
assert abs(U.det()) != 1 and not U.is_unimodular() and U.is_even()
assert ep^2 == 0 and fp^2 == 0 and ep*fp == fp*ep and ep*fp == 2
assert U.gram_matrix() == Matrix(ZZ, 2, [0,2,2,0])

assert U2 == 2*U # Scalar-lattice multiplication: twist.

L1.<e1, f1, ep1, fp1> = U + U2 # Lattice-lattice addition: Direct sum
assert L1.is_decomposable()

Up, U2p = L1.summands # Represent U, U2 *as their images* in L1
assert Up.is_isometric_to(U)
is_isometric, witness = Up.is_isometric_to(U, witness=True) # Returns the isometry
assert witness == identity_matrix(ZZ, 2)
assert Up == U # Equality := same object OR isometric via the identity.
assert U2p == U2 # Same logic as above.

assert L1.gram_matrix() == block_matrix(U.gram_matrix(), U2.gram_matrix())

iota_U, iota_U2 = L1.embeddings
assert iota_U in U.hom(L1) # iota_U: U -> L1, inclusion as the first summand
assert iota_U.to_matrix() == identity_matrix(ZZ, 2).stack(zero_matrix(ZZ, 2)) # Of the form [id | 0]^t
assert e, f in iota_U.domain()
assert iota_U(e) == e1 and iota_U(f) == f1
assert iota_U(U) == L1.span([e1, f1])

assert ep, fp in iota_U2.domain()
assert iota_U2(ep) = ep1 and iota_U2(fp) == fp1
assert iota_U2(U2) == L1.span([ep1, fp1])


assert iota_U.is_primitive() # Primitive iff coker is torsionfree.
assert iota_U.coker() == L1 / U == U2 # Quotient as modules and attempt to lift back to lattices
assert iota_U.perp() == U2
iota = iota_U + iota_U2 
assert iota in Lattice.hom(U + U2, L1)
im_iota = iota.image()
assert im_iota == U + U2
assert iota.is_primitive() # As an embedding
assert iota.image().is_primitive() # As a sublattice
assert iota.image().is_saturated() # As a sublattice
assert iota.is_injective() and iota.is_surjective() and iota.is_bijective() and iota.is_isomorphism()
assert iota.image().saturation() == iota.image() == L1
assert iota.image().index() == 1
assert L1 / iota_U.image() == iota_U2.image() and L1 / iota_U2.image() == iota_U.image()
assert iota_U.perp() == iota_U2.image() and iota_U2.perp() == iota_U.image()

C2 = CyclicGroup(2) == ZZ / (2 * ZZ) # May need to wrap groups for this notation.
K4 = C2 + C2 # If this doesn't work in sage, we should wrap groups.
assert U2.discriminant_group().is_isomorphic(K4) # Isomorphism as groups
assert U2.discriminant_group() != K4 # Need to specify the form
assert U2.discriminant_group() == U2.dual() / U2 # Automatically apply the canonical inclusion L -> L^*
iota_dual = U2.dual()

assert U2.dual() == (1/2) * U # Need to handle automatic base change to QQ to handle duals and rational twists.
assert U2.discriminant_group() == ( (1/2) * U ) / U

disc_ring = QQ/ZZ # If sage doesn't support this, need to wrap.
A_U2.<g1, g2> = BilinearModule(K4, Matrix(disc_ring, 2, [0, 1/2, 1/2, 0]))
assert U2.discriminant_group().is_isometric_to(A_U2)
assert U2.discriminant_group() == A_U2 # Isometric via the identity.
is_isometric, witness = U2.discriminant_group().is_isometric_to(A_U2, witness=True) # Returns the isometry
assert witness == identity_matrix(R, 2)

assert g1^2 == 1/2 and g2^2 == 1/2 and g1*g2 == g2*g1 == 0
assert g1^2 == A_U2.q(g1) = A_U2.b(g1, g1)
assert g1.is_isotropic() and g2.is_isotropic()

assert ep.image_in_discriminant() == A_U2(0) # Identity element
assert fp.image_in_discriminant() == A_U2(0) # Identity element
assert ep.image_in_discriminant() == A_U2(ep) # Automatically project

U2_dual.<epd, fpd> = U2.dual()
assert epd == ep/2 and fpd == fp/2
assert epd.image_in_discriminant() == g1 # Generators have canonical lifts
assert g1.lift_to_dual_lattice() == epd
assert fpd.image_in_discriminant() == g2
assert epd.image_in_discriminant() == A_U2(epd) # Automatically project.

assert set(x for x in A_U2) == set(0, g1, g2, g1+g2) # Automatically interpret 0 as the identity
assert  set(x for x in A_U2) == set(map(lambda x: A_U2(x), [0, epd/2, fpd/2, (epd + fpd)/2])) # Known explicit lifts in U2^*

assert A_U2.isotropic_elements() == A_U2.elements_of_norm(0) == set([0,g1,g2])
assert A_U2.elements_of_norm(1) == set([g1+g2])
assert A_U2.values() == set([0, 1]) # Mod 2ZZ
assert A_U2.value_map() == dict({0: [0, g1, g2], 1: [g1 + g2]})
assert A_U2.value_counter() == dict({
    0: set(x in A_U2 if x^2=0), 
    1: set(x in A_U2 if x^2=1)
})



assert len(x for x in U2 if xi < 2 for xi in x) < 10^9 # Infinite generator that can be truncated based on reasonable filters.re
assert U2.elements_of_norm(n) == set(x in U2 if x^2 = n) # Generator for infinite but efficient enumeration
assert U2.elements_of_norm(0) == U2.isotropic_elements() # Infinite generators

# TODO: assert O(U) == ? and O(U2) == ?, explicit generators and relations known from theory.
# TODO: assert O(U).stabilizer(e) == ?, O(U2).stabilizer(ep) == ?, known from theory.
# TODO: 
# TODO: assert U2.isotropic_elements() / O(U) == ..., computes O(U) orbits of isotropic vectors


G = U.orthogonal_group()
assert G == U.hom(U) # Homs are always lattice homs
assert G = U.O() # Convenience method

F = G.element_from_map_on_generators({e: f, f: e}) # Generally, in H := Hom(L1, L2) with L1 = <a1, ...> and L2  = <b1, ...>, specify a morphism by setting up a dict with entries a_1, a_2, ... and values ZZ-linear combinations of b_i.
assert F in G # Checks matrix equation to assert F is an isometry.
assert F.is_involution() and F^2 == G.id() and F.order() == 2
assert F(e) == f and F(f) == e
assert e^2 == F(e)^2 and f^2 == F(f)^2
assert F.is_injective() and F.is_surjective() and F.is_bijective() and F.is_isometry()

assert F.to_matrix() == Matrix(ZZ, 2, [0, 1, 1, 0])
assert F.is_permutation() # F.to_matrix() is a permutation matrix, thus a permutation of generators.
# TODO: assert U.invariant_sublattice(F) == ..., compute from theory
# TODO: assert U.coinvariant_sublattice(F) == ... == U.invariant_sublattice(F).perp(), compute ... from theory, but L_G := (L^G)^\perp by definition.
assert not F.is_shear()

var("a, b")
U.<e, f> = Lattice.U()
assert (a*e + b*f) == a^2*e^2 + (2*a*b)*e*f + b^2*f^2 == 2*a*b
v = (a*e + b.f).substitute({a:-1, b:-1})
assert v == -e -f and v^2 == -2 and v.is_root()
assert v.div() == 1 # Divisibility
assert U.roots() == set([e-f, -(e-f)])
R_U = U.root_sublattice()
assert R_U == Lattice.root_lattice("A1") == (e-f).span()
assert R_U.rank() == 1
assert R_U.is_primitive()
assert R_U.gens() == set([e-f]) # Always choose positive generators.
assert U / R_U == e.span()
assert R_U.perp() == (e+f).span()

assert (R_U + R_U.perp()).index() == 2 # Strategies to compute: find change-of-basis from <e,f> to <e+f, e-f> and check det == 2.

zero_disc = BilinearModule(ZZ/2, zero_matrix(QQ/ZZ, 2)) # ZZ/2ZZ with the zero BILINEAR form
assert zero_disc == BilinearModule.zero_form(ZZ/2) # Convenience wrapper.
# Note: if L is an R-lattice and M is a sublattice, then L/M always inherits a ff(R)/R-valued quadratic form, q([v]) := q(v) mod R, for any lift of [v] from L/M to L.
# It inherits a bilienar form via b([v], [w]) := b(v, w) mod R similarly.
assert U / (R_U + R_U.perp()) == zero_disc

v = e-f
s_v = v.reflection()
var("x")
assert s_v(x) == x - 2*(x*v / v^2)*v # Should allow expanding symbolic formulas
assert s_v(v) == -v
assert s_v in U.O()
assert sv * sv = U.O().id() # Multiplication := composition
# TODO: assert s_v.as_word_in_generators() == ..., generally writing f \in O(L) as as a word in terms of known generators.
assert s_v in U.weyl_group() # Group generated by reflections
assert U.W() == U.weyl_group() # Convenience
assert U.W().is_isomorphic_to(ZZ/2)
assert U.W().gens() == set([s_v])
assert s_v.is_reflection()
assert s_v.refelection_decomposition() == [s_v] # Decompose an arbitrary reflection as a word in the generators of W(L).

assert U.eichler_group() == U.E() # Subgroup of Eichler transvections


# Assert Lattice.root_lattice(...) makes sense for A,B,C,D,E types, as well as affine types, and I_n, G_2, F_4, etc.
# Assert root lattices have Coxeter diagram methods.
# Assert Weyl groups have Coxeter diagram methods.

# TODO: define Eichler transvections t_ab(x) := ...
# Assert t_ab in U.O() and t_ab not in U.W() and t_ab in U.E()
# TODO: show that Eichler formulas for (t_{a1,b1} * ... * t_{an, bn})(x) can be extracted as f(x) = ....
# TODO: is U.E() a subgroup of U.W()? Show if so.

L.<a,b> = ... # A good candidate lattice for testing Eichlers
t_ab = eichler_transvection(a, b)
# Validates: a.is_isotropic() and b in a.perp()

var("v")
assert t_ab(v) == b - (b*v)*a + (a*v)*b - (b^2/2)*(a*v)*a
assert t_ab^(-1) == eichler_transvection(a,-b)
