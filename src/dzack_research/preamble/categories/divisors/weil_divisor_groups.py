"""Weil divisor groups."""

from sage.categories.category import Category

from dzack_research.preamble.categories.divisors.divisor_groups import (
    DivisorGroups,
    _module_in_role,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


class WeilDivisorGroups(Category):
    @classmethod
    def _repr_object_names(cls):
        return "Weil divisor groups"

    def super_categories(self):
        return [DivisorGroups()]

    class ParentMethods:
        def divisor_scheme(self):
            scheme = getattr(self, "_preamble_divisor_scheme", None)
            if scheme is None:
                raise TypeError("this Weil-divisor role has no selected scheme")
            return scheme

        def prime_divisor_locus(self):
            locus = getattr(self, "_preamble_prime_divisor_locus", None)
            if locus is None:
                raise TypeError("this Weil-divisor role has no represented full prime-divisor locus")
            return locus

        def affine_divisor_coordinate_ring(self):
            ring = getattr(self, "_preamble_affine_divisor_coordinate_ring", None)
            if ring is None:
                raise TypeError("this Weil-divisor role is not an affine-normal divisor group")
            return ring

        def prime_divisor(self, point):
            spectrum = self.affine_divisor_coordinate_ring().spectrum()
            if getattr(point, "parent", lambda: None)() is not spectrum:
                point = spectrum(point)
            if point not in self.prime_divisor_locus():
                raise ValueError("a Weil prime divisor is a height-one point")
            return self.module_generator(point)

        def multiplicity(self, divisor, point):
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_coefficients

            spectrum = self.affine_divisor_coordinate_ring().spectrum()
            if getattr(point, "parent", lambda: None)() is not spectrum:
                point = spectrum(point)
            return module_coefficients(divisor, self).get(point, self.base_ring().zero())

        def principal_divisor(self, rational_function):
            from dzack_research.preamble.categories.divisors.general_divisors import principal_weil_divisor

            return principal_weil_divisor(self, rational_function)


def WeilDivisorGroup(module, scheme=None):
    from sage.rings.integer_ring import ZZ as SageZZ

    if module not in FramedFreeModules(_own_ring(SageZZ)):
        raise TypeError("Weil divisors are free on specified codimension-one subvarieties")
    return _module_in_role(
        module,
        WeilDivisorGroups(),
        "a Weil divisor group requires a represented free-module presentation",
        construction_data=None if scheme is None else {"divisor_scheme": scheme},
    )
