r"""A quotient of a presented algebra is one quotient of the same presentation.

For ``A = P/I`` the algebra ``A/(J)`` is ``P/(I + J~)``, where ``J~`` lifts the
new relations to ``P``.  Cutting the line ``x = 0`` out of the union of the two
axes ``xy = 0`` leaves the ``y``-axis, and the result is presented over the same
polynomial ring and the same scalars as the first cut, not stacked on top of it
as a second quotient object.
"""

from dzack_research.preamble.all import (
    QQ,
)


def test_a_second_cut_stays_on_the_first_presentation() -> None:
    plane = QQ.polynomial_ring("x,y")
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    axes = (plane).quotient_by_relations([x * y])

    axis = (axes).quotient_by_relations([axes(x)])

    assert axis.presentation_ring() is plane
    assert axis.base_ring() is QQ


def test_the_second_cut_imposes_both_relations() -> None:
    plane = QQ.polynomial_ring("x,y")
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    axes = (plane).quotient_by_relations([x * y])

    axis = (axes).quotient_by_relations([axes(x)])

    assert axis(x) == axis.zero()
    assert axis(y) != axis.zero()
    assert axis(y) ** 2 != axis.zero()


def test_one_quotient_operation_serves_a_free_and_a_presented_algebra() -> None:
    r"""The free polynomial algebra is the case with no relations yet."""
    plane = QQ.polynomial_ring("x,y")
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")

    axes, plane_to_axes = plane._quotient_by_algebra_elements([x * y])
    axis, axes_to_axis = axes._quotient_by_algebra_elements([axes(x)])

    assert axes.presentation_ring() is plane
    assert axis.presentation_ring() is plane
    assert plane_to_axes(x * y) == axes.zero()
    assert axes_to_axis(axes(x)) == axis.zero()
    assert axes_to_axis(axes(y)) != axis.zero()
