r"""Hom, end, and aut categories for algebras."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from sage.misc.lazy_import import LazyImport

from ..cat import Category
from ..homsets import (
    GenericAutCategory,
    GenericEndCategory,
    HomCategoryOf,
    UniversalAutElementMethods,
    UniversalEndElementMethods,
    UniversalHomElementMethods,
    UniversalHomObjectMethods,
)

if TYPE_CHECKING:
    from ..types import Algebra, AlgebraIdeal


class _AlgebraHomCategoryObjectMethods(UniversalHomObjectMethods):
    r"""Algebra-specific hom parent methods; generic hom methods are inherited."""


class _AlgebraHomomorphisms(UniversalHomElementMethods):
    @abstractmethod
    def kernel(self) -> AlgebraIdeal:
        r"""Return the kernel ideal of this algebra homomorphism."""
        ...


class AlgebraHomCategory(HomCategoryOf):
    r"""Category of algebra homs.

    Canonical chain: ``Algebras(R).HomCategory()``.
    """

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""Return the generic hom-category surface refined by algebra maps."""
        return [HomCategoryOf(self.base_category())]

    ParentMethods = _AlgebraHomCategoryObjectMethods
    ElementMethods = _AlgebraHomomorphisms


    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "AlgebraEndCategory")


class AlgebraEndCategory(GenericEndCategory):
    r"""Canonical chain: ``Algebras(R).EndCategory()``."""

    _base_category_class_and_axiom = (AlgebraHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "AlgebraAutCategory")

    class ParentMethods:
        @abstractmethod
        def base_algebra(self) -> Algebra:
            r"""Return the algebra whose endomorphisms this object contains."""
            ...

    class ElementMethods(UniversalEndElementMethods): ...



class AlgebraAutCategory(GenericAutCategory):
    r"""Canonical chain: ``Algebras(R).AutCategory()``."""

    _base_category_class_and_axiom = (AlgebraEndCategory, "Autset")

    class ParentMethods: ...

    class ElementMethods(UniversalAutElementMethods): ...
