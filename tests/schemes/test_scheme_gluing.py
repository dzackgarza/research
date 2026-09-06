from __future__ import annotations


def _doubled_origin_gluing():
    from dzack_research.preamble.all import QQ, AffineSpace
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Isomorphism,
    )
    from dzack_research.preamble.categories.schemes.schemes import Schemes

    chart = AffineSpace(1, QQ, names=("x",))
    x = chart.coordinate_algebra().algebra_generator("x")
    punctured = chart.distinguished_open(x)
    identity = punctured.categorical_identity_morphism()
    glued = Schemes(QQ).glue_affine_charts(
        chart,
        chart,
        Isomorphism(identity, identity),
    )
    return chart, punctured, glued


def _scaled_punctured_line_isomorphism(chart, punctured, scale):
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Isomorphism,
    )
    from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism

    algebra = chart.coordinate_algebra()
    x = algebra.algebra_generator("x")
    localized = punctured.coordinate_algebra()
    localization_map = localized.localization_map()
    scale = algebra.base_ring()(scale)

    def scaled_map(multiplier):
        base_map = algebra.Mor(algebra)({"x": multiplier * x})

        def pullback(element):
            numerator, denominator = localized.localization_fraction_data(element)
            return (
                localization_map(base_map(numerator))
                * localization_map(base_map(denominator)).inverse_of_unit()
            )

        return punctured.Mor(punctured)(
            ring_morphism(localized, localized, pullback)
        )

    return Isomorphism(
        scaled_map(scale),
        scaled_map(algebra.base_ring().one() / scale),
    )


def test_two_affine_charts_glue_to_an_owned_scheme_with_distinct_chart_maps() -> None:
    from dzack_research.preamble.all import QQ
    from dzack_research.preamble.categories.schemes.schemes import (
        OpenImmersions,
        Schemes,
    )

    chart, punctured, glued = _doubled_origin_gluing()

    assert glued in Schemes(QQ)
    assert glued.chart(0) is chart
    assert glued.chart(1) is chart
    assert glued.gluing_datum().left_overlap() is punctured
    assert glued.gluing_datum().right_overlap() is punctured

    left_embedding = glued.chart_embedding(0)
    right_embedding = glued.chart_embedding(1)
    assert left_embedding.domain() is chart
    assert right_embedding.domain() is chart
    assert left_embedding.codomain() is glued
    assert right_embedding.codomain() is glued
    assert left_embedding != right_embedding

    left_image = glued.chart_image(0)
    right_image = glued.chart_image(1)
    assert left_image is not right_image
    assert left_image in OpenImmersions(glued)
    assert right_image in OpenImmersions(glued)
    assert left_image.inclusion() in Schemes(QQ).Mono(left_image, glued)
    assert right_image.inclusion() in Schemes(QQ).Mono(right_image, glued)
    assert left_embedding in Schemes(QQ).Mono(chart, glued)
    assert right_embedding in Schemes(QQ).Mono(chart, glued)
    assert left_embedding.open_image() is left_image
    assert right_embedding.open_image() is right_image
    assert left_embedding.chart_isomorphism().forward().domain() is chart
    assert left_embedding.chart_isomorphism().forward().codomain() is left_image

    identity = glued.categorical_identity_morphism()
    assert identity.parent() is glued.Mor(glued)
    assert identity * left_embedding == left_embedding
    assert identity * right_embedding == right_embedding

    structure = glued.structure_morphism()
    assert structure * left_embedding == chart.structure_morphism()
    assert structure * right_embedding == chart.structure_morphism()


def test_maps_out_of_a_glued_scheme_are_exactly_compatible_chart_maps() -> None:
    chart, _punctured, glued = _doubled_origin_gluing()
    algebra = chart.coordinate_algebra()
    identity = chart.categorical_identity_morphism()
    zero = chart.Mor(chart)(
        algebra.Mor(algebra)({"x": algebra.zero()})
    )

    collapse = glued.Mor(chart)((identity, identity))
    assert collapse * glued.chart_embedding(0) == identity
    assert collapse * glued.chart_embedding(1) == identity
    assert collapse == glued.Mor(chart)((identity, identity))

    zero_map = glued.Mor(chart)((zero, zero))
    assert zero_map != collapse
    assert zero_map * glued.chart_embedding(0) == zero
    assert zero_map * glued.chart_embedding(1) == zero

    postcomposed = zero * collapse
    assert postcomposed.parent() is glued.Mor(chart)
    assert postcomposed * glued.chart_embedding(0) == zero
    assert postcomposed * glued.chart_embedding(1) == zero

    try:
        glued.Mor(chart)((identity, zero))
    except ValueError as error:
        assert "do not agree through the overlap transition" in str(error)
    else:
        raise AssertionError("incompatible chart maps must not glue to a scheme morphism")


def test_scheme_gluing_requires_an_actual_open_overlap() -> None:
    from dzack_research.preamble.all import QQ, AffineSpace
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Isomorphism,
    )
    from dzack_research.preamble.categories.schemes.schemes import Schemes

    chart = AffineSpace(1, QQ, names=("x",))
    identity = chart.categorical_identity_morphism()

    try:
        Schemes(QQ).glue_affine_charts(
            chart,
            chart,
            Isomorphism(identity, identity),
        )
    except ValueError as error:
        assert "open subscheme of the left chart" in str(error)
    else:
        raise AssertionError("scheme gluing must reject a transition not sited on open subobjects")


def test_finite_affine_atlas_retains_indexed_transition_data_and_maps_out() -> None:
    from dzack_research.preamble.all import QQ, AffineSpace
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Isomorphism,
    )
    from dzack_research.preamble.categories.schemes.schemes import (
        OpenImmersions,
        Schemes,
    )
    from dzack_research.preamble.categories.sets.finite_ordered_sets import (
        finite_ordered_set,
    )
    from dzack_research.preamble.categories.sets.indexed_families import (
        finite_indexed_family,
    )

    chart = AffineSpace(1, QQ, names=("x",))
    x = chart.coordinate_algebra().algebra_generator("x")
    punctured = chart.distinguished_open(x)
    overlap_identity = punctured.categorical_identity_morphism()
    labels = finite_ordered_set(("left", "middle", "right"))
    charts = finite_indexed_family(
        labels,
        lambda _label: chart,
        name="Three affine-line charts",
    )
    transitions = {
        ("left", "middle"): Isomorphism(overlap_identity, overlap_identity),
        ("left", "right"): Isomorphism(overlap_identity, overlap_identity),
        ("middle", "right"): Isomorphism(overlap_identity, overlap_identity),
    }

    glued = Schemes(QQ).glue_affine_atlas(charts, transitions)
    datum = glued.gluing_datum()

    assert glued in Schemes(QQ)
    assert tuple(glued.chart_indices()) == ("left", "middle", "right")
    assert glued.number_of_charts() == 3
    assert glued.chart("middle") is chart
    assert datum.transitions()["left", "right"] is transitions["left", "right"]
    assert (
        datum.transition_between("right", "left").forward()
        is transitions["left", "right"].inverse()
    )

    triple = glued.triple_overlap("left", "middle", "right")
    assert triple in OpenImmersions(chart)
    restricted = glued.transition_on_triple("left", "middle", "right")
    assert restricted.domain() is triple
    assert restricted.codomain() is glued.triple_overlap(
        "middle",
        "left",
        "right",
    )

    assert glued.chart_embedding("left") != glued.chart_embedding("middle")
    assert glued.chart_image("left") is not glued.chart_image("right")
    identity = chart.categorical_identity_morphism()
    collapse = glued.Mor(chart)(
        {
            "left": identity,
            "middle": identity,
            "right": identity,
        }
    )
    for label in labels:
        assert collapse * glued.chart_embedding(label) == identity
        assert (
            glued.categorical_identity_morphism() * glued.chart_embedding(label)
            == glued.chart_embedding(label)
        )


def test_finite_affine_atlas_verifies_inverse_and_nontrivial_triple_cocycle() -> None:
    from dzack_research.preamble.all import QQ, AffineSpace
    from dzack_research.preamble.categories.abstract_categories.hom_categories import (
        CategoricalIsomorphism,
    )
    from dzack_research.preamble.categories.schemes.schemes import Schemes

    chart = AffineSpace(1, QQ, names=("x",))
    x = chart.coordinate_algebra().algebra_generator("x")
    punctured = chart.distinguished_open(x)
    scale_two = _scaled_punctured_line_isomorphism(chart, punctured, 2)
    scale_three = _scaled_punctured_line_isomorphism(chart, punctured, 3)
    scale_six = _scaled_punctured_line_isomorphism(chart, punctured, 6)

    glued = Schemes(QQ).glue_affine_atlas(
        (chart, chart, chart),
        {
            (0, 1): scale_two,
            (0, 2): scale_six,
            (1, 2): scale_three,
        },
    )
    assert glued.number_of_charts() == 3
    assert (
        glued.transition_on_triple(1, 2, 0)
        * glued.transition_on_triple(0, 1, 2)
        == glued.transition_on_triple(0, 2, 1)
    )

    scale_five = _scaled_punctured_line_isomorphism(chart, punctured, 5)
    try:
        Schemes(QQ).glue_affine_atlas(
            (chart, chart, chart),
            {
                (0, 1): scale_two,
                (0, 2): scale_five,
                (1, 2): scale_three,
            },
        )
    except ValueError as error:
        assert "fail the triple cocycle" in str(error)
    else:
        raise AssertionError("finite scheme gluing must reject a broken triple cocycle")

    overlap_identity = punctured.categorical_identity_morphism()
    broken_inverse = CategoricalIsomorphism(
        scale_two.parent(),
        overlap_identity,
        scale_two.forward(),
        verify=False,
    )
    try:
        Schemes(QQ).glue_affine_atlas(
            (chart, chart),
            {(0, 1): broken_inverse},
        )
    except ValueError as error:
        assert "not left-invertible" in str(error)
    else:
        raise AssertionError("finite scheme gluing must verify each stated overlap inverse")


def test_finite_affine_atlas_verifies_triple_overlap_domains() -> None:
    from dzack_research.preamble.all import QQ, AffineSpace
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Isomorphism,
    )
    from dzack_research.preamble.categories.schemes.schemes import Schemes

    chart = AffineSpace(1, QQ, names=("x",))
    algebra = chart.coordinate_algebra()
    x = algebra.algebra_generator("x")

    def identity_transition(element):
        overlap = chart.distinguished_open(element)
        identity = overlap.categorical_identity_morphism()
        return Isomorphism(identity, identity)

    try:
        Schemes(QQ).glue_affine_atlas(
            (chart, chart, chart),
            {
                (0, 1): identity_transition(x),
                (0, 2): identity_transition(x - algebra.one()),
                (1, 2): identity_transition(x - algebra(2)),
            },
        )
    except ValueError as error:
        assert "does not preserve the represented triple-overlap domain" in str(error)
    else:
        raise AssertionError(
            "finite scheme gluing must reject transitions with incompatible triple domains"
        )
