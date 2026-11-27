"""Hom/end/aut layer for ``Rings()``."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, cast, final, override, TypeAlias

from sage.misc.lazy_import import LazyImport

from ..homsets import (
    GenericAutCategory,
    GenericEndCategory,
    HomCategoryOf,
    UniversalAutElementMethods,
    UniversalEndElementMethods,
    UniversalHomElementMethods,
    UniversalHomObjectMethods,
)
from ..utils import refine_category

if TYPE_CHECKING:
    from ..types import Category, Ideal, Ring, RingAut, RingEnd, RingHom, RingMorphism


class _RingHomCategoryObjectMethods(UniversalHomObjectMethods):
    r"""Ring-specific hom parent methods; generic hom methods are inherited."""


class _RingHomomorphisms(UniversalHomElementMethods):
    @abstractmethod
    def is_zero(self) -> bool: ...

    @abstractmethod
    def kernel(self) -> Ideal: ...

    @abstractmethod
    def extend_to_fraction_field(self) -> RingMorphism: ...


class _RingEndomorphisms(UniversalEndElementMethods):
    r"""Ring-specific endomorphism methods; generic endomorphism methods are
    inherited.
    """


class _RingAutomorphisms(UniversalAutElementMethods):
    r"""Ring-specific automorphism methods; generic automorphism methods are
    inherited.
    """


class RingHomCategory(HomCategoryOf):
    r"""Canonical chain: ``Rings().HomCategory()``."""

    @classmethod
    @final
    def from_sage_hom(cls, hom: RingHom) -> RingHom:
        from . import Rings

        return refine_category(hom, Rings().HomCategory())  # type: ignore[call-arg]

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        return [HomCategoryOf(self.base_category())]

    ParentMethods : TypeAlias = _RingHomCategoryObjectMethods
    ElementMethods : TypeAlias = _RingHomomorphisms

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "RingEndCategory")


class RingEndCategory(GenericEndCategory):
    r"""Canonical chain: ``Rings().EndCategory()``."""

    _base_category_class_and_axiom = (RingHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "RingAutCategory")

    @classmethod
    @final
    def from_sage_end(cls, end: RingEnd) -> RingEnd:
        from . import Rings

        return refine_category(end, Rings().EndCategory())

    class ParentMethods:
        @abstractmethod
        def category(self) -> RingEndCategory: ...

        @abstractmethod
        def base_ring(self) -> Ring:
            """If this is End(R), return R."""
            ...

        @final
        def unit_group(self) -> RingAut:
            return cast("RingAut", self.category().AutCategory().from_end_category(self))

    ElementMethods : TypeAlias = _RingEndomorphisms


class RingAutCategory(GenericAutCategory):
    r"""Canonical chain: ``Rings().AutCategory()``."""

    _base_category_class_and_axiom = (RingEndCategory, "Autset")

    class ParentMethods:
        @abstractmethod
        def end_category(self) -> RingEndCategory.ParentMethods: ...

        @final
        def base_ring(self) -> Ring:
            return self.end_category().base_ring()

        @final
        def unit_group(self) -> RingAut:
            return self

    ElementMethods : TypeAlias = _RingAutomorphisms
