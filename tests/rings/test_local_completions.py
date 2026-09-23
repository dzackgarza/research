r"""Adic completion objects and their finite quotient systems."""

from dzack_research.preamble.all import (
    QQ,
)
from dzack_research.preamble.categories.abstract_categories.products import InverseSystem




def test_multivariable_origin_completion_is_not_truncated_by_computation_precision() -> None:
    plane = QQ.polynomial_ring(("x", "y"))
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    completion = plane.adic_completion(plane.ideal(x, y), precision=4)

    xhat = completion.completion_map()(x)
    yhat = completion.completion_map()(y)
    assert xhat**4 != completion.zero()
    assert yhat**4 != completion.zero()
    fourth = completion.adic_projection(4)
    fifth = completion.adic_projection(5)
    assert fourth(xhat**4) == fourth.codomain().zero()
    assert fifth(xhat**4) != fifth.codomain().zero()
    assert completion.computation_precision() == 4


def test_completion_retains_the_adic_inverse_system_and_transition_maps() -> None:
    plane = QQ.polynomial_ring(("x", "y"))
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    completion = plane.adic_completion(plane.ideal(x, y), precision=5)

    fourth = completion.adic_truncation(4)
    second = completion.adic_truncation(2)
    transition = completion.adic_transition_map(4, 2)
    fourth_projection = completion.adic_projection(4)
    second_projection = completion.adic_projection(2)

    assert completion is not fourth
    assert completion is not second
    assert transition.domain() is fourth
    assert transition.codomain() is second
    assert transition(fourth.quotient_map()(x)) == second.quotient_map()(x)
    assert transition(fourth.quotient_map()(x**2)) == second.zero()
    assert transition * fourth_projection == second_projection

    system = completion.adic_inverse_system()
    diagram = system.functor()
    base = system.base_index_category()
    opposite = system.index_category()
    fourth_index = opposite(base(3))
    assert system in InverseSystem(base, diagram.codomain())
    assert system.stage(fourth_index) is fourth
    limit = completion.adic_limit_construction()
    assert limit.diagram() is diagram
    assert limit.object() is completion
    assert limit.structure_morphism(fourth_index) is completion.adic_projection(4)
    assert limit.factor(limit.cone()).apex_map() == completion.Mor(completion).identity()


