r"""A span is an object, and it owns its pushout.

A span :math:`A\leftarrow C\to B` is an apex with one arrow to each of two
objects, so it is a cone over the discrete diagram on those two and needs no
shape vocabulary beyond the one the diagram layer already has.  Being an
object, it has an apex, two legs, a diagram, and a colimit it asks its
category for.
"""

from dzack_research.preamble.all import (
    Sets,
    Span,
    cardinal,
)


def _two_element_span():
    r"""``2 <- 1 -> 3`` in sets, both legs picking the first element."""
    apex = Sets.Δ[0]
    left_foot = Sets.Δ[1]
    right_foot = Sets.Δ[2]
    left_leg = Sets().Mor(apex, left_foot)(lambda _value: left_foot(0))
    right_leg = Sets().Mor(apex, right_foot)(lambda _value: right_foot(0))
    return Span(left_leg, right_leg), apex, left_leg, right_leg


def test_a_span_holds_its_apex_and_both_legs() -> None:
    span, apex, left_leg, right_leg = _two_element_span()

    assert span.apex() is apex
    assert span.left_leg() == left_leg
    assert span.right_leg() == right_leg
    assert span.left_leg().domain() is span.right_leg().domain()


def test_a_span_is_a_cone_over_its_own_diagram() -> None:
    span, _apex, left_leg, right_leg = _two_element_span()
    diagram = span.diagram()

    assert span in span.cone_category()
    assert diagram(diagram.domain()(0)) is left_leg.codomain()
    assert diagram(diagram.domain()(1)) is right_leg.codomain()


def test_a_span_owns_its_pushout() -> None:
    r"""Two feet of two and three points glued along one point make four."""
    span, _apex, _left_leg, _right_leg = _two_element_span()

    glued = span.pushout()

    assert glued.cardinality() == cardinal(4)


def test_the_category_builds_the_span_its_pushout_is_taken_over() -> None:
    _span, _apex, left_leg, right_leg = _two_element_span()

    built = Sets().span(left_leg, right_leg)

    assert built.left_leg() == left_leg
    assert built.pushout().cardinality() == cardinal(4)
