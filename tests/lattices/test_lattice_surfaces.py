import pytest

from dzack_research.preamble.all import (
    AA,
    BasedFreeModule,
    FinitelyGeneratedModules,
    FinitelyPresentedAlgebras,
    FractionalIdeals,
    FramedModules,
    Groups,
    Ideals,
    Lattices,
    module_homset,
    ModuleSubobjects,
    NumberField,
    NumberFieldsWithChosenPrimitiveElement,
    OwnedNumberFields,
    OwnedOrders,
    PolynomialRing,
    ProjectiveModules,
    QQ,
    QuadraticField,
    RestrictedScalarsModules,
    Set,
    tensor,
    ZZ,
    signature_pair,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_zz_owns_ideals_and_is_the_ring_of_integers_of_qq() -> None:
    ideal = ZZ.ideal(6)
    assert ideal in Ideals(ZZ)
    assert ideal.principal_generator() == 6
    assert ideal.inclusion().domain() is ideal
    assert ideal.inclusion().codomain().base_ring() is ZZ

    order = QQ.ring_of_integers()
    assert order is ZZ
    assert order in OwnedOrders()


def test_fractional_ideal_is_a_module_subobject_of_the_fraction_field() -> None:
    ideal = ZZ.fractional_ideal(QQ(2) / 3)
    assert ideal in FractionalIdeals(ZZ)
    assert ideal.principal_generator() == QQ(2) / 3

    inverse = ~ideal
    assert inverse.principal_generator() == QQ(3) / 2
    assert (ideal * inverse).principal_generator() == 1

    image = ideal.inclusion()(ideal.module_generator(0))
    assert ideal.inclusion().is_in_image(image)


def test_subobject_orthogonal_complement_defers_to_the_inclusion() -> None:
    lattice = Lattices(ZZ)(3)
    e0, e1, e2 = lattice.module_generators()
    subobject = lattice.subobject_on((e0 + e1,))

    perpendicular = subobject.orthogonal_complement()
    via_inclusion = subobject.inclusion().orthogonal_complement()

    assert perpendicular.inclusion().codomain() is lattice
    assert via_inclusion.inclusion().codomain() is lattice
    assert perpendicular.module_rank() == 2
    assert all(
        subobject.inclusion()(source).b(perpendicular.inclusion()(target)) == 0
        for source in subobject.module_generators()
        for target in perpendicular.module_generators()
    )
    assert perpendicular.inclusion().is_in_image(e0 - e1)
    assert perpendicular.inclusion().is_in_image(e2)


def test_saturation_is_the_primitive_closure_of_an_inclusion() -> None:
    lattice = Lattices(ZZ)(2)
    e0 = lattice.module_generator(0)
    subobject = lattice.subobject_on((2 * e0,))

    assert not subobject.is_primitive()
    saturation = subobject.saturation()

    assert saturation.inclusion().codomain() is lattice
    assert saturation.is_primitive()
    assert saturation.inclusion().is_in_image(e0)


def test_radical_and_isotropic_reduction_are_inclusion_derived() -> None:
    lattice = Lattices(ZZ)([[0, 0], [0, 1]])
    e0, e1 = lattice.module_generators()

    radical = lattice.radical()
    assert radical.module_rank() == 1
    assert radical.inclusion().is_in_image(e0)
    assert not radical.inclusion().is_in_image(e1)

    quotient = lattice.radical_quotient()
    assert quotient.module_rank() == 1
    assert quotient.gram_tensor()[0, 0] == 1

    plane = Lattices(ZZ)("U")
    isotropic_line = plane.subobject_on((plane.module_generator(0),))
    reduction = isotropic_line.isotropic_reduction()
    assert reduction.module_rank() == 0


def test_reflections_are_lattice_automorphisms_with_inverse_and_composition() -> None:
    plane = Lattices(ZZ)("U")
    e, f = plane.module_generators()
    reflection = plane.reflection(e + f)
    automorphisms = plane.Aut()

    assert reflection.parent() is automorphisms
    assert automorphisms.one().parent() is automorphisms
    for vector in (e, f):
        assert (~reflection)(reflection(vector)) == vector
        assert (reflection * reflection)(vector) == vector


def test_discriminant_class_constructs_an_overlattice_inclusion() -> None:
    lattice = Lattices(ZZ)([[8]])
    discriminant = lattice.discriminant_module()
    class_generator = discriminant.module_generator(
        next(iter(discriminant.module_generating_set()))
    )

    inclusion = lattice.overlattice(4 * class_generator)

    assert inclusion.domain() is lattice
    assert inclusion.index() == 2
    assert inclusion.codomain().gram_tensor()[0, 0] == 2


def test_number_field_properties_selected_primitive_element_and_order_are_distinct() -> None:
    field = QuadraticField(2, "a")
    assert field in OwnedNumberFields()
    assert field in NumberFieldsWithChosenPrimitiveElement()
    assert field.degree() == 2
    assert field.embeddings(AA).cardinality() == 2

    order = field.ring_of_integers()
    assert order in OwnedOrders()
    assert order.base_ring() is ZZ
    assert order.integral_basis().cardinality() == 2

    algebra = field.as_algebra()
    assert algebra is not field
    assert algebra.base_ring() is QQ
    assert algebra in FinitelyPresentedAlgebras(QQ)


def test_galois_group_does_not_mean_the_normal_closure_group() -> None:
    polynomial_ring = PolynomialRing(QQ, "x")
    x = polynomial_ring.algebra_generator("x")
    field = NumberField(x**3 - 2, "a")

    assert not field.is_galois()
    with pytest.raises(ValueError, match="normal_closure_galois_group"):
        field.galois_group()


def test_orthogonal_complement_uses_the_image_of_an_arbitrary_morphism() -> None:
    source = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    plane = Lattices(ZZ)("U")
    e, f = plane.module_generators()
    morphism = module_homset(source, plane)({"x": e, "y": e})

    perpendicular = morphism.orthogonal_complement()

    assert perpendicular.module_rank() == 1
    assert perpendicular.gram_tensor() == tensor(ZZ, (), (1, 1), [[0]])
    assert perpendicular.inclusion().is_in_image(e)
    assert not perpendicular.inclusion().is_in_image(f)


def test_isotropic_reduction_of_a_line_in_u_plus_u_is_u() -> None:
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("U")
    isotropic_vector = lattice.module_generators().unrank(0)
    isotropic_line = lattice.subobject_on((isotropic_vector,))

    reduction = isotropic_line.isotropic_reduction()

    assert reduction.module_rank() == 2
    assert reduction.gram_tensor() == tensor(ZZ, (), (2, 2), [[0, 1], [1, 0]])
    assert reduction.signature_pair() == signature_pair(1, 1)
    assert reduction.is_unimodular()


def test_primitive_a1_and_a2_complements_in_e8_have_e7_and_e6_discriminants() -> None:
    e8 = Lattices(ZZ)("E8")
    module_generators = e8.module_generators()

    a1 = e8.subobject_on((module_generators.unrank(0),))
    e7 = a1.orthogonal_complement()

    assert a1.is_primitive()
    assert e7.is_primitive()
    assert e7.module_rank() == 7
    assert abs(e7.determinant()) == 2
    e7_factors = e7.discriminant_module().invariant_factors()
    assert e7_factors.cardinality() == 1
    assert e7_factors.unrank(0) == 2

    adjacent_pair = next(
        (module_generators.unrank(left_position), module_generators.unrank(right_position))
        for left_position in range(int(module_generators.cardinality()))
        for right_position in range(left_position + 1, int(module_generators.cardinality()))
        if module_generators.unrank(left_position).b(
            module_generators.unrank(right_position)
        ) != 0
    )
    a2 = e8.subobject_on(adjacent_pair)
    e6 = a2.orthogonal_complement()

    assert a2.is_primitive()
    assert e6.is_primitive()
    assert e6.module_rank() == 6
    assert abs(e6.determinant()) == 3
    e6_factors = e6.discriminant_module().invariant_factors()
    assert e6_factors.cardinality() == 1
    assert e6_factors.unrank(0) == 3


def test_diagonal_isotropic_class_glues_a1_four_to_an_index_two_even_overlattice() -> None:
    a1 = Lattices(ZZ)("A1")
    lattice = a1 + a1 + a1 + a1
    discriminant = lattice.discriminant_module()

    factors = discriminant.invariant_factors()
    assert factors.cardinality() == 4
    assert all(factor == 2 for factor in factors)
    diagonal_class = sum(discriminant.module_generators(), discriminant.zero())

    assert diagonal_class.additive_order() == 2
    assert diagonal_class.q() == discriminant.quadratic_value_module().zero()

    inclusion = lattice.overlattice(diagonal_class)
    overlattice = inclusion.codomain()

    assert inclusion.index() == 2
    assert overlattice.module_rank() == 4
    assert overlattice.is_even()
    assert abs(overlattice.determinant()) == 4
    overlattice_factors = overlattice.discriminant_module().invariant_factors()
    assert overlattice_factors.cardinality() == 2
    assert all(factor == 2 for factor in overlattice_factors)


def test_quadratic_integer_ideals_compute_as_order_modules_inside_the_field() -> None:
    field = QuadraticField(5, "a")
    order = field.ring_of_integers()
    order_basis = tuple(order.integral_basis())

    integral_ideal = order.ideal(2)
    assert integral_ideal.module_generating_set().cardinality() == 1
    assert integral_ideal.is_principal()
    assert order(integral_ideal.principal_generator() / 2).is_unit()
    assert all(
        2 * basis_element in integral_ideal
        for basis_element in order_basis
    )

    half_order = order.fractional_ideal(field(QQ(1) / 2))
    inverse = ~half_order
    product = half_order * inverse

    assert product.is_principal()
    assert product.principal_generator().is_unit()

    module_generator = half_order.module_generator(
        next(iter(half_order.module_generating_set()))
    )
    image = half_order.inclusion()(module_generator)
    assert image.parent() is half_order.inclusion().codomain()
    assert image.parent() is not half_order
    assert half_order.inclusion().lift(image) == module_generator


def test_nonprincipal_ideal_in_q_sqrt_minus_five_has_a_computable_fractional_inverse() -> None:
    field = QuadraticField(-5, "a")
    a = field.primitive_element()
    order = field.ring_of_integers()
    ideal = order.ideal(2, 1 + a)

    assert field.class_number() == 2
    assert not ideal.is_principal()
    assert ideal in ProjectiveModules(order)
    assert order(2) in ideal
    assert order(1 + a) in ideal
    assert order.one() not in ideal

    inverse = ~ideal
    assert not inverse.is_principal()
    assert inverse in ProjectiveModules(order)

    product = ideal * inverse
    assert product.is_principal()
    assert product.principal_generator().is_unit()
    assert order.one() in product


def test_fractional_ideal_of_a_nonmaximal_order_uses_that_order_not_the_maximal_order() -> None:
    field = QuadraticField(5, "a")
    a = field.primitive_element()
    order = field.order_generated_by(a)

    assert not order.is_maximal()
    assert order in OwnedOrders()
    half_order = order.fractional_ideal(field(QQ(1) / 2))

    assert half_order in FractionalIdeals(order)
    assert half_order in ModuleSubobjects(order)
    assert half_order in FramedModules(order)
    assert half_order in FinitelyGeneratedModules(order)
    assert half_order in ProjectiveModules(order)

    underlying_integer_module = half_order.restrict_scalars(
        order._ring_morphism_defining_algebra_structure()
    )
    assert underlying_integer_module in RestrictedScalarsModules(ZZ)
    assert underlying_integer_module in FramedModules(ZZ)
    assert underlying_integer_module in FinitelyGeneratedModules(ZZ)
    assert underlying_integer_module.module_generating_set().cardinality() == 2
    selected_generator = half_order.module_generator(
        next(iter(half_order.module_generating_set()))
    )
    restricted_generator = underlying_integer_module(selected_generator)
    assert restricted_generator.underlying_element() == selected_generator

    assert field(QQ(1) / 2) in half_order
    assert a / 2 in half_order
    assert (1 + a) / 2 in half_order
    assert (1 + a) / 4 not in half_order

    inverse = ~half_order
    assert inverse.is_principal()
    assert inverse.principal_generator() == 2

    product = half_order * inverse
    assert product.is_principal()
    assert product.principal_generator().is_unit()
    assert order.one() in product

    unit_ideal = order.fractional_ideal(1)
    intersection = half_order.intersection(unit_ideal)
    assert intersection.is_principal()
    assert intersection.principal_generator().is_unit()

    ideal_sum = half_order + unit_ideal
    assert ideal_sum.is_principal()
    assert ideal_sum.principal_generator() == field(QQ(1) / 2)


def test_real_quadratic_field_has_exact_embeddings_and_its_actual_galois_group() -> None:
    field = QuadraticField(5, "a")

    images = tuple(field.embedding_images(AA))
    assert field.embedding_images(AA).cardinality() == 2
    assert all(image**2 == 5 for image in images)
    assert sum(images) == 0
    assert field.ramified_primes() == Set((ZZ(5),))

    galois_group = field.galois_group()
    assert galois_group.cardinality() == field.degree() == 2


def test_swap_involution_on_u_is_an_automorphism_with_rank_one_invariants_and_coinvariants() -> None:
    group = Groups.C(2)
    plane = Lattices(ZZ)("U")

    def swap(group_element, vector):
        if group_element == group.one():
            return vector
        left, right = vector.to_tuple()
        return plane((right, left))

    group_lattice = Lattices(ZZ[group])(plane, swap)
    involution = group_lattice.group().group_generators().unrank(0)

    assert group_lattice.action().domain() is group
    assert group_lattice.action().codomain() is group_lattice.Aut()
    action = group_lattice.action_of(involution)
    assert action.parent() is group_lattice.Aut()
    left, right = group_lattice.module_generators()
    assert action(left) == right
    assert action(right) == left
    assert group_lattice.is_invariant(group_lattice((1, 1)))
    assert not group_lattice.is_invariant(group_lattice((1, -1)))

    invariants = group_lattice.module_invariants()
    coinvariants = group_lattice.module_coinvariants()
    assert invariants.module_rank() == 1
    assert coinvariants.module_rank() == 1
    assert coinvariants.is_torsion_free()


def test_group_lattice_rejects_actions_outside_the_orthogonal_automorphism_hom() -> None:
    group = Groups.C(2)
    plane = Lattices(ZZ)("U")

    def nonisometric_action(group_element, vector):
        if group_element == group.one():
            return vector
        return plane.scalar_multiple(ZZ(2), vector)

    with pytest.raises(ValueError, match="preserve the lattice form"):
        Lattices(ZZ[group])(plane, nonisometric_action)
