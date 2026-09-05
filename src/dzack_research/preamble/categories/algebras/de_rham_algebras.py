r"""Affine algebraic de Rham algebras of represented commutative algebras."""

from sage.misc.cachefunc import cached_function
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
from dzack_research.preamble.categories.modules.powers import alternating_power_product
from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.algebras.framed_free_algebras import AlternatingAlgebraOf


class DeRhamAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The algebraic de Rham algebra of the polynomial algebra on one generator."""
        from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras
        from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebra

        ring = self.base_ring()
        return DeRhamAlgebra(CommutativeAlgebras(ring).an_object())

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
        target_piece = exterior_algebra.graded_piece(degree + 1)
        target_component = target_piece.zero()
        for label, coefficient in module_coefficients(component, source_piece).items():
            d_coefficient = universal_derivation(coefficient)
            if d_coefficient == omega.zero():
                continue
            if degree == 0:
                contribution = d_coefficient
            else:
                basis_element = source_piece.module_generator(label)
                contribution = alternating_power_product(
                    omega,
                    1,
                    d_coefficient,
                    degree,
                    basis_element,
                )
            target_component += contribution
        if target_component != target_piece.zero():
            result += exterior_algebra._from_component(degree + 1, target_component)
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


@cached_function(key=lambda algebra: id(algebra))
def DeRhamAlgebra(algebra):
    r"""Return the strictly commutative DGA ``Omega^*_{A/R}``.

    The exterior algebra itself is the existing authoritative
    ``AlternatingAlgebraOf(Omega^1_{A/R})``.  The public DGA is its restriction
    from the degree-zero coefficient algebra ``A`` to the differential
    constants ``R`` along the selected algebra structure morphism.
    """

    omega = KahlerDifferentials(algebra)
    exterior = AlternatingAlgebraOf(omega)
    ring_map = algebra.algebra_structure_morphism()
    return _DeRhamAlgebra(algebra, exterior, omega, ring_map)


__all__ = ["DeRhamAlgebra", "DeRhamAlgebras"]
