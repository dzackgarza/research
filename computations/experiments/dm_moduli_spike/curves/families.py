r"""Pointed-curve families (smooth vs stable as distinct subclasses)."""

from __future__ import annotations

from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import AffineScheme


class CurveFamily(UniqueRepresentation):
    def __init__(self, base: AffineScheme, total_space: object, structure: object | None = None) -> None:
        self._base = base
        self._total = total_space
        self._structure = structure

    def base(self) -> AffineScheme:
        return self._base

    def total_space(self) -> object:
        return self._total

    def structure_morphism(self) -> object:
        return self._structure

    def fiber(self, s: object) -> object:
        raise NotImplementedError("unpointed CurveFamily.fiber requires a concrete model")

    def generic_fiber(self) -> object:
        return self.fiber("generic")

    def special_fiber(self) -> object:
        return self.fiber("special")


class PointedCurveFamily(CurveFamily):
    r"""Family of pointed curves; stable families are a distinct subclass (§13)."""

    def __init__(
        self,
        base: AffineScheme,
        total_space: object,
        sections: tuple[object, ...],
        *,
        genus: int,
        marking_set: tuple[object, ...],
    ) -> None:
        CurveFamily.__init__(self, base, total_space)
        self._sections = sections
        self._genus = int(genus)
        self._marking_set = tuple(marking_set)

    def genus(self) -> int:
        return self._genus

    def marking_set(self) -> tuple[object, ...]:
        return self._marking_set

    def marking_sections(self) -> tuple[object, ...]:
        return self._sections

    def is_stable(self) -> bool:
        return isinstance(self, StablePointedCurveFamily)

    def fiber(self, s: object) -> object:
        r"""Smooth fiber over a base point (Sage proving-set model when available)."""
        from .pointed import SmoothPointedCurve

        n = len(self._marking_set)
        return SmoothPointedCurve.from_ambient(self._genus, n, base_scheme=self._base)

    def dual_graph_specialization(self) -> object:
        r"""Contraction morphism ``Hom(Γ_special, Γ_generic)`` from family specialization."""
        from sage.categories.homset import Hom

        from ..objects.stable_graphs import StableGraphs

        Cs = self.fiber("special")
        Cg = self.fiber("generic")
        assert hasattr(Cs, "dual_graph") and hasattr(Cg, "dual_graph"), (
            f"family fibers must expose dual_graph(); found {type(Cs)!r}, {type(Cg)!r}; owned boundary=PointedCurveFamily.dual_graph_specialization"
        )
        graphs = StableGraphs(self._genus, self._marking_set)
        Gs = graphs(Cs.dual_graph())
        Gg = graphs(Cg.dual_graph())
        if Gs == Gg:
            from ..objects.gamma import StableGraphCategory

            return StableGraphCategory(self._genus, len(self._marking_set)).identity(Gs)
        morphs = [m for m in Hom(Gs, Gg) if m.is_contraction()]
        if not morphs:
            raise ValueError(f"no contraction in Hom({Gs!r}, {Gg!r}) for family specialization")
        return morphs[0]


class StablePointedCurveFamily(PointedCurveFamily):
    r"""Family of stable pointed curves of type `(g, I)`."""

    def fiber(self, s: object) -> object:
        r"""Fiber over a base point for a stable family.

        ``special`` / ``s`` / ``0`` select a maximally nodal dual-graph fiber when the
        stratification has more than the smooth stratum; ``generic`` (and other tokens)
        select the smooth Sage proving-set model when available, else the combinatorial
        smooth graph.
        """
        from .pointed import StablePointedCurve as SageStablePointedCurve

        n = len(self._marking_set)
        want_nodal = str(s).lower() in {"special", "s", "0"}
        from ..objects.stable_graphs import StableGraphs

        types = StableGraphs(self._genus, n)
        if want_nodal and types.cardinality() > 1:
            gamma = max(types, key=lambda t: int(t.num_edges()))
            return SageStablePointedCurve(
                self._genus,
                n,
                gamma,
                base_scheme=self._base,
            )
        try:
            return SageStablePointedCurve.from_ambient(self._genus, n, base_scheme=self._base)
        except NotImplementedError, ValueError, AssertionError:
            return SageStablePointedCurve(
                self._genus,
                n,
                types.smooth(),
                base_scheme=self._base,
            )
