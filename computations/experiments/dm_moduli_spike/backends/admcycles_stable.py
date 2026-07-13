r"""Adapter over the established ``admcycles`` :class:`StableGraph` interface.

This is the correctness-oriented backend.  ``admcycles`` already enumerates the
boundary strata of :math:`\overline{\mathcal M}_{g,n}` by codimension
(``admcycles.list_strata(g, n, r)``), tests isomorphism, contracts edges and
reports half-edge automorphism numbers.  The adapter converts every returned
``StableGraph`` into the spike's owned
:class:`~dm_moduli_spike.objects.graph_types.StableGraphType`, so no
``admcycles`` class ever surfaces in the public API.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.records import StableGraph

if TYPE_CHECKING:
    from ..objects.graph_types import StableGraphType, StableGraphTypes


def _require_admcycles() -> object:
    try:
        import admcycles  # type: ignore[import-not-found]
    except ImportError as error:  # pragma: no cover - environment dependent
        raise ImportError("the admcycles-stable backend requires the optional 'admcycles' package; install it into Sage's Python with `sage -pip install admcycles`") from error
    return admcycles


def _record_from_stable_graph(stable_graph: object, g: int, n: int) -> StableGraph:
    r"""Convert an ``admcycles`` ``StableGraph`` to a half-edge record.

    ``admcycles`` labels half-edges by integers; the external markings are the
    labels ``1, ..., n`` and every internal edge is a pair of the remaining
    labels.  Legs (per vertex) give incidence; edges give the involution.
    """
    genera = [int(x) for x in stable_graph.genera()]  # type: ignore[attr-defined]
    legs_per_vertex = stable_graph.legs(copy=True)  # type: ignore[attr-defined]
    edges = stable_graph.edges(copy=True)  # type: ignore[attr-defined]
    markings = sorted(int(m) for m in stable_graph.list_markings())  # type: ignore[attr-defined]
    assert markings == list(range(1, n + 1)), f"admcycles markings {markings} are not exactly 1, ..., {n}"

    label_vertex: dict[int, int] = {}
    for vertex, labels in enumerate(legs_per_vertex):
        for label in labels:
            label_vertex[int(label)] = vertex

    ordered_labels = sorted(label_vertex)
    flag_of_label = {label: index for index, label in enumerate(ordered_labels)}
    num_flags = len(ordered_labels)

    flag_vertex = [label_vertex[label] for label in ordered_labels]
    involution = list(range(num_flags))
    for a, b in edges:
        flag_a, flag_b = flag_of_label[int(a)], flag_of_label[int(b)]
        involution[flag_a] = flag_b
        involution[flag_b] = flag_a
    marking_to_flag = [flag_of_label[m] for m in range(1, n + 1)]

    record = StableGraph(
        vertex_genera=tuple(genera),
        flag_vertex=tuple(flag_vertex),
        flag_involution=tuple(involution),
        marking_to_flag=tuple(marking_to_flag),
    )
    assert record.genus() == g, f"converted record genus {record.genus()} != ambient genus {g}"
    return record


def _record_to_stable_graph(record: StableGraph, g: int, n: int) -> object:
    r"""Convert an owned half-edge :class:`StableGraph` to ``admcycles.StableGraph``.

    Labels are assigned so markings keep labels ``1, ..., n`` and remaining
    half-edges receive consecutive unused integers.  Round-trips through
    :func:`_record_from_stable_graph` preserve the owned curve type.
    """
    admcycles = _require_admcycles()
    StableGraphAdm = admcycles.StableGraph  # type: ignore[attr-defined]

    assert record.genus() == g, f"record genus {record.genus()} != ambient {g}"
    assert record.num_markings() == n, f"record markings {record.num_markings()} != ambient {n}"

    next_label = n + 1
    flag_label: dict[int, int] = {}
    for marking in range(1, n + 1):
        flag_label[record.marking_to_flag[marking - 1]] = marking

    for flag in range(record.num_flags()):
        if flag not in flag_label:
            flag_label[flag] = next_label
            next_label += 1

    legs = [
        [flag_label[flag] for flag in record.flags_at(vertex)]
        for vertex in range(record.num_vertices())
    ]
    edges = [(flag_label[a], flag_label[b]) for a, b in record.internal_edges()]
    stable_graph = StableGraphAdm(list(record.vertex_genera), legs, edges)
    roundtrip = _record_from_stable_graph(stable_graph, g, n)
    assert roundtrip.genus() == g
    assert roundtrip.num_markings() == n
    assert roundtrip.num_edges() == record.num_edges()
    return stable_graph


class AdmcyclesStableGraphBackend:
    r"""Enumeration and cross-checks via ``admcycles.list_strata``."""

    def is_available(self) -> bool:
        try:
            _require_admcycles()
        except ImportError:  # optional admcycles not installed
            return False
        return True

    def stable_curve_types(self, curve_types: StableGraphTypes, max_codim: int | None = None) -> tuple[StableGraphType, ...]:
        admcycles = _require_admcycles()
        g = curve_types.genus()
        n = curve_types.number_of_markings()
        dimension = curve_types.dimension()
        cap = dimension if max_codim is None else min(int(max_codim), dimension)
        result: list[StableGraphType] = []
        for codim in range(cap + 1):
            for stable_graph in admcycles.list_strata(g, n, codim):  # type: ignore[attr-defined]
                record = _record_from_stable_graph(stable_graph, g, n)
                # Cross-check the reported codimension against the actual edge
                # count rather than trusting the bucket label.
                assert record.num_edges() == codim, f"admcycles returned a codim-{codim} graph with {record.num_edges()} edges"
                result.append(curve_types.from_graph(record))
        return tuple(result)

    def admcycles_automorphism_number(self, curve_types: StableGraphTypes, curve_type: StableGraphType) -> int:
        r"""The ``admcycles`` automorphism number of the ``StableGraph`` matching
        ``curve_type``; used to cross-check the incidence-graph implementation."""
        record = curve_type.canonical_representative()
        stable_graph = _record_to_stable_graph(record, curve_types.genus(), curve_types.number_of_markings())
        return int(stable_graph.automorphism_number())  # type: ignore[attr-defined]

    def to_admcycles(self, curve_types: StableGraphTypes, curve_type: StableGraphType) -> object:
        r"""Owned Γ object → ``admcycles.StableGraph`` (adapter surface)."""
        return _record_to_stable_graph(
            curve_type.canonical_representative(),
            curve_types.genus(),
            curve_types.number_of_markings(),
        )
