r"""Coxeter diagrams as Sage parents.

EXAMPLES::

    sage: diagram = CoxeterDiagrams().from_cartan_type(["A", 3])
    sage: diagram.category().is_subcategory(CoxeterDiagrams().Finite())
    True
    sage: diagram.coxeter_matrix()
    [1 3 2]
    [3 1 3]
    [2 3 1]
"""

from collections.abc import Hashable, Iterable, Iterator, Mapping, Sequence
from typing import TYPE_CHECKING, Any, ClassVar, cast

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.matrix.constructor import matrix
from sage.rings.infinity import infinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
from sage.graphs.graph import Graph
from sage.structure.category_object import normalize_names
from sage.structure.element_wrapper import ElementWrapper
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.sets import Sets

COXETER_NEGATIVE_FOUR_NODE_COLOR = "#F8F9FE"
COXETER_NEGATIVE_TWO_NODE_COLOR = "#BFC9CA"
COXETER_NODE_COLORS = {
    -4: COXETER_NEGATIVE_FOUR_NODE_COLOR,
    -2: COXETER_NEGATIVE_TWO_NODE_COLOR,
}
COXETER_DRAWING_CONVENTIONS = (
    ("square -4 root", f"white node, fill {COXETER_NEGATIVE_FOUR_NODE_COLOR}"),
    ("square -2 root", f"black node, fill {COXETER_NEGATIVE_TWO_NODE_COLOR}"),
    ("root squares", "stored as self-loops in root_intersection_graph(), omitted from TikZ"),
    ("single edge", "Coxeter exponent 3"),
    ("double edge", "Coxeter exponent 4"),
    ("triple edge", "Coxeter exponent 6"),
    ("thick edge", "Coxeter bond ∞, parallel mirrors: b(v,w)² = v²w²"),
    ("dashed edge", "Coxeter bond ∞, divergent mirrors: b(v,w)² > v²w²"),
)


class CoxeterDiagrams(Category):
    r"""Finite Coxeter diagrams and Coxeter-matrix-preserving maps.

    Rooted diagrams use the drawing convention documented on
    :class:`FiniteCoxeterDiagram`: square ``-4`` roots are white nodes, square
    ``-2`` roots are black nodes, root squares are stored as self-loops in the
    root-intersection graph, and the TikZ renderer omits those self-loops.
    """

    def _repr_object_names(self) -> str:
        return "finite Coxeter diagrams"

    def super_categories(self) -> list[Category]:
        return [Sets().Finite()]

    @staticmethod
    def minimal_edge_lattices() -> dict[str, Any]:
        r"""Return minimal rank-two realizations of the Coxeter edges that occur.

        The diagrams here come from fundamental domains of (usually hyperbolic)
        reflection groups, so every vertex is the mirror of a root and the
        roots have norm $-2$ or $-4$.  That pins the edge: with
        $t=b(r_1,r_2)^2/q(r_1)q(r_2)=\cos^2(\pi/m)$, and pairings against a
        norm $-4$ root even because its divisibility is, the whole list is

        =============  =========  =====  =========================
        $q_1,q_2$      $b$        $t$    edge
        =============  =========  =====  =========================
        $-2,-2$        $0$        $0$    none, $m=2$
        $-2,-2$        $1$        $1/4$  single, $m=3$
        $-2,-4$        $2$        $1/2$  double, $m=4$
        $-2,-2$        $2$        $1$    parallel, $m=\infty$
        $-2,-2$        $\geq 3$   $>1$   ultraparallel
        =============  =========  =====  =========================

        **There is no triple edge.**  $m=6$ needs $t=3/4$, so $4b^2=3q_1q_2$;
        with $q_1q_2\in\{4,8,16\}$ that asks for $b^2\in\{3,6,12\}$ and none is
        a square.  In general $m=6$ forces the two norms to differ by a factor
        of three up to squares -- smallest even case $\langle-2,-6\rangle$ with
        $b=3$, which is $G_2$ -- and a norm $-6$ root needs divisibility $3$ or
        $6$, which $-2$ and $-4$ roots do not produce.  So the crystallographic
        restriction tightens from $m\in\{2,3,4,6\}$ to $m\in\{2,3,4\}$ here;
        $m=5$ is out separately, $\cos^2(\pi/5)$ being irrational.

        ``parallel`` is degenerate and has to be: $t=1$ is the parabolic
        boundary, where the mirrors meet at infinity.  That is a fact about
        its form -- it has a radical -- and not about what kind of object it
        is.  ``ultraparallel`` is indefinite but nondegenerate: the mirrors
        diverge.
        """
        return {
            "orthogonal": _integral_lattice_with_names(
                matrix(ZZ, 2, [-2, 0, 0, -2]),
                names=("r1", "r2"),
            ),
            "single": _integral_lattice_with_names(
                matrix(ZZ, 2, [-2, 1, 1, -2]),
                names=("r1", "r2"),
            ),
            "double": _integral_lattice_with_names(
                matrix(ZZ, 2, [-2, 2, 2, -4]),
                names=("r1", "r2"),
            ),
            "parallel": _integral_lattice_with_names(
                matrix(ZZ, 2, [-2, 2, 2, -2]),
                names=("r1", "r2"),
            ),
            "ultraparallel": _integral_lattice_with_names(
                matrix(ZZ, 2, [-2, 3, 3, -2]),
                names=("r1", "r2"),
            ),
        }

    def from_coxeter_matrix(
        self,
        coxeter_matrix: CoxeterMatrix,
        names: Sequence[str] | str | None = None,
    ) -> FiniteCoxeterDiagram:
        r"""Construct a diagram from its Coxeter matrix."""
        return FiniteCoxeterDiagram(coxeter_matrix, names=names)

    def from_cartan_type(
        self,
        cartan_type: Any,
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


class FiniteCoxeterDiagram(CoxeterDiagramParent):
    r"""A finite Coxeter diagram whose elements are its vertices.

    A diagram may be rooted: its vertices carry actual roots in a source
    lattice, a full root-intersection matrix, and preferred plotting
    coordinates.  The rooted drawing convention is part of the object API:

    * square ``-4`` roots are white nodes, with fill
      ``COXETER_NEGATIVE_FOUR_NODE_COLOR`` = ``#F8F9FE``;
    * square ``-2`` roots are black nodes, with fill
      ``COXETER_NEGATIVE_TWO_NODE_COLOR`` = ``#BFC9CA``;
    * diagonal terms ``r_i^2`` are stored as self-loops by
      :meth:`root_intersection_graph`;
    * TikZ output omits self-loops and renders edges from the Coxeter
      exponents: single for ``3``, double for ``4``, triple for ``6``.

    Use :meth:`drawing_conventions`, :meth:`node_color`, :meth:`roots`,
    :meth:`root_intersection_matrix`, and :meth:`preferred_positions` to extract
    the packaged data from a diagram object.
    """

    Element = CoxeterVertex
    negative_four_node_color = COXETER_NEGATIVE_FOUR_NODE_COLOR
    negative_two_node_color = COXETER_NEGATIVE_TWO_NODE_COLOR

    if TYPE_CHECKING:
        element_class: ClassVar[type[CoxeterVertex]]

    def __init__(
        self,
        coxeter_matrix: CoxeterMatrix,
        names: Sequence[str] | str | None = None,
        root_morphism: FormMorphism | None = None,
        positions: Mapping[Hashable, Sequence[object]] | None = None,
    ) -> None:
        self._coxeter_matrix = CoxeterMatrix(coxeter_matrix)
        self._index_set = finite_ordered_set(
            tuple(self._coxeter_matrix.index_set())
        )
        rank = len(self._index_set)
        if names is None:
            names = tuple(f"s_{i}" for i in self._index_set)
        if root_morphism is not None:
            assert root_morphism.domain().rank() == rank, (
                "a rooted Coxeter diagram needs one root for every vertex"
            )
        self._root_morphism = root_morphism
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
        cartan_type: Any,
        names: Sequence[str] | str | None = None,
    ) -> FiniteCoxeterDiagram:
        r"""Construct the diagram of a crystallographic Cartan type."""
        return cls(CoxeterMatrix(cartan_type), names=names)

    @classmethod
    def from_roots(
        cls,
        roots: Sequence[Any],
        names: Sequence[str] | str | None = None,
        positions: Mapping[Hashable, Sequence[object]] | None = None,
        index_set: Sequence[Hashable] | None = None,
    ) -> FiniteCoxeterDiagram:
        r"""Construct the diagram and root subobject determined by ``roots``."""
        roots = tuple(roots)
        assert roots, "a rooted Coxeter diagram needs at least one root"
        rank = len(roots)
        realization = roots[0].parent()
        assert all(root.parent() is realization for root in roots), (
            "all diagram roots must belong to the same lattice"
        )
        match index_set:
            case None:
                index_set = Sets.Δ[rank - 1]
            case Sequence():
                index_set = finite_ordered_set(index_set)
            case Parent():
                index_set = finite_ordered_set(index_set)
            case _:
                raise TypeError(
                    "a Coxeter index set is a finite set or finite sequence"
                )
        assert index_set.cardinality() == rank, f"index set must have one entry per root; index_set={index_set!r}, roots={rank}"
        if names is None:
            names = tuple(f"s_{i}" for i in index_set)
        normalized_names = normalize_names(rank, names)
        gram = realization.gram_of(roots)
        entries = [[1 if i == j else _coxeter_exponent(gram[i, i], gram[j, j], gram[i, j]) for j in range(rank)] for i in range(rank)]
        # Coxeter bonds m=∞ (parallel or divergent mirrors) make the root span
        # degenerate.  That is a fact about the form, not about what kind of
        # object this is: a lattice here is a free module with a Z-valued
        # form, and nothing in that asks the form to be nondegenerate.
        root_module = _integral_lattice_with_names(
            gram,
            names=normalized_names,
            generating_set=finite_ordered_set(roots),
        )
        homset = root_module.Hom(realization)
        root_morphism = homset({root: root for root in roots})
        return cls(
            CoxeterMatrix(entries, index_set=index_set),
            names=normalized_names,
            root_morphism=root_morphism,
            positions=positions,
        )

    def _Hom_(
        self,
        codomain: FiniteCoxeterDiagram,
        category: Category | None = None,
    ) -> CoxeterDiagramHomset:
        hom_category = CoxeterDiagrams() if category is None else category
        cache = self.__dict__.setdefault("_coxeter_homsets", {})
        key = (codomain, hom_category)
        homset = cache.get(key)
        if homset is None:
            homset = CoxeterDiagramHomset(
                self,
                codomain,
                category=hom_category,
            )
            cache[key] = homset
        return homset

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
            and self._root_morphism == other._root_morphism
            and self._preferred_positions == other._preferred_positions
        )

    def __hash__(self) -> int:
        return hash(
            (
                self._index_set,
                self._matrix_entries(),
                self.variable_names(),
                self._root_morphism,
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
        return len(self._index_set)

    def vertex(self, index: int) -> CoxeterVertex:
        return self(self._index_set[index])

    def vertices(self) -> tuple[CoxeterVertex, ...]:
        return tuple(self)

    def index_set(self) -> Any:
        return self._index_set

    def coxeter_matrix(self) -> CoxeterMatrix:
        return self._coxeter_matrix

    def graph(self) -> Graph:
        return self._coxeter_matrix.coxeter_graph()

    def Aut(self) -> Any:
        r"""Return the finite group of Coxeter-diagram automorphisms."""
        return refine(
            self.graph().automorphism_group(edge_labels=True),
            OwnedFiniteGroups(),
        )

    def drawing_conventions(self) -> dict[str, str]:
        r"""Return the node, edge, and self-loop drawing conventions.

        The conventions are attached to the Coxeter diagram object rather than
        to the Sterk fixture data.  In particular, a rooted Sterk object
        contains its root squares, its preferred positions, and the colors used
        by :meth:`tikz`.
        """
        return dict(COXETER_DRAWING_CONVENTIONS)

    def root_morphism(self) -> FormMorphism:
        r"""Return the morphism sending the formal root generators to roots."""
        assert self._root_morphism is not None, (
            "this Coxeter diagram is not realized by roots"
        )
        return self._root_morphism

    def root_lattice(self) -> Any:
        r"""Return the abstract lattice generated by the diagram roots."""
        return self.root_morphism().domain()

    def root_realization(self) -> Any:
        r"""Return the lattice in which the diagram roots are realized."""
        return self.root_morphism().codomain()

    def roots(self) -> Any:
        r"""Return the roots realizing the diagram vertices."""
        morphism = self.root_morphism()
        return finite_ordered_set(
            tuple(
                morphism(morphism.domain().generator(label))
                for label in morphism.domain().generating_set()
            )
        )

    def root(self, vertex: Hashable) -> Any:
        r"""Return the root element attached to ``vertex``."""
        vertex = self._element_constructor_(vertex).value
        return self.roots()[self._index_set.index(vertex)]

    def root_intersection_matrix(self) -> Any:
        r"""Return the Gram matrix of the abstract root lattice."""
        return self.root_lattice().gram_matrix()

    def root_intersection_graph(self) -> Graph:
        r"""Return the root graph, with loop labels recording root squares.

        The loops are data: a loop label is the diagonal term ``r_i^2``.  They
        are not rendered by :meth:`tikz`, which draws only Coxeter edges between
        distinct vertices.
        """
        intersections = self.root_intersection_matrix()
        graph = Graph(loops=True)
        graph_add = cast(Any, graph)
        graph_add.add_vertices(self._index_set)
        graph_add.add_edges(
            [
                (
                    left,
                    left,
                    intersections[i, i],
                )
                for i, left in enumerate(self._index_set)
            ]
            + [
                (
                    left,
                    self._index_set[j],
                    intersections[i, j],
                )
                for i, left in enumerate(self._index_set)
                for j in range(i + 1, len(self._index_set))
                if intersections[i, j] != 0
            ]
        )
        return graph

    def preferred_positions(self) -> dict[Hashable, tuple[Any, Any]]:
        r"""Return stored positions, or compute a graph layout if none are stored."""
        if self._preferred_positions is not None:
            return dict(self._preferred_positions)
        if self._computed_positions is None:
            layout = cast(Any, self.graph()).layout()
            self._computed_positions = {vertex: (coordinates[0], coordinates[1]) for vertex, coordinates in layout.items()}
        return dict(self._computed_positions)

    def node_color(self, vertex: Hashable) -> str:
        r"""Return the TikZ fill color for ``vertex`` from its root square.

        Square ``-4`` roots use ``#F8F9FE``; square ``-2`` roots use
        ``#BFC9CA``.  The color is extractable from the object because it is a
        convention of rooted Coxeter diagrams, not a Sterk fixture.
        """
        vertex = self._element_constructor_(vertex).value
        index = self._index_set.index(vertex)
        norm = self.root_intersection_matrix()[index, index]
        assert norm in COXETER_NODE_COLORS, f"no Coxeter node color is defined for square {norm}"
        return COXETER_NODE_COLORS[norm]

    def subdiagram(self, vertices: Iterable[Hashable]) -> FiniteCoxeterDiagram:
        selected = tuple(self._element_constructor_(vertex).value for vertex in vertices)
        assert len(selected) == len(set(selected)), f"an induced subdiagram requires distinct vertices; vertices={selected!r}"
        entries = [[self._coxeter_matrix[left, right] for right in selected] for left in selected]
        names = tuple(self.variable_names()[self._index_set.index(vertex)] for vertex in selected)
        positions = None if self._preferred_positions is None else {vertex: self._preferred_positions[vertex] for vertex in selected}
        if self._root_morphism is not None:
            roots = tuple(
                self.roots()[self._index_set.index(vertex)]
                for vertex in selected
            )
            return FiniteCoxeterDiagram.from_roots(
                roots,
                names=names,
                positions=positions,
                index_set=selected,
            )
        return FiniteCoxeterDiagram(
            CoxeterMatrix(entries, index_set=selected),
            names=names,
            positions=positions,
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
        r"""Return TikZ code for the rooted Coxeter diagram.

        Root squares determine node fills: square ``-4`` roots use
        ``#F8F9FE`` and square ``-2`` roots use ``#BFC9CA``.  The
        root-intersection graph stores those squares as self-loops, but TikZ
        deliberately omits the loops and draws only edges between distinct
        vertices: single, double, or triple according to Coxeter exponent
        ``3``, ``4``, or ``6``.
        """
        selected_positions = _normalize_positions(self._index_set, positions) if positions is not None else self.preferred_positions()
        assert selected_positions is not None
        intersections = self.root_intersection_matrix()
        header = [
            rf"\begin{{tikzpicture}}[scale={scale}]",
            r"\definecolor{coxeterNegativeFour}{HTML}{F8F9FE}",
            r"\definecolor{coxeterNegativeTwo}{HTML}{BFC9CA}",
            r"\tikzset{coxeter node/.style={circle,draw,minimum size=6mm,inner sep=0pt}}",
            r"\tikzset{coxeter double/.style={double,double distance=1.4pt}}",
            r"\tikzset{coxeter triple/.style={double,double distance=2.6pt,postaction={draw}}}",
            r"\tikzset{coxeter parallel/.style={line width=1.6pt}}",
            r"\tikzset{coxeter divergent/.style={dashed}}",
        ]

        def edge(i: int, left: Any, j: int) -> str:
            right = self._index_set[j]
            return (
                rf"\draw[{_tikz_edge_style(intersections[i, i], intersections[j, j], intersections[i, j])}] "
                rf"({_tikz_node_name(left)}) -- ({_tikz_node_name(right)});"
            )

        edge_lines = [
            edge(i, left, j)
            for i, left in enumerate(self._index_set)
            for j in range(i + 1, len(self._index_set))
            if intersections[i, j] != 0
        ]

        def node(i: int, vertex: Any) -> str:
            x, y = selected_positions[vertex]
            norm = intersections[i, i]
            fill = _tikz_node_color(norm)
            text = "white" if norm == -2 else "black"
            label = self.variable_names()[i]
            return (
                rf"\node[coxeter node,fill={fill},text={text}] "
                rf"({_tikz_node_name(vertex)}) at ({x},{y}) {{$ {label} $}};"
            )

        node_lines = [
            node(i, vertex)
            for i, vertex in enumerate(self._index_set)
        ]
        return "\n".join(
            [
                *header,
                *edge_lines,
                *node_lines,
                r"\end{tikzpicture}",
            ]
        )

    def _matrix_entries(self) -> tuple[tuple[object, ...], ...]:
        return tuple(tuple(self._coxeter_matrix[left, right] for right in self._index_set) for left in self._index_set)


def _normalize_positions(
    index_set: Sequence[Hashable],
    positions: Mapping[Hashable, Sequence[object]] | None,
) -> dict[Hashable, tuple[object, object]] | None:
    if positions is None:
        return None
    assert set(positions) == set(index_set), f"positions need one coordinate pair for every vertex; index_set={tuple(index_set)!r}, positions={tuple(positions)!r}"
    assert all(len(coordinates) == 2 for coordinates in positions.values()), (
        "every diagram position must be a coordinate pair"
    )
    return {
        vertex: (coordinates[0], coordinates[1])
        for vertex, coordinates in positions.items()
    }


def _coxeter_exponent(left_norm: object, right_norm: object, pairing: object) -> object:
    r"""Coxeter bond $m$ of a rank-two root pair.

    ``product`` is $(2\cos\theta)^2 = 4\,b(v,w)^2/(v^2 w^2)$: values $1,2,3$
    give $m=3,4,6$; $\geq 4$ means the mirrors do not meet in the interior —
    parallel ($=4$) or divergent ($>4$) — so the bond is $\infty$ (Vinberg,
    *Hyperbolic reflection groups*).
    """
    if pairing == 0:
        return 2
    product = 4 * pairing ** 2 / (left_norm * right_norm)
    if product >= 4:
        return infinity
    exponent_by_product = {1: 3, 2: 4, 3: 6}
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
    if exponent == infinity:
        # The Coxeter matrix collapses both to ∞; the drawing keeps Vinberg's
        # distinction: thick = parallel mirrors, dashed = divergent mirrors.
        product = 4 * pairing ** 2 / (left_norm * right_norm)
        return "coxeter parallel" if product == 4 else "coxeter divergent"
    assert False, f"TikZ export does not render Coxeter bond m={exponent}"


def _tikz_node_color(norm: object) -> str:
    norm = norm
    assert norm in COXETER_NODE_COLORS, f"no Coxeter node color is defined for square {norm}"
    if norm == -4:
        return "coxeterNegativeFour"
    return "coxeterNegativeTwo"


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

    def __contains__(self, morphism: Any) -> bool:
        return (
            isinstance(morphism, CoxeterDiagramMorphism)
            and morphism.parent() is self
        )


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
        match images:
            case Mapping():
                image_map = dict(images)
                assert set(image_map) == set(domain.index_set()), (
                    f"a diagram morphism needs one image for every vertex; domain={domain.index_set()!r}, supplied={tuple(image_map)!r}"
                )
            case Sequence():
                assert len(images) == domain.cardinality(), f"a diagram morphism needs one image for every vertex; expected={domain.cardinality()}, found={len(images)}"
                image_map = dict(zip(domain.index_set(), images, strict=True))
            case _:
                raise TypeError(
                    "a diagram morphism is specified by a vertex map or an "
                    "ordered sequence of images"
                )
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
        assert other.codomain() is self.domain(), "morphisms compose only when the inner codomain is the outer domain"
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
