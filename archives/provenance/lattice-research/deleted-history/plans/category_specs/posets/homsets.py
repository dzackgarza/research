r"""Hom, end, and aut categories for posets."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..cat import Category
from ..homsets import GenericAutCategory, GenericEndCategory, HomCategoryOf

if TYPE_CHECKING:
    from ..types import Poset


class _PosetHomCategoryObjectMethods:
    r"""Poset-specific hom parent methods; generic hom methods are inherited."""


class _OrderPreservingMaps:
    @abstract_method
    def is_order_preserving(self) -> bool:
        r"""Return whether this map preserves the partial order."""
        ...

    @abstract_method
    def is_order_embedding(self) -> bool:
        r"""Return whether this order-preserving map reflects the order."""
        ...


class _PosetEndomorphisms:
    r"""Endomorphisms of posets; generic endomorphism methods are inherited."""


class _PosetAutomorphisms:
    @final
    def is_order_automorphism(self) -> bool:
        r"""Return ``True`` because this morphism is an automorphism of posets."""
        return True


class PosetHomCategory(HomCategoryOf):
    r"""Category of homs whose elements are order-preserving maps.

    Canonical chain: ``Posets().HomCategory()``.
    """

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""Return the generic hom-category surface refined by order-preserving maps."""
        return [HomCategoryOf(self.base_category())]

    ParentMethods = _PosetHomCategoryObjectMethods
    ElementMethods = _OrderPreservingMaps
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "PosetEndCategory")


class PosetEndCategory(GenericEndCategory):
    r"""Canonical chain: ``Posets().EndCategory()``."""
    _base_category_class_and_axiom = (PosetHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "PosetAutCategory")

    class ParentMethods:
        @abstract_method
        def base_poset(self) -> Poset:
            r"""Return the poset whose endomorphisms this object contains."""
            ...

    ElementMethods = _PosetEndomorphisms
    class MorphismMethods: ...


class PosetAutCategory(GenericAutCategory):
    r"""Canonical chain: ``Posets().AutCategory()``."""
    _base_category_class_and_axiom = (PosetEndCategory, "Autset")

    class ParentMethods: ...
    ElementMethods = _PosetAutomorphisms
    class MorphismMethods: ...
