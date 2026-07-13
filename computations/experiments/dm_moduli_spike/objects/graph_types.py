r"""Isomorphism classes of stable dual graphs and their Sage parent.

A :class:`StableGraphType` is an immutable ``Element`` representing an
isomorphism class -- an *index* for a stratum of
:math:`\overline{\mathcal M}_{g,n}`.  Representative-level operations
(contraction, flags, edges) live on :class:`~dm_moduli_spike.objects.records.StableGraph`.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, ClassVar

from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from .automorphism_action import AutomorphismAction
from .canonical import CanonicalKey, automorphism_group, automorphism_number, canonical_key, canonical_record, to_json
from .records import StableGraph, intern_graph

if TYPE_CHECKING:
    pass


class StableGraphType(Element):
    r"""An isomorphism class of stable dual graphs of type ``(g, n)``."""

    __slots__ = ("_graph", "_canonical_key")

    def __init__(self, parent: StableGraphTypes, graph: StableGraph) -> None:
        super().__init__(parent)
        canonical = intern_graph(canonical_record(graph))
        self._graph = canonical
        self._canonical_key: CanonicalKey = canonical_key(canonical)

    def canonical_representative(self) -> StableGraph:
        return self._graph

    def canonical_key(self) -> CanonicalKey:
        return self._canonical_key

    def record(self) -> StableGraph:
        r"""Deprecated alias for :meth:`canonical_representative`."""
        return self._graph

    def automorphism_group(self) -> object:
        return automorphism_group(self._graph)

    def automorphism_action(self) -> AutomorphismAction:
        return AutomorphismAction.from_graph(self._graph)

    def total_genus(self) -> int:
        return self._graph.genus()

    def num_vertices(self) -> int:
        return self._graph.num_vertices()

    def num_flags(self) -> int:
        return self._graph.num_flags()

    def num_edges(self) -> int:
        return self._graph.num_edges()

    def num_markings(self) -> int:
        return self._graph.num_markings()

    def vertex_genera(self) -> tuple[int, ...]:
        return self._graph.vertex_genera

    def valence(self, vertex: int) -> int:
        return self._graph.valence(vertex)

    def is_stable(self) -> bool:
        return self._graph.is_stable()

    def is_smooth(self) -> bool:
        return self._graph.num_edges() == 0

    def first_betti_number(self) -> int:
        return self._graph.first_betti_number()

    def codimension(self) -> int:
        return self._graph.num_edges()

    def stratum_dimension(self) -> int:
        return sum(3 * self._graph.vertex_genera[v] - 3 + self._graph.valence(v) for v in range(self._graph.num_vertices()))

    def automorphism_number(self) -> int:
        return automorphism_number(self._graph)

    def one_edge_degenerations(self) -> tuple[StableGraphType, ...]:
        from .enumeration import one_edge_degenerations

        return one_edge_degenerations(self)

    def contracts_to(self, other: StableGraphType) -> bool:
        if other.num_edges() > self.num_edges():
            return False
        target = other.canonical_key()
        if self.canonical_key() == target:
            return True
        visited: set[object] = {self.canonical_key()}
        queue: deque[StableGraphType] = deque([self])
        while queue:
            current = queue.popleft()
            current_graph = current.canonical_representative()
            from .edge_orbits import automorphism_edge_orbit_indices

            for group in automorphism_edge_orbit_indices(current_graph):
                representative = current_graph.internal_edges()[group[0]]
                image_type, _ = current_graph.contract(representative)
                image = self.parent()(image_type)
                key = image.canonical_key()
                if key == target:
                    return True
                if key not in visited:
                    visited.add(key)
                    queue.append(image)
        return False

    def admits_contraction_to(self, other: StableGraphType) -> bool:
        return self.contracts_to(other)

    def edge_orbits(self) -> tuple[tuple[tuple[int, int], ...], ...]:
        from .edge_orbits import automorphism_edge_orbits

        return automorphism_edge_orbits(self._graph)

    def covers(self) -> tuple[tuple[StableGraphType, StableGraphType], ...]:
        r"""Distinct contraction targets ``[\Gamma/e]``, one per ``Aut(\Gamma)`` edge orbit."""
        from .edge_orbits import automorphism_edge_orbit_indices

        seen: dict[object, tuple[StableGraphType, StableGraphType]] = {}
        graph = self._graph
        for group in automorphism_edge_orbit_indices(graph):
            representative = graph.internal_edges()[group[0]]
            target_type, _ = graph.contract(representative)
            target = self.parent()(target_type)
            seen.setdefault(target.canonical_key(), (target, self))
        return tuple(seen.values())

    def split_system(self, anchor_marking: int = 1) -> frozenset[frozenset[int]]:
        from .splits import split_system

        return split_system(self, anchor_marking=anchor_marking)

    def to_json(self) -> dict[str, object]:
        return to_json(self._graph, self.parent().genus(), self.parent().number_of_markings())

    def _richcmp_(self, other: object, op: int) -> bool:
        from sage.structure.richcmp import richcmp

        assert isinstance(other, StableGraphType)
        return bool(richcmp(self._canonical_key, other._canonical_key, op))

    def __hash__(self) -> int:
        return hash((self.parent().genus(), self.parent().number_of_markings(), self._canonical_key))

    def __getstate__(self) -> tuple[StableGraphTypes, StableGraph, CanonicalKey]:
        return (self.parent(), self._graph, self._canonical_key)

    def __setstate__(self, state: tuple[StableGraphTypes, StableGraph, CanonicalKey]) -> None:
        parent, graph, key = state
        Element.__init__(self, parent)
        self._graph = graph
        self._canonical_key = key

    def _repr_(self) -> str:
        genera = self._graph.vertex_genera
        return f"Stable graph type of genus {self.total_genus()} with {self.num_edges()} node(s), vertex genera {genera}"


class StableGraphTypes(UniqueRepresentation, Parent):
    r"""The finite set of stable graph types of a fixed stable ``(g, n)``."""

    Element = StableGraphType

    if TYPE_CHECKING:
        element_class: ClassVar[type[StableGraphType]]

    def __init__(self, g: int, n: int) -> None:
        g = int(g)
        n = int(n)
        assert g >= 0 and n >= 0, f"(g, n) must be nonnegative integers; (g, n)=({g}, {n})"
        assert 2 * g - 2 + n > 0, f"(g, n)=({g}, {n}) is not in the stable range 2g - 2 + n > 0"
        self._g = g
        self._n = n
        self._element_cache: dict[CanonicalKey, StableGraphType] = {}
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def dimension(self) -> int:
        return 3 * self._g - 3 + self._n

    def _repr_(self) -> str:
        return f"Stable graph types of genus {self._g} with {self._n} marking(s)"

    def __call__(self, x: StableGraph | StableGraphType) -> StableGraphType:
        if isinstance(x, StableGraphType):
            assert x.parent() is self, f"cannot re-parent a stable graph type from {x.parent()} into {self}"
            return x
        assert isinstance(x, StableGraph), f"expected a StableGraph or StableGraphType; found {type(x)}"
        assert x.genus() == self._g, f"graph genus {x.genus()} does not match ambient genus {self._g}"
        assert x.num_markings() == self._n, f"graph has {x.num_markings()} markings, ambient has {self._n}"
        canonical = intern_graph(canonical_record(x))
        key = canonical_key(canonical)
        cached = self._element_cache.get(key)
        if cached is not None:
            return cached
        element = self.element_class(self, canonical)
        self._element_cache[key] = element
        return element

    def _element_constructor_(self, data: StableGraph | StableGraphType) -> StableGraphType:
        return self(data)

    def from_graph(self, graph: StableGraph) -> StableGraphType:
        return self(graph)

    def from_record(self, graph: StableGraph) -> StableGraphType:
        r"""Backward-compatible alias for :meth:`from_graph`."""
        return self(graph)

    def smooth(self) -> StableGraphType:
        flags = tuple(range(self._n))
        graph = StableGraph(
            vertex_genera=(self._g,),
            flag_vertex=(0,) * self._n,
            flag_involution=flags,
            marking_to_flag=flags,
        )
        return self(graph)

    def from_vertices(
        self,
        genera: Sequence[int],
        markings: Sequence[Sequence[int]],
        edges: Sequence[tuple[int, int]],
    ) -> StableGraphType:
        genera = tuple(int(g) for g in genera)
        markings = tuple(tuple(int(m) for m in vertex_markings) for vertex_markings in markings)
        edges = tuple((int(u), int(v)) for u, v in edges)
        assert len(genera) == len(markings), f"genera and markings must be indexed by the same vertex set; |genera|={len(genera)}, |markings|={len(markings)}"

        flag_vertex: list[int] = []
        flag_involution: list[int] = []
        marking_to_flag_by_label: dict[int, int] = {}

        for vertex, vertex_markings in enumerate(markings):
            for label in vertex_markings:
                flag = len(flag_vertex)
                flag_vertex.append(vertex)
                flag_involution.append(flag)
                assert label not in marking_to_flag_by_label, f"marking label {label} used twice"
                marking_to_flag_by_label[label] = flag

        for u, v in edges:
            flag_u = len(flag_vertex)
            flag_vertex.append(u)
            flag_involution.append(flag_u + 1)
            flag_vertex.append(v)
            flag_involution.append(flag_u)

        labels = sorted(marking_to_flag_by_label)
        assert labels == list(range(1, self._n + 1)), f"markings must be exactly 1, ..., {self._n}; found {labels}"
        marking_to_flag = tuple(marking_to_flag_by_label[label] for label in labels)

        graph = StableGraph(
            vertex_genera=genera,
            flag_vertex=tuple(flag_vertex),
            flag_involution=tuple(flag_involution),
            marking_to_flag=marking_to_flag,
        )
        return self(graph)

    def from_json(self, data: dict[str, object]) -> StableGraphType:
        schema = data.get("schema", 1)
        assert isinstance(schema, int), f"unsupported JSON schema version {schema!r}; only schema 1 is supported"
        assert schema == 1, f"unsupported JSON schema version {schema!r}; only schema 1 is supported"
        ambient = data["ambient"]
        assert isinstance(ambient, dict)
        assert int(ambient["g"]) == self._g and int(ambient["n"]) == self._n, f"JSON ambient {ambient} does not match {self}"
        raw_vertices = data["vertices"]
        raw_edges = data["edges"]
        assert isinstance(raw_vertices, list) and isinstance(raw_edges, list)
        vertex_ids: list[int] = []
        for vertex in raw_vertices:
            assert isinstance(vertex, dict), f"expected vertex object; found {vertex!r}"
            assert "id" in vertex and "genus" in vertex and "markings" in vertex, f"vertex {vertex!r} lacks required fields"
            vertex_ids.append(int(vertex["id"]))
        assert len(vertex_ids) == len(set(vertex_ids)), f"duplicate vertex ids in JSON: {vertex_ids}"
        by_id = {int(v["id"]): v for v in raw_vertices}
        order = sorted(by_id)
        position = {vertex_id: index for index, vertex_id in enumerate(order)}
        genera = tuple(int(by_id[vertex_id]["genus"]) for vertex_id in order)
        markings = tuple(tuple(int(m) for m in by_id[vertex_id]["markings"]) for vertex_id in order)
        for edge in raw_edges:
            assert isinstance(edge, dict) and "ends" in edge, f"edge {edge!r} lacks ends"
            ends = edge["ends"]
            assert isinstance(ends, list) and len(ends) == 2, f"edge ends must be a pair; found {ends!r}"
            for endpoint in ends:
                assert int(endpoint) in by_id, f"edge endpoint {endpoint!r} is not a declared vertex id"
        edges = tuple((position[int(e["ends"][0])], position[int(e["ends"][1])]) for e in raw_edges)
        return self.from_vertices(genera=genera, markings=markings, edges=edges)

    def __iter__(self) -> Iterator[StableGraphType]:
        from .enumeration import all_stable_curve_types

        yield from all_stable_curve_types(self)

    def cardinality(self) -> int:
        return int(sum(1 for _ in self))
