r"""Projective jets are local quotients at actual represented rational points."""

from dzack_research.preamble.all import QQ, ProjectiveSpace


def test_noncoordinate_projective_point_jet_retains_stalk_and_local_quotient() -> None:
    plane = ProjectiveSpace(2, QQ)
    bundle = plane.O(2)
    point = plane.point_morphism((1, 2, 3))

    evaluation = bundle.jet_evaluation(point, 2)
    jets = evaluation.codomain()

    assert evaluation.domain() is bundle.global_sections()
    assert jets.jet_line_bundle() is bundle
    assert jets.jet_point() is point
    assert jets.jet_affine_chart() is plane.standard_affine_chart(0)
    assert jets.jet_spectrum_point().local_ring() is jets.jet_stalk()
    assert jets.jet_stalk().maximal_ideal() == jets.jet_maximal_ideal()
    assert jets.jet_local_quotient().quotient_source() is jets.jet_stalk()
    assert jets.jet_local_quotient().defining_ideal() == jets.jet_maximal_ideal().power(2)
    assert jets.jet_residue_field() is jets.jet_spectrum_point().residue_field()
    assert jets.jet_order() == 2
    assert jets.dimension() == 3
    assert evaluation.kernel().dimension() == 3


def test_double_point_condition_is_nonreduced_and_stronger_than_value_evaluation() -> None:
    plane = ProjectiveSpace(2, QQ)
    bundle = plane.O(2)
    point = plane.point_morphism((1, 2, 3))

    values = bundle.jet_evaluation(point, 1)
    doubles = bundle.jet_evaluation(point, 2)

    assert values.codomain().dimension() == 1
    assert doubles.codomain().dimension() == 3
    assert doubles.codomain().jet_maximal_ideal().power(2) != doubles.codomain().jet_maximal_ideal()
    assert doubles.kernel().dimension() < values.kernel().dimension()


def test_noncoordinate_imposed_multiplicity_parameter_space_retains_actual_condition() -> None:
    plane = ProjectiveSpace(2, QQ)
    bundle = plane.O(3)
    point = plane.point_morphism((1, 1, 2))

    system = bundle.imposed_multiplicity_linear_system(point, 2)

    assert system.ambient_section_space() is bundle.global_sections()
    assert system.imposed_jet_evaluation().codomain().jet_point() is point
    assert system.constrained_section_space() is system.imposed_jet_evaluation().kernel()
    assert system.projective_dimension() == int(system.constrained_section_space().dimension()) - 1
