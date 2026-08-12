# Repo-scoped stubs; see lexicon/README.md. CartanMatrix is a Matrix subclass
# constructed from a Cartan-type datum like ["E", 8].
from typing import Any

from sage.structure.element import Matrix

class CartanMatrix(Matrix):
    def __init__(self, *args: Any, **kwds: Any) -> None: ...
    def __new__(cls, *args: Any, **kwds: Any) -> CartanMatrix: ...
