"""Foundational mathematical nouns."""

from collections.abc import Sequence
from typing import Literal, NewType

from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import Matrix
from sage.symbolic.expression import Expression as SymbolicExpression

from dzack_research.preamble.categories.sets import FiniteOrderedSet
from dzack_research.preamble.rings import RealApproximation, RealNumber

type SignaturePair = tuple[Integer, Integer]
type CartanType = tuple[Literal["A", "D", "E"], Integer]
type LatticeName = str | CartanType
type OrderedSet[E] = FiniteOrderedSet
type MatrixData = Sequence[Sequence[Rational]]

GramMatrix = NewType("GramMatrix", Matrix)

__all__ = [
    "CartanType",
    "GramMatrix",
    "Integer",
    "LatticeName",
    "MatrixData",
    "OrderedSet",
    "Rational",
    "RealApproximation",
    "RealNumber",
    "SignaturePair",
    "SymbolicExpression",
]
