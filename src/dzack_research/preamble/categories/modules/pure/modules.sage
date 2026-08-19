r"""The owned category of modules over a ring.

An $R$-module is an additively commutative group $M$ together with a ring
morphism $\rho:R\to\operatorname{End}(M)$; the scalar action *is* $\rho$, by
$r\cdot m:=\rho(r)(m)$.  That morphism is the defining datum, so this category
requires it: an object placed here without one is visibly unfinished.

Requiring it is the point.  Sage's ``Modules(R)`` is a placement, and the
preamble's own constructors reached it by refinement, so a module could exist
having never constructed the thing that makes it a module.  Every defect this
layer has produced -- a free module built twice on one $(R,S)$, generators
that were a tuple in one path and a set in another -- came of structure being
implied rather than carried.

The obligation cannot be a gate: ``_refine_category_`` admits anything and no
hook runs.  What it can be is *visible*, which is what ``abstract_method``
gives -- an unmet obligation resolves to the declaration, and the constructor
sweep reports it.

Modelled on the spike's module neighbourhood and owned here.  Over a field the
category dispatches, since a vector space is what a module over a field is.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.categories.modules import Module

from typing import Self

from sage.categories.additive_groups import AdditiveGroups
from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.fields import Fields as SageFields
from sage.categories.modules import Modules as SageModules
from sage.misc.abstract_method import abstract_method


class Modules(Category_over_base_ring):
    r"""Modules over $R$: an additive group with a ring morphism from $R$."""

    @staticmethod
    def __classcall_private__(cls: type, base_ring: "Ring") -> "Category":
        if base_ring in SageFields():
            return VectorSpaces(base_ring)
        category: "Category" = Category_over_base_ring.__classcall__(cls, base_ring)
        return category

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules"

    def super_categories(self) -> list:
        # A module is an additively commutative group with a ring action,
        # so the additive structure files at the owned additive spine.
        from dzack_research.preamble.categories.group.magmas import AdditiveGroups as OwnedAdditiveGroups

        return [
            SageModules(self.base_ring()),
            OwnedAdditiveGroups(),
            AdditiveGroups().AdditiveCommutative(),
        ]

    def __contains__(self, module: "Module") -> bool:
        r"""Return whether ``module`` is an object of this category.

        Test category membership first.  This includes abelian groups, since
        each has a canonical structure as a module over the integers.  Sage's
        base-ring membership test decides all remaining cases.
        """
        if Category.__contains__(self, module):
            return True
        return Category_over_base_ring.__contains__(self, module)

    class ParentMethods:
        @abstract_method
        def _ring_morphism_defining_module_action(self: Self) -> "Morphism":
            r"""Return $\rho:R\to\operatorname{End}(M)$, which is the module.

            Not a convenience: this morphism is what being an $R$-module
            *is*, and the scalar action is read off it.  A constructor that
            cannot produce it has not built a module, whatever category it
            placed the object in.

            $\operatorname{End}(M)$ is taken where the additive structure
            lives, so it is the endomorphism ring in $R\text{-Mod}$.
            """

        def scalar_action(self: Self) -> "Morphism":
            r"""Return the action, under the name the mathematics uses."""
            return self._ring_morphism_defining_module_action()

        def scalar_multiple(self: Self, scalar: "Element", element: "Element") -> "Element":
            r"""Return $r\cdot m$, which is $\rho(r)(m)$ and nothing else."""
            return self.scalar_action()(scalar)(element)


class VectorSpaces(Category_over_base_ring):
    r"""Modules over a field, which is what this category dispatches to."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "vector spaces"

    def super_categories(self) -> list:
        from sage.categories.vector_spaces import VectorSpaces as SageVectorSpaces

        return [
            SageVectorSpaces(self.base_ring()),
            Category_over_base_ring.__classcall__(Modules, self.base_ring()),
        ]
