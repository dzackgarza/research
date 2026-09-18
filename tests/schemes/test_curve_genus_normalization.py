"""Global curve genus is assembled from an actual normalization and local delta data."""

from dzack_research.preamble.categories.schemes.curve_genus import (
    rational_quintic_with_nonrational_node_normalization,
    rational_quintic_with_two_nodes_normalization,
)


def test_two_node_quintic_has_three_local_defects_and_rational_normalization() -> None:
    data = rational_quintic_with_two_nodes_normalization()
    curve = data.curve()
    normalization = data.normalization_curve()

    assert data is curve
    assert curve.normalization_data() is curve
    contributions = tuple(data.local_contributions())

    assert data.normalization_morphism().domain() is normalization
    assert data.normalization_morphism().codomain() is curve
    assert normalization.relative_dimension() == 1
    assert normalization.arithmetic_genus() == 0
    assert curve.arithmetic_genus() == 6
    assert tuple(int(item.delta_invariant()) for item in contributions) == (1, 1, 4)
    assert tuple(int(item.residue_degree()) for item in contributions) == (1, 1, 1)
    assert tuple(int(item.weighted_contribution()) for item in contributions) == (1, 1, 4)
    assert data.total_delta_contribution() == 6
    assert data.genus_comparison().holds()
    assert curve.geometric_genus() == 0
    assert curve.genus_comparison() is data.genus_comparison()


def test_nonrational_singular_point_retains_residue_degree_in_global_delta_sum() -> None:
    data = rational_quintic_with_nonrational_node_normalization()
    curve = data.curve()
    nonrational, infinity = tuple(data.local_contributions())

    assert int(nonrational.residue_degree()) == 2
    assert int(nonrational.delta_invariant()) == 1
    assert int(nonrational.weighted_contribution()) == 2
    assert int(infinity.residue_degree()) == 1
    assert int(infinity.delta_invariant()) == 4
    assert int(infinity.weighted_contribution()) == 4
    assert data.total_delta_contribution() == 6
    assert curve.arithmetic_genus() == 6
    assert curve.geometric_genus() == 0
    assert data.genus_comparison().arithmetic_genus() == (
        data.genus_comparison().geometric_genus()
        + data.genus_comparison().total_delta_contribution()
    )
    assert data.is_geometrically_integral()
    assert data.normalization_is_connected()
