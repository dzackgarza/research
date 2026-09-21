
from dzack_research.preamble.all import (
    QQ,
    ZZ,
    Algebras,
    Groups,
    OwnedOrders,
    QuadraticField,
)
from dzack_research.preamble.categories.sets import Sets, finite_ordered_set


def test_algebra_transpose_uses_the_stated_left_adjoint_source() -> None:
    scalar_presentation = QQ.free_module(["s"]).symmetric_algebra()
    s = scalar_presentation.algebra_generator("s")
    extension_ring = (scalar_presentation).quotient_by_relations((s**2 - 2,))
    ring_map = extension_ring.algebra_structure_morphism()

    source_presentation = QQ.free_module(["x"]).symmetric_algebra()
    x = source_presentation.algebra_generator("x")
    source = (source_presentation).quotient_by_relations((x**4 - 2,))

    target_presentation = extension_ring.free_module(["y"]).symmetric_algebra()
    y = target_presentation.algebra_generator("y")
    target = (target_presentation).quotient_by_relations((y**2 - extension_ring.algebra_generator("s"),),
    )

    adjunction = Algebras(QQ).Associative().Unital().base_change_adjunction(ring_map)
    independently_extended = adjunction.left_adjoint()(source)
    morphism = independently_extended.Mor(target)(
        {"x": target.algebra_generator("y")}
    )
    transpose = adjunction.mor_set_isomorphism_forward(morphism, source)
    restricted_target = adjunction.right_adjoint()(target)

    assert transpose.domain() is source
    assert transpose.codomain() is restricted_target
    assert transpose(source.algebra_generator("x")) == restricted_target(
        target.algebra_generator("y")
    )


def test_abelianization_transpose_uses_the_quotient_projection_on_its_domain() -> None:
    group = Groups.S(3)
    target = Groups.C(6)
    target_generator = target.group_generators()[0]
    group_generators = group.group_generators()
    group_morphism = group.Mor(target)(
        {
            group_generators[0]: target.one(),
            group_generators[1]: target_generator**3,
        }
    )

    first_adjunction = Groups().abelianization_adjunction()
    assert first_adjunction.right_adjoint()(target) is target
    factored = first_adjunction.mor_set_isomorphism_inverse(group_morphism, target)
    recovered = first_adjunction.mor_set_isomorphism_forward(factored, group)

    for generator in group_generators:
        assert recovered(generator) == group_morphism(generator)


def test_fraction_field_transpose_is_indexed_by_the_stated_source_order() -> None:
    field = QuadraticField(2, "a")
    maximal_order = field.ring_of_integers()
    nonmaximal_order = field.order_generated_by(2 * field.primitive_element())
    adjunction = OwnedOrders().fraction_field_adjunction()
    fraction_field = adjunction.left_adjoint()

    assert maximal_order is not nonmaximal_order
    assert fraction_field(maximal_order) is field
    assert fraction_field(nonmaximal_order) is field

    identity = field.Mor(field).identity()
    maximal_restriction = adjunction.mor_set_isomorphism_forward(
        identity,
        maximal_order,
    )
    nonmaximal_restriction = adjunction.mor_set_isomorphism_forward(
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

    recovered = adjunction.mor_set_isomorphism_inverse(nonmaximal_restriction, field)
    assert recovered(field.primitive_element()) == field.primitive_element()


def test_free_group_transpose_uses_the_stated_left_adjoint_source() -> None:
    source = finite_ordered_set((ZZ(11), ZZ(13)))
    adjunction = Sets().free_group_adjunction()
    free_group = adjunction.left_adjoint()(source)
    target = Groups.C(3)
    target_generator = target.group_generators()[0]
    generator_map = Sets().Mor(source, target)(lambda point: target_generator if point == 11 else target_generator**2)
    group_morphism = free_group.Mor(target)(generator_map)

    transpose = adjunction.mor_set_isomorphism_forward(group_morphism, source)

    for point in source:
        assert transpose(point) == generator_map(point)
