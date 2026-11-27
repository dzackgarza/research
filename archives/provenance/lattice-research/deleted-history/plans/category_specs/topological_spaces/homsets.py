r"""Hom, end, and aut categories for topological spaces."""

from __future__ import annotations

from typing import final, override

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..homsets import GenericAutCategory, GenericEndCategory, HomCategoryOf

class _TopologicalHomCategoryObjectMethods:
    r"""Topological hom parent methods; generic hom methods are inherited."""


class _ContinuousMaps:
    @abstract_method
    def is_continuous(self) -> bool:
        r"""Return whether this map is continuous."""
        ...


class _Homeomorphisms:
    @override
    @final
    def is_homeomorphism(self) -> bool:
        r"""Return ``True`` because this element is a homeomorphism."""
        return True


class _ShortMaps(_ContinuousMaps):
    @override
    @final
    def is_short(self) -> bool:
        r"""Return ``True`` because this element is a short map."""
        return True


class _Isometries:
    @override
    @final
    def is_isometry(self) -> bool:
        r"""Return ``True`` because this element is an isometry."""
        return True


class TopologicalSpaceHomCategory(HomCategoryOf):
    r"""Category of homs whose elements are continuous maps.

    Canonical chain: ``TopologicalSpaces().HomCategory()``.
    """

    @override
    @final
    def extra_super_categories(self):
        r"""Return the generic hom-category surface refined by continuous maps."""
        return [HomCategoryOf(self.base_category())]

    ParentMethods = _TopologicalHomCategoryObjectMethods
    ElementMethods = _ContinuousMaps
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "TopologicalSpaceEndCategory")


class TopologicalSpaceEndCategory(GenericEndCategory):
    r"""Canonical chain: ``TopologicalSpaces().EndCategory()``."""
    _base_category_class_and_axiom = (TopologicalSpaceHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "TopologicalSpaceAutCategory")

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...


class TopologicalSpaceAutCategory(GenericAutCategory):
    r"""Canonical chain: ``TopologicalSpaces().AutCategory()``."""
    _base_category_class_and_axiom = (TopologicalSpaceEndCategory, "Autset")

    class ParentMethods: ...
    ElementMethods = _Homeomorphisms
    class MorphismMethods: ...


class MetricSpaceHomCategory(TopologicalSpaceHomCategory):
    r"""Category of homs whose elements are short maps of metric spaces.

    Canonical chain: ``TopologicalSpaces().Metric().HomCategory()``.
    """

    @override
    @final
    def extra_super_categories(self):
        r"""Return the continuous-map hom category refined by short maps."""
        return [TopologicalSpaceHomCategory(self.base_category())]

    ElementMethods = _ShortMaps

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "MetricSpaceEndCategory")


class MetricSpaceEndCategory(GenericEndCategory):
    r"""Canonical chain: ``TopologicalSpaces().Metric().EndCategory()``."""
    _base_category_class_and_axiom = (MetricSpaceHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "MetricSpaceAutCategory")

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...


class MetricSpaceAutCategory(GenericAutCategory):
    r"""Canonical chain: ``TopologicalSpaces().Metric().AutCategory()``."""
    _base_category_class_and_axiom = (MetricSpaceEndCategory, "Autset")

    class ParentMethods: ...
    ElementMethods = _Isometries
    class MorphismMethods: ...
