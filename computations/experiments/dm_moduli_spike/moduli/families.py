r"""Families over a base scheme."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..categories.base import AffineScheme
    from ..curves.pointed import SmoothPointedCurve, StablePointedCurve
    from .instances import ModuliStack


class FamiliesOver:
    r"""Groupoid of families over `S` for a moduli stack fiber."""

    __slots__ = ("_stack", "_base")

    def __init__(self, stack: ModuliStack, base: AffineScheme) -> None:
        self._stack = stack
        self._base = base

    def stack(self) -> ModuliStack:
        return self._stack

    def over_scheme(self) -> AffineScheme:
        return self._base

    def an_element(self) -> FamilyOver:
        return FamilyOver(self._stack, self._base)


class FamilyOver:
    r"""A single family `\pi : \mathcal C \to S` in the moduli problem."""

    __slots__ = ("_stack", "_base")

    def __init__(self, stack: ModuliStack, base: AffineScheme) -> None:
        self._stack = stack
        self._base = base

    def over_scheme(self) -> AffineScheme:
        return self._base

    def fiber(self, point: object) -> SmoothPointedCurve | StablePointedCurve:
        from ..curves.pointed import SmoothPointedCurve, StablePointedCurve

        g = self._stack.genus()
        n = self._stack.number_of_markings()
        base = self.over_scheme()
        if self._stack.is_proper():
            return StablePointedCurve.from_ambient(g, n, base_scheme=base)
        return SmoothPointedCurve.from_ambient(g, n, base_scheme=base)

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
