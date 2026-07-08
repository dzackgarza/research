# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Callable
from typing import Any, TypeVar

_F = TypeVar("_F", bound=Callable[..., Any])

def abstract_method(f: _F) -> _F: ...
