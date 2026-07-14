r"""Parent ``StableGraphs(g, I)`` of canonical stable graphs with typed incidence sets."""

from __future__ import annotations

from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from sage.categories.action import Action

from .canonical import canonical_record
from .graph_types import StableGraphTypes
from .records import StableGraph as StableGraphRecord
from .records import intern_graph


def _markings(I: object) -> tuple[int, ...]:
    from sage.rings.integer import Integer

    if isinstance(I, (int, Integer)):
        return tuple(range(1, int(I) + 1))
    return tuple(int(x) for x in I)


class _PermutationAction(Action):
    r"""Left action of a permutation group on a finite enumerated set of labels."""

    def _act_(self, g: object, x: object) -> object:
        # Sage permutations are 1-based on {1,...,n}; labels may be 0-based indices.
        labels = list(self.codomain())
        if x not in labels:
            raise ValueError(f"{x!r} not in action codomain")
        # Prefer native permutation action when labels are the standard domain.
        try:
            return g(x)
        except (TypeError, ValueError, IndexError):
            pass
        idx = labels.index(x)
        # Fall back: interpret g as acting on positions 1..n.
        image_pos = int(g(idx + 1)) - 1
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
        labels = tuple(domain)
    key = (id(group), labels)
    cached = _PERMUTATION_ACTIONS.get(key)
    if cached is not None:
        return cached
    S = FiniteEnumeratedSet(labels)
    action = _PermutationAction(group, S, is_left=True, op=None)
    _PERMUTATION_ACTIONS[key] = action
    return action


class StableGraphs(UniqueRepresentation, Parent):
    r"""Finite enumerated set of isomorphism classes of stable graphs of type `(g,I)`."""

    def __init__(self, g: int, I: object) -> None:
        self._g = int(g)
        self._I = _markings(I)
        self._n = len(self._I)
        self._types = StableGraphTypes(self._g, self._n)
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def genus(self) -> int:
        return self._g

    def marking_set(self) -> tuple[int, ...]:
        return self._I

    def number_of_markings(self) -> int:
        return self._n

    def _element_constructor_(self, data: object) -> StableGraph:
        if isinstance(data, StableGraph):
            assert data.parent() is self
            return data
        if isinstance(data, StableGraphRecord):
            rec = intern_graph(canonical_record(data))
            return StableGraph(self, rec)
        raise TypeError(f"cannot construct StableGraph from {type(data)}")

    def __iter__(self):
        for gamma in self._types:
            yield StableGraph(self, gamma.canonical_representative())

    def cardinality(self) -> int:
        return int(self._types.cardinality()) if hasattr(self._types, "cardinality") else len(list(self))

    def an_element(self) -> StableGraph:
        return StableGraph(self, self._types.smooth().canonical_representative())

    def smooth(self) -> StableGraph:
        return self.an_element()

    def __contains__(self, obj: object) -> bool:
        if isinstance(obj, StableGraph):
            return obj.parent() is self or (
                obj.genus() == self._g and obj.num_markings() == self._n
            )
        if isinstance(obj, StableGraphRecord):
            try:
                return obj.genus() == self._g and obj.num_markings() == self._n
            except Exception:
                return False
        return False

    def half_edges_at(self, graph: StableGraph | StableGraphRecord, vertex: int) -> tuple[int, ...]:
        rec = graph.record() if isinstance(graph, StableGraph) else graph
        return rec.flags_at(vertex)

    def _repr_(self) -> str:
        return f"StableGraphs({self._g}, {self._I})"


class StableGraph(Element):
    r"""Canonical stable graph element of :class:`StableGraphs`."""

    def __init__(self, parent: StableGraphs, record: StableGraphRecord) -> None:
        self._record = record
        Element.__init__(self, parent)

    def record(self) -> StableGraphRecord:
        return self._record

    def num_vertices(self) -> int:
        return self._record.num_vertices()

    def num_edges(self) -> int:
        return self._record.num_edges()

    def num_markings(self) -> int:
        return self._record.num_markings()

    def genus(self) -> int:
        return self._record.genus()

    def vertex_genera(self) -> tuple[int, ...]:
        return self._record.vertex_genera

    def vertices(self) -> Vertices:
        return Vertices(self)

    def half_edges(self) -> HalfEdges:
        return HalfEdges(self)

    def edges(self) -> Edges:
        return Edges(self)

    def legs(self) -> Legs:
        return Legs(self)

    def automorphism_group(self, on: str = "half_edges") -> object:
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
        return StableGraphCategory(self.genus(), self.num_markings()).hom(self.record(), other.record())

    def _repr_(self) -> str:
        return f"StableGraph(g={self.genus()}, e={self.num_edges()})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, StableGraph):
            return self._record is other._record or self._record == other._record
        if isinstance(other, StableGraphRecord):
            return self._record == other
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self._record)


class Vertices(UniqueRepresentation, Parent):
    def __init__(self, graph: StableGraph) -> None:
        from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets

        self._graph = graph
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def __iter__(self):
        for v in range(self._graph.num_vertices()):
            yield Vertex(self, v)

    def cardinality(self) -> int:
        return self._graph.num_vertices()


class Vertex(Element):
    def __init__(self, parent: Vertices, index: int) -> None:
        self._index = int(index)
        Element.__init__(self, parent)

    def genus(self) -> int:
        return self.parent()._graph.vertex_genus(self._index)  # type: ignore[attr-defined]

    def valence(self) -> int:
        return self.parent()._graph.record().valence(self._index)  # type: ignore[attr-defined]

    def _repr_(self) -> str:
        return f"Vertex({self._index})"


class HalfEdges(UniqueRepresentation, Parent):
    def __init__(self, graph: StableGraph) -> None:
        from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets

        self._graph = graph
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def __iter__(self):
        for h in range(self._graph.record().num_flags()):
            yield HalfEdge(self, h)

    def cardinality(self) -> int:
        return self._graph.record().num_flags()


class HalfEdge(Element):
    def __init__(self, parent: HalfEdges, index: int) -> None:
        self._index = int(index)
        Element.__init__(self, parent)

    def vertex(self) -> int:
        return self.parent()._graph.record().flag_vertex[self._index]  # type: ignore[attr-defined]

    def partner(self) -> int:
        return self.parent()._graph.record().flag_involution[self._index]  # type: ignore[attr-defined]

    def _repr_(self) -> str:
        return f"HalfEdge({self._index})"


class Edges(UniqueRepresentation, Parent):
    def __init__(self, graph: StableGraph) -> None:
        from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets

        self._graph = graph
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def __iter__(self):
        for i, pair in enumerate(self._graph.record().internal_edges()):
            yield Edge(self, i, pair)

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


class Legs(UniqueRepresentation, Parent):
    def __init__(self, graph: StableGraph) -> None:
        from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets

        self._graph = graph
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def __iter__(self):
        for i, flag in enumerate(self._graph.record().legs()):
            yield Leg(self, i + 1, flag)

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
