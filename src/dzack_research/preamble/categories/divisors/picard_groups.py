"""Picard groups."""

from dzack_research.preamble.categories.divisors.divisor_groups import _divisor_role_specimen, _module_in_role
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.owned_category_bases import Category


class _PicardGroupConstruction:
    r"""The selected scheme defining one represented Picard group."""

    def __init__(self, scheme) -> None:
        self._scheme = scheme

    def scheme(self):
        return self._scheme


class _ProjectivePicardConstruction(_PicardGroupConstruction):
    r"""The projective-bundle decomposition defining a represented Picard group."""

    def __init__(self, scheme, base_picard_group, hyperplane_factor, biproduct) -> None:
        super().__init__(scheme)
        self._base_picard_group = base_picard_group
        self._hyperplane_factor = hyperplane_factor
        self._biproduct = biproduct

    def base_picard_group(self):
        return self._base_picard_group

    def hyperplane_factor(self):
        return self._hyperplane_factor

    def biproduct(self):
        return self._biproduct


class PicardGroups(Category):
    def an_object(self):
        return _divisor_role_specimen(self)

    @classmethod
    def _repr_object_names(cls):
        return "Picard groups"

    def super_categories(self):
        from sage.rings.integer_ring import ZZ as SageZZ

        return [FramedModules(_own_ring(SageZZ))]

    def trivial(self, scheme):
        r"""Return the represented zero Picard group for ``scheme``.

        This is an explicit construction for a scheme whose Picard triviality
        is already known; it does not assert or decide that theorem.
        """
        from sage.rings.integer_ring import ZZ as SageZZ

        from dzack_research.preamble.categories.sets.finite_ordered_sets import (
            finite_ordered_set,
        )

        integers = _own_ring(SageZZ)
        return self(
            integers.free_module(finite_ordered_set(())),
            scheme=scheme,
        )

    def _call_(self, module, scheme=None, construction=None):
        if module not in self.super_categories()[0]:
            raise TypeError("a Picard group must carry its quotient framing")
        if construction is None and scheme is not None:
            construction = _PicardGroupConstruction(scheme)
        if construction is not None and scheme is not None and construction.scheme() is not scheme:
            raise ValueError("the selected Picard construction is attached to a different scheme")
        return _module_in_role(
            module,
            self,
            "a Picard group requires a represented framed-module presentation",
            construction_data=(
                None
                if construction is None
                else {"_picard_group_construction": construction}
            ),
        )

    class ParentMethods:
        def picard_group_construction(self):
            construction = getattr(self, "_picard_group_construction", None)
            if construction is None:
                raise TypeError("this Picard-group role has no selected scheme")
            return construction

        def picard_scheme(self):
            return self.picard_group_construction().scheme()

        def _projective_picard_construction(self):
            construction = self.picard_group_construction()
            if not isinstance(construction, _ProjectivePicardConstruction):
                raise TypeError("this Picard group has no selected projective-bundle decomposition")
            return construction

        def projective_base_picard_group(self):
            return self._projective_picard_construction().base_picard_group()

        def projective_hyperplane_factor(self):
            return self._projective_picard_construction().hyperplane_factor()

        def projective_picard_biproduct(self):
            return self._projective_picard_construction().biproduct()

        def _from_projective_biproduct(self, element):
            decomposition = self.projective_picard_biproduct()
            return self.linear_combination(decomposition.framing_coefficients(element))

        def base_picard_inclusion(self):

            base = self.projective_base_picard_group()
            injection = self.projective_picard_biproduct().injection(0)
            return base.module_category().Mor(base, self)(
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
