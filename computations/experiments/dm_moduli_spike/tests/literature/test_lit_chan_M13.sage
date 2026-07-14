r"""Tier-1 literature oracle: Chan's explicit `\overline{\mathcal M}_{1,3}` example.

* Chan, *Tropical curves and metric graphs* (2012), Example 4.3 / Figure 4:
  the banana dual graph with open stack presentation
  `[M_{0,4} \times M_{0,3} / C_2]`, where the product side is identified with
  `M_{0,4}` up to `C_2` branch exchange on the parallel edges.
"""

from __future__ import annotations

from sage.rings.integer_ring import ZZ

from dm_moduli_spike import Mbar_gn, ProductStack, QuotientStack, spec

from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.testing_support.support.fixtures import (
    chan_m13_curve_type,
    induced_edge_permutation_group,
    marking_generator_images,
)


def test_chan_M13_open_stack_is_quotient_M04_over_C2():
    r"""Chan Example 4.3: open stratum is a ``QuotientStack`` with factors `(0,3)+(0,4)`."""
    types = StableGraphs(1, 3)
    gamma = chan_m13_curve_type(types)
    graph = gamma.canonical_representative()
    XSbar = Mbar_gn(1, 3, base=spec(ZZ))
    Sigma = XSbar.stratification()
    S = Sigma.stratum(graph)
    underlying = S.underlying_stack()
    assert isinstance(underlying, QuotientStack)
    assert int(underlying.group().order()) == 2
    assert isinstance(S.clutching_morphism().domain(), ProductStack)
    factors = S.clutching_morphism().domain().factors()
    assert sorted((f.genus(), f.number_of_markings()) for f in factors) == [(0, 3), (0, 4)]
    group = induced_edge_permutation_group(graph)
    assert group.order() == 2


def test_chan_M13_clutching_factors():
    r"""Chan Example 4.3: clutching source is ``ProductStack`` of `Mbar_{0,3}` and `Mbar_{0,4}`."""
    types = StableGraphs(1, 3)
    gamma = chan_m13_curve_type(types)
    graph = gamma.canonical_representative()
    XSbar = Mbar_gn(1, 3, base=spec(ZZ))
    S = XSbar.stratification().stratum(graph)
    xi = S.clutching_morphism()
    assert xi in xi.parent()
    assert xi.codomain() is XSbar
    assert sorted((f.genus(), f.number_of_markings()) for f in xi.domain().factors()) == [(0, 3), (0, 4)]


def test_chan_M13_edge_automorphism_and_contraction_targets():
    r"""Chan Example 4.3: `C_2` edge action collapses parallel contractions to one target."""
    types = StableGraphs(1, 3)
    gamma = chan_m13_curve_type(types)
    group = induced_edge_permutation_group(gamma.canonical_representative())
    assert group.order() == 2
    data = gamma.elementary_contractions()
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
    r"""Chan Example 4.3: markings fixed under `C_2`; quotient Aut order two."""
    types = StableGraphs(1, 3)
    gamma = chan_m13_curve_type(types)
    graph = gamma.canonical_representative()
    for marking_perm in marking_generator_images(graph):
        assert marking_perm == (1, 2, 3)
    XSbar = Mbar_gn(1, 3, base=spec(ZZ))
    S = XSbar.stratification().stratum(graph)
    assert isinstance(S.underlying_stack(), QuotientStack)
    assert int(S.underlying_stack().group().order()) == 2
