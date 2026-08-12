# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Callable
from typing import TypeVar

_F = TypeVar("_F", bound=Callable[..., object])

class AbstractMethod:
    r"""The descriptor Sage's ``@abstract_method`` leaves on a class.

    A category states an obligation by binding one of these; an object whose
    lookup still resolves to it has not implemented the obligation.  The
    obligations sweep reads exactly that, so the descriptor is part of the
    checked surface.
    """
    _f: Callable[..., object]
    def __call__(self, *args: object, **kwds: object) -> object: ...

def abstract_method(f: _F | None = ..., optional: bool = ...) -> _F | AbstractMethod: ...

def abstract_methods_of_class(cls: type) -> dict[str, list[str]]: ...
