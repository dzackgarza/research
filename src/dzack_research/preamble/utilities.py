"""Reusable helpers for the Sage preamble."""

from collections.abc import Callable, Iterable

from typing import Any

__all__ = ["lmap", "lzip", "to_var_names", "zipsum"]


def lmap[T, U](f: Callable[[T], U], ls: Iterable[T]) -> list[U]:
    """Return ``map(f, ls)`` as a list."""
    return list(map(f, ls))


def lzip(*iterables: Iterable[Any]) -> list[tuple[Any, ...]]:
    """Return ``zip(*iterables)`` as a list."""
    return list(zip(*iterables))


def to_var_names(s: str) -> list[str]:
    """Split a comma-separated list of generator names."""
    return [x.replace(" ", "").strip() for x in s.split(",")]


def zipsum[C, G, T](
    coefficients: Iterable[C],
    elements: Iterable[G],
    zero: T,
    *,
    term: Callable[[C, G], T] | None = None,
) -> T:
    """Sum a zipped pairwise product of coefficients and elements.

    General in all three: the summand type is whatever ``term`` produces and
    ``zero`` is a unit for, which the module cases instantiate but do not
    define.
    """
    if term is None:
        term = lambda coefficient, element: coefficient * element
    return sum(
        (
            term(coefficient, element)
            for coefficient, element in zip(coefficients, elements, strict=True)
        ),
        zero,
    )
