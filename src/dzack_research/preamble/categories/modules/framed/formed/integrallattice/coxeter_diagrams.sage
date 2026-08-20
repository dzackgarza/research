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

from typing import TYPE_CHECKING
from dzack_research.preamble.lexicon import Element
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import GramMatrix
    from dzack_research.preamble.owned_category import ConstructionData
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from dzack_research.preamble.lexicon import ModuleElement

from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import _integral_lattice_with_names
from dzack_research.preamble.categories.sets.sets import finite_ordered_set
from sage.combinat.root_system.cartan_type import CartanType
if TYPE_CHECKING:
    from sage.groups.perm_gps.permgroup import PermutationGroup_generic
    from sage.groups.perm_gps.permgroup_element import PermutationGroupElement

from collections import Counter
from collections.abc import Hashable, Iterable, Iterator, Mapping, Sequence
from itertools import combinations
from typing import TYPE_CHECKING, cast

from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category, HomsetsCategory
from sage.categories.morphism import Morphism
from sage.combinat.posets.posets import Poset
from sage.misc.cachefunc import cached_method
from sage.matrix.constructor import matrix
from sage.rings.infinity import infinity, PlusInfinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.category_object import normalize_names
from sage.structure.element_wrapper import ElementWrapper
from sage.structure.parent import Parent

from dzack_research.preamble.lexicon import CoxeterMatrix, Graph
from dzack_research.preamble.categories.sets.owned_sets import Sets

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet
    from sage.graphs.graph import GraphOption
    from sage.plot.graphics import Graphics
    from sage.structure.element import RingElement
    from sage.structure.parent import ElementConstructorInput, MembershipInput


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
    ("single edge", "Coxeter matrix entry 3"),
    ("double edge", "Coxeter matrix entry 4"),
    ("triple edge", "Coxeter matrix entry 6"),
    ("thick edge", "Coxeter bond ∞, parallel mirrors: b(v,w)² = v²w²"),
    ("dashed edge", "Coxeter bond ∞, divergent mirrors: b(v,w)² > v²w²"),
)


class CoxeterDiagrams(Category):
    r"""Finite Coxeter diagrams and Coxeter-matrix-preserving maps.

    Rooted diagrams use the drawing convention documented on
    :class:`CoxeterDiagrams.ParentMethods`: square ``-4`` roots are white nodes, square
    ``-2`` roots are black nodes, root squares are stored as self-loops in the
    root-intersection graph, and the TikZ renderer omits those self-loops.
    """

    def _repr_object_names(self) -> str:
        return "finite Coxeter diagrams"

    def super_categories(self) -> list[Category]:
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.vinberg_invariants import ProjectiveWeightedGraphs
        return [ProjectiveWeightedGraphs().Symmetric()]

    @staticmethod
    def minimal_edge_lattices() -> dict[str, "FormModule"]:
        r"""Return minimal rank-two realizations of the Coxeter edges that occur.

        The diagrams here come from fundamental domains of (usually hyperbolic)
        reflection groups, so every vertex is the mirror of a root and the
        roots have square $-2$ or $-4$.  That pins the edge: with
        $t=b(r_1,r_2)^2/q(r_1)q(r_2)=\cos^2(\pi/m)$, and pairings against a
        square $-4$ root even because its divisibility is, the whole list is

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
        a square.  In general $m=6$ forces the two squares to differ by a factor
        of three up to squares -- smallest even case $\langle-2,-6\rangle$ with
        $b=3$, which is $G_2$ -- and a square $-6$ root needs divisibility $3$ or
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
                matrix(SageZZ, 2, [-2, 0, 0, -2]),
                names=("r1", "r2"),
            ),
            "single": _integral_lattice_with_names(
                matrix(SageZZ, 2, [-2, 1, 1, -2]),
                names=("r1", "r2"),
            ),
            "double": _integral_lattice_with_names(
                matrix(SageZZ, 2, [-2, 2, 2, -4]),
                names=("r1", "r2"),
            ),
            "parallel": _integral_lattice_with_names(
                matrix(SageZZ, 2, [-2, 2, 2, -2]),
                names=("r1", "r2"),
            ),
            "ultraparallel": _integral_lattice_with_names(
                matrix(SageZZ, 2, [-2, 3, 3, -2]),
                names=("r1", "r2"),
            ),
        }

    def from_coxeter_matrix(
        self,
        coxeter_matrix: CoxeterMatrix,
        names: Sequence[str] | str | None = None,
        root_morphism: Morphism | None = None,
        positions: Mapping[Hashable, Sequence["RingElement | float"]] | None = None,
    ) -> Parent:
        r"""Construct a diagram from its Coxeter matrix."""
        return object_of(
            self,
            coxeter_matrix=coxeter_matrix,
            names=names,
            root_morphism=root_morphism,
            positions=positions,
        )

    def from_cartan_type(
        self,
        cartan_type: "CartanType",
        names: Sequence[str] | str | None = None,
        scale: "Integer | int | None" = None,
    ) -> Parent:
        r"""Construct the diagram of a crystallographic Cartan type.

        Without ``scale`` the diagram is unrooted: it carries the type's
        Coxeter matrix and nothing else.  With ``scale`` it is the reference
        rooted realization of ``(type, scale)``: the roots are the simple
        roots of the type read with this project's sign convention, so the
        root Gram matrix is ``-scale`` times the symmetrized Cartan matrix,
        normalized -- as Sage's symmetrizer normalizes it -- so that the
        short roots have square `2`.  The Gram data is delegated to Sage's
        root-system machinery; there is no per-type matrix table, and these
        outputs *are* the identification catalogue that
        :meth:`scaled_cartan_type` verifies against.
        """
        if scale is None:
            return self.from_coxeter_matrix(CoxeterMatrix(cartan_type), names=names)
        scale = Integer(scale)
        assert scale >= 1, f"a lattice scale is a positive integer; scale={scale}"
        cartan = CartanType(cartan_type)
        gram = -scale * cartan.cartan_matrix().symmetrized_matrix()
        realization = _integral_lattice_with_names(gram)
        return self.from_roots(tuple(realization.module_generators()), names=names)

    def from_roots(
        self,
        roots: Sequence["ModuleElement"],
        names: Sequence[str] | str | None = None,
        positions: Mapping[Hashable, Sequence["RingElement | float"]] | None = None,
        index_set: "Sequence[Hashable] | OrderedSet | None" = None,
    ) -> Parent:
        r"""Construct the diagram and root subobject determined by ``roots``."""
        roots = tuple(roots)
        assert roots, "a rooted Coxeter diagram needs at least one root"
        rank = len(roots)
        realization = roots[0].parent()
        assert all(root.parent() is realization for root in roots), (
            "all diagram roots must belong to the same lattice"
        )
        vertex_index_set: "OrderedSet"
        match index_set:
            case None:
                vertex_index_set = Sets.Δ[rank - 1]
            case Sequence():
                vertex_index_set = finite_ordered_set(index_set)
            case Parent():
                vertex_index_set = finite_ordered_set(index_set)
            case _:
                assert False, (
                    "a Coxeter index set is a finite set or finite sequence"
                )
        assert vertex_index_set.cardinality() == rank, f"index set must have one entry per root; index_set={vertex_index_set!r}, roots={rank}"
        if names is None:
            names = tuple(f"s_{i}" for i in vertex_index_set)
        normalized_names = normalize_names(rank, names)
        gram = realization.gram_of(roots)
        entries = [[1 if i == j else _coxeter_matrix_entry(gram[i, i], gram[j, j], gram[i, j]) for j in range(rank)] for i in range(rank)]
        # Coxeter bonds m=∞ (parallel or divergent mirrors) make the root span
        # degenerate.  That is a fact about the form, not about what kind of
        # object this is: a lattice here is a free module with a Z-valued
        # form, and nothing in that asks the form to be nondegenerate.
        root_module = _integral_lattice_with_names(
            gram,
            names=normalized_names,
            module_generating_set=finite_ordered_set(roots),
        )
        homset = root_module.Hom(realization)
        root_morphism = homset({root: root for root in roots})
        return self.from_coxeter_matrix(
            CoxeterMatrix(entries, index_set=vertex_index_set),
            names=normalized_names,
            root_morphism=root_morphism,
            positions=positions,
        )


    class Homsets(HomsetsCategory):
        r"""The Coxeter-matrix-preserving maps between two diagrams.

        A morphism of diagrams is an element of one of these homsets.  The
        homset is the parent and the morphism is its element.
        """

        class ParentMethods:
            r"""Coxeter-matrix-preserving maps between two finite diagrams."""

            if TYPE_CHECKING:
                # This homset connects two diagrams, and its elements are the maps
                # between them.
                def domain(self) -> "Parent": ...
                def codomain(self) -> "Parent": ...
                def __call__(
                    self,
                    x: "ElementConstructorInput" = ...,
                    *args: "ElementConstructorInput",
                    **kwds: "ElementConstructorInput",
                ) -> "Morphism": ...

            def _element_constructor_(
                self,
                images: Mapping[Hashable, Hashable] | Sequence[Hashable],
            ) -> "Morphism":
                return self.element_class(self, images)

            def __contains__(self, morphism: "MembershipInput") -> bool:
                # ``in`` is asked of an arbitrary value.
                return (
                    isinstance(morphism, self.element_class)
                    and morphism.parent() is self
                )


        class ElementMethods:
            r"""A map of vertices preserving every Coxeter matrix entry."""

            if TYPE_CHECKING:

                def parent(self) -> Parent: ...

            def __init__(
                self,
                parent: Parent,
                images: Mapping[Hashable, Hashable] | Sequence[Hashable],
            ) -> None:
                super().__init__(parent)
                domain = parent.domain()
                codomain = parent.codomain()
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
                        assert False, (
                            "a diagram morphism is specified by a vertex map or an "
                            "ordered sequence of images"
                        )
                assert all(image in codomain.index_set() for image in image_map.values()), (
                    f"every image must be a vertex of the codomain; images={tuple(image_map.values())!r}, codomain={codomain.index_set()!r}"
                )
                source_matrix = domain.coxeter_matrix()
                target_matrix = codomain.coxeter_matrix()
                assert all(source_matrix[left, right] == target_matrix[image_map[left], image_map[right]] for left in domain.index_set() for right in domain.index_set()), (
                    "a Coxeter-diagram morphism must preserve every Coxeter matrix entry"
                )
                self._images = image_map

            def _call_(self, vertex: "ElementConstructorInput") -> Element:
                # Sage calls a morphism on an arbitrary value and lets the domain
                # convert; the parameter is unrestricted for that reason.
                domain = self.domain()
                codomain = self.codomain()
                converted = domain(vertex)
                image: Element = codomain(self._images[converted.value])
                return image

            def __call__(
                self,
                *args: "ElementConstructorInput",
                **kwds: "ElementConstructorInput",
            ) -> Element:
                return self._call_(*args, **kwds)

            def images(self) -> tuple[Element, ...]:
                domain = self.domain()
                return tuple(self(domain.vertex(i)) for i in range(domain.cardinality()))

            def __mul__(
                self,
                other: "ElementConstructorInput",
            ) -> Morphism:
                assert isinstance(other, CoxeterDiagrams.Homsets.ElementMethods), (
                    "morphism composition needs a diagram morphism; "
                    f"found={type(other)}"
                )
                assert other.codomain() is self.domain(), "morphisms compose only when the inner codomain is the outer domain"
                domain = other.domain()
                codomain = self.codomain()
                composite: Morphism = domain.hom(
                    [self(other(domain.vertex(i))).value for i in range(domain.cardinality())],
                    codomain=codomain,
                )
                return composite


    class ElementMethods(ElementWrapper):
        r"""A vertex of a finite Coxeter diagram."""

        if TYPE_CHECKING:
            # A vertex is built only by its diagram, so that diagram is the parent.
            def parent(self) -> "Parent": ...

        def _repr_(self) -> str:
            parent = self.parent()
            name: str = parent.variable_names()[parent.index_set().index(self.value)]
            return name


    class ParentMethods:
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
          matrix entries: single for ``3``, double for ``4``, triple for ``6``.

        Use :meth:`drawing_conventions`, :meth:`node_color`, :meth:`roots`,
        :meth:`root_intersection_matrix`, and :meth:`preferred_positions` to extract
        the packaged data from a diagram object.
        """

        negative_four_node_color = COXETER_NEGATIVE_FOUR_NODE_COLOR
        negative_two_node_color = COXETER_NEGATIVE_TWO_NODE_COLOR

        def __init__(
            self,
            coxeter_matrix: CoxeterMatrix,
            names: Sequence[str] | str | None = None,
            root_morphism: Morphism | None = None,
            positions: Mapping[Hashable, Sequence["RingElement | float"]] | None = None,
            **rest: "ConstructionData",
        ) -> None:
            self._coxeter_matrix = CoxeterMatrix(coxeter_matrix)
            self._index_set = finite_ordered_set(
                tuple(self._coxeter_matrix.index_set())
            )
            rank = self._index_set.cardinality()
            if names is None:
                names = tuple(f"s_{i}" for i in self._index_set)
            if root_morphism is not None:
                assert root_morphism.domain().rank() == rank, (
                    "a rooted Coxeter diagram needs one root for every vertex"
                )
            self._root_morphism = root_morphism
            self._preferred_positions = _normalize_positions(self._index_set, positions)
            self._computed_positions: dict[
                Hashable,
                tuple["RingElement | float", "RingElement | float"],
            ] | None = None
            super().__init__(
                cardinality=rank,
                names=normalize_names(rank, names),
                **rest,
            )

        @cached_method
        def _Hom_(
            self,
            codomain: Parent,
            category: Category | None = None,
        ) -> Parent:
            # The default spelling is cached onto the same homset as the
            # named one, so the two ways of asking give one object.
            if category is None:
                default_homset: Parent = self._Hom_(codomain, CoxeterDiagrams())
                return default_homset
            assert category.is_subcategory(CoxeterDiagrams()), (
                "a Coxeter-diagram homset category must refine "
                f"CoxeterDiagrams; category={category}"
            )
            diagram_homset: Parent = super()._Hom_(codomain, category)
            return diagram_homset

        def hom(
            self,
            images: Mapping[Hashable, Hashable] | Sequence[Hashable],
            codomain: Parent,
        ) -> Morphism:
            r"""Construct the Coxeter-matrix-preserving map with the given images."""
            return self._Hom_(codomain)(images)

        def _repr_(self) -> str:
            return f"Finite Coxeter diagram on {self.cardinality()} vertices"

        def __eq__(self, other: "MembershipInput") -> bool:
            return (
                other in CoxeterDiagrams()
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

        def __contains__(self, vertex: "MembershipInput") -> bool:
            if isinstance(vertex, self.element_class):
                return vertex.parent() is self
            return vertex in self._index_set

        def _element_constructor_(
            self,
            vertex: "ElementConstructorInput",
        ) -> Element:
            if isinstance(vertex, self.element_class):
                assert vertex.parent() is self, f"a vertex belongs to a different Coxeter diagram; vertex={vertex!r}"
                return vertex
            assert vertex in self._index_set, f"a vertex must lie in the index set; vertex={vertex!r}, index_set={self._index_set!r}"
            return self.element_class(self, vertex)

        def __iter__(self) -> Iterator[Element]:
            return (self(vertex) for vertex in self._index_set)

        def vertex(self, index: int) -> Element:
            return self(self._index_set[index])

        def vertices(self) -> tuple[Element, ...]:
            return tuple(self)

        def index_set(self) -> "OrderedSet":
            return self._index_set

        def coxeter_matrix(self) -> CoxeterMatrix:
            return self._coxeter_matrix

        def schlafli_matrix(self) -> "GramMatrix":
            r"""Return the Schläfli matrix $C_{ij} = -2\cos(\pi/m_{ij})$ over $AA$.

            The literature's form: the Gram matrix of the unit normals to the
            mirrors, with $C_{ii} = -2\cos\pi = 2$ and $C_{ij} = -2$ on a bond
            $m_{ij} = \infty$.  Under it, elliptic reads as positive definite and
            parabolic as positive semidefinite.

            **This repository's sign is the opposite one.**  The convention fixed
            by ``tests/coxeter_tdd_specs/literature/PROJECT_CONVENTIONS.md`` and
            realized by :meth:`root_intersection_matrix` is
            $B_{ij} = +2\cos(\pi/m_{ij})$, so $B = -C$: roots have square $-2$ and
            $-4$, elliptic is negative definite, and a single edge is
            $[[-2,1],[1,-2]]$.  The two differ by negating a subset of basis
            vectors on a tree diagram, and $\det B = (-1)^n \det C$, so
            determinant claims transfer unchanged in even rank only.  This method
            is where the literature's spelling is available; every other matrix on
            this class is in the repository's sign.

            Exact throughout: $2\cos(\pi/m) = \zeta + \zeta^{-1}$ for $\zeta$ a
            primitive $2m$-th root of unity, so no floating cosine is taken.
            """
            # Local: AA/QQbar are needed only here, and the module otherwise
            # stays inside ZZ and QQ.
            from sage.rings.qqbar import AA

            return matrix(
                AA,
                [
                    [_schlafli_entry(matrix_entry) for matrix_entry in row]
                    for row in self._matrix_entries()
                ],
            )

        def graph(self) -> Graph:
            return self._coxeter_matrix.coxeter_graph()

        def is_connected(self) -> bool:
            r"""Return whether the Coxeter graph of this diagram is connected.

            A thin delegation to :meth:`graph`.  Sage's convention that the empty
            graph is connected stands: the empty subdiagram is a legitimate member
            of the induced-subdiagram enumeration, and it is connected.
            """
            return bool(self.graph().is_connected())

        def connected_components(self) -> tuple[Parent, ...]:
            r"""Return the connected components as induced subdiagrams.

            Each component is the induced subdiagram on one connected component
            of :meth:`graph`, with its vertices in this diagram's index-set
            order, so rootedness is preserved where present.  The empty diagram
            has no components.
            """
            components = [
                set(component)
                for component in self.graph().connected_components(sort=False)
            ]
            return tuple(
                self.subdiagram(
                    [vertex for vertex in self._index_set if vertex in component]
                )
                for component in components
            )

        def is_elliptic(self) -> bool:
            r"""Return whether this diagram is elliptic (spherical).

            Coxeter's classification, asked of Sage exactly: a diagram is
            elliptic when its Coxeter group is finite, which is
            ``coxeter_matrix().is_finite()``.  The empty diagram is elliptic --
            its Coxeter group is trivial -- and is answered directly, because
            Sage's rank-zero Coxeter matrix carries no recognized Coxeter type
            and its stored ``is_finite`` flag reports ``False``.
            """
            if self._index_set.cardinality() == 0:
                return True
            return bool(self._coxeter_matrix.is_finite())

        def is_parabolic(self) -> bool:
            r"""Return whether this diagram is parabolic (euclidean).

            The standard definition: the diagram is nonempty and every connected
            component is affine, asked componentwise of Sage's classification
            through ``is_affine()`` on each component's Coxeter matrix.
            """
            components = self.connected_components()
            return bool(components) and all(
                component.coxeter_matrix().is_affine() for component in components
            )

        def coxeter_group(self) -> "Parent":
            r"""Return the Coxeter group $W$ of this diagram, in Sage's
            reflection representation.

            Delegated to Sage's ``CoxeterGroup`` on this diagram's own
            ``CoxeterMatrix``, which already carries $m=\infty$ natively (its
            internal encoding is $-1$; no caller re-encodes).  Infinite groups
            are ordinary outputs: the representation is by matrices, not by an
            enumeration.
            """
            from sage.combinat.root_system.coxeter_group import CoxeterGroup

            return CoxeterGroup(self._coxeter_matrix)

        def finitely_presented_coxeter_group(self) -> "Parent":
            r"""Return $\langle s_v \mid s_v^2,\ (s_v s_w)^{m_{vw}}
            \text{ for finite } m_{vw}\rangle$.

            The Coxeter presentation read off this diagram's Coxeter matrix: one
            generator per vertex, named by the vertex; an $m=\infty$ bond
            contributes no relation.  What comes back is a finitely presented
            group -- the chosen-presentation *data*, where
            :meth:`coxeter_group` is the represented group.
            """
            # Local: a module-level import here would close a cycle.
            from dzack_research.preamble.categories.group.groups import (
                coxeter_presentation,
            )

            free, relations = coxeter_presentation(
                self._coxeter_matrix, names=self.variable_names()
            )
            return free / list(relations)

        def Aut(self) -> "PermutationGroup_generic":
            r"""Return the finite group of Coxeter-diagram automorphisms.

            On a rooted diagram the group preserves the full root Gram data: it
            is the automorphism group of :meth:`root_intersection_graph` with its
            edge labels (root pairings) and loop labels (root squares).  The
            bond-only group -- automorphisms of :meth:`graph` -- is blind to root
            squares: it can send a square ``-2`` root to a square ``-4`` root
            across a symmetric bond pattern, fusing subdiagram orbits that the
            Gram data keeps apart.  An unrooted diagram has only its bonds and
            gets the bond-preserving group.
            """
            if self._root_morphism is None:
                return self.graph().automorphism_group(edge_labels=True)
            return self.root_intersection_graph().automorphism_group(edge_labels=True)

        def elliptic_subdiagram_orbits(
            self,
        ) -> dict[Parent, frozenset[Parent]]:
            r"""Return the :meth:`Aut`-orbits of the elliptic induced subdiagrams.

            The group acts on vertex sets, and the action is computed by GAP
            through ``PermutationGroup.orbit(..., action="OnSets")``.  Every
            elliptic induced subdiagram participates -- disconnected ones and the
            empty one included.  Ellipticity is decided once per orbit: a diagram
            automorphism preserves the Coxeter matrix, and on a rooted diagram
            the root Gram data, so it preserves ellipticity.

            Each orbit is returned as a set of subdiagrams, keyed by its
            representative: the subdiagram on the orbit's lexicographically least
            vertex tuple.
            """
            group = self.Aut()
            labels = tuple(self._index_set)
            orbits: dict[Parent, frozenset[Parent]] = {}
            # The empty subdiagram is elliptic and fixed by every automorphism,
            # so its orbit needs no group computation.
            empty = self.subdiagram(())
            orbits[empty] = frozenset((empty,))
            seen: set[frozenset[Hashable]] = set()
            for size in range(1, len(labels) + 1):
                for selection in combinations(labels, size):
                    if frozenset(selection) in seen:
                        continue
                    if not self.subdiagram(selection).is_elliptic():
                        continue
                    orbit_vertex_tuples = [
                        tuple(sorted(member))
                        for member in group.orbit(selection, action="OnSets")
                    ]
                    seen.update(frozenset(member) for member in orbit_vertex_tuples)
                    members = {
                        vertex_tuple: self.subdiagram(vertex_tuple)
                        for vertex_tuple in orbit_vertex_tuples
                    }
                    representative = members[min(orbit_vertex_tuples)]
                    orbits[representative] = frozenset(members.values())
            return orbits

        def parabolic_subdiagram_orbits(
            self,
        ) -> dict[Parent, frozenset[Parent]]:
            r"""Return the :meth:`Aut`-orbits of the parabolic induced subdiagrams.

            The sibling of :meth:`elliptic_subdiagram_orbits`, with parabolicity
            in place of ellipticity: a diagram automorphism preserves the Coxeter
            matrix, and on a rooted diagram the root Gram data, so it preserves
            parabolicity, and the property is decided once per orbit.  The empty
            subdiagram is not parabolic -- :meth:`is_parabolic` asks for a
            nonempty diagram with every component affine -- so no empty orbit
            appears.

            Each orbit is returned as a set of subdiagrams, keyed by its
            representative: the subdiagram on the orbit's lexicographically least
            vertex tuple.
            """
            group = self.Aut()
            labels = tuple(self._index_set)
            orbits: dict[Parent, frozenset[Parent]] = {}
            seen: set[frozenset[Hashable]] = set()
            for size in range(1, len(labels) + 1):
                for selection in combinations(labels, size):
                    if frozenset(selection) in seen:
                        continue
                    if not self.subdiagram(selection).is_parabolic():
                        continue
                    orbit_vertex_tuples = [
                        tuple(sorted(member))
                        for member in group.orbit(selection, action="OnSets")
                    ]
                    seen.update(frozenset(member) for member in orbit_vertex_tuples)
                    members = {
                        vertex_tuple: self.subdiagram(vertex_tuple)
                        for vertex_tuple in orbit_vertex_tuples
                    }
                    representative = members[min(orbit_vertex_tuples)]
                    orbits[representative] = frozenset(members.values())
            return orbits

        def subdiagram_orbit_poset(
            self,
            orbits: Mapping[Parent, frozenset[Parent]],
        ) -> Poset:
            r"""Return the inclusion order on subdiagram orbits, on representatives.

            Consumes what :meth:`elliptic_subdiagram_orbits` and
            :meth:`parabolic_subdiagram_orbits` return.  The order is the orbit
            order, not literal containment of the representatives:
            $[H]\le[K]$ when some member of $[H]$ is an induced subdiagram of
            some member of $[K]$.  Because :meth:`Aut` acts transitively on each
            orbit, that holds exactly when some member of $[H]$ has its vertices
            inside the representative of $[K]$, which is what is checked.  A
            partial order: reflexive because a representative is a member of its
            own orbit; antisymmetric because both containments force equal vertex
            counts, hence equal vertex sets; transitive because an automorphism
            carrying the containing member of $[K]$ onto its representative
            carries the contained member of $[H]$ along.
            """
            vertex_sets = {
                representative: tuple(
                    frozenset(member.index_set()) for member in members
                )
                for representative, members in orbits.items()
            }

            def orbit_below(
                below: Parent, above: Parent
            ) -> bool:
                target = frozenset(above.index_set())
                return any(
                    member_vertices <= target
                    for member_vertices in vertex_sets[below]
                )

            return Poset((tuple(orbits), orbit_below))

        def drawing_conventions(self) -> dict[str, str]:
            r"""Return the node, edge, and self-loop drawing conventions.

            The conventions are attached to the Coxeter diagram object rather than
            to the Sterk fixture data.  In particular, a rooted Sterk object
            contains its root squares, its preferred positions, and the colors used
            by :meth:`tikz`.
            """
            return dict(COXETER_DRAWING_CONVENTIONS)

        def root_morphism(self) -> Morphism:
            r"""Return the morphism sending the formal root generators to roots.

            Returned as an object of $\operatorname{Ar}(\text{lattices})$, because
            that is what it is: a Coxeter system realized in a lattice is the pair
            $(\Phi,\iota)$ with $\iota:\langle\Phi\rangle\to L$, and a morphism of
            such pairs is a commuting square -- a map of root systems below a map
            of lattices.  Refining here is what makes the square askable, by
            ``is_commuting_square`` on the arrow, rather than leaving $\iota$ a
            bare attribute and the pair unsayable.

            The realization is *not* asserted to be primitive.  A root sublattice
            need not be saturated in the lattice realizing it -- $A_1^{8}\subset
            E_8$ has index $2$ in its saturation -- so primitivity is a question
            to ask of this arrow (``Subobject(...).is_primitive()``), never a
            condition built into what a Coxeter system is.
            """
            assert self._root_morphism is not None, (
                "this Coxeter diagram is not realized by roots"
            )
            # Local: arrow_categories reaches the module node, so a module-level
            # import would close that cycle; by call time this module is built.
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import ArrowCategory
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
            from dzack_research.preamble.refine import refine

            return refine(self._root_morphism, ArrowCategory(IntegralLattices(SageZZ)))

        def root_lattice(self) -> "FormModule":
            r"""Return the abstract lattice generated by the diagram roots."""
            return self.root_morphism().domain()

        def root_realization(self) -> "FormModule":
            r"""Return the lattice in which the diagram roots are realized."""
            return self.root_morphism().codomain()

        def roots(self) -> "OrderedSet":
            r"""Return the roots realizing the diagram vertices."""
            morphism = self.root_morphism()
            return finite_ordered_set(
                tuple(
                    morphism(morphism.domain().module_generator(label))
                    for label in morphism.domain().module_generating_set()
                )
            )

        def root(self, vertex: Hashable) -> "ModuleElement":
            r"""Return the root element attached to ``vertex``."""
            vertex = self._element_constructor_(vertex).value
            return self.roots()[self._index_set.index(vertex)]

        def root_intersection_matrix(self) -> "GramMatrix":
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
            graph_add = graph
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
                    for j in range(i + 1, self._index_set.cardinality())
                    if intersections[i, j] != 0
                ]
            )
            return graph

        def scaled_cartan_type(self) -> "tuple[CartanType, Integer] | None":
            r"""Return the Cartan type and scale that this rooted diagram realizes.

            Defined on connected elliptic rooted diagrams.  The normalization:
            scale `1` means the root Gram matrix equals the *negated* symmetrized
            Cartan matrix of the type with short roots of square `2`; scale `2`
            means twice that, and so on.  The rank-two double-bond pair is
            returned as ``(C2, 1)`` -- `B_2` and `C_2` name one root system, and
            this method fixes the `C` spelling once, here.  The empty diagram
            returns ``None``, the distinguished empty value: it realizes no
            Cartan type, and no fake type is invented for it.

            Recognition reads the Coxeter type off Sage's classification and the
            scale and the `B`-versus-`C` decoration off the root squares: the
            shortest root square is `-2` times the scale, and on a bond-``4``
            chain `B_n` has exactly one short root where `C_n` has `n - 1`.  The
            recognized pair is then *verified*: the reference rooted diagram of
            ``(type, scale)`` is built by :meth:`from_cartan_type`, and the two
            root-intersection graphs must be isomorphic with their edge labels --
            loops carry root squares and edges carry pairings, so this is Gram
            equality up to relabeling.
            """
            if self._index_set.cardinality() == 0:
                return None
            assert self.is_connected(), (
                "a Cartan type names a connected diagram; ask "
                "component_scaled_cartan_types() for the components"
            )
            assert self.is_elliptic(), (
                "only an elliptic diagram realizes a finite root system"
            )
            intersections = self.root_intersection_matrix()
            rank = intersections.nrows()
            squares = [-intersections[i, i] for i in range(rank)]
            shortest = min(squares)
            scale = Integer(shortest) // 2
            assert 2 * scale == shortest, (
                f"the shortest root square must be -2 times the scale; squares={squares!r}"
            )
            coxeter_type = self._coxeter_matrix.coxeter_type()
            assert coxeter_type is not self._coxeter_matrix, (
                "Sage recognizes every finite Coxeter type, so an elliptic "
                f"diagram's type is never unknown; matrix={self._coxeter_matrix!r}"
            )
            cartan = coxeter_type.cartan_type()
            if cartan.type() == "B":
                short_count = sum(1 for square in squares if square == 2 * scale)
                if rank == 2:
                    # One root system, two names: the fixed spelling is C2.
                    cartan = CartanType(["C", 2])
                elif short_count == 1:
                    cartan = CartanType(["B", rank])
                else:
                    assert short_count == rank - 1, (
                        "a bond-4 chain has one short root (B) or one long root "
                        f"(C); squares={squares!r}"
                    )
                    cartan = CartanType(["C", rank])
            reference = CoxeterDiagrams().from_cartan_type(cartan, scale=scale)
            assert self.root_intersection_graph().is_isomorphic(
                reference.root_intersection_graph(), edge_labels=True
            ), (
                f"recognition promised {cartan} at scale {scale}, but the root "
                "Gram data is not that reference's up to relabeling"
            )
            return (cartan, scale)

        def component_scaled_cartan_types(self) -> "Counter[tuple[CartanType, Integer]]":
            r"""Return the multiset of ``(Cartan type, scale)`` over the components.

            Each connected component of an elliptic rooted diagram realizes one
            scaled Cartan type; the multiset collects them with multiplicity.
            The empty diagram has no components and returns the empty multiset.
            """
            return Counter(
                component.scaled_cartan_type()
                for component in self.connected_components()
            )

        def preferred_positions(
            self,
        ) -> dict[Hashable, tuple["RingElement | float", "RingElement | float"]]:
            r"""Return stored positions, or compute a graph layout if none are stored."""
            if self._preferred_positions is not None:
                return dict(self._preferred_positions)
            if self._computed_positions is None:
                layout = self.graph().layout()
                self._computed_positions = {vertex: (coordinates[0], coordinates[1]) for vertex, coordinates in layout.items()}
            return dict(self._computed_positions)

        def equivariant_positions(
            self,
            automorphism: "PermutationGroupElement",
        ) -> dict[Hashable, tuple["RingElement", "RingElement"]]:
            r"""Return exact vertex positions intertwining ``automorphism`` with
            a plane isometry, so the drawing carries the diagram's symmetry.

            For $\sigma$ of order $2$ the intertwined isometry is complex
            conjugation: the two vertices of each $2$-orbit sit at $z$ and
            $\bar z$, and each fixed vertex sits on the real axis.  Such a
            layout always exists.

            For $\sigma$ of order $n\ge3$ it is the rotation
            $z\mapsto\zeta_n z$: the $k$-th member of each orbit sits at
            $\zeta_n^k$ times its representative, one circle per orbit.  Here
            existence is constrained: an orbit of length $d<n$ forces
            $\zeta_n^d z=z$, so $z=0$ -- hence every orbit must be free except
            for at most one fixed vertex, at the origin, and that is asserted.

            Coordinates are exact real algebraic numbers (``AA``), computed in
            the cyclotomic field the way the source notebook's exact $n$-gon
            did; the intertwining $f(\sigma v)=\rho(f(v))$ is asserted on every
            vertex, in ``QQbar``, before anything is returned.  The map is
            injective by construction: distinct radii per orbit, distinct
            abscissae per conjugation pair.  Positions are returned, not
            stored: which automorphism to display by is the caller's choice,
            where :meth:`preferred_positions` is the diagram's own.

            The harder sibling notion is a stated absence: an equivariant
            injection of the vertex set into the *vertex set of a lattice
            polytope* $P$ realizing a subgroup of the diagram's automorphisms
            inside $P$'s restricted automorphism group.  The source notebook
            (``Coble Lattice Invariants``) explored it by brute force over
            subgroups of $\mathrm{Aut}(P)$ and over all vertex bijections,
            which is enumeration this codebase does not admit; no owned
            construction exists.
            """
            from sage.rings.qqbar import QQbar
            from sage.rings.number_field.number_field import CyclotomicField

            order = Integer(automorphism.order())
            assert order >= 2, (
                "the identity carries no symmetry to intertwine; pass a "
                "nontrivial element of Aut()"
            )
            orbits = [
                tuple(cycle)
                for cycle in automorphism.cycle_tuples(singletons=True)
                if all(vertex in self._index_set for vertex in cycle)
            ]
            assert sorted(
                vertex for orbit in orbits for vertex in orbit
            ) == sorted(self._index_set), (
                "the automorphism must permute exactly this diagram's vertices"
            )

            complex_positions: dict[Hashable, "Element"] = {}
            zeta = QQbar(CyclotomicField(order).gen())
            if order == 2:
                imaginary = QQbar(CyclotomicField(4).gen())
                place = Integer(0)
                for orbit in sorted(orbits, key=lambda cycle: len(cycle)):
                    if len(orbit) == 1:
                        complex_positions[orbit[0]] = QQbar(place)
                    else:
                        complex_positions[orbit[0]] = QQbar(place) + imaginary
                        complex_positions[orbit[1]] = QQbar(place) - imaginary
                    place += 1
            else:
                fixed = [orbit for orbit in orbits if len(orbit) == 1]
                assert all(len(orbit) in (1, order) for orbit in orbits) and len(fixed) <= 1, (
                    f"a rotation by a primitive order-{order} root of unity fixes "
                    f"only the origin, so every orbit must be free except at most "
                    f"one fixed vertex; orbit lengths are "
                    f"{sorted(len(orbit) for orbit in orbits)}"
                )
                radius = Integer(1)
                for orbit in orbits:
                    if len(orbit) == 1:
                        complex_positions[orbit[0]] = QQbar(0)
                        continue
                    for exponent, vertex in enumerate(orbit):
                        complex_positions[vertex] = QQbar(radius) * zeta**exponent
                    radius += 1

            for vertex in self._index_set:
                image_vertex = automorphism(vertex)
                expected = (
                    complex_positions[vertex].conjugate()
                    if order == 2
                    else zeta * complex_positions[vertex]
                )
                assert complex_positions[image_vertex] == expected, (
                    f"the layout does not intertwine the automorphism at {vertex}"
                )
            return {
                vertex: (value.real(), value.imag())
                for vertex, value in complex_positions.items()
            }

        def node_color(self, vertex: Hashable) -> str:
            r"""Return the TikZ fill color for ``vertex`` from its root square.

            Square ``-4`` roots use ``#F8F9FE``; square ``-2`` roots use
            ``#BFC9CA``.  The color is extractable from the object because it is a
            convention of rooted Coxeter diagrams, not a Sterk fixture.
            """
            vertex = self._element_constructor_(vertex).value
            index = self._index_set.index(vertex)
            square = self.root_intersection_matrix()[index, index]
            assert square in COXETER_NODE_COLORS, f"no Coxeter node color is defined for square {square}"
            return COXETER_NODE_COLORS[square]

        def subdiagram(self, vertices: Iterable[Hashable]) -> Parent:
            selected = tuple(self._element_constructor_(vertex).value for vertex in vertices)
            assert len(selected) == len(set(selected)), f"an induced subdiagram requires distinct vertices; vertices={selected!r}"
            entries = [[self._coxeter_matrix[left, right] for right in selected] for left in selected]
            names = tuple(self.variable_names()[self._index_set.index(vertex)] for vertex in selected)
            positions = None if self._preferred_positions is None else {vertex: self._preferred_positions[vertex] for vertex in selected}
            # The empty subdiagram carries no root: an empty selection has no
            # realization to be rooted in, so it is the unrooted empty diagram.
            if self._root_morphism is not None and selected:
                roots = tuple(
                    self.roots()[self._index_set.index(vertex)]
                    for vertex in selected
                )
                return CoxeterDiagrams().from_roots(
                    roots,
                    names=names,
                    positions=positions,
                    index_set=selected,
                )
            return CoxeterDiagrams().from_coxeter_matrix(
                CoxeterMatrix(entries, index_set=selected),
                names=names,
                positions=positions,
            )

        def plot(self, **options: "GraphOption") -> "Graphics":
            plot_options = {
                "edge_labels": True,
                "vertex_labels": dict(zip(self._index_set, self.variable_names(), strict=True)),
                "vertex_size": 200,
                **options,
            }
            return self.graph().plot(**plot_options)

        def tikz(
            self,
            positions: Mapping[Hashable, Sequence["RingElement | float"]] | None = None,
            scale: "RingElement | float" = 1,
            highlight: Iterable[Hashable] | None = None,
        ) -> str:
            r"""Return TikZ code for the rooted Coxeter diagram.

            Root squares determine node fills: square ``-4`` roots use
            ``#F8F9FE`` and square ``-2`` roots use ``#BFC9CA``.  The
            root-intersection graph stores those squares as self-loops, but TikZ
            deliberately omits the loops and draws only edges between distinct
            vertices: single, double, or triple according to Coxeter matrix entry
            ``3``, ``4``, or ``6``.

            ``highlight`` names vertices of *this* diagram -- an induced
            subdiagram's vertex selection, e.g. a key of
            :meth:`elliptic_subdiagram_orbits` read through ``index_set()`` --
            and renders that subdiagram highlighted inside this diagram's own
            picture: a halo behind each named vertex and behind each bond both
            of whose endpoints are named.  The subdiagram is induced, so the
            haloed bonds are exactly its bonds.
            """
            selected_positions = _normalize_positions(self._index_set, positions) if positions is not None else self.preferred_positions()
            assert selected_positions is not None
            intersections = self.root_intersection_matrix()
            header = [
                rf"\begin{{tikzpicture}}[scale={scale}]",
                r"\definecolor{coxeterNegativeFour}{HTML}{F8F9FE}",
                r"\definecolor{coxeterNegativeTwo}{HTML}{BFC9CA}",
                r"\definecolor{coxeterHighlight}{HTML}{B3E5FC}",
                r"\tikzset{coxeter node/.style={circle,draw,minimum size=6mm,inner sep=0pt}}",
                r"\tikzset{coxeter double/.style={double,double distance=1.4pt}}",
                r"\tikzset{coxeter triple/.style={double,double distance=2.6pt,postaction={draw}}}",
                r"\tikzset{coxeter parallel/.style={line width=1.6pt}}",
                r"\tikzset{coxeter divergent/.style={dashed}}",
                r"\tikzset{coxeter highlight/.style={coxeterHighlight,line width=12pt,line cap=round}}",
            ]

            highlighted: tuple[Hashable, ...] = ()
            if highlight is not None:
                highlighted = tuple(
                    self._element_constructor_(vertex).value for vertex in highlight
                )
                assert len(highlighted) == len(set(highlighted)), (
                    f"a highlighted subdiagram selects distinct vertices; highlight={highlighted!r}"
                )

            def halo_edge(left: Hashable, right: Hashable) -> str:
                x_left, y_left = selected_positions[left]
                x_right, y_right = selected_positions[right]
                return (
                    rf"\draw[coxeter highlight] ({x_left},{y_left}) -- ({x_right},{y_right});"
                )

            def halo_node(vertex: Hashable) -> str:
                x, y = selected_positions[vertex]
                return rf"\fill[coxeterHighlight] ({x},{y}) circle (6mm);"

            halo_lines = [
                halo_edge(left, self._index_set[j])
                for i, left in enumerate(self._index_set)
                for j in range(i + 1, self._index_set.cardinality())
                if left in highlighted
                and self._index_set[j] in highlighted
                and intersections[i, j] != 0
            ] + [halo_node(vertex) for vertex in highlighted]

            def edge(i: int, left: "Element", j: int) -> str:
                right = self._index_set[j]
                return (
                    rf"\draw[{_tikz_edge_style(intersections[i, i], intersections[j, j], intersections[i, j])}] "
                    rf"({_tikz_node_name(left)}) -- ({_tikz_node_name(right)});"
                )

            edge_lines = [
                edge(i, left, j)
                for i, left in enumerate(self._index_set)
                for j in range(i + 1, self._index_set.cardinality())
                if intersections[i, j] != 0
            ]

            def node(i: int, vertex: "Element") -> str:
                x, y = selected_positions[vertex]
                square = intersections[i, i]
                fill = _tikz_node_color(square)
                text = "white" if square == -2 else "black"
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
                    *halo_lines,
                    *edge_lines,
                    *node_lines,
                    r"\end{tikzpicture}",
                ]
            )

        def _matrix_entries(self) -> tuple[tuple[Integer | PlusInfinity, ...], ...]:
            return tuple(tuple(self._coxeter_matrix[left, right] for right in self._index_set) for left in self._index_set)


def _normalize_positions(
    index_set: Sequence[Hashable],
    positions: Mapping[Hashable, Sequence["RingElement | float"]] | None,
) -> dict[Hashable, tuple["RingElement | float", "RingElement | float"]] | None:
    if positions is None:
        return None
    assert set(positions) == set(index_set), f"positions need one coordinate pair for every vertex; index_set={tuple(index_set)!r}, positions={tuple(positions)!r}"
    assert all(len(coordinates) == 2 for coordinates in positions.values()), (
        "every diagram position must be a coordinate pair"
    )
    return {
        vertex: (coordinates[0r], coordinates[1r])
        for vertex, coordinates in positions.items()
    }


def _schlafli_entry(matrix_entry: "Integer | PlusInfinity") -> "Element":
    r"""Entry $-2\cos(\pi/m)$ of the Schläfli matrix at Coxeter bond $m$.

    $\zeta + \zeta^{-1} = 2\cos(\pi/m)$ for $\zeta = e^{i\pi/m}$ a primitive
    $2m$-th root of unity, which keeps the entry algebraic and exact.  At
    $m = \infty$ the mirrors are parallel, $\cos 0 = 1$, and the entry is
    $-2$.
    """
    # Local: AA/QQbar are needed only here, and the module otherwise stays
    # inside ZZ and QQ.
    from sage.rings.qqbar import AA, QQbar

    # Sage's ``CoxeterMatrix`` writes $m=\infty$ as $-1$, which is the entry a
    # matrix read off a Cartan type actually carries; ``infinity`` is what a
    # diagram built from roots carries.  Both name the same bond.
    if matrix_entry is infinity or matrix_entry == -1:
        return AA(-2)
    bond = Integer(matrix_entry)
    assert bond >= 1, f"a Coxeter matrix entry is an integer at least 1 or infinity; matrix_entry={matrix_entry}"
    zeta = QQbar.zeta(2 * bond)
    return AA(-(zeta + zeta ** -1))


def _coxeter_matrix_entry(
    left_square: "Element",
    right_square: "Element",
    pairing: "Element",
) -> "Element":
    r"""Coxeter bond $m$ of a rank-two root pair.

    ``product`` is $(2\cos\theta)^2 = 4\,b(v,w)^2/(v^2 w^2)$: values $1,2,3$
    give $m=3,4,6$; $\geq 4$ means the mirrors do not meet in the interior —
    parallel ($=4$) or divergent ($>4$) — so the bond is $\infty$ (Vinberg,
    *Hyperbolic reflection groups*).
    """
    if pairing == 0:
        return 2
    product = 4 * pairing ** 2 / (left_square * right_square)
    if product >= 4:
        return infinity
    entry_by_product = {1: 3, 2: 4, 3: 6}
    assert product in entry_by_product, f"unsupported rank-two root angle; left_square={left_square}, right_square={right_square}, pairing={pairing}, product={product}"
    return entry_by_product[product]


def _tikz_edge_style(
    left_square: "Element",
    right_square: "Element",
    pairing: "Element",
) -> str:
    matrix_entry = _coxeter_matrix_entry(left_square, right_square, pairing)
    if matrix_entry == 3:
        return "-"
    if matrix_entry == 4:
        return "coxeter double"
    if matrix_entry == 6:
        return "coxeter triple"
    if matrix_entry == infinity:
        # The Coxeter matrix collapses both to ∞; the drawing keeps Vinberg's
        # distinction: thick = parallel mirrors, dashed = divergent mirrors.
        product = 4 * pairing ** 2 / (left_square * right_square)
        return "coxeter parallel" if product == 4 else "coxeter divergent"
    assert False, f"TikZ export does not render Coxeter bond m={matrix_entry}"


def _tikz_node_color(square: "Element") -> str:
    assert square in COXETER_NODE_COLORS, f"no Coxeter node color is defined for square {square}"
    if square == -4:
        return "coxeterNegativeFour"
    return "coxeterNegativeTwo"


def _tikz_node_name(vertex: Hashable) -> str:
    return "v" + "".join(character if character.isalnum() else "_" for character in str(vertex))


__all__ = [
    "CoxeterDiagrams",
]
