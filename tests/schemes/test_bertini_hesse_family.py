r"""The Hesse pencil represents Bertini's good locus without declaring every fibre smooth."""

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.schemes.bertini_families import (
    HesseBertiniFamily,
)


def test_hesse_pencil_retains_its_base_locus_and_actual_jet_maps() -> None:
    application = HesseBertiniFamily()
    system = application.linear_system()
    point = application.basepoint()
    projectivization = system.quotient_projectivization().arrow().domain()
    comparison = system.quotient_projectivization_comparison()

    assert system.projective_dimension() == 1
    assert projectivization.projectivization_module() is system.selected_section_space().dual_module()
    assert comparison.forward().domain() is projectivization
    assert comparison.forward().codomain() is system
    assert application.base_locus_point().codomain() is application.base_locus()
    assert application.base_locus_point().domain() is point.domain()
    assert application.basepoint_value_evaluation().codomain().jet_point() is point
    assert application.basepoint_first_jet_evaluation().codomain().jet_point() is point
    assert application.basepoint_first_jet_evaluation().codomain().jet_order() == 2


def test_hesse_discriminant_is_the_actual_open_good_parameter_locus() -> None:
    application = HesseBertiniFamily()
    parameter_scheme = application.parameter_scheme()
    good = application.good_parameter_locus()
    bad = application.exceptional_parameter_locus()

    assert good.inclusion().codomain() is parameter_scheme
    assert bad.inclusion().codomain() is parameter_scheme
    assert application.discriminant() == application.parameter() ** 3 - application.parameter_ring().one()
    assert application.parameter_is_good(QQ.zero())
    assert not application.parameter_is_good(QQ.one())
    assert application.theorem_hypotheses()
    assert application.theorem_conclusion_is_exact()


def test_smooth_and_exceptional_singular_members_coexist_in_one_complete_intersection_family() -> None:
    application = HesseBertiniFamily()
    smooth = application.general_member()
    singular = application.exceptional_member()

    assert smooth.base_change_source_complete_intersection() is application.family()
    assert singular.base_change_source_complete_intersection() is application.family()
    assert smooth.is_smooth()
    assert not singular.is_smooth()
    assert tuple(smooth.defining_degrees()) == (3,)
    assert tuple(singular.defining_degrees()) == (3,)


def test_family_restricts_to_the_good_open_with_its_projection_map() -> None:
    application = HesseBertiniFamily()
    restricted = application.restriction_to_good_locus()
    projection = application.good_locus_restriction_map()

    assert restricted.scheme_base_ring() is application.good_parameter_locus().coordinate_algebra()
    assert projection.domain() is restricted
    assert projection.codomain() is application.family()
