r"""Moduli problems represented by Deligne--Mumford stacks."""

from __future__ import annotations


class ModuliProblem:
    r"""Base class for moduli problems `[\pi : C \to S]`."""

    __slots__ = ("_g", "_n", "_name")

    def __init__(self, g: int, n: int, name: str) -> None:
        self._g = int(g)
        self._n = int(n)
        self._name = name

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f"{self._name}({self._g}, {self._n})"


class SmoothPointedCurves(ModuliProblem):
    r"""Families of smooth proper connected `n`-pointed genus-`g` curves."""

    def __init__(self, g: int, n: int) -> None:
        super().__init__(g, n, "SmoothPointedCurves")


class StablePointedCurves(ModuliProblem):
    r"""Families of stable pointed curves; defines the Deligne--Mumford compactification."""

    def __init__(self, g: int, n: int) -> None:
        super().__init__(g, n, "StablePointedCurves")
