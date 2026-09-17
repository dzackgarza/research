r"""Affine algebraic de Rham algebras of represented commutative algebras."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.algebras.differential_graded_algebras import (
    Differential,
    DifferentialGradedAlgebras,
)
from dzack_research.preamble.categories.algebras.restricted_graded_algebras import (
    RestrictedGradedAlgebra,
)
from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing


class _DeRhamConstruction:
    r"""The selected algebra and differential module defining its de Rham algebra."""

    def __init__(self, source_algebra, kahler_differentials) -> None:
        self._source_algebra = source_algebra
        self._kahler_differentials = kahler_differentials

    def source_algebra(self):
        return self._source_algebra

    def kahler_differentials(self):
        return self._kahler_differentials


class DeRhamAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The de Rham algebra of a finite dual-number presentation.

        The witness must inhabit the same represented cohomology route used by
        downstream DGA constructions.  A polynomial algebra over ``R`` is
        infinite as an ``R``-module, while the current cohomology owner retains
        finite presentations of cycles and boundaries.  The selected quotient
        ``R[x]/(x^2)`` is still nontrivial Kähler calculus and is finite free
        over ``R``.
        """
        ring = self.base_ring()
        polynomial = Algebras(ring).Associative().Unital().Commutative().an_object()
        label = next(iter(polynomial.algebra_generating_set()))
        generator = polynomial.algebra_generator(label)
        return self((polynomial).quotient_by_relations((generator**2,)))

    def _call_(self, algebra):
        r"""Construct ``Omega^*_{A/R}`` from the represented ``R``-algebra ``A``.

        The source algebra is the defining datum.  This category constructor
        owns the Kähler-differential/exterior-algebra realization and identity
        cache; ``A.de_rham_algebra()`` is the algebra's spelling of it.
        """
        if algebra not in Algebras(self.base_ring()).Associative().Unital().Commutative():
            raise TypeError(
                "an algebraic de Rham algebra is constructed from a commutative algebra over the same base ring"
            )
        return _de_rham_algebra_from_source(algebra)

    @classmethod
    def _repr_object_names(cls):
        return "algebraic de Rham algebras"

    def super_categories(self):
        return [DifferentialGradedAlgebras(self.base_ring()).Supercommutative().Alternating()]

    class ParentMethods:
        def de_rham_construction(self):
            return self._de_rham_construction

        def de_rham_source_algebra(self):
            return self.de_rham_construction().source_algebra()

        def kahler_differentials(self):
            return self.de_rham_construction().kahler_differentials()


def _de_rham_differential_on_extension(exterior_algebra, omega, universal_derivation, element):
    element = exterior_algebra(element)
    result = exterior_algebra.zero()
    for degree, component in element.homogeneous_components().items():
        source_piece = exterior_algebra.graded_piece(degree)
        target_degree = degree + 1
        if target_degree not in exterior_algebra.degree_index_set():
            continue
        target_piece = exterior_algebra.graded_piece(target_degree)
        target_component = target_piece.zero()
        for label, coefficient in source_piece.framing_coefficients(component).items():
            d_coefficient = universal_derivation(coefficient)
            if d_coefficient == omega.zero():
                continue
            if degree == 0:
                contribution = d_coefficient
            else:
                basis_element = source_piece.module_generator(label)
                contribution = omega.exterior_power_product(
                    1,
                    d_coefficient,
                    degree,
                    basis_element,
                )
            target_component += contribution
        if target_component != target_piece.zero():
            result += exterior_algebra.from_component(target_degree, target_component)
    return result


class _DeRhamAlgebra(RestrictedGradedAlgebra):
    r"""The de Rham algebra with source and differential constructor-owned."""

    def __init__(self, algebra, exterior, omega, ring_map) -> None:
        self._de_rham_construction = _DeRhamConstruction(algebra, omega)
        RestrictedGradedAlgebra.__init__(
            self,
            exterior,
            ring_map,
            extra_categories=(DeRhamAlgebras(algebra.base_ring()),),
        )
        universal = omega.universal_derivation()

        def differential(element):
            extension_element = self.realize(element)
            image = _de_rham_differential_on_extension(
                exterior,
                omega,
                universal,
                extension_element,
            )
            return self.from_realization(image)

        self._preamble_differential = Differential(self, differential)


@cached_function(key=lambda algebra: id(algebra))
def _de_rham_algebra_from_source(algebra):
    omega = algebra.kahler_differentials()
    exterior = omega.exterior_algebra()
    ring_map = algebra.algebra_structure_morphism()
    return _DeRhamAlgebra(algebra, exterior, omega, ring_map)


__all__ = ["DeRhamAlgebras"]
