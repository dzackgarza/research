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
