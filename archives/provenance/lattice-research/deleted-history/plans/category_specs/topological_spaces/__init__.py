r"""Topological-space category surface.

Topological spaces are sets with a topology. This subtree owns the category
``TopologicalSpaces()`` and its metric-space subcategory. The set category exposes
``Sets().Topological()`` and ``Sets().Metric()`` as the same mathematical
categories, not as set-local duplicates.

Subcategory hierarchy::

    TopologicalSpaces() = Sets().Topological()
    |-- Connected()
    |-- Compact()
    |-- Metric() = Sets().Metric()
    |-- Subobjects()
    |-- Quotients()
    |-- Subquotients()
    |-- ObjectsOver()
    |-- ObjectsUnder()
    |-- CartesianProducts()
    `-- HomCategory()
        |-- EndCategory()
        `-- AutCategory()

Named set constructors live under ``Sets().Constructors()`` and refine into this
category when they carry topological structure. ``TopologicalSpaces().Constructors()``
is reserved for constructors whose primary mathematical output is a topological space,
not for every named set with a topology.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import Category
from ..cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ..sets import Sets
from .homsets import (
    MetricSpaceAutCategory,
    MetricSpaceEndCategory,
    MetricSpaceHomCategory,
    TopologicalSpaceAutCategory,
    TopologicalSpaceEndCategory,
    TopologicalSpaceHomCategory,
)
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.objects_over import _ObjectsOver
from .subcategories.constructions.objects_under import _ObjectsUnder
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients

if TYPE_CHECKING:
    from ..types import Subset


class _TopologicalSpaceObjectMethods:
    r"""Methods on objects in the category of topological spaces."""

    @override
    @final
    def is_topological(self) -> bool:
        r"""Return ``True`` because this object lies in ``TopologicalSpaces()``."""
        return True

    @abstract_method
    def is_connected(self) -> bool:
        r"""Return whether this topological space is connected."""
        ...

    @abstract_method
    def closure(self, U: Subset) -> Subset:
        r"""Return the closure of ``U`` in this topological space."""
        ...

    @abstract_method
    def interior(self, U: Subset) -> Subset:
        r"""Return the interior of ``U`` in this topological space."""
        ...

    @abstract_method
    def boundary(self, U: Subset) -> Subset:
        r"""Return the boundary of ``U`` in this topological space."""
        ...

    @abstract_method
    def is_open(self, U: Subset) -> bool:
        r"""Return whether ``U`` is open in this topological space."""
        ...

    @abstract_method
    def is_closed(self, U: Subset) -> bool:
        r"""Return whether ``U`` is closed in this topological space."""
        ...

    @abstract_method
    def is_compact(self) -> bool:
        r"""Return whether this topological space is compact."""
        ...


class _TopologicalSpaceElementMethods:
    r"""Methods on points of topological spaces."""


class _TopologicalSpaceMorphismMethods:
    r"""Methods on morphisms of topological spaces."""


class TopologicalSpaces(CategoryWithAxiom):
    r"""Category of topological spaces.

    Canonical chain: ``TopologicalSpaces()``.
    """

    _base_category_class_and_axiom = (Sets, "Topological")
    ParentMethods = _TopologicalSpaceObjectMethods
    ElementMethods = _TopologicalSpaceElementMethods
    MorphismMethods = _TopologicalSpaceMorphismMethods
    HomCategory = TopologicalSpaceHomCategory
    Metric = LazyImport("category_specs.topological_spaces.subcategories.metric", "MetricSpacesCategory")
    Connected = LazyImport("category_specs.topological_spaces.subcategories.connected", "_ConnectedTopologicalSpaces")
    Compact = LazyImport("category_specs.topological_spaces.subcategories.compact", "_CompactTopologicalSpaces")

    @override
    @final
    def _sage_super_categories(self) -> tuple[Category, ...]:
        return (SageSets().Topological(),)

    @override
    @final
    def _repr_object_names(self) -> str:
        return "topological spaces"

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return the set-theoretic supercategories of topological spaces."""
        return [SageSets().Topological(), Sets()]

    class Constructors:
        r"""Topological-space constructors.

        No standalone Sage topological-space constructor has been admitted. Named sets
        such as real intervals are constructed under ``Sets().Constructors()`` and
        refined into this subtree.
        """

    _Constructors = Constructors

    @cached_method
    @final
    def Constructors(self):
        r"""Return the topological-space constructor collector."""
        return self.__class__._Constructors()

    class SubcategoryMethods:
        @cached_method
        @final
        def Connected(self) -> Category:
            r"""Return the connected-space subcategory."""
            return self._with_axiom("Connected")

        @cached_method
        @final
        def Compact(self) -> Category:
            r"""Return the compact-space subcategory."""
            return self._with_axiom("Compact")

        @cached_method
        @final
        def Metric(self) -> Category:
            r"""Return the metric-space subcategory."""
            return self._with_axiom("Metric")

    Subobjects = _Subobjects
    Quotients = _Quotients
    Subquotients = _Subquotients
    ObjectsOver = _ObjectsOver
    ObjectsUnder = _ObjectsUnder
    CartesianProducts = _CartesianProducts

from .subcategories.metric import MetricSpacesCategory

MetricSpacesObject = MetricSpacesCategory.ParentMethods
MetricSpacesElement = MetricSpacesCategory.ElementMethods
MetricSpacesMorphism = MetricSpacesCategory.MorphismMethods
MetricSpacesHomCategory = MetricSpaceHomCategory
MetricSpacesEndCategory = MetricSpaceEndCategory
MetricSpacesAutCategory = MetricSpaceAutCategory
MetricSpacesHom = MetricSpaceHomCategory.ParentMethods
MetricSpacesEnd = MetricSpaceEndCategory.ParentMethods
MetricSpacesAut = MetricSpaceAutCategory.ParentMethods
MetricSpacesEndomorphism = MetricSpaceEndCategory.ElementMethods
MetricSpacesAutomorphism = MetricSpaceAutCategory.ElementMethods


TopologicalSpacesCategory = TopologicalSpaces
TopologicalSpacesObject = TopologicalSpaces.ParentMethods
TopologicalSpacesElement = TopologicalSpaces.ElementMethods
TopologicalSpacesMorphism = TopologicalSpaces.MorphismMethods
TopologicalSpacesHomCategory = TopologicalSpaceHomCategory
TopologicalSpacesEndCategory = TopologicalSpaceEndCategory
TopologicalSpacesAutCategory = TopologicalSpaceAutCategory
TopologicalSpacesHom = TopologicalSpaceHomCategory.ParentMethods
TopologicalSpacesEnd = TopologicalSpaceEndCategory.ParentMethods
TopologicalSpacesAut = TopologicalSpaceAutCategory.ParentMethods
TopologicalSpacesEndomorphism = TopologicalSpaceEndCategory.ElementMethods
TopologicalSpacesAutomorphism = TopologicalSpaceAutCategory.ElementMethods
