from dzack_research.preamble.all import (
    AffineSchemes,
    AffineSpaces,
    OpenImmersions,
    ProjectiveSpace,
    QQ,
    Schemes,
)


def test_the_standard_charts_of_a_projective_line_are_affine_lines_of_ratios() -> None:
    r"""``U_i = D_+(x_i) = Spec Q[x_k/x_i]``, affine ``1``-space on one ratio."""
    line = ProjectiveSpace(1, QQ)
    charts = line.standard_affine_charts()

    assert int(charts.cardinality().finite_value()) == 2
    for index, other in ((0, 1), (1, 0)):
        chart = line.standard_affine_chart(index)
        assert chart in AffineSpaces(QQ)
        assert int(chart.relative_dimension()) == 1
        labels = chart.coordinate_algebra().algebra_generating_set()
        assert int(labels.cardinality().finite_value()) == 1
        assert next(iter(labels)) == f"x{other}_over_x{index}"


def test_a_standard_overlap_is_the_open_where_the_other_coordinate_is_invertible() -> None:
    r"""``U_0 cap U_1 = D(x_1/x_0)``, and ``x_1/x_0`` is a unit on it."""
    line = ProjectiveSpace(1, QQ)
    chart = line.standard_affine_chart(0)
    overlap = line.standard_chart_overlap(0, 1)
    ratio = chart.coordinate_algebra().algebra_generator("x1_over_x0")

    assert overlap in OpenImmersions(chart)
    assert overlap.is_distinguished_open()
    assert overlap.distinguished_open_element() == ratio
    assert overlap.inclusion().codomain() is chart
    restricted = overlap.inclusion().coordinate_algebra_morphism()(ratio)
    assert restricted.is_unit()
    assert restricted * restricted.inverse_of_unit() == overlap.coordinate_algebra().one()


def test_the_projective_line_transition_inverts_the_ratio() -> None:
    r"""``phi_{10}`` sends ``x_0/x_1`` to ``(x_1/x_0)^{-1}``: the map ``t |-> 1/t``."""
    line = ProjectiveSpace(1, QQ)
    transition = line.standard_chart_transition(0, 1)
    forward = transition.forward()
    source_overlap = line.standard_chart_overlap(0, 1)
    target_overlap = line.standard_chart_overlap(1, 0)

    assert forward.domain() is source_overlap
    assert forward.codomain() is target_overlap
    assert transition.inverse().domain() is target_overlap
    assert transition.inverse().codomain() is source_overlap

    target_ratio = target_overlap.inclusion().coordinate_algebra_morphism()(
        line.standard_affine_chart(1).coordinate_algebra().algebra_generator("x0_over_x1")
    )
    source_ratio = source_overlap.inclusion().coordinate_algebra_morphism()(
        line.standard_affine_chart(0).coordinate_algebra().algebra_generator("x1_over_x0")
    )
    assert forward.coordinate_algebra_morphism()(target_ratio) == (
        source_ratio.inverse_of_unit()
    )


def test_a_projective_plane_chart_change_divides_the_two_ratios() -> None:
    r"""``phi_{20}`` sends ``x_1/x_2`` to ``(x_1/x_0)(x_2/x_0)^{-1}``.

    This is the identity ``x_1/x_2 = (x_1/x_0)/(x_2/x_0)`` in the section ring
    of ``U_0 cap U_2``, which is what makes the standard charts agree where
    they meet.  Two charts alone cannot show it: it needs a third homogeneous
    coordinate to divide.
    """
    plane = ProjectiveSpace(2, QQ)
    forward = plane.standard_chart_transition(0, 2).forward()
    source_restriction = plane.standard_chart_overlap(
        0, 2
    ).inclusion().coordinate_algebra_morphism()
    target_restriction = plane.standard_chart_overlap(
        2, 0
    ).inclusion().coordinate_algebra_morphism()
    chart_zero = plane.standard_affine_chart(0).coordinate_algebra()
    chart_two = plane.standard_affine_chart(2).coordinate_algebra()

    one_over_two = target_restriction(chart_two.algebra_generator("x1_over_x2"))
    one_over_zero = source_restriction(chart_zero.algebra_generator("x1_over_x0"))
    two_over_zero = source_restriction(chart_zero.algebra_generator("x2_over_x0"))

    assert forward.coordinate_algebra_morphism()(one_over_two) == (
        one_over_zero * two_over_zero.inverse_of_unit()
    )


def test_the_projective_plane_is_the_scheme_glued_from_its_standard_atlas() -> None:
    r"""``P^2_Q`` is the gluing of ``U_0, U_1, U_2`` along their overlaps.

    The atlas construction checks the pairwise inverse conditions and the
    cocycle ``phi_{ki} = phi_{kj} phi_{ji}`` on every triple overlap before it
    returns a scheme, so a chart change that were wrong in any one coordinate
    could not produce this object.
    """
    plane = ProjectiveSpace(2, QQ)
    glued = plane.glued_from_standard_charts()

    assert glued in Schemes(QQ)
    assert glued.scheme_base_ring() is QQ
    for index in range(3):
        chart = plane.standard_affine_chart(index)
        assert chart in AffineSchemes(QQ)
        assert int(chart.relative_dimension()) == 2
