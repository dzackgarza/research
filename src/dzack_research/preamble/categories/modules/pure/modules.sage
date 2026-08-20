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
    from sage.categories.morphism import Morphism
    from sage.structure.parent import Parent
    from dzack_research.preamble.owned_category import ConstructionData

from typing import Self

from sage.categories.additive_groups import AdditiveGroups
from sage.categories.category import Category
from dzack_research.preamble.owned_category_bases import Category_over_base_ring
from dzack_research.preamble.owned_category_bases import HomsetsCategory
from sage.categories.fields import Fields as SageFields
from sage.categories.modules import Modules as SageModules
from sage.misc.abstract_method import abstract_method
from sage.structure.element import Element as SageElement
from sage.structure.element import ModuleElement


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
            ...

        def scalar_action(self: Self) -> "Morphism":
            r"""Return the action, under the name the mathematics uses."""
            return self._ring_morphism_defining_module_action()

        def scalar_multiple(self: Self, scalar: "Element", element: "Element") -> "Element":
            r"""Return $r\cdot m$, which is $\rho(r)(m)$ and nothing else."""
            return self.scalar_action()(scalar)(element)

    class Homsets(HomsetsCategory):
        r"""$\operatorname{Hom}_R(M,N)$ of two modules over one ring."""

        class ParentMethods:
            def __init__(
                self,
                domain: "Module",
                codomain: "Module",
                **rest: "ConstructionData",
            ) -> None:
                assert domain.base_ring() == codomain.base_ring(), (
                    "module morphisms require the same base ring"
                )
                super().__init__(
                    domain=domain,
                    codomain=codomain,
                    base=domain.base_ring(),
                    check=False,
                    **rest,
                )

            def _element_constructor_(self, images: "ConstructionData") -> "Morphism":
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

                return ModuleMorphism(self, images)

            def zero(self) -> "Morphism":
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
                from dzack_research.preamble.categories.sets.owned_sets import Sets
                from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet
                from sage.categories.homset import Hom
                from sage.categories.morphism import SetMorphism

                return ModuleMorphism(
                    self,
                    SetMorphism(
                        Hom(
                            self.domain().module_generating_set(),
                            UnderlyingSet(self.codomain()),
                            Sets(),
                        ),
                        lambda element_of_S: self.codomain().zero(),
                    ),
                )

            def identity(self) -> "Morphism":
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

                assert self.domain() is self.codomain(), (
                    "an identity belongs to an endomorphism homset"
                )
                return ModuleMorphism(
                    self,
                    self.domain().module_generator_morphism(),
                )

            def __contains__(self, morphism: "ConstructionData") -> bool:
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

                return (
                    isinstance(morphism, ModuleMorphism)
                    and morphism.parent() is self
                )

            def _repr_(self) -> str:
                return f"Hom({self.domain()}, {self.codomain()})"

    class ElementMethods(ModuleElement):
        r"""An element of a module: where Sage's module element enters the chain.

        The module level is where addition acquires scalars, so this is where
        ``ModuleElement`` enters, as ``Element`` enters at the set level and
        ``Parent`` at the parent root.  Sage finds the scalar action only for a
        ``ModuleElement`` (``sage/structure/coerce_actions.pyx``), so without
        this an element of a chain-built module has no $r\cdot m$ at all.
        """

        def __init__(self: Self, parent: "Parent", **rest: "ConstructionData") -> None:
            ModuleElement.__init__(self, parent)

        def __bool__(self: Self) -> bool:
            r"""Return whether this element differs from $0$.

            Sage states this for every element -- an element is true when it is
            not the zero of its parent -- and also declares it abstract on
            ``AdditiveMagmas.AdditiveUnital``.  In category order that
            declaration precedes the implementation, so the implementation is
            named here, on the level whose objects have a zero.
            """
            return SageElement.__bool__(self)


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
