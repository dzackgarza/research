r"""The category is the class: ``ParentMethods`` as the implementation class.

Sage builds a whole method MRO out of ``super_categories()`` and then throws
away the one thing that would make those method classes implementation
classes: ``Category._make_named_class`` passes ``prepend_cls_bases=False`` to
:func:`~sage.structure.dynamic_class.dynamic_class`, so the ``ParentMethods``
class itself never enters the MRO -- only a copy of its ``__dict__`` does.  A
copied ``__dict__`` carries no bases, so it cannot carry ``Parent``, so it
cannot carry fields.  That, and nothing else, is why every level of the
preamble needs a hand-written parent class beside its category, and why the
data those categories' methods need has to be installed by a separate step
after construction.

:class:`OwnedCategoryMixin` puts ``ParentMethods`` / ``ElementMethods`` /
``MorphismMethods`` *into the bases* of the named class instead.  Then:

* the named class inherits ``Parent`` (or ``Element``) through the root
  level's ``ParentMethods``, so ``SomeCategory().parent_class`` is directly
  instantiable and its instances hold data;
* zero-argument ``super()`` inside those methods resolves along the category
  graph, so construction threads exactly the way method lookup already
  threads, and a level supplies only the datum it declares;
* every method a mathematician reaches is in the source class it was written
  in, because that class is in the MRO.  Nothing is copied, generated or
  synthesized.

Two measurements fixed this shape:

* ``prepend_cls_bases=True`` -- splicing ``ParentMethods.__bases__`` in while
  still copying its dict -- does not work.  The ``__class__`` cell of every
  method still points at the provider class, which is not in the MRO, so
  zero-argument ``super()`` raises ``TypeError: obj is not an instance or
  subtype of type``.  Since cooperative ``super()`` is the whole mechanism,
  that variant is unusable.
* The root of an owned chain must have Sage's ``Sets()`` among its super
  categories.  ``Parent._init_category_`` re-wraps ``type(self)`` into
  ``dynamic_class(name, (type(self), category.parent_class))`` unless the
  parent is already an instance of ``Sets().parent_class``; under the flip
  those two are the same class, and the re-wrap raises ``TypeError:
  duplicate base class``.  The owned ``Sets`` root already declares Sage's
  ``Sets()``, which is what makes this work.

.. SEEALSO:: :mod:`dzack_research.preamble.refine`, which hoists owned
   ``ParentMethods`` ahead of a *Sage-native* concrete class.  That remains
   the route for parents the preamble adopts rather than constructs; a parent
   built through an owned chain already has its methods in the right order
   and needs no rebuild.
"""

from __future__ import annotations

import copyreg
from abc import ABCMeta
from typing import TYPE_CHECKING

from sage.categories.category import Category, CategoryWithParameters
from sage.misc.lazy_attribute import lazy_attribute
from sage.structure.category_object import CategoryObject
from sage.structure.parent import Parent as SageParent
from sage.misc.classcall_metaclass import ClasscallMetaclass
from sage.misc.inherit_comparison import InheritComparisonMetaclass
from sage.structure.dynamic_class import (
    DynamicClasscallMetaclass,
    DynamicInheritComparisonClasscallMetaclass,
    DynamicInheritComparisonMetaclass,
    DynamicMetaclass,
    dynamic_class,
)

if TYPE_CHECKING:
    from typing import Any

    from sage.structure.parent import Parent

    # The construction data one level of an owned chain hands to the levels
    # above it.  Genuinely open: each level consumes the datum it declares and
    # passes the rest on, and the union closes only at the root, in Sage's
    # ``Parent.__init__`` keywords.  Named and aliased exactly once, here, so
    # that every ``**rest`` in every chain says what it carries and no site
    # writes the bare escape.
    type ConstructionData = Any


class _DynamicABCMetaclass(DynamicMetaclass, ABCMeta):
    pass


class _DynamicABCClasscallMetaclass(DynamicClasscallMetaclass, _DynamicABCMetaclass):
    pass


class _DynamicABCInheritComparisonMetaclass(
    DynamicInheritComparisonMetaclass, _DynamicABCMetaclass
):
    pass


class _DynamicABCInheritComparisonClasscallMetaclass(
    DynamicInheritComparisonClasscallMetaclass,
    _DynamicABCClasscallMetaclass,
    _DynamicABCInheritComparisonMetaclass,
):
    pass


for _abc_metaclass in (
    _DynamicABCMetaclass,
    _DynamicABCClasscallMetaclass,
    _DynamicABCInheritComparisonMetaclass,
    _DynamicABCInheritComparisonClasscallMetaclass,
):
    # Pickle dispatches a *class* on its metaclass, and Sage registers its four
    # dynamic metaclasses this way; without the same registration for the
    # crossed ones, pickling a parent_class that carries obligations falls
    # through to a by-name lookup that cannot resolve a dynamic class.
    copyreg.pickle(_abc_metaclass, _abc_metaclass.__reduce__)


def _abc_metaclass_for(bases: tuple[type, ...]) -> type:
    r"""Sage's dynamic metaclass for ``bases``, crossed with :class:`ABCMeta`.

    Enforcement of an obligation is ``ABCMeta`` refusing to instantiate a class
    that still has an unimplemented ``abstractmethod``.  Getting that on a
    ``parent_class`` needs both halves and neither is optional:

    * the provider declares ``metaclass=ABCMeta``, because ``ABCMeta.__new__``
      collects abstract names from the new class's own namespace and from each
      base's ``__abstractmethods__`` -- and a *plain* class has no
      ``__abstractmethods__``, so with the provider merely in the bases nothing
      is collected and nothing is enforced;
    * and the generated class's metaclass must be a subclass of both Sage's
      dynamic metaclass and ``ABCMeta``, or Python refuses the class outright
      with ``TypeError: metaclass conflict``.

    This is why the prior art's ``prepend_cls_bases=False`` was not arbitrary:
    copying the provider's dict put the abstract methods into the namespace,
    which is the other place ``ABCMeta`` looks.  Putting the provider in the
    bases instead is what makes cooperative ``super()`` work, so the collection
    has to come from the provider being an ABC in its own right.

    The four crossings above mirror Sage's own four dynamic metaclasses and,
    critically, **inherit from each other the same way Sage's do**.  Generating
    them independently (one cached ``type(base, ABCMeta)`` per Sage metaclass)
    is wrong and was measured wrong: a class whose bases mix a plain-crossed
    ``parent_class`` with a ``ClasscallMetaclass`` base then has two sibling
    metaclasses and neither dominates, so Python refuses it with ``TypeError:
    metaclass conflict``.  Preserving the lattice is what makes a Classcall
    level compose with an obligation declared further down.
    """
    metaclass: type = _DynamicABCMetaclass
    if any(isinstance(base, ClasscallMetaclass) for base in bases):
        metaclass = _DynamicABCClasscallMetaclass
    if any(isinstance(base, InheritComparisonMetaclass) for base in bases):
        metaclass = (
            _DynamicABCInheritComparisonClasscallMetaclass
            if metaclass is _DynamicABCClasscallMetaclass
            else _DynamicABCInheritComparisonMetaclass
        )
    assert all(issubclass(metaclass, type(base)) for base in bases), (
        f"no crossed metaclass dominates the bases of {bases}"
    )
    return metaclass


class CatConstructionsMixin:
    r"""Carry what ``Cat`` declares a category can do, and nothing else.

    An owned **root** -- a category whose super categories are all Sage's --
    takes this one.  Everything below it inherits the constructions through
    ``subcategory_class`` and needs no declaration of its own.

    **Keep this separate from** :class:`OwnedCategoryMixin`.  The two do
    different jobs.  This one routes ``subcategory_class``, which is a *view*
    on a category, and no category competes for it.  The flip rebuilds
    ``parent_class`` / ``element_class`` / ``morphism_class``, which changes
    what a category's **objects** are.

    Giving a family the flip together makes MRO conflicts appear.  One example
    is ``OwnedCategoryOverBaseRing`` and the categories over it:
    ``TypeError: Cannot create a consistent method resolution order (MRO) for
    bases Modules.parent_class, FreeModules.ParentMethods``.

    A conflict of that kind is the design's own tripwire.  Its cause is a
    non-root methods class that names a base, which states the class graph by
    hand in place of the category graph.  Remove that base.  Do not avoid the
    flip, and do not apply the flip in stages: the migration is one sweep, and
    the conflicts it shows are the sites to repair.
    """

    def _make_named_class(
        self,
        name: str,
        method_provider: str,
        cache: bool = False,
        picklable: bool = True,
    ) -> type:
        if name == "subcategory_class":
            return self._subcategory_class_with_cat_constructions(
                method_provider, cache=cache, picklable=picklable
            )
        return super()._make_named_class(  # type: ignore[misc]
            name, method_provider, cache=cache, picklable=picklable
        )


    def _subcategory_class_with_cat_constructions(
        self,
        method_provider: str,
        cache: bool = False,
        picklable: bool = True,
    ) -> type:
        r"""``subcategory_class``, carrying what ``Cat`` declares a category can do.

        This is how the constructions reach a category, and it has to be this
        rather than the Cat-object attribute fallback, because **most owned
        categories are not objects the preamble builds**.  Measured on the real
        tree: of nine representative owned categories exactly one -- the bare
        root -- is a ``Parent``.  Every axiom category, every functorial
        construction and every join is a class Sage constructs, including
        ``Lattices.U.category()``, which is a ``JoinCategory``.  No change to
        the preamble's own class declarations reaches those, because
        ``Category.join`` builds them inside Sage.

        ``subcategory_class`` does reach all of them: Sage's
        ``Category.__init__`` sets a category's own class to
        ``dynamic_class(name, (cls, self.subcategory_class))``, and builds that
        from the super categories' ``subcategory_class``es.  So tying it once,
        at the owned root, propagates down the whole owned tree and through
        joins -- no per-category declaration, and nothing written on a Sage
        class.  ``Cat.ParentMethods`` enters as a **base**, never as a copied
        dict, so each construction keeps its source where it is declared.

        Cat is excluded: it is not an object of itself, so its own
        subcategories must not be handed the constructions.
        """
        category = self
        assert isinstance(category, Category), (
            "OwnedCategoryMixin is mixed into a Category"
        )
        cat_constructions = _cat_constructions()
        provider = getattr(category, method_provider, None)
        if provider is cat_constructions:
            return super()._make_named_class(  # type: ignore[misc]
                "subcategory_class", method_provider,
                cache=cache, picklable=picklable,
            )
        bases = tuple(
            super_category.subcategory_class
            for super_category in category._super_categories_for_classes
        )
        carried = any(cat_constructions in base.mro() for base in bases)
        if provider is not None:
            bases = (provider,) + bases
        if not carried:
            # Last, never first.  A base that already carries the
            # constructions has them at the end of its own linearization, so
            # asking for them first here contradicts that base's order and C3
            # refuses the class: ``TypeError: Cannot create a consistent method
            # resolution order (MRO) for bases Rngs.subcategory_class,
            # Cat.ParentMethods, ...``.  Most general goes last, and nothing
            # here competes for a name anyway.
            bases = bases + (cat_constructions,)
        declaring_class = type(category)
        if declaring_class.__name__.endswith("_with_category"):
            declaring_class = declaring_class.__base__
        doccls = provider or declaring_class
        return dynamic_class(
            f"{declaring_class.__name__}.subcategory_class",
            bases,
            None,
            doccls=doccls,
            reduction=(getattr, (category, "subcategory_class")) if picklable else None,
            cache=cache,
        )


class OwnedCategoryMixin(CatConstructionsMixin):
    r"""Tie a category to its implementation classes.

    A mixin rather than a ``Category`` subclass because
    ``CategoryWithParameters._make_named_class`` -- inherited by
    ``Category_over_base``, ``JoinCategory``, ``CategoryWithAxiom`` and the
    functorial-construction categories such as ``CartesianProductsCategory``
    -- calls ``Category._make_named_class`` *by name*, so an override placed
    further down the ``Category`` hierarchy is bypassed.  Placed first in the
    bases it handles the tied names itself and delegates the rest along the
    MRO, which composes with every one of those.

    Intercepting ``CategoryWithParameters`` costs something, and the decision
    is to pay it back rather than accept it.  That override exists to share one
    named class between categories differing only in a parameter -- its own
    doctest asserts ``Algebras(GF(7)).parent_class is
    Algebras(GF(5)).parent_class`` -- and taking the tied names before it runs
    would silently make that ``False``.  Sharing is still right under the flip,
    because the flip puts construction on the class but never the parameter:
    two such categories have the same provider and the same super-category
    named classes, so literally the same bases, and each object holds its own
    parameter as instance data.  So the cache is honoured below, and measured
    to track Sage: same key shares, different key does not, and a shared class
    still enforces its obligations.
    """

    _TIED_NAMED_CLASSES = frozenset(
        ("parent_class", "element_class", "morphism_class")
    )

    def _make_named_class(
        self,
        name: str,
        method_provider: str,
        cache: bool = False,
        picklable: bool = True,
    ) -> type:
        if name not in self._TIED_NAMED_CLASSES:
            return super()._make_named_class(  # type: ignore[misc]
                name, method_provider, cache=cache, picklable=picklable
            )
        assert cache is False, (
            "the three tied names are built by lazy attributes on the category "
            "(Category.parent_class / element_class / morphism_class), none of "
            "which passes a cache argument; only subcategory_class does, and "
            "that is delegated above.  If a caller ever passes one, it needs a "
            "cache here rather than being silently dropped."
        )
        category = self
        assert isinstance(category, Category), (
            "OwnedCategoryMixin is mixed into a Category"
        )
        declaring_class = type(category)
        if declaring_class.__name__.endswith("_with_category"):
            declaring_class = declaring_class.__base__
        bases = tuple(
            getattr(super_category, name)
            for super_category in category._super_categories_for_classes
        )
        provider = getattr(category, method_provider, None)
        if provider is not None:
            bases = (provider,) + bases
        if len(bases) > 1 and object in bases:
            # A super category with no methods class of its own contributes
            # ``object``.  Left in place beside a real base it is a base that
            # every other base already derives from, and C3 refuses the class:
            # ``TypeError: Cannot create a consistent method resolution order
            # (MRO) for bases object, Modules.parent_class,
            # FreeModules.ParentMethods``.
            bases = tuple(base for base in bases if base is not object)
        doccls = provider or declaring_class
        class_name = f"{declaring_class.__name__}.{name}"
        reduction = (getattr, (category, name)) if picklable else None

        # Sharing the named class between categories that differ only in a
        # parameter is ``CategoryWithParameters``' whole reason to exist, and
        # its own doctest asserts ``Algebras(GF(7)).parent_class is
        # Algebras(GF(5)).parent_class``.  Intercepting the tied names ahead of
        # that override would drop it, so the cache is honoured here instead.
        # It stays sound under the flip because the parameter is never on the
        # class: two such categories have the same ``ParentMethods`` and the
        # same super-category named classes, hence literally the same bases,
        # and each object carries its own parameter as instance data.
        key: tuple[object, ...] | None = None
        if isinstance(category, CategoryWithParameters):
            key = (declaring_class, name, category._make_named_class_key(name))
            shared = category._make_named_class_cache.get(key)
            if shared is not None:
                return shared

        if not any(isinstance(base, ABCMeta) for base in bases):
            result = dynamic_class(
                class_name, bases, None, doccls=doccls,
                reduction=reduction, cache=cache,
            )
        else:
            # A level declared obligations, so this class carries them.  Built
            # by hand because :func:`dynamic_class` takes no metaclass, so the
            # crossed dynamic/ABCMeta one cannot be requested from it; this
            # mirrors ``dynamic_class_internal`` in
            # ``sage/structure/dynamic_class.py`` and reproduces exactly its
            # ``_reduction`` / ``_doccls`` / ``__doc__`` / ``__module__``
            # bookkeeping.  Two things there are deliberately not mirrored: its
            # ``weak_cached_function`` cache, which the assertion above shows is
            # never asked for on this path, and its ``__slots__`` suppression,
            # which cannot fire because a provider is a plain Python class and
            # so always contributes a ``__dictoffset__``.
            result = _abc_metaclass_for(bases)(
                class_name,
                bases,
                {
                    "_reduction": reduction,
                    "_doccls": (doccls,),
                    "__doc__": doccls.__doc__,
                    "__module__": doccls.__module__,
                },
            )

        if key is not None:
            if key[2] != category._make_named_class_key(name):
                # The parameter's category was refined while we built, so the
                # key we would store is stale.  Sage's own override handles
                # this the same way: discard and recompute.
                return self._make_named_class(
                    name, method_provider, cache=cache, picklable=picklable
                )
            category._make_named_class_cache[key] = result
        return result


def object_of(category: Category, **data: ConstructionData) -> Parent:
    r"""The object of ``category`` built from the data its levels declare.

    The instantiable class is ``category.parent_class``; this is the one line
    that spells that, so a construction's public name stays one thin function
    with the signature its callers already write.

    A free function rather than a method on :class:`OwnedCategoryMixin`
    because the category an object is built in is routinely a
    ``JoinCategory`` -- ``Sets().Finite().CartesianProducts()`` already is --
    and a join is Sage's class, which the preamble consumes and does not
    extend.  The join's ``parent_class`` has the owned levels among its bases,
    so it constructs exactly the same way.

    The base ring is not supplied here.  A level that sits over a ring states
    its own ``base`` when it calls ``super().__init__``, the way the module
    homset does, because a level may name a base its category does not -- and
    injecting one here would arrive twice at the levels that already do.
    """
    return category.parent_class(category=category, **data)


def _cat() -> Category:
    r"""``Cat()``, resolved late: the constructions it declares import this module."""
    from dzack_research.preamble.categories.abstract_categories.cat import Cat

    return Cat()


def _cat_constructions() -> type:
    r"""``Cat.ParentMethods``: what a category can do as an object of Cat."""
    from dzack_research.preamble.categories.abstract_categories.cat import Cat

    return Cat.ParentMethods


class OwnedParent:
    r"""Base of the root ``ParentMethods`` of an owned chain: elements come
    from the category.

    Sage's :meth:`Parent.element_class` composes the parent's own ``Element``
    attribute with the category's ``element_class``, and returns
    ``NotImplemented`` when the parent declares no ``Element``.  A chain-built
    parent declares none: the category's ``ElementMethods`` *is* the element
    implementation class, for exactly the reason ``ParentMethods`` is the
    parent one.  This says so.

    Reaches only objects built through the chain.  An *adopted* Sage parent
    keeps its own ``Element`` -- ``refine`` does not hoist a methods class that
    declares ``Parent`` (see ``refine._IMPLEMENTATION_BASES``), so this never
    enters such a parent's MRO and cannot shadow it.
    """

    @lazy_attribute
    def element_class(self) -> type:
        return self.category().element_class


class OwnedCategoryObject:
    r"""A Sage category that is additionally an **object of** :math:`\mathbf{Cat}`.

    Sage's ``Category`` is not a ``CategoryObject``: ``Category.category()``
    answers ``Objects()`` and there is no attribute fallback, so the only way to
    give every category the constructions declared in ``Cat.ParentMethods`` was
    to write them onto Sage's own ``Category`` class.  Being a ``Parent`` whose
    ``_category`` is ``Cat()`` replaces that: ``CategoryObject.__getattr__``
    falls through to ``self._category.parent_class``, so a category reaches
    ``Cat``'s constructions the ordinary Sage way and nothing is installed on a
    class the preamble does not own.

    **What this currently buys, stated so it is not re-derived.**  It buys no
    computation.  Two justifications for it have been measured and falsified:
    the \(\mathbf{Cat}\) constructions do *not* reach a category this way --
    they arrive through ``subcategory_class``, which is what covers the joins
    and axiom categories most owned categories actually are -- and ``Hom(C, D)``
    does *not* route to the functor space by parenthood either; that follows
    the domain being an owned category, again through ``subcategory_class``.
    It is kept because a category **is** an object of \(\mathbf{Cat}\), which
    is what ``Cat.super_categories() == [Objects()]`` says, and the code should
    say it too: foundational structure is not discarded for having no callers.
    Its one near-use so far: had Sage's ``Morphism`` been available as a base
    for functors, it would have *required* the boundary categories to be
    parents -- see ``abstract_categories/functors.sage``, which explains why
    that route is closed.

    The base order below every subclass must keep is
    ``OwnedCategoryMixin, OwnedCategoryObject, <Sage category base>, Parent``:

    * the flip first, so its ``_make_named_class`` wins;
    * ``OwnedCategoryObject`` before the Sage base, because that is the one
      semantic change -- ``category()`` answers ``Cat()`` rather than
      ``Objects()``;
    * the Sage base before ``Parent``, or ``__contains__``, ``__call__``,
      ``base``/``base_ring`` and ``element_class`` resolve to parent
      element-construction logic, which is wrong for a category;
    * ``Parent`` last, present only so the object really is one.
    """

    def _init_cat_object(self) -> None:
        r"""Initialize the parent shell without a second class rewrite.

        Not ``Parent.__init__(category=Cat())``: that runs
        ``Parent._init_category_``, which rewrites ``__class__`` into a dynamic
        class -- and Sage's ``Category.__init__`` already made one
        ``*_with_category``.  Two rewrites give ``Sets_with_category_with_category``,
        and ``CategoryWithAxiom.__classget__`` strips exactly one layer before
        checking that a nested axiom class belongs to its base category, so
        ``Sets().Finite()`` fails.  ``CategoryObject._init_category_`` records
        the category and rewrites nothing, which is all that is wanted here.
        """
        SageParent.__init__(self, category=None)
        CategoryObject._init_category_(self, _cat())

    def category(self) -> Category:
        return _cat()


