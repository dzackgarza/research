r"""Vinberg invariant matrices: the projective invariant of a family of mirrors.

For two non-isotropic vectors \(r,s\) of a formed module the **Vinberg
invariant** is

.. MATH::

    t(r,s) \;=\; \bigl[\,4\,b(r,s)^2 \;:\; q(r)\,q(s)\,\bigr] \;\in\; \mathbb P^1(R),

the projective point of the pair.  Rescaling either vector multiplies
numerator and denominator by the same square, so \(t\) depends on the two
mirrors and not on the normals chosen for them; that invariance is why it is
Vinberg's invariant, and it is why the value is a point of the projective line
rather than an element of \(R\).  Over \(\mathbb Z\) the ratio
\(4b(r,s)^2/q(r)q(s)\) is usually not an integer, so no matrix over the base
ring can hold these values while a matrix of projective points can.

Dehomogenized, \(t = 4\cos^2(\pi/m)\) for the angle \(\pi/m\) between the
mirrors, so the crystallographic bonds are the integers

======  ===  ===  ===  ===  ==========
\(m\)   2    3    4    6    \(\infty\)
\(t\)   0    1    2    3    \(\geq 4\)
======  ===  ===  ===  ===  ==========

and the invariant matrix carries strictly more than the Coxeter matrix: at
\(t \geq 4\) the Coxeter bond is \(\infty\) either way, while \(t = 4\)
says the mirrors are parallel and \(t > 4\) says they diverge.

Sources.  Vinberg, *Hyperbolic reflection groups*, Russian Math. Surveys 40
(1985), sections 1 and 4, for the invariant, the classification of a pair of
mirrors, and the Lannér and quasi-Lannér conditions; Lannér, *On complexes
with transitive groups of automorphisms* (1950), for the cocompact simplex
groups; Bourbaki, *Groupes et algebres de Lie* VI.1.1 for crystallographic
Coxeter bonds.
"""

from itertools import combinations

from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.qqbar import AA, QQbar

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.coxeter_diagrams import CoxeterDiagrams
from dzack_research.preamble.categories.graph_categories import (
    LabelledDigraphs,
    LabelledGraphs,
)
from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    OrderedEnumeratedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.set_categories import NN
from dzack_research.preamble.owned_category import _object_of


def _projective_line_over(base_ring):
    r"""Return the owned projective line over the invariant coefficient ring."""
    from dzack_research.preamble.categories.schemes.schemes import ProjectiveSpaces

    return ProjectiveSpaces(base_ring)(1)


class ProjectiveWeightedGraphs(OwnedCategoryOverBaseRing):
    r"""Finite graphs or digraphs with exact projective vertex and edge weights.

    Every undirected instance is read through its symmetric directed adjacency,
    so the common immediate owner of the mixed directed/undirected category is
    ``LabelledDigraphs``.
    """

    @classmethod
    def _repr_object_names(cls):
        return "projectively weighted graphs"

    def an_object(self):
        return VinbergInvariantMatrices().from_coxeter_diagram(
            CoxeterDiagrams().from_cartan_type(["A", 2])
        ).weighted_graph()

    def super_categories(self):
        return [LabelledDigraphs()]

    def from_weights(
        self,
        vertices,
        edge_weights,
        *,
        vertex_weights=None,
        directed=False,
        symmetric=False,
    ):
        r"""Return the represented projectively weighted graph on ``vertices``."""
        base_ring = self.base_ring()
        vertices = finite_ordered_set(vertices)
        edge_space = vertices**2
        projective_line = _projective_line_over(base_ring)
        normalized_edges = {
            edge_space(edge): projective_line(weight)
            for edge, weight in dict(edge_weights).items()
        }
        if any(
            edge[0] not in vertices or edge[1] not in vertices
            for edge in normalized_edges
        ):
            raise ValueError(
                f"the weighted edges {tuple(normalized_edges)} are not edges of a graph on "
                f"the vertices {vertices}: some edge has an endpoint that is not a vertex"
            )
        if vertex_weights is None:
            normalized_vertices = {
                vertex: projective_line([1, 1]) for vertex in vertices
            }
        else:
            normalized_vertices = {
                vertex: projective_line(weight)
                for vertex, weight in dict(vertex_weights).items()
            }
        if set(normalized_vertices) != set(vertices):
            raise ValueError(
                f"a weighted graph on the vertices {vertices} needs exactly one weight per "
                f"vertex, but weights were given for {tuple(normalized_vertices)}"
            )
        if symmetric:
            for left, right in normalized_edges:
                reverse = edge_space((right, left))
                if reverse in normalized_edges:
                    if normalized_edges[edge_space((left, right))] != normalized_edges[reverse]:
                        raise ValueError(
                            f"the weighting is not symmetric: the edge ({left}, {right}) has "
                            f"weight {normalized_edges[edge_space((left, right))]}, but the "
                            f"reverse edge has weight {normalized_edges[reverse]}"
                        )
        return _object_of(
            self,
            base_ring=base_ring,
            vertices=tuple(vertices),
            edge_weights=normalized_edges,
            vertex_weights=normalized_vertices,
            directed=directed,
            symmetric=symmetric,
        )

    class ParentMethods:
        def __init__(
            self,
            base_ring,
            vertices,
            edge_weights,
            vertex_weights,
            directed,
            symmetric,
            **rest,
        ) -> None:
            self._base_ring = base_ring
            self._vertices = finite_ordered_set(vertices)
            self._edge_space = self._vertices**2
            self._edge_weights = dict(edge_weights)
            self._vertex_weights = dict(vertex_weights)
            self._directed = bool(directed)
            self._symmetric = bool(symmetric)
            self._projective_line = _projective_line_over(base_ring)
            super().__init__(**rest)

        def base_ring(self):
            return self._base_ring

        def vertices(self):
            return self._vertices

        def __contains__(self, vertex) -> bool:
            return vertex in self.vertices()

        is_parent_of = __contains__

        def _element_constructor_(self, vertex):
            return self.vertices()(vertex)

        def __iter__(self):
            return iter(self.vertices())

        def cardinality(self):
            return self._vertices.cardinality()

        def is_directed(self) -> bool:
            return self._directed

        def is_symmetric(self) -> bool:
            return self._symmetric

        def projective_line(self):
            return self._projective_line

        def vertex_weight(self, vertex):
            if vertex not in self._vertices:
                raise ValueError(
                    f"{vertex} has no weight in {self}: it is not one of the vertices "
                    f"{self._vertices}"
                )
            return self._vertex_weights[vertex]

        vertex_label = vertex_weight

        def has_edge(self, left, right) -> bool:
            edge = self._edge_space((left, right))
            reverse = self._edge_space((right, left))
            if edge in self._edge_weights:
                return True
            if self._symmetric and reverse in self._edge_weights:
                return True
            return False

        def edge_weight(self, left, right):
            edge = self._edge_space((left, right))
            reverse = self._edge_space((right, left))
            if edge in self._edge_weights:
                return self._edge_weights[edge]
            if self._symmetric and reverse in self._edge_weights:
                return self._edge_weights[reverse]
            raise ValueError(
                f"the pair ({left}, {right}) has no edge weight in {self}: the vertices are "
                f"not joined by an edge"
            )

        edge_label = edge_weight

        def edges(self):
            return finite_ordered_set(tuple(self._edge_weights))

        def num_edges(self):
            return self.edges().cardinality()

        def induced_subgraph(self, vertices):
            r"""Return the projectively weighted subgraph on ``vertices``.

            The selected labels remain the vertex set; every retained vertex
            and every edge with both endpoints selected keeps its exact point
            of ``P^1``.  This is an induced subgraph, so no new edge is inferred
            from the ambient graph.
            """
            selected = finite_ordered_set(tuple(vertices))
            if any(vertex not in self._vertices for vertex in selected):
                raise ValueError(
                    f"cannot form the subgraph of {self} induced on {selected}: some of these "
                    f"are not vertices of the graph, whose vertices are {self._vertices}"
                )
            edge_weights = {
                tuple(edge): weight
                for edge, weight in self._edge_weights.items()
                for left, right in (tuple(edge),)
                if left in selected and right in selected
            }
            vertex_weights = {
                vertex: self.vertex_weight(vertex) for vertex in selected
            }
            return ProjectiveWeightedGraphs(self.base_ring()).from_weights(
                tuple(selected),
                edge_weights,
                vertex_weights=vertex_weights,
                directed=self.is_directed(),
                symmetric=self.is_symmetric(),
            )

        subgraph = induced_subgraph
        subdiagram = induced_subgraph

        def vinberg_invariant_matrix(self):
            r"""Reconstruct the symmetric Vinberg matrix represented by this graph.

            A Vinberg graph omits exactly the orthogonal pairs, whose invariant
            is the projective point ``[0:1]``.  Vertex weights supply the
            diagonal.  Thus a symmetric projectively weighted graph determines
            one projective invariant matrix.  An asymmetric/directed graph is
            more general data and is deliberately not coerced into a symmetric
            reflection arrangement.
            """
            if self.is_directed() or not self.is_symmetric():
                raise ValueError(
                    f"{self} does not determine a Vinberg invariant matrix: the matrix is "
                    f"symmetric, so the graph must be undirected with symmetric weights"
                )
            vertices = tuple(self.vertices())
            ring = self.base_ring()
            numerators = []
            denominators = []
            for left in vertices:
                numerator_row = []
                denominator_row = []
                for right in vertices:
                    if left == right:
                        weight = self.vertex_weight(left)
                    elif self.has_edge(left, right):
                        weight = self.edge_weight(left, right)
                    else:
                        weight = self.projective_line()([ring.zero(), ring.one()])
                    numerator_row.append(ring(weight[0]))
                    denominator_row.append(ring(weight[1]))
                numerators.append(numerator_row)
                denominators.append(denominator_row)
            return _vinberg_invariant_matrix(
                ring,
                vertices,
                numerators,
                denominators,
            )

        def projectivization(self):
            r"""Return this graph: its weights already lie in ``P^1``."""
            return self

        def _repr_(self):
            if self._directed:
                orientation = "digraph"
            else:
                orientation = "graph"
            return f"Projectively weighted {orientation} on {self.cardinality()} vertices"
def _reflection_cosine(index):
    r"""Return \(\cos(\pi/n)\) as an exact algebraic real."""
    index = SageZZ(index)
    assert index >= 1, f"a reflection cosine is indexed by an integer n >= 1; got {index}"
    if index == 1:
        return AA(-1)
    if index == 2:
        return AA.zero()
    root_of_unity = QQbar.zeta(2 * index)
    return AA((root_of_unity + root_of_unity**-1) / 2)


def _reflection_cosine_index(cosine):
    r"""Return the \(n\) with ``cosine`` \(=\cos(\pi/n)\), or ``None``.

    Exact, and without enumeration: for \(x\in[-1,1)\) put
    \(\zeta = x + i\sqrt{1-x^2}\), a point of the unit circle in
    \(\overline{\mathbb Q}\).  Then \(x=\cos(\pi/n)\) exactly when \(\zeta\) is
    a primitive \(2n\)-th root of unity, which is to say that \(\zeta\) has
    finite multiplicative order \(2n\) and \(\zeta^n=-1\).  Anything of
    infinite order, or of odd order, or with \(\zeta^n=+1\), is not a
    reflection cosine.
    """
    value = QQbar(cosine)
    if value == -1:
        return SageZZ.one()
    if value <= -1 or value >= 1:
        return None
    root_of_unity = value + QQbar.gen() * QQbar(1 - value**2).sqrt()
    order = root_of_unity.multiplicative_order()
    if order is Infinity or order % 2 != 0:
        return None
    index = SageZZ(order // 2)
    return index if root_of_unity**index == -1 else None


def _reflection_cosine_position(cosine):
    r"""Return the position of ``cosine`` in the enumeration, or ``None``.

    Position \(k\) carries \(n=k+1\), which is the one step between \(\omega\)
    and the positive integers that index the cosines.
    """
    index = _reflection_cosine_index(cosine)
    return None if index is None else NN(index - 1)


def reflection_cosines():
    r"""Return \(X_{\mathrm{ref}}=\{\cos(\pi/n) : n\in\mathbb Z_{\geq 1}\}\).

    The values a Coxeter bond can take as a cosine, as an owned set: countably
    infinite, enumerated by \(n\), and with exact membership through
    :func:`_reflection_cosine_index`.  Position \(k\) of the enumeration
    carries \(n=k+1\): the index set is \(\omega\) and the cosines start at
    \(n=1\).

    Membership is decided in \(\overline{\mathbb Q}\) and never by rounding,
    so \(1/2\) and \((1+\sqrt 5)/4\) belong, being \(\cos(\pi/3)\) and
    \(\cos(\pi/5)\), while \(1/3\) does not.
    """
    return OrderedEnumeratedSets()(
        NN,
        lambda position: _reflection_cosine(int(position) + 1),
        index_of=_reflection_cosine_position,
        contains=lambda value: _reflection_cosine_index(value) is not None,
        name="Reflection cosines { cos(pi/n) : n >= 1 }",
    )


def _coxeter_bond(invariant):
    r"""Return the Coxeter bond \(m\) of the Vinberg invariant ``invariant``.

    ``invariant`` is \(t=4\cos^2(\pi/m)\) as an exact rational or algebraic
    real.  Mirrors at \(t\geq 4\) do not meet inside hyperbolic space, so the
    bond is \(\infty\); otherwise \(\cos(\pi/m)=\sqrt t/2\) and the bond is the
    reflection-cosine index of that value.
    """
    assert invariant >= 0, (
        f"a Vinberg invariant of two mirrors is a square ratio and is never "
        f"negative; got {invariant}"
    )
    if invariant >= 4:
        return Infinity
    index = _reflection_cosine_index(AA(invariant).sqrt() / 2)
    assert index is not None, (
        f"the Vinberg invariant {invariant} is not 4 cos^2(pi/m) for any "
        f"integer m, so this pair of mirrors has no Coxeter bond"
    )
    return index


class VinbergInvariantMatrices(OwnedCategory):
    r"""Symmetric matrices of Vinberg invariants on a finite set of mirrors.

    The entries are points ``[4 b(r,s)^2 : q(r)q(s)]`` of a projective line,
    not scalars of the coefficient ring, so this is not an object of
    ``MatrixSpaces(R)``.  The same data is exactly the symmetric labelled graph
    whose non-orthogonal pairs are edges and whose projective invariants are
    vertex and edge labels; that is the immediate owned placement used here.
    """

    def an_object(self):
        r"""The invariant matrix of the \(A_2\) diagram."""
        return self.from_coxeter_diagram(CoxeterDiagrams().from_cartan_type(["A", 2]))

    @classmethod
    def _repr_object_names(cls):
        return "Vinberg invariant matrices"

    def super_categories(self):
        return [LabelledGraphs()]

    class ParentMethods:
        def __init__(self, base_ring, index_set, numerators, denominators, **rest) -> None:
            self._base_ring = base_ring
            self._index_set = finite_ordered_set(index_set)
            self._numerators = numerators
            self._denominators = denominators
            self._projective_line = _projective_line_over(base_ring)
            super().__init__(**rest)

        def base_ring(self):
            return self._base_ring

        def index_set(self):
            r"""Return the ordered set of mirrors this matrix is indexed by."""
            return self._index_set

        def vertices(self):
            return self.index_set()

        def __contains__(self, mirror) -> bool:
            return mirror in self.index_set()

        is_parent_of = __contains__

        def _element_constructor_(self, mirror):
            return self.index_set()(mirror)

        def __iter__(self):
            return iter(self.index_set())

        def has_edge(self, left, right) -> bool:
            return left != right and self.vinberg_ratio(left, right) != 0

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
            return self.vinberg_invariant(vertex, vertex)

        def edge_label(self, left, right):
            if not self.has_edge(left, right):
                raise ValueError(
                    f"the mirrors {left} and {right} of {self} are orthogonal, so they are "
                    f"not joined by an edge of the Vinberg diagram and the edge has no label"
                )
            return self.vinberg_invariant(left, right)

        def cardinality(self):
            return self._index_set.cardinality()

        def projective_line(self):
            r"""Return \(\mathbb P^1(R)\), where the invariants take their values."""
            return self._projective_line

        def _positions(self, left, right):
            ranking = self._index_set.ranking_map()
            return ranking(left), ranking(right)

        def vinberg_invariant(self, left, right):
            r"""Return \([4b(r,s)^2 : q(r)q(s)]\in\mathbb P^1(R)\) for the two mirrors.

            The diagonal entry is \([4:1]\), the invariant of a mirror with
            itself: \(m_{vv}=1\) and \(4\cos^2\pi=4\).
            """
            i, j = self._positions(left, right)
            return self._projective_line(
                [self._numerators[i][j], self._denominators[i][j]]
            )

        def vinberg_ratio(self, left, right):
            r"""Return the dehomogenized invariant \(t=4\cos^2(\pi/m)\).

            The denominator is \(q(r)q(s)\), which is nonzero because the
            normals of mirrors are non-isotropic, so the projective point of
            :meth:`vinberg_invariant` always has an affine representative.
            """
            i, j = self._positions(left, right)
            denominator = self._denominators[i][j]
            assert denominator != 0, (
                f"the Vinberg invariant of the mirrors {left} and {right} in {self} has "
                f"denominator q(r)q(s) = 0, so one of their normals is isotropic and is "
                f"not the normal of a mirror"
            )
            return self._numerators[i][j] / denominator

        def coxeter_entry(self, left, right):
            r"""Return the Coxeter bond \(m\) between the two mirrors.

            This is the conversion to Coxeter data, and it is partial: an
            invariant that is not \(4\cos^2(\pi/m)\) for an integer \(m\) names
            a pair of mirrors at an angle no Coxeter matrix can record, and the
            conversion refuses rather than rounding to a nearby bond.
            """
            if left == right:
                return SageZZ.one()
            return _coxeter_bond(self.vinberg_ratio(left, right))

        def coxeter_matrix(self):
            r"""Return the Coxeter matrix this invariant matrix determines."""
            from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix

            vertices = tuple(self._index_set)
            bonds = [
                [self.coxeter_entry(left, right) for right in vertices]
                for left in vertices
            ]
            # Sage writes an infinite Coxeter bond as the matrix entry -1.
            entries = [
                [-1 if bond is Infinity else bond for bond in row] for row in bonds
            ]
            return CoxeterMatrix(entries, index_set=vertices)

        def coxeter_diagram(self):
            r"""Return the Coxeter diagram of this invariant matrix.

            The passage forgets exactly the distinction between parallel and
            divergent mirrors, both of which the Coxeter matrix writes as
            \(m=\infty\).
            """
            return CoxeterDiagrams().from_coxeter_matrix(self.coxeter_matrix())

        def submatrix(self, mirrors):
            r"""Return the invariant matrix on the selected mirrors."""
            vertices = tuple(mirrors)
            ranking = self._index_set.ranking_map()
            positions = tuple(ranking(vertex) for vertex in vertices)
            return _vinberg_invariant_matrix(
                self._base_ring,
                vertices,
                [[self._numerators[i][j] for j in positions] for i in positions],
                [[self._denominators[i][j] for j in positions] for i in positions],
            )

        def weighted_graph(self):
            r"""Return the projectively weighted graph of mirrors.

            An edge joins two mirrors whose invariant is nonzero, that is,
            every pair that is not orthogonal, and it carries the projective
            invariant of that pair as its exact weight.  The diagonal Vinberg
            invariant is retained as the vertex weight.
            """
            vertices = tuple(self._index_set)
            edge_weights = {}
            for left, right in combinations(vertices, 2):
                if self.vinberg_ratio(left, right) == 0:
                    continue
                i, j = self._positions(left, right)
                edge_weights[left, right] = (
                    self._numerators[i][j],
                    self._denominators[i][j],
                )
            vertex_weights = {}
            for vertex in vertices:
                i, _j = self._positions(vertex, vertex)
                vertex_weights[vertex] = (
                    self._numerators[i][i],
                    self._denominators[i][i],
                )
            return ProjectiveWeightedGraphs(self._base_ring).from_weights(
                vertices,
                edge_weights,
                vertex_weights=vertex_weights,
                directed=False,
                symmetric=True,
            )

        def is_crystallographic(self) -> bool:
            r"""Return whether every bond is \(2, 3, 4, 6\) or \(\infty\).

            The crystallographic restriction (Bourbaki VI.1.1): those are the
            bonds a reflection group preserving a lattice can realize, and in
            invariants they are \(t\in\{0,1,2,3\}\) together with \(t\geq 4\).
            """
            for left, right in combinations(self._index_set, 2):
                ratio = self.vinberg_ratio(left, right)
                if ratio < 4 and ratio not in (0, 1, 2, 3):
                    return False
            return True

        def is_simply_laced(self) -> bool:
            r"""Return whether every bond is \(2\) or \(3\).

            Equivalently every invariant is \(0\) or \(1\): all mirrors meet at
            right angles or at \(\pi/3\), which is the condition under which
            every root has the same square.
            """
            for left, right in combinations(self._index_set, 2):
                if self.vinberg_ratio(left, right) not in (0, 1):
                    return False
            return True

        def _vertex_deleted_diagrams(self):
            r"""Return the subdiagrams obtained by deleting one mirror."""
            diagram = self.coxeter_diagram()
            vertices = tuple(diagram.index_set())
            return finite_ordered_set(
                tuple(
                    diagram.induced_subdiagram(
                        tuple(other for other in vertices if other != vertex)
                    )
                    for vertex in vertices
                )
            )

        def is_elliptic(self) -> bool:
            r"""Return whether the Schlaefli form is positive definite."""
            return self.coxeter_diagram().is_elliptic()

        def is_parabolic(self) -> bool:
            r"""Return whether the Schlaefli form is positive semidefinite of corank one."""
            return self.coxeter_diagram().is_parabolic()

        def is_hyperbolic(self) -> bool:
            r"""Return whether the Schlaefli form has negative index of inertia one."""
            return self.coxeter_diagram().is_hyperbolic()

        def is_compact_hyperbolic(self) -> bool:
            r"""Return whether this is a Lannér diagram.

            Lannér's condition (Lannér 1950; Vinberg, *Hyperbolic reflection
            groups*, section 4): the diagram is hyperbolic and every proper
            subdiagram is elliptic.  Such a diagram is the diagram of a compact
            hyperbolic simplex, and its reflection group is cocompact.

            Deleting one mirror suffices to test it: a principal submatrix of a
            positive definite matrix is positive definite, so if every
            vertex-deleted subdiagram is elliptic then so is every smaller one.
            """
            if not self.is_hyperbolic():
                return False
            return all(
                subdiagram.is_elliptic()
                for subdiagram in self._vertex_deleted_diagrams()
            )

        def is_paracompact_hyperbolic(self) -> bool:
            r"""Return whether this is a quasi-Lannér diagram.

            Vinberg's condition (*Hyperbolic reflection groups*, section 4):
            the diagram is hyperbolic, every proper subdiagram has positive
            semidefinite Schlaefli form, and at least one of them is
            degenerate.  Such a diagram is the diagram of a hyperbolic simplex
            of finite volume with at least one ideal vertex, so its reflection
            group has finite covolume but is not cocompact.

            The degeneracy is stated on the index of inertia and not through
            parabolicity, because a proper subdiagram may be a direct sum of
            several affine components and so have a radical of dimension
            greater than one.
            """
            if not self.is_hyperbolic():
                return False
            deleted = self._vertex_deleted_diagrams()
            if any(subdiagram.negative_inertia_index() != 0 for subdiagram in deleted):
                return False
            return any(subdiagram.zero_inertia_index() != 0 for subdiagram in deleted)

        def _repr_(self):
            return f"Vinberg invariant matrix on {self.cardinality()} mirrors"

    def from_root_gram(self, gram, index_set=None):
        r"""Return the invariant matrix of a Gram of mirror normals.

        The numerators are \(4b(r_v,r_w)^2\) and the denominators are
        \(q(r_v)q(r_w)\), so the entries are the projective invariants of the
        pairs of mirrors and nothing is divided.
        """
        rank = gram.tensor_shape()[0]
        if index_set is None:
            index_set = range(rank)
        squares = [gram[i, i] for i in range(rank)]
        assert all(square != 0 for square in squares), (
            f"the Gram matrix {gram} is not the Gram matrix of the normals of a family of "
            f"mirrors: its diagonal {tuple(squares)} has a zero, and the normal of a "
            f"mirror is not isotropic"
        )
        return _vinberg_invariant_matrix(
            gram.base_ring(),
            tuple(index_set),
            [[4 * gram[i, j] ** 2 for j in range(rank)] for i in range(rank)],
            [[squares[i] * squares[j] for j in range(rank)] for i in range(rank)],
        )

    def from_coxeter_diagram(self, diagram):
        r"""Return the invariant matrix of a Coxeter diagram.

        A rooted diagram supplies its root Gram, which is the exact integral
        datum and separates parallel mirrors from divergent ones.  An unrooted
        diagram supplies only its bonds, and the invariants are then the
        algebraic numbers \(4\cos^2(\pi/m)\), with the two open cases
        collapsed onto the single value \(4\).
        """
        if diagram.is_rooted():
            return self.from_root_gram(
                diagram.root_gram_tensor(), index_set=tuple(diagram.index_set())
            )
        vertices = tuple(diagram.index_set())
        values = [
            [_vinberg_invariant_of_bond(diagram.coxeter_entry(left, right)) for right in vertices]
            for left in vertices
        ]
        return _vinberg_invariant_matrix(
            AA,
            vertices,
            values,
            [[AA.one() for _ in vertices] for _ in vertices],
        )

    def from_invariants(self, base_ring, values, index_set=None):
        r"""Return the invariant matrix with the stated dehomogenized invariants.

        The combinatorial presentation: the caller states \(t_{vw}\) directly,
        with no mirrors behind it.  The denominators are all one, which is what
        makes these values themselves the projective points.
        """
        rows = tuple(tuple(row) for row in values)
        # The rows carry their own enumeration; the mirrors are indexed by it
        # unless the caller names them otherwise.
        row_positions = finite_ordered_set(
            tuple(position for position, _row in enumerate(rows))
        )
        mirrors = row_positions if index_set is None else finite_ordered_set(index_set)
        assert mirrors.cardinality() == row_positions.cardinality(), (
            f"the mirrors {mirrors} cannot index the invariant matrix: there are "
            f"{mirrors.cardinality()} of them, but the matrix has "
            f"{row_positions.cardinality()} rows"
        )
        return _vinberg_invariant_matrix(
            base_ring,
            tuple(mirrors),
            [[base_ring(entry) for entry in row] for row in rows],
            [[base_ring.one() for _ in mirrors] for _ in mirrors],
        )


def _vinberg_invariant_of_bond(bond):
    r"""Return \(t=4\cos^2(\pi/m)\) for a Coxeter bond ``m``.

    At \(m=\infty\) the mirrors are parallel, \(\cos 0 = 1\), and \(t=4\).
    That is the smallest value at which the mirrors fail to meet, so the
    unrooted diagram records the parallel case and cannot record divergence.
    """
    if bond is Infinity or bond == -1:
        return AA(4)
    return 4 * _reflection_cosine(bond) ** 2


def _vinberg_invariant_matrix(base_ring, index_set, numerators, denominators):
    return _object_of(
        VinbergInvariantMatrices(),
        base_ring=base_ring,
        index_set=index_set,
        numerators=numerators,
        denominators=denominators,
    )


__all__ = [
    "ProjectiveWeightedGraphs",
    "VinbergInvariantMatrices",
    "reflection_cosines",
]
