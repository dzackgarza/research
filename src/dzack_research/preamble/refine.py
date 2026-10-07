"""Owned category refinement for parents already owned by the preamble.

Sage's ``_refine_category_`` joins categories but leaves the concrete class
before category methods in the MRO.  For an owned parent, this helper rebuilds
its dispatch class so owned category methods win; an abstract contract of the
category is fulfilled by the implementation the object already has.  Adoption of Sage parents is
not performed here: free modules, groups, rings and other adopted objects enter
through owned facades that hold the Sage parent as a private engine.
"""

import inspect
from collections.abc import Iterable, Iterator
from contextlib import contextmanager

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.misc.abstract_method import AbstractMethod
from sage.misc.cachefunc import cached_function
from sage.structure.category_object import CategoryObject
from sage.structure.dynamic_class import dynamic_class
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.mor_foundation import (
    OwnedMor,
)

_PREAMBLE_PACKAGE = __name__.rpartition(".")[0] + "."


# A methods class naming one of these among its bases is an implementation
# class, not a mixin: it is the class an owned category is tied to.
_IMPLEMENTATION_BASES = (Parent, Element, Morphism)


@cached_function
def _owned_mixins(category: Category, attr: str) -> tuple[type, ...]:
    """Return owned nested method classes in category order.

    A function of the category alone, which is a unique representation, so it
    is computed once per category rather than once per object built in it.
    """
    providers: list[type] = []
    for cat in category.all_super_categories(proper=False):
        for category_type in type(cat).__mro__:
            if not category_type.__module__.startswith(_PREAMBLE_PACKAGE):
                continue
            provider = vars(category_type).get(attr)
            if not isinstance(provider, type) or provider in providers:
                continue
            if issubclass(provider, _IMPLEMENTATION_BASES):
                # The root of an owned construction chain declares its methods
                # class over the host runtime base, so that class *is* the
                # implementation rather than a mixin over one.  An adopted Sage
                # parent already has its own, and hoisting this one would
                # shadow it.
                continue
            providers.append(provider)
    return tuple(providers)


def _supply_abstract_contracts(new_class: type, mixins: tuple[type, ...], inherited: type) -> None:
    """Let an implementation the object already has fulfil each abstract contract it reaches.

    The rebuilt class puts the owned methods of the category before the
    class they refine, so a category operation wins over a class method of
    the same name.  An ``abstract_method`` is not an operation: it states that
    a participant of the category supplies one (``STY-48``).  When the
    winner for a name is such a contract and ``inherited`` already resolves
    that name to a preamble implementation, that implementation is the
    participant's answer, and it is aliased onto ``new_class`` ahead of the
    contract.  An implementation defined outside the preamble, by a Sage host
    class, does not fulfil an owned contract.
    """
    contracts = {
        name
        for provider in mixins
        for name, value in vars(provider).items()
        if not name.startswith("_") and isinstance(value, AbstractMethod)
    }
    for name in contracts:
        if not isinstance(inspect.getattr_static(new_class, name), AbstractMethod):
            continue
        definer = next(
            (klass for klass in inherited.__mro__ if name in vars(klass)),
            None,
        )
        if definer is None or not definer.__module__.startswith(_PREAMBLE_PACKAGE):
            continue
        supplied = vars(definer)[name]
        if isinstance(supplied, AbstractMethod):
            continue
        setattr(new_class, name, supplied)


def _rebuild_parent_class(parent: Parent, category: Category) -> None:
    providers = _owned_mixins(category, "ParentMethods")
    if not providers:
        return
    inherited = type(parent).__dict__.get("_preamble_inherited", type(parent))
    carried = frozenset(inherited.__mro__)
    mixins = tuple(provider for provider in providers if provider is not object and provider not in carried)
    if not mixins:
        return

    # ``inherited`` already contains the method providers reached by earlier
    # construction steps.  A later refinement prepends only newly reached
    # providers, which can otherwise let a *supercategory* method shadow the
    # more specific operation already selected by the final category.  Keep
    # the final category order authoritative for colliding public operations.
    # The alias is the original provider's descriptor, not a second
    # implementation.  Private construction hooks stay on their provider so
    # ``run_construction_hooks`` still executes each level exactly once.
    new_names = {
        name
        for provider in mixins
        for name in vars(provider)
        if not name.startswith("_")
    }
    preferred = {}
    seen = set()
    for provider in reversed(providers):
        for name, value in vars(provider).items():
            if name.startswith("_") or name in seen:
                continue
            seen.add(name)
            if provider in carried and name in new_names:
                preferred[name] = value

    concrete = type(parent).__dict__.get("_preamble_concrete", inherited)
    new_class = dynamic_class(
        f"Owned{concrete.__name__}",
        (*mixins, inherited),
        doccls=concrete,
    )
    for name, value in preferred.items():
        setattr(new_class, name, value)
    _supply_abstract_contracts(new_class, mixins, inherited)
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
    element_class = dynamic_class(
        f"{type(parent).__name__}.element_class",
        (*mixins, native),
        doccls=native,
    )
    _supply_abstract_contracts(element_class, mixins, native)
    parent.element_class = element_class


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
    _supply_abstract_contracts(new_class, mixins, inherited)
    new_class._preamble_concrete = concrete
    new_class._preamble_inherited = inherited
    morphism.__class__ = new_class


def check_certifying_predicates(obj: SageObject, category: Category, held: Category) -> None:
    """Raise ``ValueError`` unless ``obj`` has each property ``category`` certifies beyond ``held``.

    A category states the property that admits an object as the sequence of
    public operations that reads it off, left to right: ``"is_even"`` asks the
    lattice, ``"module_rank.is_finite"`` asks the lattice for its rank and the
    rank for its finiteness.  The last operation answers ``True`` or the
    object does not belong.  A category ``held`` already contains is not asked
    again.
    """
    for certified in category.all_super_categories(proper=False):
        category_type = type(certified)
        if not category_type.__module__.startswith(_PREAMBLE_PACKAGE):
            continue
        statement = getattr(category_type, "_certifying_predicate", None)
        if statement is None or held.is_subcategory(certified):
            continue
        answer = obj
        for operation in statement.split("."):
            answer = getattr(answer, operation)()
        if answer is not True:
            raise ValueError(
                f"{obj} is not an object of {certified}: {statement}() answers {answer}"
            )


def realize_owned_category[SageObjectT: SageObject](obj: SageObjectT) -> SageObjectT:
    r"""Realize the owned methods of the category already chosen at construction.

    This is runtime plumbing, not mathematical refinement.  In particular it
    never changes ``obj.category()`` and therefore cannot be used to add
    construction data or category membership after instantiation.
    """
    category = obj.category()
    if isinstance(obj, Morphism):
        _rebuild_morphism_class(obj, category)
        return obj
    if isinstance(obj, Parent):
        _rebuild_parent_class(obj, category)
        if not isinstance(obj, OwnedMor):
            _rebuild_element_class(obj, category)
    return obj


@contextmanager
def construction_scope(obj: SageObject) -> Iterator[set[type]]:
    r"""Share Sage's construction-hook traversal with nested refinements.

    ``Parent.__init__`` calls the hooks in its initial MRO itself.  Reserve
    those providers while it runs; refinements add their new providers to the
    same traversal.  The set lasts only for the active construction call.
    """
    reached = obj.__dict__.get("_preamble_construction_hooks")
    if reached is not None:
        yield reached
        return
    reached = set(type(obj).__mro__)
    obj._preamble_construction_hooks = reached
    try:
        yield reached
    finally:
        del obj._preamble_construction_hooks


def run_construction_hooks(obj: SageObject, reached: set[type]) -> None:
    r"""Run the construction step of every level ``obj`` has newly reached.

    A category level states what it establishes on its objects in
    ``__init_extra__``, and the host runs those hooks in one pass over the MRO
    from ``Parent.__init__`` (``sage/structure/parent.pyx``).  Neither
    ``CategoryObject._refine_category_`` nor ``Parent._refine_category_`` runs
    them.  ``reached`` is shared by the enclosing construction and any
    refinement a hook requests.  Enter a provider before invoking it so a
    nested refinement preserves the enclosing traversal.
    """
    for provider in type(obj).__mro__:
        if provider in reached:
            continue
        reached.add(provider)
        if "__init_extra__" in vars(provider):
            provider.__init_extra__(obj)


def refine[SageObjectT: SageObject](
    obj: SageObjectT,
    category: Category | Iterable[Category],
) -> SageObjectT:
    r"""Add a verified property/axiom category to an already constructed object."""
    from dzack_research.preamble.owned_category import owned_category_join

    target = category if isinstance(category, Category) else owned_category_join(tuple(category))
    check_certifying_predicates(obj, target, obj.category())
    if isinstance(obj, Morphism):
        # A morphism's mathematical membership is determined by its Mor
        # parent.  There is no independent Sage category slot to mutate here;
        # the target only supplies the owned morphism-method surface selected
        # by that already-constructed Mor theory.
        _rebuild_morphism_class(obj, target)
        return obj
    with construction_scope(obj) as reached:
        current = obj.category()
        if current is not target:
            CategoryObject._init_category_(obj, owned_category_join((current, target)))
        realized = realize_owned_category(obj)
        run_construction_hooks(obj, reached)
        return realized
