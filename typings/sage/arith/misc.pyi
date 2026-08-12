# Repo-scoped stubs; see lexicon/README.md.
from typing import Any

from sage.rings.integer import Integer
from sage.structure.factorization import Factorization

# gcd(a, b) on two elements, or gcd(seq) on an iterable of them. Sage returns
# the generator of the ideal they span, an Integer over ZZ.
def gcd(a: Any, b: Any = ..., **kwargs: Any) -> Integer: ...

# Binomial coefficient. Integral for integer arguments, which is the only
# regime this tree uses it in.
def binomial(x: Any, m: Any, **kwds: Any) -> Integer: ...

# Iterable as (prime, exponent) pairs.
def factor(n: int | Integer, **kwds: Any) -> Factorization: ...
def next_prime(n: int | Integer, proof: bool | None = ...) -> Integer: ...
