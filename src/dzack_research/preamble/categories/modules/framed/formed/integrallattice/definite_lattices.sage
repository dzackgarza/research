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

        Every method here reads the *length* Gram matrix: $G$ when the form
        is positive definite and $-G$ when it is negative definite, because
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

        def _length_gram_matrix(self: "Module") -> "Matrix":
            r"""Return the positive matrix measuring squared lengths: $\pm G$."""
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
            the positive regime -- the engine runs on the length Gram
            matrix $\pm G$, so no caller twists anything.

            Fincke--Pohst, reached through PARI's ``qfminim`` (up to sign),
            with both signs restored: an embedding search places module generators
            on vectors, and $x$ and $-x$ are different placements.
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
            gram = matrix(SageZZ, self._length_gram_matrix())
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
            $L(-1)$ transport of the norm-2 convention)."""
            positive, negative = self.signature_pair()
            return self.vectors_of_square(2 if negative == 0 else -2)

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
            gram = self._length_gram_matrix()
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

            LLL-reduce the length Gram, round the target's coordinates in the
            reduced framing, and come back.  An approximation with a proven
            exponential factor, which is the trade for polynomial time;
            :meth:`closest_vector` is the exact answer.
            """
            from sage.modules.free_module_element import vector

            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.utilities import zipsum

            point = self._target_coordinates(target)
            gram = self._length_gram_matrix()
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

            gram = self._length_gram_matrix()
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
                        norm = vector(SageQQ, signed) * gram * vector(SageQQ, signed)
                        inequalities.append(
                            [norm / 2] + [-entry for entry in row_vector]
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

            gram = self._length_gram_matrix()
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

            def norm(candidate: "FreeModuleElement") -> "Element":
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
                    or norm(other) > norm(candidate)
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

            gram = self._length_gram_matrix()
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

            gram = self._length_gram_matrix()
            n = gram.nrows()
            assert n > 0, "the rank-0 lattice has no framing to measure"
            product_of_norms = prod(
                SR(gram[i, i]).sqrt() for i in range(n)
            )
            return (SR(gram.determinant()).sqrt() / product_of_norms) ** (
                SageQQ(1) / n
            )

    class Subobjects(SubobjectsCategory):
        r"""Submodules of a definite lattice, framed by their inclusion."""

        class ParentMethods:
            def LLL(self: "DefiniteSubobjectParent") -> "Module":
                r"""Return this subobject on an LLL reduced framing.

                The same submodule of the same ambient, generated by shorter
                and more nearly orthogonal vectors.  What is reduced is the
                inclusion's matrix: its rows are the generators of $S$ written
                in the ambient's framing, so the arrow carries the reduction
                and no call site rebuilds an embedding out of rows it reduced
                itself.

                The target must be $I_{n,0}$ or $I_{0,n}$.  Reduction reads
                those rows as vectors and compares their lengths, which is
                only what they mean when the ambient's form is the standard
                one; over any other definite form the same rows are
                coordinates and their entries are not lengths.  $I_{0,n}$ is
                admitted because $S$ and $S(-1)$ have the same short vectors.
                """
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
                from dzack_research.preamble.categories.sets.sets import finite_ordered_set
                from dzack_research.preamble.utilities import zipsum
                inclusion = self.embedding()
                ambient = inclusion.codomain()
                gram = matrix(SageZZ, ambient.gram_matrix())
                standard = identity_matrix(SageZZ, gram.nrows())
                assert gram == standard or gram == -standard, (
                    f"{ambient} is not $I_(n,0)$ or $I_(0,n)$, so the rows of "
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
                generator's image in the ambient.

                Not ``subobject_on``: it puts a generating set into the
                normal form of its rows, which is the framing this replaces.
                """
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
                from dzack_research.preamble.categories.sets.sets import finite_ordered_set
                from dzack_research.preamble.utilities import zipsum
                ambient = self.embedding().codomain()
                reduced = finite_ordered_set(tuple(
                    zipsum(row, ambient.module_generators(), ambient.zero())
                    for row in rows
                ))
                sub = ambient._sub_form_module(
                    matrix([[left.b(right) for right in reduced] for left in reduced]),
                    reduced,
                )
                return Subobject(sub.Hom(ambient)({
                    generator: generator for generator in reduced
                }))

            def BKZ(
                self: "DefiniteSubobjectParent", block_size: int = 10
            ) -> "Module":
                r"""Return this subobject on a BKZ reduced framing.

                Block Korkine--Zolotarev reduction (Schnorr--Euchner, through
                ``fpylll``): stronger than :meth:`LLL`, the same contract --
                the same submodule of the same ambient on shorter, more
                nearly orthogonal generators, with the same $I_{n,0}$ /
                $I_{0,n}$ gate on the ambient, for the same reason: the
                reducer reads rows as vectors and compares lengths.
                """
                import fpylll

                inclusion = self.embedding()
                ambient = inclusion.codomain()
                gram = matrix(SageZZ, ambient.gram_matrix())
                standard = identity_matrix(SageZZ, gram.nrows())
                assert gram == standard or gram == -standard, (
                    f"{ambient} is not $I_(n,0)$ or $I_(0,n)$, so the rows of "
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
