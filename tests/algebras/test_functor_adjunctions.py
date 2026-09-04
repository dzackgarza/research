from dzack_research.preamble.all import (
    AlgebraRestrictionOfScalarsFunctor,
    FinitelyPresentedAlgebra,
    FramedAlgebras,
    QQ,
    SymmetricAlgebraOn,
    ZZ,
    algebra_base_change_adjunction,
)
from dzack_research.preamble.categories.rings import ring_homset


def _quadratic_algebra_tower():
    scalar_presentation = SymmetricAlgebraOn(QQ, ["s"])
    s = scalar_presentation.algebra_generator("s")
    extension_ring = FinitelyPresentedAlgebra(
        scalar_presentation,
        (s**2 - 2,),
    )
    ring_map = extension_ring.algebra_structure_morphism()

    source_presentation = SymmetricAlgebraOn(QQ, ["x"])
    x = source_presentation.algebra_generator("x")
    source = FinitelyPresentedAlgebra(
        source_presentation,
        (x**4 - 2,),
    )

    target_presentation = SymmetricAlgebraOn(extension_ring, ["y"])
    y = target_presentation.algebra_generator("y")
    target = FinitelyPresentedAlgebra(
        target_presentation,
        (y**2 - extension_ring.algebra_generator("s"),),
    )
    return extension_ring, ring_map, source, target


def _assert_algebra_maps_agree(left, right) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for label in left.domain().algebra_generating_set():
        generator = left.domain().algebra_generator(label)
        assert left(generator) == right(generator)


def test_algebra_scalar_extension_restriction_has_the_hom_bijection() -> None:
    extension_ring, ring_map, source, target = _quadratic_algebra_tower()
    adjunction = algebra_base_change_adjunction(ring_map)
    extension = adjunction.left_adjoint()
    restriction = adjunction.right_adjoint()

    extended_source = extension(source)
    restricted_target = restriction(target)

    # Restriction changes the scalar structure, not the underlying ring.  Its
    # selected QQ-presentation must nevertheless include both the scalar
    # generator s and the original algebra generator y.
    restricted_labels = restricted_target.algebra_generating_set()
    assert int(restricted_labels.cardinality()) == 2
    scalar_label = restricted_labels.unrank(0)
    algebra_label = restricted_labels.unrank(1)
    assert int(scalar_label.summand_index()) == 0
    assert scalar_label.summand_element() == "s"
    assert int(algebra_label.summand_index()) == 1
    assert algebra_label.summand_element() == "y"
    assert restricted_target.algebra_generator(scalar_label) == target(
        extension_ring.algebra_generator("s")
    )
    assert restricted_target.algebra_generator(algebra_label) == target.algebra_generator("y")
    for relation in restricted_target.relations():
        assert restricted_target.algebra_presentation_morphism()(relation) == 0

    # y^4 = s^2 = 2, so x |-> y defines an S-algebra morphism
    # S tensor_QQ A -> B.  Its transpose is the corresponding QQ-algebra map
    # A -> Res(B), and transposing back recovers the original map.
    phi = extended_source.Mor(target)(
        {"x": target.algebra_generator("y")}
    )
    transpose = adjunction.hom_set_isomorphism_forward(phi)
    assert transpose(source.algebra_generator("x")) == restricted_target(
        target.algebra_generator("y")
    )
    recovered = adjunction.hom_set_isomorphism_inverse(transpose)
    _assert_algebra_maps_agree(recovered, phi)

    # Check the inverse composite in the other direction as well, using the
    # distinct map x |-> -y.
    psi = source.Mor(restricted_target)(
        {"x": -restricted_target.algebra_generator(algebra_label)}
    )
    inverse_transpose = adjunction.hom_set_isomorphism_inverse(psi)
    recovered_psi = adjunction.hom_set_isomorphism_forward(inverse_transpose)
    _assert_algebra_maps_agree(recovered_psi, psi)


def test_algebra_scalar_extension_restriction_naturality_and_triangles() -> None:
    _, ring_map, source, target = _quadratic_algebra_tower()
    adjunction = algebra_base_change_adjunction(ring_map)
    extension = adjunction.left_adjoint()
    restriction = adjunction.right_adjoint()

    source_involution = source.Mor(source)(
        {"x": -source.algebra_generator("x")}
    )
    left, right = adjunction.unit_transformation().naturality_square(source_involution)
    _assert_algebra_maps_agree(left, right)

    target_involution = target.Mor(target)(
        {"y": -target.algebra_generator("y")}
    )
    left, right = adjunction.counit_transformation().naturality_square(
        target_involution
    )
    _assert_algebra_maps_agree(left, right)

    restricted_target = restriction(target)
    first_triangle = restriction(adjunction.counit(target)) * adjunction.unit(
        restricted_target
    )
    identity_restricted_target = restricted_target.Mor(restricted_target)(
        {
            label: restricted_target.algebra_generator(label)
            for label in restricted_target.algebra_generating_set()
        }
    )
    _assert_algebra_maps_agree(first_triangle, identity_restricted_target)

    extended_source = extension(source)
    second_triangle = adjunction.counit(extended_source) * extension(
        adjunction.unit(source)
    )
    identity_extended_source = extended_source.Mor(extended_source)(
        {
            label: extended_source.algebra_generator(label)
            for label in extended_source.algebra_generating_set()
        }
    )
    _assert_algebra_maps_agree(second_triangle, identity_extended_source)


def test_algebra_restriction_remains_functorial_when_finite_framing_is_lost() -> None:
    ring_map = ring_homset(ZZ, QQ)(lambda element: QQ(element))
    restriction = AlgebraRestrictionOfScalarsFunctor(ring_map)

    source = SymmetricAlgebraOn(QQ, ["x"])
    middle = SymmetricAlgebraOn(QQ, ["y"])
    target = SymmetricAlgebraOn(QQ, ["z"])
    first = source.Mor(middle)(
        {"x": middle.algebra_generator("y") + 1}
    )
    second = middle.Mor(target)(
        {"y": 2 * target.algebra_generator("z")}
    )

    restricted_source = restriction(source)
    assert restricted_source not in FramedAlgebras(ZZ)
    assert restricted_source(source.algebra_generator("x")) == source.algebra_generator("x")

    source_generator = source.algebra_generator("x")
    carried_identity = restriction(source.Mor(source)({"x": source_generator}))
    assert carried_identity(source_generator) == source_generator

    carried_composite = restriction(second * first)
    composed_carried = restriction(second) * restriction(first)
    assert carried_composite(source_generator) == composed_carried(source_generator)
    assert carried_composite(source_generator) == 2 * target.algebra_generator("z") + 1
