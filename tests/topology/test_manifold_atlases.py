from sage.rings.infinity import Infinity

from dzack_research.preamble.categories.manifolds import (
    ComplexManifolds,
    DifferentiableManifolds,
    SmoothManifolds,
    TopologicalManifolds,
)
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces


def _two_chart_translation(manifold, shift):
    source = manifold.chart("x", "x")
    target = manifold.chart("y", "y")
    x = source.coordinate(0)
    y = target.coordinate(0)
    transition = source.transition_to(target, (x + shift,), (y - shift,))
    return source, target, transition


def test_topological_atlas_retains_labels_and_nonidentity_transition() -> None:
    manifold = TopologicalManifolds()(1, "T")
    source, target, transition = _two_chart_translation(manifold, 1)

    assert manifold in TopologicalManifolds()
    assert manifold in TopologicalSpaces()
    assert manifold.regularity() == "topological"
    assert tuple(manifold.chart_labels()) == ("x", "y")
    assert manifold.atlas()["x"] is source
    assert manifold.atlas()["y"] is target
    assert transition.source() is source
    assert transition.target() is target
    assert tuple(transition.forward_expressions()) == (source.coordinate(0) + 1,)
    assert tuple(transition.inverse_expressions()) == (target.coordinate(0) - 1,)
    assert source.coordinate(0).parent() is target.coordinate(0).parent()
    assert all(
        expression.parent() is source.coordinate(0).parent()
        for expression in transition.forward_expressions()
    )
    assert transition.inverse().inverse() is transition
    assert manifold.transition("y", "x") is transition.inverse()


def test_finite_Ck_atlas_retains_exact_differentiability_degree() -> None:
    manifold = DifferentiableManifolds()(1, "C2", 2)
    source, target, transition = _two_chart_translation(manifold, 2)

    assert manifold in DifferentiableManifolds()
    assert manifold in TopologicalManifolds()
    assert manifold in TopologicalSpaces()
    assert manifold.differentiability_degree() == 2
    assert manifold.regularity() == "C^2"
    assert not manifold.is_smooth()
    assert transition.regularity() == "C^2"
    assert tuple(transition.forward_expressions()) == (source.coordinate(0) + 2,)
    assert tuple(transition.inverse_expressions()) == (target.coordinate(0) - 2,)


def test_smooth_atlas_is_a_differentiable_and_topological_atlas() -> None:
    manifold = SmoothManifolds()(1, "S")
    source, target, transition = _two_chart_translation(manifold, 3)

    assert manifold in SmoothManifolds()
    assert manifold in DifferentiableManifolds()
    assert manifold in TopologicalManifolds()
    assert manifold in TopologicalSpaces()
    assert manifold.differentiability_degree() == Infinity
    assert manifold.regularity() == "smooth"
    assert manifold.is_smooth()
    assert transition.regularity() == "smooth"
    assert tuple(transition.forward_expressions()) == (source.coordinate(0) + 3,)
    assert tuple(transition.inverse_expressions()) == (target.coordinate(0) - 3,)


def test_holomorphic_map_retains_its_selected_chart_presentation() -> None:
    line = ComplexManifolds().affine_space(1, name="C")
    chart = line.atlas()["standard"]
    z = chart.coordinate(0)

    square = line.holomorphic_polynomial_map(line, (z**2,))
    presentation = square.presentation()

    assert tuple(presentation.coordinate_expressions()) == (z**2,)
    assert presentation.coordinate_expressions()[0].parent() is z.parent()
    assert presentation.source_chart_label() == "standard"
    assert presentation.target_chart_label() == "standard"
    assert square.source_chart() is chart
    assert square.target_chart() is chart
