# Repo-scoped stubs; see lexicon/README.md. SR is the symbolic ring parent:
# converting an exact scalar into SR is the typed way to move a computation
# into exact symbolic arithmetic (repo policy bans floats in domain values).
from sage.structure.parent import Parent
from sage.symbolic.expression import Expression

class SymbolicRing(Parent):
    def __call__(self, x: object = ..., *args: object, **kwds: object) -> Expression: ...

SR: SymbolicRing
