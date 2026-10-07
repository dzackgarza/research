"""Small reusable helpers shared by the active preamble."""

from collections.abc import Callable, Iterable, Sequence
from functools import reduce
from operator import add, mul
from typing import overload

__all__ = ["lmap", "lzip", "to_var_names", "zipsum"]


def lmap[T, U](function: Callable[[T], U], values: Iterable[T]) -> list[U]:
    return list(map(function, values))


@overload
def lzip[A](first: Iterable[A], /) -> list[tuple[A]]: ...
@overload
def lzip[A, B](first: Iterable[A], second: Iterable[B], /) -> list[tuple[A, B]]: ...
@overload
def lzip[A, B, C](
    first: Iterable[A], second: Iterable[B], third: Iterable[C], /
) -> list[tuple[A, B, C]]: ...
def lzip[T](*iterables: Iterable[T]) -> Sequence[tuple[T, ...]]:
    r"""The tuples of corresponding entries, one component per iterable.

    The overloads keep each component's own type, as ``zip`` does in
    typeshed; one shared type for every component would widen mixed
    iterables to their join.
    """
    return list(zip(*iterables))


def to_var_names(names: str) -> list[str]:
    return [name.replace(" ", "").strip() for name in names.split(",")]


def zipsum[C, G, T](
    coefficients: Iterable[C],
    elements: Iterable[G],
    zero: T,
    *,
    term: Callable[[C, G], T] = mul,
) -> T:
    """Return the sum of pairwise terms from two equally sized iterables."""
    summands = (
        term(coefficient, element)
        for coefficient, element in zip(coefficients, elements, strict=True)
    )
    return reduce(add, summands, zero)
