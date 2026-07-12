r"""The canonical semantic representation of a stable curve type.

A stable curve type is the dual graph indexing a stratum of the
Deligne-Mumford compactification :math:`\overline{\mathcal M}_{g,n}`.  The
source of truth is an immutable half-edge record

.. math::

    \Gamma = (V, H, \iota, \partial, w, \lambda)

where

* ``V`` is the finite set of component vertices ``0, ..., |V| - 1``;
* ``H`` is the finite set of flags (half-edges) ``0, ..., |H| - 1``;
* :math:`\iota\colon H \to H` is an involution -- its two-element orbits are
  the internal edges, its fixed points are the legs;
* :math:`\partial\colon H \to V` records incidence;
* :math:`w\colon V \to \mathbf Z_{\ge 0}` is the component-genus function;
* :math:`\lambda\colon \{1, \ldots, n\} \xrightarrow{\sim} H^{\iota}` labels the
  legs.

The half-edge formulation is deliberate: the involution that swaps the two
branches of a self-loop is part of the graph automorphism group relevant to the
stack quotient, and a bare vertex multigraph cannot express it.

This module owns *only* the immutable record and its structural validation.  No
mutable graph object is ever used as a hash key; identity is decided downstream
by the canonical labelling in :mod:`dm_moduli_spike.objects.canonical`.
"""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.graphs.graph import Graph


_RecordKey = tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], tuple[int, ...]]
_GRAPH_INTERN: dict[_RecordKey, StableGraph] = {}


def intern_graph(graph: StableGraph) -> StableGraph:
    r"""Return a shared :class:`StableGraph` instance for identical data."""
    key = (
        graph.vertex_genera,
        graph.flag_vertex,
        graph.flag_involution,
        graph.marking_to_flag,
    )
    cached = _GRAPH_INTERN.get(key)
    if cached is None:
        _GRAPH_INTERN[key] = graph
        return graph
    return cached


# Backward-compatible alias used by older imports and tests.
def intern_record(graph: StableGraph) -> StableGraph:
    return intern_graph(graph)


class StableGraph:
    r"""Immutable half-edge record for a connected stable dual graph.

    The constructor validates the structural axioms (indices in range, ``iota``
    an involution, legs are exactly the marked flags, markings are exactly
    ``1, ..., n``, connectivity, and stability at every vertex).  It does *not*
    know the ambient ``(g, n)``; the total genus is intrinsic and is exposed via
    :meth:`genus`.  Matching that intrinsic genus against an ambient
    :math:`\overline{\mathcal M}_{g,n}` is the job of the parent
    :class:`~dm_moduli_spike.objects.graph_types.StableGraphTypes`.
    """

    __slots__ = (
        "_vertex_genera",
        "_flag_vertex",
        "_flag_involution",
        "_marking_to_flag",
        "_frozen",
    )

    def __setattr__(self, name: str, value: object) -> None:
        if getattr(self, "_frozen", False):
            raise AttributeError(f"{type(self).__name__} is immutable; cannot set {name!r}")
        object.__setattr__(self, name, value)

    def __init__(
        self,
        vertex_genera: Sequence[int],
        flag_vertex: Sequence[int],
        flag_involution: Sequence[int],
        marking_to_flag: Sequence[int],
    ) -> None:
        vertex_genera = tuple(int(g) for g in vertex_genera)
        flag_vertex = tuple(int(v) for v in flag_vertex)
        flag_involution = tuple(int(f) for f in flag_involution)
        marking_to_flag = tuple(int(f) for f in marking_to_flag)

        num_vertices = len(vertex_genera)
        num_flags = len(flag_vertex)

        # (1) every index is in range.
        assert num_vertices >= 1, f"a stable curve type has at least one vertex; vertex_genera={vertex_genera}"
        assert all(g >= 0 for g in vertex_genera), f"vertex genera must be nonnegative; vertex_genera={vertex_genera}"
        assert len(flag_involution) == num_flags, f"flag_vertex and flag_involution must be indexed by the same flag set; |flag_vertex|={num_flags}, |flag_involution|={len(flag_involution)}"
        assert all(0 <= v < num_vertices for v in flag_vertex), f"every flag must attach to a vertex in range; flag_vertex={flag_vertex}, num_vertices={num_vertices}"
        assert all(0 <= f < num_flags for f in flag_involution), f"the involution must land in the flag set; flag_involution={flag_involution}, num_flags={num_flags}"

        # (2) the involution squares to the identity.
        for flag in range(num_flags):
            assert flag_involution[flag_involution[flag]] == flag, f"iota must be an involution; iota(iota({flag}))={flag_involution[flag_involution[flag]]} != {flag}"

        # (3) the fixed flags are exactly the image of the marking map, and
        # (4) the markings are exactly 1, ..., n with no repetition.
        legs = frozenset(flag for flag in range(num_flags) if flag_involution[flag] == flag)
        assert len(set(marking_to_flag)) == len(marking_to_flag), f"marking labels must map to distinct flags; marking_to_flag={marking_to_flag}"
        assert frozenset(marking_to_flag) == legs, f"the marked flags must be exactly the legs (fixed points of iota); marked={sorted(marking_to_flag)}, legs={sorted(legs)}"

        self._vertex_genera = vertex_genera
        self._flag_vertex = flag_vertex
        self._flag_involution = flag_involution
        self._marking_to_flag = marking_to_flag
        object.__setattr__(self, "_frozen", True)

        # (5) the internal graph is connected.
        assert self._is_connected(), f"the underlying graph must be connected; vertex_genera={vertex_genera}, flag_vertex={flag_vertex}, flag_involution={flag_involution}"

        # (6) every vertex is stable: 2 w(v) - 2 + n_v > 0.
        for vertex in range(num_vertices):
            valence = self.valence(vertex)
            assert 2 * vertex_genera[vertex] - 2 + valence > 0, f"vertex {vertex} is unstable: 2*{vertex_genera[vertex]} - 2 + {valence} = {2 * vertex_genera[vertex] - 2 + valence} is not > 0"

    # -- structural accessors ----------------------------------------------------

    @property
    def vertex_genera(self) -> tuple[int, ...]:
        return self._vertex_genera

    @property
    def flag_vertex(self) -> tuple[int, ...]:
        return self._flag_vertex

    @property
    def flag_involution(self) -> tuple[int, ...]:
        return self._flag_involution

    @property
    def marking_to_flag(self) -> tuple[int, ...]:
        return self._marking_to_flag

    def num_vertices(self) -> int:
        return len(self._vertex_genera)

    def num_flags(self) -> int:
        return len(self._flag_vertex)

    def num_markings(self) -> int:
        return len(self._marking_to_flag)

    def legs(self) -> tuple[int, ...]:
        r"""The leg flags (fixed points of the involution), sorted by flag id."""
        return tuple(flag for flag in range(self.num_flags()) if self._flag_involution[flag] == flag)

    def edge_flags(self) -> tuple[int, ...]:
        r"""The flags that belong to an internal edge (non-fixed points)."""
        return tuple(flag for flag in range(self.num_flags()) if self._flag_involution[flag] != flag)

    def internal_edges(self) -> tuple[tuple[int, int], ...]:
        r"""The internal edges as ordered flag pairs ``(f, iota(f))`` with
        ``f < iota(f)``.  A self-loop is a pair of distinct flags on the same
        vertex; the two entries are the two branches of the loop."""
        edges = []
        for flag in range(self.num_flags()):
            partner = self._flag_involution[flag]
            if flag < partner:
                edges.append((flag, partner))
        return tuple(edges)

    def num_edges(self) -> int:
        return len(self.internal_edges())

    def valence(self, vertex: int) -> int:
        r"""The valence :math:`n_v = \#\partial^{-1}(v)`: every incident flag,
        counting both branches of a self-loop and every leg."""
        return sum(1 for v in self._flag_vertex if v == vertex)

    def flags_at(self, vertex: int) -> tuple[int, ...]:
        return tuple(flag for flag in range(self.num_flags()) if self._flag_vertex[flag] == vertex)

    def markings_at(self, vertex: int) -> tuple[int, ...]:
        r"""The marking labels (1-indexed) whose leg sits on ``vertex``."""
        return tuple(marking + 1 for marking, flag in enumerate(self._marking_to_flag) if self._flag_vertex[flag] == vertex)

    def is_loop(self, edge: tuple[int, int]) -> bool:
        flag, partner = edge
        return self._flag_vertex[flag] == self._flag_vertex[partner]

    # -- derived invariants ------------------------------------------------------

    def first_betti_number(self) -> int:
        r""":math:`b_1(\Gamma) = |E| - |V| + 1` for the connected graph."""
        return self.num_edges() - self.num_vertices() + 1

    def genus(self) -> int:
        r"""The total (arithmetic) genus
        :math:`g(\Gamma) = b_1(\Gamma) + \sum_v w(v)`."""
        return self.first_betti_number() + sum(self._vertex_genera)

    def is_stable(self) -> bool:
        r"""Total by construction -- the constructor rejects unstable data -- so
        this always returns ``True`` on a live record; it exists as an explicit
        semantic verb for callers holding a record."""
        return all(2 * self._vertex_genera[v] - 2 + self.valence(v) > 0 for v in range(self.num_vertices()))

    def _is_connected(self) -> bool:
        num_vertices = self.num_vertices()
        if num_vertices <= 1:
            return True
        adjacency: list[set[int]] = [set() for _ in range(num_vertices)]
        for flag, partner in self.internal_edges():
            u = self._flag_vertex[flag]
            v = self._flag_vertex[partner]
            adjacency[u].add(v)
            adjacency[v].add(u)
        seen = {0}
        stack = [0]
        while stack:
            current = stack.pop()
            for neighbour in adjacency[current]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)
        return len(seen) == num_vertices

    # -- views -------------------------------------------------------------------

    def edge_of_flag(self) -> dict[int, int]:
        r"""Map each edge-flag to the index of the internal edge it belongs to."""
        mapping: dict[int, int] = {}
        for index, (flag, partner) in enumerate(self.internal_edges()):
            mapping[flag] = index
            mapping[partner] = index
        return mapping

    def sage_multigraph(self) -> Graph:
        r"""A derived Sage looped multigraph view: one bare integer vertex per
        component, one edge per internal edge (including self-loops).

        Genus and marking labels are *not* attached to this view; use
        :meth:`vertex_genera`, :meth:`markings_at`, and
        :mod:`dm_moduli_spike.objects.canonical` for decorated identity data.
        """
        from sage.graphs.graph import Graph

        graph = Graph(loops=True, multiedges=True)
        for vertex in range(self.num_vertices()):
            graph.add_vertex(vertex)
        for flag, partner in self.internal_edges():
            graph.add_edge(self._flag_vertex[flag], self._flag_vertex[partner])
        return graph

    def __iter__(self) -> Iterator[object]:
        yield from (self._vertex_genera, self._flag_vertex, self._flag_involution, self._marking_to_flag)

    def __repr__(self) -> str:
        return (
            "StableGraph("
            f"vertex_genera={self._vertex_genera}, "
            f"flag_vertex={self._flag_vertex}, "
            f"flag_involution={self._flag_involution}, "
            f"marking_to_flag={self._marking_to_flag})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StableGraph):
            return NotImplemented
        return (
            self._vertex_genera == other._vertex_genera
            and self._flag_vertex == other._flag_vertex
            and self._flag_involution == other._flag_involution
            and self._marking_to_flag == other._marking_to_flag
        )

    def __hash__(self) -> int:
        return hash(
            (
                self._vertex_genera,
                self._flag_vertex,
                self._flag_involution,
                self._marking_to_flag,
            )
        )

    # -- labeled-graph operations ------------------------------------------------

    def vertices(self) -> tuple[int, ...]:
        return tuple(range(self.num_vertices()))

    def vertex_genus(self, vertex: int) -> int:
        return self._vertex_genera[vertex]

    def graph_type(self):
        from .graph_types import StableGraphTypes

        return StableGraphTypes(self.genus(), self.num_markings())(self)

    def contract(self, edge: tuple[int, int]):
        from .contractions import contract_edge

        return contract_edge(self, edge)

    def canonical_form(self):
        from .canonical import canonical_record
        from .contractions import flag_map
        from .graph_types import StableGraphTypes

        canonical = intern_graph(canonical_record(self))
        parent = StableGraphTypes(self.genus(), self.num_markings())
        graph_type = parent(canonical)
        certificate = {flag: flag for flag in range(self.num_flags())} if self == canonical else flag_map(self, canonical)
        return graph_type, canonical, certificate

    def to_labeled_json(self) -> dict[str, object]:
        from .canonical import to_labeled_json

        return to_labeled_json(self, self.genus(), self.num_markings())


StableGraphRecord = StableGraph
