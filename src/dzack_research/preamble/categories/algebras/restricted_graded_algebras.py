r"""Restriction of scalar constants for represented graded power algebras."""

from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets

from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumElement,
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.modules.restricted_scalars import restrict_scalars
from dzack_research.preamble.categories.rings import owned_ring_view
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.refine import refine


class RestrictedGradedAlgebraElement(GradedDirectSumElement):
    def _mul_(self, other):
        return self.parent().multiply(self, other)


class RestrictedGradedAlgebra(GradedDirectSumModule):
    r"""The same graded ring read over the constants of its degree-zero algebra."""

    Element = RestrictedGradedAlgebraElement

    def __init__(self, extension_algebra, ring_map) -> None:
        self._extension_algebra = extension_algebra
        self._ring_map = ring_map
        self._degree_zero_algebra = extension_algebra.base_ring()
        base = owned_ring_view(ring_map.domain())
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

        GradedDirectSumModule.__init__(
            self,
            base,
            piece,
            name=f"{extension_algebra} over {base}",
            realize_generator=realize_generator,
            realized_object=extension_algebra,
            from_realization=from_realization,
        )

        from dzack_research.preamble.categories.algebras import (
            FramedAlgebras,
            GradedAlgebras,
            StrictlyGradedCommutativeAlgebras,
        )

        categories = [
            GradedAlgebras(base),
            StrictlyGradedCommutativeAlgebras(base),
        ]
        try:
            degree_zero_labels = tuple(self.degree_zero_algebra().algebra_generating_set())
            degree_one_labels = tuple(extension_algebra.free_source_module().module_generating_set())
        except (AttributeError, TypeError):
            self._preamble_algebra_generating_set = None
        else:
            self._preamble_algebra_generating_set = finite_ordered_set(
                tuple(("degree zero", label) for label in degree_zero_labels)
                + tuple(("degree one", label) for label in degree_one_labels)
            )
            self._preamble_algebra_generator_values = {
                ("degree zero", label): self.from_degree_zero(
                    self.degree_zero_algebra().algebra_generator(label)
                )
                for label in degree_zero_labels
            }
            self._preamble_algebra_generator_values.update(
                {
                    ("degree one", label): self.from_realization(
                        self.extension_algebra().algebra_generator(label)
                    )
                    for label in degree_one_labels
                }
            )
            categories.append(FramedAlgebras(base))
        refine(self, categories)

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
        return SetMorphism(
            Hom(self.base_ring(), self, Sets()),
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


_RESTRICTED_GRADED_CACHE = {}


def restrict_graded_algebra_scalars(algebra, ring_map):
    key = (id(algebra), id(ring_map))
    cached = _RESTRICTED_GRADED_CACHE.get(key)
    if cached is not None and cached.extension_algebra() is algebra and cached.ring_map() is ring_map:
        return cached
    result = RestrictedGradedAlgebra(algebra, ring_map)
    _RESTRICTED_GRADED_CACHE[key] = result
    return result


__all__ = [
    "RestrictedGradedAlgebra",
    "RestrictedGradedAlgebraElement",
    "restrict_graded_algebra_scalars",
]
