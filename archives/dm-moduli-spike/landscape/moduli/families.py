r"""Families over a base scheme."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...categories.base import AffineScheme
    from ..curves.pointed import SmoothPointedCurve, StablePointedCurve
    from .stack import DeligneMumfordModuliStackOver


class FamiliesOver:
    r"""Groupoid of families over `S` for a base-changed moduli stack."""

    __slots__ = ("_stack_over",)

    def __init__(self, stack_over: DeligneMumfordModuliStackOver) -> None:
        self._stack_over = stack_over

    def stack(self) -> DeligneMumfordModuliStackOver:
        return self._stack_over

    def over_scheme(self) -> AffineScheme:
        return self._stack_over.over_scheme()

    def an_element(self) -> FamilyOver:
        return FamilyOver(self._stack_over)


class FamilyOver:
    r"""A single family `\pi : \mathcal C \to S` in the moduli problem."""

    __slots__ = ("_stack_over",)

    def __init__(self, stack_over: DeligneMumfordModuliStackOver) -> None:
        self._stack_over = stack_over

    def over_scheme(self) -> AffineScheme:
        return self._stack_over.over_scheme()

    def fiber(self, point: object) -> SmoothPointedCurve | StablePointedCurve:
        from ..curves.pointed import SmoothPointedCurve, StablePointedCurve

        g = self._stack_over.genus()
        n = self._stack_over.number_of_markings()
        base = self.over_scheme()
        if self._stack_over.is_proper():
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
