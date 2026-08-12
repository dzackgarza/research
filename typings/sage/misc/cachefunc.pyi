# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Callable
from typing import Any, TypeVar, overload

_F = TypeVar("_F", bound=Callable[..., Any])

def cached_method(f: _F) -> _F: ...

# Both spellings Sage supports: bare ``@cached_function`` and the factory
# form ``@cached_function(key=...)`` (cachefunc.pyx: key normalizes the
# arguments before lookup).
@overload
def cached_function(f: _F) -> _F: ...
@overload
def cached_function(
    *, key: Callable[..., object] | None = ..., do_pickle: bool = ...
) -> Callable[[_F], _F]: ...
