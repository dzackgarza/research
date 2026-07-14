r"""General finite stratifications and dual-graph stratification of DM boundaries."""

from __future__ import annotations

from typing import cast

from sage.combinat.posets.posets import FinitePoset
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from .stacks import (
    Boundary,
    LocallyClosedImmersion,
    LocallyClosedSubstack,
    ProductStack,
    QuotientStack,
    Stack,
    StackMorphism,
)


class Stratifications(UniqueRepresentation, Parent):
    r"""Parent of stratifications of a fixed space ``X``."""

    Element: type[Stratification]

    def __init__(self, space: object) -> None:
        from sage.categories.sets_cat import Sets

        self._space = space
        Parent.__init__(self, category=Sets())

    def space(self) -> object:
        return self._space

    def _element_constructor_(
        self,
        poset: object,
        strata: dict[object, Stratum] | None = None,
        indexing_category: object | None = None,
    ) -> Stratification:
        if isinstance(poset, Stratification):
            assert poset.space() is self._space, f"cannot re-parent stratification of {poset.space()!r} into {self!r}"
            return poset
        assert isinstance(poset, FinitePoset), f"expected FinitePoset or Stratification; found {type(poset)!r}"
        return cast(
            Stratification,
            self.element_class(
                self,
                poset,
                strata,
                indexing_category=indexing_category,
            ),
        )

    def __contains__(self, obj: object) -> bool:
        return isinstance(obj, Stratification) and obj.parent() is self

    def _repr_(self) -> str:
        return f"Stratifications({self._space!r})"


class Stratum:
    r"""Locally closed stratum of a stratification; underlying stack is typically a quotient."""

    def __init__(
        self,
        stratification: Stratification,
        index: object,
        underlying: Stack,
        *,
        immersion: LocallyClosedImmersion | None = None,
    ) -> None:
        ambient = stratification.space()
        if not isinstance(ambient, Stack):
            raise TypeError(f"stratification ambient must be a Stack; found {type(ambient)}")
        self._stratification = stratification
        self._index = index
        self._underlying = underlying
        self._ambient = ambient
        self._immersion = immersion or LocallyClosedImmersion(underlying, ambient)
        self._clutching: ClutchingMorphism | None = None
        self._substack = LocallyClosedSubstack(ambient, underlying, immersion=self._immersion)

    def stratification(self) -> Stratification:
        return self._stratification

    def index(self) -> object:
        return self._index

    def ambient(self) -> Stack:
        return self._ambient

    def underlying_stack(self) -> Stack:
        return self._underlying

    def immersion(self) -> LocallyClosedImmersion:
        return self._immersion

    def as_substack(self) -> LocallyClosedSubstack:
        return self._substack

    def clutching_morphism(self) -> ClutchingMorphism | None:
        return self._clutching

    def _repr_(self) -> str:
        return f"Stratum({self._index!r})"


class Stratification(Element):
    r"""Stratification of a space: index poset plus locally closed strata.

    Construct via ``Stratifications(X)(poset, strata=...)``.
    """

    def __init__(
        self,
        parent: Stratifications,
        poset: FinitePoset,
        strata: dict[object, Stratum] | None = None,
        *,
        indexing_category: object | None = None,
    ) -> None:
        self._poset = poset
        self._strata = dict(strata or {})
        self._indexing_category = indexing_category
        Element.__init__(self, parent)

    def space(self) -> object:
        return cast(Stratifications, self.parent()).space()

    def indexing_category(self) -> object | None:
        return self._indexing_category

    def index_poset(self) -> FinitePoset:
        return self._poset

    def specialization_poset(self) -> FinitePoset:
        return self._poset

    def closure_poset(self) -> FinitePoset:
        return self._poset.dual()

    def stratum(self, p: object) -> Stratum:
        if p in self._strata:
            return self._strata[p]
        for key, stratum in self._strata.items():
            if key == p:
                return stratum
        raise KeyError(p)

    def strata(self) -> tuple[Stratum, ...]:
        return tuple(self._strata[p] for p in self._poset)

    def restrict(self, subspace: object) -> Stratification:
        return cast(
            Stratification,
            Stratifications(subspace)(
                self._poset,
                self._strata,
                indexing_category=self._indexing_category,
            ),
        )

    def _repr_(self) -> str:
        return f"Stratification({self.space()!r}, |P|={self._poset.cardinality()})"


Stratifications.Element = Stratification


class StratifiedSpace(UniqueRepresentation, Parent):
    def __init__(self, underlying: object, stratification: Stratification) -> None:
        from ..categories.base import AffineScheme
        from ..categories.stratified import StratifiedSpaces

        self._underlying = underlying
        self._stratification = stratification
        assert hasattr(underlying, "base_scheme"), (
            f"StratifiedSpace requires underlying.base_scheme(); found {type(underlying)!r}; "
            f"underlying={underlying!r}; owned boundary=StratifiedSpace.__init__; "
            "pass a GeometricObject that exposes base_scheme()"
        )
        base = underlying.base_scheme()
        assert isinstance(base, AffineScheme), (
            f"underlying.base_scheme() must return AffineScheme; found {type(base)!r}; underlying={underlying!r}; owned boundary=StratifiedSpace.__init__"
        )
        Parent.__init__(self, category=StratifiedSpaces(base))

    def underlying_space(self) -> object:
        return self._underlying

    def stratification(self) -> Stratification:
        return self._stratification


class ClutchingMorphism(StackMorphism):
    r"""Clutching morphism as a stack morphism in a Hom-set."""

    def __init__(self, domain: Stack, codomain: Stack, graph: object | None = None) -> None:
        self._graph = graph
        StackMorphism.__init__(self, domain, codomain, kind="clutching")

    def graph(self) -> object | None:
        return self._graph


class StableDualGraph(UniqueRepresentation):
    r"""Indexer producing the stable dual-graph stratification of a moduli stack."""

    def indexing_category(self, stack: Stack) -> object:
        from ..objects.stable_graphs import StableGraphs

        assert hasattr(stack, "genus") and hasattr(stack, "number_of_markings"), (
            f"stack must expose genus() and number_of_markings(); found {type(stack)!r}; owned boundary=StableDualGraph.indexing_category"
        )
        g = int(stack.genus())
        if hasattr(stack, "marking_set"):
            I = stack.marking_set()
        else:
            I = range(1, int(stack.number_of_markings()) + 1)
        return StableGraphs(g, I)

    def __repr__(self) -> str:
        return "StableDualGraph()"


def dual_graph_boundary_poset(boundary: Boundary, order: str = "specialization") -> FinitePoset:
    r"""Boundary specialization poset from combinatorial Γ thinification."""
    ambient = boundary.ambient_space()
    assert hasattr(ambient, "genus") and hasattr(ambient, "number_of_markings"), (
        f"boundary ambient must expose genus() and number_of_markings(); "
        f"found type={type(ambient)!r}; ambient={ambient!r}; "
        "owned boundary=dual_graph_boundary_poset; "
        "attach moduli type on coarse spaces via ModuliStack.coarse_space()"
    )
    g = ambient.genus()
    n = ambient.number_of_markings()
    from ..objects.gamma import StableGraphCategory

    gamma = StableGraphCategory(int(g), int(n))
    full = gamma.specialization_poset()
    minima = list(full.minimal_elements())
    smooth = minima[0]
    sub = full.subposet([x for x in full if x != smooth])
    if order == "closure":
        return sub.dual()
    return sub


def _factor_marking_set(graph: object, vertex: int) -> tuple[object, ...]:
    r"""Half-edges at ``vertex`` as the marking set of the factor moduli stack."""
    assert hasattr(graph, "flags_at"), f"graph must expose flags_at(vertex); found {type(graph)!r}; owned boundary=_factor_marking_set"
    return tuple(graph.flags_at(vertex))


def build_dual_graph_stratification(stack: Stack) -> Stratification:
    r"""Dual-graph stratification of a moduli stack.

    Stratum factors are ``Mbar`` or ``M`` according to whether ``stack`` is
    proper (axiom), matching the ambient stack — not a boolean constructor flag.
    """
    from ..moduli.instances import M_gI, Mbar_gI
    from ..objects.gamma import StableGraphCategory
    from ..objects.stable_graphs import StableGraph as StableGraphElement
    from ..objects.stable_graphs import StableGraphs

    assert hasattr(stack, "genus") and hasattr(stack, "number_of_markings"), (
        f"stack must expose genus() and number_of_markings(); found {type(stack)!r}; owned boundary=build_dual_graph_stratification"
    )
    g = int(stack.genus())
    n = int(stack.number_of_markings())
    I = stack.marking_set() if hasattr(stack, "marking_set") else tuple(range(1, n + 1))
    base = stack.base_scheme()
    factor = Mbar_gI if stack.is_proper() else M_gI
    Gamma = StableGraphCategory(g, n)
    indexing = StableGraphs(g, I)
    poset = Gamma.specialization_poset()
    raw: dict[object, tuple[ProductStack, QuotientStack, object]] = {}
    for graph in poset:
        assert isinstance(graph, StableGraphElement), f"specialization poset elements must be StableGraph; found {type(graph)!r}"
        factors = []
        for v in range(graph.num_vertices()):
            w = graph.vertex_genus(v)
            marks = _factor_marking_set(graph, v)
            factors.append(factor(w, marks, base=base))
        product = ProductStack(tuple(factors), base=base)
        aut = graph.automorphism_group(on="half_edges")
        action = graph.action_on_half_edges()
        quot = QuotientStack(product, aut, action)
        raw[graph] = (product, quot, graph)
    strat = cast(Stratification, Stratifications(stack)(poset, {}, indexing_category=indexing))
    for graph, (product, quot, _g) in raw.items():
        stratum = Stratum(strat, graph, quot)
        stratum._clutching = ClutchingMorphism(product, stack, graph=graph)
        strat._strata[graph] = stratum
    return strat


def scheme_compactification_stratification(open_part: object, boundary: object, ambient: object) -> Stratification:
    r"""Two-stratum stratification for the independent A1↪P1 generality test."""
    from sage.combinat.posets.posets import Poset

    def _require_stack(piece: object, role: str) -> Stack:
        if isinstance(piece, Stack):
            return piece
        assert hasattr(piece, "as_stack"), (
            f"{role} requires Stack or as_stack(); found {type(piece)!r}; "
            f"piece={piece!r}; owned boundary=scheme_compactification_stratification; "
            "pass SchemeStack / Boundary / Stack from SchemeStack.stratify"
        )
        stack = piece.as_stack()
        assert isinstance(stack, Stack), f"{role}.as_stack() must return Stack; found {type(stack)!r}; piece={piece!r}"
        return stack

    poset = Poset((["open", "boundary"], [("open", "boundary")]), cover_relations=True, facade=True)
    strat = cast(Stratification, Stratifications(ambient)(poset, {}))
    open_stack = _require_stack(open_part, "open stratum")
    bd_stack = _require_stack(boundary, "boundary stratum")
    strat._strata["open"] = Stratum(strat, "open", open_stack)
    strat._strata["boundary"] = Stratum(strat, "boundary", bd_stack)
    return strat
