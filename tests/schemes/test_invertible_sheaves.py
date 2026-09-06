r"""Rank-one locally free sheaves from a 1-cocycle of transition units.

An invertible sheaf trivialized on a distinguished affine cover is the free
rank-one module on each chart glued by units on the overlaps.  Tensoring
multiplies the cocycles, so the tensor powers and the dual are the same cover
with the units raised to an integer power, which is what makes the classes a
group.  The specimen is the two-chart cover of the affine line by ``D(x)``
and ``D(1 - x)``.
"""

import pytest

from dzack_research.preamble.all import (
    PolynomialRing,
    QQ,
    Schemes,
    Spec,
)


def _two_chart_cover():
    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    overlap_algebra = cover.intersection(0, 1).coordinate_algebra()
    restriction = scheme.structure_sheaf().restriction_map(scheme, cover.intersection(0, 1))
    return scheme, algebra, x, cover, overlap_algebra, restriction


def test_a_unit_cocycle_glues_a_rank_one_sheaf_that_is_free_on_each_chart() -> None:
    scheme, algebra, x, cover, overlap_algebra, restriction = _two_chart_cover()
    unit = restriction(x)

    line_bundle = cover.glue_invertible_module({(0, 1): unit})

    assert line_bundle.scheme() is scheme
    assert line_bundle.cover() is cover
    assert line_bundle.transition_unit(0, 1) == unit
    # Reading the cocycle the other way inverts the unit, which is what makes
    # the two trivializations agree in both directions.
    assert line_bundle.transition_unit(1, 0) == unit.inverse_of_unit()
    # Each chart carries the free rank-one module over its own section ring.
    for index in (0, 1):
        chart_sections = line_bundle.sections_on_chart(index)
        assert chart_sections.base_ring() is cover.open(index).coordinate_algebra()
        assert chart_sections.module_generating_set().cardinality() == 1


def test_the_tensor_powers_raise_the_cocycle_and_the_dual_inverts_it() -> None:
    scheme, algebra, x, cover, overlap_algebra, restriction = _two_chart_cover()
    unit = restriction(x)
    line_bundle = cover.glue_invertible_module({(0, 1): unit})

    cube = line_bundle.tensor_power(3)
    dual = line_bundle.dual_sheaf()
    trivial = line_bundle.tensor_power(0)

    assert cube.transition_unit(0, 1) == unit**3
    assert dual.transition_unit(0, 1) == unit.inverse_of_unit()
    assert trivial.transition_unit(0, 1) == overlap_algebra.one()
    # L tensor L^{-1} is the structure sheaf: the cocycles cancel.
    assert line_bundle.tensor_product(dual).transition_unit(0, 1) == overlap_algebra.one()
    # Tensoring adds the exponents.
    assert line_bundle.tensor_product(cube).transition_unit(0, 1) == unit**4


def test_a_global_section_is_a_compatible_pair_of_local_sections() -> None:
    r"""``L`` glued by ``x`` has the section that is ``1`` on ``D(x)`` and ``x`` on ``D(1-x)``."""
    scheme, algebra, x, cover, overlap_algebra, restriction = _two_chart_cover()
    line_bundle = cover.glue_invertible_module({(0, 1): restriction(x)})
    sections = line_bundle.global_sections()

    left = line_bundle.sections_on_chart(0)
    right = line_bundle.sections_on_chart(1)
    left_generator = left.module_generator(0)
    right_generator = right.module_generator(0)
    right_x = scheme.structure_sheaf().restriction_map(scheme, cover.open(1))(x)

    compatible = sections((left_generator, right.scalar_multiple(right_x, right_generator)))
    assert compatible in sections
    assert compatible.component(0) == left_generator

    # The pair that ignores the transition is not a section.
    with pytest.raises(ValueError, match="do not agree"):
        sections((left_generator, right_generator))


def test_gluing_schemes_states_the_representation_it_would_need() -> None:
    scheme, algebra, x, cover, overlap_algebra, restriction = _two_chart_cover()

    with pytest.raises(AssertionError, match="owned scheme morphism"):
        Schemes(QQ).glue((scheme,), (cover.open(0),), {})
