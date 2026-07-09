# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Sequence
from typing import TypeVar

_T = TypeVar("_T")

def choice(seq: Sequence[_T]) -> _T: ...
