"""Named structural fixtures and independent literature oracles."""

from __future__ import annotations

from itertools import combinations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dm_moduli_spike.objects.graph_types import StableGraphType, StableGraphTypes
    from dm_moduli_spike.objects.records import StableGraph
    from dm_moduli_spike.objects.stratification import DMStratification

BoundaryLabel = tuple[str, ...] | tuple[str, int, frozenset[int]]

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
    seen: set[tuple[int, frozenset[int]]] = set()
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
                key = (a, a_set) if (a, a_set) <= (b, b_set) else (b, b_set)
                if key in seen:
                    continue
                seen.add(key)
                labels.add(("sep", key[0], key[1]))
    return labels


def boundary_label(curve_type: StableGraphType, g: int, n: int) -> BoundaryLabel:
    assert curve_type.codimension() == 1
    record = curve_type.canonical_representative()
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
    b_set = markings[1]
    if (genera[1], b_set) < (a, a_set):
        a, a_set = genera[1], b_set
    return ("sep", a, frozenset(a_set))


def expected_clutching_signature_irr(g: int, n: int) -> tuple[tuple[int, int], ...]:
    return ((g - 1, n + 2),)


def expected_clutching_signature_sep(g: int, n: int, a: int, marking_set: frozenset[int]) -> tuple[tuple[int, int], ...]:
    b = g - a
    b_set = frozenset(label for label in range(1, n + 1) if label not in marking_set)
    return (
        (a, len(marking_set) + 1),
        (b, len(b_set) + 1),
    )


def clutching_signature(curve_type: StableGraphType) -> tuple[tuple[int, int], ...]:
    r"""Sorted ``(g(v), valence(v))`` factors of the clutching source product."""
    record = curve_type.canonical_representative()
    return tuple(sorted((record.vertex_genera[v], record.valence(v)) for v in range(record.num_vertices())))


def classify_chan_m20(record: StableGraph) -> str:
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
    if num_vertices == 2 and genera == (1, 0) and loops == 1 and bridges == 1:
        return "IV"
    if num_vertices == 2 and genera == (0, 0) and bridges == 3 and loops == 0:
        return "I"
    if num_vertices == 2 and genera == (0, 0) and loops == 2 and bridges == 1:
        return "II"
    raise AssertionError(f"graph does not match any Chan Figure 3 type: V={num_vertices} G={genera} E={num_edges} L={loops}")


def induced_edge_permutation_group(graph: StableGraph) -> object:
    r"""Sage ``PermutationGroup`` of `\operatorname{Aut}(G)` acting on edge indices."""
    return graph.automorphism_group(on="edges")


def flag_generator_images(graph: StableGraph) -> tuple[tuple[int, ...], ...]:
    r"""0-indexed flag images of Aut generators (test helper)."""
    from dm_moduli_spike.objects._automorphism_action import _GraphAutomorphismData

    return _GraphAutomorphismData.from_graph(graph).on_flags()


def marking_generator_images(graph: StableGraph) -> tuple[tuple[int, ...], ...]:
    from dm_moduli_spike.objects._automorphism_action import _GraphAutomorphismData

    return _GraphAutomorphismData.from_graph(graph).on_markings()


def vertex_generator_images(graph: StableGraph) -> tuple[tuple[int, ...], ...]:
    from dm_moduli_spike.objects._automorphism_action import _GraphAutomorphismData

    return _GraphAutomorphismData.from_graph(graph).on_vertices()


def edge_generator_images(graph: StableGraph) -> tuple[tuple[int, ...], ...]:
    from dm_moduli_spike.objects._automorphism_action import _GraphAutomorphismData

    return _GraphAutomorphismData.from_graph(graph).on_edges()


def chan_m13_curve_type(types: StableGraphTypes) -> StableGraphType:
    return types.from_vertices(
        genera=(0, 0),
        markings=((1, 2), (3,)),
        edges=((0, 1), (0, 1)),
    )


def m11_types(stratification: DMStratification) -> tuple[StableGraphType, StableGraphType]:
    poset = stratification.specialization_poset()
    smooth = next(x for x in poset if x.num_edges() == 0)
    nodal = next(x for x in poset if x.num_edges() == 1)
    return smooth, nodal


def m12_types(stratification: DMStratification) -> dict[str, StableGraphType]:
    return {
        "A": stratification.find_unique_type(
            vertex_genera=(1,),
            marking_blocks=((1, 2),),
        ),
        "B": stratification.find_unique_type(
            vertex_genera=(0,),
            loops=(1,),
            marking_blocks=((1, 2),),
        ),
        "C": stratification.find_unique_type(
            vertex_genera=(0, 1),
            edge_multiset=((0, 1, 1),),
            marking_blocks=((1, 2), ()),
        ),
        "D": stratification.find_unique_type(
            vertex_genera=(0, 0),
            loops=(1, 0),
            edge_multiset=((0, 1, 1),),
            marking_blocks=((), (1, 2)),
        ),
        "E": stratification.find_unique_type(
            vertex_genera=(0, 0),
            edge_multiset=((0, 1, 2),),
            marking_blocks=((1,), (2,)),
        ),
    }


def m20_types(stratification: DMStratification) -> dict[str, StableGraphType]:
    by_name: dict[str, StableGraphType] = {}
    for gamma in stratification.strata():
        name = classify_chan_m20(gamma.canonical_representative())
        assert name not in by_name, f"duplicate Chan type {name}"
        by_name[name] = gamma
    assert set(by_name) == set(CHAN_M20_COVERS) | {"I", "II", "III", "IV", "V", "VI", "VII"}
    return by_name


def genus_six_counterexample() -> StableGraphType:
    from dm_moduli_spike.objects.graph_types import StableGraphTypes

    types = StableGraphTypes(6, 0)
    return types.from_vertices(
        genera=(1, 0, 1, 0, 1, 0),
        markings=((), (), (), (), (), ()),
        edges=((0, 1), (0, 4), (1, 2), (1, 5), (2, 3), (3, 4), (3, 5), (4, 5)),
    )
