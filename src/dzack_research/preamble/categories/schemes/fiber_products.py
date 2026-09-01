"""Affine scheme fiber products derived from commutative-algebra pushouts."""

from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.schemes import (
    AffineSchemes,
    SchemeMorphism,
    Spec,
    affine_spec_morphism,
    refine_scheme,
)


class FiberProductSchemes(OwnedCategoryOverBaseRing):
    r"""Affine schemes equipped as selected pullbacks of one cospan."""

    def super_categories(self):
        return [AffineSchemes(self.base_ring())]

    class ParentMethods:
        def fiber_product_cospan(self):
            return self._preamble_fiber_product_cospan

        def fiber_product_base(self):
            return self.fiber_product_cospan()[0].codomain()

        def fiber_product_projections(self):
            return self._preamble_fiber_product_projections

        def left_projection(self):
            return self.fiber_product_projections()[0]

        def right_projection(self):
            return self.fiber_product_projections()[1]

        def from_pullback_cone(self, left_map, right_map):
            r"""Return the unique represented map into this affine fiber product."""
            if left_map.domain() is not right_map.domain():
                raise ValueError("a pullback cone requires one common source")
            left_projection, right_projection = self.fiber_product_projections()
            if left_map.codomain() is not left_projection.codomain():
                raise ValueError("the left pullback-cone map has the wrong codomain")
            if right_map.codomain() is not right_projection.codomain():
                raise ValueError("the right pullback-cone map has the wrong codomain")
            algebra_pushout = self._preamble_fiber_product_algebra_pushout
            induced = algebra_pushout.from_pushout_cocone(
                left_map.coordinate_algebra_morphism(),
                right_map.coordinate_algebra_morphism(),
            )
            return affine_spec_morphism(induced)


def scheme_fiber_product(left_map, right_map):
    r"""Return ``X x_S Y`` for two represented affine scheme maps to ``S``."""
    if not isinstance(left_map, SchemeMorphism) or not isinstance(
        right_map, SchemeMorphism
    ):
        raise TypeError("a represented scheme fiber product is specified by scheme morphisms")
    if left_map.codomain() is not right_map.codomain():
        raise ValueError("fiber-product maps require one common codomain")

    left = left_map.domain()
    right = right_map.domain()
    base_scheme = left_map.codomain()
    base_ring = left.scheme_base_ring()
    affine = AffineSchemes(base_ring)
    if left not in affine or right not in affine or base_scheme not in affine:
        raise NotImplementedError(
            "the active scheme fiber-product backend currently requires affine schemes"
        )

    from dzack_research.preamble.categories.abstract_categories import Pushout

    algebra_pushout = Pushout(
        left_map.coordinate_algebra_morphism(),
        right_map.coordinate_algebra_morphism(),
    )
    product = Spec(algebra_pushout)
    left_projection = affine_spec_morphism(algebra_pushout.left_pushout_map())
    right_projection = affine_spec_morphism(algebra_pushout.right_pushout_map())
    product._preamble_fiber_product_cospan = (left_map, right_map)
    product._preamble_fiber_product_algebra_pushout = algebra_pushout
    product._preamble_fiber_product_projections = (
        left_projection,
        right_projection,
    )
    return refine_scheme(product, base_ring, [FiberProductSchemes(base_ring)])


__all__ = ["FiberProductSchemes", "scheme_fiber_product"]
