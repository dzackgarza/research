r"""Owned categories of groups."""

from typing import Any

from sage.categories.category import Category
from sage.categories.finite_groups import FiniteGroups as SageFiniteGroups
from sage.categories.groups import Groups as SageGroups
from sage.misc.latex import latex


class OwnedGroups(Category):
    r"""Groups whose notebook-facing methods are owned by the preamble."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "groups"

    def super_categories(self) -> list:
        return [SageGroups()]

    class ParentMethods:
        def _latex_(self: Any) -> str:
            r"""Return the group displayed by its distinguished generators."""
            generators = tuple(self.gens())
            if not generators:
                return r"\{1\}"
            entries = ", ".join(str(latex(generator)) for generator in generators)
            return rf"\left\langle {entries} \right\rangle"


class OwnedFiniteGroups(Category):
    r"""Finite groups whose notebook-facing methods are owned by the preamble."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finite groups"

    def super_categories(self) -> list:
        return [OwnedGroups(), SageFiniteGroups()]
