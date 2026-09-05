r"""Restriction of scalar constants for represented graded power algebras."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumElement,
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.modules.pure.modules import restrict_scalars
from dzack_research.preamble.categories.rings.ring_foundation import (
    _owned_ring,
    ring_morphism,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.algebras.algebras import FramedAlgebras
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.algebras.graded_commutative_algebras import StrictlyGradedCommutativeAlgebras
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import (
    CoproductOfFamily,
    Sets,
)


class RestrictedGradedAlgebraElement(GradedDirectSumElement):
    def _mul_(self, other):
        return self.parent().multiply(self, other)


class RestrictedGradedAlgebra(GradedDirectSumModule):
    r"""The same graded ring read over the constants of its degree-zero algebra."""

    Element = RestrictedGradedAlgebraElement

    def __init__(self, extension_algebra, ring_map, *, extra_categories=()) -> None:
        self._extension_algebra = extension_algebra
        self._ring_map = ring_map
        self._degree_zero_algebra = extension_algebra.base_ring()
        base = _owned_ring(ring_map.domain())
        self._preamble_algebra_base_ring = base
        self._restricted_pieces = {}

        def piece(degree):
            degree = int(degree)
            cached = self._restricted_pieces.get(degree)
            if cached is not None:
                return cached
            extension_piece = extension_algebra.graded_piece(degree)
            result = restrict_scalars(extension_piece, ring_map)
            self._restricted_pieces[degree] = result
            return result

        def realize_generator(degree, label):
            restricted_piece = piece(degree)
            underlying = restricted_piece.module_generator(label).underlying_element()
            return extension_algebra._from_component(degree, underlying)

        def from_realization(element):
            element = extension_algebra(element)
            return self.from_components(
                {
                    degree: piece(degree)(component)
                    for degree, component in element.homogeneous_components().items()
                }
            )

        categories = [
            GradedAlgebras(base),
            StrictlyGradedCommutativeAlgebras(base),
            *tuple(extra_categories),
        ]
        try:
            degree_zero_labels = self.degree_zero_algebra().algebra_generating_set()
            degree_one_labels = extension_algebra.free_source_module().module_generating_set()
        except (AttributeError, TypeError):
            self._preamble_algebra_generating_set = None
        else:
            framing = CoproductOfFamily(
                Sets.Δ[1],
                lambda index: degree_zero_labels if int(index) == 0 else degree_one_labels,
            )
            self._preamble_algebra_generating_set = framing

            def generator_value(tagged):
                if int(tagged.summand_index()) == 0:
                    return self.from_degree_zero(
                        self.degree_zero_algebra().algebra_generator(
                            tagged.summand_element()
                        )
                    )
                return self.from_realization(
                    self.extension_algebra().algebra_generator(
                        tagged.summand_element()
                    )
                )

            self._preamble_algebra_generator_values = indexed_family(
                framing,
                generator_value,
                name="Restricted graded-algebra generators",
            )
            categories.append(FramedAlgebras(base))
        GradedDirectSumModule.__init__(
            self,
            base,
            piece,
            name=f"{extension_algebra} over {base}",
            realize_generator=realize_generator,
            realized_object=extension_algebra,
            from_realization=from_realization,
            extra_categories=tuple(categories),
        )

    def extension_algebra(self):
        return self._extension_algebra

    def degree_zero_algebra(self):
        return self._degree_zero_algebra

    def ring_map(self):
        return self._ring_map

    def algebra_base_ring(self):
        return self.base_ring()

    def multiply(self, left, right):
        return self.from_realization(self.realize(left) * self.realize(right))

    def realize(self, element):
        r"""Return the same finite homogeneous sum in the extension algebra.

        The restricted homogeneous pieces need not themselves carry a finite
        framing over the smaller constants ring.  Realization therefore uses
        the stored underlying element of each restricted piece directly,
        rather than expanding it in an artificial restricted-scalar basis.
        """
        element = self(element)
        result = self.extension_algebra().zero()
        for degree, component in element.homogeneous_components().items():
            underlying = (
                component.underlying_element()
                if hasattr(component, "underlying_element")
                else component
            )
            result += self.extension_algebra()._from_component(degree, underlying)
        return result

    def one(self):
        return self.from_realization(self.extension_algebra().one())

    def algebra_generating_set(self):
        if self._preamble_algebra_generating_set is None:
            raise NotImplementedError("this restricted graded algebra has no selected finite algebra framing")
        return self._preamble_algebra_generating_set

    def algebra_generator(self, label):
        kind, source_label = label
        if kind == "degree zero":
            return self.from_degree_zero(
                self.degree_zero_algebra().algebra_generator(source_label)
            )
        if kind == "degree one":
            return self.from_realization(
                self.extension_algebra().algebra_generator(source_label)
            )
        raise ValueError(f"unknown graded-algebra generator label {label!r}")

    def algebra_structure_morphism(self):
        return ring_morphism(
            self.base_ring(),
            self,
            lambda scalar: self.from_degree_zero(
                self.degree_zero_algebra()(self.ring_map()(scalar))
            ),
        )

    def from_degree_zero(self, element):
        return self.from_realization(self.extension_algebra()(element))

    def degree_zero_element(self, element):
        realized = self.realize(element)
        component = realized.homogeneous_component(0)
        coefficients = module_coefficients(component, realized.parent().graded_piece(0))
        scalar = coefficients.get(0, self.degree_zero_algebra().zero())
        return self.degree_zero_algebra()(scalar)


@cached_function(key=lambda algebra, ring_map: (id(algebra), id(ring_map)))
def restrict_graded_algebra_scalars(algebra, ring_map):
    result = RestrictedGradedAlgebra(algebra, ring_map)
    return result


__all__ = [
    "RestrictedGradedAlgebra",
    "RestrictedGradedAlgebraElement",
    "restrict_graded_algebra_scalars",
]
