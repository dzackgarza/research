r"""Sage category surfaces for the owned synthetic lattice spike.

Ratified organization (M-RATIFY): two SEPARATE categories, no shared root.

- ``Lattices(R)`` -- based free ``R``-modules with a symmetric ``K``-valued form,
  on ``Modules(R).WithBasis().FiniteDimensional()``. Possibly-degenerate base;
  ``Nondegenerate`` is an axiom attached by the constructor iff ``det(G) != 0``.
- ``DiscriminantForms(R)`` -- finite abelian groups (NOT "modules over ZZ")
  carrying a finite bilinear/quadratic form valued in a quotient module.

``K`` (the form value ring) is per-object via ``value_module()``; the categories
are parameterized by the module base ring ``R`` only. Shared form predicates live
in Python mixins keyed on abstract, fail-loud ``value_module()``/``gram_matrix``
hooks -- there is deliberately no mixin-level default for those hooks.
"""

from __future__ import annotations

from sage.categories.category_types import Category_over_base_ring
from sage.categories.category_with_axiom import (
    CategoryWithAxiom_over_base_ring,
    all_axioms,
    axiom,
)
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups
from sage.categories.homsets import HomsetsCategory
from sage.categories.modules import Modules
from sage.categories.sets_cat import Sets
from sage.misc.abstract_method import abstract_method
from sage.rings.integer_ring import ZZ


_FORM_AXIOMS = (
    "Nondegenerate",
    "Integral",
    "Even",
    "Unimodular",
    "Definite",
    "PositiveDefinite",
    "NegativeDefinite",
    "Indefinite",
    "Bilinear",
    "Quadratic",
    "WithSourceLattice",
)

for _axiom_name in _FORM_AXIOMS:
    if _axiom_name not in all_axioms:
        all_axioms.add(_axiom_name)


class Lattices(Category_over_base_ring):
    r"""Based free ``R``-modules with a symmetric ``K``-valued form.

    Base is possibly-degenerate; ``Nondegenerate`` is an axiom subcategory.
    """

    def _repr_object_names(self):
        return f"synthetic lattices over {self.base_ring()}"

    def super_categories(self):
        return [Modules(self.base_ring()).WithBasis().FiniteDimensional()]

    def additional_structure(self):
        return self

    class SubcategoryMethods:
        Nondegenerate = axiom("Nondegenerate")
        Integral = axiom("Integral")
        Even = axiom("Even")
        Unimodular = axiom("Unimodular")
        Definite = axiom("Definite")
        PositiveDefinite = axiom("PositiveDefinite")
        NegativeDefinite = axiom("NegativeDefinite")
        Indefinite = axiom("Indefinite")

    class ParentMethods:
        @abstract_method
        def value_ring(self):
            r"""Return the value ring of the bilinear form."""

        @abstract_method
        def rational_span(self):
            r"""Return ``self tensor_ZZ QQ`` with its induced bilinear form."""

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
        pass

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


class DiscriminantForms(Category_over_base_ring):
    r"""Finite abelian groups with a discriminant bilinear/quadratic form.

    Typed as a finite abelian group (fixing Sage's "modules over ZZ" mis-typing);
    the form is extra structure layered on the group.
    """

    def _repr_object_names(self):
        return f"synthetic discriminant forms over {self.base_ring()}"

    def super_categories(self):
        return [CommutativeAdditiveGroups().Finite()]

    def additional_structure(self):
        return self

    class SubcategoryMethods:
        Bilinear = axiom("Bilinear")
        Quadratic = axiom("Quadratic")
        Nondegenerate = axiom("Nondegenerate")
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

    class MorphismMethods:
        pass


class NondegenerateLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "Nondegenerate")


class IntegralLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "Integral")


class EvenLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "Even")

    def extra_super_categories(self):
        return (Lattices(self.base_ring()).Integral(),)


class UnimodularLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "Unimodular")

    def extra_super_categories(self):
        return (Lattices(self.base_ring()).Integral(),)


class DefiniteLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "Definite")


class PositiveDefiniteLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "PositiveDefinite")

    def extra_super_categories(self):
        return (Lattices(self.base_ring()).Definite(),)

    class ParentMethods:
        def _positive_definite_algorithm_not_implemented(self, name):
            raise NotImplementedError(f"{name} is gated to positive-definite lattices but is not implemented in this spike")

        def LLL(self):
            from sage.matrix.constructor import matrix
            from sage.rings.integer_ring import ZZ

            if not (self.base_ring() is ZZ):
                raise ValueError("LLL is implemented only for ZZ-lattices in this spike")
            if not (self.is_integral()):
                raise ValueError(f"LLL requires an integral Gram matrix; gram={self.gram_matrix()}")
            change_of_basis = matrix(ZZ, self.gram_matrix()).LLL_gram()
            return self.sublattice(change_of_basis, label="LLL")

        def BKZ(self, block_size=10, **kwargs):
            from sage.matrix.constructor import matrix
            from sage.rings.integer_ring import ZZ

            if not (self.base_ring() is ZZ):
                raise ValueError("BKZ is implemented only for ZZ-lattices in this spike")
            if not (self.is_integral()):
                raise ValueError(f"BKZ requires an integral Gram matrix; gram={self.gram_matrix()}")
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

            if not (self.base_ring() is ZZ):
                raise ValueError("short vector enumeration is implemented only for ZZ-lattices in this spike")
            if not (self.is_integral()):
                raise ValueError(f"short vector enumeration requires an integral Gram matrix; gram={self.gram_matrix()}")
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
            if not (len(target) == self.rank()):
                raise ValueError("closest vector target must have one coordinate per lattice basis vector; "
                f"rank={self.rank()}, target={target}")
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


class NegativeDefiniteLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "NegativeDefinite")

    def extra_super_categories(self):
        return (Lattices(self.base_ring()).Definite(),)


class IndefiniteLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "Indefinite")


class BilinearDiscriminantForms(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantForms, "Bilinear")


class QuadraticDiscriminantForms(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantForms, "Quadratic")

    def extra_super_categories(self):
        return (DiscriminantForms(self.base_ring()).Bilinear(),)


class NondegenerateDiscriminantForms(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantForms, "Nondegenerate")


class EvenDiscriminantForms(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantForms, "Even")

    def extra_super_categories(self):
        return (DiscriminantForms(self.base_ring()).Quadratic(),)


class WithSourceLatticeDiscriminantForms(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantForms, "WithSourceLattice")


Lattices.Nondegenerate = NondegenerateLattices
Lattices.Integral = IntegralLattices
Lattices.Even = EvenLattices
Lattices.Unimodular = UnimodularLattices
Lattices.Definite = DefiniteLattices
Lattices.PositiveDefinite = PositiveDefiniteLattices
Lattices.NegativeDefinite = NegativeDefiniteLattices
Lattices.Indefinite = IndefiniteLattices

DiscriminantForms.Bilinear = BilinearDiscriminantForms
DiscriminantForms.Quadratic = QuadraticDiscriminantForms
DiscriminantForms.Nondegenerate = NondegenerateDiscriminantForms
DiscriminantForms.Even = EvenDiscriminantForms
DiscriminantForms.WithSourceLattice = WithSourceLatticeDiscriminantForms
