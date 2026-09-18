from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.algebras.algebras import Algebras


def _polynomial_algebra_descent(variable):
    ambient = QQ.polynomial_ring("x")
    x = ambient.algebra_generator("x")
    scheme = (ambient).affine_spectrum()
    cover = scheme.distinguished_open_cover(x, ambient.one() - x)
    local_algebras = tuple(
        cover.open(index).coordinate_algebra().polynomial_ring(variable)
        for index in cover.atlas()
    )
    left = cover.restrict_algebra(local_algebras[0], 0, 1)
    right = cover.restrict_algebra(local_algebras[1], 1, 0)
    forward = left.Mor(right)({variable: right.algebra_generator(variable)})
    inverse = right.Mor(left)({variable: left.algebra_generator(variable)})
    transition = forward.parent().base_category().Core().Mor(left, right)(forward, inverse)
    datum = cover.glue_algebras(
        local_algebras,
        {(0, 1): transition},
    ).gluing_datum()
    return scheme, cover, datum


def test_noncyclic_polynomial_algebra_descent_has_one_general_relative_spectrum() -> None:
    scheme, cover, datum = _polynomial_algebra_descent("z")
    relative = datum.relative_spectrum()
    glued = relative.arrow().domain()

    assert relative.arrow().codomain() is scheme
    assert datum.sheaf().relative_spectrum() is relative
    for index in cover.atlas():
        assert glued.gluing_datum().chart(index).coordinate_algebra() is datum.local_algebra(index)
        algebra_map = datum.local_algebra(index).algebra_structure_morphism()
        expected = cover.open(index).inclusion() * Algebras(
            algebra_map.domain().base_ring()
        ).Associative().Unital().Commutative().spectrum()(algebra_map)
        assert relative.arrow() * glued.gluing_datum().chart_embedding(index) == expected


def test_relative_spec_is_contravariant_on_a_nonidentity_algebra_descent_map() -> None:
    scheme, source_cover, source = _polynomial_algebra_descent("z")
    _same_scheme, target_cover, target = _polynomial_algebra_descent("w")
    assert source_cover.ambient_scheme().coordinate_algebra() is target_cover.ambient_scheme().coordinate_algebra()

    # Rebuild the target datum on the source cover so the algebra-descent Hom
    # has one literal cover owner, while retaining a genuinely different local algebra.
    target_local = tuple(
        source_cover.open(index).coordinate_algebra().polynomial_ring("w")
        for index in source_cover.atlas()
    )
    target_left = source_cover.restrict_algebra(target_local[0], 0, 1)
    target_right = source_cover.restrict_algebra(target_local[1], 1, 0)
    target_forward = target_left.Mor(target_right)(
        {"w": target_right.algebra_generator("w")}
    )
    target_inverse = target_right.Mor(target_left)(
        {"w": target_left.algebra_generator("w")}
    )
    target_transition = target_forward.parent().base_category().Core().Mor(
        target_left,
        target_right,
    )(target_forward, target_inverse)
    target = source_cover.glue_algebras(
        target_local,
        {(0, 1): target_transition},
    ).gluing_datum()
    local_maps = tuple(
        source.local_algebra(index).Mor(target.local_algebra(index))(
            {"z": target.local_algebra(index).algebra_generator("w") ** 2}
        )
        for index in source_cover.atlas()
    )
    algebra_map = source.Mor(target)(local_maps)

    source_relative = source.relative_spectrum()
    target_relative = target.relative_spectrum()
    induced = algebra_map.relative_spectrum_morphism()

    assert induced.domain() is target_relative.arrow().domain()
    assert induced.codomain() is source_relative.arrow().domain()
    assert source_relative.arrow() * induced == target_relative.arrow()
    for index in source_cover.atlas():
        expected = (
            source_relative.arrow().domain().chart_embedding(index)
            * Algebras(
                algebra_map.local_map(index).domain().base_ring()
            ).Associative().Unital().Commutative().spectrum()(algebra_map.local_map(index))
        )
        assert induced * target_relative.arrow().domain().chart_embedding(index) == expected


def test_relative_spectrum_atlas_refinement_keeps_the_same_map_to_the_base() -> None:
    from dzack_research.preamble.categories.schemes.gluing import FiniteAffineAtlases
    from dzack_research.preamble.categories.schemes.schemes import Schemes

    scheme, _cover, datum = _polynomial_algebra_descent("z")
    relative = datum.relative_spectrum()
    total_space = relative.arrow().domain()
    coarse = total_space.finite_affine_atlas()
    left = coarse.chart(0)
    right = coarse.chart(1)
    overlap = coarse.overlap(0, 1)
    whole_overlap = overlap.distinguished_open(overlap.coordinate_algebra().one())
    schemes = Schemes(QQ)
    left_forward = whole_overlap.corestriction(overlap.categorical_identity_morphism())
    left_inverse = whole_overlap.inclusion()
    left_to_overlap = schemes.Core().Mor(
        left_forward.domain(),
        left_forward.codomain(),
    )(
        left_forward,
        left_inverse,
    )
    right_forward = whole_overlap.corestriction(coarse.transition_between(1, 0).forward())
    right_inverse = coarse.transition_between(0, 1).forward() * whole_overlap.inclusion()
    right_to_overlap = schemes.Core().Mor(
        right_forward.domain(),
        right_forward.codomain(),
    )(
        right_forward,
        right_inverse,
    )
    fine = FiniteAffineAtlases(total_space)(
        (left, right, overlap),
        (
            coarse.transition_between(0, 1),
            left_to_overlap,
            right_to_overlap,
        ),
        (
            coarse.chart_embedding(0),
            coarse.chart_embedding(1),
            coarse.chart_embedding(0) * overlap.inclusion(),
        ),
    )
    refinement = FiniteAffineAtlases(total_space).Mor(fine, coarse)(
        (0, 1, 0),
        (
            left.categorical_identity_morphism(),
            right.categorical_identity_morphism(),
            overlap.inclusion(),
        ),
    )

    comparison = refinement.comparison_morphism()
    refined_structure = relative.arrow() * comparison
    assert comparison == total_space.categorical_identity_morphism()
    assert refined_structure.codomain() is scheme
    for fine_index in fine.chart_indices():
        coarse_index = refinement.coarse_index(fine_index)
        expected = (
            relative.arrow()
            * coarse.chart_embedding(coarse_index)
            * refinement.chart_map(fine_index)
        )
        assert refined_structure * fine.chart_embedding(fine_index) == expected
