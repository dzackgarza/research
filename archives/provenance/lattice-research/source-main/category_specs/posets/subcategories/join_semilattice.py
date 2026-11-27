r"""Order-theoretic join-semilattice poset subcategory."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, cast, final, overload, override

from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...utils import with_axiom
from .. import Posets

if TYPE_CHECKING:
    from ...types import PosetElement

if TYPE_CHECKING:
    def foldable_operation[MethodT: Callable[..., object]](
        function: MethodT,
    ) -> MethodT: ...

    def cached_method[MethodT: Callable[..., object]](method: MethodT) -> MethodT: ...
else:

    from ...utils import foldable_operation


class _JoinSemilatticePosets(Category):
    r"""Posets in which every pair has a join.

    Canonical chain: ``Posets().JoinSemilattice()``.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return posets as the strict supercategory of join-semilattices."""
        return [Posets()]

    class SubcategoryMethods:
        @final
        def Finite(self) -> Category:
            r"""Return the finite join-semilattice subcategory."""
            return cast(Category, with_axiom(self, "Finite"))

    Finite = LazyImport(
        "category_specs.posets.subcategories.finite_join_semilattice",
        "_FiniteJoinSemilatticePosets",
    )

    class ParentMethods:
        @overload
        def join(self, x: PosetElement, y: PosetElement) -> PosetElement: ...

        @overload
        def join(self, elements: Sequence[PosetElement]) -> PosetElement: ...

        @abstractmethod
        @foldable_operation
        def join(self, x: PosetElement, y: PosetElement) -> PosetElement:
            r"""Return the least upper bound of ``x`` and ``y``.

            ``JoinSemilattice`` introduces ``join`` as the primitive binary
            operation; the sequence overload folds this binary operation.
            """
            ...

    class ElementMethods: ...
