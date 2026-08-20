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

This file is also the only category-spec Python file allowed to perform
attribute rebinding.  The rebinding here is not a mathematical surface: it is
the source-grounded bridge to Sage's generated ``parent_class`` /
``subcategory_class`` machinery and to the aggregate ``Cat().Constructors()``
view.  Spec categories, constructor collectors, category-obligation examples,
and mapping code must not copy this pattern.
"""

from __future__ import annotations

import copyreg
import inspect
from abc import ABCMeta, abstractmethod
from collections.abc import Callable
from functools import wraps
from typing import TYPE_CHECKING, Any, cast, final, overload, override

from sage.categories.algebra_functor import AlgebrasCategory as SageAlgebrasCategory
from sage.categories.cartesian_product import (
    CartesianProductsCategory as SageCartesianProductsCategory,
)
from sage.categories.category import Category as SageCategory
from sage.categories.category import (
    CategoryWithParameters as SageCategoryWithParameters,
)
from sage.categories.category import JoinCategory as SageJoinCategory
from sage.categories.category_singleton import (
    Category_singleton as SageCategorySingleton,
)
from sage.categories.category_types import Category_ideal as SageCategoryIdeal
from sage.categories.category_types import Category_module as SageCategoryModule
from sage.categories.category_types import Category_over_base as SageCategoryOverBase
from sage.categories.category_types import (
    Category_over_base_ring as SageCategoryOverBaseRing,
)
from sage.categories.category_with_axiom import (
    CategoryWithAxiom as SageCategoryWithAxiom,
)
from sage.categories.category_with_axiom import (
    CategoryWithAxiom_over_base_ring as SageCategoryWithAxiomOverBaseRing,
)
from sage.categories.category_with_axiom import (
    CategoryWithAxiom_singleton as SageCategoryWithAxiomSingleton,
)
from sage.categories.covariant_functorial_construction import (
    CovariantConstructionCategory as SageCovariantConstructionCategory,
)
from sage.categories.covariant_functorial_construction import (
    FunctorialConstructionCategory as SageFunctorialConstructionCategory,
)
from sage.categories.covariant_functorial_construction import (
    RegressiveCovariantConstructionCategory as SageRegressiveCovariantConstructionCategory,  # noqa: E501
)
from sage.categories.dual import DualObjectsCategory as SageDualObjectsCategory
from sage.categories.filtered_modules import (
    FilteredModulesCategory as SageFilteredModulesCategory,
)
from sage.categories.graded_modules import (
    GradedModulesCategory as SageGradedModulesCategory,
)
from sage.categories.homsets import Homsets as SageHomsets
from sage.categories.homsets import HomsetsCategory as SageHomsetsCategory
from sage.categories.homsets import HomsetsOf as SageHomsetsOf
from sage.categories.isomorphic_objects import (
    IsomorphicObjectsCategory as SageIsomorphicObjectsCategory,
)
from sage.categories.quotients import QuotientsCategory as SageQuotientsCategory
from sage.categories.realizations import (
    RealizationsCategory as SageRealizationsCategory,
)
from sage.categories.subobjects import SubobjectsCategory as SageSubobjectsCategory
from sage.categories.subquotients import (
    SubquotientsCategory as SageSubquotientsCategory,
)
from sage.categories.super_modules import (
    SuperModulesCategory as SageSuperModulesCategory,
)
from sage.categories.tensor import TensorProductsCategory as SageTensorProductsCategory
from sage.categories.with_realizations import (
    WithRealizationsCategory as SageWithRealizationsCategory,
)
from sage.cpython.type import can_assign_class
from sage.misc.classcall_metaclass import ClasscallMetaclass
from sage.misc.constant_function import ConstantFunction
from sage.misc.inherit_comparison import (
    InheritComparisonMetaclass,
)
from sage.structure.category_object import CategoryObject
from sage.structure.dynamic_class import (
    DynamicClasscallMetaclass,
    DynamicInheritComparisonClasscallMetaclass,
    DynamicInheritComparisonMetaclass,
    DynamicMetaclass,
)
from sage.structure.dynamic_class import (
    dynamic_class as sage_dynamic_class,
)
from sage.structure.parent import Parent

from .universal_subcategory_methods import UniversalSubcategoryMethods

if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.categories.homset import Homset as Hom
    from sage.structure.element import Element as CategoryElement

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
_ABC_METHOD_PROVIDER_CACHE: dict[type, type] = {}
_CONCRETE_METHOD_PROVIDER_CACHE: dict[type, type | None] = {}
_CAT_CONSTRUCTOR_METADATA_NAMES = frozenset({"base_ring", "category", "names", "provenance"})
_CAT_CONSTRUCTOR_CLASS: type | None = None
_CAT_CONSTRUCTOR_OWNERS: dict[str, SageCategory] = {}


class _DynamicABCMetaclass(DynamicMetaclass, ABCMeta):
    pass


class _DynamicABCClasscallMetaclass(DynamicClasscallMetaclass, _DynamicABCMetaclass):
    pass


class _DynamicABCInheritComparisonMetaclass(DynamicInheritComparisonMetaclass, _DynamicABCMetaclass):
    pass


class _DynamicABCInheritComparisonClasscallMetaclass(
    DynamicInheritComparisonClasscallMetaclass,
    _DynamicABCClasscallMetaclass,
    _DynamicABCInheritComparisonMetaclass,
):
    pass


for _abc_dynamic_metaclass in (
    _DynamicABCMetaclass,
    _DynamicABCClasscallMetaclass,
    _DynamicABCInheritComparisonMetaclass,
    _DynamicABCInheritComparisonClasscallMetaclass,
):
    copyreg.pickle(_abc_dynamic_metaclass, _abc_dynamic_metaclass.__reduce__)


def _abc_dynamic_metaclass_for(bases: tuple[type, ...]) -> type:
    metaclass: type = _DynamicABCMetaclass
    for base in bases:
        if isinstance(base, ClasscallMetaclass):
            if not issubclass(metaclass, ClasscallMetaclass):
                if metaclass is _DynamicABCMetaclass:
                    metaclass = _DynamicABCClasscallMetaclass
                elif metaclass is _DynamicABCInheritComparisonMetaclass:
                    metaclass = _DynamicABCInheritComparisonClasscallMetaclass
                else:
                    raise TypeError(f"no ABC dynamic metaclass composes with ClasscallMetaclass for {metaclass!r}")
        if isinstance(base, InheritComparisonMetaclass):
            if not issubclass(metaclass, InheritComparisonMetaclass):
                if metaclass is _DynamicABCMetaclass:
                    metaclass = _DynamicABCInheritComparisonMetaclass
                elif metaclass is _DynamicABCClasscallMetaclass:
                    metaclass = _DynamicABCInheritComparisonClasscallMetaclass
                else:
                    raise TypeError(f"no ABC dynamic metaclass composes with InheritComparisonMetaclass for {metaclass!r}")
    return metaclass


def _requires_abc_dynamic_class(bases: tuple[type, ...], cls: type | None) -> bool:
    if any(isinstance(base, ABCMeta) for base in bases):
        return True
    if cls is None:
        return False
    return any(bool(value.__isabstractmethod__) for value in cls.__dict__.values())


def _dynamic_abc_class(
    name: str,
    bases: tuple[type, ...],
    cls: type | None = None,
    reduction: object = None,
    doccls: type | None = None,
    prepend_cls_bases: bool = True,
) -> type:
    if len(bases) > 1 and object in bases:
        bases = tuple(base for base in bases if base is not object)

    if not _requires_abc_dynamic_class(bases, cls):
        return cast(
            type,
            sage_dynamic_class(
                name,
                bases,
                cls,
                reduction=reduction,
                doccls=doccls,
                prepend_cls_bases=prepend_cls_bases,
            ),
        )

    if reduction is None:
        reduction = (
            _dynamic_abc_class,
            (name, bases, cls, reduction, doccls, prepend_cls_bases),
        )
    if cls is None:
        methods: dict[str, Any] = {}
    else:
        methods = dict(cls.__dict__)
        for key in ("__dict__", "__weakref__"):
            if key in methods:
                del methods[key]
        if prepend_cls_bases:
            all_bases: set[type] = set()
            for base in bases:
                all_bases.update(base.mro())
            cls_bases = tuple(base for base in cls.__bases__ if base not in all_bases)
            bases = cls_bases + bases

    if doccls is None:
        if cls is not None:
            doccls = cls
        else:
            assert bases, "dynamic ABC class construction requires a doc source"
            doccls = bases[0]

    methods["_reduction"] = reduction
    methods["_doccls"] = (doccls,)
    methods["__doc__"] = doccls.__doc__
    methods["__module__"] = doccls.__module__

    if all(not base.__dictoffset__ for base in bases):
        methods["__slots__"] = ()

    return cast(type, _abc_dynamic_metaclass_for(bases)(name, bases, methods))


def _append_unique_class(classes: list[type], cls: type) -> None:
    if cls not in classes:
        classes.append(cls)


def _method_provider_namespace(
    provider: type,
    *,
    abstract: bool | None = None,
) -> dict[str, Any]:
    namespace: dict[str, Any] = {
        "__doc__": provider.__doc__,
        "__module__": provider.__module__,
    }
    for name, value in provider.__dict__.items():
        if name in {"__dict__", "__module__", "__weakref__"}:
            continue
        if name.startswith("__") and name.endswith("__"):
            continue
        is_abstract = bool(value.__isabstractmethod__)
        if abstract is not None and is_abstract is not abstract:
            continue
        namespace[name] = value
    return namespace


def _abc_method_provider(provider: type) -> type:
    cached_provider = _ABC_METHOD_PROVIDER_CACHE.get(provider)
    if cached_provider is not None:
        return cached_provider
    provider_bases = tuple(_abc_method_provider(base) for base in provider.__bases__ if base is not object)
    provider_class = ABCMeta(
        f"{provider.__qualname__}ABC",
        provider_bases,
        _method_provider_namespace(provider),
    )
    _ABC_METHOD_PROVIDER_CACHE[provider] = provider_class
    return provider_class


def _concrete_method_provider(provider: type) -> type | None:
    cached_provider = _CONCRETE_METHOD_PROVIDER_CACHE.get(provider)
    if provider in _CONCRETE_METHOD_PROVIDER_CACHE:
        return cached_provider
    namespace = _method_provider_namespace(provider, abstract=False)
    if len(namespace) == 2:
        _CONCRETE_METHOD_PROVIDER_CACHE[provider] = None
        return None
    provider_class = type(f"{provider.__qualname__}ConcreteMethods", (), namespace)
    _CONCRETE_METHOD_PROVIDER_CACHE[provider] = provider_class
    return provider_class


def _abc_parent_class_bases(category: SageCategory) -> tuple[type, ...]:
    bases: list[type] = []
    for source_category in category._super_categories_for_classes:
        _append_unique_class(bases, source_category.parent_class)
    return tuple(bases)


def _static_category_class(category: SageCategory) -> type:
    cls = cast(type, category.__class__)
    if isinstance(cls, DynamicMetaclass):
        base = cls.__base__
        if base is None:
            raise TypeError("dynamic Sage category class must have a base class")
        return cast(type, base)
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
    match hasattr(category, "base_ring"):
        case True:
            base_ring = category.base_ring()
            match base_ring:
                case None:
                    return prefix
                case _:
                    return f"{prefix}_{_identifier_fragment(str(base_ring))}"
        case False:
            return prefix


def _validate_cat_constructor_method_name(prefix: str, constructor_name: str) -> None:
    normalized_name = _camel_case_to_snake(constructor_name)
    forbidden_starts = {f"{prefix}_from_", f"{_singular_prefix(prefix)}_from_"}
    assert not any(normalized_name.startswith(start) for start in forbidden_starts), f"{constructor_name} repeats Cat constructor prefix {prefix}; use from_* locally"


def _cat_constructor_method_names(prefix: str, provider: type) -> tuple[str, ...]:
    candidates = [
        name
        for name, value in provider.__dict__.items()
        if not name.startswith("_")
        and name not in _CAT_CONSTRUCTOR_METADATA_NAMES
        and name.isidentifier()
        and callable(value)
        and not hasattr(value, "_cat_constructor_generated_forwarder")
    ]
    for name in candidates:
        _validate_cat_constructor_method_name(prefix, name)
    return tuple(candidates)


def _cat_constructor_forwarder(prefix: str, constructor_name: str) -> Callable[..., Any]:
    def forwarded_constructor(self: SageCategory, *args: Any, **kwargs: Any) -> Any:
        constructors = _CAT_CONSTRUCTOR_OWNERS[prefix].Constructors()
        return getattr(constructors, constructor_name)(*args, **kwargs)

    forwarded_constructor.__name__ = f"{prefix}_{constructor_name}"
    forwarded_constructor.__qualname__ = f"Cat.Constructors.{prefix}_{constructor_name}"
    forwarded_constructor.__doc__ = f"Forward to ``{prefix}.Constructors().{constructor_name}``."
    setattr(forwarded_constructor, "_cat_constructor_generated_forwarder", True)
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
            match hasattr(_CAT_CONSTRUCTOR_CLASS, method_name):
                case True:
                    existing = getattr(_CAT_CONSTRUCTOR_CLASS, method_name)
                    assert existing.__name__ == method_name, f"duplicate Cat constructor method: {method_name}"
                case False:
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

    assert _CAT_CONSTRUCTOR_CLASS is None or _CAT_CONSTRUCTOR_CLASS is constructor_class, "Cat.Constructors class already registered"
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
    static_cls = _static_category_class(category)
    match hasattr(static_cls, "ParentMethods"):
        case True:
            return cast(type | None, getattr(static_cls, "ParentMethods"))
        case False:
            return None


def _declared_defining_predicates(category: SageCategory) -> tuple[str, ...]:
    static_cls = _static_category_class(category)
    match hasattr(static_cls, "_defining_predicates"):
        case True:
            predicates = tuple(getattr(static_cls, "_defining_predicates"))
        case False:
            assert False, f"{category} must declare _defining_predicates"
    assert predicates, f"{category} must declare at least one defining predicate"
    assert all(isinstance(predicate, str) and predicate for predicate in predicates), f"{category} has invalid defining predicates: {predicates}"
    return predicates


def _validate_defining_predicates(category: SageCategory, predicates: tuple[str, ...]) -> None:
    ambient_parent_class = category.base_category().parent_class
    local_parent_methods = _local_parent_methods(category)
    missing_from_ambient = tuple(predicate for predicate in predicates if not hasattr(ambient_parent_class, predicate))
    missing_from_subcategory = tuple(predicate for predicate in predicates if local_parent_methods is None or predicate not in local_parent_methods.__dict__)
    assert not missing_from_ambient, f"{category} defining predicates are not exposed on ambient category {category.base_category()}: {missing_from_ambient}"
    assert not missing_from_subcategory, f"{category} defining predicates are not implemented on its ParentMethods: {missing_from_subcategory}"


def _cat_category() -> SageCategory:
    from dzack_research.preamble.categories.abstract_categories.cat import Cat

    category = Cat()
    if not isinstance(category, SageCategory):
        raise TypeError("Cat() must construct a Sage category")
    return category


def _copy_method_provider_namespace(provider: type, namespace: dict[str, Any]) -> None:
    namespace.update(_method_provider_namespace(provider))


def _combined_subcategory_methods(local_provider: type | None) -> type:
    if local_provider is None:
        return UniversalSubcategoryMethods
    cached_provider = _COMBINED_SUBCATEGORY_METHODS_CACHE.get(local_provider)
    if cached_provider is not None:
        return cached_provider

    namespace: dict[str, Any] = {
        "__doc__": local_provider.__doc__,
        "__module__": local_provider.__module__,
    }
    _copy_method_provider_namespace(UniversalSubcategoryMethods, namespace)
    _copy_method_provider_namespace(local_provider, namespace)
    provider = type(f"{local_provider.__qualname__}WithCatConstructions", (), namespace)
    _COMBINED_SUBCATEGORY_METHODS_CACHE[local_provider] = provider
    return provider


def _make_named_parent_class_with_abc(
    category: SageCategory,
    name: str,
    method_provider: str,
    cache: bool = False,
    picklable: bool = True,
    bases: tuple[type, ...] | None = None,
) -> type:
    assert name == "parent_class", "ABC bridge only owns parent_class construction"
    assert method_provider == "ParentMethods", "ABC bridge only owns ParentMethods construction"
    assert cache is False, "category lazy attributes own parent_class caching"

    cls = _static_category_class(category)
    class_name = f"{cls.__name__}.{name}"
    if bases is None:
        bases = _abc_parent_class_bases(category)

    match hasattr(category, method_provider):
        case True:
            method_provider_cls = getattr(category, method_provider)
            assert inspect.isclass(method_provider_cls), f"{cls.__name__}.{method_provider} should be a class"
            doccls = method_provider_cls
        case False:
            method_provider_cls = None
            doccls = cls

    reduction = (getattr, (category, name)) if picklable else None
    # The flip. This tree passed ``prepend_cls_bases=False``, which is Sage's
    # own choice and discards the provider's bases -- so a ``ParentMethods``
    # could not carry ``Parent``, could not hold fields, and could not have a
    # constructor, which is the whole reason a concrete class had to sit beside
    # every category. The provider goes into the BASES instead, with no copied
    # dict: ``prepend_cls_bases=True`` is not the working shape, because it
    # splices the bases while still copying the dict, leaving each method's
    # ``__class__`` cell pointing at a provider outside the MRO so
    # zero-argument ``super()`` raises. Cooperative ``super()`` is the
    # mechanism, so the provider must genuinely be a base.
    if method_provider_cls is not None:
        bases = (method_provider_cls,) + tuple(bases)
    return _dynamic_abc_class(
        class_name,
        bases,
        None,
        prepend_cls_bases=False,
        doccls=doccls,
        reduction=reduction,
    )


def _make_named_element_class_without_abstract_methods(
    category: SageCategory,
    delegate: Callable[..., type],
    name: str,
    method_provider: str,
    cache: bool = False,
    picklable: bool = True,
) -> type:
    assert name == "element_class", "element bridge only owns element_class construction"
    assert method_provider == "ElementMethods", "element bridge only owns ElementMethods construction"

    match hasattr(category, method_provider):
        case False:
            return delegate(name, method_provider, cache=cache, picklable=picklable)
        case True:
            local_provider = getattr(category, method_provider)
            concrete_provider = _concrete_method_provider(local_provider)
            if concrete_provider is None:
                concrete_provider = type(
                    f"{local_provider.__qualname__}ConcreteMethods",
                    (),
                    _method_provider_namespace(local_provider, abstract=False),
                )
            temporary_provider = "_cat_concrete_element_methods"
            setattr(category, temporary_provider, concrete_provider)
            generated_class = delegate(name, temporary_provider, cache=cache, picklable=picklable)
            delattr(category, temporary_provider)
            return generated_class


def _project_join_category(categories: tuple[SageCategory, ...]) -> SageCategory:
    joined_categories = tuple(SageCategory.join(categories, as_list=True))
    assert joined_categories, "category refinement requires at least one category"
    if len(joined_categories) == 1:
        return joined_categories[0]
    joined_category = SageJoinCategory(joined_categories)
    joined_category.parent_class = _make_named_parent_class_with_abc(
        joined_category,
        "parent_class",
        "ParentMethods",
        bases=_abc_parent_class_bases(joined_category),
    )
    return joined_category


def refine_parent_category(parent: Parent, categories: tuple[SageCategory, ...]) -> Parent:
    current_category = parent.category()
    category = _project_join_category((current_category, *categories))
    if category is current_category:
        return parent

    CategoryObject._init_category_(parent, category)
    if can_assign_class(parent):
        base = parent.__class__.__base__
        assert base is not None, "refined Sage parent class must have a base class"
        parent.__class__ = _dynamic_abc_class(
            f"{base.__name__}_with_category",
            (base, category.parent_class),
            doccls=base,
        )
    parent.__dict__.pop("element_class", None)
    parent.__dict__.pop("_abstract_element_class", None)
    return parent


def refine_parent_class(parent_class: type[Parent], categories: tuple[SageCategory, ...]) -> type[Parent]:
    r"""Return ``parent_class`` refined by project category parent methods."""
    assert issubclass(parent_class, Parent), "project class refinement requires a Sage Parent subclass"
    category = _project_join_category(categories)
    return _dynamic_abc_class(
        f"{parent_class.__name__}_with_category",
        (parent_class, category.parent_class),
        doccls=parent_class,
    )


def _make_named_class_with_cat_subcategory_methods(
    category: SageCategory,
    delegate: Callable[..., type],
    name: str,
    method_provider: str,
    cache: bool = False,
    picklable: bool = True,
) -> type:
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
    if name == "parent_class" and method_provider == "ParentMethods":
        return _make_named_parent_class_with_abc(
            category,
            name,
            method_provider,
            cache=cache,
            picklable=picklable,
        )

    if name == "element_class" and method_provider == "ElementMethods":
        return _make_named_element_class_without_abstract_methods(
            category,
            delegate,
            name,
            method_provider,
            cache=cache,
            picklable=picklable,
        )

    if name != "subcategory_class" or method_provider != "SubcategoryMethods":
        return delegate(name, method_provider, cache=cache, picklable=picklable)

    match hasattr(category, method_provider):
        case True:
            local_provider = getattr(category, method_provider)
        case False:
            local_provider = None
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
        match hasattr(initializer, "_cat_constructor_registration_wrapper"):
            case True:
                return
            case False:
                pass

        @wraps(initializer)
        def initialize_and_register(self: SageCategory, *args: Any, **kwargs: Any) -> None:
            initializer(self, *args, **kwargs)
            _register_cat_constructor_owner(self)

        setattr(
            initialize_and_register,
            "_cat_constructor_registration_wrapper",
            True,
        )
        setattr(cls, "__init__", initialize_and_register)

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

    @final
    def category(self) -> SageCategory:
        r"""Return ``Cat()`` as the category of this category object.

        This is the only direct semantic override in the mixin.  Without it,
        Sage's ``Category.category`` reports ``Objects()`` for category
        objects, so ``Sets().category()`` would not be ``Cat()`` and ordinary
        Sage membership ``Sets() in Cat()`` would not express that categories
        are objects of the category of categories.  The returned value is the
        same singleton stored by
        ``CategoryObject._init_category_`` during initialization.
        """
        return _cat_category()

    @final
    def Hom(self, codomain: SageCategory) -> Hom:
        r"""Return ``Hom_{Cat}(self, codomain)``."""
        assert codomain in self.category(), "codomain must be an object of Cat()"
        return cast(Hom, Parent.Hom(self, codomain))

    @final
    def _make_named_class(
        self,
        name: str,
        method_provider: str,
        cache: bool = False,
        picklable: bool = True,
    ) -> type:
        r"""Inject Cat's universal ``SubcategoryMethods`` into wrapped categories.

        The wrapper layer owns this Sage-integration policy; this method only
        supplies the proper superclass delegate for the current wrapped base.
        """
        return _make_named_class_with_cat_subcategory_methods(
            self,
            getattr(super(), "_make_named_class"),
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
    def __classcall__(cls: type[SageCategorySingleton]) -> SageCategory:
        if isinstance(cls, DynamicMetaclass):
            cls = cls.__base__
        obj = getattr(super(SageCategorySingleton, cls), "__classcall__")(cls)
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
    def __classcall__(
        cls: type[SageCategoryWithAxiomSingleton],
        base_category: SageCategory | None = None,
    ) -> SageCategory:
        if isinstance(cls, DynamicMetaclass):
            cls = cls.__base__
        if base_category is None:
            return getattr(SageCategoryWithAxiom, "__classcall__")(cls)
        obj = getattr(super(SageCategorySingleton, cls), "__classcall__")(cls, base_category)
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

    def __init__(self, base_category: SageCategory | None = None) -> None:
        assert base_category is not None, "singleton axiom initialization requires a resolved base category"
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

    def Endset(self) -> SageCategory:
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
        match hasattr(type(self), "Endset"):
            case True:
                axiom_category = type(self).Endset
                if isinstance(axiom_category, type) and issubclass(axiom_category, SageCategoryWithAxiom):
                    return axiom_category(self)
                return SageHomsets().Endset()
            case False:
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

    class ParentMethods:
        @abstractmethod
        def ambient(self) -> CategoryObject:
            r"""Return the ambient object of which ``self`` is a subobject."""
            ...

        @abstractmethod
        def inclusion(self) -> Morphism:
            r"""Return the inclusion morphism from this subobject to its ambient."""
            ...

        @final
        def lift(self, x: CategoryElement) -> CategoryElement:
            r"""Include an element of this subobject into its ambient object."""
            return self.inclusion()(x)


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
