r"""Finitely generated free modules of finite rank with a chosen basis.

This file defines:
1. ``FinitelyGeneratedModules``: the category of finitely generated modules over a base ring $R$,
   constructed via Sage's ``CategoryWithAxiom_over_base_ring`` framework for the ``FinitelyGenerated`` axiom.
2. ``FinitelyGeneratedFreeModules``: the category of free modules of finite rank $n \ge 0$
   with a chosen ordered basis, declaring both ``FreeModules(R)`` and
   ``FinitelyGeneratedModules(R)`` in its supercategories.
3. ``BasedFreeModule``: the owned parent $R^n$ of finite rank $n$.
"""

from typing import Any

import sage.categories.category_with_axiom as cwa
from sage.categories.category_types import Category_over_base_ring
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.modules import Modules
from sage.matrix.matrix0 import Matrix
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp

# 1. Register FinitelyGenerated axiom string if not present in Sage's axiom container
if "FinitelyGenerated" not in cwa.all_axioms:
    cwa.all_axioms.add("FinitelyGenerated")


class FinitelyGeneratedModules(CategoryWithAxiom_over_base_ring):
    r"""Category of finitely generated modules over a base ring."""

    _base_category_class_and_axiom = (Modules, "FinitelyGenerated")

    class ParentMethods:
        def is_finitely_generated(self: Any) -> bool:
            r"""Return whether this module is finitely generated.

            Always ``True`` for objects in this category.
            """
            return True


setattr(Modules, "FinitelyGenerated", FinitelyGeneratedModules)


class FinitelyGeneratedFreeModules(Category_over_base_ring):
    r"""Category of finitely generated free modules of finite rank with a chosen basis."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely generated based free modules"

    def super_categories(self) -> list:
        return [
            FreeModules(self.base_ring()),
            FinitelyGeneratedModules(self.base_ring()),
        ]

    class ParentMethods:
        r"""What a chosen finite basis of a free module makes askable."""

        def rank(self: Any) -> Any:
            r"""Return the number of basis elements, which is the finite rank."""
            return ZZ(self.num_module_generators())


class BasedFreeModuleElement(ModuleElement):
    r"""An element of a based free module: its coordinates, and nothing else."""

    def __init__(self, parent: Any, coordinates: Any) -> None:
        ModuleElement.__init__(self, parent)
        self._coordinates_ = vector(parent.base_ring(), list(coordinates))
        assert len(self._coordinates_) == parent.num_module_generators(), (
            f"{parent} has rank {parent.num_module_generators()}, got "
            f"{len(self._coordinates_)} coordinates"
        )

    def _coordinates(self) -> Any:
        r"""Return the coordinates in the parent's basis."""
        return self._coordinates_

    def _add_(self, other: Any) -> "BasedFreeModuleElement":
        return self.parent()._from_coordinates(self._coordinates_ + other._coordinates_)

    def _sub_(self, other: Any) -> "BasedFreeModuleElement":
        return self.parent()._from_coordinates(self._coordinates_ - other._coordinates_)

    def _neg_(self) -> "BasedFreeModuleElement":
        return self.parent()._from_coordinates(-self._coordinates_)

    def _lmul_(self, factor: Any) -> "BasedFreeModuleElement":
        return self.parent()._from_coordinates(
            self.parent().base_ring()(factor) * self._coordinates_
        )

    _rmul_ = _lmul_

    def _richcmp_(self, other: Any, op: int) -> bool:
        return richcmp(self._coordinates_, other._coordinates_, op)

    def __hash__(self) -> int:
        return hash(tuple(self._coordinates_))

    def __iter__(self):
        return iter(self._coordinates_)

    def _repr_(self) -> str:
        return repr(self._coordinates_)


class BasedFreeModule(Parent):
    r"""Finitely generated based free module $R^n$ of finite rank $n$ with its standard basis.

    Named for what it is rather than ``FreeModule``, which is Sage's factory
    and stays reachable: this universe's free module and Sage's are different
    objects, and shadowing the name would make which one a caller got depend on
    import order.
    """

    Element = BasedFreeModuleElement

    def __init__(self, base_ring: Any, rank: Any) -> None:
        self._rank = ZZ(rank)
        assert self._rank >= 0, f"a rank is not negative, got {rank}"
        # The category goes in at construction, not only by the refinement
        # below: Sage discovers the base ring's action on this parent while
        # initializing it, and a category arriving afterwards is too late for
        # scalar multiplication by anything but the integers.
        Parent.__init__(
            self, base=base_ring, category=FinitelyGeneratedFreeModules(base_ring)
        )
        refine(self, FinitelyGeneratedFreeModules(base_ring))

    def gens(self) -> tuple:
        return tuple(
            self._from_coordinates(
                [self.base_ring()(i == j) for j in range(self._rank)]
            )
            for i in range(self._rank)
        )

    def ngens(self) -> int:
        return int(self._rank)

    def zero(self) -> BasedFreeModuleElement:
        return self._from_coordinates([self.base_ring().zero()] * self._rank)

    def _from_coordinates(self, coordinates: Any) -> BasedFreeModuleElement:
        return self.element_class(self, coordinates)

    def _element_constructor_(self, x: Any) -> BasedFreeModuleElement:
        r"""Return the element ``x`` names.

        A coordinate vector is accepted, because here it is an element: the
        basis is part of this object, so its entries already mean something.
        What is refused is an element of a *different* module, which is a map's
        business and not a constructor's.
        """
        if isinstance(x, BasedFreeModuleElement):
            assert x.parent() is self, (
                f"{x} belongs to {x.parent()}; carrying it here is a morphism's "
                "job, not a constructor's"
            )
            return x
        return self._from_coordinates(x)

    def __contains__(self, x: Any) -> bool:
        return isinstance(x, BasedFreeModuleElement) and x.parent() is self

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, BasedFreeModule)
            and other.base_ring() is self.base_ring()
            and other._rank == self._rank
        )

    def __hash__(self) -> int:
        return hash((type(self).__name__, self.base_ring(), self._rank))

    def _repr_(self) -> str:
        return f"Free module of rank {self._rank} over {self.base_ring()}"
