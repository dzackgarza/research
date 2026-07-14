r"""Tier-3 differential check: backend adapters must not leak third-party types.

Not a literature oracle — agreement with ``admcycles`` is tier-3 CAS differential evidence.
"""

from __future__ import annotations

from dm_moduli_spike.objects.stable_graphs import StableGraph, StableGraphs
from dm_moduli_spike.objects.model import _enumerate_stable_graph_levels

from dm_moduli_spike.backends.admcycles_decorated import AdmcyclesDecoratedGraphBackend
from dm_moduli_spike.backends.admcycles_stable import AdmcyclesStableGraphBackend


def test_stable_backend_returns_owned_curve_types_only():
    backend = AdmcyclesStableGraphBackend()
    types = StableGraphs(1, 2)
    pure_keys = {
        gamma.canonical_key()
        for level in _enumerate_stable_graph_levels(1, 2, backend="pure-sage").curve_type_levels()
        for gamma in level
    }
    produced = backend.stable_curve_types(types)
    produced_keys = {gamma.canonical_key() for gamma in produced}
    assert produced_keys == pure_keys
    assert all(isinstance(gamma, StableGraph) for gamma in produced)
    assert all(gamma.parent() == types for gamma in produced)


def test_decorated_backend_matches_pure_sage_canonical_keys():
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0)]:
        pure = _enumerate_stable_graph_levels(g, n, backend="pure-sage")
        decorated = _enumerate_stable_graph_levels(g, n, backend="admcycles-decorated")
        assert decorated.is_complete()
        assert decorated.backend() == "admcycles-decorated"
        pure_keys = {
            gamma.canonical_key()
            for level in pure.curve_type_levels()
            for gamma in level
        }
        decorated_keys = {
            gamma.canonical_key()
            for level in decorated.curve_type_levels()
            for gamma in level
        }
        assert pure_keys == decorated_keys
        produced = AdmcyclesDecoratedGraphBackend().stable_curve_types(StableGraphs(g, n))
        produced_keys = {gamma.canonical_key() for gamma in produced}
        assert produced_keys == pure_keys
        assert all(
            isinstance(gamma, StableGraph) and gamma.parent() == StableGraphs(g, n)
            for gamma in produced
        )


def test_decorated_backend_rank_buckets_match_edge_counts():
    stratification = _enumerate_stable_graph_levels(1, 2, backend="admcycles-decorated")
    for codim, level in enumerate(stratification.curve_type_levels()):
        assert all(gamma.num_edges() == codim for gamma in level)


def test_decorated_morphism_adapter_matches_native_contraction():
    from admcycles.decorated_graph import DecoratedGraph

    from dm_moduli_spike.backends.admcycles_decorated import contraction_from_decorated_morphism

    loop = DecoratedGraph([0], [[1]], [(0, 0, 1)])
    loop_morphism = loop.edge_contraction_morphism([(0, 0, 1)])
    loop_contraction = contraction_from_decorated_morphism(loop_morphism, 1, 1)
    assert loop_contraction.target_type().is_smooth()

    parallel = DecoratedGraph([0, 0], [[1], [2]], [(0, 1, 2)])
    parallel_morphism = parallel.edge_contraction_morphism([(0, 1, 1)])
    adapted = contraction_from_decorated_morphism(parallel_morphism, 1, 2)
    types = StableGraphs(1, 2)
    theta = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    graph = theta.canonical_representative()
    _, native = graph.contract(graph.internal_edges()[0])
    assert adapted.target_type() == native.target_type()


def test_decorated_converter_expands_loops_and_parallel_multiplicities():
    from admcycles.decorated_graph import DecoratedGraph

    from dm_moduli_spike.backends.admcycles_decorated import _record_from_decorated_graph

    loop = DecoratedGraph([0], [[1]], [(0, 0, 1)])
    loop_record = _record_from_decorated_graph(loop, 1, 1)
    assert loop_record.num_edges() == 1

    parallel = DecoratedGraph([0, 0], [[1], [2]], [(0, 1, 2)])
    parallel_record = _record_from_decorated_graph(parallel, 1, 2)
    assert parallel_record.num_edges() == 2


def test_auto_backend_prefers_decorated_when_available():
    auto = _enumerate_stable_graph_levels(0, 4, backend="auto")
    decorated = _enumerate_stable_graph_levels(0, 4, backend="admcycles-decorated")
    assert auto.is_complete()
    assert auto.backend() == "admcycles-decorated"
    assert auto.rank_sizes() == decorated.rank_sizes()


def test_record_to_stable_graph_roundtrip_preserves_type():
    from dm_moduli_spike.backends.admcycles_stable import _record_from_stable_graph, _record_to_stable_graph

    types = StableGraphs(1, 2)
    theta = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    graph = theta.canonical_representative()
    stable = _record_to_stable_graph(graph, 1, 2)
    roundtrip = _record_from_stable_graph(stable, 1, 2)
    assert types.from_graph(roundtrip) == theta


def test_stable_backend_aut_number_agrees_via_owned_roundtrip():
    from dm_moduli_spike.backends.admcycles_stable import _record_from_stable_graph

    backend = AdmcyclesStableGraphBackend()
    types = StableGraphs(1, 2)
    for level in _enumerate_stable_graph_levels(1, 2, backend="pure-sage").curve_type_levels():
        for gamma in level:
            stable = backend.to_admcycles(types, gamma)
            assert types.from_graph(_record_from_stable_graph(stable, 1, 2)) == gamma
            assert gamma.automorphism_number() == backend.admcycles_automorphism_number(types, gamma)


def test_record_to_decorated_graph_roundtrip_preserves_type():
    from dm_moduli_spike.backends.admcycles_decorated import _record_from_decorated_graph, _record_to_decorated_graph

    types = StableGraphs(1, 2)
    theta = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    graph = theta.canonical_representative()
    decorated = _record_to_decorated_graph(graph, 1, 2)
    roundtrip = _record_from_decorated_graph(decorated, 1, 2)
    assert types(roundtrip) == theta


def test_decorated_stratification_covers_have_upstream_morphisms():
    from admcycles.decorated_graph import DecoratedGraph

    from dm_moduli_spike.backends.admcycles_decorated import (
        _record_to_decorated_graph,
        contraction_from_decorated_morphism,
    )

    for g, n in [(1, 1), (1, 2), (2, 0)]:
        stratification = _enumerate_stable_graph_levels(g, n, backend="admcycles-decorated")
        for witness in stratification.contraction_witnesses():
            domain = witness.domain()
            decorated = _record_to_decorated_graph(domain, g, n)
            matched = False
            for u, v, _size in decorated.edge_orbit_representatives():
                morphism = decorated.edge_contraction_morphism([(u, v, 1)])
                adapted = contraction_from_decorated_morphism(morphism, g, n, domain_graph=domain)
                if adapted.target_type() == witness.target_type():
                    matched = True
                    break
            assert matched, f"no upstream morphism for cover in Mbar({g}, {n})"
