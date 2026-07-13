r"""Families over a base scheme."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..curves.pointed import StablePointedCurve, SmoothPointedCurve
    from .stack import DeligneMumfordModuliStack


class FamiliesOver:
    r"""Groupoid of families over a base `S` for a moduli stack."""

    __slots__ = ("_stack", "_base_scheme")

    def __init__(self, stack: DeligneMumfordModuliStack, base_scheme: object) -> None:
        self._stack = stack
        self._base_scheme = base_scheme

    def stack(self) -> DeligneMumfordModuliStack:
        return self._stack

    def base_scheme(self) -> object:
        return self._base_scheme

    def an_element(self) -> FamilyOver:
        return FamilyOver(self._stack, self._base_scheme)


class FamilyOver:
    r"""A single family `\pi : \mathcal C \to S` in the moduli problem."""

    __slots__ = ("_stack", "_base_scheme")

    def __init__(self, stack: DeligneMumfordModuliStack, base_scheme: object) -> None:
        self._stack = stack
        self._base_scheme = base_scheme

    def fiber(self, point: object) -> SmoothPointedCurve | StablePointedCurve:
        from ..curves.pointed import SmoothPointedCurve, StablePointedCurve

        if self._stack.is_proper():
            return StablePointedCurve(self._stack.genus(), self._stack.number_of_markings())
        return SmoothPointedCurve(self._stack.genus(), self._stack.number_of_markings())

    def specialization(self, generic: object, special: object) -> Specialization:
        return Specialization(generic, special)


class Specialization:
    r"""Specialization of fibers along a trait; induces a dual-graph contraction map."""

    __slots__ = ("_generic", "_special")

    def __init__(self, generic: object, special: object) -> None:
        self._generic = generic
        self._special = special

    def dual_graph_map(self) -> DualGraphContractionMap:
        return DualGraphContractionMap(self._generic, self._special)


class DualGraphContractionMap:
    r"""Placeholder for the contraction morphism on dual graphs induced by specialization."""

    __slots__ = ("_generic", "_special")

    def __init__(self, generic: object, special: object) -> None:
        self._generic = generic
        self._special = special

    def is_contraction(self) -> bool:
        return True
