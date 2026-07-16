r"""Owned Protocols for Sage surfaces used by this spike.

Firewall: product code types against these Protocols instead of ``object`` /
``Any`` at Sage permutation-group and ring call sites.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator, Sequence
from typing import Protocol, runtime_checkable


@runtime_checkable
class SageRing(Protocol):
    def has_coerce_map_from(self, other: object) -> bool: ...

    def __call__(self, elt: object) -> object: ...

    def one(self) -> object: ...


@runtime_checkable
class SagePermutationGroup(Protocol):
    def order(self) -> object: ...

    def orbits(self) -> Sequence[Iterable[object]]: ...


@runtime_checkable
class SagePermutation(Protocol):
    def __call__(self, x: object) -> object: ...


@runtime_checkable
class FiniteLabelSet(Protocol):
    def __iter__(self) -> Iterator[object]: ...

    def list(self) -> Sequence[object]: ...
