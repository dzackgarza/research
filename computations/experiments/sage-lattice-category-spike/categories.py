r"""Sage category surfaces for the owned synthetic lattice spike."""

from __future__ import annotations

from sage.categories.category_types import Category_over_base_ring
from sage.categories.category_with_axiom import (
    CategoryWithAxiom_over_base_ring,
    all_axioms,
    axiom,
)
from sage.categories.homsets import HomsetsCategory
from sage.categories.modules import Modules
from sage.categories.sets_cat import Sets
from sage.misc.abstract_method import abstract_method
from sage.rings.integer_ring import ZZ


_LATTICE_AXIOMS = (
    "Symmetric",
    "Nondegenerate",
    "Integral",
    "Even",
    "Unimodular",
    "Definite",
    "PositiveDefinite",
    "NegativeDefinite",
    "Indefinite",
    "Embedded",
    "WithDistinguishedBasis",
    "FiniteBilinearForms",
    "FiniteQuadraticForms",
    "WithSourceLattice",
)

for _axiom_name in _LATTICE_AXIOMS:
    if _axiom_name not in all_axioms:
        all_axioms.add(_axiom_name)


class QuadraticModules(Category_over_base_ring):
    r"""Finite-rank modules carrying a bilinear/quadratic form."""

    def _repr_object_names(self):
        return f"synthetic quadratic modules over {self.base_ring()}"

    def super_categories(self):
        return [Modules(self.base_ring()).WithBasis()]

    def additional_structure(self):
        return self

    class ParentMethods:
        @abstract_method
        def value_ring(self):
            r"""Return the value ring of the form."""

        @abstract_method
        def gram_matrix(self):
            r"""Return the Gram matrix in the distinguished basis."""

        @abstract_method
        def bilinear_form(self):
            r"""Return the bilinear form carried by this module."""


class RationalLattices(Category_over_base_ring):
    r"""Synthetic finite-rank modules with symmetric form valued in ``QQ``."""

    def _repr_object_names(self):
        return f"synthetic rational lattices over {self.base_ring()}"

    def super_categories(self):
        return [QuadraticModules(self.base_ring()), Modules(self.base_ring()).WithBasis()]

    def additional_structure(self):
        return self

    class SubcategoryMethods:
        Symmetric = axiom("Symmetric")
        Nondegenerate = axiom("Nondegenerate")
        Integral = axiom("Integral")
        Even = axiom("Even")
        Unimodular = axiom("Unimodular")
        Definite = axiom("Definite")
        PositiveDefinite = axiom("PositiveDefinite")
        NegativeDefinite = axiom("NegativeDefinite")
        Indefinite = axiom("Indefinite")
        Embedded = axiom("Embedded")
        WithDistinguishedBasis = axiom("WithDistinguishedBasis")

    class ParentMethods:
        @abstract_method
        def value_ring(self):
            r"""Return the value ring of the bilinear form."""

        @abstract_method
        def rational_span(self):
            r"""Return ``self tensor_ZZ QQ`` with its induced bilinear form."""

        @abstract_method
        def basis_matrix(self):
            r"""Return basis coordinates in this lattice's rationalization."""

        @abstract_method
        def gram_matrix(self):
            r"""Return the Gram matrix in the distinguished module basis."""

        @abstract_method
        def bilinear_form(self):
            r"""Return the bilinear form carried by this lattice."""

        @abstract_method
        def dual_lattice(self):
            r"""Return the metric dual lattice in ``self.rational_span()``."""

        @abstract_method
        def discriminant_group(self):
            r"""Return the finite quotient ``L# / L`` when defined."""

        @abstract_method
        def signature_pair(self):
            r"""Return ``(positive, negative)`` for the rational form."""

        @abstract_method
        def is_integral(self):
            r"""Return whether the Gram matrix has integral entries."""

        @abstract_method
        def is_even(self):
            r"""Return whether every diagonal value lies in ``2 ZZ``."""

        @abstract_method
        def is_unimodular(self):
            r"""Return whether the integral lattice has determinant ``+-1``."""

    class ElementMethods:
        def b(self, other):
            r"""Evaluate the parent bilinear form on ``self`` and ``other``."""
            return self.parent().b(self, other)

        def q(self):
            r"""Evaluate the diagonal value ``b(self, self)``."""
            return self.b(self)

    class MorphismMethods:
        @abstract_method
        def matrix(self):
            r"""Return the matrix of this lattice morphism."""

    class Homsets(HomsetsCategory):
        r"""Homsets of form-preserving lattice morphisms."""

        def extra_super_categories(self):
            return [Sets()]

        class ParentMethods:
            @abstract_method
            def from_matrix(self, matrix_data):
                r"""Construct the lattice morphism represented by ``matrix_data``."""

        class ElementMethods:
            @abstract_method
            def kernel(self):
                r"""Return the kernel lattice of this morphism."""

            @abstract_method
            def image(self):
                r"""Return the image lattice of this morphism."""


class DiscriminantGroups(Category_over_base_ring):
    r"""Finite quotient modules with discriminant bilinear/quadratic forms."""

    def _repr_object_names(self):
        return f"synthetic discriminant groups over {self.base_ring()}"

    def super_categories(self):
        return [Modules(self.base_ring())]

    def additional_structure(self):
        return self

    class SubcategoryMethods:
        FiniteBilinearForms = axiom("FiniteBilinearForms")
        FiniteQuadraticForms = axiom("FiniteQuadraticForms")
        Even = axiom("Even")
        WithSourceLattice = axiom("WithSourceLattice")

    class ParentMethods:
        @abstract_method
        def cover(self):
            r"""Return the covering lattice/module ``L#``."""

        @abstract_method
        def relations(self):
            r"""Return the relation lattice/module ``L``."""

        @abstract_method
        def invariants(self):
            r"""Return Smith invariants of the finite quotient."""

        @abstract_method
        def primary_part(self, p):
            r"""Return the ``p``-primary discriminant form."""


class SymmetricRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLattices, "Symmetric")


class NondegenerateRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLattices, "Nondegenerate")


class IntegralRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLattices, "Integral")


class EvenRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLattices, "Even")

    def extra_super_categories(self):
        return (RationalLattices(self.base_ring()).Integral(),)


class UnimodularRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLattices, "Unimodular")

    def extra_super_categories(self):
        return (RationalLattices(self.base_ring()).Integral(),)


class DefiniteRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLattices, "Definite")


class PositiveDefiniteRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLattices, "PositiveDefinite")

    def extra_super_categories(self):
        return (RationalLattices(self.base_ring()).Definite(),)

    class ParentMethods:
        def _positive_definite_algorithm_not_implemented(self, name):
            raise NotImplementedError(f"{name} is gated to positive-definite lattices but is not implemented in this spike")

        def LLL(self):
            from sage.matrix.constructor import matrix
            from sage.rings.integer_ring import ZZ

            assert self.base_ring() is ZZ, "LLL is implemented only for ZZ-lattices in this spike"
            assert self.is_integral(), f"LLL requires an integral Gram matrix; gram={self.gram_matrix()}"
            change_of_basis = matrix(ZZ, self.gram_matrix()).LLL_gram()
            return self.sublattice(change_of_basis, label="LLL")

        def BKZ(self, block_size=10, **kwargs):
            from sage.matrix.constructor import matrix
            from sage.rings.integer_ring import ZZ

            assert self.base_ring() is ZZ, "BKZ is implemented only for ZZ-lattices in this spike"
            assert self.is_integral(), f"BKZ requires an integral Gram matrix; gram={self.gram_matrix()}"
            import fpylll

            gram = matrix(ZZ, self.gram_matrix())
            gram_matrix = fpylll.IntegerMatrix.from_matrix(gram)
            transform = fpylll.IntegerMatrix.identity(gram.nrows())
            gso = fpylll.GSO.Mat(gram_matrix, U=transform, gram=True)
            lll = fpylll.LLL.Reduction(gso)
            params = fpylll.BKZ.Param(block_size=block_size, **kwargs)
            reduction = fpylll.BKZ.Reduction(gso, lll, params)
            reduction()
            change_of_basis = matrix(
                ZZ,
                transform.nrows,
                transform.ncols,
                [transform[i, j] for i in range(transform.nrows) for j in range(transform.ncols)],
            )
            return self.sublattice(change_of_basis, label="BKZ")

        def short_vectors(self, n, **kwargs):
            from sage.quadratic_forms.quadratic_form import QuadraticForm
            from sage.rings.integer_ring import ZZ

            assert self.base_ring() is ZZ, "short vector enumeration is implemented only for ZZ-lattices in this spike"
            assert self.is_integral(), f"short vector enumeration requires an integral Gram matrix; gram={self.gram_matrix()}"
            q = QuadraticForm(2 * self.gram_matrix().change_ring(ZZ))
            return [[self(vector) for vector in vectors] for vectors in q.short_vector_list_up_to_length(n, **kwargs)]

        def shortest_vector(self):
            if self.rank() == 0:
                return self.zero()
            bound = min(self.gen(i).q() for i in range(self.rank())) + 1
            for vectors in self.short_vectors(bound):
                for vector in vectors:
                    if not vector == self.zero():
                        return vector
            raise ArithmeticError("positive-definite short-vector enumeration returned no nonzero vector")

        def closest_vector(self, target):
            from itertools import product

            from sage.functions.other import ceil, floor, sqrt
            from sage.matrix.constructor import matrix
            from sage.modules.free_module_element import vector
            from sage.rings.integer_ring import ZZ
            from sage.rings.rational_field import QQ

            target = vector(QQ, target.coordinates() if hasattr(target, "coordinates") and target.parent() is self else target)
            assert len(target) == self.rank(), (
                "closest vector target must have one coordinate per lattice basis vector; "
                f"rank={self.rank()}, target={target}"
            )
            if self.rank() == 0:
                return self.zero()
            gram = matrix(QQ, self.gram_matrix())

            def distance_squared(coordinates):
                delta = matrix(QQ, 1, self.rank(), [QQ(coordinates[i]) - target[i] for i in range(self.rank())])
                return (delta * gram * delta.transpose())[0, 0]

            center = [ZZ(round(target[i])) for i in range(self.rank())]
            best_coordinates = tuple(center)
            best_distance = distance_squared(best_coordinates)
            inverse_gram = gram.inverse()
            ranges = []
            for i in range(self.rank()):
                radius = sqrt(best_distance * inverse_gram[i, i])
                lower = ZZ(floor(target[i] - radius)) - 1
                upper = ZZ(ceil(target[i] + radius)) + 1
                ranges.append(range(lower, upper + 1))
            for coordinates in product(*ranges):
                distance = distance_squared(coordinates)
                if distance < best_distance or (distance == best_distance and tuple(coordinates) < best_coordinates):
                    best_distance = distance
                    best_coordinates = tuple(ZZ(coordinate) for coordinate in coordinates)
            return self(best_coordinates)

        def voronoi_cell(self, radius=None):
            from sage.geometry.polyhedron.constructor import Polyhedron
            from sage.matrix.constructor import matrix
            from sage.rings.integer_ring import ZZ
            from sage.rings.rational_field import QQ

            if self.rank() == 0:
                return Polyhedron(vertices=[[]], base_ring=QQ)
            gram = matrix(QQ, self.gram_matrix())

            def cell_from_bound(bound):
                inequalities = []
                for vectors in self.short_vectors(bound):
                    for lattice_vector in vectors:
                        if lattice_vector == self.zero():
                            continue
                        coordinates = list(lattice_vector.coordinates())
                        column = matrix(QQ, self.rank(), 1, coordinates)
                        gram_vector = gram * column
                        inequalities.append(
                            [QQ(lattice_vector.q()) / 2]
                            + [-gram_vector[i, 0] for i in range(self.rank())]
                        )
                return Polyhedron(ieqs=inequalities, base_ring=QQ)

            if radius is not None:
                return cell_from_bound(ZZ(radius))
            bound = ZZ(max(self.gen(i).q() for i in range(self.rank())) + 1)
            for _ in range(8):
                cell = cell_from_bound(bound)
                if cell.is_compact():
                    return cell
                bound *= 2
            raise ArithmeticError("failed to find a compact Voronoi cell from enumerated short vectors")


class NegativeDefiniteRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLattices, "NegativeDefinite")

    def extra_super_categories(self):
        return (RationalLattices(self.base_ring()).Definite(),)


class IndefiniteRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLattices, "Indefinite")


class EmbeddedRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLattices, "Embedded")


class WithDistinguishedBasisRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLattices, "WithDistinguishedBasis")


class FiniteBilinearDiscriminantGroups(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantGroups, "FiniteBilinearForms")


class FiniteQuadraticDiscriminantGroups(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantGroups, "FiniteQuadraticForms")

    def extra_super_categories(self):
        return (DiscriminantGroups(self.base_ring()).FiniteBilinearForms(),)


class EvenDiscriminantGroups(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantGroups, "Even")

    def extra_super_categories(self):
        return (DiscriminantGroups(self.base_ring()).FiniteQuadraticForms(),)


class WithSourceLatticeDiscriminantGroups(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantGroups, "WithSourceLattice")


RationalLattices.Symmetric = SymmetricRationalLattices
RationalLattices.Nondegenerate = NondegenerateRationalLattices
RationalLattices.Integral = IntegralRationalLattices
RationalLattices.Even = EvenRationalLattices
RationalLattices.Unimodular = UnimodularRationalLattices
RationalLattices.Definite = DefiniteRationalLattices
RationalLattices.PositiveDefinite = PositiveDefiniteRationalLattices
RationalLattices.NegativeDefinite = NegativeDefiniteRationalLattices
RationalLattices.Indefinite = IndefiniteRationalLattices
RationalLattices.Embedded = EmbeddedRationalLattices
RationalLattices.WithDistinguishedBasis = WithDistinguishedBasisRationalLattices

DiscriminantGroups.FiniteBilinearForms = FiniteBilinearDiscriminantGroups
DiscriminantGroups.FiniteQuadraticForms = FiniteQuadraticDiscriminantGroups
DiscriminantGroups.Even = EvenDiscriminantGroups
DiscriminantGroups.WithSourceLattice = WithSourceLatticeDiscriminantGroups


def Lattices(base_ring=ZZ):
    r"""Return the synthetic lattice category over ``base_ring``."""
    return RationalLattices(base_ring)
