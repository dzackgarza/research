r"""Curves and pointed-curve families (Sage-backed when smooth)."""

from __future__ import annotations

from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import AffineScheme, spec
from ..categories.curves import Curves, PointedCurves, SmoothCurves, StablePointedCurves
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
        return self._genus if not self._nodal else self._genus  # combinatorial default

    def is_smooth(self) -> bool:
        return not self._nodal and "Smooth" in self._axioms

    def is_nodal(self) -> bool:
        return self._nodal

    def sage_curve(self) -> object:
        if self._sage_curve is None:
            raise ValueError("no Sage curve model attached")
        return self._sage_curve

    def singular_locus(self) -> object:
        curve = self.sage_curve()
        if hasattr(curve, "singular_points"):
            return curve.singular_points()
        return ()

    def irreducible_components(self) -> tuple[object, ...]:
        return (self,)

    def normalization(self) -> object:
        curve = self.sage_curve()
        if hasattr(curve, "normalization"):
            return curve.normalization()
        return curve

    def dual_graph(self) -> object:
        from ..objects.graph_types import StableGraphTypes

        return StableGraphTypes(self._genus, 0).smooth().canonical_representative()


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
    ) -> None:
        Curve.__init__(self, base, genus=genus, sage_curve=sage_curve, nodal=nodal)
        self._markings = markings
        self._marking_set = marking_set
        self._graph = graph

    def marking_set(self) -> tuple[object, ...]:
        return self._marking_set

    def marked_point(self, i: object) -> object:
        idx = self._marking_set.index(i)
        return self._markings[idx]

    def markings(self) -> tuple[object, ...]:
        return self._markings

    def dual_graph(self) -> object:
        if self._graph is not None:
            return self._graph
        from ..objects.graph_types import StableGraphTypes

        return StableGraphTypes(self._genus, len(self._marking_set)).smooth().canonical_representative()


class StablePointedCurve(PointedCurve):
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
        raise NotImplementedError

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
        self._marking_set = marking_set
        self._stable = stable

    def marking_sections(self) -> tuple[object, ...]:
        return self._sections

    def fiber(self, s: object) -> PointedCurve:
        from .pointed import SmoothPointedCurve, StablePointedCurve

        if self._stable:
            return StablePointedCurve.from_ambient(self._genus, len(self._marking_set), base_scheme=self._base)
        return SmoothPointedCurve.from_ambient(self._genus, len(self._marking_set), base_scheme=self._base)

    def dual_graph_specialization(self) -> object:
        from ..objects.gamma import StableGraphCategory

        g, n = self._genus, len(self._marking_set)
        Gamma = StableGraphCategory(g, n)
        special = max(Gamma.objects(), key=lambda x: x.num_edges())
        generic = min(Gamma.objects(), key=lambda x: x.num_edges())
        morphs = list(Gamma.hom(special, generic))
        if not morphs:
            return Gamma.identity(generic)
        return morphs[0]


class StablePointedCurveFamily(PointedCurveFamily):
    def __init__(self, base: AffineScheme, total_space: object, sections: tuple[object, ...], *, genus: int, marking_set: tuple[object, ...]) -> None:
        PointedCurveFamily.__init__(
            self, base, total_space, sections, genus=genus, marking_set=marking_set, stable=True
        )
