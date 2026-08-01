r"""Finitely generated free modules of finite rank with a chosen basis.

This file defines:
1. ``FinitelyGeneratedFreeModules``: the category of free modules of finite rank $n \ge 0$
   with a chosen ordered basis, declaring both ``FramedFreeModules(R)`` and
   ``FinitelyGeneratedModules(R)`` in its supercategories.
2. ``BasedFreeModule``: the owned parent $R^n$ of finite rank $n$.
"""

from typing import Any

from sage.categories.category_types import Category_over_base_ring
from sage.matrix.matrix0 import Matrix
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from sage.rings.integer import Integer as SageInteger


class FinitelyGeneratedFreeModules(Category_over_base_ring):
    r"""Category of finitely generated free modules of finite rank with a chosen basis."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely generated based free modules"

    def super_categories(self) -> list:
        return [
            FramedFreeModules(self.base_ring()),
            FinitelyGeneratedModules(self.base_ring()),
        ]

    class ParentMethods:
        r"""What a chosen finite basis of a free module makes askable."""

        def rank(self: Any) -> Any:
            r"""Return the number of basis elements, which is the finite rank."""
            return ZZ(self.ngens())


class BasedFreeModuleElement(ModuleElement):
    r"""An element of a based free module: its coordinates, and nothing else."""

    def __init__(self, parent: Any, coordinates: Any) -> None:
        ModuleElement.__init__(self, parent)
        self._coordinates_ = vector(parent.base_ring(), list(coordinates))
        assert len(self._coordinates_) == parent.ngens(), (
            f"{parent} has rank {parent.ngens()}, got "
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

    def __init__(self, base_ring: Any, generating_set: Any) -> None:
        assert not isinstance(generating_set, (int, SageInteger)), (
            "BasedFreeModule requires its framing set; use "
            "standard_framing_set(n) when the canonical [n] framing is intended; "
            f"got {generating_set!r}"
        )
        cardinality = generating_set.cardinality()
        self._rank = ZZ(cardinality)
        assert self._rank >= 0, f"a generating set cardinality is not negative, got {cardinality}"
        # The category goes in at construction, not only by the refinement
        # below: Sage discovers the base ring's action on this parent while
        # initializing it, and a category arriving afterwards is too late for
        # scalar multiplication by anything but the integers.
        Parent.__init__(
            self, base=base_ring, category=FinitelyGeneratedFreeModules(base_ring)
        )
        assert generating_set.category().is_subcategory(OrderedSets().TotallyOrdered()), (
            "a finitely generated free module requires a totally ordered framing set"
        )
        assert generating_set.cardinality() == self._rank, (
            "the free module rank must equal the cardinality of its framing set"
        )
        self._generating_set = generating_set
        refine(self, FinitelyGeneratedFreeModules(base_ring))
        self._framing_map = {
            e: self._from_coordinates(
                [self.base_ring()(i == j) for j in range(self._rank)]
            )
            for i, e in enumerate(self._generating_set)
        }
        self._gens = TotallyOrderedSet(tuple(self._framing_map.values()))

    def gens(self) -> TotallyOrderedFiniteSet:
        return self._gens

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


def standard_framing_set(rank: Any) -> Any:
    """Return the canonical ordered framing set ``[rank]`` for ``R^rank``."""
    rank = int(rank)
    assert rank >= 0, f"a free-module rank is not negative, got {rank}"
    return Sets.Δ[rank - 1]


def Free_ZZ(generating_set: Any) -> BasedFreeModule:
    r"""Construct the owned finitely generated free module over ``ZZ``.

    A supplied finite set is given the finite total order used by the
    finitely-generated framed layer at construction time; its actual elements
    remain the framing labels.
    """
    match generating_set.category().is_subcategory(OrderedSets().TotallyOrdered()):
        case True:
            ordered = generating_set
        case False:
            ordered = refine(
                TotallyOrderedFiniteSet(tuple(generating_set)),
                OrderedSets().TotallyOrdered(),
            )
    return BasedFreeModule(ZZ, ordered)
