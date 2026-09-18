"""Analytic disc families use complex-manifold topology and an algebraic analytification bridge."""

from dzack_research.preamble.categories.manifolds import ComplexManifolds
from dzack_research.preamble.categories.schemes.analytic_families import (
    AnalyticDiscFamily,
)


def test_selected_disc_family_is_an_actual_holomorphic_family_over_an_open_disc() -> None:
    family = AnalyticDiscFamily()
    base = family.analytic_base()
    total = family.analytic_total_space()
    arrow = family.analytic_family_morphism()

    assert base in ComplexManifolds()
    assert total in ComplexManifolds()
    assert base.is_open_submanifold()
    assert total.is_open_submanifold()
    assert base.disc_radius() == 1.0
    assert arrow.domain() is total
    assert arrow.codomain() is base
    assert family in ComplexManifolds().SliceOver(base)
    assert family.analytic_family_object() is family
    assert arrow.coordinate_expressions() == (
        total.atlas()["standard"].coordinate(1),
    )
    assert family.analytic_family_object().arrow() is arrow


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


def test_affine_analytic_family_does_not_claim_unrepresented_comparisons() -> None:
    family = AnalyticDiscFamily()

    assert family.coherent_gaga_applies() is False
    assert not hasattr(family, "coherent_cohomology_comparison")
    assert not hasattr(family, "formal_comparison")
