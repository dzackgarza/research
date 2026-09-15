r"""Toric blowups of smooth surfaces at torus-fixed points."""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.schemes import _refine_scheme
from dzack_research.preamble.categories.schemes.toric.fans import RationalPolyhedralFans
from dzack_research.preamble.categories.schemes.toric.toric_schemes import ToricSchemes


class ToricFixedPointBlowups(OwnedCategoryOverBaseRing):
    r"""Smooth toric surfaces obtained by blowing up one torus-fixed point.

    A torus-fixed point of a smooth toric surface is indexed by a maximal
    two-dimensional cone ``sigma = <u,v>``.  Its blowup is the star subdivision
    introducing the primitive ray ``u+v`` and replacing ``sigma`` by
    ``<u,u+v>`` and ``<u+v,v>``.  The identity lattice map from the subdivided
    fan to the original fan is the blowdown morphism.
    """

    def an_object(self):
        surface = ToricSchemes(self.base_ring()).an_object()
        return surface.toric_fixed_point_blowup(surface.fan().maximal_cones()[0])

    def super_categories(self):
        return [ToricSchemes(self.base_ring())]

    def _repr_object_names(self):
        return f"toric fixed-point blowups over {self.base_ring()}"

    def __contains__(self, candidate) -> bool:
        return (
            candidate in ToricSchemes(self.base_ring())
            and getattr(candidate, "_preamble_blowup_source", None) is not None
            and getattr(candidate, "_preamble_exceptional_ray", None) is not None
        )

    class ParentMethods:
        def is_toric_fixed_point_blowup(self) -> bool:
            return True

        def blowup_source(self):
            return self._preamble_blowup_source

        def blowup_morphism(self):
            return self._preamble_blowup_morphism

        blowdown = blowup_morphism

        def blowup_center_cone(self):
            r"""Return the maximal source-fan cone indexing the blown-up fixed point."""
            return self._preamble_blowup_center_cone

        def exceptional_ray(self):
            return self._preamble_exceptional_ray

        def exceptional_divisor(self):
            return self.torus_invariant_prime_divisor(self.exceptional_ray())

        def exceptional_self_intersection(self):
            exceptional = self.exceptional_divisor()
            return self.divisor_intersection(exceptional, exceptional)

        def _refined_ray_for_source_ray(self, source_ray):
            (source_vector,) = tuple(source_ray.rays())
            for target_ray in self.fan().cones(1):
                if target_ray == self.exceptional_ray():
                    continue
                (target_vector,) = tuple(target_ray.rays())
                if _same_ray_vector(source_vector, target_vector):
                    return target_ray
            raise ArithmeticError("a source ray disappeared from the star subdivision")

        def strict_transform_divisor(self, divisor):
            r"""Return the strict transform of a torus-invariant divisor.

            Star subdivision preserves every old ray.  The strict transform
            keeps the coefficient on each preserved prime divisor and has
            coefficient zero on the exceptional prime.  This is independent
            of the total transform supplied by :meth:`blowup_morphism`.
            """
            source = self.blowup_source()
            source_group = source.weil_divisor_group()
            target_group = self.weil_divisor_group()
            divisor = source_group(divisor)
            coefficients = source_group.framing_coefficients(divisor)
            return target_group.linear_combination(
                {
                    self._refined_ray_for_source_ray(ray): coefficient
                    for ray, coefficient in coefficients.items()
                    if coefficient != source_group.base_ring().zero()
                }
            )

        @cached_method
        def picard_pullback_morphism(self):
            r"""Return ``f^*: Pic(X) -> Pic(Bl_p X)`` for the toric blowdown.

            The map is induced from the existing Cartier-divisor pullback.  Its
            construction through the quotient presentations verifies that
            principal-divisor relations vanish after pullback.
            """
            source = self.blowup_source()
            source_picard = source.picard_group()
            target_picard = self.picard_group()
            source_weil = source.weil_divisor_group()
            target_weil = self.weil_divisor_group()

            def image(label):
                pulled = self.blowup_morphism().pullback_divisor(
                    source_weil.module_generator(label)
                )
                coefficients = target_weil.framing_coefficients(pulled)
                return target_picard.linear_combination(coefficients)

            return source_picard.module_category().Mor(source_picard, target_picard)(image)

        def exceptional_picard_class(self):
            return self.picard_group().module_generator(self.exceptional_ray())

        def is_del_pezzo(self) -> bool:
            r"""Decide the del Pezzo condition in the complete toric-surface regime."""
            if not self.fan().is_complete():
                return False
            return self.is_ample(-self.canonical_divisor())

        def del_pezzo_degree(self):
            r"""Return ``(-K)^2`` for a represented toric del Pezzo blowup."""
            if not self.is_del_pezzo():
                raise ValueError("the represented toric blowup is not a del Pezzo surface")
            anticanonical = -self.canonical_divisor()
            return self.divisor_intersection(anticanonical, anticanonical)


def _same_ray_vector(left, right) -> bool:
    return bool(left == right)


def _toric_fixed_point_blowup(surface, center_cone):
    r"""Blow up the torus-fixed point indexed by ``center_cone`` on a smooth toric surface."""
    base = surface.scheme_base_ring()
    if surface not in ToricSchemes(base):
        raise TypeError("the represented fixed-point blowup requires a toric surface")
    fan = surface.fan()
    if int(fan.dimension()) != 2:
        raise ValueError("the represented toric fixed-point blowup is for surfaces")
    if not fan.is_smooth():
        raise ValueError("the represented toric fixed-point blowup requires a smooth source fan")
    if center_cone not in fan.maximal_cones():
        raise ValueError("the blowup center is a maximal cone of the source fan")

    center_rays = tuple(center_cone.rays())
    if len(center_rays) != 2:
        raise ValueError("a torus-fixed point on a smooth toric surface is indexed by a two-ray cone")
    first, second = center_rays
    new_ray_vector = first + second

    refined_maximal_cones = []
    for cone in fan.maximal_cones():
        if cone == center_cone:
            refined_maximal_cones.extend(((first, new_ray_vector), (new_ray_vector, second)))
        else:
            refined_maximal_cones.append(tuple(cone.rays()))

    fans = RationalPolyhedralFans(fan.cocharacter_lattice())
    refined_fan = fans(tuple(refined_maximal_cones))
    if not refined_fan.is_smooth():
        raise ArithmeticError("star subdivision of a smooth surface cone did not remain smooth")
    if fan.is_complete() and not refined_fan.is_complete():
        raise ArithmeticError("star subdivision of a complete fan did not remain complete")

    blowup = refined_fan.toric_variety(base)
    lattice = fan.cocharacter_lattice()
    identity = lattice.module_category().Mor(lattice, lattice).identity()
    blowdown = blowup.toric_morphism(identity, surface)

    exceptional = None
    for ray_cone in refined_fan.cones(1):
        (primitive,) = tuple(ray_cone.rays())
        if _same_ray_vector(primitive, new_ray_vector):
            exceptional = ray_cone
            break
    if exceptional is None:
        raise ArithmeticError("the star-subdivision ray is absent from the refined fan")

    blowup._preamble_blowup_source = surface
    blowup._preamble_blowup_morphism = blowdown
    blowup._preamble_blowup_center_cone = center_cone
    blowup._preamble_exceptional_ray = exceptional
    return _refine_scheme(blowup, base, [ToricFixedPointBlowups(base)])


__all__ = ["ToricFixedPointBlowups"]
