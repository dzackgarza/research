r"""Affine algebraic de Rham algebras of represented commutative algebras."""

from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras
from dzack_research.preamble.categories.algebras.differential_graded_algebras import (
    Differential,
    StrictlyCommutativeDifferentialGradedAlgebras,
)
from dzack_research.preamble.categories.algebras.kahler_differentials import (
    KahlerDifferentials,
)
from dzack_research.preamble.categories.algebras.restricted_graded_algebras import (
    RestrictedGradedAlgebra,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing


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
        from dzack_research.preamble.categories.algebras.free_algebras import (
            FinitelyPresentedAlgebra,
        )

        ring = self.base_ring()
        polynomial = CommutativeAlgebras(ring).an_object()
        label = next(iter(polynomial.algebra_generating_set()))
        generator = polynomial.algebra_generator(label)
        return self(FinitelyPresentedAlgebra(polynomial, (generator**2,)))

    def _call_(self, algebra):
        r"""Construct ``Omega^*_{A/R}`` from the represented ``R``-algebra ``A``.

        The source algebra is the defining datum.  This category constructor
        owns the Kähler-differential/exterior-algebra realization and identity
        cache; :func:`DeRhamAlgebra` is notation for this operation.
        """
        if algebra not in CommutativeAlgebras(self.base_ring()):
            raise TypeError(
                "an algebraic de Rham algebra is constructed from a commutative algebra over the same base ring"
            )
        cached = _DE_RHAM_CACHE.get(id(algebra))
        if cached is not None and cached.de_rham_source_algebra() is algebra:
            return cached
        omega = algebra.kahler_differentials()
        exterior = omega.exterior_algebra()
        ring_map = algebra.algebra_structure_morphism()
        result = _DeRhamAlgebra(algebra, exterior, omega, ring_map)
        _DE_RHAM_CACHE[id(algebra)] = result
        return result

    @classmethod
    def _repr_object_names(cls):
        return "algebraic de Rham algebras"

    def super_categories(self):
        return [StrictlyCommutativeDifferentialGradedAlgebras(self.base_ring())]

    class ParentMethods:
        def de_rham_source_algebra(self):
            return self._preamble_de_rham_source_algebra

        def kahler_differentials(self):
            return self._preamble_kahler_differentials


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
        for label, coefficient in module_coefficients(component, source_piece).items():
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
            result += exterior_algebra._from_component(target_degree, target_component)
    return result


class _DeRhamAlgebra(RestrictedGradedAlgebra):
    r"""The de Rham algebra with source and differential constructor-owned."""

    def __init__(self, algebra, exterior, omega, ring_map) -> None:
        self._preamble_de_rham_source_algebra = algebra
        self._preamble_kahler_differentials = omega
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


_DE_RHAM_CACHE = {}


__all__ = ["DeRhamAlgebras"]
