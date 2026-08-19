r"""
Extended lattice-interface surface migrated from the retired
``lattice_interface_spec.sage``.

This file records the remaining planned surface beyond
``interface_semantics.sage``: dual lattices and discriminant lifts,
direct-sum embeddings, explicit orthogonal groups of ``U`` and ``U(2)``,
root/Weyl data, and Eichler transvections.
"""

from src import DynkinDiagram, Lattice, eichler_transvection

# ============================================================================
# 1. DUAL LATTICES AND EXPLICIT DISCRIMINANT-LIFT SEMANTICS
# ============================================================================

E8 = Lattice.E(8)
E8_2 = E8.twist(2)

assert E8.dual() == E8
assert E8_2.dual() == QQ(1, 2) * E8
assert E8_2.discriminant_group() == E8_2.dual() / E8_2
assert E8_2.discriminant_group() == E8 / (2 * E8)

U = Lattice.U()
e, f = tuple(U.basis())
U2 = U.twist(2)
ep, fp = tuple(U2.basis())

A_U2 = U2.discriminant_group()
g1, g2 = tuple(A_U2.gens())

assert A_U2.cardinality() == 4
assert g1.additive_order() == 2 and g2.additive_order() == 2
assert A_U2.q(g1) == 0 and A_U2.q(g2) == 0
assert A_U2.b(g1, g1) == 0 and A_U2.b(g2, g2) == 0
assert A_U2.b(g1, g2) == QQ(1, 2)
assert A_U2.q(g1 + g2) == 1
assert set(A_U2) == {A_U2.zero(), g1, g2, g1 + g2}
assert A_U2.isotropic_elements() == {A_U2.zero(), g1, g2}
assert A_U2.elements_of_norm(1) == {g1 + g2}
assert A_U2.value_map() == {
    0: {A_U2.zero(), g1, g2},
    1: {g1 + g2},
}

U2_dual = U2.dual()
ep_dual, fp_dual = tuple(U2_dual.basis())
assert ep_dual == ep / 2 and fp_dual == fp / 2
assert ep_dual.discriminant_class() == g1
assert fp_dual.discriminant_class() == g2
assert g1.lift() == ep_dual
assert g2.lift() == fp_dual
assert ep.discriminant_class() == A_U2.zero()
assert fp.discriminant_class() == A_U2.zero()


# ============================================================================
# 2. DIRECT SUMS, SUMMANDS, EMBEDDINGS, AND SATURATED IMAGES
# ============================================================================

L1 = U + U2
e1, f1, ep1, fp1 = tuple(L1.basis())

Up, U2p = L1.summands
assert Up.is_isometric_to(U)
assert U2p.is_isometric_to(U2)

iota_U, iota_U2 = L1.embeddings
assert iota_U.to_matrix() == identity_matrix(ZZ, 2).stack(zero_matrix(ZZ, 2))
assert iota_U2.to_matrix() == zero_matrix(ZZ, 2).stack(identity_matrix(ZZ, 2))
assert all(v in iota_U.domain() for v in (e, f))
assert all(v in iota_U2.domain() for v in (ep, fp))
assert iota_U(e) == e1 and iota_U(f) == f1
assert iota_U2(ep) == ep1 and iota_U2(fp) == fp1
assert iota_U.image() == L1.span([e1, f1])
assert iota_U2.image() == L1.span([ep1, fp1])
assert iota_U.is_primitive()
assert iota_U2.is_primitive()
assert iota_U.cokernel().is_isomorphic_to(U2)
assert iota_U2.cokernel().is_isomorphic_to(U)
assert iota_U.image().perp() == iota_U2.image()
assert iota_U2.image().perp() == iota_U.image()

iota = iota_U.direct_sum(iota_U2)
assert iota.domain().is_isometric_to(U + U2)
assert iota.image() == L1
assert iota.is_injective() and iota.is_surjective()
assert iota.is_bijective() and iota.is_isomorphism()
assert iota.image().is_primitive()
assert iota.image().is_saturated()
assert iota.image().saturation() == L1
assert iota.image().index() == 1


# ============================================================================
# 3. THE EXPLICIT GROUPS O(U) AND O(U(2))
# ============================================================================

I2 = identity_matrix(ZZ, 2)
swap = matrix(ZZ, [[0, 1], [1, 0]])
minus_I2 = -I2
minus_swap = -swap

assert set(U.orthogonal_group()) == {I2, swap, minus_I2, minus_swap}
assert set(U2.orthogonal_group()) == {I2, swap, minus_I2, minus_swap}
assert U.orthogonal_group().is_isomorphic_to(CyclicPermutationGroup([2, 2]))
assert U2.orthogonal_group().is_isomorphic_to(CyclicPermutationGroup([2, 2]))

assert set(U.orthogonal_group().stabilizer(e)) == {I2}
assert set(U2.orthogonal_group().stabilizer(ep)) == {I2}
assert set(U.orthogonal_group().stabilizer_of_isotropic_line(e)) == {I2, minus_I2}
assert set(U2.orthogonal_group().stabilizer_of_isotropic_line(ep)) == {I2, minus_I2}

assert U.primitive_isotropic_vector_orbits() == {e}
assert U2.primitive_isotropic_vector_orbits() == {ep}
assert U2.isotropic_vector_orbits() == {U2.zero()} | {n * ep for n in ZZ if n > 0}


# ============================================================================
# 4. INVOLUTIONS, ROOTS, REFLECTIONS, AND WEYL GROUPS
# ============================================================================

G = U.orthogonal_group()
assert G.is_subgroup_of(U.hom(U))

F = G.from_matrix(swap)
assert F in G
assert F.is_involution() and F.order() == 2
assert F(e) == f and F(f) == e
assert F.to_matrix() == swap
assert F.is_permutation()
assert not F.is_shear()

assert U.invariant_sublattice(F) == U.span([e + f])
assert U.coinvariant_sublattice(F) == U.span([e - f])
assert U.coinvariant_sublattice(F) == U.invariant_sublattice(F).perp()

v = e - f
assert v * v == -2
assert v.divisibility() == 1
assert v.is_root()
assert U.roots() == {v, -v}

R_U = U.root_sublattice()
assert R_U == Lattice.root_lattice("A1")
assert R_U == U.span([v])
assert R_U.rank() == 1
assert R_U.is_primitive()
assert R_U.gens() == {v}
assert U / R_U == U.span([e + f])
assert R_U.perp() == U.span([e + f])
assert (R_U + R_U.perp()).index() == 2

zero_disc = BilinearModule.zero_form(CyclicGroup(2))
assert U / (R_U + R_U.perp()) == zero_disc

s_v = v.reflection()
assert s_v(e) == f and s_v(f) == e
assert s_v(v) == -v
assert s_v in U.orthogonal_group()
assert s_v * s_v == U.orthogonal_group().identity()
assert s_v.as_word_in_generators() == [s_v]
assert s_v in U.weyl_group()
assert U.W() == U.weyl_group()
assert U.W().is_isomorphic_to(CyclicGroup(2))
assert U.W().gens() == {s_v}
assert s_v.is_reflection()
assert s_v.reflection_decomposition() == [s_v]

assert Lattice.root_lattice("A1").coxeter_diagram() == DynkinDiagram("A1")
assert Lattice.root_lattice("B3").coxeter_diagram() == DynkinDiagram("B3")
assert Lattice.root_lattice("C3").coxeter_diagram() == DynkinDiagram("C3")
assert Lattice.root_lattice("D4").coxeter_diagram() == DynkinDiagram("D4")
assert Lattice.root_lattice("E8").coxeter_diagram() == DynkinDiagram("E8")
assert Lattice.root_lattice("F4").coxeter_diagram() == DynkinDiagram("F4")
assert Lattice.root_lattice("G2").coxeter_diagram() == DynkinDiagram("G2")
assert U.W().coxeter_diagram() == DynkinDiagram("A1")


# ============================================================================
# 5. EICHLER TRANSVECTIONS
# ============================================================================

assert U.eichler_group() == U.E()
assert U.E().is_trivial()
assert U.E().is_subgroup(U.W())

L_eich = Lattice.from_string("U + A_1")
e0, f0, r = tuple(L_eich.basis())
assert e0.is_isotropic()
assert r in e0.perp()
assert r * r == -2

t_er = eichler_transvection(e0, r)
for basis_vector in tuple(L_eich.basis()):
    assert t_er(basis_vector) == (
        basis_vector - (r * basis_vector) * e0 + (e0 * basis_vector) * r - QQ(r * r, 2) * (e0 * basis_vector) * e0
    )

assert t_er.inverse() == eichler_transvection(e0, -r)
assert t_er in L_eich.orthogonal_group()
assert t_er in L_eich.E()
assert t_er == (r + e0).reflection() * r.reflection()
assert t_er.as_word_in_reflections() == [(r + e0).reflection(), r.reflection()]

L_eich2 = Lattice.from_string("U + A_1 + A_1")
e2, f2, r1, r2 = tuple(L_eich2.basis())
t1 = eichler_transvection(e2, r1)
t2 = eichler_transvection(e2, r2)
t12 = eichler_transvection(e2, r1 + r2)

assert t1 * t2 == t12
for basis_vector in tuple(L_eich2.basis()):
    assert (t1 * t2)(basis_vector) == t12(basis_vector)
