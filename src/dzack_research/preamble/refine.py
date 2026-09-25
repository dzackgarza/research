"""Owned category refinement for parents already owned by the preamble.

Sage's ``_refine_category_`` joins categories but leaves the concrete class
before category methods in the MRO.  For an owned parent, this helper rebuilds
its dispatch class so owned category methods win.  Adoption of Sage parents is
not performed here: free modules, groups, rings and other adopted objects enter
through owned facades that hold the Sage parent as a private engine.
"""

from collections.abc import Iterable, Iterator
from contextlib import contextmanager

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function
from sage.structure.category_object import CategoryObject
from sage.structure.dynamic_class import dynamic_class
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

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
    for provider in providers:
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


def _assert_certifying_predicates_hold(obj: SageObject, category: Category) -> None:
    """Require every owned certified property before category admission.

    A category states the property that admits an object as the sequence of
    owned operations that reads it off, left to right: ``"is_even"`` asks the
    lattice, ``"module_rank.is_finite"`` asks the lattice for its rank and the
    rank for its finiteness.  The last operation answers ``True`` or the
    object does not belong.
    """
    for candidate_category in category.all_super_categories(proper=False):
        category_type = type(candidate_category)
        if not category_type.__module__.startswith(_PREAMBLE_PACKAGE):
            continue
        statement = getattr(category_type, "_certifying_predicate", None)
        if statement is None:
            continue
        answer = obj
        for operation in statement.split("."):
            answer = getattr(answer, operation)()
        assert answer is True, (
            f"refining {obj} into {candidate_category} requires "
            f"{statement}() to hold"
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
    _assert_certifying_predicates_hold(obj, target)
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
