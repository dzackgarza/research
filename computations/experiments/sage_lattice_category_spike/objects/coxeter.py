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
from typing import TYPE_CHECKING, ClassVar, cast

from sage.categories.category import Category
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.structure.category_object import normalize_names
from sage.structure.element_wrapper import ElementWrapper
from sage.structure.parent import Parent

from ..lexicon import CartanType, CoxeterDiagram, CoxeterMatrix, Graph
from .categories import _own_methods
from .functors import CatObject


class CoxeterDiagrams(CatObject, Category):
    r"""Finite Coxeter diagrams and Coxeter-matrix-preserving maps."""

    def _repr_object_names(self) -> str:
        return "finite Coxeter diagrams"

    def super_categories(self) -> list[Category]:
        return [FiniteEnumeratedSets()]

    ParentMethods = _own_methods(CoxeterDiagram)

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
    ) -> None:
        self._coxeter_matrix = CoxeterMatrix(coxeter_matrix)
        self._index_set = tuple(self._coxeter_matrix.index_set())
        rank = len(self._index_set)
        if names is None:
            names = tuple(f"s_{i}" for i in self._index_set)
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
        )

    def __hash__(self) -> int:
        return hash((self._index_set, self._matrix_entries(), self.variable_names()))

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

    def subdiagram(self, vertices: Iterable[Hashable]) -> FiniteCoxeterDiagram:
        selected = tuple(self._element_constructor_(vertex).value for vertex in vertices)
        assert len(selected) == len(set(selected)), f"an induced subdiagram requires distinct vertices; vertices={selected!r}"
        entries = [[self._coxeter_matrix[left, right] for right in selected] for left in selected]
        names = tuple(self.variable_names()[self._index_set.index(vertex)] for vertex in selected)
        return FiniteCoxeterDiagram(
            CoxeterMatrix(entries, index_set=selected),
            names=names,
        )

    def plot(self, **options: object) -> object:
        plot_options = {
            "edge_labels": True,
            "vertex_labels": dict(zip(self._index_set, self.variable_names(), strict=True)),
            "vertex_size": 200,
            **options,
        }
        return self.graph().plot(**plot_options)

    def _matrix_entries(self) -> tuple[tuple[object, ...], ...]:
        return tuple(tuple(self._coxeter_matrix[left, right] for right in self._index_set) for left in self._index_set)


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
