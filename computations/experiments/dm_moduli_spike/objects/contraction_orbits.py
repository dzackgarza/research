r"""Contraction orbits at the stable-graph isomorphism-class level."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contractions import StableGraphContraction
    from .graph_types import StableGraphType


class ContractionOrbit:
    r"""One edge-orbit of elementary contractions between isomorphism classes."""

    __slots__ = ("_source", "_target", "_representative", "_orbit_size")

    def __init__(
        self,
        source: StableGraphType,
        target: StableGraphType,
        representative: StableGraphContraction,
        orbit_size: int,
    ) -> None:
        self._source = source
        self._target = target
        self._representative = representative
        self._orbit_size = int(orbit_size)

    def source(self) -> StableGraphType:
        return self._source

    def target(self) -> StableGraphType:
        return self._target

    def representative(self) -> StableGraphContraction:
        return self._representative

    def orbit_size(self) -> int:
        return self._orbit_size

    def __repr__(self) -> str:
        return f"ContractionOrbit({self._source!r} -> {self._target!r}, orbit size {self._orbit_size})"
