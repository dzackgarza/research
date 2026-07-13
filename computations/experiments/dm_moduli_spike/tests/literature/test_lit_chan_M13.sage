r"""Tier-1 literature oracle: Chan's explicit `\overline{\mathcal M}_{1,3}` example.

* Chan, *Tropical curves and metric graphs* (2012), Example 4.3 / Figure 4:
  the banana dual graph with open stack presentation
  `[M_{0,4} \times M_{0,3} / C_2]`, where the product side is identified with
  `M_{0,4}` up to `C_2` branch exchange on the parallel edges.
"""

from __future__ import annotations

from dm_moduli_spike import DMCompactificationModel, ModuliFactor, StableGraphTypes
from dm_moduli_spike.objects.edge_orbits import _elementary_contraction_data
from tests.support.fixtures import chan_m13_curve_type, induced_edge_permutation_group


def test_chan_M13_open_stack_is_quotient_M04_over_C2():
    r"""Chan Example 4.3: open stack `[M_{0,4}/C_2]` with clutching factors `(0,3)+(0,4)`.

    The clutching source records `M_{0,4} \times M_{0,3}`; on the banana vertex
    the four half-edges (two markings plus two edge branches) index `M_{0,4}`,
    and `C_2` exchanges the parallel edge branches while fixing the markings.
    """
    types = StableGraphTypes(1, 3)
    gamma = chan_m13_curve_type(types)
    stratum = DMCompactificationModel(1, 3).stratum(gamma)
    presentation = stratum.open_stack_presentation()
    assert presentation.group_order() == 2
    assert presentation.dimension() == 1
    assert sorted((factor.genus(), factor.number_of_markings()) for factor in presentation.product()) == [(0, 3), (0, 4)]
    assert sorted((factor.genus(), factor.number_of_markings()) for factor in stratum.clutching_morphism().source_factors()) == [(0, 3), (0, 4)]
    banana_factor = next(factor for factor in presentation.product() if factor.number_of_markings() == 4)
    assert banana_factor == ModuliFactor(0, 4, flags=banana_factor.flags())
    edge_action = presentation.automorphism_action().on_edges()
    assert any(image[0] != 0 or image[1] != 1 for image in edge_action)


def test_chan_M13_clutching_factors():
    r"""Chan Example 4.3: clutching source factors `M_{0,3}` and `M_{0,4}`."""
    types = StableGraphTypes(1, 3)
    gamma = chan_m13_curve_type(types)
    stratum = DMCompactificationModel(1, 3).stratum(gamma)
    factors = stratum.clutching_morphism().source_factors()
    assert len(factors) == 2
    assert sorted((factor.genus(), factor.number_of_markings()) for factor in factors) == [(0, 3), (0, 4)]
    presentation = stratum.open_stack_presentation()
    assert presentation.group_order() == 2
    assert presentation.dimension() == 1


def test_chan_M13_edge_automorphism_and_contraction_targets():
    r"""Chan Example 4.3: `C_2` edge action collapses parallel contractions to one target."""
    types = StableGraphTypes(1, 3)
    gamma = chan_m13_curve_type(types)
    group = induced_edge_permutation_group(gamma.automorphism_action())
    assert group.order() == 2
    data = _elementary_contraction_data(gamma)
    assert len(data) == 1
    targets = {target.canonical_key() for target, _witness, _size in data}
    assert len(targets) == 1
    graph = gamma.canonical_representative()
    images = []
    for edge in graph.internal_edges():
        image, _ = graph.contract(edge)
        images.append(image.canonical_key())
    assert len(set(images)) == 1


def test_chan_M13_markings_fixed_and_quotient_presentation():
    r"""Chan Example 4.3: markings fixed under `C_2`; quotient presentation dimension one."""
    types = StableGraphTypes(1, 3)
    gamma = chan_m13_curve_type(types)
    action = gamma.automorphism_action()
    for marking_perm in action.on_markings():
        assert marking_perm == (1, 2, 3)
    stratum = DMCompactificationModel(1, 3).stratum(gamma)
    presentation = stratum.open_stack_presentation()
    assert presentation.group_order() == 2
    assert sorted((factor.genus(), factor.number_of_markings()) for factor in presentation.product()) == [(0, 3), (0, 4)]
    assert presentation.dimension() == 1
