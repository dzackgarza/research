r"""Plane cubics with a double point form a six-dimensional projective system."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_cubics_with_a_double_coordinate_point() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    bundle = plane.O(3)
    point = plane.point_morphism((1, 0, 0))
    system = bundle.imposed_multiplicity_linear_system(point, 2)

    assert system in ImposedMultiplicityLinearSystems(QQ)
    assert system.ambient_section_space().dimension() == 10
    assert system.constrained_section_space().dimension() == 7
    evaluation = system.imposed_jet_evaluation()
    assert evaluation.domain() is system.ambient_section_space()
    assert evaluation.kernel() is system.constrained_section_space()
    assert evaluation.codomain().jet_order() == 2
    assert evaluation.codomain().jet_point() is point
    assert system.imposed_vanishing_order() == 2
    assert system.projective_dimension() == 6
