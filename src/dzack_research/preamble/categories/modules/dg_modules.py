r"""Graded modules and differential graded modules over a represented DGA."""

from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.modules.cochain_complexes import CochainComplexes
from dzack_research.preamble.categories.modules.graded_modules import GradedModules


class GradedAlgebraModules(OwnedParameterizedCategory):
    r"""Right graded modules over one selected graded algebra ``A``."""

    def an_object(self):
        r"""The graded algebra this category is over, as a module over itself."""
        return self.base()

    @classmethod
    def _repr_object_names(cls):
        return "graded modules over a graded algebra"

    def graded_algebra(self):
        return self.base()

    def parameter_category(self):
        r"""The graded algebras over the parameter's own base and grading monoid."""
        from dzack_research.preamble.categories.algebras.graded_algebras import (
            GradedAlgebras,
        )

        algebra = self.parameter()
        return GradedAlgebras(algebra.base_ring(), algebra.grading_monoid())

    def super_categories(self):

        algebra = self.graded_algebra()
        return [GradedModules(algebra.base_ring(), algebra.grading_monoid())]

    def __contains__(self, obj):
        if obj is self.graded_algebra():
            return obj in GradedModules(obj.base_ring(), obj.grading_monoid())
        return super().__contains__(obj)

    class ParentMethods:
        def graded_algebra(self):
            return self._preamble_graded_algebra

        def right_action(self):
            return self._preamble_graded_algebra_action

        def act(self, module_element, algebra_element):
            return self.right_action()(module_element, algebra_element)


class DifferentialGradedModules(OwnedParameterizedCategory):
    r"""Right differential graded modules over one selected DGA ``(A,d)``."""

    def an_object(self):
        r"""The DGA this category is over, as a module over itself."""
        return self.base()

    @classmethod
    def _repr_object_names(cls):
        return "differential graded modules"

    def dga(self):
        return self.base()

    def parameter_category(self):
        r"""The differential graded algebras over the parameter's own base."""
        from dzack_research.preamble.categories.algebras.differential_graded_algebras import (
            DifferentialGradedAlgebras,
        )

        return DifferentialGradedAlgebras(self.parameter().base_ring())

    def super_categories(self):

        dga = self.dga()
        return [
            GradedAlgebraModules(dga),
            CochainComplexes(dga.base_ring()),
        ]

    def __contains__(self, obj):
        if obj is self.dga():
            from dzack_research.preamble.categories.algebras.differential_graded_algebras import (
                DifferentialGradedAlgebras,
            )

            return obj in DifferentialGradedAlgebras(obj.base_ring())
        return super().__contains__(obj)

    class ParentMethods:
        def dga(self):
            return self._preamble_dg_algebra

        def is_differential_graded_module(self) -> bool:
            return True



__all__ = [
    "DifferentialGradedModules",
    "GradedAlgebraModules",
]
