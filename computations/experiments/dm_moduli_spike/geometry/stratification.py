r"""General finite stratifications and dual-graph stratification of DM boundaries."""

from __future__ import annotations

from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.combinat.posets.posets import FinitePoset

from .stacks import (
    Boundary,
    ClosedImmersion,
    LocallyClosedImmersion,
    ProductStack,
    QuotientStack,
    Stack,
    StackMorphism,
)


class Stratifications(UniqueRepresentation, Parent):
    def __init__(self, space: object) -> None:
        from sage.categories.sets_cat import Sets

        self._space = space
        Parent.__init__(self, category=Sets())

    def space(self) -> object:
        return self._space

    def __contains__(self, obj: object) -> bool:
        return isinstance(obj, Stratification) and obj.space() is self._space

    def _repr_(self) -> str:
        return f"Stratifications({self._space!r})"


class Stratum:
    def __init__(
        self,
        stratification: Stratification,
        index: object,
        underlying: Stack,
        *,
        immersion: LocallyClosedImmersion | None = None,
    ) -> None:
        self._stratification = stratification
        self._index = index
        self._underlying = underlying
        self._immersion = immersion or LocallyClosedImmersion(underlying, stratification.space())  # type: ignore[arg-type]
        self._clutching: ClutchingMorphism | None = None

    def index(self) -> object:
        return self._index

    def underlying_stack(self) -> Stack:
        return self._underlying

    def immersion(self) -> LocallyClosedImmersion:
        return self._immersion

    def clutching_morphism(self) -> ClutchingMorphism | None:
        return self._clutching

    def _repr_(self) -> str:
        return f"Stratum({self._index!r})"


class Stratification:
    def __init__(
        self,
        space: object,
        poset: FinitePoset,
        strata: dict[object, Stratum] | None = None,
    ) -> None:
        self._space = space
        self._poset = poset
        self._strata = dict(strata or {})

    def space(self) -> object:
        return self._space

    def index_poset(self) -> FinitePoset:
        return self._poset

    def specialization_poset(self) -> FinitePoset:
        return self._poset

    def closure_poset(self) -> FinitePoset:
        return self._poset.dual()

    def stratum(self, p: object) -> Stratum:
        if p in self._strata:
            return self._strata[p]
        raise KeyError(p)

    def strata(self) -> tuple[Stratum, ...]:
        return tuple(self._strata[p] for p in self._poset)

    def restrict(self, subspace: object) -> Stratification:
        return Stratification(subspace, self._poset, self._strata)

    def _repr_(self) -> str:
        return f"Stratification({self._space!r}, |P|={self._poset.cardinality()})"


class StratifiedSpace(UniqueRepresentation):
    def __init__(self, underlying: object, stratification: Stratification) -> None:
        self._underlying = underlying
        self._stratification = stratification

    def underlying_space(self) -> object:
        return self._underlying

    def stratification(self) -> Stratification:
        return self._stratification

    def stratification_poset(self, order: str = "specialization") -> FinitePoset:
        if order == "specialization":
            return self._stratification.specialization_poset()
        if order == "closure":
            return self._stratification.closure_poset()
        raise ValueError(order)


class ClutchingMorphism(StackMorphism):
    r"""Clutching morphism as a stack morphism in a Hom-set."""

    def __init__(self, domain: Stack, codomain: Stack, graph: object | None = None) -> None:
        self._graph = graph
        StackMorphism.__init__(self, domain, codomain, kind="clutching")


class StableDualGraph:
    r"""Indexer producing the stable dual-graph stratification."""

    def __repr__(self) -> str:
        return "StableDualGraph()"


def dual_graph_boundary_poset(boundary: Boundary, order: str = "specialization") -> FinitePoset:
    r"""Boundary specialization poset from combinatorial Γ thinification."""
    ambient = boundary.ambient_space()
    g = getattr(ambient, "genus", lambda: None)()
    n = getattr(ambient, "number_of_markings", lambda: None)()
    if g is None or n is None:
        from sage.combinat.posets.posets import Poset

        return Poset([[0, 1]], facade=True)
    from ..objects.gamma import StableGraphCategory

    gamma = StableGraphCategory(int(g), int(n))
    full = gamma.specialization_poset()
    # boundary = omit smooth (minimal) stratum
    minima = list(full.minimal_elements())
    smooth = minima[0]
    sub = full.subposet([x for x in full if x != smooth])
    if order == "closure":
        return sub.dual()
    return sub


def build_dual_graph_stratification(stack: Stack, *, compact: bool = True) -> Stratification:
    from ..objects.gamma import StableGraphCategory
    from ..moduli.instances import M_gI, Mbar_gI

    g = int(stack.genus())  # type: ignore[attr-defined]
    n = int(stack.number_of_markings())  # type: ignore[attr-defined]
    base = stack.base_scheme()
    Gamma = StableGraphCategory(g, n)
    poset = Gamma.specialization_poset()
    strata: dict[object, Stratum] = {}
    for graph in poset:
        factors = []
        for v in range(graph.num_vertices()):
            w = graph.vertex_genera[v]
            flags = graph.flags_at(v)
            I = tuple(range(1, len(flags) + 1))
            if compact:
                factors.append(Mbar_gI(w, I, base=base))
            else:
                factors.append(M_gI(w, I, base=base))
        product = ProductStack(tuple(factors), base=base)
        aut = graph.automorphism_group(on="half_edges")
        quot = QuotientStack(product, aut)
        # placeholder; stratification filled below
        strata[graph] = (product, quot, graph)
    strat = Stratification(stack, poset, {})
    for graph, (product, quot, _g) in strata.items():
        stratum = Stratum(strat, graph, quot)
        stratum._clutching = ClutchingMorphism(product, stack, graph=graph)
        strat._strata[graph] = stratum
    return strat


def scheme_compactification_stratification(open_part: object, boundary: object, ambient: object) -> Stratification:
    r"""Two-stratum stratification for the independent A1↪P1 generality test."""
    from sage.combinat.posets.posets import Poset

    poset = Poset((["open", "boundary"], [("open", "boundary")]), cover_relations=True, facade=True)
    strat = Stratification(ambient, poset, {})
    # underlying stacks are formal placeholders wrapping scheme objects
    open_stack = getattr(open_part, "as_stack", lambda: open_part)()
    bd_stack = getattr(boundary, "as_stack", lambda: boundary)()
    if not isinstance(open_stack, Stack):
        from ..categories.base import spec
        from sage.rings.rational_field import QQ

        open_stack = Stack(spec(QQ), name="OpenStratum")
    if not isinstance(bd_stack, Stack):
        from ..categories.base import spec
        from sage.rings.rational_field import QQ

        bd_stack = Stack(spec(QQ), name="BoundaryStratum")
    strat._strata["open"] = Stratum(strat, "open", open_stack)  # type: ignore[index]
    strat._strata["boundary"] = Stratum(strat, "boundary", bd_stack)  # type: ignore[index]
    return strat
