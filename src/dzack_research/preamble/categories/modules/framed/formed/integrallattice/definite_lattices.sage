r"""``DefiniteLattices`` — integral lattices whose form is definite.

The category exists to carry what only a definite form supports: a length.
Its ``Subobjects`` axiom is where reduction lives, because reducing means
choosing shorter generators for a submodule, and that is a statement about an
inclusion rather than about a lattice on its own.

EXAMPLES::

    sage: from dzack_research.preamble import catalogue
    sage: from dzack_research.preamble.categories import DefiniteLattices
    sage: Lattices.E8 in DefiniteLattices()
    True
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.modules import Module

from typing import Protocol, TYPE_CHECKING

from sage.categories.category import Category
from sage.categories.subobjects import SubobjectsCategory
from sage.matrix.constructor import matrix
from sage.matrix.special import identity_matrix
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

if TYPE_CHECKING:
    from sage.geometry.polyhedron.base import Polyhedron
    from sage.modules.free_module_element import FreeModuleElement
    from sage.structure.element import Element, Matrix
    from dzack_research.preamble.lexicon import RingElement
    from dzack_research.preamble.categories.sets.sets import Set
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        ModuleMorphism,
    )

    class DefiniteSubobjectParent(Protocol):
        r"""What reduction asks of a subobject: its inclusion."""

        def embedding(self) -> "ModuleMorphism": ...


class DefiniteLattices(Category):
    r"""Category of definite integral lattices.

    Definite and not positive definite: this project writes the root lattices
    negative definite, so pinning the sign here would put $E_8$ outside the
    category that reduction is defined on.  The sign is read where it matters,
    which is at the standard target below.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "definite integral lattices"

    def super_categories(self) -> list:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
        return [IntegralLattices()]

    class ParentMethods:
        r"""The distance vocabulary a definite form supports.

        Every method here reads the positive definite Gram matrix $\pm G$:
        $G$ when the form is positive definite and $-G$ when it is negative
        definite, because
        the distance geometry of $L$ and $L(-1)$ is the same geometry -- a
        closest vector, a Voronoi cell, a heuristic length do not see the
        sign this project writes root lattices with.  Values are exact: a
        length that needs a square root comes back symbolic, never a float.

        Reference implementations: Sage's
        ``sage.modules.free_module_integer.IntegerLattice`` (``babai``,
        ``closest_vector``, ``voronoi_cell``, ``voronoi_relevant_vectors``);
        the Voronoi relevance criterion is Conway--Sloane's (SPLAG ch. 21):
        $v$ is relevant iff $\pm v$ are the only shortest vectors of the
        coset $v+2L$.
        """

        def _positive_definite_gram_matrix(self: "Module") -> "Matrix":
            r"""Return the positive definite Gram matrix $\pm G$."""
            gram = matrix(SageQQ, self.gram_matrix())
            positive, negative = self.signature_pair()
            assert positive + negative == gram.nrows(), (
                f"{self} is degenerate, so no matrix measures its lengths; "
                "a definite lattice has no radical"
            )
            return gram if negative == 0 else -gram

        def vectors_of_square(self: "Module", square: "RingElement") -> "Set":
            r"""Return $\{x\in L: b(x,x)=\text{square}\}$, both signs included.

            Finite exactly because the form is definite, which is why the
            vocabulary sits on this category.  The sign regime is the
            lattice's own: a positive definite form takes no negative
            values and a negative definite one no positive values, and a
            square of the wrong sign is a caller error, asserted by name.
            Negative definite is *by definition* the $L(-1)$ transport of
            the positive regime -- the engine runs on the positive definite
            Gram matrix $\pm G$, so no caller twists anything.

            Fincke--Pohst, reached through PARI's ``qfminim`` (up to sign),
            with both signs restored: an embedding search places module generators
            on vectors, and $x$ and $-x$ are different placements.

            The indefinite case is a stated gap.  For indefinite $L$ of rank
            at least three this set is infinite, so the question is whether
            $k$ is represented at all, and that is decided adelically: the
            local conditions at every place, together with Eichler's theorem
            that such a lattice's spinor genus holds one class, so the genus
            answer descends to the class.  PARI's ``qfsolve`` is the engine
            candidate; no method here calls it.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            from dzack_research.preamble.utilities import zipsum

            positive, negative = self.signature_pair()
            sign = 1 if negative == 0 else -1
            length = sign * SageZZ(square)
            assert length >= 0, (
                f"a definite form takes values of one sign only; "
                f"square={square}, signature={self.signature_pair()}"
            )
            if length == 0:
                return finite_ordered_set((self.zero(),))
            gram = matrix(SageZZ, self._positive_definite_gram_matrix())
            _count, _largest, coordinates = gram.__pari__().qfminim(length, None)
            halves = tuple(
                zipsum(column, self.module_generators(), self.zero())
                for column in matrix(SageZZ, coordinates).columns()
                if column * gram * column == length
            )
            return finite_ordered_set(
                halves + tuple(-element for element in halves)
            )

        def roots(self: "Module") -> "Set":
            r"""Return the roots: the vectors of square $2$ in the positive
            definite regime and of square $-2$ in the negative definite one
            (the AG convention this repo writes root lattices with -- the
            $L(-1)$ transport of the convention that a root has square
            $2$)."""
            positive, negative = self.signature_pair()
            return self.vectors_of_square(2 if negative == 0 else -2)

        def vectors_of_square_and_divisibility(
            self: "Module", square: "RingElement", divisibility: "RingElement"
        ) -> "Set":
            r"""Return $\{x\in L: b(x,x)=\text{square},\ \operatorname{div}(x)=\text{divisibility}\}$.

            The divisibility of $x$ is the positive generator of the pairing
            ideal $b(x, L)\subseteq\mathbb Z$ -- the owned
            :meth:`IntegralLattices.ElementMethods.div` -- so this set is
            the square's vectors filtered by their own divisibility, which
            is the definition (reference operation: Hecke
            ``vectors_of_square_and_divisibility``).
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set

            return finite_ordered_set(
                tuple(
                    element
                    for element in self.vectors_of_square(square)
                    if element.div() == divisibility
                )
            )

        def close_vectors(
            self: "Module", target: "Element", square_bound: "RingElement"
        ) -> tuple:
            r"""Return the $(x, b(x-t,x-t))$ with $x\in L$ within the bound of $t$.

            Enumeration of the lattice points in a ball about a rational
            point $t\in L\otimes\mathbb Q$ -- the affine counterpart of
            :meth:`vectors_of_square`, and the engine behind coset
            questions: the vectors of $t + L$ of a given square are the
            $x - t$ over this enumeration.  Fincke--Pohst around a target,
            reached through PARI's ``qfcvp`` on the positive definite Gram
            matrix;
            every returned displacement is re-verified exactly, so the
            engine's floating bound cannot admit a stray point.  The sign
            regime is the lattice's own, as in :meth:`vectors_of_square`:
            the bound and the returned squares carry the definite form's
            sign.  (Reference operations: Hecke ``close_vectors`` /
            ``enumerate_quadratic_triples``.)
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.utilities import zipsum

            point = self._target_coordinates(target)
            positive, negative = self.signature_pair()
            sign = 1 if negative == 0 else -1
            length_bound = sign * square_bound
            assert length_bound >= 0, (
                f"a definite form takes values of one sign only; "
                f"square_bound={square_bound}, signature={self.signature_pair()}"
            )
            positive_gram = matrix(SageZZ, self._positive_definite_gram_matrix())
            _count, _largest, coordinates = positive_gram.__pari__().qfcvp(
                point.__pari__().Col(), length_bound + SageQQ(1) / 2
            )
            pairs = []
            for column in matrix(SageQQ, coordinates).columns():
                displacement = column - point
                length = displacement * positive_gram * displacement
                if length > length_bound:
                    continue  # the engine bound is floating; the filter is exact
                pairs.append(
                    (
                        zipsum(
                            (SageZZ(entry) for entry in column),
                            self.module_generators(),
                            self.zero(),
                        ),
                        sign * length,
                    )
                )
            return tuple(pairs)

        def root_sublattice(self: "Module") -> "Module":
            r"""Return $R(L)\hookrightarrow L$: the sublattice the roots
            generate, recognized and refined into ``RootLattices``.

            Root-lattice recognition, computed from the definitions rather
            than from determinant tables (reference implementation: Hecke
            ``root_lattice_recognition``, ``QuadForm/Quad/ZLattices.jl``):

            1. The roots are finite (definiteness), and any group order on
               the coordinate module splits them into positive and negative
               halves; lexicographic order is used.  A positive root is
               *simple* exactly when it is not the sum of two positive
               roots, so the simple system is read off by membership.
            2. All roots have square $\pm 2$, so the root system is simply
               laced and its irreducible components are of type $A$, $D$,
               or $E$ -- the classification supplies the candidates, and
               each component is matched to its type by graph isomorphism
               of Dynkin diagrams (Sage's certificate orders the component's
               simple roots into the type's standard labelling).
            3. The decisive check: the reordered simple system's matrix
               $\bigl(2\,b(\alpha_i,\alpha_j)/b(\alpha_j,\alpha_j)\bigr)$
               must equal the recognized type's Cartan matrix, and the
               recognized type must have exactly as many roots as $L$ does.

            The returned subobject's domain is framed on the reordered
            simple system and refined by ``refine_root_lattice``, so
            ``cartan_type``, ``coxeter_number``, ``highest_root`` and the
            root-system vocabulary answer natively on it.

            Stated absence: a lattice without roots has the zero lattice as
            its root sublattice, and the zero subobject is not constructed
            here -- the empty case is asserted by name.
            """
            from sage.combinat.root_system.cartan_type import CartanType
            from sage.graphs.graph import Graph

            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.root_lattices import refine_root_lattice
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

            roots = tuple(self.roots())
            assert roots, (
                f"{self} has no roots; its root sublattice is the zero "
                "lattice, which this method does not construct"
            )
            coordinates = {
                root: tuple(_coordinate_vector(root)) for root in roots
            }
            positive_roots = [
                root
                for root in roots
                if coordinates[root] > tuple([0] * len(coordinates[root]))
            ]
            positive_set = set(
                coordinates[root] for root in positive_roots
            )
            simple_roots = [
                candidate
                for candidate in positive_roots
                if not any(
                    tuple(
                        left - right
                        for left, right in zip(
                            coordinates[candidate], coordinates[other]
                        )
                    )
                    in positive_set
                    for other in positive_roots
                    if other is not candidate
                )
            ]

            def cartan_entry(row: "Element", column: "Element") -> "Element":
                return 2 * row.b(column) / column.b(column)

            adjacency = Graph(
                [
                    (i, j)
                    for i in range(len(simple_roots))
                    for j in range(i + 1, len(simple_roots))
                    if cartan_entry(simple_roots[i], simple_roots[j]) != 0
                ]
            )
            adjacency.add_vertices(range(len(simple_roots)))

            ordered_simple_roots: list = []
            component_types: list = []
            for component_vertices in adjacency.connected_components(sort=True):
                size = len(component_vertices)
                candidates = [CartanType(["A", size])]
                if size >= 4:
                    candidates.append(CartanType(["D", size]))
                if size in (6, 7, 8):
                    candidates.append(CartanType(["E", size]))
                component_graph = adjacency.subgraph(component_vertices)
                for candidate in candidates:
                    standard_graph = Graph(
                        candidate.dynkin_diagram().to_undirected(),
                        multiedges=False,
                    )
                    isomorphic, certificate = component_graph.is_isomorphic(
                        standard_graph, certificate=True
                    )
                    if isomorphic:
                        break
                else:
                    assert False, (
                        "a root system of vectors of square ±2 is simply "
                        "laced, so every component is of type A, D, or E; "
                        f"a component of size {size} matched none"
                    )
                by_standard_label = {
                    certificate[vertex]: vertex for vertex in component_vertices
                }
                ordered_simple_roots.extend(
                    simple_roots[by_standard_label[label]]
                    for label in candidate.index_set()
                )
                component_types.append(candidate)

            recognized = (
                component_types[0]
                if len(component_types) == 1
                else CartanType(component_types)
            )
            cartan_rows = matrix(
                SageZZ,
                [
                    [
                        cartan_entry(row_root, column_root)
                        for column_root in ordered_simple_roots
                    ]
                    for row_root in ordered_simple_roots
                ],
            )
            assert cartan_rows == recognized.cartan_matrix(), (
                "the reordered simple system does not carry the recognized "
                "type's Cartan matrix"
            )
            assert 2 * len(
                recognized.root_system().root_lattice().positive_roots()
            ) == len(roots), (
                "the recognized type's root count disagrees with the "
                "lattice's roots"
            )

            sublattice = self._induced_lattice(
                matrix(
                    SageZZ,
                    [coordinates[root] for root in ordered_simple_roots],
                )
            )
            assert sublattice is not None, "the simple system is nonempty"
            refine_root_lattice(sublattice, recognized)
            embedding = sublattice.Hom(self)(
                {
                    label: label
                    for label in sublattice.module_generating_set()
                }
            )
            return Subobject(embedding)

        def roots_of_square(self: "Module", square: "RingElement") -> "Set":
            r"""Return the roots of the given square: the vectors $r$ with
            $q(r)=\text{square}$ whose reflection preserves $L$.

            The general root criterion -- the one ``reflection`` on
            ``IntegralLattices`` asserts -- used as a filter: $r$ is a root
            exactly when $2\,b(x,r)/q(r)$ is integral for every $x$, decided
            on the module generators.  At square $\pm2$ every vector of that
            square passes (the pairing bound makes the coefficient
            integral), which is why :meth:`roots` needs no filter; at square
            $\pm4$ the criterion asks every pairing to be even and does real
            work.  The Coxeter configurations of this program mix square
            $-2$ and $-4$ roots, and the sources selected the $-4$ ones by
            primitivizing and testing the square, which omits the
            reflection-integrality that makes a vector a root.

            Enumeration is definite-regime (finite, via
            :meth:`vectors_of_square`); for a hyperbolic lattice the
            fundamental roots come from ``vinberg_algorithm`` and
            ``allcock_edgewalk`` on ``HyperbolicLattices``.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set

            square = SageZZ(square)
            assert square != 0, "a root is anisotropic; square 0 names no root"
            return finite_ordered_set(
                tuple(
                    candidate
                    for candidate in self.vectors_of_square(square)
                    if all(
                        2 * generator.b(candidate) / square in self.base_ring()
                        for generator in self.module_generators()
                    )
                )
            )

        def _target_coordinates(self: "Module", target: "Element") -> "FreeModuleElement":
            r"""Read a CVP target as rational coordinates in this framing."""
            from sage.modules.free_module_element import vector
            from sage.structure.element import Element as SageElement

            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

            if isinstance(target, SageElement) and target.parent() is self:
                return vector(SageQQ, _coordinate_vector(target))
            point = vector(SageQQ, target)
            gram = matrix(SageQQ, self.gram_matrix())
            assert len(point) == gram.nrows(), (
                "a closest-vector target has one coordinate per module "
                f"generator; rank {gram.nrows()}, target {point}"
            )
            return point

        def closest_vector(self: "Module", target: "Element") -> "Element":
            r"""Return the lattice vector nearest ``target`` in $L\otimes\mathbb Q$.

            Exact: the candidates are enumerated in the box that Babai's
            rounding bounds, and the least squared distance wins, with the
            lexicographically least coordinates breaking ties so the answer
            is well defined when the target is equidistant from several
            vectors.  Exhaustive enumeration and not an approximation --
            :meth:`babai` is the fast inexact neighbor.
            """
            from itertools import product

            from sage.functions.other import ceil, floor, sqrt
            from sage.modules.free_module_element import vector

            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.utilities import zipsum

            point = self._target_coordinates(target)
            gram = self._positive_definite_gram_matrix()
            if gram.nrows() == 0:
                return self.zero()

            def distance_squared(coordinates: tuple) -> "Element":
                delta = vector(
                    SageQQ,
                    [SageQQ(entry) - point[i] for i, entry in enumerate(coordinates)],
                )
                return delta * gram * delta

            best_coordinates = tuple(SageZZ(entry.round()) for entry in point)
            best_distance = distance_squared(best_coordinates)
            inverse_gram = gram.inverse()
            ranges = []
            for i in range(gram.nrows()):
                radius = sqrt(best_distance * inverse_gram[i, i])
                lower = SageZZ(floor(point[i] - radius)) - 1
                upper = SageZZ(ceil(point[i] + radius)) + 1
                ranges.append(range(lower, upper + 1))
            for raw_coordinates in product(*ranges):
                candidate = tuple(SageZZ(entry) for entry in raw_coordinates)
                distance = distance_squared(candidate)
                if distance < best_distance or (
                    distance == best_distance and candidate < best_coordinates
                ):
                    best_distance = distance
                    best_coordinates = candidate
            return zipsum(best_coordinates, self.module_generators(), self.zero())

        def babai(self: "Module", target: "Element") -> "Element":
            r"""Return Babai's rounding approximation to the closest vector.

            LLL-reduce the positive definite Gram matrix, round the target's
            coordinates in the
            reduced framing, and come back.  An approximation with a proven
            exponential factor, which is the trade for polynomial time;
            :meth:`closest_vector` is the exact answer.
            """
            from sage.modules.free_module_element import vector

            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.utilities import zipsum

            point = self._target_coordinates(target)
            gram = self._positive_definite_gram_matrix()
            if gram.nrows() == 0:
                return self.zero()
            transform = matrix(SageQQ, matrix(SageZZ, gram).LLL_gram())
            reduced_coordinates = point * transform.inverse()
            rounded = vector(
                SageZZ, [SageZZ(entry.round()) for entry in reduced_coordinates]
            )
            return zipsum(rounded * transform, self.module_generators(), self.zero())

        # Sage's ``IntegerLattice`` names the same algorithm both ways.
        approximate_closest_vector = babai

        def voronoi_cell(self: "Module", bound: "RingElement | None" = None) -> "Polyhedron":
            r"""Return the Voronoi cell of the origin, a rational polytope.

            The intersection of the half-spaces
            $\{x: \langle x,v\rangle\le q(v)/2\}$ over nonzero short vectors
            $v$, in coordinates against the module generators.  With no
            ``bound`` the enumeration radius doubles until the cell closes
            up, which it must once the relevant vectors are inside.
            """
            from sage.geometry.polyhedron.constructor import Polyhedron as polyhedron
            from sage.modules.free_module_element import vector

            gram = self._positive_definite_gram_matrix()
            if gram.nrows() == 0:
                return polyhedron(vertices=[[]], base_ring=SageQQ)

            def cell_from_bound(radius: "RingElement") -> "Polyhedron":
                _count, _largest, coordinates = (
                    gram.__pari__().qfminim(radius, None)
                )
                inequalities = []
                for column in matrix(SageZZ, coordinates).columns():
                    for signed in (column, -column):
                        row_vector = vector(SageQQ, signed) * gram
                        square = vector(SageQQ, signed) * gram * vector(SageQQ, signed)
                        inequalities.append(
                            [square / 2] + [-entry for entry in row_vector]
                        )
                return polyhedron(ieqs=inequalities, base_ring=SageQQ)

            if bound is not None:
                return cell_from_bound(SageZZ(bound))
            radius = SageZZ(max(gram[i, i] for i in range(gram.nrows())) + 1)
            for _doubling in range(8):
                cell = cell_from_bound(radius)
                if cell.is_compact():
                    return cell
                radius *= 2
            assert False, (
                f"no compact Voronoi cell within enumeration radius {radius} "
                f"for {self}; the relevant vectors are longer than expected"
            )

        def voronoi_relevant_vectors(self: "Module") -> "Set":
            r"""Return the Voronoi-relevant vectors, a finite Set.

            $v$ is relevant iff $\pm v$ are the unique shortest vectors of
            the coset $v+2L$ (Conway--Sloane, SPLAG ch. 21): exactly the
            vectors whose half-space is a facet of the Voronoi cell.
            """
            from sage.modules.free_module_element import vector

            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            from dzack_research.preamble.utilities import zipsum

            gram = self._positive_definite_gram_matrix()
            if gram.nrows() == 0:
                return finite_ordered_set(())
            radius = SageZZ(max(gram[i, i] for i in range(gram.nrows())) + 1)
            for _doubling in range(8):
                if self.voronoi_cell(bound=radius).is_compact():
                    break
                radius *= 2
            _count, _largest, coordinates = (
                gram.__pari__().qfminim(2 * radius, None)
            )
            candidates = [
                vector(SageZZ, signed)
                for column in matrix(SageZZ, coordinates).columns()
                for signed in (column, -column)
            ]

            def square(candidate: "FreeModuleElement") -> "Element":
                return candidate * gram * candidate

            relevant = [
                candidate
                for candidate in candidates
                if all(
                    other == candidate
                    or other == -candidate
                    or any(
                        (candidate[i] - other[i]) % 2 != 0
                        for i in range(gram.nrows())
                    )
                    or square(other) > square(candidate)
                    for other in candidates
                )
            ]
            return finite_ordered_set(
                tuple(
                    zipsum(candidate, self.module_generators(), self.zero())
                    for candidate in relevant
                )
            )

        def gaussian_heuristic(self: "Module", exact_form: bool = False) -> "Element":
            r"""Return the heuristic expected shortest length, exact and symbolic.

            The Stirling form $\det(G)^{1/2n}\sqrt{n/(2\pi e)}$, or with
            ``exact_form`` the Gamma form
            $(\sqrt{\det G}\,\Gamma(1+n/2))^{1/n}/\sqrt\pi$.  Both are exact
            symbolic expressions; the $n$-th root is taken with the rational
            exponent $1/n\in\mathbb Q$, because a Python ``1 / n`` is a
            float and silently destroys exactness.
            """
            from sage.functions.gamma import gamma
            from sage.symbolic.constants import e, pi
            from sage.symbolic.ring import SR

            gram = self._positive_definite_gram_matrix()
            n = gram.nrows()
            assert n > 0, "the rank-0 lattice has no shortest nonzero vector"
            exponent = SageQQ(1) / n
            determinant_sqrt = SR(gram.determinant()).sqrt()
            if exact_form:
                return (
                    determinant_sqrt * gamma(1 + SageQQ(n) / 2)
                ) ** exponent / pi.sqrt()
            return determinant_sqrt**exponent * (n / (2 * pi * e)).sqrt()

        def hadamard_ratio(self: "Module") -> "Element":
            r"""Return $(\sqrt{\det G}/\prod_i\|g_i\|)^{1/n}$, exact and symbolic.

            $1$ exactly when the generators are orthogonal, smaller as the
            framing skews; the standard measure of how reduced a framing
            already is.  The $n$-th root uses the rational exponent
            $1/n\in\mathbb Q$ -- see :meth:`gaussian_heuristic` on why
            ``1 / n`` is banned here.
            """
            from sage.misc.misc_c import prod
            from sage.symbolic.ring import SR

            gram = self._positive_definite_gram_matrix()
            n = gram.nrows()
            assert n > 0, "the rank-0 lattice has no framing to measure"
            product_of_norms = prod(
                SR(gram[i, i]).sqrt() for i in range(n)
            )
            return (SR(gram.determinant()).sqrt() / product_of_norms) ** (
                SageQQ(1) / n
            )

        def theta_series(self: "Module", prec: "RingElement") -> "Element":
            r"""Return $\theta_L(q)=\sum_{x\in L}q^{\pm b(x,x)}$ to $O(q^{\text{prec}})$.

            Exponents read the positive definite Gram matrix $\pm G$, so for a
            negative
            definite lattice this is the theta series of $L(-1)$ -- the same
            transport every method of this category makes.  The series
            converges for $|q|<1$ exactly because the form is definite
            (Conway--Sloane, SPLAG ch. 2): each coefficient counts the finite
            set :meth:`vectors_of_square` returns, and an indefinite lattice
            has infinitely many vectors of one square, so the vocabulary sits
            on this category.

            Engine: Sage's ``QuadraticForm.theta_series`` (PARI ``qfrep``
            behind it) on the quadratic form $x\mapsto x(\pm G)x^t$, whose
            Hessian is $2(\pm G)$.
            """
            from sage.quadratic_forms.quadratic_form import QuadraticForm

            gram = matrix(SageZZ, self._positive_definite_gram_matrix())
            return QuadraticForm(SageZZ, 2 * gram).theta_series(prec)

        def kissing_number(self: "Module") -> "RingElement":
            r"""Return the number of vectors of minimal nonzero length.

            The kissing number of the sphere packing on $L$: each minimal
            vector names one sphere touching the sphere at the origin
            (Conway--Sloane, SPLAG ch. 1).  Both signs are counted -- $x$ and
            $-x$ touch at antipodal points -- and PARI's count already
            includes both: $E_8$ answers $240$.

            Fincke--Pohst, reached through PARI's ``qfminim`` on the length
            Gram matrix.
            """
            gram = matrix(SageZZ, self._positive_definite_gram_matrix())
            assert gram.nrows() > 0, (
                "the rank-0 lattice has no nonzero vector"
            )
            count, _minimal, _vectors = gram.__pari__().qfminim(None, 0)
            return SageZZ(count)

        def packing_radius(self: "Module") -> "Element":
            r"""Return $\rho=\lambda_1/2$, exact and symbolic.

            Half the minimal distance between distinct lattice points: open
            balls of this radius centered at lattice points are disjoint, and
            it is the largest radius with that property (Conway--Sloane,
            SPLAG ch. 1).  The length is $\sqrt{\min b(x,x)}$ on the length
            Gram matrix, returned symbolic and exact, never a float.
            """
            from sage.symbolic.ring import SR

            gram = matrix(SageZZ, self._positive_definite_gram_matrix())
            assert gram.nrows() > 0, (
                "the rank-0 lattice has no pair of distinct points"
            )
            minimal = SageZZ(gram.__pari__().qfminim(None, 0)[1])
            return SR(minimal).sqrt() / 2

        def covering_radius(self: "Module") -> "Element":
            r"""Return the covering radius, exact and symbolic.

            The least $R$ with $L\otimes\mathbb R=\bigcup_{v\in L}\bar B(v,R)$:
            the distance from the origin to a deepest hole.  Every deep hole
            is a vertex of the Voronoi cell (Conway--Sloane, SPLAG ch. 2), so
            the covering radius is the circumradius of :meth:`voronoi_cell` --
            the largest length among its vertices, whose coordinates are
            rational, so the squared radius is exact and the length is its
            symbolic square root.
            """
            from sage.modules.free_module_element import vector
            from sage.symbolic.ring import SR

            gram = self._positive_definite_gram_matrix()
            squared = max(
                point * gram * point
                for point in (
                    vector(SageQQ, vertex)
                    for vertex in self.voronoi_cell().vertices_list()
                )
            )
            return SR(squared).sqrt()

        def successive_minima(self: "Module") -> "tuple[Element, ...]":
            r"""Return $(\lambda_1,\dots,\lambda_n)$, exact and symbolic.

            $\lambda_i$ is the least length $r$ such that $L$ holds $i$
            linearly independent vectors of length at most $r$ (Cassels,
            *An Introduction to the Geometry of Numbers*, ch. VIII), read on
            the positive definite Gram matrix.  Greedy attains every
            $\lambda_i$: scan
            the vectors in increasing length and keep each one independent of
            those kept so far -- any $i$ independent vectors of length at most
            $r$ include one outside the span of the first $i-1$ kept, so the
            $i$-th kept length is at most $\lambda_i$, and the $i$ kept
            vectors witness $\lambda_i$ at most that length.

            The enumeration bound is the largest diagonal entry of the LLL
            reduced Gram matrix: its rows are $n$ independent vectors, so
            $\lambda_n^2$ is at most that entry.  Fincke--Pohst through
            PARI's ``qfminim``.
            """
            from sage.symbolic.ring import SR

            gram = matrix(SageZZ, self._positive_definite_gram_matrix())
            n = gram.nrows()
            assert n > 0, "the rank-0 lattice has no successive minima"
            transformation = matrix(SageZZ, gram.LLL_gram())
            reduced = transformation.transpose() * gram * transformation
            bound = max(reduced[i, i] for i in range(n))
            _count, _largest, coordinates = gram.__pari__().qfminim(bound, None)
            columns = sorted(
                matrix(SageZZ, coordinates).columns(),
                key=lambda column: column * gram * column,
            )
            independent: "list[FreeModuleElement]" = []
            for column in columns:
                if matrix(SageZZ, independent + [column]).rank() == len(independent) + 1:
                    independent.append(column)
                    if len(independent) == n:
                        break
            assert len(independent) == n, (
                f"the LLL reduced generators of {self} are {n} independent "
                f"vectors of squared length at most {bound}, so the "
                "enumeration up to that bound holds a full independent set"
            )
            return tuple(
                SR(column * gram * column).sqrt() for column in independent
            )

        def contact_polytope(self: "Module") -> "Polyhedron":
            r"""Return the convex hull of the minimal vectors, a rational polytope.

            The vertices are the vectors of minimal nonzero length -- the
            sphere centers touching the sphere at the origin (Conway--Sloane,
            SPLAG ch. 1) -- in coordinates against the module generators,
            the same coordinates :meth:`voronoi_cell` speaks.
            """
            from sage.geometry.polyhedron.constructor import Polyhedron as polyhedron

            gram = matrix(SageZZ, self._positive_definite_gram_matrix())
            assert gram.nrows() > 0, (
                "the rank-0 lattice has no nonzero vector"
            )
            minimal = SageZZ(gram.__pari__().qfminim(None, 0)[1])
            positive, negative = self.signature_pair()
            sign = 1 if negative == 0 else -1
            return polyhedron(
                vertices=[
                    element._coordinates()
                    for element in self.vectors_of_square(sign * minimal)
                ],
                base_ring=SageQQ,
            )

        def hermite_invariant(self: "Module") -> "Element":
            r"""Return $\gamma(L)=\lambda_1^2/\det(\pm G)^{1/n}$, exact and symbolic.

            The Hermite *constant* $\gamma_n$ is the supremum of this
            invariant over the rank-$n$ lattices (Conway--Sloane, SPLAG
            ch. 1); this method returns the invariant of one lattice, so it
            is named for what it computes.  $E_8$ answers $2$, which is
            $\gamma_8$.  The $n$-th root uses the rational exponent
            $1/n\in\mathbb Q$ -- see :meth:`gaussian_heuristic` on why
            ``1 / n`` is banned here.
            """
            from sage.symbolic.ring import SR

            gram = matrix(SageZZ, self._positive_definite_gram_matrix())
            n = gram.nrows()
            assert n > 0, "the rank-0 lattice has no minimal nonzero vector"
            minimal = SageZZ(gram.__pari__().qfminim(None, 0)[1])
            return minimal / SR(gram.determinant()) ** (SageQQ(1) / n)

        def center_density(self: "Module") -> "Element":
            r"""Return $\delta=\rho^n/\sqrt{\det(\pm G)}$, exact and symbolic.

            The number of sphere centers per unit volume when the spheres
            have the packing radius $\rho$: the packing density with the ball
            volume factored out (Conway--Sloane, SPLAG ch. 1), which is why
            it is the column lattice tables print.
            """
            from sage.symbolic.ring import SR

            gram = matrix(SageZZ, self._positive_definite_gram_matrix())
            n = gram.nrows()
            assert n > 0, "the rank-0 lattice packs no spheres"
            return self.packing_radius() ** n / SR(gram.determinant()).sqrt()

        def packing_density(self: "Module") -> "Element":
            r"""Return $\Delta=V_n\,\delta$, the fraction of space the packing fills.

            $V_n=\pi^{n/2}/\Gamma(1+n/2)$ is the volume of the unit ball, and
            $\delta$ is :meth:`center_density` (Conway--Sloane, SPLAG ch. 1).
            Exact and symbolic: $\pi$ stays $\pi$.
            """
            from sage.functions.gamma import gamma
            from sage.symbolic.constants import pi

            gram = matrix(SageZZ, self._positive_definite_gram_matrix())
            n = gram.nrows()
            assert n > 0, "the rank-0 lattice packs no spheres"
            ball_volume = pi ** (SageQQ(n) / 2) / gamma(1 + SageQQ(n) / 2)
            return ball_volume * self.center_density()

    class Subobjects(SubobjectsCategory):
        r"""Submodules of a definite lattice, framed by their inclusion."""

        class ParentMethods:
            def LLL(self: "DefiniteSubobjectParent") -> "Module":
                r"""Return this subobject on an LLL reduced framing.

                The same submodule of the same codomain, generated by
                shorter and more nearly orthogonal vectors.  What is reduced
                is the inclusion's matrix: its rows are the generators of $S$
                written in the codomain's framing, so the arrow carries the
                reduction and no call site rebuilds an embedding out of rows
                it reduced itself.

                The codomain must be $I_{n,0}$ or $I_{0,n}$.  Reduction reads
                those rows as vectors and compares their lengths, which is
                only what they mean when the codomain's form is the standard
                one; over any other definite form the same rows are
                coordinates and their entries are not lengths.  $I_{0,n}$ is
                admitted because $S$ and $S(-1)$ have the same short vectors.
                """
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
                from dzack_research.preamble.categories.sets.sets import finite_ordered_set
                from dzack_research.preamble.utilities import zipsum
                inclusion = self.embedding()
                codomain = inclusion.codomain()
                gram = matrix(SageZZ, codomain.gram_matrix())
                standard = identity_matrix(SageZZ, gram.nrows())
                assert gram == standard or gram == -standard, (
                    f"{codomain} is not $I_(n,0)$ or $I_(0,n)$, so the rows of "
                    "an inclusion into it are coordinates and not vectors"
                )
                return self._subobject_on_reduced_rows(
                    inclusion.matrix().LLL().rows()
                )

            def _subobject_on_reduced_rows(
                self: "DefiniteSubobjectParent", rows: "Iterable"
            ) -> "Module":
                r"""Return this subobject reframed on the given generator rows.

                A new subobject and not a new arrow out of $S$: the reduced
                generators induce a different form on the domain, so the old
                domain is not one this arrow could preserve.  A row is one
                generator's image in the codomain.

                Not ``subobject_on``: it puts a generating set into the
                normal form of its rows, which is the framing this replaces.
                """
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
                from dzack_research.preamble.categories.sets.sets import finite_ordered_set
                from dzack_research.preamble.utilities import zipsum
                codomain = self.embedding().codomain()
                reduced = finite_ordered_set(tuple(
                    zipsum(row, codomain.module_generators(), codomain.zero())
                    for row in rows
                ))
                sub = codomain._sub_form_module(
                    matrix([[left.b(right) for right in reduced] for left in reduced]),
                    reduced,
                )
                return Subobject(sub.Hom(codomain)({
                    generator: generator for generator in reduced
                }))

            def BKZ(
                self: "DefiniteSubobjectParent", block_size: int = 10
            ) -> "Module":
                r"""Return this subobject on a BKZ reduced framing.

                Block Korkine--Zolotarev reduction (Schnorr--Euchner, through
                ``fpylll``): stronger than :meth:`LLL`, the same contract --
                the same submodule of the same codomain on shorter, more
                nearly orthogonal generators, with the same $I_{n,0}$ /
                $I_{0,n}$ gate on the codomain, for the same reason: the
                reducer reads rows as vectors and compares lengths.
                """
                import fpylll

                inclusion = self.embedding()
                codomain = inclusion.codomain()
                gram = matrix(SageZZ, codomain.gram_matrix())
                standard = identity_matrix(SageZZ, gram.nrows())
                assert gram == standard or gram == -standard, (
                    f"{codomain} is not $I_(n,0)$ or $I_(0,n)$, so the rows of "
                    "an inclusion into it are coordinates and not vectors"
                )
                rows = matrix(SageZZ, inclusion.matrix())
                if rows.nrows() < 2:
                    # fpylll rejects block_size < 2, and on one row BKZ is
                    # LLL anyway: block reduction has no block to work on.
                    return self.LLL()
                basis = fpylll.IntegerMatrix.from_matrix(rows)
                # fpylll requires a block size of at least 2 and no more
                # than the number of rows being reduced.
                clamped = max(2r, min(int(block_size), rows.nrows()))
                fpylll.BKZ.reduction(
                    basis, fpylll.BKZ.Param(block_size=clamped)
                )
                reduced_rows = matrix(SageZZ, basis.nrows, basis.ncols)
                basis.to_matrix(reduced_rows)
                return self._subobject_on_reduced_rows(reduced_rows.rows())

            def HKZ(self: "DefiniteSubobjectParent") -> "Module":
                r"""Return this subobject on an HKZ reduced framing.

                Hermite--Korkine--Zolotarev reduction is full-block BKZ: the
                block is the whole rank.
                """
                return self.BKZ(block_size=self.rank())
