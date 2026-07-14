r"""Curves and pointed-curve families (Sage-backed when smooth)."""

from __future__ import annotations

from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import AffineScheme
from ..geometry.stacks import StackMorphism


class Curve(UniqueRepresentation):
    def __init__(
        self,
        base: AffineScheme,
        *,
        genus: int,
        sage_curve: object | None = None,
        nodal: bool = False,
        axioms: frozenset[str] | None = None,
    ) -> None:
        self._base = base
        self._genus = int(genus)
        self._sage_curve = sage_curve
        self._nodal = nodal
        self._axioms = frozenset(axioms or ({"Nodal"} if nodal else {"Smooth"}))

    def base_scheme(self) -> AffineScheme:
        return self._base

    def declared_axioms(self) -> frozenset[str]:
        return self._axioms

    def dimension(self) -> int:
        return 1

    def arithmetic_genus(self) -> int:
        return self._genus

    def geometric_genus(self) -> int:
        return self._genus

    def is_smooth(self) -> bool:
        return not self._nodal and "Smooth" in self._axioms

    def is_nodal(self) -> bool:
        return self._nodal

    def sage_curve(self) -> object:
        if self._sage_curve is None:
            raise ValueError("no Sage curve model attached")
        return self._sage_curve

    def singular_locus(self) -> object:
        if self._sage_curve is None:
            return ()
        curve = self._sage_curve
        if hasattr(curve, "singular_points"):
            return curve.singular_points()
        return ()

    def irreducible_components(self) -> tuple[object, ...]:
        return (self,)

    def normalization(self) -> object:
        if self._sage_curve is None:
            return self
        curve = self._sage_curve
        if hasattr(curve, "normalization"):
            return curve.normalization()
        return curve

    def dual_graph(self) -> object:
        from ..objects.stable_graphs import StableGraphs

        return StableGraphs(self._genus, ()).smooth()


class PointedCurve(Curve):
    def __init__(
        self,
        base: AffineScheme,
        *,
        genus: int,
        markings: tuple[object, ...],
        marking_set: tuple[object, ...],
        sage_curve: object | None = None,
        nodal: bool = False,
        graph: object | None = None,
        stable: bool = False,
    ) -> None:
        Curve.__init__(self, base, genus=genus, sage_curve=sage_curve, nodal=nodal)
        self._markings = markings
        self._marking_set = marking_set
        self._graph = graph
        self._stable = stable

    def marking_set(self) -> tuple[object, ...]:
        return self._marking_set

    def marked_point(self, i: object) -> object:
        idx = self._marking_set.index(i)
        return self._markings[idx]

    def markings(self) -> tuple[object, ...]:
        return self._markings

    def is_stable(self) -> bool:
        return bool(self._stable)

    def dual_graph(self) -> object:
        if self._graph is not None:
            from ..objects.stable_graphs import StableGraphs

            if hasattr(self._graph, "record"):
                return self._graph
            return StableGraphs(self._genus, self._marking_set)(self._graph)
        from ..objects.stable_graphs import StableGraphs

        return StableGraphs(self._genus, self._marking_set).smooth()


class StablePointedCurve(PointedCurve):
    def __init__(self, *args: object, **kwargs: object) -> None:
        kwargs["stable"] = True
        PointedCurve.__init__(self, *args, **kwargs)  # type: ignore[misc]

    def is_stable(self) -> bool:
        return True


class NormalizationMorphism(StackMorphism):
    def __init__(self, source: Curve, target: Curve) -> None:
        StackMorphism.__init__(self, source, target, kind="normalization")


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

    def fiber(self, s: object) -> Curve:
        raise NotImplementedError("unpointed CurveFamily.fiber requires a concrete model")

    def generic_fiber(self) -> Curve:
        return self.fiber("generic")

    def special_fiber(self) -> Curve:
        return self.fiber("special")


class PointedCurveFamily(CurveFamily):
    def __init__(
        self,
        base: AffineScheme,
        total_space: object,
        sections: tuple[object, ...],
        *,
        genus: int,
        marking_set: tuple[object, ...],
        stable: bool = False,
    ) -> None:
        CurveFamily.__init__(self, base, total_space)
        self._sections = sections
        self._genus = int(genus)
        self._marking_set = tuple(marking_set)
        self._stable = stable

    def genus(self) -> int:
        return self._genus

    def marking_set(self) -> tuple[object, ...]:
        return self._marking_set

    def marking_sections(self) -> tuple[object, ...]:
        return self._sections

    def fiber(self, s: object) -> object:
        from .pointed import SmoothPointedCurve, StablePointedCurve as SageStablePointedCurve

        n = len(self._marking_set)
        if self._stable:
            try:
                return SageStablePointedCurve.from_ambient(self._genus, n, base_scheme=self._base)
            except (NotImplementedError, ValueError, AssertionError):
                from ..objects.graph_types import StableGraphTypes

                types = StableGraphTypes(self._genus, n)
                want_nodal = str(s) in {"special", "s", "0"}
                if want_nodal and types.cardinality() > 1:
                    gamma = max(types, key=lambda t: t.num_edges())
                else:
                    gamma = types.smooth()
                return SageStablePointedCurve(
                    self._genus,
                    n,
                    gamma,
                    base_scheme=self._base,
                )
        return SmoothPointedCurve.from_ambient(self._genus, n, base_scheme=self._base)

    def dual_graph_specialization(self) -> object:
        r"""Contraction morphism ``Hom(Γ_special, Γ_generic)`` from family specialization."""
        from sage.categories.homset import Hom

        from ..objects.stable_graphs import StableGraphs

        Cs = self.fiber("special")
        Cg = self.fiber("generic")
        graphs = StableGraphs(self._genus, self._marking_set)
        Gs = graphs(Cs.dual_graph().record() if hasattr(Cs.dual_graph(), "record") else Cs.dual_graph())
        Gg = graphs(Cg.dual_graph().record() if hasattr(Cg.dual_graph(), "record") else Cg.dual_graph())
        if Gs == Gg:
            from ..objects.gamma import StableGraphCategory

            return StableGraphCategory(self._genus, len(self._marking_set)).identity(Gs.record())
        homset = Hom(Gs, Gg)
        morphs = list(homset)
        if not morphs:
            from ..objects.gamma import StableGraphCategory

            return StableGraphCategory(self._genus, len(self._marking_set)).identity(Gg.record())
        morph = morphs[0]
        assert morph.is_contraction()
        return morph


class StablePointedCurveFamily(PointedCurveFamily):
    def __init__(
        self,
        base: AffineScheme,
        total_space: object,
        sections: tuple[object, ...],
        *,
        genus: int,
        marking_set: tuple[object, ...],
    ) -> None:
        PointedCurveFamily.__init__(
            self, base, total_space, sections, genus=genus, marking_set=marking_set, stable=True
        )
