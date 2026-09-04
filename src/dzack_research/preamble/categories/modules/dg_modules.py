r"""Graded modules and differential graded modules over a represented DGA."""

from dzack_research.preamble.categories.abstract_categories.objects import OwnedParameterizedCategory

from dzack_research.preamble.refine import refine


class GradedAlgebraModules(OwnedParameterizedCategory):
    r"""Right graded modules over one selected graded algebra ``A``."""

    @classmethod
    def _repr_object_names(cls):
        return "graded modules over a graded algebra"

    def graded_algebra(self):
        return self.base()

    def super_categories(self):
        from dzack_research.preamble.categories.modules.graded_modules import GradedModules

        algebra = self.graded_algebra()
        return [GradedModules(algebra.base_ring(), algebra.grading_monoid())]

    class ParentMethods:
        def graded_algebra(self):
            return self._preamble_graded_algebra

        def right_action(self):
            return self._preamble_graded_algebra_action

        def act(self, module_element, algebra_element):
            return self.right_action()(module_element, algebra_element)


class DifferentialGradedModules(OwnedParameterizedCategory):
    r"""Right differential graded modules over one selected DGA ``(A,d)``."""

    @classmethod
    def _repr_object_names(cls):
        return "differential graded modules"

    def dga(self):
        return self.base()

    def super_categories(self):
        from dzack_research.preamble.categories.modules.cochain_complexes import CochainComplexes

        dga = self.dga()
        return [
            GradedAlgebraModules(dga),
            CochainComplexes(dga.base_ring()),
        ]

    class ParentMethods:
        def dga(self):
            return self._preamble_dg_algebra

        def is_differential_graded_module(self) -> bool:
            return True


def regular_dg_module(dga):
    r"""Read a DGA as its canonical right DG-module over itself."""
    dga._preamble_graded_algebra = dga
    dga._preamble_dg_algebra = dga
    dga._preamble_graded_algebra_action = lambda module_element, algebra_element: (
        module_element * algebra_element
    )
    return refine(dga, DifferentialGradedModules(dga))


__all__ = [
    "DifferentialGradedModules",
    "GradedAlgebraModules",
    "regular_dg_module",
]
