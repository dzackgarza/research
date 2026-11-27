r"""Parameterized category of G-sets."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.categories.category import Category
from sage.categories.g_sets import GSets as SageGSets
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Group, GroupElement, Set, SetElement, Subset

from .. import Sets


class _GSets(Category):
    r"""Sets equipped with an action of a fixed group ``G``.

    Canonical chain: ``Sets().GSets(G)``.
    """

    @override
    @final
    def __init__(self, acting_group: Group, base_category: Category | None = None) -> None:
        Category.__init__(self)
        self._acting_group = acting_group
        self._base_category = Sets() if base_category is None else base_category

    @final
    def acting_group(self) -> Group:
        r"""Return the group acting on the objects of this category."""
        return self._acting_group

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"{self._acting_group}-sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [self._base_category, SageGSets(self._acting_group)]

    class ParentMethods:
        @abstract_method
        def acting_group(self) -> Group:
            r"""Return the group acting on this set."""
            ...

        @abstract_method
        def action(self, g: GroupElement, x: SetElement) -> SetElement:
            r"""Return the action of ``g`` on ``x``."""
            ...

        @abstract_method
        def orbit(self, x: SetElement) -> Set:
            r"""Return the orbit of ``x`` under the acting group."""
            ...

        @abstract_method
        def stabilizer(self, x: SetElement) -> Group:
            r"""Return the stabilizer subgroup of ``x``."""
            ...

        @abstract_method
        def fixed_points(self, subgroup: Group | None = None) -> Subset:
            r"""Return elements fixed by ``subgroup`` or by the full acting group."""
            ...

    class ElementMethods:
        @abstract_method
        def act_by(self, g: GroupElement) -> SetElement:
            r"""Return the result of acting on this element by ``g``."""
            ...

    class MorphismMethods: ...
