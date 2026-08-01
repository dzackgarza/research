r"""Override-refine: category methods before class methods.

Sage's ``Parent._refine_category_`` builds

    dynamic_class(name, (concrete_base, category.parent_class))

so concrete class methods shadow ``ParentMethods``.  This module flips that
order:

- parents (including homsets and standalone category objects) get
  ``(*ParentMethods, concrete)`` as their class;
- element-bearing parents get ``element_class = (*ElementMethods, native)``
  — a dynamic *subclass* of the native element type.  Sage sanctions
  subclassing Cython element classes (``Parent.__make_element_class__``,
  :issue:`24715`); instances are genuine native elements for every Sage
  code path (isinstance, hashing, comparison, arithmetic — Cython
  ``_new_c`` preserves the subclass), while category dunders win;
- morphisms get ``(*MorphismMethods, concrete)`` by ``__class__``
  assignment (Sage's own morphism classes are heap types).

Categories install by calling :func:`hook_post_init` on the relevant Sage
*class* (not by replacing constructors, and not by ``setattr`` of API
methods).

EXAMPLES::

    sage: from dzack_research.preamble.refine import refine
    sage: from dzack_research.preamble.categories import IntegralLattices
    sage: from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
    sage: from sage.matrix.constructor import matrix
    sage: from sage.rings.integer_ring import ZZ
    sage: L = _integral_lattice_with_names(matrix(ZZ, [[0, 1], [1, 0]]))
    sage: refine(L, IntegralLattices())
    sage: L.q(L.gens()[0])
    0
"""

from typing import Any, Callable

from sage.categories.morphism import Morphism
from sage.cpython.type import can_assign_class
from sage.structure.category_object import CategoryObject
from sage.structure.dynamic_class import dynamic_class
from sage.structure.element import Element

__all__ = [
    "hook_post_init",
    "hooked_classes",
    "refine",
]

_HOOKS: dict[type, list[tuple[Any, Callable[[Any], bool] | None]]] = {}
_ORIGINAL_INIT: dict[type, Any] = {}
_AFTER: dict[type, list[Callable[[Any], None]]] = {}
_BEFORE: dict[type, list[Callable[[Any], None]]] = {}

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
        }:
            continue
        if candidate is object:
            continue
        return candidate
    assert False, f"cannot find concrete base for {cls!r}"  # noqa: B011

_OWNED_CATEGORY_NAMES = frozenset(
    {
        "IntegralLattices",
        "DirectSumObjects",
        "HyperbolicLattices",
        "LatticeHomomorphisms",
        "LatticeIsometries",
        "OwnedGroups",
        "OwnedFiniteGroups",
        "FinitelyGeneratedModules",
        "FramedModules",
        "FinitelyPresentedModules",
        "FreeModules",
        "FramedFreeModules",
        "FinitelyGeneratedFreeModules",
        "TorsionModules",
        "FinitelyPresentedTorsionModules",
        "GroupModules",
        "GroupLattices",
        "FormModules",
        "BilinearFormModules",
        "QuadraticFormModules",
        "Subobjects",
        "FreeFormModules",
        "TorsionModulesWithForm",
        "DiscriminantBilinearModules",
        "DiscriminantQuadraticModules",
        "FinitelyPresentedGroups",
        "PicardGroups",
        "DivisorGroups",
        "ClassGroups",
        "WeilDivisorGroups",
        "CartierDivisorGroups",
        "RingedSpaces",
        "LocallyRingedSpaces",
        "Schemes",
        "AffineSpaces",
        "ProjectiveSpaces",
        "ClosedSubschemes",
        "OpenSubschemes",
        "Varieties",
        "Curves",
        "Surfaces",
        "AffineSpace",
        "ProjectiveSpace",
        "Subscheme",
        "OpenSubscheme",
        "ClosedSubscheme",
        "QuasiScheme",
        "ToricVariety",
        "Curve",
        "Surface",
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

def _is_morphism(obj: Any) -> bool:
    """Return whether ``obj`` is a map rather than an object of a category.

    Sage's own morphisms say so by their type, and an element of a homset says
    so by its parent.  An owned morphism is neither: it is a plain object with
    a domain and a codomain, which is what being a map consists of here, so
    that is what is asked.
    """
    if isinstance(obj, Morphism):
        return True
    if isinstance(obj, Element) and _is_homset(obj.parent()):
        return True
    return (
        not isinstance(obj, CategoryObject)
        and hasattr(obj, "domain")
        and hasattr(obj, "codomain")
    )

def _rebuild_parent_class(obj: Any, category: Any) -> None:
    # Only preamble/category ParentMethods mixins precede the concrete class —
    # never the full Sage parent_class (which would hoist Modules.basis etc.).
    mixins = _method_mixins(category, "ParentMethods")
    if not mixins:
        return
    assert can_assign_class(obj), (
        f"cannot assign __class__ on {type(obj).__name__}; "
        "override-refine requires a heap type"
    )
    concrete = _concrete_base(obj)
    new_cls = dynamic_class(
        f"{concrete.__name__}_with_category",
        (*mixins, concrete),
        doccls=concrete,
    )
    new_cls._preamble_concrete = concrete
    obj.__class__ = new_cls

def _rebuild_element_class(parent: Any, category: Any) -> None:
    """Install ``element_class = (*ElementMethods, native)``.

    Only called for element-bearing parents (:func:`refine` routes homsets
    and morphisms elsewhere).  When the category requests ``ElementMethods``,
    the parent must declare its native element type via Sage's
    nested-``Element`` convention — the raw ingredient
    ``Parent.element_class`` itself is built from.

    Elements the parent constructed *before* refinement (its stored basis)
    keep the plain native type; parents hand out ``element_class`` instances
    at their output boundary (``gens`` in the owning ``ParentMethods``).
    """
    mixins = _method_mixins(category, "ElementMethods")
    if not mixins:
        return

    native = getattr(parent, "Element", Element)

    for key in ("element_class", "_abstract_element_class"):
        parent.__dict__.pop(key, None)

    parent.element_class = dynamic_class(
        f"{type(parent).__name__}.element_class",
        (*mixins, native),
        doccls=native,
    )

def _refine_morphism(obj: Any, category: Any) -> Any:
    """Reassign a morphism's class so ``MorphismMethods`` precede it."""
    mixins = _method_mixins(category, "MorphismMethods")
    if not mixins:
        return obj

    assert can_assign_class(obj), (
        f"cannot assign __class__ on {type(obj).__name__}; "
        "override-refine requires a heap morphism type"
    )
    concrete = _concrete_base(obj)
    new_cls = dynamic_class(
        f"{concrete.__name__}_with_category",
        (*mixins, concrete),
        doccls=concrete,
    )
    new_cls._preamble_concrete = concrete
    obj.__class__ = new_cls
    return obj

def refine(obj: Any, category: Any) -> Any:
    r"""Refine ``obj`` so ``category``'s methods precede concrete class methods.

    Joins ``category`` into ``obj.category()`` as Sage does, then rebuilds
    ``obj.__class__`` as ``(category.ParentMethods, concrete)`` — only the
    *new* subcategory's methods first (not the full ``parent_class``, which
    would hoist unrelated Sage category methods over the concrete class).

    Element-bearing parents additionally get the subclassed
    ``element_class``.  Morphisms get ``MorphismMethods`` by ``__class__``
    assignment; they are *not* passed through Sage's ``_refine_category_``
    (they do not store ``_category`` — membership lives on the Hom).
    """
    if isinstance(category, (list, tuple)):
        from sage.categories.category import Category

        category = Category.join(category)

    if _is_morphism(obj):
        return _refine_morphism(obj, category)

    from sage.structure.parent import Parent

    # Objects of the category — parents, homsets, and standalone category
    # objects alike — receive ``ParentMethods`` before their concrete class.
    CategoryObject._refine_category_(obj, category)
    _rebuild_parent_class(obj, category)

    # An element-bearing parent manufactures elements; homsets manufacture
    # morphisms (their ``ParentMethods.__call__`` refines each one) and
    # standalone category objects manufacture neither.
    if isinstance(obj, Parent) and not _is_homset(obj):
        _rebuild_element_class(obj, category)
    return obj

def hook_post_init(
    cls: type,
    category: Any,
    *,
    predicate: Callable[[Any], bool] | None = None,
    before: Callable[[Any], None] | None = None,
    after: Callable[[Any], None] | None = None,
) -> None:
    r"""After ``cls.__init__``, :func:`refine` the instance into ``category``.

    This is the only class-level intervention categories need.  It does not
    replace constructors and does not ``setattr`` API methods.

    ``before(self)`` runs before refine, which is where a class claims its own
    concrete and element types: refine reads both when it builds the parent and
    element classes, so a later hook would be too late.
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
            for hook in _BEFORE.get(cls, ()):
                hook(self)
            for cat, pred in _HOOKS.get(cls, ()):
                if pred is not None and not pred(self):
                    continue
                refine(self, cat)
            after_hooks = _AFTER.get(cls)
            if after_hooks:
                for hook in after_hooks:
                    hook(self)

        cls.__init__ = _init  # noqa: intentional post-init registration

    if before is not None:
        _BEFORE.setdefault(cls, [])
        if before not in _BEFORE[cls]:
            _BEFORE[cls].append(before)

    if after is not None:
        _AFTER.setdefault(cls, [])
        if after not in _AFTER[cls]:
            _AFTER[cls].append(after)

def hooked_classes() -> tuple[type, ...]:
    """Return classes with a preamble post-init hook."""
    return tuple(_HOOKS)
