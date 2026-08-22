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
    sage: refine(L, IntegralLattices(ZZ))
    sage: L.q(L.module_generators()[0])
    0
"""

from collections.abc import Callable, Iterable

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent
from sage.structure.parent import ElementConstructorInput
from sage.structure.sage_object import SageObject
from sage.cpython.type import can_assign_class
from sage.misc.abstract_method import AbstractMethod
from sage.structure.category_object import CategoryObject
from sage.structure.parent import Parent as SageParent
from sage.structure.dynamic_class import dynamic_class
from sage.structure.element import Element

from dzack_research.preamble.owned_category import (
    OwnedCategoryMixin,
    declared_implementation_types,
)

__all__ = [
    "hook_post_init",
    "hooked_classes",
    "refine",
]

_HOOKS: dict[
    type[SageObject],
    list[tuple[Category, Callable[[SageObject], bool] | None]],
] = {}
_ORIGINAL_INIT: dict[type[SageObject], Callable[..., None]] = {}
_AFTER: dict[type[SageObject], list[Callable[[SageObject], None]]] = {}
_BEFORE: dict[type[SageObject], list[Callable[[SageObject], None]]] = {}
_IMPLEMENTED_MIXINS: dict[type, type] = {}
_PY_SET = set


def _implemented_mixin(mixin: type) -> type:
    r"""Return the concrete implementations declared by ``mixin``.

    Sage abstract methods are category obligations.  They must not precede
    the concrete parent methods that satisfy them when override-refining.
    """
    cached = _IMPLEMENTED_MIXINS.get(mixin)
    if cached is not None:
        return cached
    abstract_names = _PY_SET(
        name
        for name, value in vars(mixin).items()
        if isinstance(value, AbstractMethod)
    )
    if not abstract_names:
        return mixin
    implemented = {
        name: value
        for name, value in vars(mixin).items()
        if name not in abstract_names
        and name not in _PY_SET(["__dict__", "__weakref__"])
    }
    filtered = type(
        f"{mixin.__name__}Implementations",
        (),
        implemented,
    )
    _IMPLEMENTED_MIXINS[mixin] = filtered
    return filtered

def _concrete_base(obj: "SageObject") -> type:
    """Return the non-dynamic concrete class Sage would use as ``__base__``."""
    cls = type(obj)
    cached: type | None = cls.__dict__.get("_preamble_concrete")
    if cached is not None:
        return cached

    for candidate in cls.__mro__:
        name = candidate.__name__
        if name.endswith("_with_category"):
            continue
        if name.endswith("_with_equality_by_id") or name == "WithEqualityById":
            # Sage's ``Hom`` splices identity comparison onto the class of the
            # homset it caches (``sage/categories/homset.py``).  That wrapper
            # is Sage's, and it is not the class the homset is built from.
            continue
        if name in _PY_SET((
            "parent_class",
            "element_class",
            "morphism_class",
            "ParentMethods",
            "ElementMethods",
            "MorphismMethods",
        )):
            continue
        if candidate is object:
            continue
        return candidate
    assert False, f"cannot find concrete base for {cls!r}"  # noqa: B011

# Ownership is provenance, which the class hierarchy already records: a
# category is this project's when its class was defined here.  The preamble
# is an ordinary package, so a category is owned when its ``__module__`` sits
# inside it.  Sage's own categories are never owned, so their
# ``ParentMethods`` are never hoisted over a concrete class.
#
# A name registry stood here instead, and an unlisted category's methods were
# silently dropped: once a refine target has *any* owned category among its
# super categories, ``_preamble_mixins`` stops being empty and the fallback in
# ``_method_mixins`` never runs.  Refining a lattice into ``TensorProduct``
# installed no ``cartesian_source`` for exactly this reason.  Provenance
# admits every owned category by construction, so there is nothing to omit.
_PREAMBLE_PACKAGE = __name__.rpartition(".")[0] + "."
assert _PREAMBLE_PACKAGE != ".", (
    "refine.sage must be imported as a module of the preamble package"
)
_MIXIN_CACHE: dict[tuple[Category, str], tuple[type, ...]] = {}

# A methods class that names one of these among its bases is an
# implementation class, not a mixin: it is the class an owned category is
# tied to. See ``dzack_research.preamble.owned_category``.
_IMPLEMENTATION_BASES = (Parent, Element, Morphism)


def _is_owned_category(category_type: type) -> bool:
    """Whether ``category_type`` was defined by this project."""
    return category_type.__module__.startswith(_PREAMBLE_PACKAGE)


def _preamble_mixins(category: "Category", attr: str) -> tuple[type, ...]:
    """Collect preamble ``ParentMethods`` / ``ElementMethods`` / ``MorphismMethods``."""
    mixins: list[type] = []
    for cat in category.all_super_categories(proper=False):
        category_type = type(cat)
        if not _is_owned_category(category_type):
            continue
        # Every declaration the category's class graph makes, not only the
        # most derived: a category class that both derives from an owned
        # construction base and declares its own methods class would
        # otherwise hide the base's, and the base would reach exactly those
        # categories with nothing of their own to add.
        provider, inherited = declared_implementation_types(
            category_type,
            OwnedCategoryMixin._IMPLEMENTATION_PROVIDER_NAMES[attr],
        )
        if provider is None:
            continue
        for nested in (provider,) + inherited:
            if issubclass(nested, _IMPLEMENTATION_BASES):
                # The root of an owned construction chain declares its methods
                # class to *be* the implementation class -- it names ``Parent``
                # (or ``Element``, or ``Morphism``) among its own bases; see
                # ``dzack_research.preamble.owned_category``.  An object built
                # through that chain already has the class in the right place.
                # An object the preamble *adopts* is a Sage parent with its own
                # instance layout, and a second structural base is not a mixin
                # it can wear: Python refuses the ``__class__`` assignment with
                # "object layout differs".  Its own category's ``parent_class``
                # still carries these methods, behind the concrete class where
                # a Sage parent's own definitions belong.
                continue
            implemented = _implemented_mixin(nested)
            if implemented not in mixins:
                mixins.append(implemented)
    return tuple(mixins)

def _method_mixins(category: "Category", attr: str) -> tuple[type, ...]:
    """Preamble mixins if present; otherwise the category's own nested methods class.

    Cached per ``(category, attr)`` the way Sage caches ``parent_class``: the
    answer is a fact about the category, and refinement asks for it once per
    constructed object.
    """
    key = (category, attr)
    cached = _MIXIN_CACHE.get(key)
    if cached is not None:
        return cached
    mixins = _preamble_mixins(category, attr)
    if not mixins:
        provider, inherited = declared_implementation_types(
            type(category),
            OwnedCategoryMixin._IMPLEMENTATION_PROVIDER_NAMES[attr],
        )
        mixins = (() if provider is None else (provider,) + inherited)
    _MIXIN_CACHE[key] = mixins
    return mixins

def _is_homset(obj: "SageObject") -> bool:
    from sage.categories.homset import Homset

    return isinstance(obj, Homset)

def _is_morphism(obj: "SageObject") -> bool:
    r"""Return whether ``obj`` is a Sage morphism."""
    return isinstance(obj, Morphism)

def _is_chain_built(obj: "SageObject") -> bool:
    r"""Whether ``obj``'s class comes from its category rather than a class.

    A chain-built parent has no hand-written parent class anywhere in its
    method resolution order: every entry is a category-generated class, a
    nested methods class, or one of Sage's own bases.  So the test is for a
    hand-written one, and finding none is what says the class *is* the
    category.

    A category generates its classes under the name
    ``"<category>.parent_class"`` -- Sage's ``Category._make_named_class``
    and the owned override both -- and Sage renames a refined parent's class
    with the suffix ``_with_category``.
    """
    for candidate in type(obj).__mro__:
        name = candidate.__name__
        if name.endswith("_with_category") or name.endswith(".parent_class"):
            continue
        if name.endswith("ParentMethods") or name == "Parent":
            continue
        if issubclass(candidate, SageParent):
            return False
    return True


def _resolved_requirements(category: "Category") -> type | None:
    r"""The concrete answer to each name the join declares abstract.

    In category order a subcategory precedes its supercategories, so a
    requirement declared on the subcategory -- ``EvenLattices.is_even`` --
    stands in front of the supercategory that computes it.  Reading the join
    puts the provider first: for every abstract name, the first concrete
    definition down the ``parent_class`` linearization is collected into one
    class, and that class is hoisted.  A name with no provider stays abstract,
    which is what the obligation assertion below reports.

    Only ``ParentMethods`` names are hoisted; the class itself cannot be,
    since C3 refuses a base that already sits inside the class it precedes.
    """
    required: set[str] = _PY_SET()
    for cat in category.all_super_categories(proper=False):
        category_type = type(cat)
        if not _is_owned_category(category_type):
            continue
        provider, inherited = declared_implementation_types(
            category_type,
            OwnedCategoryMixin._IMPLEMENTATION_PROVIDER_NAMES["ParentMethods"],
        )
        if provider is None:
            continue
        for methods in (provider,) + inherited:
            required.update(
                name
                for name, value in vars(methods).items()
                if isinstance(value, AbstractMethod)
            )
    resolved: dict[str, Callable[..., ElementConstructorInput]] = {}
    for name in required:
        for klass in category.parent_class.__mro__:
            value = vars(klass).get(name)
            if value is None or isinstance(value, AbstractMethod):
                continue
            resolved[name] = value
            break
    if not resolved:
        return None
    return type("ResolvedRequirements", (), resolved)


def _reclass_chain_built(obj: "Parent", category: "Category") -> None:
    r"""Install the joined ``parent_class``, resolved requirements in front."""
    resolved = _resolved_requirements(category)
    if resolved is None:
        obj.__class__ = category.parent_class
        return
    assert can_assign_class(obj), (
        f"cannot assign __class__ on {type(obj).__name__}; "
        "override-refine requires a heap type"
    )
    obj.__class__ = dynamic_class(
        f"{category.parent_class.__name__}_with_category",
        (resolved, category.parent_class),
        doccls=category.parent_class,
    )


def _rebuild_parent_class(obj: "Parent", category: "Category") -> None:
    # Owned ParentMethods precede the concrete class; the joined parent_class
    # follows it, which is where Sage itself puts it -- its own
    # ``X_with_category`` is ``(X, category.parent_class)``.  Only the *order*
    # is this preamble's: hoisting the full parent_class in front would put
    # ``Modules.basis`` and its fellows over the concrete class, and dropping
    # it took away everything Sage's categories supply and the preamble does
    # not restate.  ``CoxeterGroup.order()`` calls ``len(self)``, and
    # ``__len__`` is on ``FiniteEnumeratedSets.parent_class``.
    mixins = _method_mixins(category, "ParentMethods")
    if not mixins:
        return
    concrete = _concrete_base(obj)
    # The single base is the class the object already had -- Sage's own
    # ``X_with_category``, which is ``(X, its category.parent_class)``.  Using
    # the bare ``X`` instead dropped every method Sage's categories supply and
    # the preamble does not restate: ``CoxeterGroup.order()`` calls
    # ``len(self)``, and ``__len__`` is on ``FiniteEnumeratedSets.parent_class``.
    # Kept across a second refinement so the wrappers do not nest.
    inherited = type(obj).__dict__.get("_preamble_inherited", type(obj))
    # Hoist only what that class does not already carry.  A methods class
    # already inside it is installed, in category order, and C3 refuses a base
    # placed in front of a class that contains it: ``TypeError: Cannot create
    # a consistent method resolution order (MRO) for bases
    # FormModules.Homsets.ParentMethods, FormModules.Homsets.parent_class``.
    # ``object`` arrives here the same way, from a super category with no
    # methods class of its own, and is a base every other base derives from.
    carried = frozenset(inherited.__mro__)
    mixins = tuple(
        mixin for mixin in mixins if mixin is not object and mixin not in carried
    )
    if not mixins:
        return
    assert can_assign_class(obj), (
        f"cannot assign __class__ on {type(obj).__name__}; "
        "override-refine requires a heap type"
    )
    new_cls = dynamic_class(
        f"{concrete.__name__}_with_category",
        (*mixins, inherited),
        doccls=concrete,
    )
    new_cls._preamble_concrete = concrete
    new_cls._preamble_inherited = inherited
    obj.__class__ = new_cls

def _rebuild_element_class(parent: "Parent", category: "Category") -> None:
    """Install ``element_class = (*ElementMethods, native)``.

    Only called for element-bearing parents (:func:`refine` routes homsets
    and morphisms elsewhere).  When the category requests ``ElementMethods``,
    the parent must declare its native element type via Sage's
    nested-``Element`` convention — the raw ingredient
    ``Parent.element_class`` itself is built from.

    Elements the parent constructed *before* refinement (its stored basis)
    keep the plain native type; parents hand out ``element_class`` instances
    at their output boundary (``module_generators`` in the owning
    ``ParentMethods``).
    """
    mixins = _method_mixins(category, "ElementMethods")
    if not mixins:
        return

    native = next(
        (
            candidate.__dict__["Element"]
            for candidate in type(parent).__mro__
            if "Element" in candidate.__dict__
        ),
        Element,
    )

    for key in ("element_class", "_abstract_element_class"):
        parent.__dict__.pop(key, None)

    parent.element_class = dynamic_class(
        f"{type(parent).__name__}.element_class",
        (*mixins, native),
        doccls=native,
    )


def _assert_certifying_predicates_hold(
    obj: "SageObject",
    category: "Category",
) -> None:
    r"""Evaluate the predicates the target categories claim of their objects.

    A category class carrying ``_certifying_predicate`` names a method the
    candidate must answer ``True`` to be admitted -- ``is_nondegenerate`` for
    the ``Nondegenerate`` axiom, say.  The claim is always the participant's
    own: a finitely generated lattice computes its radical, while an object
    whose nondegeneracy is a theorem answers through its own method, which is
    then auditable by name on the object.  Placement never grants the
    property; the object asserts it, here, or is refused.
    """
    for cat in category.all_super_categories(proper=False):
        category_type = type(cat)
        if not _is_owned_category(category_type):
            continue
        # Read through the class: Sage hands out ``<Class>_with_category``
        # dynamic subclasses, so the marker sits one level up the MRO.
        predicate_name = next(
            (
                candidate.__dict__["_certifying_predicate"]
                for candidate in category_type.__mro__
                if "_certifying_predicate" in candidate.__dict__
            ),
            None,
        )
        if predicate_name is None:
            continue
        match predicate_name:
            case "is_finitely_generated":
                certified = obj.is_finitely_generated()
            case "is_integral":
                certified = obj.is_integral()
            case "is_nondegenerate":
                certified = obj.is_nondegenerate()
            case "is_even":
                certified = obj.is_even()
            case _:
                raise AssertionError(
                    f"unknown certifying predicate {predicate_name!r}"
                )
        assert certified is True, (
            f"refining {obj} into {cat} requires {predicate_name}() to hold, "
            "and the object answers otherwise"
        )


def _assert_preamble_obligations_are_met(
    obj: "SageObject",
    category: "Category",
) -> None:
    r"""Require the data declared abstract by the preamble's categories."""
    required: set[str] = set()
    for cat in category.all_super_categories(proper=False):
        if not type(cat).__module__.startswith(_PREAMBLE_PACKAGE):
            continue
        provider, inherited = _declared_method_providers(
            cat, type(cat), "ParentMethods"
        )
        if provider is None:
            continue
        for methods in (provider,) + inherited:
            required.update(
                name
                for name, value in vars(methods).items()
                if isinstance(value, AbstractMethod)
            )
    missing: list[str] = []
    for name in required:
        implementation = next(
            (
                candidate.__dict__[name]
                for candidate in type(obj).__mro__
                if name in candidate.__dict__
            ),
            None,
        )
        if implementation is None or isinstance(implementation, AbstractMethod):
            missing.append(name)
    assert not missing, (
        f"refining {obj} into {category} requires implementations of "
        f"{sorted(missing)}"
    )

def _refine_morphism[M: Morphism](obj: M, category: "Category") -> M:
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

def refine[S: SageObject](
    obj: S,
    category: "Category | Iterable[Category]",
) -> S:
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
    target_category = (
        category
        if isinstance(category, Category)
        else Category.join(category)
    )

    if _is_morphism(obj):
        return _refine_morphism(obj, target_category)

    from sage.structure.parent import Parent

    # Objects of the category — parents, homsets, and standalone category
    # objects alike — receive ``ParentMethods`` before their concrete class.
    CategoryObject._refine_category_(obj, target_category)
    # Rebuilt from the object's *joined* category, never from this call's
    # argument.  The join is what the object now claims to be, and the class
    # has to say the same thing: rebuilding from the argument alone starts
    # again at the concrete base, so a second refine drops the mixins the
    # first one installed and the last call wins.  Reading the join keeps the
    # class a function of the category, so refining is order-independent and
    # idempotent -- which is the invariant override-refine exists to hold.
    joined_category = obj.category()
    if _is_chain_built(obj):
        # A chain-built parent already *is* its category, so the class is the
        # joined category's ``parent_class`` and nothing of the chain is
        # hoisted.  What is hoisted is the implementation shims: a
        # subcategory declares an obligation abstract, and in category order
        # that declaration precedes the supercategory that computes it, so a
        # participant would answer ``NotImplementedError`` for a name it can
        # compute.  The shims carry the concrete members only.
        _reclass_chain_built(obj, joined_category)
        obj.__dict__.pop("element_class", None)
        obj.__dict__.pop("_abstract_element_class", None)
    else:
        _rebuild_parent_class(obj, joined_category)

        # An element-bearing parent manufactures elements; homsets manufacture
        # morphisms (their ``ParentMethods.__call__`` refines each one) and
        # standalone category objects manufacture neither.
        if isinstance(obj, Parent) and not _is_homset(obj):
            _rebuild_element_class(obj, joined_category)
    _assert_preamble_obligations_are_met(obj, target_category)
    _assert_certifying_predicates_hold(obj, target_category)
    return obj

def hook_post_init(
    cls: type[SageObject],
    category: "Category",
    *,
    predicate: Callable[[SageObject], bool] | None = None,
    before: Callable[[SageObject], None] | None = None,
    after: Callable[[SageObject], None] | None = None,
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
        # Looked up dynamically: the initializer to preserve is whichever one
        # ``cls`` resolves today, its own or an inherited one.
        original_init = next(
            candidate.__dict__["__init__"]
            for candidate in cls.__mro__
            if "__init__" in candidate.__dict__
        )
        _ORIGINAL_INIT[cls] = original_init

        def _init(
            self: "SageObject",
            *args: ElementConstructorInput,
            **kwargs: ElementConstructorInput,
        ) -> None:
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

        setattr(cls, "__init__", _init)  # intentional post-init registration

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
