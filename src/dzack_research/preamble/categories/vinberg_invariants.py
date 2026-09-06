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
from sage.schemes.projective.projective_space import ProjectiveSpace
from sage.sets.positive_integers import PositiveIntegers

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.coxeter_diagrams import CoxeterDiagrams
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
    ordered_enumerated_set,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import object_of


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


def reflection_cosines():
    r"""Return \(X_{\mathrm{ref}}=\{\cos(\pi/n) : n\in\mathbb Z_{\geq 1}\}\).

    The values a Coxeter bond can take as a cosine, as an owned set: countably
    infinite, enumerated by \(n\), and with exact membership through
    :func:`_reflection_cosine_index`.  Position \(k\) of the enumeration
    carries \(n=k+1\), since the index set is the positive integers.

    Membership is decided in \(\overline{\mathbb Q}\) and never by rounding,
    so \(1/2\) and \((1+\sqrt 5)/4\) belong, being \(\cos(\pi/3)\) and
    \(\cos(\pi/5)\), while \(1/3\) does not.
    """
    return ordered_enumerated_set(
        PositiveIntegers(),
        _reflection_cosine,
        rank=_reflection_cosine_index,
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
    r"""Symmetric matrices of Vinberg invariants on a finite set of mirrors."""

    def an_object(self):
        r"""The invariant matrix of the \(A_2\) diagram."""
        return self.from_coxeter_diagram(CoxeterDiagrams().from_cartan_type(["A", 2]))

    @classmethod
    def _repr_object_names(cls):
        return "Vinberg invariant matrices"

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def __init__(self, base_ring, index_set, numerators, denominators, **rest) -> None:
            self._base_ring = base_ring
            self._index_set = finite_ordered_set(index_set)
            self._numerators = numerators
            self._denominators = denominators
            self._projective_line = ProjectiveSpace(base_ring, 1)
            super().__init__(**rest)

        def base_ring(self):
            return self._base_ring

        def index_set(self):
            r"""Return the ordered set of mirrors this matrix is indexed by."""
            return self._index_set

        def cardinality(self):
            return self._index_set.cardinality()

        def projective_line(self):
            r"""Return \(\mathbb P^1(R)\), where the invariants take their values."""
            return self._projective_line

        def _positions(self, left, right):
            return self._index_set.position(left), self._index_set.position(right)

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
                "a mirror has a non-isotropic normal, so the Vinberg invariant "
                "of a pair of mirrors has a nonzero denominator"
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
            positions = tuple(self._index_set.position(vertex) for vertex in vertices)
            return _vinberg_invariant_matrix(
                self._base_ring,
                vertices,
                [[self._numerators[i][j] for j in positions] for i in positions],
                [[self._denominators[i][j] for j in positions] for i in positions],
            )

        def weighted_graph(self):
            r"""Return the graph of mirrors, edges labelled by the invariant.

            An edge joins two mirrors whose invariant is nonzero, that is,
            every pair that is not orthogonal, and it carries the projective
            invariant of that pair as its label.
            """
            from sage.graphs.graph import Graph

            graph = Graph(multiedges=False, loops=False)
            graph.add_vertices(tuple(self._index_set))
            for left, right in combinations(self._index_set, 2):
                if self.vinberg_ratio(left, right) != 0:
                    graph.add_edge(left, right, self.vinberg_invariant(left, right))
            return graph

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
            "a mirror has a non-isotropic normal; a Gram with an isotropic "
            "diagonal entry does not present a family of mirrors"
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
        rank = len(values)
        if index_set is None:
            index_set = range(rank)
        return _vinberg_invariant_matrix(
            base_ring,
            tuple(index_set),
            [[base_ring(entry) for entry in row] for row in values],
            [[base_ring.one() for _ in range(rank)] for _ in range(rank)],
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
    return object_of(
        VinbergInvariantMatrices(),
        base_ring=base_ring,
        index_set=index_set,
        numerators=numerators,
        denominators=denominators,
    )


__all__ = ["VinbergInvariantMatrices", "reflection_cosines"]
