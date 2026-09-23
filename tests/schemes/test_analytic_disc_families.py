"""Analytic disc families use complex-manifold topology and an algebraic analytification bridge."""

from dzack_research.preamble.categories.schemes.analytic_families import (
    AnalyticDiscFamily,
)




def test_disc_family_is_the_restriction_of_the_selected_algebraic_analytification() -> None:
    family = AnalyticDiscFamily()
    total_inclusion, base_inclusion = family.comparison_maps()

    assert family.comparison_square_commutes()
    assert total_inclusion.domain() is family.analytic_total_space()
    assert base_inclusion.domain() is family.analytic_base()
    assert (
        base_inclusion * family.analytic_family_morphism()
        == family.analytified_family_morphism() * total_inclusion
    )


