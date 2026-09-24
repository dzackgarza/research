r"""Finite Coxeter diagrams, optionally rooted in an integral lattice."""

from itertools import combinations

from sage.categories.morphism import Morphism
from sage.combinat.posets.posets import Poset
from sage.combinat.root_system.cartan_type import CartanType
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
from sage.graphs.graph import Graph
from sage.matrix.constructor import matrix as engine_matrix
from sage.misc.cachefunc import cached_method
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.graph_categories import LabelledGraphs
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    _cross_engine_ring_value,
    _engine_element,
    _engine_numeral,
    _own_ring,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.tensors.tensor import _engine_component_matrix, tensor


def _engine_cartan_type_data(value):
    r"""Lower owned session numerals before Sage parses Cartan presentation data."""
    if isinstance(value, list):
        return [_engine_cartan_type_data(entry) for entry in value]
    if isinstance(value, tuple):
        return tuple(_engine_cartan_type_data(entry) for entry in value)
    parent = getattr(value, "parent", lambda: None)()
    if parent is not None and parent in OwnedRings():
        return _engine_numeral(_own_ring(SageZZ), value)
    return value


def _coxeter_entry(q1, q2, pairing):
    integers = _own_ring(SageZZ)
    q1 = _engine_element(integers, q1)
    q2 = _engine_element(integers, q2)
    pairing = _engine_element(integers, pairing)
    if q1 == 0 or q2 == 0:
        raise ValueError(
            f"cannot compute the Coxeter angle of two vectors with squares {q1} and {q2}: "
            f"a root must have nonzero square"
        )
    if pairing == 0:
        return SageZZ(2)
    four_cos_squared = QQ(4 * pairing**2) / QQ(q1 * q2)
    if four_cos_squared == 1:
        return SageZZ(3)
    if four_cos_squared == 2:
        return SageZZ(4)
    if four_cos_squared == 3:
        return SageZZ(6)
    if four_cos_squared >= 4:
        return Infinity
    raise ValueError(
        f"two roots with squares {q1}, {q2} and pairing {pairing} have no crystallographic "
        f"Coxeter angle pi/m: 4 cos^2(pi/m) would be {four_cos_squared}, which is not 0, 1, 2, 3 "
        f"or at least 4"
    )


class CoxeterDiagramMorphism(Morphism):
    r"""A vertex map preserving every Coxeter exponent.

    A Coxeter diagram is its symmetric matrix ``(m_vw)``.  A morphism sends
    vertices to vertices and preserves that entire matrix, including the
    entries ``m=2`` that are omitted from the drawn graph.  Thus composition
    is ordinary composition of the underlying vertex maps.
    """

    def __init__(self, parent, function) -> None:
        Morphism.__init__(self, parent)
        self._vertex_function = function

    def __call__(self, vertex):
        source_vertex = self.domain().index_set()(vertex)
        return self.codomain().index_set()(self._vertex_function(source_vertex))

    def __mul__(self, other):
        if not isinstance(other, CoxeterDiagramMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        return CoxeterDiagrams().Mor(other.domain(), self.codomain())(
            lambda vertex: self(other(vertex))
        )

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, CoxeterDiagramMorphism)
            and other.parent() is self.parent()
            and all(self(vertex) == other(vertex) for vertex in self.domain().index_set())
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(
            (
                id(self.parent()),
                tuple(self(vertex) for vertex in self.domain().index_set()),
            )
        )

    def images(self):
        r"""Return the images in source-vertex order."""
        return finite_ordered_set(
            tuple(self(vertex) for vertex in self.domain().index_set())
        )

    def is_identity(self) -> bool:
        return self.domain() is self.codomain() and all(
            self(vertex) == vertex for vertex in self.domain().index_set()
        )


class CoxeterDiagramMor(CategoricalMor):
    r"""The bond-preserving maps between two represented Coxeter diagrams."""

    Element = CoxeterDiagramMorphism

    def _element_constructor_(self, datum):
        if isinstance(datum, CoxeterDiagramMorphism):
            if datum.parent() is self:
                return datum
            raise ValueError(
                f"{datum} is a morphism {datum.domain()} -> {datum.codomain()}, not a morphism "
                f"{self.domain()} -> {self.codomain()} of Coxeter diagrams"
            )
        if callable(datum):
            function = datum
        else:
            images = tuple(datum)
            vertices = tuple(self.domain().index_set())
            if len(images) != len(vertices):
                raise ValueError(
                    f"{images} does not define a morphism of Coxeter diagrams from {self.domain()}: "
                    f"it gives {len(images)} images for {len(vertices)} vertices"
                )
            assignment = dict(zip(vertices, images, strict=True))
            function = assignment.__getitem__
        morphism = CoxeterDiagramMorphism(self, function)
        for left in self.domain().index_set():
            for right in self.domain().index_set():
                if self.domain().coxeter_entry(left, right) != self.codomain().coxeter_entry(
                    morphism(left), morphism(right)
                ):
                    raise ValueError(
                        f"{morphism} is not a morphism of Coxeter diagrams: the vertices {left}, {right} "
                        f"have Coxeter entry {self.domain().coxeter_entry(left, right)} in {self.domain()}, "
                        f"but their images {morphism(left)}, {morphism(right)} have entry "
                        f"{self.codomain().coxeter_entry(morphism(left), morphism(right))} in {self.codomain()}"
                    )
        return morphism

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"there is no identity morphism from {self.domain()} to {self.codomain()}: an "
                f"identity needs its domain and codomain to be the same Coxeter diagram"
            )
        return self(lambda vertex: vertex)


class CoxeterDiagramMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = CoxeterDiagramMor


class CoxeterDiagrams(OwnedCategory):
    r"""Finite Coxeter diagrams: labelled graphs encoding a symmetric angle matrix."""

    _MorCategory = CoxeterDiagramMorCategoryConstruction

    def an_object(self):
        r"""The diagram of ``A_2``: two vertices joined by an edge of order 3."""
        return self.from_cartan_type(["A", 2])

    @classmethod
    def _repr_object_names(cls):
        return "Coxeter diagrams"

    def super_categories(self):
        return [LabelledGraphs()]

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError(
                f"there are no morphisms of Coxeter diagrams from {domain} to {codomain}: both "
                f"must be Coxeter diagrams"
            )
        return self.MorCategory().Of(domain, codomain)

    @cached_method
    def minimal_edge_lattices(self):
        r"""Return the five minimal integral rank-two mirror configurations."""
        from dzack_research.preamble.categories.sets.indexed_families import indexed_family

        labels = finite_ordered_set(
            ("orthogonal", "single", "double", "parallel", "ultraparallel")
        )
        grams = {
            "orthogonal": ((-2, 0), (0, -2)),
            "single": ((-2, 1), (1, -2)),
            "double": ((-2, 2), (2, -4)),
            "parallel": ((-2, 2), (2, -2)),
            "ultraparallel": ((-2, 3), (3, -2)),
        }
        integers = _own_ring(SageZZ)
        return indexed_family(
            labels,
            lambda label: Lattices(integers)(grams[str(label)], names=("r1", "r2")),
            name="Minimal Coxeter edge lattices",
        )

    class ParentMethods:
        def __init__(
            self,
            coxeter_matrix,
            names=None,
            roots=None,
            root_gram=None,
            positions=None,
            **rest,
        ) -> None:
            self._coxeter_matrix = CoxeterMatrix(coxeter_matrix)
            self._index_set = finite_ordered_set(tuple(self._coxeter_matrix.index_set()))
            if names is None:
                names = (f"s_{index}" for index in self._index_set)
            elif isinstance(names, str):
                names = (part.strip() for part in names.split(","))
            # One name per vertex, stated as the pairing of the names with the
            # vertices rather than by measuring the names against the vertex
            # cardinality.
            self._names = tuple(
                name for _vertex, name in zip(self._index_set, names, strict=True)
            )
            self._roots = None if roots is None else tuple(roots)
            self._root_gram = root_gram
            if positions is None:
                self._preferred_positions = None
            else:
                if set(positions) != set(self._index_set):
                    raise ValueError(
                        f"the drawing positions {positions} do not place the vertices "
                        f"{self._index_set}: every vertex needs exactly one position"
                    )
                if any(len(coordinates) != 2 for coordinates in positions.values()):
                    raise ValueError(
                        f"the drawing positions {positions} are not all points of the plane: every "
                        f"position must be a pair of coordinates"
                    )
                self._preferred_positions = {vertex: (coordinates[0], coordinates[1]) for vertex, coordinates in positions.items()}
            self._computed_positions = None
            super().__init__(**rest)

        def index_set(self):
            return self._index_set

        def cardinality(self):
            return self._index_set.cardinality()

        def vertex(self, position):
            return self.index_set()[int(position)]

        def vertices(self):
            return self.index_set()

        def __contains__(self, vertex) -> bool:
            return vertex in self.index_set()

        is_parent_of = __contains__

        def _element_constructor_(self, vertex):
            return self.index_set()(vertex)

        def __iter__(self):
            return iter(self.index_set())

        def has_edge(self, left, right) -> bool:
            return left != right and self.coxeter_entry(left, right) != 2

        def edges(self):
            edge_space = self.index_set()**2
            return finite_ordered_set(
                tuple(
                    edge_space((left, right))
                    for left, right in combinations(tuple(self.index_set()), 2)
                    if self.has_edge(left, right)
                )
            )

        def is_directed(self) -> bool:
            return False

        def is_symmetric(self) -> bool:
            return True

        def vertex_label(self, vertex):
            self.index_set()(vertex)
            return "Coxeter vertex"

        def edge_label(self, left, right):
            if not self.has_edge(left, right):
                raise ValueError(
                    f"the vertices {left} and {right} of {self} are not joined by an edge, so the "
                    f"edge has no label"
                )
            return self.coxeter_entry(left, right)

        def num_vertices(self):
            return self.cardinality()

        def mor(self, images, codomain):
            return CoxeterDiagrams().Mor(self, codomain)(images)

        def vertex_weight(self, vertex):
            return self.vinberg_invariant_matrix().vertex_weight(vertex)

        def edge_weight(self, left, right):
            return self.vinberg_invariant_matrix().edge_weight(left, right)

        def vertex_names(self):
            return self._names

        def coxeter_matrix(self):
            return self._coxeter_matrix

        def coxeter_entry(self, left, right):
            entry = self._coxeter_matrix[left, right]
            return Infinity if entry == -1 else entry

        def is_rooted(self) -> bool:
            return self._roots is not None

        def roots(self):
            if self._roots is None:
                raise ValueError(
                    f"{self} has no roots: it was given only by its Coxeter matrix, not by "
                    f"roots in a lattice"
                )
            return self._roots

        def root_gram_tensor(self):
            if self._root_gram is None:
                raise ValueError(
                    f"{self} has no Gram matrix of roots: it was given only by its Coxeter "
                    f"matrix, not by roots in a lattice"
                )
            return self._root_gram

        def preferred_positions(self):
            r"""Return stored presentation coordinates, or a computed graph layout."""
            if self._preferred_positions is not None:
                return dict(self._preferred_positions)
            if self._computed_positions is None:
                layout = self.graph().layout()
                self._computed_positions = {vertex: (coordinates[0], coordinates[1]) for vertex, coordinates in layout.items()}
            return dict(self._computed_positions)

        def tikz_picture(self):
            r"""Return a TikZ view of this live Coxeter diagram.

            The Coxeter matrix remains the mathematical datum.  The rendering
            draws exactly the pairs with ``m_ij != 2``.  The conventional
            ``m=3`` bond is unlabeled; every other bond carries its Coxeter
            order, including ``infinity``.
            """
            positions = self.preferred_positions()
            ranking = self.index_set().ranking_map()
            node_names = {
                vertex: f"v{ranking(vertex)}" for vertex in self.index_set()
            }
            lines = [
                r"\begin{tikzpicture}[every node/.style={circle,draw,inner sep=1.5pt}]"
            ]
            for vertex in self.index_set():
                x, y = positions[vertex]
                label = self.vertex_names()[ranking(vertex)]
                lines.append(
                    rf"  \node ({node_names[vertex]}) at ({float(x):.6g},{float(y):.6g}) {{$ {label} $}};"
                )
            for left, right in combinations(self.index_set(), 2):
                bond = self.coxeter_entry(left, right)
                if bond == 2:
                    continue
                if bond == 3:
                    label = ""
                else:
                    bond_label = r"\infty" if bond == Infinity else str(bond)
                    label = (
                        rf" node[midway,fill=white,draw=none] {{$ {bond_label} $}}"
                    )
                lines.append(
                    rf"  \draw ({node_names[left]}) --{label} ({node_names[right]});"
                )
            lines.append(r"\end{tikzpicture}")
            return "\n".join(lines)

        def graph(self):
            r"""Return the Coxeter graph: one vertex per mirror, edges labelled by the bond.

            This is the graph of the definition (Bourbaki, *Groupes et algèbres
            de Lie* IV.1.9; Humphreys, *Reflection Groups and Coxeter Groups*
            §2.3): vertices \(v,w\) are joined exactly when \(m_{vw}\neq 2\),
            and the edge carries the label \(m_{vw}\).  The label is the datum.
            The customary drawing that renders \(m=4\) as a double edge and
            \(m=6\) as a triple edge is a rendering of that label available for
            two of its values, and never a second kind of edge.

            The Coxeter matrix records only \(m\), so at \(m=\infty\) it cannot
            say whether the two mirrors are parallel or divergent.  That
            distinction is a fact about the roots, and a rooted diagram answers
            it through :meth:`mirrors_are_parallel` and
            :meth:`mirrors_are_divergent`.
            """
            graph = Graph(multiedges=False, loops=False)
            graph.add_vertices(tuple(self.index_set()))
            for left, right in combinations(self.index_set(), 2):
                bond = self.coxeter_entry(left, right)
                if bond != 2:
                    graph.add_edge(left, right, bond)
            return graph

        def connected_components(self):
            r"""Return the connected components, as induced subdiagrams."""
            return finite_ordered_set(
                tuple(
                    self.induced_subdiagram(component)
                    for component in self.graph().connected_components(sort=False)
                )
            )

        def is_connected(self) -> bool:
            r"""Return whether this diagram has exactly one connected component.

            One component is the definition, so the diagram on no vertices is
            not connected: it has zero components, not one.
            """
            return self.graph().connected_components_number() == 1

        def induced_subdiagram(self, vertices):
            vertices = tuple(vertices)
            if not vertices:
                return _coxeter_diagram(
                    CoxeterMatrix(engine_matrix(SageZZ, 0, 0), index_set=()),
                    names=(),
                    roots=() if self.is_rooted() else None,
                    root_gram=(
                        tensor(self._root_gram.base_ring(), (), (0, 0), [])
                        if self.is_rooted()
                        else None
                    ),
                    positions=None if self._preferred_positions is None else {},
                )
            if any(vertex not in self.index_set() for vertex in vertices):
                raise ValueError(
                    f"cannot form the subdiagram of {self} induced on {vertices}: some of them are "
                    f"not vertices of {self}, whose vertices are {self.index_set()}"
                )
            matrix_ = self.coxeter_matrix()
            entries = [[matrix_[left, right] for right in vertices] for left in vertices]
            ranking = self.index_set().ranking_map()
            names = tuple(self._names[ranking(vertex)] for vertex in vertices)
            preferred_positions = None if self._preferred_positions is None else {vertex: self._preferred_positions[vertex] for vertex in vertices}
            if self.is_rooted():
                selected = finite_ordered_set(
                    tuple(self.index_set().ranking_map()(vertex) for vertex in vertices)
                )
                roots = tuple(self._roots[position] for position in selected)
                gram = tensor(
                    self._root_gram.base_ring(),
                    (),
                    (selected.cardinality(), selected.cardinality()),
                    [
                        [self._root_gram[i, j] for j in selected]
                        for i in selected
                    ],
                )
            else:
                roots = None
                gram = None
            return _coxeter_diagram(
                CoxeterMatrix(entries, index_set=vertices),
                names=names,
                roots=roots,
                root_gram=gram,
                positions=preferred_positions,
            )

        def schlafli_tensor(self):
            r"""Return the normalized reflection Gram tensor ``S_ii=1``.

            A rooted diagram retains more metric data than its Coxeter matrix:
            an infinite bond can mean parallel or divergent mirrors.  Normalize
            the actual root Gram in that case, using
            ``S_ij = -|b(r_i,r_j)|/sqrt(q(r_i)q(r_j))``.  An unrooted diagram
            has only the bond labels, so its infinite bond is necessarily the
            parallel boundary value ``-1``.
            """
            from sage.all import AA as SageAA
            from sage.all import cos, pi

            real_algebraics = _own_ring(SageAA)
            rooted_gram = self.root_gram_tensor() if self.is_rooted() else None
            ranking = self.index_set().ranking_map()
            values = []
            for left in self.index_set():
                row = []
                for right in self.index_set():
                    if left == right:
                        row.append(real_algebraics.one())
                        continue
                    if rooted_gram is not None:
                        i = int(ranking(left))
                        j = int(ranking(right))
                        left_square = SageAA(
                            _engine_element(rooted_gram.base_ring(), rooted_gram[i, i])
                        )
                        right_square = SageAA(
                            _engine_element(rooted_gram.base_ring(), rooted_gram[j, j])
                        )
                        pairing = SageAA(
                            _engine_element(rooted_gram.base_ring(), rooted_gram[i, j])
                        )
                        normalized = -abs(pairing) / (left_square * right_square).sqrt()
                        row.append(_cross_engine_ring_value(normalized))
                        continue
                    m = self.coxeter_entry(left, right)
                    if m == Infinity:
                        row.append(-real_algebraics.one())
                    else:
                        row.append(_cross_engine_ring_value(-SageAA(cos(pi / m))))
                values.append(row)
            mirrors = self.cardinality()
            return tensor(real_algebraics, (), (mirrors, mirrors), values)

        def _inertia_counts(self):
            r"""Return \((n_+,n_-,n_0)\) of the Schlaefli form, by Sylvester.

            The Coxeter diagram is classified by the inertia of its Schlaefli
            form, and that form is allowed to be degenerate, so the zero index
            \(n_0\) is part of the answer.  This is not a signature *pair*.
            """

            eigenvalues = _engine_component_matrix(self.schlafli_tensor()).eigenvalues()
            positive = sum(1 for value in eigenvalues if value > 0)
            negative = sum(1 for value in eigenvalues if value < 0)
            # The three indices sum to the rank of the Schlaefli form, which is
            # the number of vertices of the diagram.
            zero = int(self.cardinality()) - positive - negative
            return cardinal(positive), cardinal(negative), cardinal(zero)

        def positive_inertia_index(self):
            r"""Return \(n_+\), the positive index of inertia of the Schlaefli form."""
            return self._inertia_counts()[0]

        def negative_inertia_index(self):
            r"""Return \(n_-\), the negative index of inertia of the Schlaefli form."""
            return self._inertia_counts()[1]

        def zero_inertia_index(self):
            r"""Return \(n_0\), the dimension of the radical of the Schlaefli form."""
            return self._inertia_counts()[2]

        def is_elliptic(self) -> bool:
            return self.negative_inertia_index() == 0 and self.zero_inertia_index() == 0

        def is_parabolic(self) -> bool:
            return self.negative_inertia_index() == 0 and self.zero_inertia_index() == 1

        def is_hyperbolic(self) -> bool:
            return self.negative_inertia_index() == 1

        def _induced_subdiagrams(self, predicate, *, connected):
            r"""Return the induced subdiagrams satisfying ``predicate``.

            The vertex subsets of a finite diagram are finite in number, so the
            enumeration terminates by the finiteness of the index set.
            """
            vertices = tuple(self.index_set())
            selected = []
            for size in range(len(vertices) + 1):
                for subset in combinations(vertices, size):
                    diagram = self.induced_subdiagram(subset)
                    if predicate(diagram) and (not connected or diagram.is_connected()):
                        selected.append(diagram)
            return finite_ordered_set(tuple(selected))

        def elliptic_subdiagrams(self, *, connected=False):
            r"""Return the elliptic induced subdiagrams.

            The subdiagram on no vertices is elliptic: its Schlaefli form on the
            zero space has no negative and no zero index of inertia.  It is the
            minimum of :meth:`subdiagram_poset`, and it is excluded by
            ``connected=True`` because it has no connected component at all.
            """
            return self._induced_subdiagrams(
                lambda diagram: diagram.is_elliptic(), connected=connected
            )

        def parabolic_subdiagrams(self, *, connected=False):
            r"""Return the parabolic induced subdiagrams."""
            return self._induced_subdiagrams(
                lambda diagram: diagram.is_parabolic(), connected=connected
            )

        def schlaflian(self):
            r"""Return \(\det C\) for the Schlaefli matrix \(C\) of this diagram.

            \(C_{vv}=2\) and \(C_{vw}=-2\cos(\pi/m_{vw})\), so \(C\) is twice
            the normalized :meth:`schlafli_tensor`.  This is the normalization
            the literature determinant tables use: \(n+1\) for \(A_n\), \(2\)
            for \(B_n\) and \(C_n\), \(4\) for \(D_n\), \(9-n\) for \(E_n\),
            \(5-n\) for \(F_n\) and \(3-n\) for \(G_n\).  It vanishes exactly
            on the diagrams with a radical, which is where each family passes
            from elliptic to parabolic.
            """
            normalized = _engine_component_matrix(self.schlafli_tensor())
            return (2 * normalized).determinant()

        def vinberg_invariant_matrix(self):
            r"""Return the Vinberg invariant matrix of this diagram.

            The projective invariants \([4b(r_v,r_w)^2:q(r_v)q(r_w)]\) of the
            pairs of mirrors.  On a rooted diagram they come from the root
            Gram and are exact over the base ring; on an unrooted one only the
            bonds are available, and the invariants are the algebraic numbers
            \(4\cos^2(\pi/m)\).  The passage back to the Coxeter matrix loses
            the distinction between parallel and divergent mirrors.
            """
            from dzack_research.preamble.categories.vinberg_invariants import (
                VinbergInvariantMatrices,
            )

            return VinbergInvariantMatrices().from_coxeter_diagram(self)

        def coxeter_group(self):
            r"""Return the Coxeter group \(W\) of this diagram.

            \(W=\langle s_v \mid s_v^2,\ (s_v s_w)^{m_{vw}}\rangle\), one
            involution per vertex.  The owned group carries that presentation:
            it answers ``presenting_free_group`` and ``defining_relations`` as
            well as ``order``, so the presented group and the reflection
            representation are one object here and not two constructions.
            """
            from dzack_research.preamble.categories.group.groups import Groups

            return Groups.Coxeter(self.coxeter_matrix())

        def finitely_presented_coxeter_group(self):
            r"""Return the same owned Coxeter group, which retains its defining presentation."""
            return self.coxeter_group()

        @cached_method
        def _bond_preserving_permutation_group(self):
            r"""Return the owned automorphism group of the labelled Coxeter graph.

            NetworkX enumerates graph automorphisms on the finite ordinal of
            vertex positions.  The public group is then the corresponding
            subgroup of the owned symmetric group.  This avoids Sage's current
            ``Graph.automorphism_group`` crash while keeping the maintained
            graph-isomorphism algorithm as the computation owner.
            """
            import networkx as nx

            from dzack_research.preamble.categories.group.groups import Groups

            vertices = tuple(self.index_set())
            graph = nx.Graph()
            for position in range(len(vertices)):
                attributes = {}
                if self.is_rooted():
                    attributes["root_square"] = self._root_gram[position, position]
                graph.add_node(position, **attributes)
            for left_position, right_position in combinations(range(len(vertices)), 2):
                bond = self.coxeter_entry(
                    vertices[left_position], vertices[right_position]
                )
                if bond != 2:
                    graph.add_edge(left_position, right_position, bond=bond)

            node_match = (
                nx.algorithms.isomorphism.categorical_node_match(
                    "root_square", None
                )
                if self.is_rooted()
                else None
            )
            edge_match = nx.algorithms.isomorphism.categorical_edge_match(
                "bond", None
            )
            matcher = nx.algorithms.isomorphism.GraphMatcher(
                graph, graph, node_match=node_match, edge_match=edge_match
            )
            symmetric = Groups.S(len(vertices))
            automorphisms = tuple(
                symmetric(
                    [mapping[position] + 1 for position in range(len(vertices))]
                )
                for mapping in matcher.isomorphisms_iter()
            )
            return symmetric.subgroup(automorphisms)

        def Aut(self):
            r"""Return the group of diagram automorphisms.

            The automorphisms of the Coxeter graph with its bond labels: for
            \(A_n\) with \(n\geq 2\) the path reversal, of order two; for
            \(D_4\) the symmetric group on the three outer nodes, triality; for
            \(E_8\) trivial.
            """
            return self._bond_preserving_permutation_group()

        def _orbit_vertex_sets(self, diagram):
            r"""Return the vertex sets of the :meth:`Aut`-orbit of ``diagram``."""
            vertices = tuple(diagram.index_set())
            if not vertices:
                # The empty vertex set is fixed by every permutation.
                return (frozenset(),)
            ranking = self.index_set().ranking_map()
            unranking = ranking.inverse()
            positions = tuple(int(ranking(vertex)) for vertex in vertices)
            group = self._bond_preserving_permutation_group()
            images = {
                frozenset(int(automorphism(position + 1)) - 1 for position in positions)
                for automorphism in group
            }
            return tuple(
                frozenset(unranking(position) for position in image)
                for image in images
            )

        def _vertex_set_orbits(self, subdiagrams):
            r"""Return one representative subdiagram per :meth:`Aut`-orbit."""
            seen = set()
            representatives = []
            for diagram in subdiagrams:
                if frozenset(diagram.index_set()) in seen:
                    continue
                seen.update(self._orbit_vertex_sets(diagram))
                representatives.append(diagram)
            return finite_ordered_set(tuple(representatives))

        def subdiagram_orbits(self):
            r"""Return one induced subdiagram per :meth:`Aut`-orbit."""
            return self._vertex_set_orbits(
                self._induced_subdiagrams(lambda diagram: True, connected=False)
            )

        def elliptic_subdiagram_orbits(self, *, connected=False):
            r"""Return one elliptic induced subdiagram per :meth:`Aut`-orbit."""
            return self._vertex_set_orbits(self.elliptic_subdiagrams(connected=connected))

        def parabolic_subdiagram_orbits(self, *, connected=False):
            r"""Return one parabolic induced subdiagram per :meth:`Aut`-orbit."""
            return self._vertex_set_orbits(self.parabolic_subdiagrams(connected=connected))

        def _maximal_by_vertex_inclusion(self, subdiagrams):
            r"""Return the members maximal for inclusion of vertex sets."""
            vertex_sets = tuple(frozenset(diagram.index_set()) for diagram in subdiagrams)
            return finite_ordered_set(
                tuple(
                    diagram
                    for diagram, vertices in zip(subdiagrams, vertex_sets, strict=True)
                    if not any(
                        vertices < other for other in vertex_sets
                    )
                )
            )

        def maximal_elliptic_subdiagrams(self, *, connected=False):
            r"""Return the elliptic induced subdiagrams maximal for inclusion."""
            return self._maximal_by_vertex_inclusion(
                self.elliptic_subdiagrams(connected=connected)
            )

        def maximal_parabolic_subdiagrams(self, *, connected=False):
            r"""Return the parabolic induced subdiagrams maximal for inclusion."""
            return self._maximal_by_vertex_inclusion(
                self.parabolic_subdiagrams(connected=connected)
            )

        def _subdiagram_poset_on(self, subdiagrams):
            r"""Return ``subdiagrams`` ordered by inclusion of their vertex sets."""
            members = tuple(subdiagrams)
            vertices_of = {
                id(diagram): frozenset(diagram.index_set()) for diagram in members
            }

            def below(left, right) -> bool:
                return vertices_of[id(left)] <= vertices_of[id(right)]

            return Poset((members, below))

        def subdiagram_poset(self):
            r"""Return every induced subdiagram, ordered by inclusion of vertices.

            The maximum is the diagram itself and the minimum is the subdiagram
            on no vertices.
            """
            return self._subdiagram_poset_on(
                self._induced_subdiagrams(lambda diagram: True, connected=False)
            )

        def elliptic_subdiagram_poset(self, *, connected=False):
            r"""Return the elliptic induced subdiagrams ordered by inclusion."""
            return self._subdiagram_poset_on(
                self.elliptic_subdiagrams(connected=connected)
            )

        def parabolic_subdiagram_poset(self, *, connected=False):
            r"""Return the parabolic induced subdiagrams ordered by inclusion."""
            return self._subdiagram_poset_on(
                self.parabolic_subdiagrams(connected=connected)
            )

        def _subdiagram_orbit_poset_on(self, representatives):
            r"""Return the orbit order on one representative per :meth:`Aut`-orbit.

            The order on orbits, not on the representatives:
            \([H]\leq[K]\) when some member of \([H]\) is an induced
            subdiagram of some member of \([K]\).  :meth:`Aut` is transitive
            on each orbit, so an automorphism carrying that member of \([K]\)
            to the representative of \([K]\) carries the member of \([H]\)
            along, and the relation holds exactly when some member of
            \([H]\) has its vertices inside the representative of \([K]\),
            which is what is asked here.

            It is a partial order.  Reflexive, because a representative is a
            member of its own orbit.  Antisymmetric, because every member of
            an orbit has the same number of vertices, so two containments
            force equality and hence one orbit.  Transitive, by the same
            transport of the containment along an automorphism.
            """
            members = tuple(representatives)
            orbit_vertex_sets = {
                id(diagram): self._orbit_vertex_sets(diagram) for diagram in members
            }

            def below(left, right) -> bool:
                target = frozenset(right.index_set())
                return any(
                    vertices <= target for vertices in orbit_vertex_sets[id(left)]
                )

            return Poset((members, below))

        def subdiagram_orbit_poset(self, orbits):
            r"""Return the orbit-inclusion poset on the supplied representatives."""
            return self._subdiagram_orbit_poset_on(tuple(orbits))

        def elliptic_subdiagram_orbit_poset(self, *, connected=False):
            r"""Return the elliptic subdiagram orbits in the orbit order."""
            return self._subdiagram_orbit_poset_on(
                self.elliptic_subdiagram_orbits(connected=connected)
            )

        def parabolic_subdiagram_orbit_poset(self, *, connected=False):
            r"""Return the parabolic subdiagram orbits in the orbit order."""
            return self._subdiagram_orbit_poset_on(
                self.parabolic_subdiagram_orbits(connected=connected)
            )

        def root_realization(self):
            r"""Return the lattice in which the diagram roots are realized."""
            roots = self.roots()
            assert roots, (
                f"{self} has no vertices, so it has no roots and no lattice in which they lie"
            )
            return roots[0].parent()

        def root_lattice(self):
            r"""Return the abstract lattice presented by the root Gram.

            One module generator per vertex, paired by the root Gram.  It is
            the domain of :meth:`root_morphism`; the realization is its
            codomain, and the two coincide exactly when the roots generate a
            finite-index sublattice with the same Gram framing.
            """
            return Lattices(self.root_realization().base_ring())(
                self.root_gram_tensor()
            )

        def root_morphism(self):
            r"""Return the morphism carrying each formal root to its realization.

            The map \(\rho:\Lambda\to L\) from :meth:`root_lattice` to
            :meth:`root_realization` sending the \(v\)-th module generator to
            the \(v\)-th root.  It preserves the form by construction, because
            the Gram of the domain is the Gram of the roots; a diagram is a
            realization of its abstract root data through this arrow, and not
            through a stored copy of the roots on the lattice.
            """
            roots = self.roots()
            return self.root_lattice().Mor(self.root_realization())(
                {position: root for position, root in enumerate(roots)}
            )

        def root(self, vertex):
            r"""Return the selected realizing root attached to ``vertex``."""
            normalized = self.index_set()(vertex)
            position = int(self.index_set().ranking_map()(normalized))
            return self.roots()[position]

        def scaled_cartan_type(self):
            r"""Recognize a connected elliptic crystallographic rooted diagram as ``(type, scale)``."""
            if not self.is_rooted() or self.cardinality() == 0:
                return None
            if not self.is_connected() or not self.is_elliptic():
                raise ValueError(
                    f"cannot recognize a Cartan type of {self}: the diagram must be connected and "
                    f"elliptic (spherical), and it is not both"
                )
            gram = self.root_gram_tensor()
            rank = int(self.cardinality())
            squares = tuple(-SageZZ(gram[index, index]) for index in range(rank))
            shortest = min(squares)
            if shortest <= 0 or shortest % 2:
                raise ValueError(
                    f"cannot recognize a scaled Cartan type of {self}: the shortest root must "
                    f"have square -2k for a positive integer k, but the squares are {squares}"
                )
            scale = SageZZ(shortest // 2)
            coxeter_type = self.coxeter_matrix().coxeter_type()
            if coxeter_type is self.coxeter_matrix():
                raise ValueError(
                    f"{self} is elliptic, but its Coxeter matrix {self.coxeter_matrix()} was not "
                    f"recognized as a finite Coxeter type"
                )
            cartan = coxeter_type.cartan_type()
            if str(cartan[0]) == "H":
                raise ValueError(
                    f"{self} has Coxeter type {cartan}, which is not crystallographic, so it has "
                    f"no Cartan type and no integral root scale"
                )
            if str(cartan[0]) == "B":
                short_count = sum(square == 2 * scale for square in squares)
                if rank == 2:
                    cartan = CartanType(["C", 2])
                elif short_count == 1:
                    cartan = CartanType(["B", rank])
                elif short_count == rank - 1:
                    cartan = CartanType(["C", rank])
                else:
                    raise ArithmeticError(
                        f"{self} has Coxeter type B/C of rank {rank}, but its root squares {squares} "
                        f"match neither B (one short root) nor C (one long root)"
                    )
            reference = Lattices.root_lattice(str(cartan[0]), int(cartan[1])).twist(scale)
            reference_diagram = CoxeterDiagrams().from_roots(tuple(reference.module_generators()))
            if not self.root_intersection_graph().is_isomorphic(
                reference_diagram.root_intersection_graph(), edge_labels=True
            ):
                raise ArithmeticError(
                    f"{self} was recognized as Cartan type {cartan} with scale {scale}, but the "
                    f"roots of that type do not have the same Gram data as the roots of {self}"
                )
            return cartan, scale

        def component_scaled_cartan_types(self):
            r"""Return the component-indexed family of scaled Cartan types, retaining multiplicity."""
            from dzack_research.preamble.categories.sets.indexed_families import indexed_family

            components = self.connected_components()
            labels = finite_ordered_set(tuple(range(int(components.cardinality()))))
            return indexed_family(
                labels,
                lambda position: components[int(position)].scaled_cartan_type(),
                name="Scaled Cartan types of Coxeter components",
            )

        def drawing_conventions(self):
            return {
                "root squares": "stored as self-loops in root_intersection_graph(), omitted from TikZ",
                "ordinary Coxeter bond": "m=3 is drawn without a label",
                "other Coxeter bonds": "the Coxeter exponent labels the edge",
            }

        def node_color(self, vertex):
            r"""Return the archived rooted-diagram fill convention determined by root square."""
            square = self.root(vertex).q()
            colors = {-4: "#F8F9FE", -2: "#BFC9CA"}
            try:
                return colors[int(square)]
            except KeyError as error:
                raise ValueError(
                    f"cannot draw the vertex {vertex} of {self}: node colors are defined for "
                    f"roots of square -2 and -4, and this root has square {square}"
                ) from error

        def equivariant_positions(self, automorphism):
            r"""Return exact planar positions intertwining a finite diagram automorphism."""
            from sage.rings.number_field.number_field import CyclotomicField
            from sage.rings.qqbar import QQbar

            order = int(automorphism.order())
            if order < 2:
                raise ValueError(
                    f"cannot place the vertices of {self} symmetrically under {automorphism}: it "
                    f"has order {order}, and a symmetric layout needs an automorphism of order at least 2"
                )
            unseen = set(self.index_set())
            orbits = []
            while unseen:
                start = next(iter(unseen))
                orbit = []
                point = start
                while point not in orbit:
                    orbit.append(point)
                    unseen.discard(point)
                    point = automorphism(point)
                if point != start:
                    raise ArithmeticError(
                        f"{automorphism} is not a permutation of the vertices of {self}: following it "
                        f"from {start} does not return to {start}"
                    )
                orbits.append(tuple(orbit))
            zeta = QQbar(CyclotomicField(order).gen())
            positions = {}
            if order == 2:
                imaginary = QQbar(CyclotomicField(4).gen())
                place = 0
                for orbit in sorted(orbits, key=len):
                    if len(orbit) == 1:
                        positions[orbit[0]] = QQbar(place)
                    elif len(orbit) == 2:
                        positions[orbit[0]] = QQbar(place) + imaginary
                        positions[orbit[1]] = QQbar(place) - imaginary
                    else:
                        raise ValueError(
                            f"{automorphism} has order 2 but an orbit {orbit} of length {len(orbit)}: "
                            f"an involution has only fixed points and 2-cycles"
                        )
                    place += 1
            else:
                fixed = tuple(orbit for orbit in orbits if len(orbit) == 1)
                if any(len(orbit) not in (1, order) for orbit in orbits) or len(fixed) > 1:
                    raise ValueError(
                        f"cannot place the vertices of {self} as a rotation by {automorphism}: a "
                        f"rotation of order {order} needs every orbit of length 1 or {order} and at most "
                        f"one fixed vertex, but the orbits are {orbits}"
                    )
                radius = 1
                for orbit in orbits:
                    if len(orbit) == 1:
                        positions[orbit[0]] = QQbar.zero()
                        continue
                    for exponent, vertex in enumerate(orbit):
                        positions[vertex] = QQbar(radius) * zeta**exponent
                    radius += 1
            return {
                vertex: (value.real(), value.imag()) for vertex, value in positions.items()
            }

        def subdiagram(self, vertices):
            return self.induced_subdiagram(vertices)

        def plot(self, **options):
            return self.graph().plot(**options)

        def tikz(self, **_options):
            return self.tikz_picture()

        def root_intersection_graph(self):
            r"""Return the graph of root squares and root pairings.

            Vertex \(v\) carries \(q(r_v)\) as a loop label and the edge
            \(vw\) carries \(b(r_v,r_w)\), for every pair that pairs nonzero.
            This is the exact integral datum the Coxeter matrix summarizes: the
            Coxeter bond is recovered from \(4b(r_v,r_w)^2/q(r_v)q(r_w)\), and
            the pairings themselves separate diagrams the bonds identify.
            """
            gram = self.root_gram_tensor()
            graph = Graph(multiedges=False, loops=True)
            graph.add_vertices(tuple(self.index_set()))
            for position, vertex in enumerate(self.index_set()):
                graph.add_edge(vertex, vertex, gram[position, position])
            for (i, left), (j, right) in combinations(enumerate(self.index_set()), 2):
                if gram[i, j] != 0:
                    graph.add_edge(left, right, gram[i, j])
            return graph

        def _root_pair_discriminant(self, left, right):
            r"""Return \(b(r_v,r_w)^2-q(r_v)q(r_w)\) for the two vertices."""
            gram = self.root_gram_tensor()
            ranking = self.index_set().ranking_map()
            i = ranking(left)
            j = ranking(right)
            return gram[i, j] ** 2 - gram[i, i] * gram[j, j]

        def mirrors_are_parallel(self, left, right) -> bool:
            r"""Return whether the two mirrors are parallel.

            Two mirrors of a hyperbolic reflection group either meet, are
            parallel (they meet at one point of the boundary), or diverge
            (Vinberg, *Hyperbolic reflection groups*, §1).  The rank-two form
            on \(\langle r_v,r_w\rangle\) decides which: it is definite when
            they meet, degenerate when they are parallel, and indefinite
            nondegenerate when they diverge, so the discriminant
            \(b(r_v,r_w)^2-q(r_v)q(r_w)\) is the whole test.  The Coxeter
            matrix cannot make this distinction, collapsing both open cases to
            \(m=\infty\).
            """
            return self._root_pair_discriminant(left, right) == 0

        def mirrors_are_divergent(self, left, right) -> bool:
            r"""Return whether the two mirrors diverge (are ultraparallel).

            The complementary open case of :meth:`mirrors_are_parallel`:
            \(b(r_v,r_w)^2>q(r_v)q(r_w)\), so the rank-two form is indefinite
            and the mirrors have a common perpendicular rather than a common
            boundary point.
            """
            return self._root_pair_discriminant(left, right) > 0

        def _repr_(self):
            rooted = "rooted " if self.is_rooted() else ""
            return f"{rooted}Coxeter diagram on {self.cardinality()} vertices"

    def from_coxeter_matrix(self, coxeter_matrix, names=None, positions=None):
        if isinstance(coxeter_matrix, (list, tuple)):
            entries = tuple(tuple(row) for row in coxeter_matrix)
            coxeter_matrix = CoxeterMatrix(
                entries,
                index_set=tuple(position for position, _row in enumerate(entries)),
            )
        return _coxeter_diagram(coxeter_matrix, names=names, positions=positions)

    def from_cartan_type(self, cartan_type, names=None, *, rooted=False, scale=None, positions=None):
        cartan_type = CartanType(_engine_cartan_type_data(cartan_type))
        if scale is not None:
            scale = _own_ring(SageZZ)(scale)
            if scale < 1:
                raise ValueError(
                    f"cannot scale the root lattice of type {cartan_type} by {scale}: the scale "
                    f"must be a positive integer"
                )
            rooted = True
        if not rooted:
            return _coxeter_diagram(CoxeterMatrix(cartan_type), names=names, positions=positions)

        if str(cartan_type[0]) == "H":
            lattice = Lattices.root_lattice("H", int(cartan_type[1]))
            if scale is not None and scale != 1:
                lattice = lattice.twist(scale)
            roots = tuple(lattice.module_generators())
            mirrors = finite_ordered_set(tuple(CoxeterMatrix(cartan_type).index_set()))
            gram = tensor(
                lattice.base_ring(),
                (),
                (mirrors.cardinality(), mirrors.cardinality()),
                [[left.b(right) for right in roots] for left in roots],
            )
            return _coxeter_diagram(
                CoxeterMatrix(cartan_type),
                names=names,
                roots=roots,
                root_gram=gram,
                positions=positions,
            )
        lattice = Lattices(_own_ring(SageZZ))(cartan_type)
        if scale is not None and scale != 1:
            lattice = lattice.twist(scale)
        return self.from_roots(tuple(lattice.module_generators()), names=names, positions=positions)

    def from_roots(self, roots, names=None, index_set=None, positions=None):
        roots = tuple(roots)
        if not roots:
            raise ValueError(
                "cannot form a Coxeter diagram from roots: no roots were given, and the "
                "diagram needs at least one to determine its lattice"
            )
        realization = roots[0].parent()
        if any(root.parent() is not realization for root in roots):
            raise ValueError(
                f"the roots {roots} do not all lie in one lattice: the first lies in "
                f"{realization}, and a Coxeter diagram of roots needs a single lattice"
            )
        # The roots carry their own enumeration; the vertices are indexed by it
        # unless the caller names them otherwise.
        root_positions = finite_ordered_set(
            tuple(position for position, _root in enumerate(roots))
        )
        mirrors = root_positions if index_set is None else finite_ordered_set(index_set)
        if mirrors.cardinality() != root_positions.cardinality():
            raise ValueError(
                f"the index set {index_set} does not label the {len(roots)} roots: it has "
                f"{mirrors.cardinality()} elements, and there must be one per root"
            )
        gram = tensor(
            realization.base_ring(),
            (),
            (mirrors.cardinality(), mirrors.cardinality()),
            [[left.b(right) for right in roots] for left in roots],
        )
        entries = [
            [
                SageZZ.one()
                if i == j
                else _coxeter_entry(gram[i, i], gram[j, j], gram[i, j])
                for j, _right in enumerate(roots)
            ]
            for i, _left in enumerate(roots)
        ]
        return _coxeter_diagram(
            CoxeterMatrix(entries, index_set=tuple(mirrors)),
            names=names,
            roots=roots,
            root_gram=gram,
            positions=positions,
        )




__all__ = ["CoxeterDiagrams"]


def _coxeter_diagram(coxeter_matrix, **data):
    r"""Return the diagram its category generates from this matrix."""
    return _object_of(CoxeterDiagrams(), coxeter_matrix=coxeter_matrix, **data)
