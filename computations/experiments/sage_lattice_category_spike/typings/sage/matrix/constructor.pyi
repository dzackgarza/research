# Repo-scoped stubs; see lexicon/README.md. The matrix constructors are
# heavily overloaded dispatch factories in Sage; the stub keeps the argument
# surface permissive and the return type exact.
from typing import Any

from sage.rings.integer import Integer
from sage.structure.element import Matrix
from sage.structure.parent import Parent

def matrix(*args: Any, **kwds: Any) -> Matrix: ...
def identity_matrix(ring: Parent | int | Integer, n: int | Integer = ...) -> Matrix: ...
def column_matrix(*args: Any, **kwds: Any) -> Matrix: ...
