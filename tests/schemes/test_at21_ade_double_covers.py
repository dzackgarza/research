r"""AT21 double covers are live toric-pyramid hypersurfaces with their boundary data."""

from dzack_research.preamble.all import ADELogPairs, QQ, Schemes


def test_d4_cover_is_the_pyramid_hypersurface_with_projection_and_deck_involution() -> None:
    pair = ADELogPairs(QQ).at21("D", 4)
    cover = pair.double_cover(pair.source_normal_form_section(constant=1))

    assert cover.scheme() is cover
    assert cover in Schemes(QQ)
    assert cover.scheme().inclusion().codomain() is cover.ambient_toric_threefold()
    assert cover.cover_morphism().domain() is cover.scheme()
    assert cover.cover_morphism().codomain() is pair.scheme()
    assert cover.ambient_toric_threefold().polarizing_polytope() is pair.pyramid()
    assert cover.deck_involution().domain() is cover.scheme()
    assert cover.deck_involution().codomain() is cover.scheme()

    for cone in cover.scheme().gluing_datum().chart_indices():
        deck = cover.local_deck_involution(cone)
        assert deck * deck == deck.domain().categorical_identity_morphism()
        assert cover.local_cover_map(cone) * deck == cover.local_cover_map(cone)


def test_branch_ramification_and_pulled_boundary_are_actual_closed_subschemes() -> None:
    pair = ADELogPairs(QQ).at21("D", 4)
    cover = pair.double_cover(pair.source_normal_form_section(constant=1))

    assert cover.branch_subscheme().inclusion().codomain() is pair.scheme()
    assert cover.ramification_subscheme().inclusion().codomain() is cover.scheme()
    assert cover.base_boundary_subscheme().inclusion().codomain() is pair.scheme()
    assert cover.boundary_subscheme().inclusion().codomain() is cover.scheme()
    boundary = cover.boundary_divisor()
    assert tuple(boundary.parent().components(boundary)) == (cover.boundary_subscheme(),)
    scheme, log_boundary = cover.equipped_pair()
    assert scheme is cover.scheme()
    assert set(log_boundary.parent().components(log_boundary)) == {
        cover.boundary_subscheme(),
        cover.ramification_subscheme(),
    }


def test_e8_source_orbit_retains_local_global_singularity_comparison() -> None:
    pair = ADELogPairs(QQ).at21("E", 8)
    cover = pair.double_cover(pair.source_normal_form_section(constant=0))
    comparison = dict(cover.local_global_singularity_comparison())

    assert cover.dynkin_diagram().cardinality() == 8
    assert comparison["global_dynkin_rank"] == 8
    assert comparison["local_milnor_number"] == 8
    assert comparison["local_tjurina_number"] == 8
