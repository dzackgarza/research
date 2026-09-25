r"""Shared narrowing helpers for boundary values entering typed APIs."""

from __future__ import annotations

from collections.abc import Iterable


def as_int(value: object) -> int:
    r"""Require a value convertible to ``int`` (Python int or Sage Integer)."""
    from sage.rings.integer import Integer

    if isinstance(value, bool):
        raise TypeError(f"refusing bool as int; value={value!r}; owned boundary=as_int")
    if isinstance(value, int):
        return value
    if isinstance(value, Integer):
        return int(value)
    raise TypeError(f"expected int or Integer; found {type(value)!r}; value={value!r}; owned boundary=as_int")


def as_frozenset(value: object) -> frozenset[object]:
    if isinstance(value, frozenset):
        return value
    if isinstance(value, (set, list, tuple)):
        return frozenset(value)
    raise TypeError(f"expected set-like; found {type(value)!r}; value={value!r}; owned boundary=as_frozenset")


def as_iterable(value: object) -> Iterable[object]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Iterable):
        raise TypeError(f"expected non-string iterable; found {type(value)!r}; owned boundary=as_iterable")
    return value
