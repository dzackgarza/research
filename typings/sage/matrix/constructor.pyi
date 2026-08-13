# Repo-scoped stubs; see lexicon/README.md. `matrix` is Sage's dispatch
# factory: callable, and carrying the named constructors (matrix.diagonal,
# matrix.identity, ...) that the repo's idiom policy prefers over index-loop
# assembly. The factory's class has no importable runtime name (a cython
# function with attached attributes), so the stub names its shape locally
# (STUB_ONLY in lexicon/verify_against_sage.py).
from collections.abc import Sequence
from typing import Any

from sage.rings.integer import Integer
from sage.structure.element import Matrix as _MatrixClass
from sage.structure.parent import Parent

class _MatrixConstructor:
    def __call__(self, *args: Any, **kwds: Any) -> _MatrixClass: ...
    def diagonal(self, *args: Any, **kwds: Any) -> _MatrixClass: ...
    def identity(self, *args: Any, **kwds: Any) -> _MatrixClass: ...
    def zero(self, *args: Any, **kwds: Any) -> _MatrixClass: ...
    def block(self, *args: Any, **kwds: Any) -> _MatrixClass: ...

matrix: _MatrixConstructor

def identity_matrix(ring: Parent | int | Integer, n: int | Integer = ...) -> _MatrixClass: ...
def column_matrix(*args: Any, **kwds: Any) -> _MatrixClass: ...
def diagonal_matrix(diagonal: Sequence[int | Integer]) -> _MatrixClass: ...

# Upstream binds ``Matrix = matrix`` as the documented capitalized alias.
Matrix: _MatrixConstructor
