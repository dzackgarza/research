from __future__ import annotations


def _quadratic_algebra(ring):
    from dzack_research.preamble.all import FinitelyPresentedAlgebra, SymmetricAlgebraOn

    presentation = SymmetricAlgebraOn(ring, ("z",))
    z = presentation.algebra_generator("z")
    return FinitelyPresentedAlgebra(
        presentation,
        (z * z - ring.one(),),
    )


def _sign_transition(source, target, sign):
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Isomorphism,
    )

    sign = source.base_ring()(sign)
    target_sign = target.base_ring()(sign)
    forward = source.Mor(target)(
        {"z": target_sign * target.algebra_generator("z")}
    )
    inverse = target.Mor(source)(
        {"z": sign * source.algebra_generator("z")}
    )
    return Isomorphism(forward, inverse)


def _two_chart_sign_datum():
    from dzack_research.preamble.all import QQ, PolynomialRing, Spec

    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    local_algebras = tuple(
        _quadratic_algebra(open_subscheme.coordinate_algebra())
        for open_subscheme in cover.opens()
    )
    left_overlap = cover.restrict_algebra(local_algebras[0], 0, 1)
    right_overlap = cover.restrict_algebra(local_algebras[1], 1, 0)
    transition = _sign_transition(left_overlap, right_overlap, -1)
    datum = cover.glue_algebras(local_algebras, {(0, 1): transition})
    return algebra, cover, local_algebras, datum


def test_two_chart_algebra_descent_has_algebra_sections_and_algebra_restrictions() -> None:
    from dzack_research.preamble.categories.algebras.algebras import (
        Algebras,
        CommutativeAlgebras,
    )

    algebra, _cover, local_algebras, datum = _two_chart_sign_datum()
    sections = datum.compatible_sections()
    sheaf = datum.sheaf()

    assert sections in Algebras(algebra)
    assert sections in CommutativeAlgebras(algebra)
    assert sections.algebra_base_ring() is algebra
    assert not sections.is_framed()
    assert sheaf.global_sections() is sections
    assert sheaf.underlying_module_sheaf() is datum.underlying_module_datum().sheaf()
    assert sheaf.sections_on_chart(0) is local_algebras[0]
    assert sheaf.sections_on_intersection(0, 0, 1) is datum.restricted_algebra(0, 0, 1)

    left_z = local_algebras[0].algebra_generator("z")
    right_z = local_algebras[1].algebra_generator("z")
    twisted_generator = sections((left_z, -right_z))
    assert twisted_generator * twisted_generator == sections.one()
    assert sections.one().components() == tuple(
        local_algebra.one() for local_algebra in local_algebras
    )

    restriction = sheaf.restriction_map(0, 0, 1)
    assert restriction.domain() is local_algebras[0]
    restricted_left = datum.restricted_algebra(0, 0, 1)
    assert restriction.codomain().algebra_over_extension() is restricted_left
    restricted_z = datum.restrict_section_between_intersections(
        0,
        left_z,
        (0,),
        (0, 1),
    )
    assert restricted_z == restricted_left.algebra_generator("z")

    overlap_transition = sheaf.transition(0, 1, 0, 1)
    assert overlap_transition.domain() is datum.restricted_algebra(0, 0, 1)
    assert overlap_transition.codomain() is datum.restricted_algebra(1, 0, 1)


def test_three_chart_algebra_descent_checks_the_algebra_cocycle() -> None:
    from dzack_research.preamble.all import QQ, PolynomialRing, Spec

    algebra = PolynomialRing(QQ, ("x", "y"))
    x, y = algebra.algebra_generators()
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(
        x,
        y,
        algebra.one() - x - y,
    )
    local_algebras = tuple(
        _quadratic_algebra(open_subscheme.coordinate_algebra())
        for open_subscheme in cover.opens()
    )

    transitions = {}
    signs = {(0, 1): -1, (1, 2): -1, (0, 2): 1}
    for (left_index, right_index), sign in signs.items():
        left_overlap = cover.restrict_algebra(
            local_algebras[left_index],
            left_index,
            right_index,
        )
        right_overlap = cover.restrict_algebra(
            local_algebras[right_index],
            right_index,
            left_index,
        )
        transitions[left_index, right_index] = _sign_transition(
            left_overlap,
            right_overlap,
            sign,
        )

    datum = cover.glue_algebras(local_algebras, transitions)
    triple_left = datum.transition_on_intersection(0, 1, 0, 1, 2)
    triple_right = datum.transition_on_intersection(1, 2, 0, 1, 2)
    triple_direct = datum.transition_on_intersection(0, 2, 0, 1, 2)
    triple_source = datum.restricted_algebra(0, 0, 1, 2)
    for label in triple_source.algebra_generating_set():
        generator = triple_source.algebra_generator(label)
        assert triple_right(triple_left(generator)) == triple_direct(generator)

    local_z = local_algebras[0].algebra_generator("z")
    direct_restriction = datum.restrict_section_between_intersections(
        0,
        local_z,
        (0,),
        (0, 1, 2),
    )
    pair_restriction = datum.restrict_section_between_intersections(
        0,
        local_z,
        (0,),
        (0, 1),
    )
    iterated_restriction = datum.restrict_section_between_intersections(
        0,
        pair_restriction,
        (0, 1),
        (0, 1, 2),
    )
    assert iterated_restriction == direct_restriction

    bad_transitions = dict(transitions)
    left_overlap = cover.restrict_algebra(local_algebras[0], 0, 2)
    right_overlap = cover.restrict_algebra(local_algebras[2], 2, 0)
    bad_transitions[0, 2] = _sign_transition(left_overlap, right_overlap, -1)
    try:
        cover.glue_algebras(local_algebras, bad_transitions)
    except ValueError as error:
        assert "fail the cocycle condition" in str(error)
    else:
        raise AssertionError("incompatible algebra transitions must fail the triple cocycle")


def test_algebra_descent_morphisms_use_endpoint_homs_and_compose() -> None:
    from dzack_research.preamble.categories.algebras.algebras import Algebras

    algebra, cover, local_algebras, source = _two_chart_sign_datum()
    transition = source.transition(0, 1)
    middle = cover.glue_algebras(local_algebras, {(0, 1): transition})
    target = cover.glue_algebras(local_algebras, {(0, 1): transition})

    sign_maps = tuple(
        local_algebra.Mor(local_algebra)(
            {"z": -local_algebra.algebra_generator("z")}
        )
        for local_algebra in local_algebras
    )
    first = source.Mor(middle)(sign_maps)
    second = middle.Mor(target)(sign_maps)
    composite = first.then(second)

    assert first.parent() is source.Mor(middle)
    assert second.parent() is middle.Mor(target)
    assert composite.parent() is source.Mor(target)
    for index, local_algebra in enumerate(local_algebras):
        z = local_algebra.algebra_generator("z")
        assert composite.local_map(index)(z) == z

    source_identity = source.Mor(source).identity()
    right_unit = first * source_identity
    for index in range(len(local_algebras)):
        z = local_algebras[index].algebra_generator("z")
        assert right_unit.local_map(index)(z) == first.local_map(index)(z)

    sections = source.compatible_sections()
    left_z = local_algebras[0].algebra_generator("z")
    right_z = local_algebras[1].algebra_generator("z")
    section = sections((left_z, -right_z))
    global_map = first.global_sections_map()
    assert global_map.domain() is sections
    assert global_map.codomain() is middle.compatible_sections()
    assert global_map(section * section) == global_map(section) * global_map(section)
    assert global_map(sections.one()) == middle.compatible_sections().one()
    assert source_identity.global_sections_map()(section) == section
    assert sections in Algebras(algebra)

    left_overlap = cover.restrict_algebra(local_algebras[0], 0, 1)
    right_overlap = cover.restrict_algebra(local_algebras[1], 1, 0)
    identity_transition = _sign_transition(left_overlap, right_overlap, 1)
    incompatible_target = cover.glue_algebras(
        local_algebras,
        {(0, 1): identity_transition},
    )
    local_identities = tuple(
        local_algebra.Mor(local_algebra).identity()
        for local_algebra in local_algebras
    )
    try:
        source.Mor(incompatible_target)(local_identities)
    except ValueError as error:
        assert "incompatible with transition maps" in str(error)
    else:
        raise AssertionError("algebra descent morphisms must commute with overlap transitions")
