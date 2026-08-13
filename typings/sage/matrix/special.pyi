# Repo-scoped stubs; see lexicon/README.md.
from typing import Any

from sage.matrix.matrix0 import Matrix as _ConcreteMatrix
from sage.structure.element import Matrix

# special.py:2222,2249-2255 / matrix0.pyx:54 — block construction returns
# a concrete matrix through block_matrix().
def block_diagonal_matrix(*blocks: Any, **kwds: Any) -> _ConcreteMatrix: ...

def identity_matrix(ring: Any, n: Any = ..., sparse: bool = ...) -> Matrix: ...
def column_matrix(*args: Any, **kwds: Any) -> Matrix: ...

# special.py:678,898-905 / matrix0.pyx:54 — diagonal construction returns a
# concrete matrix through matrix().
def diagonal_matrix(ring: Any, entries: Any = ..., sparse: bool = ...) -> _ConcreteMatrix: ...
