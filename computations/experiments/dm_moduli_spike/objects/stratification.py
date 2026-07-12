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

from collections.abc import Iterable, Iterator, Sequence
from dataclasses import dataclass
from typing import TYPE_CHECKING

from .contractions import StableGraphContraction
from .graph_types import StableGraphType, StableGraphTypes
from .isomorphisms import transport_contraction
from .strata import DMStratum

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset


@dataclass(frozen=True, slots=True)
class EnumerationResult:
    r"""Certificate metadata for a stratification enumeration.

    ``construction_mode`` is one of:

    * ``enumerated`` — full or truncated rank-by-rank enumeration;
    * ``induced_subposet`` — Hasse diagram of a supplied type family.
    """

    levels: tuple[tuple[StableGraphType, ...], ...]
    complete_through_codim: int
    globally_complete: bool
    has_full_rank_support: bool
    backend: str | None = None
    construction_mode: str = "enumerated"


def _normalize_codim_cap(max_codim: int | None, dimension: int) -> tuple[int, bool]:
    if max_codim is None:
        return dimension, True
    if int(max_codim) != max_codim:
        raise ValueError(f"max_codim must be an integer; found {max_codim!r}")
    max_codim = int(max_codim)
    if max_codim < 0:
        raise ValueError(f"max_codim must be nonnegative; found {max_codim}")
    if max_codim >= dimension:
        return dimension, True
    return max_codim, False


def _levels_are_contiguous(levels: list[dict[object, StableGraphType]]) -> bool:
    if not levels:
        return False
    return all(levels[codim] for codim in range(len(levels)))


def build_stratification(curve_types: StableGraphTypes, max_codim: int | None = None) -> DMStratification:
    r"""Enumerate rank by rank and recover covers by contraction."""
    from .enumeration import one_edge_degenerations

    dimension = curve_types.dimension()
    codim_cap, is_effective_full = _normalize_codim_cap(max_codim, dimension)

    smooth = curve_types.smooth()
    levels: list[dict[object, StableGraphType]] = [{smooth.canonical_key(): smooth}]
    for _ in range(codim_cap):
        current = levels[-1]
        nxt: dict[object, StableGraphType] = {}
        for gamma in current.values():
            for delta in one_edge_degenerations(gamma):
                nxt[delta.canonical_key()] = delta
        if not nxt:
            break
        levels.append(nxt)

    return _finish_stratification(
        curve_types,
        levels,
        max_codim=max_codim,
        codim_cap=codim_cap,
        dimension=dimension,
        exhaustive=is_effective_full and len(levels) == codim_cap + 1 and _levels_are_contiguous(levels),
        backend="pure-sage",
        construction_mode="enumerated",
    )


def build_stratification_from_types(
    curve_types: StableGraphTypes,
    types: Iterable[StableGraphType],
    max_codim: int | None = None,
    *,
    exhaustive: bool = False,
    induced_order: bool = True,
    backend: str | None = None,
) -> DMStratification:
    r"""Bucket an externally enumerated collection of stable curve types by
    codimension and recover covers by contraction.  Used by non-default
    enumeration backends (e.g. admcycles); the mathematical invariants are
    checked independently of the enumerator."""
    dimension = curve_types.dimension()
    codim_cap, is_effective_full = _normalize_codim_cap(max_codim, dimension)
    levels: list[dict[object, StableGraphType]] = []
    enumerated = tuple(types)
    for gamma in enumerated:
        codim = gamma.num_edges()
        if codim > codim_cap:
            continue
        while len(levels) <= codim:
            levels.append({})
        levels[codim][gamma.canonical_key()] = gamma
    if not levels:
        levels = [{curve_types.smooth().canonical_key(): curve_types.smooth()}]
    return _finish_stratification(
        curve_types,
        levels,
        max_codim=max_codim,
        codim_cap=codim_cap,
        dimension=dimension,
        exhaustive=exhaustive,
        backend=backend,
        construction_mode="induced_subposet" if induced_order else "enumerated",
    )


def _all_types(levels: list[dict[object, StableGraphType]]) -> tuple[StableGraphType, ...]:
    return tuple(gamma for level in levels for gamma in level.values())


def _induced_cover_pairs(types: tuple[StableGraphType, ...]) -> list[tuple[StableGraphType, StableGraphType]]:
    covers: list[tuple[StableGraphType, StableGraphType]] = []
    for delta in types:
        for gamma in types:
            if gamma == delta or not delta.contracts_to(gamma):
                continue
            if any(theta != gamma and theta != delta and delta.contracts_to(theta) and theta.contracts_to(gamma) for theta in types):
                continue
            covers.append((gamma, delta))
    return covers


def _orbit_contraction_witness(
    delta_type: StableGraphType,
    gamma_type: StableGraphType,
) -> StableGraphContraction | None:
    delta_graph = delta_type.canonical_representative()
    gamma_graph = gamma_type.canonical_representative()
    for orbit in delta_type.elementary_contraction_orbits():
        if orbit.target() == gamma_type:
            return transport_contraction(orbit.representative(), domain=delta_graph, codomain=gamma_graph)
    return None


def _finish_stratification(
    curve_types: StableGraphTypes,
    levels: list[dict[object, StableGraphType]],
    max_codim: int | None,
    codim_cap: int,
    dimension: int,
    *,
    exhaustive: bool,
    backend: str | None = None,
    construction_mode: str = "enumerated",
) -> DMStratification:
    by_key: dict[object, StableGraphType] = {}
    for level in levels:
        by_key.update(level)

    all_types = _all_types(levels)
    if construction_mode == "induced_subposet":
        cover_pairs = _induced_cover_pairs(all_types)
    else:
        cover_pairs = []
        included = set(by_key)
        for rank in range(1, len(levels)):
            for delta_type in levels[rank].values():
                for orbit in delta_type.elementary_contraction_orbits():
                    gamma_type = orbit.target()
                    key = gamma_type.canonical_key()
                    if key not in included:
                        continue
                    gamma_type = by_key[key]
                    cover_pairs.append((gamma_type, delta_type))

    unique_covers = list({(gamma, delta): None for gamma, delta in cover_pairs})
    contractions: list[StableGraphContraction] = []
    for gamma_type, delta_type in unique_covers:
        witness = _orbit_contraction_witness(delta_type, gamma_type)
        if witness is not None:
            contractions.append(witness)

    _, is_effective_full = _normalize_codim_cap(max_codim, dimension)
    smooth_present = bool(levels) and curve_types.smooth().canonical_key() in levels[0]
    has_full_rank_support = is_effective_full and smooth_present and _levels_are_contiguous(levels) and len(levels) == codim_cap + 1
    return DMStratification(
        g=curve_types.genus(),
        n=curve_types.number_of_markings(),
        curve_types=curve_types,
        levels=levels,
        covers=unique_covers,
        contractions=tuple(contractions),
        exhaustive=exhaustive,
        has_full_rank_support=has_full_rank_support,
        codim_cap=codim_cap,
        backend=backend,
        construction_mode=construction_mode,
    )


class DMStratification:
    r"""A finite (or rank-truncated) stratification of
    :math:`\overline{\mathcal M}_{g,n}`."""

    def __init__(
        self,
        g: int,
        n: int,
        curve_types: StableGraphTypes,
        levels: list[dict[object, StableGraphType]],
        covers: list[tuple[StableGraphType, StableGraphType]],
        contractions: tuple[StableGraphContraction, ...],
        exhaustive: bool,
        has_full_rank_support: bool,
        codim_cap: int,
        backend: str | None = None,
        construction_mode: str = "enumerated",
    ) -> None:
        self._g = g
        self._n = n
        self._curve_types = curve_types
        self._levels = levels
        self._covers = covers
        self._contractions = contractions
        self._exhaustive = exhaustive
        self._has_full_rank_support = has_full_rank_support
        self._codim_cap = codim_cap
        self._backend = backend
        self._construction_mode = construction_mode

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def dimension(self) -> int:
        return self._curve_types.dimension()

    # -- ranks and strata --------------------------------------------------------

    def curve_type_levels(self) -> list[tuple[StableGraphType, ...]]:
        return [tuple(level.values()) for level in self._levels]

    def _stratum(self, curve_type: StableGraphType) -> DMStratum:
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

    def find_unique_type(
        self,
        *,
        vertex_genera: Sequence[int],
        marking_blocks: Sequence[Sequence[int]],
        loops: Sequence[int] | None = None,
        edge_multiset: Sequence[tuple[int, int, int]] | None = None,
    ) -> DMStratum:
        r"""Locate the unique stratum matching a vertex-indexed construction.

        The lookup is semantic: vertices are numbered ``0, ..., |V|-1`` in the
        order given by ``vertex_genera``; the resulting type is matched by
        canonical key, not by internal vertex numbering in the stratification.
        """
        genera = tuple(int(g) for g in vertex_genera)
        markings = tuple(tuple(int(m) for m in block) for block in marking_blocks)
        edges: list[tuple[int, int]] = []
        if loops is not None:
            for vertex, count in enumerate(loops):
                for _ in range(int(count)):
                    edges.append((vertex, vertex))
        if edge_multiset is not None:
            for u, v, multiplicity in edge_multiset:
                for _ in range(int(multiplicity)):
                    edges.append((int(u), int(v)))
        candidate = self._curve_types.from_vertices(genera=genera, markings=markings, edges=tuple(edges))
        matches = [self._stratum(gamma) for level in self._levels for gamma in level.values() if gamma == candidate]
        assert len(matches) == 1, f"expected exactly one stratum matching {genera}, markings={markings}, edges={edges}; found {len(matches)}"
        return matches[0]

    # -- completeness metadata ---------------------------------------------------

    def has_full_rank_support(self) -> bool:
        r"""Every codimension ``0, ..., dim`` has at least one stratum."""
        return self._has_full_rank_support

    def is_exhaustive(self) -> bool:
        r"""The enumerator attests that every stratum type is present."""
        return self._exhaustive

    def is_complete(self) -> bool:
        r"""Alias for :meth:`is_exhaustive`."""
        return self.is_exhaustive()

    def construction_mode(self) -> str:
        return self._construction_mode

    def is_full_stratification(self) -> bool:
        r"""True when this object is the complete stratification of :math:`\overline{\mathcal M}_{g,n}`."""
        return self.is_exhaustive() and self.has_full_rank_support()

    def maximum_codim(self) -> int:
        return len(self._levels) - 1

    def enumeration_result(self) -> EnumerationResult:
        r"""Structured completeness certificate for this stratification."""
        return EnumerationResult(
            levels=tuple(self.curve_type_levels()),
            complete_through_codim=self.maximum_codim() if self.is_exhaustive() else -1,
            globally_complete=self.is_exhaustive(),
            has_full_rank_support=self.has_full_rank_support(),
            backend=self._backend,
            construction_mode=self._construction_mode,
        )

    def backend(self) -> str | None:
        return self._backend

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
        status = "exhaustive" if self._exhaustive else f"truncated at codim {self.maximum_codim()}"
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

    def __iter__(self) -> Iterator[DMStratum]:
        return iter(self._poset)

    def __contains__(self, element: object) -> bool:
        return element in self._poset

    def is_lequal(self, left: DMStratum, right: DMStratum) -> bool:
        return bool(self._poset.le(left, right))

    def cover_relations(self) -> list[list[DMStratum]]:
        return list(self._poset.cover_relations())

    def rank(self, element: DMStratum) -> int:
        return int(self._poset.rank(element))

    def subposet(self, elements: Sequence[DMStratum]) -> StratificationPoset:
        return StratificationPoset(self._poset.subposet(list(elements)), self._convention)

    def order_complex(self) -> object:
        return self._poset.order_complex()

    def is_isomorphic(self, other: object) -> bool:
        if isinstance(other, StratificationPoset):
            return bool(self._poset.is_isomorphic(other._poset))
        return bool(self._poset.is_isomorphic(other))

    def __repr__(self) -> str:
        return f"Stratification poset ({self._convention} order) on {self.cardinality()} strata"
