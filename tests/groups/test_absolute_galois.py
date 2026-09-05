import pytest

from sage.misc.unknown import Unknown
from sage.categories.homset import Homset
from sage.rings.finite_rings.integer_mod_ring import Integers

from dzack_research.preamble.all import GF, NumberField, PolynomialRing, QQ, QuadraticField
from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
    OpenAbsoluteGaloisSubgroup,
)
from dzack_research.preamble.categories.group.profinite.absolute_galois_groups import (
    AbsoluteGaloisGroups,
    AbsoluteGaloisGroupsOfFiniteFields,
    OpenAbsoluteGaloisSubgroups,
)
from dzack_research.preamble.categories.group.profinite.field_morphisms import (
    ExactFieldMorphism,
    exact_embeddings,
    exact_field_homset,
    field_generators,
)
from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
    PrimeProlongation,
)
from dzack_research.preamble.categories.group.profinite.galois_quotient import (
    GaloisRestrictionMap,
    extensions_along,
    restrict_along,
)
from dzack_research.preamble.categories.sets import Sets


def _quadratic_number_field(radicand, name="a"):
    return QuadraticField(radicand, name)


def test_absolute_galois_surface_is_publicly_exported() -> None:
    from dzack_research.preamble import all as preamble

    assert preamble.AbsoluteGaloisGroup is AbsoluteGaloisGroup
    assert preamble.ExactFieldMorphism is ExactFieldMorphism
    assert preamble.OpenAbsoluteGaloisSubgroups is OpenAbsoluteGaloisSubgroups
    assert preamble.PrimeProlongation is PrimeProlongation


def _cubic_number_field(radicand, name="a"):
    polynomial_ring = PolynomialRing(QQ, "x")
    x = polynomial_ring.algebra_generator("x")
    return NumberField(x**3 - QQ(radicand), name)


def test_absolute_galois_group_is_the_slice_automorphism_group_with_exact_maps() -> (
    None
):
    field = GF(9, "u")
    group = AbsoluteGaloisGroup(field)
    embedding = group.base_embedding()
    extension_object = group.extension_object()

    assert group in AbsoluteGaloisGroups()
    assert group in AbsoluteGaloisGroupsOfFiniteFields()
    assert group in OwnedGroups()
    u = field.multiplicative_generator()
    assert embedding(field.one()) == group.algebraic_closure().one()
    assert embedding(u + u) == embedding(u) + embedding(u)
    assert embedding(u * u) == embedding(u) * embedding(u)
    assert embedding.domain() is field
    assert embedding.codomain() is group.algebraic_closure()
    assert extension_object.arrow() is embedding
    assert extension_object in group.slice_category()

    frobenius = group.frobenius()
    degree_four = group.finite_extension(4)
    alpha = degree_four.embedding()(field_generators(degree_four.field())[0])
    base_generator = field_generators(field)[0]
    square = group.slice_automorphism(frobenius)

    assert frobenius.parent() is group
    assert frobenius.domain() is group.algebraic_closure()
    assert frobenius.codomain() is group.algebraic_closure()
    assert frobenius(alpha) == alpha**9
    assert frobenius(alpha) != alpha**3
    assert frobenius(embedding(base_generator)) == embedding(base_generator)
    assert square.domain() is extension_object
    assert square.codomain() is extension_object
    assert square.right() is frobenius.as_morphism()
    assert square.left()(base_generator) == base_generator
    assert (~frobenius * frobenius)(alpha) == alpha
    assert square * group.slice_automorphism(frobenius**2) == group.slice_automorphism(
        frobenius**3
    )
    assert ~square == group.slice_automorphism(~frobenius)
    assert group.slice_automorphism(group.one()) * square == square
    assert tuple(group.topological_group_generators()) == (frobenius,)

    field_endomorphisms = group.arrow_set()
    assert not isinstance(group, Homset)
    assert field_endomorphisms in group.super_categories()
    assert frobenius.as_morphism().parent() is field_endomorphisms
    assert frobenius in group
    assert frobenius.as_morphism() in group


def test_exact_closure_maps_do_not_enumerate_infinite_generators_or_admit_set_maps() -> (
    None
):
    group = AbsoluteGaloisGroup(QQ)
    closure = group.algebraic_closure()
    homset = exact_field_homset(closure, closure)
    identity = homset.identity()
    same_identity = homset.identity()
    separate_identity = exact_field_homset(closure, closure).identity()

    assert identity == same_identity
    assert hash(identity) == hash(same_identity)
    assert identity == separate_identity
    assert hash(identity) == hash(separate_identity)
    identity_element = group(separate_identity)
    assert identity_element == group.one()
    assert ~identity_element * identity_element == group.one()


    fake_map = Sets().Mor(closure, closure)(lambda element: closure.one()
        if element == closure.one()
        else closure.zero())
    with pytest.raises(TypeError, match="genuine field-homomorphism"):
        exact_field_homset(closure, closure)(fake_map)


def test_only_known_group_size_and_conjugacy_claims_are_decided() -> None:
    finite_group = AbsoluteGaloisGroup(GF(5))
    frobenius = finite_group.frobenius()
    conjugacy_class = frobenius.conjugacy_class()

    assert finite_group.is_finite() is False
    assert finite_group.is_finitely_generated() is False
    assert frobenius in conjugacy_class
    assert frobenius**2 not in conjugacy_class

    rational_group = AbsoluteGaloisGroup(QQ)
    assert rational_group.is_finite() is Unknown
    assert rational_group.order() is Unknown
    assert rational_group.is_finitely_generated() is Unknown
    with pytest.raises(NotImplementedError, match="conjugacy membership"):
        rational_group.one() in rational_group.one().conjugacy_class()


def test_finite_coordinates_restriction_maps_and_extension_cosets_obey_their_laws() -> (
    None
):
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    degree_two = group.finite_extension(2)
    degree_four = group.finite_extension(4)
    quotient_two = group.finite_quotient(degree_two)
    quotient_four = group.finite_quotient(degree_four)
    restriction_two = group.restriction_map(degree_two)
    restriction_four = group.restriction_map(degree_four)

    assert quotient_two.order() == 2
    assert quotient_four.order() == 4
    with pytest.raises(ValueError, match="outside this finite quotient"):
        quotient_two(-1)
    with pytest.raises(ValueError, match="outside this finite quotient"):
        quotient_two(quotient_two.order())
    assert restriction_four.is_continuous()
    assert restriction_four.is_surjective()
    assert restriction_four(frobenius**3 * frobenius**2) == (
        restriction_four(frobenius**3) * restriction_four(frobenius**2)
    )

    smaller_generator = field_generators(degree_two.field())[0]
    compatible_embeddings = [
        embedding
        for embedding in exact_embeddings(degree_two.field(), degree_four.field())
        if degree_four.embedding()(embedding(smaller_generator))
        == degree_two.embedding()(smaller_generator)
    ]
    assert len(compatible_embeddings) == 1
    inclusion = compatible_embeddings[0]
    sigma = restriction_four(frobenius)
    tau = restriction_two(frobenius)

    assert restrict_along(sigma.action(), inclusion) == tau.action()
    extensions = extensions_along(
        tau.action(),
        inclusion,
        [candidate.action() for candidate in quotient_four],
    )
    assert extensions.cardinality() == 2
    assert sigma.action() in extensions

    coset = group.lifts(restriction_four(frobenius**3))
    kernel = coset.kernel()
    assert kernel.index() == 4
    assert kernel.is_normal()
    assert frobenius not in kernel
    assert frobenius**4 in kernel
    assert frobenius**3 in coset
    assert coset.representative() == frobenius**3


def test_number_field_restriction_fiber_is_a_coset_without_a_false_chosen_lift() -> (
    None
):
    group = AbsoluteGaloisGroup(QQ)
    field = _quadratic_number_field(2)
    stage = group.extension_data(field)
    quotient = group.finite_quotient(stage)
    nontrivial = next(element for element in quotient if element != quotient.one())
    coset = group.lifts(nontrivial)

    assert group.is_abelian() is Unknown
    assert stage.degree() == 2
    assert quotient.order() == 2
    assert coset.finite_automorphism() == nontrivial
    assert coset.extension() is stage
    assert coset.kernel().index() == 2
    assert group.one() not in coset
    with pytest.raises(ValueError, match="extension coset"):
        group.lift(nontrivial)
    with pytest.raises(ValueError, match="no canonically selected representative"):
        coset.representative()


def test_extension_data_extends_a_nondefault_chosen_base_embedding() -> None:
    base_field = _cubic_number_field(2, "a")
    closure = AbsoluteGaloisGroup(QQ).algebraic_closure()
    chosen_base_embedding = exact_embeddings(base_field, closure)[1]
    group = AbsoluteGaloisGroup(
        base_field,
        closure=closure,
        embedding=chosen_base_embedding,
    )
    polynomial_ring = PolynomialRing(base_field, "y")
    y = polynomial_ring.algebra_generator("y")
    extension_field = base_field.extension(y**2 - base_field(3), "b")
    stage = group.extension_data(extension_field)

    assert stage.degree() == 2
    assert group.finite_quotient(stage).order() == 2
    assert all(
        stage.embedding()(stage.base_embedding()(generator))
        == chosen_base_embedding(generator)
        for generator in field_generators(base_field)
    )

    foreign_group = AbsoluteGaloisGroup(
        base_field,
        closure=closure,
        embedding=exact_embeddings(base_field, closure)[0],
    )
    quotient = group.finite_quotient(stage)
    finite_automorphism = quotient.one()
    for operation in (
        lambda: foreign_group.extension_data(stage),
        lambda: foreign_group.open_subgroup(stage),
        lambda: OpenAbsoluteGaloisSubgroup(foreign_group, stage),
        lambda: GaloisRestrictionMap(foreign_group, quotient),
        lambda: foreign_group.lift(finite_automorphism),
        lambda: foreign_group.lifts(finite_automorphism),
    ):
        with pytest.raises(ValueError, match="different realization"):
            operation()


def test_open_subgroups_are_actual_subgroups_and_classes_forget_the_embedding() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    index_two = group.open_subgroup(group.finite_extension(2))
    index_three = group.open_subgroup(group.finite_extension(3))
    intersection = index_two.intersection(index_three)

    assert index_two in OpenAbsoluteGaloisSubgroups()
    assert index_two.supergroup() is group
    assert index_two.supergroup() is group
    assert index_two.index() == 2
    assert frobenius not in index_two
    assert frobenius**2 in index_two
    assert index_two.inclusion()(index_two.frobenius()) == frobenius**2
    assert intersection.index() == 6
    assert intersection <= index_two
    assert intersection <= index_three

    conjugacy_class = index_two.conjugacy_class()
    assert conjugacy_class == group.open_subgroup_class(index_two.fixed_field())
    assert conjugacy_class.index() == 2
    assert conjugacy_class.representative().index() == 2

    first_quadratic = group.open_subgroup_class(group.finite_extension(2))
    assert first_quadratic == conjugacy_class


def test_open_subgroup_classes_compare_the_K_extension_not_field_parent_identity() -> (
    None
):
    group = AbsoluteGaloisGroup(QQ)
    first = group.open_subgroup_class(_quadratic_number_field(2, "a"))
    second = group.open_subgroup_class(_quadratic_number_field(2, "b"))

    assert first == second
    assert hash(first) == hash(second)


def test_core_of_a_nonnormal_open_subgroup_is_the_normal_closure_subgroup() -> None:
    group = AbsoluteGaloisGroup(QQ)
    subgroup = group.open_subgroup(_cubic_number_field(2))
    core = subgroup.core()

    assert subgroup.index() == 3
    assert not subgroup.is_normal()
    assert core.index() == 6
    assert core.is_normal()
    assert core <= subgroup


def test_decomposition_inertia_and_frobenius_project_to_exact_finite_objects() -> None:
    group = AbsoluteGaloisGroup(QQ)
    field = _quadratic_number_field(5)
    stage = group.extension_data(field)
    quotient = group.finite_quotient(stage)
    prime_above_two = field.primes_above(2)[0]
    prolongation = PrimeProlongation(2, lambda extension: prime_above_two)

    decomposition = group.decomposition_group(2, prolongation=prolongation)
    inertia = group.inertia_group(2, prolongation=prolongation)
    decomposition_image = decomposition.image(quotient)
    inertia_image = inertia.image(quotient)
    frobenius_image = group.frobenius_class(2).image(quotient, prime_above_two)

    assert decomposition_image.order() == 2
    assert inertia_image.order() == 1
    assert frobenius_image.representative() != quotient.one()
    assert frobenius_image == group.frobenius_class(2).image(quotient, prime_above_two)
    assert decomposition.conjugacy_class() == group.decomposition_group_class(2)
    assert inertia.conjugacy_class() == group.inertia_group_class(2)
    assert (
        group.decomposition_group_class(2)
        .representative(prolongation)
        .image(quotient)
        .order()
        == 2
    )


def test_continuous_characters_factor_through_finite_quotients_and_are_homomorphisms() -> (
    None
):
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    cyclotomic = group.cyclotomic_character(3)
    quadratic = group.quadratic_character(2)

    for character in (cyclotomic, quadratic):
        assert character.is_continuous()
        assert character.factor_extension().degree() == 2
        assert character(frobenius**5) == character(frobenius**2) * character(
            frobenius**3
        )
        assert character(group.one()) == character.codomain().one()
        assert character.kernel().index() == 2
        assert frobenius not in character.kernel()
        assert frobenius**2 in character.kernel()

    field_nine = AbsoluteGaloisGroup(GF(9, "u"))
    chi_five = field_nine.cyclotomic_character(5)
    assert chi_five(field_nine.frobenius()).value() == Integers(5)(4)


def test_quadratic_kummer_character_does_not_install_a_false_characteristic_two_formula() -> (
    None
):
    group = AbsoluteGaloisGroup(GF(4, "u"))
    with pytest.raises(ValueError, match="characteristic different from two"):
        group.quadratic_character(field_generators(group.base_field())[0])
