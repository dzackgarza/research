# Repo-scoped stubs; see lexicon/README.md.
from typing import Any

from sage.rings.integer import Integer

def ceil(x: Any) -> Integer: ...
def floor(x: Any) -> Integer: ...
def sqrt(x: Any) -> Any: ...

# The absolute-value symbolic function (an instance of Function_abs), the
# same kind of object as exp/sin/cos in sage.functions.log / .trig.
class Function_abs:
    def __call__(self, x: object) -> Any: ...

abs_symbolic: Function_abs
