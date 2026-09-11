r"""Owned Chow-group roles for represented algebraic cycles."""

from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyPresentedModules,
    FreeModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)


class ChowGroups(OwnedCategoryOverBaseRing):
    r"""Finitely presented ``ZZ``-modules carrying one scheme and cycle degree."""

    @classmethod
    def _repr_object_names(cls):
        return "Chow groups"

    def super_categories(self):
        return [FinitelyPresentedModules(self.base_ring())]

    class ParentMethods:
        def chow_scheme(self):
            return self._preamble_chow_scheme

        def cycle_dimension(self):
            return self._preamble_cycle_dimension

        def cycle_codimension(self):
            return int(self.chow_scheme().dimension()) - int(self.cycle_dimension())


class TorusInvariantCycleGroups(OwnedCategoryOverBaseRing):
    r"""Free ``ZZ``-modules on orbit closures in one fixed dimension."""

    @classmethod
    def _repr_object_names(cls):
        return "torus-invariant cycle groups"

    def super_categories(self):
        return [FreeModules(self.base_ring())]

    class ParentMethods:
        def cycle_scheme(self):
            return self._preamble_cycle_scheme

        def cycle_dimension(self):
            return self._preamble_cycle_dimension

        def cycle_codimension(self):
            return int(self.cycle_scheme().dimension()) - int(self.cycle_dimension())


def ChowGroup(module, scheme, cycle_dimension):
    r"""Read ``module`` as ``A_cycle_dimension(scheme)`` without changing it."""
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        _SelectedFinitePresentationModules,
    )

    ring = module.base_ring()
    if module not in _SelectedFinitePresentationModules(ring):
        raise TypeError("a represented Chow group requires a selected finite presentation")
    result = module._same_presentation_module(
        module.module_generating_set(),
        _extra_categories=(ChowGroups(ring),),
        _extra_construction_data={
            "chow_scheme": scheme,
            "cycle_dimension": int(cycle_dimension),
        },
    )
    return result


__all__ = ["ChowGroup", "ChowGroups", "TorusInvariantCycleGroups"]
