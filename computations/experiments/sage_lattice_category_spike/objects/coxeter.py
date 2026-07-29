r"""Coxeter diagrams as Sage parents.

EXAMPLES::

    sage: from sage_lattice_category_spike import CoxeterDiagrams, Lattice
    sage: diagram = Lattice("A3").coxeter_diagram()
    sage: diagram.category().is_subcategory(CoxeterDiagrams().Finite())
    True
    sage: diagram.coxeter_matrix()
    [1 3 2]
    [3 1 3]
    [2 3 1]
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Iterator, Mapping, Sequence
from typing import TYPE_CHECKING, Any, ClassVar, cast

from sage.categories.category import Category
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.matrix.constructor import matrix
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.category_object import normalize_names
from sage.structure.element_wrapper import ElementWrapper
from sage.structure.parent import Parent

from ..lexicon import CartanType, CoxeterDiagram, CoxeterMatrix, Graph
from .categories import own_methods
from .functors import CatObject


class CoxeterDiagrams(CatObject, Category):
    r"""Finite Coxeter diagrams and Coxeter-matrix-preserving maps."""

    def _repr_object_names(self) -> str:
        return "finite Coxeter diagrams"

    def super_categories(self) -> list[Category]:
        return [FiniteEnumeratedSets()]

    ParentMethods = own_methods(CoxeterDiagram)

    def from_coxeter_matrix(
        self,
        coxeter_matrix: CoxeterMatrix,
        names: Sequence[str] | str | None = None,
    ) -> FiniteCoxeterDiagram:
        r"""Construct a diagram from its Coxeter matrix."""
        return FiniteCoxeterDiagram(coxeter_matrix, names=names)

    def from_cartan_type(
        self,
        cartan_type: CartanType,
        names: Sequence[str] | str | None = None,
    ) -> FiniteCoxeterDiagram:
        r"""Construct the diagram of a crystallographic Cartan type."""
        return self.from_coxeter_matrix(CoxeterMatrix(cartan_type), names=names)


class CoxeterVertex(ElementWrapper):
    r"""A vertex of a finite Coxeter diagram."""

    def _repr_(self) -> str:
        parent = cast(FiniteCoxeterDiagram, self.parent())
        return parent.variable_names()[parent.index_set().index(self.value)]


if TYPE_CHECKING:
    CoxeterDiagramParent = Parent[CoxeterVertex]
else:
    CoxeterDiagramParent = Parent


class FiniteCoxeterDiagram(CoxeterDiagram, CoxeterDiagramParent):
    r"""A finite Coxeter diagram whose elements are its vertices."""

    Element = CoxeterVertex

    if TYPE_CHECKING:
        element_class: ClassVar[type[CoxeterVertex]]

    def __init__(
        self,
        coxeter_matrix: CoxeterMatrix,
        names: Sequence[str] | str | None = None,
        source_lattice: Any | None = None,
        roots: Sequence[Any] | None = None,
        positions: Mapping[Hashable, Sequence[object]] | None = None,
        root_intersection_matrix: Sequence[Sequence[object]] | None = None,
    ) -> None:
        self._coxeter_matrix = CoxeterMatrix(coxeter_matrix)
        self._index_set = tuple(self._coxeter_matrix.index_set())
        rank = len(self._index_set)
        if names is None:
            names = tuple(f"s_{i}" for i in self._index_set)
        if roots is not None:
            assert source_lattice is not None, "roots require their source lattice"
            assert len(roots) == rank, f"a rooted Coxeter diagram needs one root for every vertex; rank={rank}, roots={len(roots)}"
            assert all(root.parent() is source_lattice for root in roots), (
                "diagram roots must be elements of the declared source lattice, not coordinate rows"
            )
        if root_intersection_matrix is not None:
            root_intersections = tuple(tuple(ZZ(entry) for entry in row) for row in root_intersection_matrix)
            assert len(root_intersections) == rank and all(len(row) == rank for row in root_intersections), (
                f"root intersection matrix must be {rank} by {rank}; found={root_intersections!r}"
            )
        else:
            root_intersections = None
        self._source_lattice = source_lattice
        self._roots = None if roots is None else tuple(roots)
        self._root_intersection_matrix = root_intersections
        self._preferred_positions = _normalize_positions(self._index_set, positions)
        self._computed_positions: dict[Hashable, tuple[Any, Any]] | None = None
        Parent.__init__(
            self,
            category=CoxeterDiagrams(),
            names=normalize_names(rank, names),
        )

    @classmethod
    def from_cartan_type(
        cls,
        cartan_type: CartanType,
        names: Sequence[str] | str | None = None,
    ) -> FiniteCoxeterDiagram:
        r"""Construct the diagram of a crystallographic Cartan type."""
        return cls(CoxeterMatrix(cartan_type), names=names)

    @classmethod
    def from_lattice_roots(
        cls,
        source_lattice: Any,
        roots: Sequence[Any],
        names: Sequence[str] | str | None = None,
        positions: Mapping[Hashable, Sequence[object]] | None = None,
        index_set: Sequence[Hashable] | None = None,
    ) -> FiniteCoxeterDiagram:
        r"""Construct the diagram determined by actual roots in a lattice.

        The roots must already be elements of ``source_lattice``.  This method
        reads their bilinear pairings, records the full intersection matrix
        including diagonal squares, and derives the Coxeter exponents from the
        rank-two reflection angles.
        """
        roots = tuple(roots)
        rank = len(roots)
        if index_set is None:
            index_set = tuple(range(rank))
        else:
            index_set = tuple(index_set)
        assert len(index_set) == rank, f"index set must have one entry per root; index_set={index_set!r}, roots={rank}"
        assert all(root.parent() is source_lattice for root in roots), (
            "diagram roots must be elements of the declared source lattice, not coordinate rows"
        )
        intersections = tuple(tuple(ZZ(source_lattice.b(left, right)) for right in roots) for left in roots)
        entries = [[ZZ.one() if i == j else _coxeter_exponent(intersections[i][i], intersections[j][j], intersections[i][j]) for j in range(rank)] for i in range(rank)]
        return cls(
            CoxeterMatrix(entries, index_set=index_set),
            names=names,
            source_lattice=source_lattice,
            roots=roots,
            positions=positions,
            root_intersection_matrix=intersections,
        )

    def _Hom_(
        self,
        codomain: FiniteCoxeterDiagram,
        category: Category | None = None,
    ) -> CoxeterDiagramHomset:
        return CoxeterDiagramHomset(self, codomain, category=category)

    def hom(
        self,
        images: Mapping[Hashable, Hashable] | Sequence[Hashable],
        codomain: FiniteCoxeterDiagram,
    ) -> CoxeterDiagramMorphism:
        r"""Construct the Coxeter-matrix-preserving map with the given images."""
        return cast(CoxeterDiagramMorphism, self._Hom_(codomain)(images))

    def _repr_(self) -> str:
        return f"Finite Coxeter diagram on {self.cardinality()} vertices"

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, FiniteCoxeterDiagram)
            and self._index_set == other._index_set
            and self._matrix_entries() == other._matrix_entries()
            and self.variable_names() == other.variable_names()
            and self._root_intersection_matrix == other._root_intersection_matrix
            and self._preferred_positions == other._preferred_positions
        )

    def __hash__(self) -> int:
        return hash(
            (
                self._index_set,
                self._matrix_entries(),
                self.variable_names(),
                self._root_intersection_matrix,
                None if self._preferred_positions is None else tuple(sorted(self._preferred_positions.items())),
            )
        )

    def __contains__(self, vertex: object) -> bool:
        if isinstance(vertex, CoxeterVertex):
            return vertex.parent() is self
        return vertex in self._index_set

    def _element_constructor_(self, vertex: object) -> CoxeterVertex:
        if isinstance(vertex, CoxeterVertex):
            assert vertex.parent() is self, f"a vertex belongs to a different Coxeter diagram; vertex={vertex!r}"
            return vertex
        assert vertex in self._index_set, f"a vertex must lie in the index set; vertex={vertex!r}, index_set={self._index_set!r}"
        return self.element_class(self, vertex)

    def __iter__(self) -> Iterator[CoxeterVertex]:
        return (self(vertex) for vertex in self._index_set)

    def cardinality(self) -> Integer:
        return ZZ(len(self._index_set))

    def vertex(self, index: int) -> CoxeterVertex:
        return self(self._index_set[index])

    def vertices(self) -> tuple[CoxeterVertex, ...]:
        return tuple(self)

    def index_set(self) -> tuple[Hashable, ...]:
        return self._index_set

    def coxeter_matrix(self) -> CoxeterMatrix:
        return self._coxeter_matrix

    def graph(self) -> Graph:
        return self._coxeter_matrix.coxeter_graph()

    def source_lattice(self) -> Any:
        r"""Return the lattice whose elements label the diagram vertices."""
        assert self._source_lattice is not None, "this Coxeter diagram has no stored source lattice"
        return self._source_lattice

    def roots(self) -> tuple[Any, ...]:
        r"""Return the root element attached to each vertex."""
        assert self._roots is not None, "this Coxeter diagram has no stored roots"
        return self._roots

    def root(self, vertex: Hashable) -> Any:
        r"""Return the root element attached to ``vertex``."""
        vertex = self._element_constructor_(vertex).value
        return self.roots()[self._index_set.index(vertex)]

    def root_intersection_matrix(self) -> Any:
        r"""Return the matrix ``(r_i . r_j)`` for the stored roots."""
        assert self._root_intersection_matrix is not None, "this Coxeter diagram has no stored root intersection matrix"
        return matrix(ZZ, self._root_intersection_matrix)

    def root_intersection_graph(self) -> Graph:
        r"""Return the root graph, with loop labels recording root squares."""
        intersections = self.root_intersection_matrix()
        graph = Graph(loops=True)
        graph_add = cast(Any, graph)
        graph_add.add_vertices(self._index_set)
        for i, left in enumerate(self._index_set):
            graph.add_edge(left, left, intersections[i, i])
            for j in range(i + 1, len(self._index_set)):
                pairing = intersections[i, j]
                if pairing != 0:
                    graph.add_edge(left, self._index_set[j], pairing)
        return graph

    def preferred_positions(self) -> dict[Hashable, tuple[Any, Any]]:
        r"""Return stored positions, or compute a graph layout if none are stored."""
        if self._preferred_positions is not None:
            return dict(self._preferred_positions)
        if self._computed_positions is None:
            layout = cast(Any, self.graph()).layout()
            self._computed_positions = {vertex: (coordinates[0], coordinates[1]) for vertex, coordinates in layout.items()}
        return dict(self._computed_positions)

    def subdiagram(self, vertices: Iterable[Hashable]) -> FiniteCoxeterDiagram:
        selected = tuple(self._element_constructor_(vertex).value for vertex in vertices)
        assert len(selected) == len(set(selected)), f"an induced subdiagram requires distinct vertices; vertices={selected!r}"
        entries = [[self._coxeter_matrix[left, right] for right in selected] for left in selected]
        names = tuple(self.variable_names()[self._index_set.index(vertex)] for vertex in selected)
        roots = None if self._roots is None else tuple(self._roots[self._index_set.index(vertex)] for vertex in selected)
        positions = None if self._preferred_positions is None else {vertex: self._preferred_positions[vertex] for vertex in selected}
        intersections = None
        if self._root_intersection_matrix is not None:
            indices = tuple(self._index_set.index(vertex) for vertex in selected)
            intersections = tuple(tuple(self._root_intersection_matrix[i][j] for j in indices) for i in indices)
        return FiniteCoxeterDiagram(
            CoxeterMatrix(entries, index_set=selected),
            names=names,
            source_lattice=self._source_lattice,
            roots=roots,
            positions=positions,
            root_intersection_matrix=intersections,
        )

    def plot(self, **options: object) -> object:
        plot_options = {
            "edge_labels": True,
            "vertex_labels": dict(zip(self._index_set, self.variable_names(), strict=True)),
            "vertex_size": 200,
            **options,
        }
        return self.graph().plot(**plot_options)

    def tikz(self, positions: Mapping[Hashable, Sequence[object]] | None = None, scale: object = 1) -> str:
        r"""Return TikZ code for the diagram, omitting root-square loops."""
        selected_positions = _normalize_positions(self._index_set, positions) if positions is not None else self.preferred_positions()
        assert selected_positions is not None
        intersections = self.root_intersection_matrix()
        lines = [
            rf"\begin{{tikzpicture}}[scale={scale}]",
            r"\tikzset{coxeter node/.style={circle,draw,minimum size=6mm,inner sep=0pt}}",
            r"\tikzset{coxeter double/.style={double,double distance=1.4pt}}",
            r"\tikzset{coxeter triple/.style={double,double distance=2.6pt,postaction={draw}}}",
        ]
        for i, left in enumerate(self._index_set):
            for j in range(i + 1, len(self._index_set)):
                pairing = intersections[i, j]
                if pairing == 0:
                    continue
                right = self._index_set[j]
                lines.append(
                    rf"\draw[{_tikz_edge_style(intersections[i, i], intersections[j, j], pairing)}] "
                    rf"({_tikz_node_name(left)}) -- ({_tikz_node_name(right)});"
                )
        for i, vertex in enumerate(self._index_set):
            x, y = selected_positions[vertex]
            norm = intersections[i, i]
            fill = "black" if norm == -2 else "white"
            text = "white" if norm == -2 else "black"
            label = self.variable_names()[i]
            lines.append(
                rf"\node[coxeter node,fill={fill},text={text}] "
                rf"({_tikz_node_name(vertex)}) at ({x},{y}) {{$ {label} $}};"
            )
        lines.append(r"\end{tikzpicture}")
        return "\n".join(lines)

    def _matrix_entries(self) -> tuple[tuple[object, ...], ...]:
        return tuple(tuple(self._coxeter_matrix[left, right] for right in self._index_set) for left in self._index_set)


def _normalize_positions(
    index_set: Sequence[Hashable],
    positions: Mapping[Hashable, Sequence[object]] | None,
) -> dict[Hashable, tuple[object, object]] | None:
    if positions is None:
        return None
    assert set(positions) == set(index_set), f"positions need one coordinate pair for every vertex; index_set={tuple(index_set)!r}, positions={tuple(positions)!r}"
    normalized = {}
    for vertex, coordinates in positions.items():
        assert len(coordinates) == 2, f"a diagram position must be a coordinate pair; vertex={vertex!r}, coordinates={coordinates!r}"
        normalized[vertex] = (coordinates[0], coordinates[1])
    return normalized


def _coxeter_exponent(left_norm: object, right_norm: object, pairing: object) -> Integer:
    if pairing == 0:
        return ZZ(2)
    product = QQ(4) * QQ(pairing) ** 2 / (QQ(left_norm) * QQ(right_norm))
    exponent_by_product = {QQ(1): ZZ(3), QQ(2): ZZ(4), QQ(3): ZZ(6)}
    assert product in exponent_by_product, f"unsupported rank-two root angle; left_norm={left_norm}, right_norm={right_norm}, pairing={pairing}, product={product}"
    return exponent_by_product[product]


def _tikz_edge_style(left_norm: object, right_norm: object, pairing: object) -> str:
    exponent = _coxeter_exponent(left_norm, right_norm, pairing)
    if exponent == 3:
        return "-"
    if exponent == 4:
        return "coxeter double"
    if exponent == 6:
        return "coxeter triple"
    assert False, f"TikZ export only renders finite nontrivial Coxeter edges; exponent={exponent}"


def _tikz_node_name(vertex: Hashable) -> str:
    return "v" + "".join(character if character.isalnum() else "_" for character in str(vertex))


class CoxeterDiagramHomset(Homset):
    r"""Coxeter-matrix-preserving maps between two finite diagrams."""

    Element: ClassVar[type[CoxeterDiagramMorphism]]

    def __init__(
        self,
        domain: FiniteCoxeterDiagram,
        codomain: FiniteCoxeterDiagram,
        category: Category | None = None,
    ) -> None:
        hom_category = CoxeterDiagrams() if category is None else category
        assert hom_category.is_subcategory(CoxeterDiagrams()), f"a Coxeter-diagram homset category must refine CoxeterDiagrams; category={hom_category}"
        Homset.__init__(self, domain, codomain, category=hom_category)

    def _element_constructor_(
        self,
        images: Mapping[Hashable, Hashable] | Sequence[Hashable],
    ) -> CoxeterDiagramMorphism:
        return CoxeterDiagramMorphism(self, images)


class CoxeterDiagramMorphism(Morphism):
    r"""A map of vertices preserving every Coxeter exponent."""

    if TYPE_CHECKING:

        def parent(self) -> CoxeterDiagramHomset: ...

    def __init__(
        self,
        parent: CoxeterDiagramHomset,
        images: Mapping[Hashable, Hashable] | Sequence[Hashable],
    ) -> None:
        Morphism.__init__(self, parent)
        domain = cast(FiniteCoxeterDiagram, parent.domain())
        codomain = cast(FiniteCoxeterDiagram, parent.codomain())
        if isinstance(images, Mapping):
            image_map = dict(images)
            assert set(image_map) == set(domain.index_set()), (
                f"a diagram morphism needs one image for every vertex; domain={domain.index_set()!r}, supplied={tuple(image_map)!r}"
            )
        else:
            assert len(images) == domain.cardinality(), f"a diagram morphism needs one image for every vertex; expected={domain.cardinality()}, found={len(images)}"
            image_map = dict(zip(domain.index_set(), images, strict=True))
        assert all(image in codomain.index_set() for image in image_map.values()), (
            f"every image must be a vertex of the codomain; images={tuple(image_map.values())!r}, codomain={codomain.index_set()!r}"
        )
        source_matrix = domain.coxeter_matrix()
        target_matrix = codomain.coxeter_matrix()
        assert all(source_matrix[left, right] == target_matrix[image_map[left], image_map[right]] for left in domain.index_set() for right in domain.index_set()), (
            "a Coxeter-diagram morphism must preserve every Coxeter exponent"
        )
        self._images = image_map

    def _call_(self, vertex: CoxeterVertex) -> CoxeterVertex:
        domain = cast(FiniteCoxeterDiagram, self.domain())
        codomain = cast(FiniteCoxeterDiagram, self.codomain())
        vertex = domain(vertex)
        return codomain(self._images[vertex.value])

    def __call__(self, vertex: CoxeterVertex) -> CoxeterVertex:
        return self._call_(vertex)

    def images(self) -> tuple[CoxeterVertex, ...]:
        domain = cast(FiniteCoxeterDiagram, self.domain())
        return tuple(self(domain.vertex(i)) for i in range(domain.cardinality()))

    def __mul__(self, other: object) -> CoxeterDiagramMorphism:
        assert isinstance(other, CoxeterDiagramMorphism), f"morphism composition needs a CoxeterDiagramMorphism; found={type(other)}"
        assert other.codomain() == self.domain(), "morphisms compose only when the inner codomain equals the outer domain"
        domain = cast(FiniteCoxeterDiagram, other.domain())
        codomain = cast(FiniteCoxeterDiagram, self.codomain())
        return domain.hom(
            [self(other(domain.vertex(i))).value for i in range(domain.cardinality())],
            codomain=codomain,
        )


CoxeterDiagramHomset.Element = CoxeterDiagramMorphism

__all__ = [
    "CoxeterDiagramHomset",
    "CoxeterDiagramMorphism",
    "CoxeterDiagrams",
    "CoxeterVertex",
    "FiniteCoxeterDiagram",
]
