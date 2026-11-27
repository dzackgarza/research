r"""Hom, end, and aut categories for topological spaces."""

from __future__ import annotations

from abc import abstractmethod
from typing import final, override, TypeAlias

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


class _TopologicalHomCategoryObjectMethods(UniversalHomObjectMethods):
    r"""Topological hom parent methods; generic hom methods are inherited."""


class _ContinuousMaps(UniversalHomElementMethods):
    @abstractmethod
    def is_continuous(self) -> bool:
        r"""Return whether this map is continuous."""
        ...


class _Homeomorphisms(_ContinuousMaps, UniversalAutElementMethods):
    @final
    def is_homeomorphism(self) -> bool:
        r"""Return ``True`` because this element is a homeomorphism."""
        return True


class _ShortMaps(_ContinuousMaps):
    @final
    def is_short(self) -> bool:
        r"""Return ``True`` because this element is a short map."""
        return True


class _Isometries(_ShortMaps, UniversalAutElementMethods):
    @final
    def is_isometry(self) -> bool:
        r"""Return ``True`` because this element is an isometry."""
        return True


class TopologicalSpaceHomCategory(HomCategoryOf):
    r"""Category of homs whose elements are continuous maps.

    Canonical chain: ``TopologicalSpaces().HomCategory()``.
    """

    @override
    def extra_super_categories(self) -> list[Category]:
        r"""Return the generic hom-category surface refined by continuous maps."""
        return [HomCategoryOf(self.base_category())]

    ParentMethods : TypeAlias = _TopologicalHomCategoryObjectMethods
    ElementMethods : TypeAlias = _ContinuousMaps


    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "TopologicalSpaceEndCategory")


class TopologicalSpaceEndCategory(GenericEndCategory):
    r"""Canonical chain: ``TopologicalSpaces().EndCategory()``."""

    _base_category_class_and_axiom = (TopologicalSpaceHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "TopologicalSpaceAutCategory")

    class ParentMethods: ...

    class ElementMethods(UniversalEndElementMethods): ...



class TopologicalSpaceAutCategory(GenericAutCategory):
    r"""Canonical chain: ``TopologicalSpaces().AutCategory()``."""

    _base_category_class_and_axiom = (TopologicalSpaceEndCategory, "Autset")

    class ParentMethods: ...

    ElementMethods : TypeAlias = _Homeomorphisms



class MetricSpaceHomCategory(TopologicalSpaceHomCategory):
    r"""Category of homs whose elements are short maps of metric spaces.

    Canonical chain: ``TopologicalSpaces().Metric().HomCategory()``.
    """

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""Return the continuous-map hom category refined by short maps."""
        return [TopologicalSpaceHomCategory(self.base_category())]

    ElementMethods : TypeAlias = _ShortMaps

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "MetricSpaceEndCategory")


class MetricSpaceEndCategory(GenericEndCategory):
    r"""Canonical chain: ``TopologicalSpaces().Metric().EndCategory()``."""

    _base_category_class_and_axiom = (MetricSpaceHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "MetricSpaceAutCategory")

    class ParentMethods: ...

    class ElementMethods(UniversalEndElementMethods): ...



class MetricSpaceAutCategory(GenericAutCategory):
    r"""Canonical chain: ``TopologicalSpaces().Metric().AutCategory()``."""

    _base_category_class_and_axiom = (MetricSpaceEndCategory, "Autset")

    class ParentMethods: ...

    ElementMethods : TypeAlias = _Isometries
