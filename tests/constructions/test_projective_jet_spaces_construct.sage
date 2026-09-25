r"""Second-order jets on P^2 at a rational point form a three-dimensional space."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_second_order_jets_of_conics_at_a_rational_point() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    bundle = plane.O(2)
    point = plane.point_morphism((1, 2, 3))
    jets = bundle.jet_evaluation(point, 2).codomain()

    assert jets in ProjectiveJetSpaces(QQ)
    assert jets.jet_line_bundle() is bundle
    assert jets.jet_point() is point
    assert jets.jet_order() == 2
    assert jets.jet_projective_space() is plane
    assert jets.jet_homogeneous_degree() == 2
    assert jets.jet_affine_chart() is plane.standard_affine_chart(0)
    assert jets.jet_spectrum_point().local_ring() is jets.jet_stalk()
    assert jets.jet_local_quotient().quotient_source() is jets.jet_stalk()
    assert jets.jet_maximal_ideal() is jets.jet_stalk().maximal_ideal()
    assert jets.jet_residue_field() == QQ
    assert jets.dimension() == 3


def test_coordinate_point_records_its_standard_chart_index() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    bundle = plane.O(3)
    point = plane.point_morphism((0, 1, 0))
    jets = bundle.jet_evaluation(point, 1).codomain()

    assert jets.jet_coordinate_index() == 1
    assert jets.jet_affine_chart() is plane.standard_affine_chart(1)
    assert jets.jet_homogeneous_degree() == 3
