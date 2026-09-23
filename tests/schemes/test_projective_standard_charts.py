from dzack_research.preamble.all import (
    ProjectiveSpaces,
    QQ,
)






def test_the_projective_line_transition_inverts_the_ratio() -> None:
    r"""``phi_{10}`` sends ``x_0/x_1`` to ``(x_1/x_0)^{-1}``: the map ``t |-> 1/t``."""
    line = ProjectiveSpaces(QQ)(1)
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
    plane = ProjectiveSpaces(QQ)(2)
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


