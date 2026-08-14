# Repo-scoped stubs; see lexicon/README.md.
from typing import Any, Generic, TypeVar

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.categories.rings import Rings
from sage.structure.element import Element

# Unbounded: Sage does not constrain _element_constructor_ to Element —
# facade and set-theoretic parents return tuples or other parents' elements.
_E = TypeVar("_E", default=Element, covariant=True)
_CodomainElement = TypeVar("_CodomainElement")

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
        base: object = ...,
        *,
        category: object = ...,
        names: object = ...,
        normalize: bool = ...,
        facade: object = ...,
    ) -> None: ...
    # NOTE: facade_for is NOT stubbed here: it is injected by the Facade
    # axiom's ParentMethods, not defined on the base Parent class.
    def category(self) -> Category: ...
    # The base ring, when the parent has one: a bare set has none and Sage
    # answers None there (verified on Set([1, 2])), so the honest type is
    # ring-or-None; algebraic parents narrow it in their own declarations.
    def base_ring(self) -> Rings.ParentMethods | None: ...
    # Generator-naming surface (inherited from CategoryObject): the preparser
    # protocol behind ``L.<e,f> = ...``.
    def variable_names(self) -> tuple[str, ...]: ...
    def _first_ngens(self, n: int) -> tuple[Any, ...]: ...
    def inject_variables(self, scope: object = ..., verbose: bool = ...) -> None: ...
    # Element construction: the conversion map into this parent.
    def __call__(self, x: object = ..., *args: object, **kwds: object) -> _E: ...
    # The homspace out of this parent: Hom(self, codomain, category)
    # (sage/structure/parent.pyx). Typed Any because the concrete homset
    # class depends on the resolved category.
    # category_object.pyx:631 — Hom(self, codomain, category=None).
    # category_object.pyx:625 — the ``base=`` this parent was built with.
    def base(self) -> Parent: ...
    def Hom(
        self,
        codomain: Parent[_CodomainElement],
        category: Category | None = ...,
    ) -> Homset[Element, _E, _CodomainElement]: ...
    # A coercion into this parent is a morphism, or none when no coercion
    # exists.
    def coerce_map_from(self, S: object) -> Morphism | None: ...
    def has_coerce_map_from(self, S: object) -> bool: ...
    def __contains__(self, x: object) -> bool: ...
