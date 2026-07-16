# Repo-scoped stubs; see lexicon/README.md.
from typing import Any, ClassVar, Generic, TypeVar

from sage.structure.element import Element

_E = TypeVar("_E", bound=Element, default=Element, covariant=True)

class Parent(Generic[_E]):
    # Generic over the element type: Parent.__call__ (conversion into the
    # parent) returns the parent's own element class, so subclasses bind the
    # parameter instead of re-declaring __call__ at the use site. The runtime
    # class is a cython extension type (not subscriptable), so binding uses a
    # TYPE_CHECKING-conditional base alias.
    #
    # The category framework injects element_class at parent construction
    # (a class-level attribute on the dynamic parent class).
    element_class: ClassVar[Any]
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
    def category(self) -> Any: ...
    def base_ring(self) -> Any: ...
    # Generator-naming surface (inherited from CategoryObject): the preparser
    # protocol behind ``L.<e,f> = ...``.
    def variable_names(self) -> tuple[str, ...]: ...
    def _first_ngens(self, n: int) -> tuple[Any, ...]: ...
    def inject_variables(self, scope: object = ..., verbose: bool = ...) -> None: ...
    # Element construction: the conversion map into this parent.
    def __call__(self, x: object = ..., *args: object, **kwds: object) -> _E: ...
    def coerce_map_from(self, S: object) -> Any: ...
    def has_coerce_map_from(self, S: object) -> bool: ...
