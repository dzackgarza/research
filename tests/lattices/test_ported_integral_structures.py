"""The T2 rational-integral provider reached through the research arithmetic API.

Unverified: these specimens are executed only in terminal T.  The port object is
used as the prescribed finitely generated underlying finitely generated rational group; every result
that crosses back retains live preamble lattice embeddings and isometries.
"""

from sage_indefinite_port.groups.integral_structures import (
    ArithmeticSubgroup,
    RationalMatrixGroup,
)

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    Lattices,
    IntegralStructureAction,
    Modules,
)


def _proper_rational_group_and_lattices():
    plane = Lattices(QQ)("U")
    restriction = Modules(QQ).restriction_of_scalars(
        ZZ.Mor(QQ)(lambda element: QQ(element))
    )
    space = restriction(plane)
    e, f = plane.module_generators()
    standard_module = ZZ.free_module(2)
    standard = standard_module.Mono(space)(
        {0: space.wrap(e), 1: space.wrap(f)}
    )
    involution = plane.Aut()(
        {
            0: plane.scalar_multiple(QQ(2), f),
            1: plane.scalar_multiple(QQ(1) / 2, e),
        }
    )
    group = RationalMatrixGroup(plane, (involution,))
    target_module = ZZ.free_module(2)
    target = target_module.Mono(space)(
        {
            0: space.wrap(involution(e)),
            1: space.wrap(involution(f)),
        },
    )
    return plane, space, standard, target, involution, group


def _carries(source, target, isometry) -> bool:
    space = source.codomain()
    inverse = ~isometry
    return all(
        target.is_in_image(
            space.wrap(
                isometry(
                    source(source.domain().module_generator(label)).underlying_element()
                )
            )
        )
        for label in source.domain().module_generating_set()
    ) and all(
        source.is_in_image(
            space.wrap(
                inverse(
                    target(target.domain().module_generator(label)).underlying_element()
                )
            )
        )
        for label in target.domain().module_generating_set()
    )


def test_ported_integral_stabilizer_retains_the_selected_rational_group() -> None:
    _plane, _space, standard, _target, involution, group = (
        _proper_rational_group_and_lattices()
    )

    stabilizer = IntegralStructureAction(group, standard).stabilizer()

    assert stabilizer.supergroup() is group
    assert all(_carries(standard, standard, generator) for generator in stabilizer.generators())
    assert not _carries(standard, standard, involution)


def test_ported_transporter_is_an_actual_rational_isometry_of_the_lattices() -> None:
    _plane, _space, standard, target, _involution, group = (
        _proper_rational_group_and_lattices()
    )

    witness = IntegralStructureAction(group, standard).transporter(target)

    assert witness is not None
    assert witness.parent() is group.rational_lattice().Aut()
    assert _carries(standard, target, witness)


def test_ported_cosets_retain_their_orientation_and_live_representatives() -> None:
    plane, _space, standard, _target, _involution, group = (
        _proper_rational_group_and_lattices()
    )

    right_cosets = IntegralStructureAction(group, standard).right_cosets()

    assert right_cosets.ambient_group() is group
    assert right_cosets.right_subgroup().supergroup() is group
    assert right_cosets.cardinality() == 2
    assert all(
        representative.parent() is plane.Aut()
        for representative in right_cosets.representatives()
    )

    trivial = ArithmeticSubgroup(group, (plane.Aut().one(),))
    double_cosets = IntegralStructureAction(group, standard).double_cosets(trivial)
    assert double_cosets.left_subgroup() is trivial
    assert double_cosets.ambient_group() is group
    assert double_cosets.right_subgroup().supergroup() is group
    assert double_cosets.cardinality() == 2
    assert sum(
        piece.double_coset_size() for piece in double_cosets.intersections()
    ) == double_cosets.finite_ambient_order()
