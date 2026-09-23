r"""Toric blowups of smooth surfaces at torus-fixed points."""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.toric.fans import RationalPolyhedralFans
from dzack_research.preamble.categories.schemes.toric.toric_schemes import ToricSchemes


class ToricFixedPointBlowups(OwnedCategoryOverBaseRing):
    r"""Smooth toric surfaces obtained by blowing up one torus-fixed point.

    A torus-fixed point of a smooth toric surface is indexed by a maximal
    two-dimensional cone ``sigma = <u,v>``.  Its blowup is the star subdivision
    introducing the primitive ray ``u+v`` and replacing ``sigma`` by
    ``<u,u+v>`` and ``<u+v,v>`` (CLS Prop. 3.3.15).  The identity lattice map
    from the subdivided fan to the original fan is the blowdown morphism.

    The level datum is the blown-up surface, the center cone and the
    exceptional ray; an object is the toric variety of the subdivided fan,
    constructed in this category by :func:`_toric_fixed_point_blowup`.
    """

    def an_object(self):
        surface = ToricSchemes(self.base_ring()).an_object()
        return surface.toric_fixed_point_blowup(surface.fan().maximal_cones()[0])

    def super_categories(self):
        return [ToricSchemes(self.base_ring())]

    def _repr_object_names(self):
        return f"toric fixed-point blowups over {self.base_ring()}"

    class ParentMethods:
        def __init__(self, blowup_source, blowup_center_cone, exceptional_ray, **rest) -> None:
            self._blowup_source = blowup_source
            self._blowup_center_cone = blowup_center_cone
            self._exceptional_ray = exceptional_ray
            super().__init__(**rest)

        def is_toric_fixed_point_blowup(self) -> bool:
            return True

        def blowup_source(self):
            r"""The smooth toric surface whose fixed point was blown up."""
            return self._blowup_source

        @cached_method
        def blowup_morphism(self):
            r"""The blowdown ``Bl_p X -> X``, induced by the identity of ``N``.

            The star subdivision refines the fan of ``X``, so the identity
            lattice map is compatible and induces the toric morphism
            (CLS Thm. 3.3.4).
            """
            source = self.blowup_source()
            lattice = source.cocharacter_lattice()
            identity = lattice.module_category().Mor(lattice, lattice).identity()
            return self.toric_morphism(identity, source)

        blowdown = blowup_morphism

        def blowup_center_cone(self):
            r"""Return the maximal source-fan cone indexing the blown-up fixed point."""
            return self._blowup_center_cone

        def exceptional_ray(self):
            r"""The ray ``u+v`` of the subdivided fan, whose divisor is exceptional."""
            return self._exceptional_ray

        def exceptional_divisor(self):
            return self.torus_invariant_prime_divisor(self.exceptional_ray())

        def exceptional_self_intersection(self):
            exceptional = self.exceptional_divisor()
            return self.divisor_intersection(exceptional, exceptional)

        def _refined_ray_for_source_ray(self, source_ray):
            (source_vector,) = tuple(source_ray.rays())
            refined = next(
                (
                    target_ray
                    for target_ray in self.fan().cones(1)
                    if target_ray != self.exceptional_ray()
                    and tuple(target_ray.rays()) == (source_vector,)
                ),
                None,
            )
            assert refined is not None, (
                "star subdivision keeps every ray of the source fan"
            )
            return refined

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
            assert self.is_del_pezzo(), (
                "the degree (-K)^2 is taken of a del Pezzo surface"
            )
            anticanonical = -self.canonical_divisor()
            return self.divisor_intersection(anticanonical, anticanonical)


def _toric_fixed_point_blowup(surface, center_cone):
    r"""Blow up the torus-fixed point indexed by ``center_cone`` on a smooth toric surface.

    The star subdivision of the fan at ``center_cone`` is computed first; its
    toric variety is then constructed in ``ToricFixedPointBlowups(k)`` with the
    surface, the center cone and the new ray as that level's data.
    """
    base = surface.scheme_base_ring()
    assert surface in ToricSchemes(base), (
        "a torus-fixed point blowup is taken of a toric surface"
    )
    fan = surface.fan()
    assert int(fan.dimension()) == 2, (
        "the torus-fixed point blowup is constructed for surfaces"
    )
    assert fan.is_smooth(), (
        "the torus-fixed point blowup is constructed on a smooth source fan"
    )
    assert center_cone in fan.maximal_cones(), (
        "the blowup center is a maximal cone of the source fan"
    )
    assert center_cone.rays().cardinality() == 2, (
        "a torus-fixed point of a smooth toric surface is indexed by a two-ray cone"
    )
    first, second = tuple(center_cone.rays())
    new_ray_vector = first + second

    fans = RationalPolyhedralFans(fan.cocharacter_lattice())
    refined_fan = fans(
        tuple(
            subdivided
            for cone in fan.maximal_cones()
            for subdivided in (
                ((first, new_ray_vector), (new_ray_vector, second))
                if cone == center_cone
                else (tuple(cone.rays()),)
            )
        )
    )
    assert refined_fan.is_smooth(), (
        "the star subdivision of a smooth surface cone is smooth"
    )
    assert refined_fan.is_complete() or not fan.is_complete(), (
        "the star subdivision of a complete fan is complete"
    )
    exceptional = next(
        (
            ray_cone
            for ray_cone in refined_fan.cones(1)
            if tuple(ray_cone.rays()) == (new_ray_vector,)
        ),
        None,
    )
    assert exceptional is not None, (
        "the star subdivision contains the ray u+v"
    )
    return refined_fan.toric_variety(
        base,
        placements=(ToricFixedPointBlowups(base),),
        blowup_source=surface,
        blowup_center_cone=center_cone,
        exceptional_ray=exceptional,
    )


__all__ = ["ToricFixedPointBlowups"]
