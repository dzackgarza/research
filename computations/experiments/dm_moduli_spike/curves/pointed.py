r"""Sage-backed pointed curves and the dual-graph bridge.

Smooth fibers hold a real :class:`~sage.schemes.curves.curve.Curve_generic`
(plane rational / elliptic / hyperelliptic) with ordered marking scheme points.
Nodal stable fibers still use the owned combinatorial dual graph until geometric
gluing exists; the smooth models remain Sage curves.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.schemes.curves.curve import Curve_generic

    from ..categories.base import AffineScheme
    from ..objects.stable_graphs import StableGraph


def _default_base() -> AffineScheme:
    from sage.rings.rational_field import QQ

    from ..categories.base import spec

    return spec(QQ)


def _curve_generic_type() -> type:
    from sage.schemes.curves.curve import Curve_generic as CurveGenericCls

    assert isinstance(CurveGenericCls, type), f"Curve_generic import must be a type; found {type(CurveGenericCls)!r}"
    return CurveGenericCls


def rational_plane_model(ring: object) -> Curve_generic:
    r"""Smooth plane conic `\simeq \mathbb P^1` over ``ring``: `yz = x^2`."""
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
    from sage.schemes.curves.constructor import Curve as SageCurve

    R = PolynomialRing(ring, names=("x", "y", "z"))
    x, y, z = R.gens()
    return SageCurve(y * z - x**2)


def rational_markings(curve: Curve_generic, n: int) -> tuple[object, ...]:
    r"""``n`` distinct rational points on the standard conic via `[s:t] \mapsto (st:s^2:t^2)`."""
    if n < 0:
        raise ValueError(f"expected nonnegative n; found {n}")
    params: list[tuple[int, int]] = [(1, 0), (0, 1)]
    k = 1
    while len(params) < n:
        params.append((1, k))
        k += 1
    points = []
    for s, t in params[:n]:
        points.append(curve([s * t, s * s, t * t]))
    return tuple(points)


def elliptic_model(ring: object) -> Curve_generic:
    r"""Weierstrass model `y^2 = x^3 - x` over ``ring``."""
    from sage.schemes.elliptic_curves.constructor import EllipticCurve

    return EllipticCurve(ring, [0, 0, 0, -1, 0])


def hyperelliptic_model(ring: object, genus: int = 2) -> Curve_generic:
    r"""Hyperelliptic model of given genus (`y^2 = x^{2g+1} + 1`)."""
    if genus < 2:
        raise ValueError(f"hyperelliptic model requires genus >= 2; found {genus}")
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
    from sage.schemes.hyperelliptic_curves.constructor import HyperellipticCurve

    R = PolynomialRing(ring, names=("x",))
    x = R.gen()
    return HyperellipticCurve(x ** (2 * genus + 1) + 1)


class NormalizationMorphism:
    r"""Normalization morphism `\nu : C^\nu \to C`.

    Formal when the target is nodal with only a dual-graph model; Sage-backed
    when a ``Curve_generic`` normalization is available.
    """

    __slots__ = ("_domain", "_codomain")

    def __init__(self, domain: object, codomain: Curve) -> None:
        self._domain = domain
        self._codomain = codomain

    def domain(self) -> object:
        return self._domain

    def codomain(self) -> Curve:
        return self._codomain

    def source(self) -> object:
        return self._domain

    def target(self) -> Curve:
        return self._codomain

    def __repr__(self) -> str:
        return f"NormalizationMorphism({self._domain!r} → {self._codomain!r})"


class Curve:
    r"""Pure one-dimensional finite-type separated scheme over a field (theorem-backed)."""

    __slots__ = ("_g", "_base", "_sage_curve")

    def __init__(
        self,
        g: int = 0,
        *,
        sage_curve: Curve_generic | None = None,
        base_scheme: AffineScheme | None = None,
    ) -> None:
        self._g = int(g)
        self._base = base_scheme if base_scheme is not None else _default_base()
        self._sage_curve = sage_curve

    def dimension(self) -> int:
        return 1

    def arithmetic_genus(self) -> int:
        return self._g

    def geometric_genus(self) -> int:
        r"""Geometric genus; equals arithmetic genus when smooth/irreducible."""
        return self._g

    def base_scheme(self) -> AffineScheme:
        return self._base

    def is_smooth(self) -> bool:
        return True

    def is_nodal(self) -> bool:
        return False

    def singular_locus(self) -> tuple[object, ...]:
        return ()

    def irreducible_components(self) -> tuple[Curve, ...]:
        return (self,)

    def sage_curve(self) -> Curve_generic:
        if self._sage_curve is None:
            raise ValueError("no Sage curve model attached")
        if not isinstance(self._sage_curve, _curve_generic_type()):
            raise TypeError(f"expected Curve_generic; found {type(self._sage_curve)}")
        return self._sage_curve

    def normalization(self) -> NormalizationMorphism:
        if self._sage_curve is not None and hasattr(self._sage_curve, "normalization"):
            normalized = self._sage_curve.normalization()
            return NormalizationMorphism(normalized, self)
        return NormalizationMorphism(self, self)


class PointedCurve(Curve):
    r"""Base pointed curve over a field, backed by a Sage curve when smooth."""

    __slots__ = ("_n", "_markings")

    def __init__(
        self,
        g: int,
        n: int,
        *,
        sage_curve: Curve_generic | None = None,
        markings: tuple[object, ...] | None = None,
        base_scheme: AffineScheme | None = None,
    ) -> None:
        Curve.__init__(self, g, sage_curve=sage_curve, base_scheme=base_scheme)
        self._n = int(n)
        if markings is None:
            self._markings: tuple[object, ...] = ()
        else:
            if len(markings) != self._n:
                raise ValueError(f"expected {self._n} markings; found {len(markings)}")
            self._markings = tuple(markings)

    def number_of_markings(self) -> int:
        return self._n

    def marking_set(self) -> tuple[int, ...]:
        r"""Ordered marking labels `I = \{1,\ldots,n\}` (default indexing)."""
        return tuple(range(1, self._n + 1))

    def markings(self) -> tuple[object, ...]:
        return self._markings

    def marked_point(self, i: int) -> object:
        labels = self.marking_set()
        if i not in labels:
            raise KeyError(f"marking label {i} not in {labels}")
        if not self._markings:
            raise ValueError("no marking scheme-points attached")
        return self._markings[labels.index(i)]

    def marking_schemes_points(self) -> tuple[object, ...]:
        r"""Ordered marking points as morphisms `\mathrm{Spec}(k) \to C`."""
        return self.markings()

    def sage_curve(self) -> Curve_generic:
        if self._sage_curve is None:
            raise ValueError("no Sage curve model attached (nodal geometric gluing not implemented)")
        return Curve.sage_curve(self)


class SmoothPointedCurve(PointedCurve):
    r"""Smooth pointed curve of type `(g, n)` with a Sage :class:`Curve_generic` model."""

    def is_smooth(self) -> bool:
        return True

    def is_nodal(self) -> bool:
        return False

    def indexes_smooth_stratum(self) -> bool:
        return True

    def dual_graph(self) -> StableGraph:
        from ..objects.stable_graphs import StableGraphs

        return StableGraphs(self._g, self._n).smooth()

    def normalization(self) -> NormalizationMorphism:
        curve = self.sage_curve()
        if hasattr(curve, "normalization"):
            normalized = curve.normalization()
            return NormalizationMorphism(normalized, self)
        return NormalizationMorphism(curve, self)

    @classmethod
    def from_ambient(cls, g: int, n: int, base_scheme: AffineScheme | None = None) -> SmoothPointedCurve:
        r"""Build a concrete smooth model for the proving set `(0,n)`, `(1,1)`, hyperelliptic."""
        base = base_scheme if base_scheme is not None else _default_base()
        ring = base.ring()
        if g == 0:
            if n < 3:
                raise ValueError(f"smooth (0, n) requires n >= 3 for moduli; found n={n}")
            curve = rational_plane_model(ring)
            marks = rational_markings(curve, n)
            return cls(0, n, sage_curve=curve, markings=marks, base_scheme=base)
        if g == 1 and n == 1:
            curve = elliptic_model(ring)
            assert callable(curve), f"elliptic model must be callable; found {type(curve)}"
            origin = curve(0)
            return cls(1, 1, sage_curve=curve, markings=(origin,), base_scheme=base)
        if g >= 2 and n == 0:
            curve = hyperelliptic_model(ring, genus=g)
            return cls(g, 0, sage_curve=curve, markings=(), base_scheme=base)
        if g >= 2:
            curve = hyperelliptic_model(ring, genus=g)
            if n == 0:
                return cls(g, 0, sage_curve=curve, markings=(), base_scheme=base)
        raise NotImplementedError(f"no concrete Sage smooth model for (g, n)=({g}, {n}); supported proving set: (0, n>=3), (1, 1), (g>=2, n=0)")


class StablePointedCurve(PointedCurve):
    r"""Stable pointed curve; smooth fibers are Sage-backed, nodal via dual graph."""

    __slots__ = ("_graph_type",)

    def __init__(
        self,
        g: int,
        n: int,
        graph_type: StableGraph | None = None,
        *,
        sage_curve: Curve_generic | None = None,
        markings: tuple[object, ...] | None = None,
        base_scheme: AffineScheme | None = None,
    ) -> None:
        super().__init__(g, n, sage_curve=sage_curve, markings=markings, base_scheme=base_scheme)
        self._graph_type = graph_type

    def is_stable(self) -> bool:
        return True

    def is_nodal(self) -> bool:
        return self._graph_type is not None and self._graph_type.num_edges() > 0

    def is_smooth(self) -> bool:
        return self._graph_type is None or self._graph_type.num_edges() == 0

    def geometric_genus(self) -> int:
        r"""Sum of geometric genera of normalization components (dual-graph vertex weights)."""
        if self.is_smooth():
            return self._g
        graph = self.dual_graph()
        return sum(graph.vertex_genus(v) for v in range(graph.num_vertices()))

    def singular_locus(self) -> tuple[object, ...]:
        r"""Nodes of a nodal stable curve, indexed by dual-graph internal edges."""
        if self.is_smooth():
            return ()
        return tuple(self.dual_graph().edges())

    def irreducible_components(self) -> tuple[Curve, ...]:
        if self.is_smooth():
            return (self,)
        graph = self.dual_graph()
        return tuple(Curve(graph.vertex_genus(v), base_scheme=self._base) for v in range(graph.num_vertices()))

    def normalization(self) -> NormalizationMorphism:
        if self.is_smooth():
            if self._sage_curve is not None:
                curve = self.sage_curve()
                if hasattr(curve, "normalization"):
                    return NormalizationMorphism(curve.normalization(), self)
                return NormalizationMorphism(curve, self)
            return NormalizationMorphism(self, self)
        return NormalizationMorphism(self.irreducible_components(), self)

    def dual_graph(self) -> StableGraph:
        from ..objects.stable_graphs import StableGraph as StableGraphElement
        from ..objects.stable_graphs import StableGraphs

        graphs = StableGraphs(self._g, self._n)
        if self._graph_type is not None:
            element = graphs(self._graph_type._canonical_record())
            assert isinstance(element, StableGraphElement), f"StableGraphs() must return StableGraph; found {type(element)!r}"
            return element
        return graphs.smooth()

    def sage_curve(self) -> Curve_generic:
        if self.is_nodal() and self._sage_curve is None:
            raise ValueError("nodal stable fibers use combinatorial dual_graph(); geometric nodal Sage models are not implemented")
        if self._sage_curve is None:
            smooth = SmoothPointedCurve.from_ambient(self._g, self._n, self._base)
            self._sage_curve = smooth.sage_curve()
            if not self._markings:
                self._markings = tuple(smooth.markings())
        return PointedCurve.sage_curve(self)

    @classmethod
    def from_ambient(cls, g: int, n: int, base_scheme: AffineScheme | None = None) -> StablePointedCurve:
        smooth = SmoothPointedCurve.from_ambient(g, n, base_scheme)
        return cls(
            g,
            n,
            None,
            sage_curve=smooth.sage_curve(),
            markings=smooth.markings(),
            base_scheme=smooth.base_scheme(),
        )
