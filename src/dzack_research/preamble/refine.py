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
from sage.structure.category_object import CategoryObject
from sage.categories.morphism import Morphism
from sage.structure.dynamic_class import dynamic_class
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

_PREAMBLE_PACKAGE = __name__.rpartition(".")[0] + "."


# A methods class naming one of these among its bases is an implementation
# class, not a mixin: it is the class an owned category is tied to.
_IMPLEMENTATION_BASES = (Parent, Element, Morphism)


def _owned_mixins(category: Category, attr: str) -> tuple[type, ...]:
    """Return owned nested method classes in category order."""
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


def realize_owned_category(obj: SageObject):
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


def refine(obj: SageObject, category: Category | Iterable[Category]):
    r"""Add a verified property/axiom category to an already constructed object."""
    target = category if isinstance(category, Category) else Category.join(tuple(category))
    _assert_certifying_predicates_hold(obj, target)
    if isinstance(obj, Morphism):
        # A morphism's mathematical membership is determined by its Hom
        # parent.  There is no independent Sage category slot to mutate here;
        # the target only supplies the owned morphism-method surface selected
        # by that already-constructed Hom theory.
        _rebuild_morphism_class(obj, target)
        return obj
    with construction_scope(obj) as reached:
        CategoryObject._refine_category_(obj, target)
        realized = realize_owned_category(obj)
        run_construction_hooks(obj, reached)
        return realized
