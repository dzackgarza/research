r"""Parent-backed wrappers for Sage category base constructions.

This module is the local boundary with Sage's category implementation.  The
wrappers extend the Sage category base classes used by this subtree while
making their instances honest parent objects whose category is ``Cat()``.
Sage keeps ownership of category construction; this layer only controls the
minimal integration point where a category object is itself categorized.

The root ``Cat`` category is the one deliberate exception.  ``Cat()`` is the
ambient category of 1-categories in this spec, not an object of itself, so it
inherits directly from Sage's singleton category base in ``cat/__init__.py``.
Every ordinary project category below that root should inherit from the
re-exports in this file instead of raw ``sage.categories.*`` bases.
"""

from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import TYPE_CHECKING, Any, final, overload, override

from sage.categories.algebra_functor import AlgebrasCategory as SageAlgebrasCategory
from sage.categories.cartesian_product import CartesianProductsCategory as SageCartesianProductsCategory
from sage.categories.category import Category as SageCategory
from sage.categories.category import CategoryWithParameters as SageCategoryWithParameters
from sage.categories.category_singleton import Category_singleton as SageCategorySingleton
from sage.categories.category_types import Category_ideal as SageCategoryIdeal
from sage.categories.category_types import Category_module as SageCategoryModule
from sage.categories.category_types import Category_over_base as SageCategoryOverBase
from sage.categories.category_types import Category_over_base_ring as SageCategoryOverBaseRing
from sage.categories.category_with_axiom import CategoryWithAxiom as SageCategoryWithAxiom
from sage.categories.category_with_axiom import (
    CategoryWithAxiom_over_base_ring as SageCategoryWithAxiomOverBaseRing,
)
from sage.categories.category_with_axiom import CategoryWithAxiom_singleton as SageCategoryWithAxiomSingleton
from sage.categories.covariant_functorial_construction import (
    CovariantConstructionCategory as SageCovariantConstructionCategory,
)
from sage.categories.covariant_functorial_construction import (
    FunctorialConstructionCategory as SageFunctorialConstructionCategory,
)
from sage.categories.covariant_functorial_construction import (
    RegressiveCovariantConstructionCategory as SageRegressiveCovariantConstructionCategory,
)
from sage.categories.dual import DualObjectsCategory as SageDualObjectsCategory
from sage.categories.filtered_modules import FilteredModulesCategory as SageFilteredModulesCategory
from sage.categories.graded_modules import GradedModulesCategory as SageGradedModulesCategory
from sage.categories.homsets import Homsets as SageHomsets
from sage.categories.homsets import HomsetsCategory as SageHomsetsCategory
from sage.categories.homsets import HomsetsOf as SageHomsetsOf
from sage.categories.isomorphic_objects import IsomorphicObjectsCategory as SageIsomorphicObjectsCategory
from sage.categories.quotients import QuotientsCategory as SageQuotientsCategory
from sage.categories.realizations import RealizationsCategory as SageRealizationsCategory
from sage.categories.subobjects import SubobjectsCategory as SageSubobjectsCategory
from sage.categories.subquotients import SubquotientsCategory as SageSubquotientsCategory
from sage.categories.super_modules import SuperModulesCategory as SageSuperModulesCategory
from sage.categories.tensor import TensorProductsCategory as SageTensorProductsCategory
from sage.categories.with_realizations import WithRealizationsCategory as SageWithRealizationsCategory
from sage.misc.cachefunc import cached_method
from sage.misc.constant_function import ConstantFunction
from sage.structure.category_object import CategoryObject
from sage.structure.dynamic_class import DynamicMetaclass
from sage.structure.parent import Parent

from .universal_subcategory_methods import UniversalSubcategoryMethods

if TYPE_CHECKING:
    from ..types import Hom

_SageCategory = SageCategory
_SageCategoryWithParameters = SageCategoryWithParameters
_SageCategorySingleton = SageCategorySingleton
_SageCategoryIdeal = SageCategoryIdeal
_SageCategoryModule = SageCategoryModule
_SageCategoryOverBase = SageCategoryOverBase
_SageCategoryOverBaseRing = SageCategoryOverBaseRing
_SageCategoryWithAxiom = SageCategoryWithAxiom
_SageCategoryWithAxiomOverBaseRing = SageCategoryWithAxiomOverBaseRing
_SageCategoryWithAxiomSingleton = SageCategoryWithAxiomSingleton
_SageCovariantConstructionCategory = SageCovariantConstructionCategory
_SageFunctorialConstructionCategory = SageFunctorialConstructionCategory
_SageRegressiveCovariantConstructionCategory = SageRegressiveCovariantConstructionCategory
_SageHomsets = SageHomsets
_SageHomsetsCategory = SageHomsetsCategory
_SageHomsetsOf = SageHomsetsOf

_COMBINED_SUBCATEGORY_METHODS_CACHE: dict[type | None, type] = {}
_CAT_CONSTRUCTOR_METADATA_NAMES = frozenset({"base_ring", "category", "names"})
_CAT_CONSTRUCTOR_CLASS: type | None = None
_CAT_CONSTRUCTOR_OWNERS: dict[str, SageCategory] = {}


def _static_category_class(category: SageCategory) -> type:
    cls = category.__class__
    if isinstance(cls, DynamicMetaclass):
        return cls.__base__
    return cls


def _identifier_fragment(text: str) -> str:
    characters: list[str] = []
    previous_was_underscore = True
    for character in text.lower():
        if character.isalnum():
            characters.append(character)
            previous_was_underscore = False
        elif not previous_was_underscore:
            characters.append("_")
            previous_was_underscore = True
    return "".join(characters).strip("_")


def _camel_case_to_snake(name: str) -> str:
    characters: list[str] = []
    for index, character in enumerate(name):
        if character.isupper() and index and not name[index - 1].isupper():
            characters.append("_")
        characters.append(character.lower())
    return _identifier_fragment("".join(characters))


def _singular_prefix(prefix: str) -> str:
    if prefix.endswith("ies"):
        return f"{prefix[:-3]}y"
    if prefix.endswith("s"):
        return prefix[:-1]
    return prefix


def _explicit_constructors_provider(category: SageCategory) -> type | None:
    category_class = _static_category_class(category)
    for provider_name in ("Constructors", "_Constructors"):
        provider = category_class.__dict__.get(provider_name)
        if isinstance(provider, type):
            return provider
    return None


def _cat_constructor_prefix(category: SageCategory) -> str:
    prefix = _camel_case_to_snake(_static_category_class(category).__name__)
    base_getter = getattr(category, "base_ring", None)
    if callable(base_getter):
        base_ring = base_getter()
        if base_ring is not None:
            return f"{prefix}_{_identifier_fragment(str(base_ring))}"
    return prefix


def _validate_cat_constructor_method_name(prefix: str, constructor_name: str) -> None:
    normalized_name = _camel_case_to_snake(constructor_name)
    forbidden_starts = {f"{prefix}_from_", f"{_singular_prefix(prefix)}_from_"}
    assert not any(normalized_name.startswith(start) for start in forbidden_starts), (
        f"{constructor_name} repeats Cat constructor prefix {prefix}; use from_* locally"
    )


def _cat_constructor_method_names(prefix: str, provider: type) -> tuple[str, ...]:
    names: list[str] = []
    for name, value in provider.__dict__.items():
        if (
            name.startswith("_")
            or name in _CAT_CONSTRUCTOR_METADATA_NAMES
            or not name.isidentifier()
            or not callable(value)
            or getattr(value, "_cat_constructor_generated_forwarder", False)
        ):
            continue
        _validate_cat_constructor_method_name(prefix, name)
        names.append(name)
    return tuple(names)


def _cat_constructor_forwarder(prefix: str, constructor_name: str) -> Callable[..., Any]:
    def forwarded_constructor(self, *args: Any, **kwargs: Any) -> Any:
        constructors = _CAT_CONSTRUCTOR_OWNERS[prefix].Constructors()
        return getattr(constructors, constructor_name)(*args, **kwargs)

    forwarded_constructor.__name__ = f"{prefix}_{constructor_name}"
    forwarded_constructor.__qualname__ = f"Cat.Constructors.{prefix}_{constructor_name}"
    forwarded_constructor.__doc__ = f"Forward to ``{prefix}.Constructors().{constructor_name}``."
    forwarded_constructor._cat_constructor_generated_forwarder = True
    return forwarded_constructor


def _install_cat_constructor_methods() -> None:
    if _CAT_CONSTRUCTOR_CLASS is None:
        return
    for prefix, category in sorted(_CAT_CONSTRUCTOR_OWNERS.items()):
        provider = _explicit_constructors_provider(category)
        if provider is None:
            continue
        for constructor_name in _cat_constructor_method_names(prefix, provider):
            method_name = f"{prefix}_{constructor_name}"
            existing = getattr(_CAT_CONSTRUCTOR_CLASS, method_name, None)
            assert existing is None or getattr(existing, "__name__", None) == method_name, (
                f"duplicate Cat constructor method: {method_name}"
            )
            if existing is None:
                setattr(
                    _CAT_CONSTRUCTOR_CLASS,
                    method_name,
                    _cat_constructor_forwarder(prefix, constructor_name),
                )


def register_cat_constructor_class(
    constructor_class: type,
    root_category: SageCategory | None = None,
) -> None:
    r"""Register ``Cat.Constructors`` as the backend aggregation target."""
    global _CAT_CONSTRUCTOR_CLASS

    assert _CAT_CONSTRUCTOR_CLASS is None or _CAT_CONSTRUCTOR_CLASS is constructor_class, (
        "Cat.Constructors class already registered"
    )
    _CAT_CONSTRUCTOR_CLASS = constructor_class
    if root_category is not None:
        _register_cat_constructor_owner(root_category)
    _install_cat_constructor_methods()


def _register_cat_constructor_owner(category: SageCategory) -> None:
    provider = _explicit_constructors_provider(category)
    if provider is None:
        return
    prefix = _cat_constructor_prefix(category)
    existing = _CAT_CONSTRUCTOR_OWNERS.get(prefix)
    assert existing is None or existing is category, f"duplicate Cat constructor prefix: {prefix}"
    _CAT_CONSTRUCTOR_OWNERS[prefix] = category
    _install_cat_constructor_methods()


def _local_parent_methods(category: SageCategory) -> type | None:
    return getattr(_static_category_class(category), "ParentMethods", None)


def _declared_defining_predicates(category: SageCategory) -> tuple[str, ...]:
    predicates = getattr(_static_category_class(category), "_defining_predicates", None)
    assert predicates is not None, f"{category} must declare _defining_predicates"
    predicates = tuple(predicates)
    assert predicates, f"{category} must declare at least one defining predicate"
    assert all(isinstance(predicate, str) and predicate for predicate in predicates), (
        f"{category} has invalid defining predicates: {predicates}"
    )
    return predicates


def _validate_defining_predicates(category: SageCategory, predicates: tuple[str, ...]) -> None:
    ambient_parent_class = category.base_category().parent_class
    local_parent_methods = _local_parent_methods(category)
    missing_from_ambient = tuple(
        predicate for predicate in predicates if not hasattr(ambient_parent_class, predicate)
    )
    missing_from_subcategory = tuple(
        predicate
        for predicate in predicates
        if local_parent_methods is None or predicate not in local_parent_methods.__dict__
    )
    assert not missing_from_ambient, (
        f"{category} defining predicates are not exposed on ambient category "
        f"{category.base_category()}: {missing_from_ambient}"
    )
    assert not missing_from_subcategory, (
        f"{category} defining predicates are not implemented on its ParentMethods: "
        f"{missing_from_subcategory}"
    )


def _cat_category():
    from . import Cat

    return Cat()


def _copy_method_provider_namespace(provider: type, namespace: dict[str, Any]) -> None:
    for name, value in provider.__dict__.items():
        if name in {"__dict__", "__module__", "__weakref__"}:
            continue
        if name.startswith("__") and name.endswith("__"):
            continue
        namespace[name] = value


def _combined_subcategory_methods(local_provider: type | None) -> type:
    if local_provider is None:
        return UniversalSubcategoryMethods
    cached_provider = _COMBINED_SUBCATEGORY_METHODS_CACHE.get(local_provider)
    if cached_provider is not None:
        return cached_provider

    namespace: dict[str, Any] = {
        "__doc__": getattr(local_provider, "__doc__", None),
        "__module__": local_provider.__module__,
    }
    _copy_method_provider_namespace(UniversalSubcategoryMethods, namespace)
    _copy_method_provider_namespace(local_provider, namespace)
    provider = type(f"{local_provider.__qualname__}WithCatConstructions", (), namespace)
    _COMBINED_SUBCATEGORY_METHODS_CACHE[local_provider] = provider
    return provider


def _make_named_class_with_cat_subcategory_methods(
    category: SageCategory,
    delegate,
    name,
    method_provider,
    cache=False,
    picklable: bool = True,
):
    r"""Delegate Sage named-class construction with Cat's universal methods.

    Sage consumes a single flat method-provider class when building generated
    classes such as ``subcategory_class``.  Provider inheritance is not the
    mechanism Sage uses here: Sage warns about provider superclasses and does
    not install inherited provider methods.  Therefore Cat's universal
    ``SubcategoryMethods`` must be flattened into the local provider before
    Sage constructs the generated class.

    This helper is the single wrapper-layer implementation of that policy.
    Wrapped category bases call it from ``_CatObjectMixin``.  ``Cat`` calls the
    same helper explicitly because it deliberately does not inherit from the
    wrapped bases.
    """
    if name != "subcategory_class" or method_provider != "SubcategoryMethods":
        return delegate(name, method_provider, cache=cache, picklable=picklable)

    local_provider = getattr(category, method_provider, None)
    combined_provider = _combined_subcategory_methods(local_provider)
    temporary_provider = "_cat_combined_subcategory_methods"
    setattr(category, temporary_provider, combined_provider)
    generated_class = delegate(name, temporary_provider, cache=cache, picklable=picklable)
    delattr(category, temporary_provider)
    return generated_class


class _CatObjectMixin:
    r"""Mixin making a Sage category object an object of ``Cat()``.

    The wrapper classes below intentionally use exactly this base order:

    ``_CatObjectMixin, SageCategoryBase, Parent``

    Each position is forced by a different Sage behavior:

    - ``_CatObjectMixin`` must precede the Sage category base because Sage's
      ``Category.category`` returns ``Objects()`` for category objects
      (installed ``sage/categories/category.py``, ``Category.category``).  The
      local semantic change is precisely that project category objects live in
      ``Cat()`` instead.
    - ``SageCategoryBase`` must precede ``Parent`` because category objects
      must keep Sage category behavior.  If ``Parent`` is before the Sage base,
      Python resolves ``__contains__`` and ``__call__`` to parent
      element-construction logic, ``base``/``base_ring`` to
      ``CategoryObject`` storage, and ``element_class`` to ``Parent``.  Those
      are wrong for categories and force ad hoc repair overrides.  With the
      Sage base before ``Parent``, Sage's own category methods win naturally.
    - ``Parent`` must still appear in the MRO so ``isinstance(C, Parent)`` is
      true and category objects are real Sage parents.  Keeping it last gives
      the type relationship without letting generic parent methods shadow
      category semantics.

    This is why the order is not cosmetic.  It is the smallest design found
    that preserves Sage's category framework while making categories themselves
    parent objects in ``Cat()``.
    """

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        initializer = cls.__dict__.get("__init__")
        if initializer is None:
            return
        if getattr(initializer, "_cat_constructor_registration_wrapper", False):
            return

        @wraps(initializer)
        def initialize_and_register(self, *args: Any, **kwargs: Any) -> None:
            initializer(self, *args, **kwargs)
            _register_cat_constructor_owner(self)

        initialize_and_register._cat_constructor_registration_wrapper = True
        cls.__init__ = initialize_and_register

    @final
    def _init_cat_object(self) -> None:
        r"""Initialize the parent shell without recategorizing the class.

        The naive parent integration would be
        ``Parent.__init__(category=Cat())``.  That cannot be used here.
        ``Parent._init_category_`` sets ``_category`` and rewrites
        ``__class__`` to a dynamic class containing the category's
        ``parent_class`` (installed ``sage/structure/parent.pyx``,
        ``Parent._init_category_``).  Sage category objects already have their
        own class rewrite: ``Category.__init__`` creates the single
        ``*_with_category`` dynamic class from ``(self.__class__,
        self.subcategory_class)`` (installed ``sage/categories/category.py``,
        ``Category.__init__``).

        If both rewrites run, a category such as ``Sets()`` becomes
        ``Sets_with_category_with_category``.  Sage axiom descriptors are not
        written for that shape: ``CategoryWithAxiom.__classget__`` strips one
        dynamic layer before verifying that a nested axiom class belongs to the
        base category (installed ``sage/categories/category_with_axiom.py``,
        ``CategoryWithAxiom.__classget__``).  The second dynamic layer makes
        that check see ``Sets_with_category`` instead of ``Sets``, so calls
        such as ``Sets().Countable()`` fail before Sage can return the normal
        ``SubcategoryMethods.Countable`` method.

        Therefore this method separates the two effects that
        ``Parent.__init__(category=Cat())`` would combine.  First,
        ``Parent.__init__(category=None)`` initializes Parent internals without
        invoking ``Parent._init_category_``.  Then
        ``CategoryObject._init_category_`` records ``Cat()`` as the object's
        category; unlike ``Parent._init_category_``, it only stores
        ``_category`` and does not rewrite ``__class__`` (installed
        ``sage/structure/category_object.pyx``,
        ``CategoryObject._init_category_``).  Sage remains the only owner of
        category dynamic-class construction.
        """
        Parent.__init__(self, category=None)
        CategoryObject._init_category_(self, _cat_category())

    @override
    @final
    def category(self):
        r"""Return ``Cat()`` as the category of this category object.

        This is the only direct semantic override in the mixin.  Without it,
        Sage's ``Category.category`` reports ``Objects()`` for category
        objects, so ``Sets().category()`` would not be ``Cat()`` and ordinary
        Sage membership ``Sets() in Cat()`` would not express that categories
        are objects of the category of categories.  The value returned here is
        not recomputed: it is the ``_category`` stored by
        ``CategoryObject._init_category_`` during initialization.
        """
        return CategoryObject.category(self)

    @override
    @final
    def Hom(self, codomain: SageCategory) -> Hom:
        r"""Return ``Hom_{Cat}(self, codomain)``."""
        assert codomain in self.category(), "codomain must be an object of Cat()"
        return Parent.Hom(self, codomain)

    def _make_named_class(self, name, method_provider, cache=False, picklable: bool = True):
        r"""Inject Cat's universal ``SubcategoryMethods`` into wrapped categories.

        The wrapper layer owns this Sage-integration policy; this method only
        supplies the proper superclass delegate for the current wrapped base.
        """
        return _make_named_class_with_cat_subcategory_methods(
            self,
            super()._make_named_class,
            name,
            method_provider,
            cache=cache,
            picklable=picklable,
        )


class _SingletonClasscallMixin:
    r"""Closed singleton classcall bridge for Cat-backed singleton categories.

    This is not a generic singleton framework.  It exists because Sage's
    ``Category_singleton.__classcall__`` is intentionally restrictive: it
    asserts that ``cls.__mro__[1]`` is exactly Sage's ``Category_singleton`` or
    ``CategoryWithAxiom_singleton`` (installed
    ``sage/categories/category_singleton.pyx``,
    ``Category_singleton.__classcall__``).  That rejects both natural local
    designs:

    - putting ``_CatObjectMixin`` before the Sage singleton base, which we must
      do so ``category()`` reports ``Cat()`` instead of Sage's ``Objects()``;
    - defining one local singleton wrapper and inheriting later singletons such
      as ``Homsets`` from it, because Sage also rejects singleton subclasses of
      singleton subclasses.

    The mixin therefore isolates the one compatibility exception.  It preserves
    Sage's singleton caching behavior by installing the same ``ConstantFunction``
    classcall on both the concrete class and Sage's dynamic ``*_with_category``
    class.  It bypasses only Sage's direct-subclass assertion, which conflicts
    with the required Cat-backed MRO.
    """

    @staticmethod
    @final
    def __classcall__(cls):
        if isinstance(cls, DynamicMetaclass):
            cls = cls.__base__
        obj = super(SageCategorySingleton, cls).__classcall__(cls)
        cls._set_classcall(ConstantFunction(obj))
        obj.__class__._set_classcall(ConstantFunction(obj))
        return obj


class _SingletonAxiomClasscallMixin:
    r"""Closed singleton classcall bridge for Cat-backed axiom categories.

    Sage uses exactly two construction paths for singleton axiom categories in
    this subtree.  A public call such as ``TopologicalSpaces()`` has no
    explicit base category and must go through Sage's
    ``CategoryWithAxiom.__classcall__`` redirection to the declared base
    category and axiom.  A reconstruction call such as
    ``Sets().Finite().__class__(Sets())`` provides the base category directly
    and must construct/cache that singleton axiom instance.

    The optional ``base_category`` argument is therefore a closed two-case
    dispatch, not a variadic catch-all.  This mixin exists for the same reason
    as ``_SingletonClasscallMixin``: Sage's direct-subclass singleton assertion
    conflicts with the required local MRO.
    """

    @staticmethod
    @final
    def __classcall__(cls, base_category: SageCategory | None = None):
        if isinstance(cls, DynamicMetaclass):
            cls = cls.__base__
        if base_category is None:
            return SageCategoryWithAxiom.__classcall__(cls)
        obj = super(SageCategorySingleton, cls).__classcall__(cls, base_category)
        cls._set_classcall(ConstantFunction(obj))
        obj.__class__._set_classcall(ConstantFunction(obj))
        return obj


# Wrapper bases intentionally use ``_CatObjectMixin, SageCategoryBase, Parent``.
# The order is what lets Sage keep ownership of category semantics while the
# object is still a ``Parent`` whose category is ``Cat()``.
class Category(_CatObjectMixin, SageCategory, Parent):
    r"""Parent-backed re-export of Sage's ``Category`` base class."""

    def __init__(self) -> None:
        self._init_cat_object()
        SageCategory.__init__(self)


class CategoryWithParameters(_CatObjectMixin, SageCategoryWithParameters, Parent):
    r"""Parent-backed re-export of Sage's parameterized category base."""

    def __init__(self) -> None:
        self._init_cat_object()
        SageCategoryWithParameters.__init__(self)


class Category_singleton(_SingletonClasscallMixin, _CatObjectMixin, SageCategorySingleton, Parent):
    r"""Parent-backed re-export of Sage's singleton category base."""

    def __init__(self) -> None:
        self._init_cat_object()
        SageCategorySingleton.__init__(self)


class CategoryWithAxiom(_CatObjectMixin, SageCategoryWithAxiom, Parent):
    r"""Parent-backed re-export of Sage's category-with-axiom base."""

    def __init__(self, base_category: SageCategory) -> None:
        self._init_cat_object()
        SageCategoryWithAxiom.__init__(self, base_category)

    @override
    @final
    def ambient_category(self) -> SageCategory:
        r"""Return the base category of this axiom category."""
        return self.base_category()

    @override
    @final
    def defining_predicates(self) -> tuple[str, ...]:
        r"""Return the predicate names defining this axiom category."""
        predicates = _declared_defining_predicates(self)
        _validate_defining_predicates(self, predicates)
        return predicates

    @override
    @final
    def defining_predicate(self, candidate: CategoryObject) -> bool:
        r"""Return whether ``candidate`` satisfies every defining predicate."""
        return all(getattr(candidate, predicate)() for predicate in self.defining_predicates())


class CategoryWithAxiom_singleton(
    _SingletonAxiomClasscallMixin,
    _CatObjectMixin,
    SageCategoryWithAxiomSingleton,
    Parent,
):
    r"""Parent-backed re-export of Sage's singleton axiom category base."""

    def __init__(self, base_category: SageCategory) -> None:
        self._init_cat_object()
        SageCategoryWithAxiomSingleton.__init__(self, base_category)

    @override
    @final
    def ambient_category(self) -> SageCategory:
        r"""Return the base category of this singleton axiom category."""
        return self.base_category()

    @override
    @final
    def defining_predicates(self) -> tuple[str, ...]:
        r"""Return the predicate names defining this singleton axiom category."""
        predicates = _declared_defining_predicates(self)
        _validate_defining_predicates(self, predicates)
        return predicates

    @override
    @final
    def defining_predicate(self, candidate: CategoryObject) -> bool:
        r"""Return whether ``candidate`` satisfies every defining predicate."""
        return all(getattr(candidate, predicate)() for predicate in self.defining_predicates())


class CategoryWithAxiom_over_base_ring(_CatObjectMixin, SageCategoryWithAxiomOverBaseRing, Parent):
    r"""Parent-backed re-export of Sage's base-ring axiom category base."""

    def __init__(self, base_category: SageCategory) -> None:
        self._init_cat_object()
        SageCategoryWithAxiomOverBaseRing.__init__(self, base_category)

    @override
    @final
    def ambient_category(self) -> SageCategory:
        r"""Return the base category of this base-ring axiom category."""
        return self.base_category()

    @override
    @final
    def defining_predicates(self) -> tuple[str, ...]:
        r"""Return the predicate names defining this base-ring axiom category."""
        predicates = _declared_defining_predicates(self)
        _validate_defining_predicates(self, predicates)
        return predicates

    @override
    @final
    def defining_predicate(self, candidate: CategoryObject) -> bool:
        r"""Return whether ``candidate`` satisfies every defining predicate."""
        return all(getattr(candidate, predicate)() for predicate in self.defining_predicates())


class Category_over_base(_CatObjectMixin, SageCategoryOverBase, Parent):
    r"""Parent-backed re-export of Sage's category-over-base base."""

    def __init__(self, base: CategoryObject, name: str | None = None) -> None:
        self._init_cat_object()
        SageCategoryOverBase.__init__(self, base, name)


class Category_over_base_ring(_CatObjectMixin, SageCategoryOverBaseRing, Parent):
    r"""Parent-backed re-export of Sage's category-over-base-ring base."""

    def __init__(self, base: CategoryObject, name: str | None = None) -> None:
        self._init_cat_object()
        SageCategoryOverBaseRing.__init__(self, base, name)


class Category_module(_CatObjectMixin, SageCategoryModule, Parent):
    r"""Parent-backed re-export of Sage's module category base."""

    def __init__(self, base: CategoryObject, name: str | None = None) -> None:
        self._init_cat_object()
        SageCategoryModule.__init__(self, base, name)


class Category_ideal(_CatObjectMixin, SageCategoryIdeal, Parent):
    r"""Parent-backed re-export of Sage's ideal category base."""

    def __init__(self, ambient: CategoryObject, name: str | None = None) -> None:
        self._init_cat_object()
        SageCategoryIdeal.__init__(self, ambient, name)


class HomsetsCategory(_CatObjectMixin, SageHomsetsCategory, Parent):
    r"""Parent-backed re-export of Sage's homsets construction category."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageHomsetsCategory.__init__(self, category)


class HomsetsOf(_CatObjectMixin, SageHomsetsOf, Parent):
    r"""Parent-backed re-export of Sage's category-specific homsets base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageHomsetsOf.__init__(self, category)


class Homsets(_SingletonClasscallMixin, _CatObjectMixin, SageHomsets, Parent):
    r"""Parent-backed re-export of Sage's singleton homsets category."""

    def __init__(self) -> None:
        self._init_cat_object()
        SageHomsets.__init__(self)

    @cached_method
    @final
    def Endset(self):
        r"""Return Sage's existing root category of endomorphism sets.

        This override is forced by Sage's singleton-axiom descriptor, not by
        project semantics.  Sage's ``Homsets.Endset`` nested class records the
        raw Sage ``Homsets`` class as its base category class.  If the wrapped
        ``Homsets`` inherits that descriptor directly, Sage sees the wrapped
        base class and raises the assertion in
        ``sage/categories/category_with_axiom.py``,
        ``CategoryWithAxiom.__classget__``.

        A project subclass may declare its own ``Endset`` axiom class.  In that
        case the subclass is the mathematical owner of the axiom and this
        interop bridge constructs it with the current homset category as base.
        Otherwise the raw Sage root remains the canonical upstream category.
        """
        axiom_category = getattr(type(self), "Endset", None)
        if isinstance(axiom_category, type) and issubclass(axiom_category, SageCategoryWithAxiom):
            return axiom_category(self)
        return SageHomsets().Endset()


class FunctorialConstructionCategory(_CatObjectMixin, SageFunctorialConstructionCategory, Parent):
    r"""Parent-backed base for Sage functorial construction categories.

    This class is the missing part of the wrapping boundary.  Sage
    construction methods such as ``C.Subobjects()``, ``C.Quotients()``, and
    ``C.CartesianProducts()`` do not construct ordinary axiom categories; they
    construct ``FunctorialConstructionCategory`` descendants.  If local
    construction classes inherit those raw Sage bases, the result keeps Sage's
    default ``category() == Objects()`` behavior and escapes ``Cat()`` even
    when the base category ``C`` is correctly wrapped.

    The fix belongs here rather than in each construction method: every
    functorial construction category is itself a category object, so it must
    use the same ``_CatObjectMixin, SageCategoryBase, Parent`` MRO as the other
    category bases.  The concrete construction modules then import these
    re-exports and continue to rely on Sage's own
    ``FunctorialConstructionCategory.category_of`` and
    ``default_super_categories`` logic.
    """

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageFunctorialConstructionCategory.__init__(self, category)


class CovariantConstructionCategory(_CatObjectMixin, SageCovariantConstructionCategory, Parent):
    r"""Parent-backed re-export of Sage's covariant construction base."""

    @overload
    def __init__(self, category: SageCategory) -> None: ...

    @overload
    def __init__(self, category: SageCategory, structure_object: CategoryObject) -> None: ...

    def __init__(self, category: SageCategory, structure_object: CategoryObject | None = None) -> None:
        self._init_cat_object()
        if structure_object is None:
            SageCovariantConstructionCategory.__init__(self, category)
            return
        SageCovariantConstructionCategory.__init__(self, category, structure_object)


class RegressiveCovariantConstructionCategory(
    _CatObjectMixin,
    SageRegressiveCovariantConstructionCategory,
    Parent,
):
    r"""Parent-backed re-export of Sage's regressive construction base."""

    @overload
    def __init__(self, category: SageCategory) -> None: ...

    @overload
    def __init__(self, category: SageCategory, structure_object: CategoryObject) -> None: ...

    def __init__(self, category: SageCategory, structure_object: CategoryObject | None = None) -> None:
        self._init_cat_object()
        if structure_object is None:
            SageRegressiveCovariantConstructionCategory.__init__(self, category)
            return
        SageRegressiveCovariantConstructionCategory.__init__(self, category, structure_object)


class SubobjectsCategory(_CatObjectMixin, SageSubobjectsCategory, Parent):
    r"""Parent-backed re-export of Sage's subobject construction base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageSubobjectsCategory.__init__(self, category)


class QuotientsCategory(_CatObjectMixin, SageQuotientsCategory, Parent):
    r"""Parent-backed re-export of Sage's quotient construction base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageQuotientsCategory.__init__(self, category)


class SubquotientsCategory(_CatObjectMixin, SageSubquotientsCategory, Parent):
    r"""Parent-backed re-export of Sage's subquotient construction base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageSubquotientsCategory.__init__(self, category)


class CartesianProductsCategory(_CatObjectMixin, SageCartesianProductsCategory, Parent):
    r"""Parent-backed re-export of Sage's Cartesian-product construction base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageCartesianProductsCategory.__init__(self, category)


class IsomorphicObjectsCategory(_CatObjectMixin, SageIsomorphicObjectsCategory, Parent):
    r"""Parent-backed re-export of Sage's isomorphic-object construction base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageIsomorphicObjectsCategory.__init__(self, category)


class RealizationsCategory(_CatObjectMixin, SageRealizationsCategory, Parent):
    r"""Parent-backed re-export of Sage's realization construction base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageRealizationsCategory.__init__(self, category)


class WithRealizationsCategory(_CatObjectMixin, SageWithRealizationsCategory, Parent):
    r"""Parent-backed re-export of Sage's with-realizations construction base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageWithRealizationsCategory.__init__(self, category)


class DualObjectsCategory(_CatObjectMixin, SageDualObjectsCategory, Parent):
    r"""Parent-backed re-export of Sage's dual-object construction base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageDualObjectsCategory.__init__(self, category)


class TensorProductsCategory(_CatObjectMixin, SageTensorProductsCategory, Parent):
    r"""Parent-backed re-export of Sage's tensor-product construction base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageTensorProductsCategory.__init__(self, category)


class AlgebrasCategory(_CatObjectMixin, SageAlgebrasCategory, Parent):
    r"""Parent-backed re-export of Sage's algebra functor construction base."""

    def __init__(self, category: SageCategory, base_ring: CategoryObject) -> None:
        self._init_cat_object()
        SageAlgebrasCategory.__init__(self, category, base_ring)


class FilteredModulesCategory(_CatObjectMixin, SageFilteredModulesCategory, Parent):
    r"""Parent-backed re-export of Sage's filtered-module construction base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageFilteredModulesCategory.__init__(self, category)


class GradedModulesCategory(_CatObjectMixin, SageGradedModulesCategory, Parent):
    r"""Parent-backed re-export of Sage's graded-module construction base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageGradedModulesCategory.__init__(self, category)


class SuperModulesCategory(_CatObjectMixin, SageSuperModulesCategory, Parent):
    r"""Parent-backed re-export of Sage's super-module construction base."""

    def __init__(self, category: SageCategory) -> None:
        self._init_cat_object()
        SageSuperModulesCategory.__init__(self, category)
