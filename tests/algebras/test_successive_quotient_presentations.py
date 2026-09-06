r"""A quotient of a presented algebra is one quotient of the same presentation.

For ``A = P/I`` the algebra ``A/(J)`` is ``P/(I + J~)``, where ``J~`` lifts the
new relations to ``P``.  Cutting the line ``x = 0`` out of the union of the two
axes ``xy = 0`` leaves the ``y``-axis, and the result is presented over the same
polynomial ring and the same scalars as the first cut, not stacked on top of it
as a second quotient object.
"""

from dzack_research.preamble.all import (
    FinitelyPresentedAlgebra,
    PolynomialRing,
    QQ,
)


def test_a_second_cut_stays_on_the_first_presentation() -> None:
    plane = PolynomialRing(QQ, "x,y")
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    axes = FinitelyPresentedAlgebra(plane, [x * y])

    axis = FinitelyPresentedAlgebra(axes, [axes(x)])

    assert axis.presentation_ring() is plane
    assert axis.base_ring() is QQ


def test_the_second_cut_imposes_both_relations() -> None:
    plane = PolynomialRing(QQ, "x,y")
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    axes = FinitelyPresentedAlgebra(plane, [x * y])

    axis = FinitelyPresentedAlgebra(axes, [axes(x)])

    assert axis(x) == axis.zero()
    assert axis(y) != axis.zero()
    assert axis(y) ** 2 != axis.zero()
