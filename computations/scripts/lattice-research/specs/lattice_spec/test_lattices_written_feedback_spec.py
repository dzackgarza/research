"""
Executable spec distilled from the semantic comments and TODOs in
``src/lattices/lattices.py``.

This file intentionally targets the renamed lattice module directly and does
not preserve the retired ``coble_geometry_foundation`` import surface.
"""

from __future__ import annotations

import importlib

from sage.all import QQ, ZZ, IntegralLattice, identity_matrix, matrix, vector

lat = importlib.import_module("src.lattices.lattices")


def q(num: int, den: int = 1):
    return QQ(num) / QQ(den)


class TestArchitectureFromWrittenSpec:
    def test_public_nouns_are_not_sage_subclasses(self):
        native_module_type = type(IntegralLattice("U").ambient_module())
        native_lattice_type = type(IntegralLattice("U"))
        native_disc_type = type(IntegralLattice("A1").discriminant_group())

        assert not issubclass(lat.FreeBilinearModule, native_module_type)
        assert not issubclass(lat.Lattice, native_lattice_type)
        assert not issubclass(lat.DiscriminantGroup, native_disc_type)

    def test_public_object_hierarchy_matches_the_module_spec(self):
        BilinearModule = lat.BilinearModule
        QuadraticModule = lat.QuadraticModule
        FreeBilinearModule = lat.FreeBilinearModule
        TorsionBilinearModule = lat.TorsionBilinearModule
        RationalLattice = lat.RationalLattice
        Lattice = lat.Lattice
        DiscriminantForm = lat.DiscriminantForm
        DualLattice = lat.DualLattice

        assert issubclass(FreeBilinearModule, BilinearModule)
        assert issubclass(RationalLattice, FreeBilinearModule)
        assert issubclass(Lattice, RationalLattice)
        assert issubclass(DualLattice, RationalLattice)
        assert issubclass(DiscriminantForm, TorsionBilinearModule)
        assert issubclass(DiscriminantForm, QuadraticModule)

    def test_public_morphism_hierarchy_matches_the_module_spec(self):
        BilinearModuleHomSpace = lat.BilinearModuleHomSpace
        BilinearModuleMorphism = lat.BilinearModuleMorphism
        LatticeHomSpace = lat.LatticeHomSpace
        RationalLatticeMorphism = lat.RationalLatticeMorphism
        RationalLatticeHomSpace = lat.RationalLatticeHomSpace
        LatticeMorphism = lat.LatticeMorphism

        assert BilinearModuleHomSpace.Element is BilinearModuleMorphism
        assert RationalLatticeHomSpace.Element is RationalLatticeMorphism
        assert issubclass(LatticeHomSpace, RationalLatticeHomSpace)
        assert issubclass(LatticeMorphism, RationalLatticeMorphism)


class TestPromotionAndNamedConstructorsFromWrittenSpec:
    def test_rational_lattice_from_gram_is_the_unique_integrality_promotion_site(self):
        integral = lat.RationalLattice.from_gram(matrix(ZZ, [[-2]]))
        rational = lat.RationalLattice.from_gram(matrix(QQ, [[-1, q(1, 2)], [q(1, 2), -1]]))

        assert isinstance(integral, lat.Lattice)
        assert isinstance(rational, lat.RationalLattice)
        assert not isinstance(rational, lat.Lattice)

    def test_named_family_constructors_use_semantic_family_names(self):
        f4 = lat.Lattice.F4()
        g2 = lat.Lattice.G2()
        rational_f4 = lat.RationalLattice.F4()

        assert isinstance(rational_f4, lat.RationalLattice)
        assert not isinstance(rational_f4, lat.Lattice)
        assert f4 == rational_f4
        assert isinstance(g2, lat.Lattice)
        assert g2.gram_matrix() == matrix(ZZ, [[-2, 3], [3, -6]])


class TestElementSemanticsFromWrittenSpec:
    def test_named_generators_have_exact_coordinate_semantics(self):
        U = lat.Lattice.U()
        e1, e2 = tuple(U.gens())

        assert e1.to_vector() == vector(ZZ, [1, 0])
        assert e2.to_vector() == vector(ZZ, [0, 1])
        assert U.element_from(vector(ZZ, [-1, 2])) == -e1 + 2 * e2
        assert e1 * e1 == 0
        assert e1.is_isotropic()
        assert e1.perp() == e1.span()

    def test_scale_rescale_and_twist_are_distinct_semantics(self):
        Z = lat.Lattice.Z()
        A1 = lat.Lattice.A(1)

        assert Z.scale() == 1
        assert A1.scale() == 2
        assert Z.rescale(2).gram_matrix() == matrix(ZZ, [[2]])
        assert Z.twist(2).gram_matrix() == matrix(ZZ, [[2]])
        assert lat.Lattice.U().twist(q(1, 2)).gram_matrix() == matrix(QQ, [[0, q(1, 2)], [q(1, 2), 0]])


class TestDualAndDiscriminantSemanticsFromWrittenSpec:
    def test_integral_elements_project_trivially_but_dual_elements_project_nontrivially(self):
        U2 = lat.Lattice.U().rescale(2)
        e, f = tuple(U2.gens())
        A = U2.discriminant_group()
        dual = U2.dual()
        e_dual, f_dual = tuple(dual.gens())

        assert isinstance(dual, lat.DualLattice)
        assert e.discriminant_class() == A.zero()
        assert f.discriminant_class() == A.zero()
        assert e_dual.discriminant_class() in set(A.gens())
        assert f_dual.discriminant_class() in set(A.gens())
        assert A.q(e_dual.discriminant_class()) == 0
        assert A.q(f_dual.discriminant_class()) == 0
        assert A.b(e_dual.discriminant_class(), f_dual.discriminant_class()) == q(1, 2)

    def test_mixed_zz_module_and_qq_valued_subobjects_stay_generic(self):
        U2 = lat.Lattice.U().rescale(2)
        dual = U2.dual()
        submodule = dual.span((next(iter(dual.gens())),))
        quotient = dual.quotient_by(submodule)

        assert isinstance(submodule, lat.FreeBilinearModule)
        assert isinstance(quotient, lat.FreeBilinearModule)
        assert submodule.base_ring() is ZZ
        assert quotient.base_ring() is ZZ
        assert submodule.value_ring() is QQ
        assert quotient.value_ring() is QQ

    def test_discriminant_form_uses_isometry_language_and_semantic_value_maps(self):
        A2_disc = lat.Lattice.A(2).discriminant_group()
        expected = lat.DiscriminantForm.from_invariants_and_gram((3,), [[q(-2, 3)]])
        (g,) = tuple(A2_disc.gens())

        assert A2_disc.is_isometric_to(expected)
        assert A2_disc.isomorphic_as_groups(expected)
        assert A2_disc.q(g) == q(-2, 3)


class TestMorphismAndSubobjectSemanticsFromWrittenSpec:
    def test_hom_returns_a_homspace_with_semantic_constructors(self):
        U = lat.Lattice.U()
        homspace = U.hom(U)
        identity = homspace.element_from_dict({g: g for g in U.gens()})

        assert homspace.Element is lat.LatticeMorphism
        assert identity.to_matrix() == matrix(ZZ, [[1, 0], [0, 1]])
        assert identity in homspace

    def test_images_kernels_cokernels_and_primitivity_live_on_morphisms(self):
        U = lat.Lattice.U()
        U2 = U.rescale(2)
        ambient = U + U2
        iota_U, iota_U2 = ambient.embeddings

        assert iota_U.image() == ambient.span(tuple(iota_U(g) for g in U.gens()))
        assert iota_U.is_primitive()
        assert iota_U.cokernel().is_isometric_to(U2)
        assert iota_U.image().perp() == iota_U2.image()

    def test_orthogonal_complements_are_expressed_via_inclusions_not_bare_lattices(self):
        U = lat.Lattice.U()
        U2 = U.rescale(2)
        ambient = U + U2
        iota_U, iota_U2 = ambient.embeddings

        assert iota_U.image().perp() == iota_U2.image()
        assert iota_U2.image().perp() == iota_U.image()


class TestGroupSemanticsFromWrittenSpec:
    def test_orthogonal_group_uses_column_action_and_exact_membership(self):
        U = lat.Lattice.U()
        e1, e2 = tuple(U.gens())
        swap = matrix(ZZ, [[0, 1], [1, 0]])
        O = U.orthogonal_group()

        assert swap in O
        assert O.act(swap, e1.to_vector()) == e2.to_vector()
        assert O.act(swap, e2.to_vector()) == e1.to_vector()

    def test_discriminant_kernel_and_centralizer_semantics_remain_structural(self):
        U = lat.Lattice.U()
        minus_identity = -identity_matrix(ZZ, 2)
        centralizer = U.orthogonal_group().centralizer(minus_identity)
        kernel = centralizer.kernel_of_discriminant_action()

        assert minus_identity in centralizer
        assert identity_matrix(ZZ, 2) in kernel
        assert identity_matrix(ZZ, 2) in centralizer.special_orthogonal_subgroup()
