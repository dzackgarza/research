from collections.abc import Callable, Iterable
from typing import Any

def repr_lincomb(
    terms: Iterable[tuple[Any, Any]],
    is_latex: bool = ...,
    scalar_mult: str = ...,
    strip_one: bool = ...,
    repr_monomial: Callable[[Any], str] | None = ...,
    latex_scalar_mult: str | None = ...,
) -> str: ...
