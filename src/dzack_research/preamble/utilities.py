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


def zipsum(
    coefficients: Iterable[Any],
    generators: Iterable[Any],
    zero: Any,
    *,
    term: Callable[[Any, Any], Any] | None = None,
) -> Any:
    """Sum a zipped pairwise product of coefficients and generators."""
    if term is None:
        term = lambda coefficient, generator: coefficient * generator
    return sum(
        (
            term(coefficient, generator)
            for coefficient, generator in zip(coefficients, generators, strict=True)
        ),
        zero,
    )
