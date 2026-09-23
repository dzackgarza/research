r"""The Hesse pencil represents Bertini's good locus without declaring every fibre smooth."""

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.schemes.bertini_families import (
    HesseBertiniFamily,
)




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


