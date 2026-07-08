# Repo-scoped stubs; see lexicon/README.md.
from typing import Any, ClassVar

from sage.structure.element import Element

class Parent:
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
    ) -> None: ...
    def category(self) -> Any: ...
    def base_ring(self) -> Any: ...
    # Generator-naming surface (inherited from CategoryObject): the preparser
    # protocol behind ``L.<e,f> = ...``.
    def variable_names(self) -> tuple[str, ...]: ...
    def _first_ngens(self, n: int) -> tuple[Any, ...]: ...
    def inject_variables(self, scope: object = ..., verbose: bool = ...) -> None: ...
    # Element construction: the conversion map into this parent. Owned parents
    # refine the return type to their own element class (TYPE_CHECKING-only —
    # a runtime __call__ on a declaration class would shadow this method).
    def __call__(self, x: object = ..., *args: object, **kwds: object) -> Element: ...
    def coerce_map_from(self, S: object) -> Any: ...
    def has_coerce_map_from(self, S: object) -> bool: ...
