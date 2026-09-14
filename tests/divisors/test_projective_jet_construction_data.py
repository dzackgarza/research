from dzack_research.preamble.all import ProjectiveSpace, QQ


def test_projective_jet_space_consumes_its_selected_local_data() -> None:
    line = ProjectiveSpace(1, QQ, names=("x", "y"))
    bundle = line.O(1)
    point = line.point_morphism((1, 1))

    evaluation = bundle.jet_evaluation(point, 1)
    jet = evaluation.codomain()

    assert jet.jet_projective_space() is line
    assert jet.jet_line_bundle() is bundle
    assert jet.jet_point() is point
    assert jet.jet_order() == 1
    assert jet.jet_local_quotient().base_ring() is jet.jet_stalk()
