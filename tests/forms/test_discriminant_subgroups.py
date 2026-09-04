from dzack_research.preamble.all import ZZ, Lattices, signature_pair


def test_finite_torsion_enumeration_uses_smith_generators() -> None:
    discriminant = Lattices(ZZ)("A2").discriminant_module()
    assert discriminant.cardinality() == 3
    assert discriminant.elements().cardinality() == 3
    assert discriminant.cardinality() == 3


def test_a2_discriminant_form_is_anisotropic_and_not_metabolic() -> None:
    discriminant = Lattices(ZZ)("A2").discriminant_module()
    assert discriminant.is_anisotropic()
    assert discriminant.isotropic_subgroups().cardinality() == 1
    assert not discriminant.is_metabolic()


def test_a1_four_has_diagonal_lagrangian_and_primary_component() -> None:
    a1 = Lattices(ZZ)("A1")
    discriminant = (a1 + a1 + a1 + a1).discriminant_module()
    generators = discriminant.smith_form_module_generators()
    diagonal = sum(generators, discriminant.zero())
    subgroup = discriminant.subgroup_on((diagonal,))

    assert subgroup.cardinality() == 2
    assert subgroup.is_isotropic()
    assert discriminant.orthogonal_subgroup(subgroup).cardinality() == 8
    components = discriminant.primary_components()
    assert tuple(components) == (ZZ(2),)
    assert components[ZZ(2)].cardinality() == 16


def test_hyperbolic_discriminant_pair_has_lagrangian() -> None:
    lattice = Lattices(ZZ)([[2, 0], [0, -2]])
    discriminant = lattice.discriminant_module()
    assert discriminant.cardinality() == 4
    lagrangians = discriminant.lagrangian_subgroups()
    assert lagrangians
    assert all(H.cardinality() == 2 and H.is_isotropic() for H in lagrangians)
    assert discriminant.is_metabolic()


def test_orthogonal_quotient_and_overlattice_are_the_nikulin_pair() -> None:
    a1 = Lattices(ZZ)("A1")
    lattice = a1 + a1 + a1 + a1
    discriminant = lattice.discriminant_quadratic_form()
    generators = discriminant.smith_form_module_generators()
    diagonal = sum(generators, discriminant.zero())
    subgroup = discriminant.subgroup_on((diagonal,))

    quotient_form = discriminant.orthogonal_quotient(subgroup)
    inclusion = discriminant.overlattice_from_isotropic_subobject(subgroup)
    enlarged = inclusion.codomain()

    assert subgroup.is_isotropic()
    assert quotient_form.cardinality() == 4
    assert inclusion.index() == 2
    assert abs(enlarged.determinant()) == 4
    assert enlarged.is_even()
    assert enlarged.discriminant_module().cardinality() == quotient_form.cardinality()


def test_local_modification_is_exactly_p_primary_isotropic_glue() -> None:
    a1 = Lattices(ZZ)("A1")
    lattice = a1 + a1 + a1 + a1
    discriminant = lattice.discriminant_quadratic_form()
    diagonal = sum(
        discriminant.smith_form_module_generators(),
        discriminant.zero(),
    )

    inclusion = lattice.local_modification(2, diagonal)

    assert inclusion.index() == 2
    assert inclusion.codomain().is_even()
    assert inclusion.codomain().discriminant_module().cardinality() == 4
    try:
        lattice.local_modification(3, diagonal)
    except ValueError as error:
        assert "p-primary" in str(error)
    else:
        raise AssertionError("a 2-primary glue class was accepted as a 3-local modification")


def test_nonisotropic_glue_is_rejected_before_overlattice_construction() -> None:
    discriminant = Lattices(ZZ)("A1").discriminant_quadratic_form()
    generator = discriminant.smith_form_module_generators().unrank(0)
    subgroup = discriminant.subgroup_on((generator,))

    assert not subgroup.is_isotropic()
    try:
        discriminant.overlattice_from_isotropic_subobject(subgroup)
    except ValueError as error:
        assert "q-isotropic" in str(error)
    else:
        raise AssertionError("non-isotropic glue was accepted")


def test_discriminant_pairing_identifies_the_group_with_its_pontryagin_dual() -> None:
    discriminant = Lattices(ZZ)("A2").discriminant_bilinear_form()
    identification = discriminant.pontryagin_dual_identification()
    generators = discriminant.module_generators()

    character_values = set()
    for element in discriminant.elements():
        character = identification(element)
        values = tuple(character(generator) for generator in generators)
        character_values.add(values)
        assert all(
            character(target) == discriminant.b(element, target)
            for target in discriminant.elements()
        )

    assert len(character_values) == discriminant.cardinality()


def test_brown_invariant_is_the_exact_gauss_sum_phase() -> None:
    positive = Lattices(ZZ)([[2]]).discriminant_quadratic_form()
    negative = Lattices(ZZ)([[-2]]).discriminant_quadratic_form()

    assert positive.brown_invariant() == 1
    assert negative.brown_invariant() == 7


def test_milgram_compatibility_on_even_lattice_discriminant_forms() -> None:
    lattices = (
        Lattices(ZZ)([[2]]),
        Lattices(ZZ)([[-2]]),
        Lattices(ZZ)([[0, 2], [2, 0]]),
        Lattices(ZZ)("A2"),
    )
    for lattice in lattices:
        signature = lattice.signature_pair()
        positive, negative = signature.first(), signature.second()
        signature = int(positive - negative)
        assert lattice.discriminant_quadratic_form().brown_invariant() == signature % 8


def test_elementary_two_adic_u_k_and_v_one_examples() -> None:
    for exponent in (1, 2, 3):
        scale = 2**exponent
        u_k = Lattices(ZZ)([[0, scale], [scale, 0]]).discriminant_quadratic_form()
        assert tuple(u_k.invariant_factors()) == (scale, scale)
        assert u_k.brown_invariant() == 0
        assert not u_k.is_anisotropic()

    v_one = Lattices(ZZ)("D4").discriminant_quadratic_form()
    assert tuple(v_one.invariant_factors()) == (2, 2)
    assert v_one.brown_invariant() == 4
    assert v_one.is_anisotropic()
