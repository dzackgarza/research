from __future__ import annotations


def _quadratic_algebra(ring):

    presentation = ring.free_module(("z",)).symmetric_algebra()
    z = presentation.algebra_generator("z")
    return (presentation).quotient_by_relations((z * z - ring.one(),),
    )


def _sign_transition(source, target, sign):
    from dzack_research.preamble.categories.algebras.algebras import Algebras

    sign = source.base_ring()(sign)
    target_sign = target.base_ring()(sign)
    algebras = Algebras(source.algebra_base_ring()).Associative().Unital()
    forward = algebras.Mor(source, target)(
        {"z": target_sign * target.algebra_generator("z")}
    )
    inverse = algebras.Mor(target, source)(
        {"z": sign * source.algebra_generator("z")}
    )
    return algebras.Core().Mor(source, target)(forward, inverse)


def _two_chart_sign_datum():
    from dzack_research.preamble.all import QQ

    algebra = QQ.polynomial_ring("x")
    x = algebra.algebra_generator("x")
    scheme = (algebra).affine_spectrum()
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    local_algebras = tuple(
        _quadratic_algebra(open_subscheme.coordinate_algebra())
        for open_subscheme in cover.opens()
    )
    left_overlap = cover.restrict_algebra(local_algebras[0], 0, 1)
    right_overlap = cover.restrict_algebra(local_algebras[1], 1, 0)
    transition = _sign_transition(left_overlap, right_overlap, -1)
    datum = cover.glue_algebras(local_algebras, {(0, 1): transition}).gluing_datum()
    return algebra, cover, local_algebras, datum


def test_two_chart_algebra_descent_has_algebra_sections_and_algebra_restrictions() -> None:
    from dzack_research.preamble.categories.algebras.algebras import (
        Algebras,
    )
    from dzack_research.preamble.categories.modules.pure.modules import TensorProductModules

    algebra, cover, local_algebras, datum = _two_chart_sign_datum()
    sections = datum.compatible_sections()
    sheaf = datum.sheaf()

    assert sheaf in cover.cech_coverage().sheaves(
        Algebras(algebra).Associative().Unital()
    )
    assert sections in Algebras(algebra)
    assert sections in Algebras(algebra).Associative().Unital().Commutative()
    assert sections.algebra_base_ring() is algebra
    assert not sections.is_framed_module()
    module_sections = datum.underlying_module_datum().compatible_sections()
    multiplication = sections.multiplication()
    tensor_square = multiplication.domain()
    assert sections.unformed_module() is module_sections
    assert tensor_square in TensorProductModules(algebra)
    assert tensor_square.tensor_factor(0) is module_sections
    assert tensor_square.tensor_factor(1) is module_sections
    assert multiplication.codomain() is module_sections
    assert sheaf.global_sections() is sections
    assert sheaf.underlying_module_sheaf() is datum.underlying_module_datum().sheaf()
    assert sheaf.sections_on_chart(0) is local_algebras[0]
    assert sheaf.sections_on_intersection(0, 0, 1) is datum.restricted_algebra(0, 0, 1)

    left_z = local_algebras[0].algebra_generator("z")
    right_z = local_algebras[1].algebra_generator("z")
    twisted_generator = datum.compatible_section((left_z, -right_z))
    assert twisted_generator * twisted_generator == sections.one()
    assert tuple(
        datum.compatible_section_component(sections.one(), index)
        for index in cover.atlas()
    ) == tuple(local_algebra.one() for local_algebra in local_algebras)
    module_generator = module_sections(twisted_generator)
    assert multiplication(
        tensor_square.pure_tensor(module_generator, module_generator)
    ) == module_sections(sections.one())

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
    from dzack_research.preamble.all import QQ

    algebra = QQ.polynomial_ring(("x", "y"))
    x, y = algebra.algebra_generators()
    scheme = (algebra).affine_spectrum()
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

    datum = cover.glue_algebras(local_algebras, transitions).gluing_datum()
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
    middle = cover.glue_algebras(local_algebras, {(0, 1): transition}).gluing_datum()
    target = cover.glue_algebras(local_algebras, {(0, 1): transition}).gluing_datum()

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
    section = source.compatible_section((left_z, -right_z))
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
    ).gluing_datum()
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
