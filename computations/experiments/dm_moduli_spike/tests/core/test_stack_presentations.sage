r"""Symbolic quotient-stack and clutching presentations of strata."""

from __future__ import annotations

from dm_moduli_spike import DMCompactificationModel, ModuliFactor, StableGraphTypes


def test_open_stack_presentation_factors_and_automorphism_action():
    model = DMCompactificationModel(0, 4)
    types = model.curve_types()
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    stratum = model.stratum(gamma)
    presentation = stratum.open_stack_presentation()
    assert presentation.product() == (
        ModuliFactor(0, 3, flags=(0, 1, 4)),
        ModuliFactor(0, 3, flags=(2, 3, 5)),
    )
    assert presentation.group_order() == gamma.automorphism_number()
    assert not presentation.is_compact()
    assert presentation.dimension() == stratum.dimension()


def test_closure_normalization_uses_compact_factors():
    model = DMCompactificationModel(0, 4)
    types = model.curve_types()
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    stratum = model.stratum(gamma)
    presentation = stratum.closure_normalization_presentation()
    assert presentation.product() == (
        ModuliFactor(0, 3, compact=True, flags=(0, 1, 4)),
        ModuliFactor(0, 3, compact=True, flags=(2, 3, 5)),
    )
    assert all(factor.is_compact() for factor in presentation.product())


def test_clutching_morphism_targets_the_ambient_compactification():
    model = DMCompactificationModel(1, 1)
    types = model.curve_types()
    loop = types.from_vertices(genera=(0,), markings=((1,),), edges=((0, 0),))
    stratum = model.stratum(loop)
    clutching = stratum.clutching_morphism()
    # the nodal cubic glues M(0,3) to itself with a Z/2 branch swap
    assert clutching.source_factors() == (ModuliFactor(0, 3, compact=True, flags=(0, 1, 2)),)
    assert (clutching.genus(), clutching.number_of_markings()) == (1, 1)
    assert clutching.group_order() == 2
    assert clutching.curve_type() == loop


def test_m04_boundary_clutching_maps_are_pairwise_distinct():
    model = DMCompactificationModel(0, 4)
    boundary = model.stratification().boundary_strata()
    clutchings = [stratum.clutching_morphism() for stratum in boundary]
    presentations = [stratum.open_stack_presentation() for stratum in boundary]
    assert len({clutching.curve_type().canonical_key() for clutching in clutchings}) == 3
    assert len(set(clutchings)) == 3
    assert len(set(presentations)) == 3
    assert len({presentation.curve_type().canonical_key() for presentation in presentations}) == 3


def test_stratum_rejects_mismatched_ambient():
    model = DMCompactificationModel(0, 4)
    wrong = DMCompactificationModel(2, 1).curve_types().smooth()
    try:
        model.stratum(wrong)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for mismatched ambient (g, n)")


def test_stratum_is_distinct_from_its_indexing_curve_type():
    model = DMCompactificationModel(1, 1)
    smooth = model.curve_types().smooth()
    stratum = model.stratum(smooth)
    # graph-theoretic vocabulary lives on the curve type
    assert hasattr(smooth, "automorphism_number")
    assert hasattr(smooth, "one_edge_degenerations")
    # stack-geometric vocabulary lives on the stratum
    assert hasattr(stratum, "open_stack_presentation")
    assert not hasattr(smooth, "open_stack_presentation")
    assert not hasattr(stratum, "one_edge_degenerations")
