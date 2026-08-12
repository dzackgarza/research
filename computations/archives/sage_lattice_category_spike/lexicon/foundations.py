r"""Foundational nouns: scalars, tuples of invariants, set vocabulary.

Declaration-only (INVENTORY.md II.1). Every alias binds a semantic
mathematical name to the real implementation class, through the stub tree in
``typings/sage/`` for type checking and to the live class at runtime.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, NewType

from sage.categories.sets_cat import Sets as SageSets
from sage.rings.integer import Integer
from sage.rings.qqbar import AlgebraicReal
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber as RealApproximation
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.element import Element, Matrix
from sage.symbolic.expression import Expression as SymbolicExpression

__all__ = [
    "RealApproximation",
    "RealNumber",
    "CartanType",
    "GramMatrix",
    "Integer",
    "OrderedSet",
    "Rational",
    "Set",
    "SignaturePair",
    "SymbolicExpression",
]

type SignaturePair = tuple[Integer, Integer]
"""Sylvester pair (p, n); p + n < rank exactly for degenerate lattices.
Counts are ``Integer``: a Python ``int`` is a different object that happens to
print the same, and the repo bans the fork."""

type CartanType = tuple[Literal["A", "D", "E"], Integer]
"""Simply-laced Cartan datum; B/C/F/G matrices are not symmetric, hence not Gram."""

Set = SageSets.ParentMethods
"""An unordered mathematical set: a parent placed in ``Sets()``.

Typed category-first, like ``Ring`` (INVENTORY.md II.2).  Not
``collections.abc.Set``, which a ``frozenset`` satisfies and a Sage set parent
need not: that protocol describes a Python container, and a set here is an
object of a category."""

if TYPE_CHECKING:

    class _OwnedOrderedSet[E: Element](TotallyOrderedFiniteSet[E]):
        r"""The parent ``finite_ordered_set`` returns: a
        ``TotallyOrderedFiniteSet`` refined into the owned
        ``Sets().Finite().TotallyOrdered()``.

        Declared here because the refinement is invisible to the checker.
        ``refine`` installs the category's ``ParentMethods`` *ahead* of the
        concrete class, so the owned placement is what answers; ``Finite``
        implies ``Countable``, whose ``ParentMethods`` own the two operations
        below.  Same technique, same reason, as ``UnderlyingSet``'s
        ``TYPE_CHECKING`` surface block."""

        def index(self, element: E) -> int: ...
        def __getitem__(self, n: int) -> E: ...

    type OrderedSet[E: Element] = _OwnedOrderedSet[E]
else:
    # At runtime the noun is the concrete class; the owned surface arrives by
    # refinement on the instance, not by a distinct Python class.
    type OrderedSet[E] = TotallyOrderedFiniteSet[E]
"""A set carrying a distinguished linear order: the owned
``Sets().Finite().TotallyOrdered()`` parent, and nothing else.

The retired alias was ``Sequence``, whose own docstring conceded that
uniqueness of members "is the producing constructor's contract, not the
type's" -- an admission that it named a list, not a set.  A later revision
kept it as a union arm "for the input boundary"; that arm is gone too.  A
``Sequence`` is not a mathematical object, and a value typed by this noun
must answer ``cardinality``, ``index`` and ``X[n]``, which a list does not.
Code that holds a literal enumeration calls ``finite_ordered_set`` -- the one
constructor that transports an enumeration into an order -- and passes the
set."""

GramMatrix = NewType("GramMatrix", Matrix)
"""Parse-witness: the array $[b(e_i,e_j)]$ of a form $M\\otimes M\\to W$,
square and symmetric, produced only by the grammar's Gram codec
(INVENTORY.md Part III.5).

It represents NO morphism. Its companion ``MorphismMatrix`` does, and the
two are categorically different: that the correlation $c:L\\to L^\\vee$ is
represented by a matrix coinciding with the Gram matrix in dual generating
sets is a coincidence of coordinates, not an identity of objects."""

type RealNumber = AlgebraicReal | SymbolicExpression
"""An element of $\\mathbb R$, held exactly: $\\sqrt2$ in ``AA``, $\\pi$ in the
symbolic ring.  This is the noun signatures use.  Exact real arithmetic is
available, so accepting and returning exact reals is the default and nothing
about it needs an adjective."""

RealApproximation = RealApproximation
"""An mpfr approximation *of* a real number.

Distinct from ``RealNumber`` and never a substitute for it.  Approximation is
an extraction performed late, at a display or plot boundary, on a value that
was computed exactly -- so this name appears at that boundary and nowhere in
between.  Binding $\\mathbb R$ itself to mpfr would say every real in the
repo is approximate, which would make $\\sqrt2$ unsayable."""
