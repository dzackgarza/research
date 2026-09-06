r"""Finite Coxeter diagrams, optionally rooted in an integral lattice."""

from sage.categories.category import Category
from sage.combinat.posets.posets import Poset
from sage.combinat.root_system.cartan_type import CartanType
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
from sage.graphs.graph import Graph
from sage.matrix.constructor import matrix as engine_matrix
from sage.misc.cachefunc import cached_method
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.tensors.tensor import tensor
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _engine_element, _own_ring
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.tensors.tensor import _engine_component_matrix


def _coxeter_entry(q1, q2, pairing):
    integers = _own_ring(SageZZ)
    q1 = _engine_element(integers, q1)
    q2 = _engine_element(integers, q2)
    pairing = _engine_element(integers, pairing)
    if q1 == 0 or q2 == 0:
        raise ValueError("a Coxeter root has nonzero square")
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
    raise ValueError(f"the root pair does not determine a crystallographic Coxeter angle: 4 cos^2(pi/m) = {four_cos_squared}")


class CoxeterDiagrams(OwnedCategory):
    r"""Finite Coxeter diagrams: a symmetric matrix of vertex angles."""

    def an_object(self):
        r"""The diagram of ``A_2``: two vertices joined by an edge of order 3."""
        return self.from_cartan_type(["A", 2])

    @classmethod
    def _repr_object_names(cls):
        return "Coxeter diagrams"

    def super_categories(self):
        return [Sets()]

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
                names = tuple(f"s_{index}" for index in self._index_set)
            elif isinstance(names, str):
                names = tuple(part.strip() for part in names.split(","))
            else:
                names = tuple(names)
            if len(names) != len(self._index_set):
                raise ValueError("a Coxeter diagram needs one name per vertex")
            self._names = names
            self._roots = None if roots is None else tuple(roots)
            self._root_gram = root_gram
            if positions is None:
                self._preferred_positions = None
            else:
                if set(positions) != set(self._index_set):
                    raise ValueError("positions need one coordinate pair for every vertex")
                if any(len(coordinates) != 2 for coordinates in positions.values()):
                    raise ValueError("every diagram position must be a coordinate pair")
                self._preferred_positions = {vertex: (coordinates[0], coordinates[1]) for vertex, coordinates in positions.items()}
            self._computed_positions = None
            super().__init__(**rest)

        def index_set(self):
            return self._index_set

        def cardinality(self):
            return self._index_set.cardinality()

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
                raise ValueError("this Coxeter diagram has no selected root realization")
            return self._roots

        def root_gram_tensor(self):
            if self._root_gram is None:
                raise ValueError("this Coxeter diagram has no selected root realization")
            return self._root_gram

        def preferred_positions(self):
            r"""Return stored presentation coordinates, or a computed graph layout."""
            if self._preferred_positions is not None:
                return dict(self._preferred_positions)
            if self._computed_positions is None:
                layout = self.graph().layout()
                self._computed_positions = {vertex: (coordinates[0], coordinates[1]) for vertex, coordinates in layout.items()}
            return dict(self._computed_positions)

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
            vertices = tuple(self.index_set())
            for i, left in enumerate(vertices):
                for j in range(i + 1, len(vertices)):
                    right = vertices[j]
                    m = self.coxeter_entry(left, right)
                    if m != 2:
                        graph.add_edge(left, right, m)
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
                raise ValueError("an induced subdiagram uses vertices of this diagram")
            matrix_ = self.coxeter_matrix()
            entries = [[matrix_[left, right] for right in vertices] for left in vertices]
            names = tuple(self._names[self.index_set().position(vertex)] for vertex in vertices)
            preferred_positions = None if self._preferred_positions is None else {vertex: self._preferred_positions[vertex] for vertex in vertices}
            if self.is_rooted():
                positions = tuple(self.index_set().position(vertex) for vertex in vertices)
                roots = tuple(self._roots[position] for position in positions)
                gram = tensor(
                    self._root_gram.base_ring(),
                    (),
                    (len(positions), len(positions)),
                    [
                        [self._root_gram[i, j] for j in positions]
                        for i in positions
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
            r"""Return the normalized reflection Gram tensor ``S_ii=1``."""
            from sage.all import AA, cos, pi

            vertices = tuple(self.index_set())
            values = []
            for left in vertices:
                row = []
                for right in vertices:
                    if left == right:
                        row.append(AA.one())
                        continue
                    m = self.coxeter_entry(left, right)
                    if m == Infinity:
                        row.append(-AA.one())
                    else:
                        row.append(-AA(cos(pi / m)))
                values.append(row)
            return tensor(AA, (), (len(vertices), len(vertices)), values)

        def _inertia_counts(self):
            r"""Return \((n_+,n_-,n_0)\) of the Schlaefli form, by Sylvester.

            The Coxeter diagram is classified by the inertia of its Schlaefli
            form, and that form is allowed to be degenerate, so the zero index
            \(n_0\) is part of the answer.  This is not a signature *pair*.
            """

            eigenvalues = _engine_component_matrix(self.schlafli_tensor()).eigenvalues()
            positive = sum(1 for value in eigenvalues if value > 0)
            negative = sum(1 for value in eigenvalues if value < 0)
            zero = len(eigenvalues) - positive - negative
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
            from itertools import combinations

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

        @cached_method
        def _bond_preserving_permutation_group(self):
            r"""Return the engine automorphism group of the labelled Coxeter graph.

            An automorphism permutes the vertices and preserves every bond
            \(m_{vw}\); on a rooted diagram it preserves the root squares too,
            which enters as the vertex partition by square.
            """
            graph = self.graph()
            if not self.is_rooted():
                return graph.automorphism_group(edge_labels=True)
            by_square = {}
            for position, vertex in enumerate(self.index_set()):
                by_square.setdefault(self._root_gram[position, position], []).append(vertex)
            return graph.automorphism_group(
                partition=[by_square[square] for square in sorted(by_square)],
                edge_labels=True,
            )

        def Aut(self):
            r"""Return the group of diagram automorphisms.

            The automorphisms of the Coxeter graph with its bond labels: for
            \(A_n\) with \(n\geq 2\) the path reversal, of order two; for
            \(D_4\) the symmetric group on the three outer nodes, triality; for
            \(E_8\) trivial.
            """
            from dzack_research.preamble.categories.group.groups import _own_group

            return _own_group(self._bond_preserving_permutation_group())

        def _vertex_set_orbits(self, subdiagrams):
            r"""Return one representative subdiagram per :meth:`Aut`-orbit."""
            group = self._bond_preserving_permutation_group()
            seen = set()
            representatives = []
            for diagram in subdiagrams:
                vertices = tuple(diagram.index_set())
                if frozenset(vertices) in seen:
                    continue
                if vertices:
                    for image in group.orbit(vertices, action="OnSets"):
                        seen.add(frozenset(image))
                else:
                    # The empty vertex set is fixed by every permutation.
                    seen.add(frozenset())
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

        def root_realization(self):
            r"""Return the lattice in which the diagram roots are realized."""
            roots = self.roots()
            assert roots, "the diagram on no vertices realizes no roots"
            return roots[0].parent()

        def root_lattice(self):
            r"""Return the abstract lattice presented by the root Gram.

            One module generator per vertex, paired by the root Gram.  It is
            the domain of :meth:`root_morphism`; the realization is its
            codomain, and the two coincide exactly when the roots generate a
            finite-index sublattice with the same Gram framing.
            """
            gram = self.root_gram_tensor()
            rank = len(tuple(self.index_set()))
            return Lattices(self.root_realization().base_ring())(
                [[gram[i, j] for j in range(rank)] for i in range(rank)]
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

        def root_intersection_graph(self):
            r"""Return the graph of root squares and root pairings.

            Vertex \(v\) carries \(q(r_v)\) as a loop label and the edge
            \(vw\) carries \(b(r_v,r_w)\), for every pair that pairs nonzero.
            This is the exact integral datum the Coxeter matrix summarizes: the
            Coxeter bond is recovered from \(4b(r_v,r_w)^2/q(r_v)q(r_w)\), and
            the pairings themselves separate diagrams the bonds identify.
            """
            gram = self.root_gram_tensor()
            vertices = tuple(self.index_set())
            graph = Graph(multiedges=False, loops=True)
            graph.add_vertices(vertices)
            for i, left in enumerate(vertices):
                graph.add_edge(left, left, gram[i, i])
                for j in range(i + 1, len(vertices)):
                    if gram[i, j] != 0:
                        graph.add_edge(left, vertices[j], gram[i, j])
            return graph

        def _root_pair_discriminant(self, left, right):
            r"""Return \(b(r_v,r_w)^2-q(r_v)q(r_w)\) for the two vertices."""
            gram = self.root_gram_tensor()
            i = self.index_set().position(left)
            j = self.index_set().position(right)
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
            coxeter_matrix = CoxeterMatrix(entries, index_set=tuple(range(len(entries))))
        return _coxeter_diagram(coxeter_matrix, names=names, positions=positions)

    def from_cartan_type(self, cartan_type, names=None, *, rooted=False, positions=None):
        cartan_type = CartanType(cartan_type)
        if not rooted:
            return _coxeter_diagram(CoxeterMatrix(cartan_type), names=names, positions=positions)

        lattice = Lattices(_own_ring(SageZZ))(cartan_type)
        return self.from_roots(tuple(lattice.module_generators()), names=names, positions=positions)

    def from_roots(self, roots, names=None, index_set=None, positions=None):
        roots = tuple(roots)
        if not roots:
            raise ValueError("a rooted Coxeter diagram needs at least one root")
        ambient = roots[0].parent()
        if any(root.parent() is not ambient for root in roots):
            raise ValueError("all diagram roots must belong to one lattice")
        if index_set is None:
            index_set = range(len(roots))
        index_set = finite_ordered_set(index_set)
        if index_set.cardinality() != len(roots):
            raise ValueError("the index set must have one vertex per root")
        gram = tensor(
            ambient.base_ring(),
            (),
            (len(roots), len(roots)),
            [[left.b(right) for right in roots] for left in roots],
        )
        entries = [[SageZZ.one() if i == j else _coxeter_entry(gram[i, i], gram[j, j], gram[i, j]) for j in range(len(roots))] for i in range(len(roots))]
        return _coxeter_diagram(
            CoxeterMatrix(entries, index_set=tuple(index_set)),
            names=names,
            roots=roots,
            root_gram=gram,
            positions=positions,
        )




__all__ = ["CoxeterDiagrams"]


def _coxeter_diagram(coxeter_matrix, **data):
    r"""Return the diagram its category generates from this matrix."""
    return object_of(CoxeterDiagrams(), coxeter_matrix=coxeter_matrix, **data)
