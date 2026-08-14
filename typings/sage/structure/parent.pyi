# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import MutableMapping
from typing import Any, Generic, TypeVar, overload

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.rings import Rings
from sage.categories.sets_cat import Sets
from sage.structure.element import Element, RingElement

# Sage permits arbitrary Python values at its conversion and membership
# boundaries.  Keep that dynamic input localized here; algebraic outputs stay
# parameterized by the mathematical element type of the parent.
type ElementConstructorInput = Any
type MembershipInput = ElementConstructorInput

# Unbounded: Sage does not constrain _element_constructor_ to Element —
# facade and set-theoretic parents return tuples or other parents' elements.
_E = TypeVar("_E", default=Element, covariant=True)
_CodomainElement = TypeVar("_CodomainElement")
_SourceElement = TypeVar("_SourceElement")

class Parent(Generic[_E]):
    # Generic over the element type: Parent.__call__ (conversion into the
    # parent) returns the parent's own element class, so subclasses bind the
    # parameter instead of re-declaring __call__ at the use site. The runtime
    # class is a cython extension type (not subscriptable), so binding uses a
    # TYPE_CHECKING-conditional base alias.
    #
    # The category framework injects element_class at parent construction
    # (a class-level attribute on the dynamic parent class); constructing an
    # element is element_class(parent, *args). Bound to the element
    # parameter, so element construction returns the parent's element type.
    element_class: type[_E]
    def __init__(
        self,
        base: Parent[ElementConstructorInput] | None = ...,
        *,
        category: Category | None = ...,
        names: str | tuple[str, ...] | None = ...,
        normalize: bool = ...,
        facade: Parent[ElementConstructorInput]
        | tuple[Parent[ElementConstructorInput], ...]
        | bool
        | None = ...,
    ) -> None: ...
    # NOTE: facade_for is NOT stubbed here: it is injected by the Facade
    # axiom's ParentMethods, not defined on the base Parent class.
    def category(self) -> Category: ...
    # The base ring, when the parent has one: a bare set has none and Sage
    # answers None there (verified on Set([1, 2])), so the honest type is
    # ring-or-None; algebraic parents narrow it in their own declarations.
    def base_ring(self) -> Rings.ParentMethods[RingElement] | None: ...
    # Generator-naming surface (inherited from CategoryObject): the preparser
    # protocol behind ``L.<e,f> = ...``.
    def variable_names(self) -> tuple[str, ...]: ...
    def _first_ngens(self, n: int) -> tuple[_E, ...]: ...
    def inject_variables(
        self,
        scope: MutableMapping[str, _E] | None = ...,
        verbose: bool = ...,
    ) -> None: ...
    # Element construction: the conversion map into this parent.
    def __call__(
        self,
        x: ElementConstructorInput = ...,
        *args: ElementConstructorInput,
        **kwds: ElementConstructorInput,
    ) -> _E: ...
    # The homspace out of this parent: Hom(self, codomain, category)
    # (sage/structure/parent.pyx).
    # category_object.pyx:631 — Hom(self, codomain, category=None).
    # category_object.pyx:625 — the ``base=`` this parent was built with.
    def base(self) -> Parent[ElementConstructorInput] | None: ...
    @overload
    def Hom(
        self,
        codomain: Parent[_CodomainElement],
        category: Sets,
    ) -> Homset[
        SetMorphism[_E, _CodomainElement],
        _E,
        _CodomainElement,
    ]: ...
    @overload
    def Hom(
        self,
        codomain: Parent[_CodomainElement],
        category: Category | None = ...,
    ) -> Homset[Map[_E, _CodomainElement], _E, _CodomainElement]: ...
    # A coercion into this parent is a morphism, or none when no coercion
    # exists.
    def coerce_map_from(
        self,
        source: Parent[_SourceElement],
    ) -> Morphism[_SourceElement, _E] | None: ...
    def has_coerce_map_from(self, source: Parent[_SourceElement]) -> bool: ...
    def __contains__(self, x: MembershipInput) -> bool: ...
