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

from typing import TYPE_CHECKING

from sage.categories.category import Category
from sage.structure.dynamic_class import dynamic_class

if TYPE_CHECKING:
    from sage.structure.parent import Parent


class OwnedCategoryMixin:
    r"""Tie a category to its implementation classes.

    A mixin rather than a ``Category`` subclass because
    ``CategoryWithParameters._make_named_class`` -- inherited by
    ``Category_over_base``, ``JoinCategory``, ``CategoryWithAxiom`` and the
    functorial-construction categories such as ``CartesianProductsCategory``
    -- calls ``Category._make_named_class`` *by name*, so an override placed
    further down the ``Category`` hierarchy is bypassed.  Placed first in the
    bases it handles the tied names itself and delegates the rest along the
    MRO, which composes with every one of those.
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
        return dynamic_class(
            f"{declaring_class.__name__}.{name}",
            bases,
            None,
            doccls=provider or declaring_class,
            reduction=(getattr, (category, name)) if picklable else None,
            cache=cache,
        )


def object_of(category: Category, **data: object) -> Parent:
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
    """
    return category.parent_class(category=category, **data)


class OwnedCategory(OwnedCategoryMixin, Category):
    r"""A category tied to its implementation classes.

    Declaring one is ``super_categories()``, the nested method classes for the
    surfaces this level speaks to, and -- when the level introduces a datum --
    one ``__init__`` that consumes exactly that datum and passes the rest up
    with ``super().__init__(**rest)``.  There is no second place to register
    anything.

    A parameterized or functorial-construction category mixes
    :class:`OwnedCategoryMixin` into its own Sage base in the same way, first
    in the bases.
    """
