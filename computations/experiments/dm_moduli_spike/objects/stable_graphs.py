r"""Parent ``StableGraphs(g, I)`` of canonical stable graphs with typed incidence sets."""

from __future__ import annotations

from collections import deque
from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import TYPE_CHECKING, ClassVar, cast

from sage.categories.action import Action
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from .._sage_types import SagePermutation
from .._typing_utils import as_int
from .canonical import (
    CanonicalKey,
    automorphism_group,
    automorphism_number,
    canonical_key,
    canonical_record,
    to_json,
)
from .records import _GraphRecord, intern_graph

if TYPE_CHECKING:
    StableGraphParent = Parent["StableGraph"]
else:
    StableGraphParent = Parent


def _markings(I: object) -> tuple[int, ...]:
    from sage.rings.integer import Integer

    if isinstance(I, (int, Integer)):
        return tuple(range(1, int(I) + 1))
    assert isinstance(I, Iterable), f"expected marking count or iterable; found {type(I)!r}"
    return tuple(int(x) for x in I)


class _PermutationAction(Action):
    r"""Left action of a permutation group on a finite enumerated set of labels."""

    def _act_(self, g: object, x: object) -> object:
        # Sage permutations are 1-based on {1,...,n}; labels may be 0-based indices.
        labels = list(self.codomain())
        if x not in labels:
            raise ValueError(f"{x!r} not in action codomain")
        assert isinstance(g, SagePermutation) or callable(g), f"group element must be callable; found {type(g)!r}; owned boundary=_PermutationAction._act_"
        # Prefer native permutation action when labels are the standard domain.
        try:
            return g(x)
        except TypeError, ValueError, IndexError:
            # Labels may be 0-based indices while Sage acts on {1,...,n}.
            idx = labels.index(x)
            image_pos = as_int(g(idx + 1)) - 1
            return labels[image_pos]


_PERMUTATION_ACTIONS: dict[tuple[object, ...], Action] = {}


def _permutation_action(group: object, domain: object) -> Action:
    r"""Build a Sage :class:`~sage.categories.action.Action` of ``group`` on ``domain``.

    Identical ``(group, labels)`` pairs intern to one action so quotient-stack
    presentations rebuilt from the same combinatorial data stay unique.
    """
    from sage.sets.finite_enumerated_set import FiniteEnumeratedSet

    if hasattr(domain, "list"):
        labels = tuple(domain.list())
    else:
        assert isinstance(domain, Iterable), f"action domain must be iterable; found {type(domain)!r}"
        labels = tuple(domain)
    key = (id(group), labels)
    cached = _PERMUTATION_ACTIONS.get(key)
    if cached is not None:
        return cached
    S = FiniteEnumeratedSet(labels)
    action = _PermutationAction(group, S, is_left=True, op=None)
    _PERMUTATION_ACTIONS[key] = action
    return action


class StableGraphs(UniqueRepresentation, StableGraphParent):
    r"""Finite enumerated set of isomorphism classes of stable graphs of type `(g,I)`."""

    if TYPE_CHECKING:
        Element: ClassVar[type[StableGraph]]
        element_class: ClassVar[type[StableGraph]]

    @staticmethod
    def __classcall__(cls: type, *args: object, **kwds: object) -> StableGraphs:
        # Normalize so StableGraphs(g, n) and StableGraphs(g, (1..n)) share identity.
        assert not kwds, f"StableGraphs does not take keyword arguments; found {sorted(kwds)!r}"
        assert len(args) == 2, f"StableGraphs(g, I) expected 2 args; found {len(args)}"
        g, I = args
        return cast(StableGraphs, UniqueRepresentation.__classcall__(cls, int(cast(int, g)), _markings(I)))

    def __init__(self, g: int, I: object) -> None:
        self._g = int(g)
        # ``I`` is already a marking tuple when constructed via ``__classcall__``.
        self._I = tuple(as_int(x) for x in cast(tuple[object, ...], I))
        self._n = len(self._I)
        assert self._g >= 0 and self._n >= 0, f"(g, n) must be nonnegative integers; (g, n)=({self._g}, {self._n})"
        assert 2 * self._g - 2 + self._n > 0, f"(g, n)=({self._g}, {self._n}) is not in the stable range 2g - 2 + n > 0"
        self._element_cache: dict[CanonicalKey, StableGraph] = {}
        self._enumeration: tuple[StableGraph, ...] | None = None
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def genus(self) -> int:
        return self._g

    def marking_set(self) -> tuple[int, ...]:
        return self._I

    def number_of_markings(self) -> int:
        return self._n

    def dimension(self) -> int:
        return 3 * self._g - 3 + self._n

    def _element_constructor_(self, data: object) -> StableGraph:
        if isinstance(data, StableGraph):
            assert data.parent() is self, f"cannot re-parent a stable graph from {data.parent()} into {self}"
            return data
        if isinstance(data, _GraphRecord):
            assert data.genus() == self._g, f"graph genus {data.genus()} does not match ambient genus {self._g}"
            assert data.num_markings() == self._n, f"graph has {data.num_markings()} markings, ambient has {self._n}"
            canonical = intern_graph(canonical_record(data))
            key = canonical_key(canonical)
            cached = self._element_cache.get(key)
            if cached is not None:
                return cached
            element = self.element_class(self, canonical)
            self._element_cache[key] = element
            return element
        raise TypeError(f"cannot construct StableGraph from {type(data)}")

    def from_graph(self, graph: _GraphRecord) -> StableGraph:
        typed = self(graph)
        assert isinstance(typed, StableGraph), f"StableGraphs() must return StableGraph; found {type(typed)!r}"
        return typed

    def smooth(self) -> StableGraph:
        flags = tuple(range(self._n))
        graph = _GraphRecord(
            vertex_genera=(self._g,),
            flag_vertex=(0,) * self._n,
            flag_involution=flags,
            marking_to_flag=flags,
        )
        return self.from_graph(graph)

    def from_vertices(
        self,
        genera: Sequence[int],
        markings: Sequence[Sequence[int]],
        edges: Sequence[tuple[int, int]],
    ) -> StableGraph:
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

        graph = _GraphRecord(
            vertex_genera=genera,
            flag_vertex=tuple(flag_vertex),
            flag_involution=tuple(flag_involution),
            marking_to_flag=marking_to_flag,
        )
        return self.from_graph(graph)

    def from_json(self, data: dict[str, object]) -> StableGraph:
        schema = data["schema"]
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

    def _enumerated(self) -> tuple[StableGraph, ...]:
        if self._enumeration is None:
            from .enumeration import all_stable_curve_types

            self._enumeration = tuple(all_stable_curve_types(self))
        return self._enumeration

    def __iter__(self) -> Iterator[StableGraph]:
        yield from self._enumerated()

    def cardinality(self) -> int:
        return len(self._enumerated())

    def an_element(self) -> StableGraph:
        return self.smooth()

    def __contains__(self, obj: object) -> bool:
        if isinstance(obj, StableGraph):
            return obj.parent() is self or (obj.genus() == self._g and obj.num_markings() == self._n)
        if isinstance(obj, _GraphRecord):
            return obj.genus() == self._g and obj.num_markings() == self._n
        return False

    def half_edges_at(self, graph: StableGraph | _GraphRecord, vertex: int) -> tuple[int, ...]:
        rec = graph._record if isinstance(graph, StableGraph) else graph
        return rec.flags_at(vertex)

    def _repr_(self) -> str:
        return f"StableGraphs({self._g}, {self._I})"


class StableGraph(Element):
    r"""Canonical stable graph element of :class:`StableGraphs`."""

    __slots__ = ("_record", "_canonical_key")

    def __init__(self, parent: StableGraphs, record: _GraphRecord) -> None:
        canonical = intern_graph(canonical_record(record))
        self._record = canonical
        self._canonical_key: CanonicalKey = canonical_key(canonical)
        Element.__init__(self, parent)

    def parent(self) -> StableGraphs:
        return cast(StableGraphs, Element.parent(self))

    def _canonical_record(self) -> _GraphRecord:
        r"""Return the private skeletal half-edge record for this element."""
        return self._record

    def canonical_key(self) -> CanonicalKey:
        return self._canonical_key

    def num_vertices(self) -> int:
        return self._record.num_vertices()

    def num_flags(self) -> int:
        return self._record.num_flags()

    def internal_edges(self) -> tuple[tuple[int, int], ...]:
        return self._record.internal_edges()

    def num_edges(self) -> int:
        return self._record.num_edges()

    def num_markings(self) -> int:
        return self._record.num_markings()

    def genus(self) -> int:
        return self._record.genus()

    def total_genus(self) -> int:
        return self._record.genus()

    def vertex_genera(self) -> tuple[int, ...]:
        return self._record.vertex_genera

    def valence(self, vertex: int) -> int:
        return self._record.valence(vertex)

    def is_stable(self) -> bool:
        return self._record.is_stable()

    def is_smooth(self) -> bool:
        return self._record.num_edges() == 0

    def first_betti_number(self) -> int:
        return self._record.first_betti_number()

    def codimension(self) -> int:
        return self._record.num_edges()

    def stratum_dimension(self) -> int:
        return sum(3 * self._record.vertex_genera[v] - 3 + self._record.valence(v) for v in range(self._record.num_vertices()))

    def automorphism_number(self) -> int:
        return automorphism_number(self._record)

    def one_edge_degenerations(self) -> tuple[StableGraph, ...]:
        from .enumeration import one_edge_degenerations

        return one_edge_degenerations(self)

    def contracts_to(self, other: StableGraph) -> bool:
        if other.num_edges() > self.num_edges():
            return False
        target = other.canonical_key()
        if self.canonical_key() == target:
            return True
        visited: set[object] = {self.canonical_key()}
        queue: deque[StableGraph] = deque([self])
        while queue:
            current = queue.popleft()
            current_graph = current._canonical_record()
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

    def admits_contraction_to(self, other: StableGraph) -> bool:
        return self.contracts_to(other)

    def edge_orbits(self) -> tuple[tuple[tuple[int, int], ...], ...]:
        from .edge_orbits import automorphism_edge_orbits

        return automorphism_edge_orbits(self._record)

    def elementary_contractions(self) -> tuple[tuple[StableGraph, object, int], ...]:
        r"""One entry per ``Aut`` edge orbit: ``(target, contraction witness, orbit size)``."""
        from .edge_orbits import _elementary_contraction_data

        return _elementary_contraction_data(self)

    def contraction_target_multiset(self) -> tuple[tuple[StableGraph, int], ...]:
        r"""Multiset of contraction targets ``([Γ/e], |O_e|)`` over Aut edge orbits."""
        from .edge_orbits import contraction_target_multiset

        return contraction_target_multiset(self)

    def covers(self) -> tuple[tuple[StableGraph, StableGraph], ...]:
        r"""Distinct contraction targets ``[\Gamma/e]``, one per ``Aut(\Gamma)`` edge orbit."""
        from .edge_orbits import automorphism_edge_orbit_indices

        seen: dict[object, tuple[StableGraph, StableGraph]] = {}
        graph = self._record
        for group in automorphism_edge_orbit_indices(graph):
            representative = graph.internal_edges()[group[0]]
            target_type, _ = graph.contract(representative)
            target = self.parent()(target_type)
            key = target.canonical_key()
            if key not in seen:
                seen[key] = (target, self)
        return tuple(seen.values())

    def split_system(self, anchor_marking: int = 1) -> frozenset[frozenset[int]]:
        from .splits import split_system

        return split_system(self, anchor_marking=anchor_marking)

    def relabel_markings(self, sigma: Callable[[int], int]) -> StableGraph:
        r"""Apply a permutation of ``{1, ..., n}`` to the marking labels."""
        record = self._record
        genera = record.vertex_genera
        markings = tuple(record.markings_at(vertex) for vertex in range(record.num_vertices()))
        relabeled_markings = tuple(tuple(int(sigma(marking)) for marking in vertex_markings) for vertex_markings in markings)
        edges = tuple((record.flag_vertex[flag], record.flag_vertex[partner]) for flag, partner in record.internal_edges())
        return self.parent().from_vertices(genera=genera, markings=relabeled_markings, edges=edges)

    def to_json(self) -> dict[str, object]:
        return to_json(self._record, self.parent().genus(), self.parent().number_of_markings())

    def vertices(self) -> Vertices:
        return Vertices(self)

    def half_edges(self) -> HalfEdges:
        return HalfEdges(self)

    def edges(self) -> Edges:
        return Edges(self)

    def legs(self) -> Legs:
        return Legs(self)

    def automorphism_group(self, on: str | None = None) -> object:
        if on is None:
            return automorphism_group(self._record)
        return self._record.automorphism_group(on=on)

    def action_on_half_edges(self) -> Action:
        from sage.sets.finite_enumerated_set import FiniteEnumeratedSet

        n = self._record.num_flags()
        return _permutation_action(
            self.automorphism_group(on="half_edges"),
            FiniteEnumeratedSet(range(1, n + 1)),
        )

    def action_on_edges(self) -> Action:
        from sage.sets.finite_enumerated_set import FiniteEnumeratedSet

        n = self.num_edges()
        return _permutation_action(
            self.automorphism_group(on="edges"),
            FiniteEnumeratedSet(range(1, n + 1)),
        )

    def action_on_vertices(self) -> Action:
        from sage.sets.finite_enumerated_set import FiniteEnumeratedSet

        n = self.num_vertices()
        return _permutation_action(
            self.automorphism_group(on="vertices"),
            FiniteEnumeratedSet(range(1, n + 1)),
        )

    def flags_at(self, vertex: int) -> tuple[int, ...]:
        return self._record.flags_at(vertex)

    def half_edges_at(self, vertex: int) -> tuple[int, ...]:
        return self.flags_at(vertex)

    def vertex_genus(self, vertex: int) -> int:
        return self._record.vertex_genera[vertex]

    def _Hom_(self, other: object, category: object = None) -> object:
        r"""Return `\operatorname{Hom}_{\Gamma}(self, other)` with contraction morphisms."""
        from .gamma import StableGraphCategory

        if not isinstance(other, StableGraph):
            raise TypeError(f"expected StableGraph; found {type(other)}")
        if self.genus() != other.genus() or self.num_markings() != other.num_markings():
            raise TypeError("Hom requires stable graphs of the same type (g, n)")
        return StableGraphCategory(self.genus(), self.num_markings()).hom(self, other)

    def _richcmp_(self, other: object, op: int) -> bool:
        from sage.structure.richcmp import richcmp

        assert isinstance(other, StableGraph)
        return bool(richcmp(self._canonical_key, other._canonical_key, op))

    def __getstate__(self) -> tuple[StableGraphs, _GraphRecord, CanonicalKey]:
        return (self.parent(), self._record, self._canonical_key)

    def __setstate__(self, state: tuple[StableGraphs, _GraphRecord, CanonicalKey]) -> None:
        parent, graph, key = state
        Element.__init__(self, parent)
        self._record = graph
        self._canonical_key = key

    def _repr_(self) -> str:
        genera = self._record.vertex_genera
        return f"Stable graph type of genus {self.total_genus()} with {self.num_edges()} node(s), vertex genera {genera}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, StableGraph):
            return self._canonical_key == other._canonical_key and self.parent() is other.parent()
        if isinstance(other, _GraphRecord):
            return self._record == other
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.parent().genus(), self.parent().number_of_markings(), self._canonical_key))


StableGraphs.Element = StableGraph


class Vertices(UniqueRepresentation, Parent):
    Element: ClassVar[type[Vertex]]

    def __init__(self, graph: StableGraph) -> None:
        from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets

        self._graph = graph
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def _element_constructor_(self, x: object) -> Vertex:
        if isinstance(x, Vertex):
            if x.parent() is self:
                return x
            index = x._index
        else:
            index = as_int(x)
        if index < 0 or index >= self._graph.num_vertices():
            raise ValueError(f"{index} is not a vertex of {self._graph!r}")
        return cast(Vertex, self.element_class(self, index))

    def __iter__(self) -> Iterator[Vertex]:
        for v in range(self._graph.num_vertices()):
            yield self.element_class(self, v)

    def cardinality(self) -> int:
        return self._graph.num_vertices()


class Vertex(Element):
    def __init__(self, parent: Vertices, index: int) -> None:
        self._index = int(index)
        Element.__init__(self, parent)

    def genus(self) -> int:
        parent = self.parent()
        assert isinstance(parent, Vertices), f"Vertex.parent must be Vertices; found {type(parent)!r}"
        return int(parent._graph.vertex_genus(self._index))

    def valence(self) -> int:
        parent = self.parent()
        assert isinstance(parent, Vertices), f"Vertex.parent must be Vertices; found {type(parent)!r}"
        return int(parent._graph._record.valence(self._index))

    def _repr_(self) -> str:
        return f"Vertex({self._index})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vertex):
            return self.parent() is other.parent() and self._index == other._index
        if isinstance(other, int):
            return self._index == other
        return NotImplemented

    def __hash__(self) -> int:
        return hash((id(self.parent()), self._index))


Vertices.Element = Vertex


class HalfEdges(UniqueRepresentation, Parent):
    Element: ClassVar[type[HalfEdge]]

    def __init__(self, graph: StableGraph) -> None:
        from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets

        self._graph = graph
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def _element_constructor_(self, x: object) -> HalfEdge:
        if isinstance(x, HalfEdge):
            if x.parent() is self:
                return x
            index = x._index
        else:
            index = as_int(x)
        if index < 0 or index >= self._graph._record.num_flags():
            raise ValueError(f"{index} is not a half-edge of {self._graph!r}")
        return cast(HalfEdge, self.element_class(self, index))

    def __iter__(self) -> Iterator[HalfEdge]:
        for h in range(self._graph._record.num_flags()):
            yield self.element_class(self, h)

    def cardinality(self) -> int:
        return self._graph._record.num_flags()


class HalfEdge(Element):
    def __init__(self, parent: HalfEdges, index: int) -> None:
        self._index = int(index)
        Element.__init__(self, parent)

    def vertex(self) -> int:
        parent = self.parent()
        assert isinstance(parent, HalfEdges), f"HalfEdge.parent must be HalfEdges; found {type(parent)!r}"
        return int(parent._graph._record.flag_vertex[self._index])

    def partner(self) -> int:
        parent = self.parent()
        assert isinstance(parent, HalfEdges), f"HalfEdge.parent must be HalfEdges; found {type(parent)!r}"
        return int(parent._graph._record.flag_involution[self._index])

    def _repr_(self) -> str:
        return f"HalfEdge({self._index})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, HalfEdge):
            return self.parent() is other.parent() and self._index == other._index
        if isinstance(other, int):
            return self._index == other
        return NotImplemented

    def __hash__(self) -> int:
        return hash((id(self.parent()), self._index))


HalfEdges.Element = HalfEdge


class Edges(UniqueRepresentation, Parent):
    Element: ClassVar[type[Edge]]

    def __init__(self, graph: StableGraph) -> None:
        from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets

        self._graph = graph
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def _element_constructor_(self, x: object) -> Edge:
        if isinstance(x, Edge):
            if x.parent() is self:
                return x
            pair = x._pair
        elif isinstance(x, tuple) and len(x) == 2:
            pair = (as_int(x[0]), as_int(x[1]))
        elif isinstance(x, int):
            edges = self._graph._record.internal_edges()
            if x < 0 or x >= len(edges):
                raise ValueError(f"{x} is not an edge index of {self._graph!r}")
            return cast(Edge, self.element_class(self, x, edges[x]))
        else:
            raise TypeError("edges are Edge elements, edge indices, or half-edge pairs")
        for i, existing in enumerate(self._graph._record.internal_edges()):
            if existing == pair or existing == (pair[1], pair[0]):
                return cast(Edge, self.element_class(self, i, existing))
        raise ValueError(f"{pair} is not an edge of {self._graph!r}")

    def __iter__(self) -> Iterator[Edge]:
        for i, pair in enumerate(self._graph._record.internal_edges()):
            yield self.element_class(self, i, pair)

    def cardinality(self) -> int:
        return self._graph.num_edges()


class Edge(Element):
    def __init__(self, parent: Edges, index: int, pair: tuple[int, int]) -> None:
        self._index = int(index)
        self._pair = pair
        Element.__init__(self, parent)

    def half_edges(self) -> tuple[int, int]:
        return self._pair

    def _repr_(self) -> str:
        return f"Edge{self._pair}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Edge):
            return self.parent() is other.parent() and self._pair == other._pair
        if isinstance(other, tuple):
            return self._pair == other or self._pair == (other[1], other[0])
        return NotImplemented

    def __hash__(self) -> int:
        return hash((id(self.parent()), self._pair))


Edges.Element = Edge


class Legs(UniqueRepresentation, Parent):
    Element: ClassVar[type[Leg]]

    def __init__(self, graph: StableGraph) -> None:
        from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets

        self._graph = graph
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def _element_constructor_(self, x: object) -> Leg:
        if isinstance(x, Leg):
            if x.parent() is self:
                return x
            label = x._label
        else:
            label = as_int(x)
        legs = self._graph._record.legs()
        if label < 1 or label > len(legs):
            raise ValueError(f"{label} is not a leg label of {self._graph!r}")
        return cast(Leg, self.element_class(self, label, legs[label - 1]))

    def __iter__(self) -> Iterator[Leg]:
        for i, flag in enumerate(self._graph._record.legs()):
            yield self.element_class(self, i + 1, flag)

    def cardinality(self) -> int:
        return self._graph.num_markings()


class Leg(Element):
    def __init__(self, parent: Legs, label: int, flag: int) -> None:
        self._label = int(label)
        self._flag = int(flag)
        Element.__init__(self, parent)

    def label(self) -> int:
        return self._label

    def _repr_(self) -> str:
        return f"Leg({self._label})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Leg):
            return self.parent() is other.parent() and self._label == other._label
        if isinstance(other, int):
            return self._label == other
        return NotImplemented

    def __hash__(self) -> int:
        return hash((id(self.parent()), self._label))


Legs.Element = Leg
