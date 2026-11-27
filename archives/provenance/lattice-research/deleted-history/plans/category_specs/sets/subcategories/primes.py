r"""One-object subcategory for Sage ``Primes()``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import SetElement


from ...cat import Category
from .. import Sets


class _PrimesSets(Category_singleton):
    r"""One-object category whose object is the full Sage set of prime integers.

    Prime subsets, including primes in arithmetic progressions, are subobjects of this
    object and are expressed through ``PrimeSubset`` and
    ``PrimesInArithmeticProgressions`` type vocabulary.

    Constructor target:
    ``Sets().Constructors().Primes()`` refines the full Sage prime set here.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable().Infinite().Facade()]

    class ParentMethods:
        @override
        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @override
        @abstract_method
        def _an_element_(self) -> SetElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...
