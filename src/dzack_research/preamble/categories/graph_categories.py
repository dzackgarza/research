r"""Owned finite graphs, digraphs, and labelled graph structures.

A finite digraph is a finite vertex set together with a binary adjacency
relation; its morphisms are vertex maps preserving adjacency.  An undirected
graph is the symmetric case.  A labelled graph or digraph additionally carries
vertex and edge labels, and its morphisms preserve those labels.  These are the
standard graph-homomorphism notions (see Diestel, *Graph Theory*, Chapter 1,
and Bang-Jensen--Gutin, *Digraphs*, Chapter 1).
"""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.structure.element import parent as element_parent

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
    _precomposable,
)
from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of


class _FiniteDigraphEngine:
    r"""Private realization of one finite directed or symmetric graph."""

    def __init__(
        self,
        vertices,
        edges,
        *,
        symmetric=False,
        vertex_labels=None,
        edge_labels=None,
        **rest,
    ) -> None:
        self._vertices = finite_ordered_set(vertices)
        self._edge_space = self._vertices**2
        self._edges = finite_ordered_set(edges)
        self._symmetric = bool(symmetric)
        self._vertex_labels = vertex_labels
        self._edge_labels = edge_labels
        super().__init__(facade=True, **rest)

    def vertices(self):
        return self._vertices

    def edges(self):
        return self._edges

    def edge_space(self):
        return self._edge_space

    def __contains__(self, vertex) -> bool:
        return vertex in self.vertices()

    is_parent_of = __contains__

    def _element_constructor_(self, vertex):
        return self.vertices()(vertex)

    def __iter__(self):
        return iter(self.vertices())

    def cardinality(self):
        return self.vertices().cardinality()

    def has_edge(self, left, right) -> bool:
        edge = self.edge_space()((left, right))
        reverse = self.edge_space()((right, left))
        return edge in self.edges() or (
            self._symmetric and reverse in self.edges()
        )

    def is_directed(self) -> bool:
        return not self._symmetric

    def is_symmetric(self) -> bool:
        return self._symmetric

    def vertex_label(self, vertex):
        if self._vertex_labels is None:
            raise ValueError("this graph has no selected vertex labels")
        return self._vertex_labels[vertex]

    def edge_label(self, left, right):
        if self._edge_labels is None:
            raise ValueError("this graph has no selected edge labels")
        edge = self.edge_space()((left, right))
        reverse = self.edge_space()((right, left))
        match edge in self._edge_labels:
            case True:
                return self._edge_labels[edge]
            case False if self._symmetric and reverse in self._edge_labels:
                return self._edge_labels[reverse]
            case False:
                raise ValueError("the selected vertices are not joined by a labelled edge")


@cached_function
def _finite_digraph_engine_with(mixin):
    r"""Compose one consumer's private realization with the graph owner's engine.

    The consumer supplies only its additional private operations/data.  The
    graph owner retains authority over vertices, edges, adjacency, labels and
    the underlying Parent realization.
    """
    return type(
        f"_{mixin.__name__.lstrip('_')}OnFiniteDigraph",
        (mixin, _FiniteDigraphEngine),
        {},
    )


class GraphMorphism(Morphism):
    r"""A vertex map preserving directed adjacency."""

    def __init__(self, parent, set_morphism) -> None:
        Morphism.__init__(self, parent)
        self._set_morphism = set_morphism

    def underlying_set_morphism(self):
        return self._set_morphism

    def __call__(self, vertex):
        return self.underlying_set_morphism()(vertex)

    def __mul__(self, other):
        if not _precomposable(self, other):
            return NotImplemented
        return self.parent()._from_graph_map(
            self.underlying_set_morphism() * other.underlying_set_morphism()
        )

    def __eq__(self, other) -> bool:
        return (
            element_parent(other) is self.parent()
            and other.underlying_set_morphism() == self.underlying_set_morphism()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None


class DigraphHomset(CategoricalHomset):
    r"""Adjacency-preserving vertex maps between represented digraphs."""

    Element = GraphMorphism

    def _verify_graph_map(self, morphism) -> None:
        for left, right in self.domain().edges():
            if not self.codomain().has_edge(morphism(left), morphism(right)):
                raise ValueError("a digraph morphism must preserve directed adjacency")

    def _element_constructor_(self, datum):
        if element_parent(datum) is self:
            return datum
        set_morphism = Sets().Mor(self.domain(), self.codomain())(datum)
        morphism = self.element_class(self, set_morphism)
        self._verify_graph_map(morphism)
        return morphism

    def _from_graph_map(self, set_morphism):
        return self.element_class(self, set_morphism)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on one graph")
        return self._from_graph_map(
            Sets().Mor(self.domain(), self.domain()).identity()
        )


class LabelledDigraphHomset(DigraphHomset):
    r"""Digraph morphisms preserving the selected vertex and edge labels."""

    def _verify_graph_map(self, morphism) -> None:
        super()._verify_graph_map(morphism)
        for vertex in self.domain().vertices():
            if self.domain().vertex_label(vertex) != self.codomain().vertex_label(
                morphism(vertex)
            ):
                raise ValueError("a labelled-graph morphism must preserve vertex labels")
        for left, right in self.domain().edges():
            if self.domain().edge_label(left, right) != self.codomain().edge_label(
                morphism(left), morphism(right)
            ):
                raise ValueError("a labelled-graph morphism must preserve edge labels")


class DigraphHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = DigraphHomset


class LabelledDigraphHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = LabelledDigraphHomset


class Digraphs(OwnedCategory):
    r"""Finite directed graphs with graph homomorphisms."""

    _HomCategory = DigraphHomCategoryConstruction

    def super_categories(self):
        return [Sets()]

    @classmethod
    def _repr_object_names(cls):
        return "finite directed graphs"

    def an_object(self):
        return self.from_edges((0, 1), ((0, 1),))

    def from_edges(self, vertices, edges):
        vertices = finite_ordered_set(vertices)
        edge_space = vertices**2
        normalized = finite_ordered_set(tuple(edge_space(edge) for edge in edges))
        if any(
            edge[0] not in vertices or edge[1] not in vertices
            for edge in normalized
        ):
            raise ValueError("a directed edge has two endpoints in the vertex set")
        return _object_of(
            self,
            _engine=(self, _FiniteDigraphEngine, None),
            vertices=vertices,
            edges=normalized,
            symmetric=False,
        )


class Graphs(OwnedCategory):
    r"""Finite undirected graphs, viewed as symmetric directed graphs."""

    _HomCategory = DigraphHomCategoryConstruction

    def super_categories(self):
        return [Digraphs()]

    @classmethod
    def _repr_object_names(cls):
        return "finite graphs"

    def an_object(self):
        return self.from_edges((0, 1), ((0, 1),))

    def from_edges(self, vertices, edges):
        vertices = finite_ordered_set(vertices)
        edge_space = vertices**2
        normalized = finite_ordered_set(tuple(edge_space(edge) for edge in edges))
        if any(
            edge[0] not in vertices or edge[1] not in vertices
            for edge in normalized
        ):
            raise ValueError("an edge has two endpoints in the vertex set")
        return _object_of(
            self,
            _engine=(self, _FiniteDigraphEngine, None),
            vertices=vertices,
            edges=normalized,
            symmetric=True,
        )


class LabelledDigraphs(OwnedCategory):
    r"""Finite digraphs with selected vertex and edge labels."""

    _HomCategory = LabelledDigraphHomCategoryConstruction

    def super_categories(self):
        return [Digraphs()]

    @classmethod
    def _repr_object_names(cls):
        return "labelled finite directed graphs"

    def an_object(self):
        return self.from_labels(
            (0, 1),
            ((0, 1),),
            {0: "source", 1: "target"},
            {(0, 1): "arrow"},
        )

    def from_labels(self, vertices, edges, vertex_labels, edge_labels):
        vertices = finite_ordered_set(vertices)
        edge_space = vertices**2
        edges = finite_ordered_set(tuple(edge_space(edge) for edge in edges))
        if any(
            edge[0] not in vertices or edge[1] not in vertices
            for edge in edges
        ):
            raise ValueError("a directed edge has two endpoints in the vertex set")
        if set(vertex_labels) != set(vertices):
            raise ValueError("a labelled digraph has one vertex label per vertex")
        normalized_edge_labels = {
            edge_space(edge): label for edge, label in edge_labels.items()
        }
        if set(normalized_edge_labels) != set(edges):
            raise ValueError("a labelled digraph has one edge label per edge")
        return _object_of(
            self,
            _engine=(self, _FiniteDigraphEngine, None),
            vertices=vertices,
            edges=edges,
            symmetric=False,
            vertex_labels=dict(vertex_labels),
            edge_labels=normalized_edge_labels,
        )


class LabelledGraphs(OwnedCategory):
    r"""Finite undirected graphs with selected vertex and edge labels."""

    _HomCategory = LabelledDigraphHomCategoryConstruction

    def super_categories(self):
        return [Graphs(), LabelledDigraphs()]

    @classmethod
    def _repr_object_names(cls):
        return "labelled finite graphs"

    def an_object(self):
        return self.from_labels(
            (0, 1),
            ((0, 1),),
            {0: "left", 1: "right"},
            {(0, 1): "edge"},
        )

    def object(
        self,
        vertices,
        edges,
        vertex_labels,
        edge_labels,
        *,
        categories=(),
        construction_data=None,
        _engine=None,
    ):
        r"""Construct a labelled graph, optionally with stronger owned structure.

        ``LabelledGraphs`` owns the private finite-graph realization.  A
        mathematical specialization supplies only its additional category and
        construction data; it never imports or subclasses that private engine.
        """
        vertices = finite_ordered_set(vertices)
        edge_space = vertices**2
        edges = finite_ordered_set(tuple(edge_space(edge) for edge in edges))
        if any(
            edge[0] not in vertices or edge[1] not in vertices
            for edge in edges
        ):
            raise ValueError("an edge has two endpoints in the vertex set")
        if set(vertex_labels) != set(vertices):
            raise ValueError("a labelled graph has one vertex label per vertex")
        normalized_edge_labels = {
            edge_space(edge): label for edge, label in edge_labels.items()
        }
        if set(normalized_edge_labels) != set(edges):
            raise ValueError("a labelled graph has one edge label per edge")
        category = Cat().meet((self, *tuple(categories)))
        realization = (
            _FiniteDigraphEngine
            if _engine is None
            else _finite_digraph_engine_with(_engine)
        )
        return _object_of(
            category,
            _engine=(self, realization, None),
            vertices=vertices,
            edges=edges,
            symmetric=True,
            vertex_labels=dict(vertex_labels),
            edge_labels=normalized_edge_labels,
            **dict(construction_data or {}),
        )

    def from_labels(self, vertices, edges, vertex_labels, edge_labels):
        return self.object(vertices, edges, vertex_labels, edge_labels)


__all__ = [
    "Digraphs",
    "Graphs",
    "LabelledDigraphs",
    "LabelledGraphs",
]
