r"""The finite stratification of :math:`\overline{\mathcal M}_{g,n}` and its
poset facades.

The stratification is built rank by rank (rank = number of nodes = codimension)
and its covers are recovered by *contraction*, independently of generation
provenance: for every graph with ``r + 1`` edges and every internal edge, the
contracted graph has ``r`` edges and is a cover below it in the specialization
order.

Two order conventions are exposed explicitly and never conflated:

* the **specialization order** ``Gamma <=_sp Delta`` iff ``Delta -> Gamma`` by
  contraction (generic below special; the smooth graph is the minimum; rank
  ``|E|``);
* the **closure-inclusion order** ``Delta <=_cl Gamma`` iff
  ``M_Delta subset closure(M_Gamma)`` (special below generic; the smooth stratum
  is maximal), which is the dual.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .contractions import StableGraphContraction
from .strata import DMStratum

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset

    from .curve_types import StableCurveType, StableCurveTypes


def build_stratification(curve_types: StableCurveTypes, max_codim: int | None = None) -> DMStratification:
    r"""Enumerate rank by rank and recover covers by contraction."""
    from .enumeration import one_edge_degenerations

    dimension = curve_types.dimension()
    codim_cap = dimension if max_codim is None else min(int(max_codim), dimension)

    smooth = curve_types.smooth()
    levels: list[dict[object, StableCurveType]] = [{smooth.canonical_key(): smooth}]
    for _ in range(codim_cap):
        current = levels[-1]
        nxt: dict[object, StableCurveType] = {}
        for gamma in current.values():
            for delta in one_edge_degenerations(gamma):
                nxt[delta.canonical_key()] = delta
        if not nxt:
            break
        levels.append(nxt)

    return _finish_stratification(curve_types, levels, max_codim, codim_cap, dimension)


def build_stratification_from_types(
    curve_types: StableCurveTypes,
    types: object,
    max_codim: int | None = None,
) -> DMStratification:
    r"""Bucket an externally enumerated collection of stable curve types by
    codimension and recover covers by contraction.  Used by non-default
    enumeration backends (e.g. admcycles); the mathematical invariants are
    checked independently of the enumerator."""
    dimension = curve_types.dimension()
    codim_cap = dimension if max_codim is None else min(int(max_codim), dimension)
    levels: list[dict[object, StableCurveType]] = []
    for gamma in types:  # type: ignore[attr-defined]
        codim = gamma.num_edges()
        if codim > codim_cap:
            continue
        while len(levels) <= codim:
            levels.append({})
        levels[codim][gamma.canonical_key()] = gamma
    if not levels:
        levels = [{curve_types.smooth().canonical_key(): curve_types.smooth()}]
    return _finish_stratification(curve_types, levels, max_codim, codim_cap, dimension)


def _finish_stratification(
    curve_types: StableCurveTypes,
    levels: list[dict[object, StableCurveType]],
    max_codim: int | None,
    codim_cap: int,
    dimension: int,
) -> DMStratification:
    covers: list[tuple[StableCurveType, StableCurveType]] = []
    contractions: list[StableGraphContraction] = []
    included: set[object] = set()
    for level in levels:
        included.update(level.keys())
    for rank in range(1, len(levels)):
        for delta in levels[rank].values():
            for edge in delta.internal_edges():
                _, contraction = delta.contract(edge)
                gamma = contraction.codomain()
                if gamma.canonical_key() in included:
                    covers.append((gamma, delta))
                    contractions.append(contraction)

    # Deduplicate cover pairs (a single cover may be witnessed by several edges)
    # while keeping every contraction witness.
    unique_covers = list({(gamma, delta): None for gamma, delta in covers})
    complete = max_codim is None or codim_cap >= dimension
    return DMStratification(
        g=curve_types.genus(),
        n=curve_types.number_of_markings(),
        curve_types=curve_types,
        levels=levels,
        covers=unique_covers,
        contractions=tuple(contractions),
        complete=complete,
        codim_cap=codim_cap,
    )


class DMStratification:
    r"""A finite (or rank-truncated) stratification of
    :math:`\overline{\mathcal M}_{g,n}`."""

    def __init__(
        self,
        g: int,
        n: int,
        curve_types: StableCurveTypes,
        levels: list[dict[object, StableCurveType]],
        covers: list[tuple[StableCurveType, StableCurveType]],
        contractions: tuple[StableGraphContraction, ...],
        complete: bool,
        codim_cap: int,
    ) -> None:
        self._g = g
        self._n = n
        self._curve_types = curve_types
        self._levels = levels
        self._covers = covers
        self._contractions = contractions
        self._complete = complete
        self._codim_cap = codim_cap

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def dimension(self) -> int:
        return self._curve_types.dimension()

    # -- ranks and strata --------------------------------------------------------

    def curve_type_levels(self) -> list[tuple[StableCurveType, ...]]:
        return [tuple(level.values()) for level in self._levels]

    def _stratum(self, curve_type: StableCurveType) -> DMStratum:
        return DMStratum(curve_type, self._g, self._n)

    def rank_buckets(self) -> tuple[tuple[DMStratum, ...], ...]:
        return tuple(tuple(self._stratum(gamma) for gamma in level.values()) for level in self._levels)

    def rank_sizes(self) -> tuple[int, ...]:
        return tuple(len(level) for level in self._levels)

    def cardinality(self) -> int:
        return sum(len(level) for level in self._levels)

    def strata(self, codim: int | None = None) -> tuple[DMStratum, ...]:
        if codim is None:
            return tuple(stratum for bucket in self.rank_buckets() for stratum in bucket)
        if codim < 0 or codim >= len(self._levels):
            return ()
        return tuple(self._stratum(gamma) for gamma in self._levels[codim].values())

    def boundary_strata(self) -> tuple[DMStratum, ...]:
        r"""Every stratum of positive codimension (the boundary
        :math:`\partial \overline{\mathcal M}_{g,n}`)."""
        return tuple(stratum for codim in range(1, len(self._levels)) for stratum in self.strata(codim))

    # -- morphisms ---------------------------------------------------------------

    def covers(self) -> tuple[tuple[DMStratum, DMStratum], ...]:
        r"""Specialization covers ``(generic, special)``: each pair
        ``(Gamma, Delta)`` has ``Delta -> Gamma`` a one-edge contraction."""
        return tuple((self._stratum(gamma), self._stratum(delta)) for gamma, delta in self._covers)

    def contraction_witnesses(self) -> tuple[StableGraphContraction, ...]:
        return self._contractions

    # -- completeness metadata ---------------------------------------------------

    def is_complete(self) -> bool:
        return self._complete

    def maximum_codim(self) -> int:
        return len(self._levels) - 1

    # -- posets ------------------------------------------------------------------

    def _facade_poset(self) -> FinitePoset:
        from sage.combinat.posets.posets import Poset

        strata = [self._stratum(gamma) for level in self._levels for gamma in level.values()]
        cover_relations = [[self._stratum(gamma), self._stratum(delta)] for gamma, delta in self._covers]
        return Poset((strata, cover_relations), cover_relations=True, facade=True)

    def specialization_poset(self) -> StratificationPoset:
        r"""Generic below special; rank function ``codimension``."""
        return StratificationPoset(self._facade_poset(), convention="specialization")

    def closure_poset(self) -> StratificationPoset:
        r"""Special below generic (the dual of the specialization poset)."""
        return self.specialization_poset().dual()

    def __repr__(self) -> str:
        status = "complete" if self._complete else f"truncated at codim {self.maximum_codim()}"
        return f"Stratification of Mbar({self._g}, {self._n}) [{status}], rank sizes {self.rank_sizes()}"


class StratificationPoset:
    r"""A typed wrapper around a Sage finite poset that carries its order
    convention.  No method is called a bare ``poset()``: the convention is part
    of the object.
    """

    __slots__ = ("_poset", "_convention")

    def __init__(self, poset: FinitePoset, convention: str) -> None:
        assert convention in ("specialization", "closure"), f"unknown order convention {convention!r}"
        self._poset = poset
        self._convention = convention

    def convention(self) -> str:
        return self._convention

    def sage_poset(self) -> FinitePoset:
        r"""The underlying Sage facade poset (elements are :class:`DMStratum`)."""
        return self._poset

    def dual(self) -> StratificationPoset:
        dual_convention = "closure" if self._convention == "specialization" else "specialization"
        return StratificationPoset(self._poset.dual(), convention=dual_convention)

    def hasse_diagram(self) -> object:
        return self._poset.hasse_diagram()

    def cardinality(self) -> int:
        return int(self._poset.cardinality())

    def is_graded(self) -> bool:
        return bool(self._poset.is_graded())

    def rank_function(self) -> object:
        return self._poset.rank_function()

    def minimal_elements(self) -> list[DMStratum]:
        return list(self._poset.minimal_elements())

    def maximal_elements(self) -> list[DMStratum]:
        return list(self._poset.maximal_elements())

    def __repr__(self) -> str:
        return f"Stratification poset ({self._convention} order) on {self.cardinality()} strata"
