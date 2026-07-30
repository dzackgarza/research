r"""Override-refine: category methods before class methods.

Sage's ``Parent._refine_category_`` builds

    dynamic_class(name, (concrete_base, category.parent_class))

so concrete class methods shadow ``ParentMethods``.  This module flips that
order and installs thin facades so Cython elements / morphisms
(``__dictoffset__ == 0``) can still receive ``ElementMethods`` /
``MorphismMethods``, including dunders.

Categories install by calling :func:`hook_post_init` on the relevant Sage
*class* (not by replacing constructors, and not by ``setattr`` of API methods).

EXAMPLES::

    sage: from dzack_research.preamble.refine import refine
    sage: from dzack_research.preamble.categories import IntegralLattices
    sage: from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
    sage: from sage.matrix.constructor import matrix
    sage: from sage.rings.integer_ring import ZZ
    sage: L = IntegralLattice(matrix(ZZ, [[0, 1], [1, 0]]))
    sage: refine(L, IntegralLattices())
    sage: L.q(L.gens()[0])
    0
"""

from typing import Any, Callable

from sage.categories.morphism import Morphism
from sage.cpython.type import can_assign_class
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer_ring import ZZ
from sage.structure.category_object import CategoryObject
from sage.structure.dynamic_class import dynamic_class
from sage.structure.element import Element, ModuleElement

__all__ = [
    "ElementFacade",
    "MorphismFacade",
    "hook_post_init",
    "hooked_classes",
    "refine",
    "unwrap",
    "without_element_wrap",
    "wrap_element",
    "wrap_morphism",
]

_HOOKS: dict[type, list[tuple[Any, Callable[[Any], bool] | None]]] = {}
_ORIGINAL_INIT: dict[type, Any] = {}
_AFTER: dict[type, list[Callable[[Any], None]]] = {}
_WRAP_DEPTH = 0

class without_element_wrap:
    """Context manager: disable facade wrapping (for native Sage constructors)."""

    def __enter__(self) -> without_element_wrap:
        global _WRAP_DEPTH
        _WRAP_DEPTH += 1
        return self

    def __exit__(self, *exc: object) -> None:
        global _WRAP_DEPTH
        _WRAP_DEPTH -= 1

def unwrap(x: Any) -> Any:
    """Return the native value inside a preamble facade, else ``x``."""
    if isinstance(x, (ElementFacade, MorphismFacade)):
        return object.__getattribute__(x, "_value")
    return getattr(x, "_value", x) if getattr(x, "_preamble_facade", False) else x

class ElementFacade(ModuleElement):
    r"""Python facade around a Cython Sage element.

    Holds the native value at ``_value`` and forwards unknown attributes.
    Category ``ElementMethods`` sit *before* this class in the dynamic
    ``element_class`` MRO, so redefined dunders win.
    """

    _preamble_facade = True
    _native_element_type: type | None = None

    def __init__(self, parent: Any, *args: Any, **kwargs: Any) -> None:
        native_type = type(self)._native_element_type
        assert native_type is not None, "element facade missing native element type"

        if len(args) == 1 and not kwargs:
            only = args[0]
            if isinstance(only, ElementFacade):
                value = object.__getattribute__(only, "_value")
            elif isinstance(only, native_type):
                value = only
            elif isinstance(only, Element) and only.parent() is parent:
                value = native_type(parent, unwrap(only))
            elif isinstance(only, (list, tuple, FreeModuleElement)):
                entries = [ZZ(c) for c in only]
                assert len(entries) == parent.rank(), (
                    f"expected {parent.rank()} coordinates, got {len(entries)}"
                )
                value = native_type(parent, entries)
            else:
                value = native_type(parent, *args, **kwargs)
        else:
            value = native_type(parent, *args, **kwargs)

        ModuleElement.__init__(self, parent)
        object.__setattr__(self, "_value", value)

    def __getattr__(self, name: str) -> Any:
        return getattr(object.__getattribute__(self, "_value"), name)

    def __repr__(self) -> str:
        return repr(object.__getattribute__(self, "_value"))

    def __str__(self) -> str:
        return str(object.__getattribute__(self, "_value"))

    def __bool__(self) -> bool:
        return bool(object.__getattribute__(self, "_value"))

    def __len__(self) -> int:
        return len(object.__getattribute__(self, "_value"))

    def __iter__(self):
        return iter(object.__getattribute__(self, "_value"))

    def __getitem__(self, key: Any) -> Any:
        return object.__getattribute__(self, "_value")[key]

    def _sage_hash_(self) -> int:
        return hash(object.__getattribute__(self, "_value"))

    def __hash__(self) -> int:
        return hash(object.__getattribute__(self, "_value"))

    def __richcmp__(self, other: Any, op: int) -> Any:
        r"""Compare via the native value.

        ``Element`` installs a Cython ``tp_richcompare`` that subclasses inherit.
        Python ``__eq__`` alone is ignored for ``==``, so facade-vs-native
        comparisons enter coercion and recurse.  ``__richcmp__`` replaces that slot.
        """
        from sage.structure.richcmp import richcmp

        return richcmp(
            object.__getattribute__(self, "_value"),
            unwrap(other),
            op,
        )

    def __eq__(self, other: Any) -> bool:
        return bool(self.__richcmp__(other, 2))

    def __ne__(self, other: Any) -> bool:
        return bool(self.__richcmp__(other, 3))

class MorphismFacade(Morphism):
    r"""Python facade around a Cython Sage morphism.

    Same strategy as :class:`ElementFacade`: keep the native morphism for
    construction/coercion, wrap at the API boundary, and put category
    ``MorphismMethods`` *before* this class in the dynamic MRO.
    """

    _preamble_facade = True
    _native_morphism_type: type | None = None

    def __init__(self, parent: Any, *args: Any, **kwargs: Any) -> None:
        if len(args) == 1 and not kwargs:
            only = args[0]
            if isinstance(only, MorphismFacade):
                value = object.__getattribute__(only, "_value")
            elif isinstance(only, Morphism):
                value = unwrap(only)
            else:
                native_type = type(self)._native_morphism_type
                assert native_type is not None, "morphism facade missing native type"
                value = native_type(parent, only)
        else:
            native_type = type(self)._native_morphism_type
            assert native_type is not None, "morphism facade missing native type"
            value = native_type(parent, *args, **kwargs)

        Morphism.__init__(self, parent)
        object.__setattr__(self, "_value", value)

    def _call_(self, x: Any) -> Any:
        return object.__getattribute__(self, "_value")(x)

    def __getattr__(self, name: str) -> Any:
        return getattr(object.__getattribute__(self, "_value"), name)

    def __repr__(self) -> str:
        return repr(object.__getattribute__(self, "_value"))

    def __str__(self) -> str:
        return str(object.__getattribute__(self, "_value"))

    def __bool__(self) -> bool:
        return bool(object.__getattribute__(self, "_value"))

    def _sage_hash_(self) -> int:
        return hash(object.__getattribute__(self, "_value"))

    def __hash__(self) -> int:
        return hash(object.__getattribute__(self, "_value"))

    def __richcmp__(self, other: Any, op: int) -> Any:
        from sage.structure.richcmp import richcmp

        return richcmp(
            object.__getattribute__(self, "_value"),
            unwrap(other),
            op,
        )

    def __eq__(self, other: Any) -> bool:
        return bool(self.__richcmp__(other, 2))

    def __ne__(self, other: Any) -> bool:
        return bool(self.__richcmp__(other, 3))

class _HomWrapParentMethods:
    """Wrap Homset ``__call__`` output in the morphism facade when installed."""

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return wrap_morphism(self, super().__call__(*args, **kwargs))  # type: ignore[misc]

def _concrete_base(obj: Any) -> type:
    """Return the non-dynamic concrete class Sage would use as ``__base__``."""
    cls = type(obj)
    cached = getattr(cls, "_preamble_concrete", None)
    if cached is not None:
        return cached

    for candidate in cls.__mro__:
        name = candidate.__name__
        if name.endswith("_with_category"):
            continue
        if name in {
            "parent_class",
            "element_class",
            "morphism_class",
            "ParentMethods",
            "ElementMethods",
            "MorphismMethods",
            "_HomWrapParentMethods",
        }:
            continue
        if candidate is object:
            continue
        return candidate
    raise TypeError(f"cannot find concrete base for {cls!r}")

_OWNED_CATEGORY_NAMES = frozenset(
    {
        "IntegralLattices",
        "DirectSumObjects",
        "HyperbolicLattices",
        "LatticeHomomorphisms",
        "LatticeIsometries",
        "TorsionModulesWithForm",
        "DiscriminantBilinearModules",
        "DiscriminantQuadraticModules",
        "FinitelyPresentedGroups",
    }
)


def _preamble_mixins(category: Any, attr: str) -> tuple[type, ...]:
    """Collect preamble ``ParentMethods`` / ``ElementMethods`` / ``MorphismMethods``."""
    mixins: list[type] = []
    for cat in category.all_super_categories(proper=False):
        name = type(cat).__name__
        if not any(name == owned or name.startswith(owned + "_") for owned in _OWNED_CATEGORY_NAMES):
            continue
        nested = getattr(type(cat), attr, None)
        if nested is None:
            continue
        if nested not in mixins:
            mixins.append(nested)
    return tuple(mixins)

def _method_mixins(category: Any, attr: str) -> tuple[type, ...]:
    """Preamble mixins if present; otherwise the category's own nested methods class."""
    mixins = _preamble_mixins(category, attr)
    if mixins:
        return mixins
    nested = getattr(type(category), attr, None)
    if nested is not None:
        return (nested,)
    return ()

def _is_homset(obj: Any) -> bool:
    from sage.categories.homset import Homset

    return isinstance(obj, Homset)

def _rebuild_parent_class(obj: Any, category: Any) -> None:
    if not can_assign_class(obj):
        raise TypeError(
            f"cannot assign __class__ on {type(obj).__name__}; "
            "override-refine requires a heap type"
        )

    concrete = _concrete_base(obj)
    # Only preamble/category ParentMethods mixins precede the concrete class —
    # never the full Sage parent_class (which would hoist Modules.basis etc.).
    mixins: list[type] = list(_method_mixins(category, "ParentMethods"))
    if _is_homset(obj) and _method_mixins(category, "MorphismMethods"):
        mixins = [_HomWrapParentMethods, *mixins]
    if not mixins:
        return
    new_cls = dynamic_class(
        f"{concrete.__name__}_with_category",
        (*mixins, concrete),
        doccls=concrete,
    )
    new_cls._preamble_concrete = concrete
    obj.__class__ = new_cls

def _rebuild_element_class(parent: Any, category: Any) -> None:
    """Install element-method override without breaking Cython construction.

    Python elements get ``(*ElementMethods, native)`` as ``element_class``.
    Cython elements keep the native ``element_class`` for constructors/coercion
    and gain ``_preamble_element_class = (*ElementMethods, ElementFacade)``.
    """
    native = parent.Element

    mixins = _method_mixins(category, "ElementMethods")
    if not mixins:
        return

    for key in ("element_class", "_abstract_element_class"):
        parent.__dict__.pop(key, None)

    if native.__dictoffset__ != 0:
        parent.element_class = dynamic_class(
            f"{type(parent).__name__}.element_class",
            (*mixins, native),
            doccls=native,
        )
        return

    facade = dynamic_class(
        f"{type(parent).__name__}.preamble_element",
        (*mixins, ElementFacade),
        doccls=native,
    )
    facade._native_element_type = native
    facade._preamble_facade = True
    # Inherited __richcmp__ does not replace Element's Cython tp_richcompare;
    # assign on the dynamic class so facade↔native comparisons unwrap.
    facade.__richcmp__ = ElementFacade.__richcmp__
    parent._preamble_element_class = facade

def _native_morphism_type(hom: Any) -> type:
    native = hom.Element
    assert isinstance(native, type), f"{hom} has no morphism element class"
    return native

def _install_morphism_facade(hom: Any, mixins: tuple[type, ...], native: type) -> type:
    """Install ``_preamble_morphism_class`` on ``hom``; return the facade class."""
    existing = getattr(hom, "_preamble_morphism_class", None)
    if existing is not None and existing._native_morphism_type is native:
        return existing

    facade = dynamic_class(
        f"{type(hom).__name__}.preamble_morphism",
        (*mixins, MorphismFacade),
        doccls=native,
    )
    facade._native_morphism_type = native
    facade._preamble_facade = True
    hom._preamble_morphism_class = facade
    return facade

def _rebuild_morphism_class(hom: Any, category: Any) -> None:
    """Install morphism-method override without breaking Cython construction.

    Heap morphisms get ``(*MorphismMethods, native)`` as a parallel facade class
    used by :func:`wrap_morphism`.  Cython morphisms keep their native type for
    construction and gain ``_preamble_morphism_class = (*MorphismMethods, MorphismFacade)``.
    """
    if not _is_homset(hom):
        return

    mixins = _method_mixins(category, "MorphismMethods")
    if not mixins:
        return

    native = _native_morphism_type(hom)
    if native.__dictoffset__ != 0:
        # Heap morphisms: MorphismMethods before native, still via facade wrap so
        # Hom construction stays untouched (same boundary rule as Cython elements).
        facade = dynamic_class(
            f"{type(hom).__name__}.preamble_morphism",
            (*mixins, native),
            doccls=native,
        )
        facade._native_morphism_type = native
        facade._preamble_facade = True
        hom._preamble_morphism_class = facade
        return

    _install_morphism_facade(hom, mixins, native)

def _refine_morphism(obj: Any, category: Any) -> Any:
    """Refine a morphism: assign class when possible, else wrap in a facade."""
    mixins = _method_mixins(category, "MorphismMethods")
    if not mixins:
        mixins = _method_mixins(category, "ElementMethods")
    if not mixins:
        return obj

    if can_assign_class(obj):
        concrete = _concrete_base(obj)
        new_cls = dynamic_class(
            f"{concrete.__name__}_with_category",
            (*mixins, concrete),
            doccls=concrete,
        )
        new_cls._preamble_concrete = concrete
        obj.__class__ = new_cls
        return obj

    # Cython morphism: same workaround as Cython elements — facade + wrap.
    parent = obj.parent()
    native = type(unwrap(obj))
    _install_morphism_facade(parent, mixins, native)
    if can_assign_class(parent) and _HomWrapParentMethods not in type(parent).__mro__:
        # Ensure subsequent Hom(...) production also wraps.
        concrete = _concrete_base(parent)
        parent_mixins = list(_method_mixins(category, "ParentMethods"))
        parent_mixins = [_HomWrapParentMethods, *parent_mixins]
        new_parent_cls = dynamic_class(
            f"{concrete.__name__}_with_category",
            (*parent_mixins, concrete),
            doccls=concrete,
        )
        new_parent_cls._preamble_concrete = concrete
        parent.__class__ = new_parent_cls
    return wrap_morphism(parent, obj)

def refine(obj: Any, category: Any) -> Any:
    r"""Refine ``obj`` so ``category``'s methods precede concrete class methods.

    Joins ``category`` into ``obj.category()`` as Sage does, then rebuilds
    ``obj.__class__`` as ``(category.ParentMethods, concrete)`` — only the
    *new* subcategory's methods first (not the full ``parent_class``, which
    would hoist unrelated Sage category methods over the concrete class).

    For parents, also rebuilds element / morphism facades when those objects
    are Cython.  For Cython morphisms, returns a :class:`MorphismFacade`
    wrapper (the native instance cannot host ``__class__`` assignment).

    Morphisms and elements are *not* passed through Sage's
    ``_refine_category_``: they do not store ``_category`` (membership lives
    on the parent / Hom), and calling it segfaults.
    """
    if isinstance(category, (list, tuple)):
        from sage.categories.category import Category

        category = Category.join(category)

    from sage.structure.parent import Parent

    if isinstance(obj, Parent):
        CategoryObject._refine_category_(obj, category)
        _rebuild_parent_class(obj, category)
        _rebuild_element_class(obj, category)
        _rebuild_morphism_class(obj, category)
        return obj

    if isinstance(obj, Morphism) or (
        isinstance(obj, Element) and _is_homset(obj.parent())
    ):
        return _refine_morphism(obj, category)

    CategoryObject._refine_category_(obj, category)

    # Other assignable category objects.
    if can_assign_class(obj):
        concrete = _concrete_base(obj)
        mixins = (
            _method_mixins(category, "MorphismMethods")
            or _method_mixins(category, "ElementMethods")
            or _method_mixins(category, "ParentMethods")
        )
        if not mixins:
            return obj
        new_cls = dynamic_class(
            f"{concrete.__name__}_with_category",
            (*mixins, concrete),
            doccls=concrete,
        )
        new_cls._preamble_concrete = concrete
        obj.__class__ = new_cls
    return obj

def wrap_element(parent: Any, value: Any) -> Any:
    """Wrap ``value`` in the preamble element facade when one is installed."""
    if value is None or _WRAP_DEPTH:
        return value
    facade_cls = getattr(parent, "_preamble_element_class", None)
    if facade_cls is None:
        elem_cls = getattr(parent, "element_class", None)
        if elem_cls is not None and getattr(elem_cls, "_preamble_facade", False):
            facade_cls = elem_cls
    if facade_cls is None:
        return value
    if isinstance(value, facade_cls):
        return value
    return facade_cls(parent, unwrap(value))

def wrap_morphism(hom: Any, value: Any) -> Any:
    """Wrap ``value`` in the preamble morphism facade when one is installed.

    Cython morphisms become :class:`MorphismFacade` instances.  Heap morphisms
    get ``__class__`` reassigned so ``MorphismMethods`` precede the concrete
    class — same MRO flip as parents, without replacing the instance.
    """
    if value is None or _WRAP_DEPTH:
        return value
    facade_cls = getattr(hom, "_preamble_morphism_class", None)
    if facade_cls is None:
        return value
    if isinstance(value, facade_cls):
        return value

    leading: list[type] = []
    native = facade_cls._native_morphism_type
    for base in facade_cls.__mro__:
        if base is facade_cls:
            continue
        if base is MorphismFacade or base is native:
            break
        leading.append(base)

    if can_assign_class(value) and leading:
        concrete = _concrete_base(value)
        new_cls = dynamic_class(
            f"{concrete.__name__}_with_category",
            (*leading, concrete),
            doccls=concrete,
        )
        new_cls._preamble_concrete = concrete
        value.__class__ = new_cls
        return value

    return facade_cls(hom, unwrap(value))

def hook_post_init(
    cls: type,
    category: Any,
    *,
    predicate: Callable[[Any], bool] | None = None,
    after: Callable[[Any], None] | None = None,
) -> None:
    r"""After ``cls.__init__``, :func:`refine` the instance into ``category``.

    This is the only class-level intervention categories need.  It does not
    replace constructors and does not ``setattr`` API methods.

    ``after(self)`` runs after refine (e.g. Gram subdivisions).
    ``predicate(self)`` skips refine when false.
    """
    entries = _HOOKS.setdefault(cls, [])
    for existing_cat, existing_pred in entries:
        if existing_cat == category and existing_pred is predicate:
            return
    entries.append((category, predicate))

    if cls not in _ORIGINAL_INIT:
        _ORIGINAL_INIT[cls] = cls.__init__

        def _init(self: Any, *args: Any, **kwargs: Any) -> None:
            _ORIGINAL_INIT[cls](self, *args, **kwargs)
            for cat, pred in _HOOKS.get(cls, ()):
                if pred is not None and not pred(self):
                    continue
                refine(self, cat)
            after_hooks = _AFTER.get(cls)
            if after_hooks:
                for hook in after_hooks:
                    hook(self)

        cls.__init__ = _init  # noqa: intentional post-init registration

    if after is not None:
        _AFTER.setdefault(cls, [])
        if after not in _AFTER[cls]:
            _AFTER[cls].append(after)

def hooked_classes() -> tuple[type, ...]:
    """Return classes with a preamble post-init hook."""
    return tuple(_HOOKS)
