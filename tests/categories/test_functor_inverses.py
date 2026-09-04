
from dzack_research.preamble.all import (
    AbelianizationAdjunction,
    AlgebraBaseChangeAdjunction,
    AlgebraScalarExtensionFunctor,
    FinitelyPresentedAlgebra,
    FreeGroupUnderlyingSetAdjunction,
    Groups,
    OrderNumberFieldAdjunction,
    QQ,
    QuadraticField,
    SymmetricAlgebraOn,
    ZZ,
    group_homset,
)
from dzack_research.preamble.categories.rings.embeddings import number_field_homset
from dzack_research.preamble.categories.sets import Sets, finite_ordered_set


def test_algebra_transpose_uses_the_scalar_extension_construction_source() -> None:
    scalar_presentation = SymmetricAlgebraOn(QQ, ["s"])
    s = scalar_presentation.algebra_generator("s")
    extension_ring = FinitelyPresentedAlgebra(scalar_presentation, (s**2 - 2,))
    ring_map = extension_ring.algebra_structure_morphism()

    source_presentation = SymmetricAlgebraOn(QQ, ["x"])
    x = source_presentation.algebra_generator("x")
    source = FinitelyPresentedAlgebra(source_presentation, (x**4 - 2,))

    target_presentation = SymmetricAlgebraOn(extension_ring, ["y"])
    y = target_presentation.algebra_generator("y")
    target = FinitelyPresentedAlgebra(
        target_presentation,
        (y**2 - extension_ring.algebra_generator("s"),),
    )

    independently_extended = AlgebraScalarExtensionFunctor(ring_map)(source)
    morphism = independently_extended.Mor(target)(
        {"x": target.algebra_generator("y")}
    )
    adjunction = AlgebraBaseChangeAdjunction(ring_map)
    transpose = adjunction.hom_set_isomorphism_forward(morphism)
    restricted_target = adjunction.right_adjoint()(target)

    assert transpose.domain() is source
    assert transpose.codomain() is restricted_target
    assert transpose(source.algebra_generator("x")) == restricted_target(
        target.algebra_generator("y")
    )


def test_abelianization_transpose_uses_the_quotient_projection_on_its_domain() -> None:
    group = Groups.S(3)
    target = Groups.C(6)
    target_generator = target.group_generators().unrank(0)
    group_generators = group.group_generators()
    group_morphism = group_homset(group, target)(
        {
            group_generators[0]: target.one(),
            group_generators[1]: target_generator**3,
        }
    )

    first_adjunction = AbelianizationAdjunction()
    factored = first_adjunction.hom_set_isomorphism_inverse(group_morphism)
    recovered = AbelianizationAdjunction().hom_set_isomorphism_forward(factored)

    for generator in group_generators:
        assert recovered(generator) == group_morphism(generator)


def test_fraction_field_transpose_is_indexed_by_the_stated_source_order() -> None:
    field = QuadraticField(2, "a")
    maximal_order = field.ring_of_integers()
    nonmaximal_order = field.order_generated_by(2 * field.primitive_element())
    adjunction = OrderNumberFieldAdjunction()
    fraction_field = adjunction.left_adjoint()

    assert maximal_order is not nonmaximal_order
    assert fraction_field(maximal_order) is field
    assert fraction_field(nonmaximal_order) is field

    identity = number_field_homset(field, field).identity()
    maximal_restriction = adjunction.hom_set_isomorphism_forward(
        identity,
        maximal_order,
    )
    nonmaximal_restriction = adjunction.hom_set_isomorphism_forward(
        identity,
        nonmaximal_order,
    )

    assert maximal_restriction.domain() is maximal_order
    assert nonmaximal_restriction.domain() is nonmaximal_order
    assert maximal_restriction.codomain() is maximal_order
    assert nonmaximal_restriction.codomain() is maximal_order
    for basis_element in nonmaximal_order.integral_basis():
        assert nonmaximal_restriction(basis_element) == maximal_order(
            basis_element
        )

    recovered = adjunction.hom_set_isomorphism_inverse(nonmaximal_restriction)
    assert recovered(field.primitive_element()) == field.primitive_element()


def test_free_group_transpose_reads_the_intrinsic_index_set() -> None:
    source = finite_ordered_set((ZZ(11), ZZ(13)))
    free_group = Groups.Free(index_set=source)
    target = Groups.C(3)
    target_generator = target.group_generators().unrank(0)
    generator_map = Sets().hom(source, target)(lambda point: target_generator if point == 11 else target_generator**2)
    group_morphism = group_homset(free_group, target)(generator_map)

    transpose = FreeGroupUnderlyingSetAdjunction().hom_set_isomorphism_forward(
        group_morphism
    )

    for point in source:
        assert transpose(point) == generator_map(point)
