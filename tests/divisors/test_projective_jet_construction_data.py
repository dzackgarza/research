import pytest

from dzack_research.preamble.all import ProjectiveSpaces, QQ


def test_projective_jet_space_consumes_its_selected_local_data() -> None:
    line = ProjectiveSpaces(QQ)(1, names=("x", "y"))
    bundle = line.O(1)
    point = line.point_morphism((1, 1))

    evaluation = bundle.jet_evaluation(point, 1)
    jet = evaluation.codomain()

    assert jet.jet_projective_space() is line
    assert jet.jet_line_bundle() is bundle
    assert jet.jet_point() is point
    assert jet.jet_order() == 1
    assert jet.jet_local_quotient().base_ring() is jet.jet_stalk()


def test_coordinate_role_is_derived_from_the_selected_jet_point() -> None:
    line = ProjectiveSpaces(QQ)(1, names=("x", "y"))

    coordinate_jet = line.coordinate_point_jet_evaluation(2, 1, 1).codomain()
    assert coordinate_jet.jet_coordinate_index() == 1
    assert "_preamble_jet_coordinate_index" not in coordinate_jet.__dict__

    general_point = line.point_morphism((1, 1))
    general_jet = line.O(2).jet_evaluation(general_point, 1).codomain()
    with pytest.raises(ValueError, match="not selected at a coordinate point"):
        general_jet.jet_coordinate_index()
