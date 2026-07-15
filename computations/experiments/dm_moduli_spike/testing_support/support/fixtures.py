"""Named structural fixtures and independent literature oracles."""

from __future__ import annotations

from collections.abc import Iterable
from itertools import combinations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset

    from dm_moduli_spike.objects.records import _GraphRecord
    from dm_moduli_spike.objects.stable_graphs import StableGraph, StableGraphs

BoundaryLabel = tuple[str, ...] | tuple[str, int, frozenset[int]]


def strata_by_codimension(g: int, n: int) -> tuple[tuple[StableGraph, ...], ...]:
    r"""Rank-bucket :class:`StableGraph` classes by edge count (codimension)."""
    from dm_moduli_spike.objects.enumeration import stable_curve_type_levels
    from dm_moduli_spike.objects.stable_graphs import StableGraphs as _StableGraphs

    return tuple(tuple(level.values()) for level in stable_curve_type_levels(_StableGraphs(g, n)))


def rank_sizes(g: int, n: int) -> tuple[int, ...]:
    return tuple(len(bucket) for bucket in strata_by_codimension(g, n))


def strata_of_codim(g: int, n: int, codim: int) -> tuple[StableGraph, ...]:
    from dm_moduli_spike.objects.stable_graphs import StableGraphs as _StableGraphs

    return tuple(gamma for gamma in _StableGraphs(g, n) if gamma.num_edges() == int(codim))


def induced_specialization_poset(types: Iterable[StableGraph]) -> FinitePoset:
    r"""Induced specialization covers on an arbitrary :class:`StableGraph` subset."""
    from sage.combinat.posets.posets import Poset

    graphs = tuple(types)
    covers: list[tuple[StableGraph, StableGraph]] = []
    for delta in graphs:
        for gamma in graphs:
            if gamma == delta or not delta.contracts_to(gamma):
                continue
            if any(theta != gamma and theta != delta and delta.contracts_to(theta) and theta.contracts_to(gamma) for theta in graphs):
                continue
            covers.append((gamma, delta))
    return Poset((graphs, covers), cover_relations=True, facade=True)


CHAN_M20_COVERS: dict[str, tuple[str, ...]] = {
    "VII": ("V", "VI"),
    "V": ("III", "IV"),
    "VI": ("IV",),
    "III": ("I", "II"),
    "IV": ("II",),
}


def stable_pairs(max_genus: int = 3, max_markings: int = 5) -> tuple[tuple[int, int], ...]:
    pairs: list[tuple[int, int]] = []
    for g in range(max_genus + 1):
        for n in range(max_markings + 1):
            if 2 * g - 2 + n > 0:
                pairs.append((g, n))
    return tuple(pairs)


def expected_boundary_labels(g: int, n: int) -> set[BoundaryLabel]:
    labels: set[BoundaryLabel] = set()
    if g >= 1:
        labels.add(("irr",))
    ground = frozenset(range(1, n + 1))
    seen: set[tuple[int, tuple[int, ...]]] = set()
    for a in range(g + 1):
        for size in range(n + 1):
            for subset in combinations(ground, size):
                a_set = frozenset(subset)
                if 2 * a - 1 + len(a_set) <= 0:
                    continue
                if 2 * (g - a) - 1 + (n - len(a_set)) <= 0:
                    continue
                b_set = ground - a_set
                b = g - a
                # Total order: frozenset <= is subset, so incomparable parts must not be compared that way.
                left = (a, tuple(sorted(a_set)))
                right = (b, tuple(sorted(b_set)))
                key = left if left <= right else right
                if key in seen:
                    continue
                seen.add(key)
                labels.add(("sep", key[0], frozenset(key[1])))
    return labels


def boundary_label(curve_type: StableGraph, g: int, n: int) -> BoundaryLabel:
    assert curve_type.codimension() == 1
    record = curve_type._canonical_record()
    if record.num_vertices() == 1 and len(record.internal_edges()) == 1:
        flag, partner = record.internal_edges()[0]
        if record.flag_vertex[flag] == record.flag_vertex[partner]:
            return ("irr",)
    assert record.num_vertices() == 2
    genera = record.vertex_genera
    markings = tuple(frozenset(record.markings_at(vertex)) for vertex in range(2))
    edge = record.internal_edges()[0]
    left = record.flag_vertex[edge[0]]
    right = record.flag_vertex[edge[1]]
    assert left != right
    a = genera[0]
    a_set = markings[0]
    b = genera[1]
    b_set = markings[1]
    left_key = (a, tuple(sorted(a_set)))
    right_key = (b, tuple(sorted(b_set)))
    chosen = left_key if left_key <= right_key else right_key
    return ("sep", chosen[0], frozenset(chosen[1]))


def expected_clutching_signature_irr(g: int, n: int) -> tuple[tuple[int, int], ...]:
    return ((g - 1, n + 2),)


def expected_clutching_signature_sep(g: int, n: int, a: int, marking_set: frozenset[int]) -> tuple[tuple[int, int], ...]:
    b = g - a
    b_set = frozenset(label for label in range(1, n + 1) if label not in marking_set)
    return tuple(
        sorted(
            (
                (a, len(marking_set) + 1),
                (b, len(b_set) + 1),
            )
        )
    )


def clutching_signature(curve_type: StableGraph) -> tuple[tuple[int, int], ...]:
    r"""Sorted ``(g(v), valence(v))`` factors of the clutching source product."""
    record = curve_type._canonical_record()
    return tuple(sorted((record.vertex_genera[v], record.valence(v)) for v in range(record.num_vertices())))


def classify_chan_m20(record: _GraphRecord) -> str:
    genera = record.vertex_genera
    num_vertices = record.num_vertices()
    num_edges = record.num_edges()
    loops = sum(1 for flag, partner in record.internal_edges() if record.flag_vertex[flag] == record.flag_vertex[partner])
    bridges = num_edges - loops

    if num_vertices == 1 and genera == (2,) and num_edges == 0:
        return "VII"
    if num_vertices == 1 and genera == (1,) and loops == 1 and bridges == 0:
        return "V"
    if num_vertices == 2 and genera == (1, 1) and bridges == 1 and loops == 0:
        return "VI"
    if num_vertices == 1 and genera == (0,) and loops == 2:
        return "III"
    if num_vertices == 2 and sorted(genera) == [0, 1] and loops == 1 and bridges == 1:
        return "IV"
    if num_vertices == 2 and genera == (0, 0) and bridges == 3 and loops == 0:
        return "I"
    if num_vertices == 2 and genera == (0, 0) and loops == 2 and bridges == 1:
        return "II"
    raise AssertionError(f"graph does not match any Chan Figure 3 type: V={num_vertices} G={genera} E={num_edges} L={loops}")


def induced_edge_permutation_group(graph: _GraphRecord) -> object:
    r"""Sage ``PermutationGroup`` of `\operatorname{Aut}(G)` acting on edge indices."""
    return graph.automorphism_group(on="edges")


def flag_generator_images(graph: _GraphRecord) -> tuple[tuple[int, ...], ...]:
    r"""0-indexed flag images of Aut generators (test helper)."""
    from dm_moduli_spike.objects._automorphism_action import _GraphAutomorphismData

    return _GraphAutomorphismData.from_graph(graph).on_flags()


def marking_generator_images(graph: _GraphRecord) -> tuple[tuple[int, ...], ...]:
    from dm_moduli_spike.objects._automorphism_action import _GraphAutomorphismData

    return _GraphAutomorphismData.from_graph(graph).on_markings()


def vertex_generator_images(graph: _GraphRecord) -> tuple[tuple[int, ...], ...]:
    from dm_moduli_spike.objects._automorphism_action import _GraphAutomorphismData

    return _GraphAutomorphismData.from_graph(graph).on_vertices()


def edge_generator_images(graph: _GraphRecord) -> tuple[tuple[int, ...], ...]:
    from dm_moduli_spike.objects._automorphism_action import _GraphAutomorphismData

    return _GraphAutomorphismData.from_graph(graph).on_edges()


def chan_m13_curve_type(types: StableGraphs) -> StableGraph:
    return types.from_vertices(
        genera=(0, 0),
        markings=((1, 2), (3,)),
        edges=((0, 1), (0, 1)),
    )


def m11_types(graphs: StableGraphs | None = None) -> tuple[StableGraph, StableGraph]:
    from dm_moduli_spike.objects.stable_graphs import StableGraphs as _StableGraphs

    graphs = graphs if graphs is not None else _StableGraphs(1, 1)
    smooth = next(x for x in graphs if x.num_edges() == 0)
    nodal = next(x for x in graphs if x.num_edges() == 1)
    return smooth, nodal


def m12_types(graphs: StableGraphs | None = None) -> dict[str, StableGraph]:
    from dm_moduli_spike.objects.stable_graphs import StableGraphs as _StableGraphs

    graphs = graphs if graphs is not None else _StableGraphs(1, 2)
    return {
        "A": graphs.from_vertices(
            genera=(1,),
            markings=((1, 2),),
            edges=(),
        ),
        "B": graphs.from_vertices(
            genera=(0,),
            markings=((1, 2),),
            edges=((0, 0),),
        ),
        "C": graphs.from_vertices(
            genera=(0, 1),
            markings=((1, 2), ()),
            edges=((0, 1),),
        ),
        "D": graphs.from_vertices(
            genera=(0, 0),
            markings=((), (1, 2)),
            edges=((0, 0), (0, 1)),
        ),
        "E": graphs.from_vertices(
            genera=(0, 0),
            markings=((1,), (2,)),
            edges=((0, 1), (0, 1)),
        ),
    }


def m20_types(graphs: StableGraphs | None = None) -> dict[str, StableGraph]:
    from dm_moduli_spike.objects.stable_graphs import StableGraphs as _StableGraphs

    graphs = graphs if graphs is not None else _StableGraphs(2, 0)
    by_name: dict[str, StableGraph] = {}
    for gamma in graphs:
        name = classify_chan_m20(gamma._canonical_record())
        assert name not in by_name, f"duplicate Chan type {name}"
        by_name[name] = gamma
    assert set(by_name) == set(CHAN_M20_COVERS) | {"I", "II", "III", "IV", "V", "VI", "VII"}
    return by_name


def genus_six_counterexample() -> StableGraph:
    from dm_moduli_spike.objects.stable_graphs import StableGraphs

    types = StableGraphs(6, 0)
    return types.from_vertices(
        genera=(1, 0, 1, 0, 1, 0),
        markings=((), (), (), (), (), ()),
        edges=((0, 1), (0, 4), (1, 2), (1, 5), (2, 3), (3, 4), (3, 5), (4, 5)),
    )
