r"""Foundational nouns: scalars, tuples of invariants, set vocabulary.

Declaration-only (INVENTORY.md II.1). Every alias binds a semantic
mathematical name to the real implementation class, through the stub tree in
``typings/sage/`` for type checking and to the live class at runtime.
"""

from __future__ import annotations

import collections.abc
from collections.abc import Sequence
from typing import TYPE_CHECKING, Literal, NewType

from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.structure.element import Matrix

if TYPE_CHECKING:
    from sage.structure.element import ExactMatrix
from sage.symbolic.expression import Expression as SymbolicExpression

__all__ = [
    "CartanType",
    "ExactScalar",
    "GramMatrix",
    "Integer",
    "OrderedSet",
    "Rational",
    "RealNumber",
    "Set",
    "SignaturePair",
    "SymbolicExpression",
]

type ExactScalar = Integer | Rational
"""An exact Sage scalar. Never a float; ``RealNumber`` is display-only."""

type SignaturePair = tuple[int, int]
"""Sylvester pair (p, n); p + n < rank exactly for degenerate lattices."""

type CartanType = tuple[Literal["A", "D", "E"], int]
"""Simply-laced Cartan datum; B/C/F/G matrices are not symmetric, hence not Gram."""

Set = collections.abc.Set
"""Unordered mathematical set (membership + iteration)."""

type OrderedSet[T] = Sequence[T]
"""A set with a distinguished linear order (a basis, a generator tuple).
Uniqueness of members is the producing constructor's contract, not the type's."""

if TYPE_CHECKING:
    _GramBase = ExactMatrix
else:
    _GramBase = Matrix
GramMatrix = NewType("GramMatrix", _GramBase)

"""Parse-witness: a square symmetric exact matrix, produced only by the
grammar's Gram codec (INVENTORY.md Part III.5). "Gram matrix" is real
mathematical vocabulary; note there is deliberately NO "MorphismMatrix"
counterpart — the matrix expressing a morphism in bases is an ordinary
``Matrix``, and the validated-morphism witness is the morphism object
itself."""
