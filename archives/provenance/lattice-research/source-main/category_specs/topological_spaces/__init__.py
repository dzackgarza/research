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

from abc import abstractmethod
from collections.abc import Callable
from typing import TYPE_CHECKING, TypeVar, cast, final, override

from sage.misc.lazy_import import LazyImport

from ..cat import Category
from ..cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ..sets import Sets
from ..utils import with_axiom
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

_F = TypeVar("_F", bound=Callable[..., object])

if TYPE_CHECKING:
    from ..spec_core import ConstructorRegistry
    from ..types import Subset


class _TopologicalSpaceObjectMethods:
    r"""Methods on objects in the category of topological spaces."""

    @final
    def is_topological(self) -> bool:
        r"""Return ``True`` because this object lies in ``TopologicalSpaces()``."""
        return True

    @abstractmethod
    def is_connected(self) -> bool:
        r"""Return whether this topological space is connected."""
        ...

    @abstractmethod
    def closure_subset(self, U: Subset) -> Subset:
        r"""Return the closure of ``U`` in this topological space."""
        ...

    @abstractmethod
    def interior_subset(self, U: Subset) -> Subset:
        r"""Return the interior of ``U`` in this topological space."""
        ...

    @abstractmethod
    def boundary_subset(self, U: Subset) -> Subset:
        r"""Return the boundary of ``U`` in this topological space."""
        ...

    @abstractmethod
    def is_open_subset(self, U: Subset) -> bool:
        r"""Return whether ``U`` is open in this topological space."""
        ...

    @abstractmethod
    def is_closed_subset(self, U: Subset) -> bool:
        r"""Return whether ``U`` is closed in this topological space."""
        ...

    @abstractmethod
    def is_compact(self) -> bool:
        r"""Return whether this topological space is compact."""
        ...


class _TopologicalSpaceElementMethods:
    r"""Methods on points of topological spaces."""


class TopologicalSpaces(CategoryWithAxiom):
    r"""Category of topological spaces.

    Canonical chain: ``TopologicalSpaces()``.
    """

    _base_category_class_and_axiom = (Sets, "Topological")
    ParentMethods = _TopologicalSpaceObjectMethods
    ElementMethods = _TopologicalSpaceElementMethods
    HomCategory = TopologicalSpaceHomCategory
    Metric = LazyImport(
        "category_specs.topological_spaces.subcategories.metric", "MetricSpacesCategory"
    )
    Connected = LazyImport(
        "category_specs.topological_spaces.subcategories.connected",
        "_ConnectedTopologicalSpaces",
    )
    Compact = LazyImport(
        "category_specs.topological_spaces.subcategories.compact",
        "_CompactTopologicalSpaces",
    )

    @final
    def _sage_super_categories(self) -> tuple[Category, ...]:
        return ()

    @override
    @final
    def _repr_object_names(self) -> str:
        return "topological spaces"

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return the set-theoretic supercategories of topological spaces."""
        return [Sets()]

    class _Constructors:
        r"""Topological-space constructors.

        No standalone Sage topological-space constructor has been admitted. Named sets
        such as real intervals are constructed under ``Sets().Constructors()`` and
        refined into this subtree.
        """

        @final
        def provenance(self) -> ConstructorRegistry:
            r"""Return typed provenance records for topological-space constructors."""
            from category_specs.spec_core import constructor_registry_for_category

            return constructor_registry_for_category(
                TopologicalSpaces(),
                owner_category="TopologicalSpaces()",
                id_prefix="topological_spaces",
            )
    @final
    def Constructors(self) -> TopologicalSpaces._Constructors:
        r"""Return the topological-space constructor collector."""
        return self.__class__._Constructors()

    class SubcategoryMethods:
        @final
        def Connected(self) -> Category:
            r"""Return the connected-space subcategory."""
            return cast(Category, with_axiom(self, "Connected"))
        @final
        def Compact(self) -> Category:
            r"""Return the compact-space subcategory."""
            return cast(Category, with_axiom(self, "Compact"))
        @final
        def Metric(self) -> Category:
            r"""Return the metric-space subcategory."""
            return cast(Category, with_axiom(self, "Metric"))

    Subobjects = _Subobjects
    Quotients = _Quotients
    Subquotients = _Subquotients
    ObjectsOver = _ObjectsOver
    ObjectsUnder = _ObjectsUnder
    CartesianProducts = _CartesianProducts


from .subcategories.metric import MetricSpacesCategory  # noqa: E402

MetricSpacesObject = MetricSpacesCategory.ParentMethods
MetricSpacesElement = MetricSpacesCategory.ElementMethods
MetricSpacesMorphism = MetricSpaceHomCategory.ElementMethods
MetricSpacesHomCategory = MetricSpaceHomCategory
MetricSpacesEndCategory = MetricSpaceEndCategory
MetricSpacesAutCategory = MetricSpaceAutCategory
MetricSpacesHom = MetricSpaceHomCategory.ParentMethods
MetricSpacesEnd = MetricSpaceEndCategory.ParentMethods
MetricSpacesAut = MetricSpaceAutCategory.ParentMethods
MetricSpacesEndomorphism = MetricSpaceEndCategory.ElementMethods
MetricSpacesAutomorphism = MetricSpaceAutCategory.ElementMethods


TopologicalSpacesCategory = TopologicalSpaces
type TopologicalSpacesObject = TopologicalSpaces.ParentMethods
TopologicalSpacesElement = TopologicalSpaces.ElementMethods
TopologicalSpacesMorphism = TopologicalSpaceHomCategory.ElementMethods
TopologicalSpacesHomCategory = TopologicalSpaceHomCategory
TopologicalSpacesEndCategory = TopologicalSpaceEndCategory
TopologicalSpacesAutCategory = TopologicalSpaceAutCategory
TopologicalSpacesHom = TopologicalSpaceHomCategory.ParentMethods
TopologicalSpacesEnd = TopologicalSpaceEndCategory.ParentMethods
TopologicalSpacesAut = TopologicalSpaceAutCategory.ParentMethods
TopologicalSpacesEndomorphism = TopologicalSpaceEndCategory.ElementMethods
TopologicalSpacesAutomorphism = TopologicalSpaceAutCategory.ElementMethods
