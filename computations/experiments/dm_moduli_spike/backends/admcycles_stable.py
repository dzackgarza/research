r"""Adapter over the established ``admcycles`` :class:`StableGraph` interface.

This is the correctness-oriented backend.  ``admcycles`` already enumerates the
boundary strata of :math:`\overline{\mathcal M}_{g,n}` by codimension
(``admcycles.list_strata(g, n, r)``), tests isomorphism, contracts edges and
reports half-edge automorphism numbers.  The adapter converts every returned
``StableGraph`` into the spike's owned
:class:`~dm_moduli_spike.objects.curve_types.StableGraphType`, so no
``admcycles`` class ever surfaces in the public API.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.records import StableGraph

if TYPE_CHECKING:
    from ..objects.curve_types import StableGraphType, StableGraphTypes


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
                result.append(curve_types.from_record(record))
        return tuple(result)

    def admcycles_automorphism_number(self, curve_types: StableGraphTypes, curve_type: StableGraphType) -> int:
        r"""The ``admcycles`` automorphism number of the ``StableGraph`` matching
        ``curve_type``; used to cross-check the incidence-graph implementation."""
        admcycles = _require_admcycles()
        g = curve_types.genus()
        n = curve_types.number_of_markings()
        for stable_graph in admcycles.list_strata(g, n, curve_type.num_edges()):  # type: ignore[attr-defined]
            record = _record_from_stable_graph(stable_graph, g, n)
            if curve_types.from_record(record) == curve_type:
                return int(stable_graph.automorphism_number())
        raise ValueError(f"no admcycles StableGraph matched {curve_type!r}")
