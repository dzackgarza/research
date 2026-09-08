import pytest

from dzack_research.preamble.all import (
    ProjectiveCompleteIntersection,
    ProjectiveCompleteIntersections,
    ProjectiveSpace,
    QQ,
)


def test_projective_complete_intersection_retains_equations_multidegree_and_adjunction_integer() -> None:
    space = ProjectiveSpace(3, QQ)
    x0, x1, x2, x3 = space.gens()
    curve = ProjectiveCompleteIntersection(
        space.closed_subscheme(x0 * x1 - x2**2, x0**3 + x1**3 + x3**3)
    )

    assert curve in ProjectiveCompleteIntersections(QQ)
    assert curve.complete_intersection_ambient() is space
    assert tuple(curve.defining_degrees()) == (2, 3)
    assert curve.complete_intersection_codimension() == 2
    assert curve.expected_dimension() == 1
    assert curve.adjunction_twist_degree() == 1
    assert curve.is_gorenstein()


def test_redundant_homogeneous_equations_are_not_misclassified_as_a_complete_intersection() -> None:
    space = ProjectiveSpace(3, QQ)
    x0, x1, _x2, _x3 = space.gens()
    redundant = space.closed_subscheme(x0, x0 * x1)

    with pytest.raises(ValueError):
        ProjectiveCompleteIntersection(redundant)
