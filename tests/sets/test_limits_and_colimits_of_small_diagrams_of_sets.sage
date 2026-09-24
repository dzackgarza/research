r"""Limits and colimits in $\mathbf{Set}$ over small poset shapes, pullbacks and pushouts.

The limit of the constant diagram with value $S$ over a connected category
is $S$, and so is its colimit; over the discrete category on two objects the
limit is $S \times S$ and the colimit $S \sqcup S$.  For $S = \{0, 1\}$
these have $2, 2, 4, 4$ elements.  The fiber product of
$f : \{0, \dots, 3\} \to \{0, 1\}$, $n \mapsto n \bmod 2$, and
$g : \{0, 1, 2\} \to \{0, 1\}$, $0 \mapsto 0$, $1, 2 \mapsto 1$, is
$\{(a, b) : f(a) = g(b)\}$, with $2 \cdot 1 + 2 \cdot 2 = 6$ elements.  The
pushout of two points glued at one point is the wedge, with $2 + 2 - 1 = 3$
elements.  Each value is the definition of the limit or colimit in
$\mathbf{Set}$.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403


def _cospan_shape():
    return PosetCategory(Sets()(("a", "b", "c")), le=lambda left, right: left == right or right == "c")


def _span_shape():
    return PosetCategory(Sets()(("a", "b", "c")), le=lambda left, right: left == right or left == "c")


def _discrete_shape():
    return PosetCategory(Sets()(("a", "b")), le=lambda left, right: left == right)


def test_the_constant_diagram_on_the_cospan_shape_has_limit_and_colimit_two_points() -> None:
    shape = _cospan_shape()
    diagram = Cat().Mor(shape, Sets()).constant_functor(Sets.Δ[1])

    assert Sets().Limits(shape).construction(diagram).object().cardinality() == cardinal(2)
    assert Sets().Colimits(shape).construction(diagram).object().cardinality() == cardinal(2)


def test_the_constant_diagram_on_the_span_shape_has_limit_two_points() -> None:
    shape = _span_shape()
    diagram = Cat().Mor(shape, Sets()).constant_functor(Sets.Δ[1])

    assert Sets().Limits(shape).construction(diagram).object().cardinality() == cardinal(2)


def test_the_constant_diagram_on_the_span_shape_has_colimit_two_points() -> None:
    shape = _span_shape()
    diagram = Cat().Mor(shape, Sets()).constant_functor(Sets.Δ[1])

    assert Sets().Colimits(shape).construction(diagram).object().cardinality() == cardinal(2)


def test_the_limit_over_two_discrete_objects_is_the_product() -> None:
    shape = _discrete_shape()
    diagrams = Cat().Mor(shape, Sets())
    diagram = diagrams.constant_functor(Sets.Δ[1])

    assert Sets().Limits(shape).construction(diagram).object().cardinality() == cardinal(4)
    assert Sets().limit_functor(shape)(diagrams.object(diagram)).cardinality() == cardinal(4)


def test_the_colimit_over_two_discrete_objects_is_the_disjoint_union() -> None:
    shape = _discrete_shape()
    diagrams = Cat().Mor(shape, Sets())
    diagram = diagrams.constant_functor(Sets.Δ[1])

    assert Sets().Colimits(shape).construction(diagram).object().cardinality() == cardinal(4)
    assert Sets().colimit_functor(shape)(diagrams.object(diagram)).cardinality() == cardinal(4)


def test_the_fiber_product_of_parity_and_a_two_class_map_has_six_elements() -> None:
    parity_source = Sets.Δ[3]
    other_source = Sets.Δ[2]
    bits = Sets.Δ[1]
    parity = Sets().Mor(parity_source, bits)(lambda n: bits(n % 2))
    nonzero = Sets().Mor(other_source, bits)(lambda n: bits(0) if n == 0 else bits(1))

    assert Sets().fiber_product(parity, nonzero).cardinality() == cardinal(6)


def test_two_points_glued_at_a_point_form_a_three_point_wedge() -> None:
    point = Sets.Δ[0]
    two = Sets.Δ[1]
    at_zero = Sets().Mor(point, two)(lambda _p: two(0))
    span = Sets().span(at_zero, at_zero)

    assert span.apex() is point
    assert span.left_leg() == at_zero
    assert Sets().pushout(at_zero, at_zero).cardinality() == cardinal(3)
    assert span.pushout().cardinality() == cardinal(3)
