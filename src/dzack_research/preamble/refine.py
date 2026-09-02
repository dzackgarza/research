"""Owned category refinement with owned methods before concrete Sage methods.

Sage's ``_refine_category_`` joins categories but leaves the concrete class
before category methods in the MRO.  The preamble owns its interfaces, so an
adopted Sage parent is additionally reclassed with this package's method
providers before the class Sage constructed.  The object itself is unchanged.
"""

from collections.abc import Callable, Iterable

from sage.categories.category import Category
from sage.structure.category_object import CategoryObject
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.structure.dynamic_class import dynamic_class
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

_PREAMBLE_PACKAGE = __name__.rpartition(".")[0] + "."
_HOOKS: dict[type, list[tuple[Category, Callable | None]]] = {}
_ORIGINAL_INIT: dict[type, Callable] = {}
_AFTER: dict[type, list[Callable]] = {}


def _owned_mixins(category: Category, attr: str) -> tuple[type, ...]:
    """Return owned nested method classes in category order."""
    providers: list[type] = []
    for cat in category.all_super_categories(proper=False):
        for category_type in type(cat).__mro__:
            if not category_type.__module__.startswith(_PREAMBLE_PACKAGE):
                continue
            provider = vars(category_type).get(attr)
            if isinstance(provider, type) and provider not in providers:
                providers.append(provider)
    return tuple(providers)


def _rebuild_parent_class(parent: Parent, category: Category) -> None:
    mixins = _owned_mixins(category, "ParentMethods")
    if not mixins:
        return
    inherited = type(parent).__dict__.get("_preamble_inherited", type(parent))
    carried = frozenset(inherited.__mro__)
    mixins = tuple(m for m in mixins if m is not object and m not in carried)
    if not mixins:
        return
    concrete = type(parent).__dict__.get("_preamble_concrete", inherited)
    new_class = dynamic_class(
        f"Owned{concrete.__name__}",
        (*mixins, inherited),
        doccls=concrete,
    )
    new_class._preamble_concrete = concrete
    new_class._preamble_inherited = inherited
    parent.__class__ = new_class



def _rebuild_element_class(parent: Parent, category: Category) -> None:
    from sage.categories.sets_cat import Sets as SageSets

    # A facade's elements belong to the parents it stands for; it has no
    # element class of its own to rebuild.
    if category.is_subcategory(SageSets().Facade()):
        return
    mixins = _owned_mixins(category, "ElementMethods")
    if not mixins:
        return
    native = parent.element_class
    carried = frozenset(native.__mro__)
    mixins = tuple(m for m in mixins if m is not object and m not in carried)
    if not mixins:
        return
    parent.__dict__.pop("_abstract_element_class", None)
    parent.element_class = dynamic_class(
        f"{type(parent).__name__}.element_class",
        (*mixins, native),
        doccls=native,
    )


def _rebuild_morphism_class(morphism: Morphism, category: Category) -> None:
    mixins = _owned_mixins(category, "MorphismMethods")
    if not mixins:
        return
    inherited = type(morphism).__dict__.get("_preamble_inherited", type(morphism))
    carried = frozenset(inherited.__mro__)
    mixins = tuple(m for m in mixins if m is not object and m not in carried)
    if not mixins:
        return
    concrete = type(morphism).__dict__.get("_preamble_concrete", inherited)
    new_class = dynamic_class(
        f"Owned{concrete.__name__}",
        (*mixins, inherited),
        doccls=concrete,
    )
    new_class._preamble_concrete = concrete
    new_class._preamble_inherited = inherited
    morphism.__class__ = new_class


def refine(obj: SageObject, category: Category | Iterable[Category]):
    """Join ``category`` into ``obj`` and give owned methods precedence."""
    target = category if isinstance(category, Category) else Category.join(tuple(category))
    if isinstance(obj, Morphism):
        _rebuild_morphism_class(obj, target)
        return obj
    CategoryObject._refine_category_(obj, target)
    if isinstance(obj, Parent):
        _rebuild_parent_class(obj, obj.category())
        _rebuild_element_class(obj, obj.category())
    return obj


def hook_post_init(
    cls: type,
    category: Category,
    *,
    predicate: Callable | None = None,
    after: Callable | None = None,
) -> None:
    """Refine instances of ``cls`` after their existing initializer finishes."""
    entries = _HOOKS.setdefault(cls, [])
    if not any(cat == category and pred is predicate for cat, pred in entries):
        entries.append((category, predicate))

    if cls not in _ORIGINAL_INIT:
        original = next(
            candidate.__dict__["__init__"]
            for candidate in cls.__mro__
            if "__init__" in candidate.__dict__
        )
        _ORIGINAL_INIT[cls] = original

        def _init(self, *args, **kwargs):
            _ORIGINAL_INIT[cls](self, *args, **kwargs)
            for cat, pred in _HOOKS.get(cls, ()):
                if pred is None or pred(self):
                    refine(self, cat)
            for callback in _AFTER.get(cls, ()):
                callback(self)

        cls.__init__ = _init  # intentional post-init admission hook

    if after is not None:
        callbacks = _AFTER.setdefault(cls, [])
        if after not in callbacks:
            callbacks.append(after)


def hooked_classes() -> tuple[type, ...]:
    return tuple(_HOOKS)
