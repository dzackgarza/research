r"""Enrichment: derived forwarding, and classes bound to categories.

Enrichment is two different things, and each gets one mechanism here.

*Chosen* enrichment -- many structures sit on one underlying object (many
forms on $\mathbb{Z}^2$, many $G$-actions on $\mathbb{Z}^n$), so the
forgetful functor is not injective on objects and the enriched thing has to
be a distinct parent holding the pair.  Such a level declares exactly one
thing, :func:`forgets_to`: the category it enriches, and the accessor that
produces the underlying object.  The forwarding for every name that
category declares and this level does not answer itself is generated from
the category's own declared surface.  Nothing is listed by hand, nothing is
added when the lower category grows a method, and a name this level
genuinely answers differently is written here and simply wins.

*Determined* enrichment -- the object determines its own added structure (a
free algebra *is* the free module on $\operatorname{Mon}(S)$; a subobject is
the object together with its own inclusion), so the enriched thing is the
same object with more categories, and the class hierarchy can be derived.
:func:`BoundTo` resolves a class statement's bases from the category's own
``super_categories()`` through :func:`realizes`, so the class graph and the
category graph cannot drift, and construction threads by cooperative
``super().__init__``.

Both mechanisms work on all three of Sage's surfaces -- ``ParentMethods``,
``ElementMethods``, ``MorphismMethods`` -- because Sage declares three and
:mod:`dzack_research.preamble.refine` already rebuilds three.  Homsets are
parents, so they thread on the parent surface.

Generation happens when the declaration is read, never at attribute lookup:
a generated method is an ordinary function in the class ``__dict__``, so
``dir``, :mod:`inspect` and :func:`refine` all see the whole surface.  A
``__getattr__`` would answer the same calls and show an empty class.

EXAMPLES::

    sage: from dzack_research.preamble.enrichment import declared_surface
    sage: from dzack_research.preamble.categories.modules.pure.modules import Modules
    sage: "scalar_multiple" in declared_surface(Modules(ZZ), "parent")
    True
"""

from __future__ import annotations

import functools
from collections.abc import Callable
from typing import TYPE_CHECKING, Concatenate, Literal

from sage.categories.category import Category
from sage.misc.abstract_method import AbstractMethod
from sage.structure.sage_object import SageObject

if TYPE_CHECKING:
    # Declared by the stub tree, so it names a union rather than a runtime
    # object: every value a Sage method hands back.
    from sage.structure.sage_object import SageCoercionAtom

__all__ = [
    "BoundTo",
    "Surface",
    "declared_surface",
    "forgets_to",
    "forwarding_mixin",
    "realization_of",
    "realizes",
]

type Surface = Literal["parent", "element", "morphism"]
"""Which of Sage's three method surfaces a declaration speaks about."""

type MethodDeclaration = Callable[..., SageCoercionAtom] | AbstractMethod
"""A class-body entry declaring a method: a function, or the abstract
declaration standing in for one a category requires of its members."""

_METHODS_CLASS: dict[Surface, str] = {
    "parent": "ParentMethods",
    "element": "ElementMethods",
    "morphism": "MorphismMethods",
}

# A surface is the set of names *this project* declares an object must
# answer, so the declarers that count are the ones outside Sage.  This is a
# different question from the one ``refine`` asks with its preamble-package
# test: there, ownership decides whose methods may outrank a concrete class,
# which is a permission and belongs to the preamble alone.  Here it decides
# which names the enriching level is on the hook for, and a name declared by
# any non-Sage category above the underlying object is one of them.
_SAGE_PACKAGE = "sage."


def _is_sage(declarer: type) -> bool:
    return declarer.__module__.startswith(_SAGE_PACKAGE)


def _declaring_class(category: Category) -> type[Category]:
    r"""Return the class a category was declared with.

    Sage gives every category instance a dynamic ``<Name>_with_category``
    class built over its own class and its subcategory class, so the class
    written in the source -- the one a binding is keyed on -- is the first
    class of the MRO that is not that dynamic one.
    """
    for candidate in type(category).__mro__:
        if not candidate.__name__.endswith("_with_category"):
            return candidate
    assert False, f"{category} has no declaring class"  # noqa: B011


def _surface_classes(source: Category | type, surface: Surface) -> tuple[type, ...]:
    r"""Return the classes whose bodies declare ``source``'s ``surface``.

    A category declares through the nested methods classes of its non-Sage
    super-categories, most specific first.  A concrete class declares
    through the non-Sage classes of its own MRO -- which is how a surface
    this repository still keeps on a class rather than on a category, the
    morphism surface above all, can be enriched over before it moves.
    """
    if isinstance(source, Category):
        attribute = _METHODS_CLASS[surface]
        nested = (
            getattr(type(category), attribute, None)
            for category in source.all_super_categories(proper=False)
            if not _is_sage(type(category))
        )
        return tuple(methods for methods in nested if methods is not None)
    return tuple(declarer for declarer in source.__mro__ if not _is_sage(declarer))


def _declarations(
    source: Category | type,
    surface: Surface,
) -> dict[str, MethodDeclaration]:
    r"""Return ``source``'s declared methods on ``surface``, by name.

    Most specific declarer wins, which is the resolution order the object
    itself would use.  Dunders are excluded: ``__eq__`` and ``__hash__``
    on an enriched level answer about the *pair*, so relaying them would
    identify objects the enrichment exists to keep apart.
    """
    declared: dict[str, MethodDeclaration] = {}
    for methods in _surface_classes(source, surface):
        for name, declaration in vars(methods).items():
            if name.startswith("__"):
                continue
            if not (callable(declaration) or isinstance(declaration, AbstractMethod)):
                continue
            declared.setdefault(name, declaration)
    return declared


def declared_surface(source: Category | type, surface: Surface) -> frozenset[str]:
    r"""Return the names ``source`` declares on ``surface``.

    This is what a chosen enrichment over ``source`` is on the hook for:
    every one of these names is answered by the enriched level itself or by
    forwarding, and there is no third possibility.
    """
    return frozenset(_declarations(source, surface))


def _relay[**P, A](
    accessor: str,
    declared: Callable[Concatenate[SageObject, P], A],
) -> Callable[Concatenate[SageObject, P], A]:
    r"""Return the method that answers ``declared`` by forgetting first.

    The relay keeps the declared signature and ``__qualname__`` --
    :func:`functools.wraps` copies the annotations, the name and the
    documentation -- because the answer *is* the lower level's answer, and a
    reader who follows the qualified name lands where it is computed.
    """
    name = declared.__name__

    @functools.wraps(declared)
    def forwarded(enriched: SageObject, *args: P.args, **kwargs: P.kwargs) -> A:
        underlying = getattr(enriched, accessor)()
        answer: A = getattr(underlying, name)(*args, **kwargs)
        return answer

    forwarded.__doc__ = (
        f"{declared.__doc__ or ''}\n\n"
        f"Generated: answered by ``{accessor}()``, where the notion lives."
    )
    return forwarded


def _generated_methods(
    source: Category | type,
    surface: Surface,
    accessor: str,
    answered_here: frozenset[str],
) -> dict[str, Callable[..., SageCoercionAtom]]:
    generated: dict[str, Callable[..., SageCoercionAtom]] = {}
    for name, declaration in _declarations(source, surface).items():
        if name in answered_here:
            continue
        function = declaration._f if isinstance(declaration, AbstractMethod) else declaration
        assert callable(function), (
            f"{name} is declared on {source} as {declaration!r}, which names no "
            "function to relay"
        )
        generated[name] = _relay(accessor, function)
    return generated


def forwarding_mixin(
    source: Category | type,
    surface: Surface,
    accessor: str,
    *,
    answered_here: frozenset[str] = frozenset(),
) -> type:
    r"""Return a class answering ``source``'s ``surface`` by ``accessor``.

    :func:`forgets_to` is written in terms of this, and so is any enrichment
    over a surface a concrete class still holds instead of a category --
    ``ModuleMorphism``, today.

    ``answered_here`` names what the enriching level computes itself; those
    names are left out so the level's own method is the only one.
    """
    generated = _generated_methods(source, surface, accessor, answered_here)
    return type(f"ForwardingTo{_source_name(source)}", (), generated)


def _source_name(source: Category | type) -> str:
    if isinstance(source, Category):
        return _declaring_class(source).__name__
    return source.__name__


def forgets_to(
    enriched: Category | type[Category],
    *,
    through: str,
) -> Callable[[type[Category]], type[Category]]:
    r"""Declare the forgetful map of a chosen enrichment, and generate from it.

    ``enriched`` is the category this one enriches; ``through`` is the
    accessor producing the underlying object, on every surface.  Applied to
    a category class, this fills its three nested methods classes with a
    relay for each name ``enriched`` declares and this category's own body
    does not, so::

        @forgets_to(FramedModules, through="forget_form")
        class FormModules(OwnedCategoryOverBaseRing):
            def super_categories(self) -> list:
                return [FramedModules(self.base_ring())]

    is the whole declaration, and no ``self.forget_form().<same name>()``
    body is ever written.

    Each level declares its own map: ``FormModules`` forgets to
    ``FramedModules``, and the refinements below it -- free, finitely
    generated -- forget to the matching module refinements, which is where
    ``rank`` and the torsion predicates are declared.  A level that declared
    only the root's map would relay only the root's names.

    A parameterized ``enriched`` may be given as its class; the surface's
    *names* do not depend on the parameter, and the relay reads the real
    object at call time.
    """
    enriched_category = enriched if isinstance(enriched, Category) else enriched()

    def bind(category: type[Category]) -> type[Category]:
        for surface, attribute in _METHODS_CLASS.items():
            # Read through this class's own body, never an inherited one: a
            # category class that inherits ``ParentMethods`` would otherwise
            # have its relays written into its base's nested class, where
            # every sibling category would pick them up.
            methods = vars(category).get(attribute)
            if methods is None:
                methods = type(attribute, (), {})
                setattr(category, attribute, methods)
            answered_here = frozenset(vars(methods))
            generated = _generated_methods(
                enriched_category, surface, through, answered_here
            )
            for name, relay in generated.items():
                setattr(methods, name, relay)
        return category

    return bind


_REALIZATIONS: dict[Surface, dict[type[Category], type[SageObject]]] = {
    "parent": {},
    "element": {},
    "morphism": {},
}


def realizes(
    category: Category | type[Category],
    surface: Surface = "parent",
) -> Callable[[type[SageObject]], type[SageObject]]:
    r"""Bind a concrete class to ``category`` on ``surface``.

    Both directions stay readable without opening an implementation: given
    the category, its class is :func:`realization_of`; given the class, its
    category is the argument here, on the line above the class statement.
    """
    category_class = (
        _declaring_class(category) if isinstance(category, Category) else category
    )

    def bind(realization: type[SageObject]) -> type[SageObject]:
        bound = _REALIZATIONS[surface]
        existing = bound.get(category_class)
        assert existing is None or existing is realization, (
            f"{category_class.__name__} is already realized on the {surface} "
            f"surface by {existing!r}"
        )
        bound[category_class] = realization
        return realization

    return bind


def realization_of(
    category: Category | type[Category],
    surface: Surface = "parent",
) -> type[SageObject]:
    r"""Return the class bound to ``category`` on ``surface``."""
    category_class = (
        _declaring_class(category) if isinstance(category, Category) else category
    )
    realization = _REALIZATIONS[surface].get(category_class)
    assert realization is not None, (
        f"no {surface} class is bound to {category_class.__name__}; declare one "
        "with @realizes"
    )
    return realization


class BoundTo:
    r"""Bases derived from a category's ``super_categories()``.

    Written in a class statement's base list, where PEP 560's
    ``__mro_entries__`` replaces it with the classes bound to the
    category's super-categories::

        @realizes(NewLeaf)
        class NewLeafParent(BoundTo(NewLeaf)):
            def __init__(self, my_datum: "Datum", **rest: ElementConstructorInput) -> None:
                self._my_datum = my_datum
                super().__init__(**rest)

    The author names one category and writes no base class, so the MRO is a
    function of the category graph.  Construction threads by cooperative
    ``super().__init__``: each level consumes the data it owns and passes
    the rest up, and the one class whose derived bases are empty -- the root
    -- is the one that names Sage's non-cooperative ``Parent.__init__``.

    A super-category with no bound class contributes nothing, which is what
    lets a chain end at Sage's categories.
    """

    def __init__(
        self,
        category: Category | type[Category],
        surface: Surface = "parent",
    ) -> None:
        self._category = category if isinstance(category, Category) else category()
        self._surface = surface

    def __mro_entries__(
        self,
        _original_bases: tuple[type, ...],
    ) -> tuple[type[SageObject], ...]:
        # PEP 560 hands over the whole written base list; the derived bases
        # are a function of the category alone, so it is not read.
        bound = _REALIZATIONS[self._surface]
        derived: list[type[SageObject]] = []
        for super_category in self._category.super_categories():
            realization = bound.get(_declaring_class(super_category))
            if realization is None or realization in derived:
                continue
            derived.append(realization)
        return tuple(derived)

    def __repr__(self) -> str:
        return f"BoundTo({self._category}, {self._surface!r})"
