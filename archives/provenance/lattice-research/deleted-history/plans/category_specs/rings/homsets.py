"""Hom/end/aut layer for ``Rings()``."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..homsets import GenericAutCategory, GenericEndCategory, HomCategoryOf
from ..utils import refine_category

if TYPE_CHECKING:
    from ..types import Ideal, Ring, RingAut, RingEnd, RingHom, RingMorphism


class _RingHomCategoryObjectMethods:
    r"""Ring-specific hom parent methods; generic hom methods are inherited."""


class _RingHomomorphisms:
    @abstract_method
    def is_zero(self) -> bool: ...

    @abstract_method
    def kernel(self) -> Ideal: ...

    @abstract_method
    def section(self) -> RingMorphism: ...


class _RingEndomorphisms:
    r"""Ring-specific endomorphism methods; generic endomorphism methods are inherited."""


class _RingAutomorphisms:
    r"""Ring-specific automorphism methods; generic automorphism methods are inherited."""


class RingHomCategory(HomCategoryOf):
    r"""Canonical chain: ``Rings().HomCategory()``."""

    @classmethod
    @final
    def from_sage_hom(cls, hom: RingHom) -> RingHom:
        from . import Rings

        return refine_category(hom, Rings().HomCategory())

    @override
    @final
    def extra_super_categories(self):
        return [HomCategoryOf(self.base_category())]

    ParentMethods = _RingHomCategoryObjectMethods
    ElementMethods = _RingHomomorphisms
    class MorphismMethods: ...

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
        @abstract_method
        def base_ring(self) -> Ring:
            """If this is End(R), return R."""
            ...

        @final
        def unit_group(self) -> RingAut:
            return self.category().AutCategory().from_end_category(self)

    ElementMethods = _RingEndomorphisms
    class MorphismMethods: ...


class RingAutCategory(GenericAutCategory):
    r"""Canonical chain: ``Rings().AutCategory()``."""
    _base_category_class_and_axiom = (RingEndCategory, "Autset")

    class ParentMethods:
        @final
        def base_ring(self) -> Ring:
            return self.end_category().base_ring()

        @final
        def unit_group(self) -> RingAut:
            return self

    ElementMethods = _RingAutomorphisms
    class MorphismMethods: ...
