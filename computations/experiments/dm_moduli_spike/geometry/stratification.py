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


class Strata(UniqueRepresentation, Parent):
    r"""Parent of locally closed strata of a fixed stratification ``Σ``."""

    Element: type[Stratum]

    def __init__(self, stratification: Stratification) -> None:
        from sage.categories.sets_cat import Sets

        self._stratification = stratification
        Parent.__init__(self, category=Sets())

    def stratification(self) -> Stratification:
        return self._stratification

    def _element_constructor_(
        self,
        index: object,
        underlying: Stack | None = None,
        immersion: LocallyClosedImmersion | None = None,
    ) -> Stratum:
        if isinstance(index, Stratum):
            if index.parent() is self:
                return index
            raise ValueError(f"{index!r} is not a stratum of {self!r}")
        if underlying is None:
            raise TypeError("Strata(Σ)(index, underlying_stack) requires an underlying Stack")
        return cast(Stratum, self.element_class(self, index, underlying, immersion=immersion))

    def _repr_(self) -> str:
        return f"Strata({self._stratification!r})"


class Stratum(Element):
    r"""Locally closed stratum of a stratification; underlying stack is typically a quotient.

    Construct via ``Strata(Σ)(index, underlying)`` or :meth:`Stratification.stratum`.
    """

    def __init__(
        self,
        parent: Strata | Stratification,
        index: object,
        underlying: Stack,
        *,
        immersion: LocallyClosedImmersion | None = None,
    ) -> None:
        if isinstance(parent, Stratification):
            # Legacy construction Stratum(Σ, index, stack) used during stratification build.
            stratification = parent
            parent = Strata(stratification)
        else:
            stratification = parent.stratification()
        ambient = stratification.space()
        if not isinstance(ambient, Stack):
            raise TypeError(f"stratification ambient must be a Stack; found {type(ambient)}")
        self._stratification = stratification
        self._index = index
        self._underlying = underlying
        self._ambient = ambient
        self._immersion = immersion or LocallyClosedImmersion(underlying, ambient)
        self._clutching: ClutchingMorphism | None = None
        self._closure_normalization: QuotientStack | None = None
        self._substack = LocallyClosedSubstack(ambient, underlying, immersion=self._immersion)
        Element.__init__(self, parent)

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

    def closure_normalization(self) -> QuotientStack | None:
        r"""Normalization of the stratum closure: ``[∏ Mbar_{g(v),H(v)} / Aut(Γ)]``."""
        if hasattr(self, "_closure_normalization"):
            return self._closure_normalization
        return None

    def _repr_(self) -> str:
        return f"Stratum({self._index!r})"


Strata.Element = Stratum


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
        r"""Induced stratification on a union of strata ``subspace``.

        Index set is ``{p ∈ P : stratum(p) lives in subspace}``. For the DM
        boundary this drops the zero-edge smooth stratum.
        """
        from sage.combinat.posets.posets import Poset

        kept: list[object] = []
        for p in self._poset:
            if _stratum_belongs_to_subspace(self.stratum(p), subspace):
                kept.append(p)
        if not kept:
            raise ValueError(f"restrict({subspace!r}) retains no strata of {self!r}")
        covers = [(a, b) for a, b in self._poset.cover_relations() if a in kept and b in kept]
        subposet = Poset((kept, covers), cover_relations=True, facade=True)
        new_strata = {p: self._strata[p] for p in kept if p in self._strata}
        # Also match by equality for StableGraph keys
        for p in kept:
            if p not in new_strata:
                new_strata[p] = self.stratum(p)
        return cast(
            Stratification,
            Stratifications(subspace)(
                subposet,
                new_strata,
                indexing_category=self._indexing_category,
            ),
        )

    def _repr_(self) -> str:
        return f"Stratification({self.space()!r}, |P|={self._poset.cardinality()})"


def _stratum_belongs_to_subspace(stratum: Stratum, subspace: object) -> bool:
    r"""Whether a stratum index belongs to a restricted subspace (e.g. boundary)."""
    from .stacks import Boundary

    index = stratum.index()
    if isinstance(subspace, Boundary):
        # Boundary omits the open (zero-edge) stratum.
        if hasattr(index, "num_edges"):
            return int(index.num_edges()) > 0
        return index != "open"
    if hasattr(index, "num_edges") and hasattr(subspace, "num_edges"):
        return True
    return True


Stratifications.Element = Stratification


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
        from ..objects.gamma import StableGraphCategory

        assert hasattr(stack, "genus") and hasattr(stack, "number_of_markings"), (
            f"stack must expose genus() and number_of_markings(); found {type(stack)!r}; owned boundary=StableDualGraph.indexing_category"
        )
        g = int(stack.genus())
        n = int(stack.number_of_markings())
        return StableGraphCategory(g, n)

    def __repr__(self) -> str:
        return "StableDualGraph()"


def dual_graph_boundary_poset(boundary: Boundary, order: str = "specialization") -> FinitePoset:
    r"""Boundary specialization poset = full dual-graph poset restricted to |E|>0."""
    ambient = boundary.ambient_space()
    assert hasattr(ambient, "genus") and hasattr(ambient, "number_of_markings"), (
        f"boundary ambient must expose genus() and number_of_markings(); "
        f"found type={type(ambient)!r}; ambient={ambient!r}; "
        "owned boundary=dual_graph_boundary_poset; "
        "attach moduli type on coarse spaces via ModuliStack.coarse_space()"
    )
    if hasattr(ambient, "stratification"):
        full = ambient.stratification(by=StableDualGraph())
        restricted = full.restrict(boundary)
        poset = restricted.specialization_poset()
        if order == "closure":
            return poset.dual()
        return poset
    g = ambient.genus()
    n = ambient.number_of_markings()
    from ..objects.gamma import StableGraphCategory

    gamma = StableGraphCategory(int(g), int(n))
    full = gamma.specialization_poset()
    sub = full.subposet([x for x in full if x.num_edges() > 0])
    if order == "closure":
        return sub.dual()
    return sub


def _factor_marking_set(graph: object, vertex: int) -> tuple[object, ...]:
    r"""Half-edges at ``vertex`` as the marking set of the factor moduli stack."""
    assert hasattr(graph, "flags_at"), f"graph must expose flags_at(vertex); found {type(graph)!r}; owned boundary=_factor_marking_set"
    return tuple(graph.flags_at(vertex))


class _ProductStackAction(UniqueRepresentation):
    r"""Formal Aut(Γ)-action on a product of moduli factors (vertex permutation + labels).

    Wave 1 certificate: not the half-edge set action. Full PR #225 Actions wiring later.
    """

    def __init__(self, group: object, product: ProductStack, graph: object) -> None:
        self._group = group
        self._product = product
        self._graph = graph

    def group(self) -> object:
        return self._group

    def set(self) -> ProductStack:
        return self._product

    def graph(self) -> object:
        return self._graph

    def __repr__(self) -> str:
        return f"AutActionOnProduct({self._group!r}, {self._product!r})"


def build_dual_graph_stratification(stack: Stack) -> Stratification:
    r"""Dual-graph stratification of a moduli stack.

    Open stratum of ``Mbar``: ``[∏_v M_{g(v),H(v)} / Aut(Γ)]``.
    Closure normalization: ``[∏_v Mbar_{g(v),H(v)} / Aut(Γ)]``.
    Clutching: ``∏_v Mbar_{g(v),H(v)} → Mbar``.
    """
    from ..moduli.instances import M_gI, Mbar_gI
    from ..objects.gamma import StableGraphCategory
    from ..objects.stable_graphs import StableGraph as StableGraphElement

    assert hasattr(stack, "genus") and hasattr(stack, "number_of_markings"), (
        f"stack must expose genus() and number_of_markings(); found {type(stack)!r}; owned boundary=build_dual_graph_stratification"
    )
    g = int(stack.genus())
    n = int(stack.number_of_markings())
    base = stack.base_scheme()
    Gamma = StableGraphCategory(g, n)
    indexing = Gamma
    poset = Gamma.specialization_poset()
    open_factor = M_gI
    compact_factor = Mbar_gI
    # Open moduli stack uses open factors for open strata; compact ambient still
    # uses M for open strata and Mbar for clutching/closure normalization.
    strat = cast(Stratification, Stratifications(stack)(poset, {}, indexing_category=indexing))
    for graph in poset:
        assert isinstance(graph, StableGraphElement), f"specialization poset elements must be StableGraph; found {type(graph)!r}"
        open_factors = []
        compact_factors = []
        for v in range(graph.num_vertices()):
            w = graph.vertex_genus(v)
            marks = _factor_marking_set(graph, v)
            open_factors.append(open_factor(w, marks, base=base))
            compact_factors.append(compact_factor(w, marks, base=base))
        open_product = ProductStack(tuple(open_factors), base=base)
        compact_product = ProductStack(tuple(compact_factors), base=base)
        aut = graph.automorphism_group(on="half_edges")
        open_action = _ProductStackAction(aut, open_product, graph)
        compact_action = _ProductStackAction(aut, compact_product, graph)
        open_quot = QuotientStack(open_product, aut, open_action)
        closure_quot = QuotientStack(compact_product, aut, compact_action)
        stratum = Stratum(strat, graph, open_quot)
        stratum._clutching = ClutchingMorphism(compact_product, stack, graph=graph)
        stratum._closure_normalization = closure_quot
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
