"""Picard groups."""

from sage.categories.category import Category

from dzack_research.preamble.categories.divisors.divisor_groups import _module_in_role
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


class PicardGroups(Category):
    @classmethod
    def _repr_object_names(cls):
        return "Picard groups"

    def super_categories(self):
        from sage.rings.integer_ring import ZZ as SageZZ

        return [FramedModules(_own_ring(SageZZ))]

    class ParentMethods:
        def picard_scheme(self):
            scheme = getattr(self, "_preamble_picard_scheme", None)
            if scheme is None:
                raise TypeError("this Picard-group role has no selected scheme")
            return scheme

        def projective_base_picard_group(self):
            base = getattr(self, "_preamble_projective_base_picard_group", None)
            if base is None:
                raise TypeError("this Picard group has no selected projective-bundle decomposition")
            return base

        def projective_hyperplane_factor(self):
            factor = getattr(self, "_preamble_projective_hyperplane_factor", None)
            if factor is None:
                raise TypeError("this Picard group has no selected O(1) factor")
            return factor

        def projective_picard_biproduct(self):
            decomposition = getattr(self, "_preamble_projective_picard_biproduct", None)
            if decomposition is None:
                raise TypeError("this Picard group has no selected projective-bundle decomposition")
            return decomposition

        def _from_projective_biproduct(self, element):
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_coefficients

            decomposition = self.projective_picard_biproduct()
            return self.linear_combination(module_coefficients(element, decomposition))

        def base_picard_inclusion(self):
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

            base = self.projective_base_picard_group()
            injection = self.projective_picard_biproduct().injection(0)
            return module_homset(base, self)(
                {
                    label: self._from_projective_biproduct(injection(base.module_generator(label)))
                    for label in base.module_generating_set()
                }
            )

        def hyperplane_class(self):
            factor = self.projective_hyperplane_factor()
            label = factor.module_generating_set()[0]
            image = self.projective_picard_biproduct().injection(1)(factor.module_generator(label))
            return self._from_projective_biproduct(image)


def PicardGroup(module, scheme=None, construction_data=None):
    category = PicardGroups()
    if module not in category.super_categories()[0]:
        raise TypeError("a Picard group must carry its quotient framing")
    data = dict(construction_data or {})
    if scheme is not None:
        data["picard_scheme"] = scheme
    return _module_in_role(
        module,
        category,
        "a Picard group requires a represented framed-module presentation",
        construction_data=data or None,
    )
