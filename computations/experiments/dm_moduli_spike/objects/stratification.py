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
from .strata import DMStratum

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset


@dataclass(frozen=True, slots=True)
class EnumerationResult:
    r"""Certificate metadata for a stratification enumeration."""

    levels: tuple[tuple[StableGraphType, ...], ...]
    complete_through_codim: int
    globally_complete: bool
    backend: str | None = None


def _normalize_codim_cap(max_codim: int | None, dimension: int) -> int:
    if max_codim is None:
        return dimension
    if int(max_codim) != max_codim:
        raise ValueError(f"max_codim must be an integer; found {max_codim!r}")
    max_codim = int(max_codim)
    if max_codim < 0:
        raise ValueError(f"max_codim must be nonnegative; found {max_codim}")
    return min(max_codim, dimension)


def _levels_are_contiguous(levels: list[dict[object, StableGraphType]]) -> bool:
    if not levels:
        return False
    return all(levels[codim] for codim in range(len(levels)))


def build_stratification(curve_types: StableGraphTypes, max_codim: int | None = None) -> DMStratification:
    r"""Enumerate rank by rank and recover covers by contraction."""
    from .enumeration import one_edge_degenerations

    dimension = curve_types.dimension()
    codim_cap = _normalize_codim_cap(max_codim, dimension)

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
        enumeration_complete=len(levels) == codim_cap + 1,
        backend="pure-sage",
    )


def build_stratification_from_types(
    curve_types: StableGraphTypes,
    types: Iterable[StableGraphType],
    max_codim: int | None = None,
    *,
    backend: str | None = None,
) -> DMStratification:
    r"""Bucket an externally enumerated collection of stable curve types by
    codimension and recover covers by contraction.  Used by non-default
    enumeration backends (e.g. admcycles); the mathematical invariants are
    checked independently of the enumerator."""
    dimension = curve_types.dimension()
    codim_cap = _normalize_codim_cap(max_codim, dimension)
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
    smooth_present = bool(levels) and curve_types.smooth().canonical_key() in levels[0]
    structurally_complete = max_codim is None or codim_cap >= dimension
    enumeration_complete = (
        structurally_complete
        and smooth_present
        and _levels_are_contiguous(levels)
        and len(levels) == codim_cap + 1
    )
    return _finish_stratification(
        curve_types,
        levels,
        max_codim=max_codim,
        codim_cap=codim_cap,
        dimension=dimension,
        enumeration_complete=enumeration_complete,
        backend=backend,
    )


def _finish_stratification(
    curve_types: StableGraphTypes,
    levels: list[dict[object, StableGraphType]],
    max_codim: int | None,
    codim_cap: int,
    dimension: int,
    *,
    enumeration_complete: bool,
    backend: str | None = None,
) -> DMStratification:
    by_key: dict[object, StableGraphType] = {}
    for level in levels:
        by_key.update(level)

    covers: list[tuple[StableGraphType, StableGraphType]] = []
    contractions: list[StableGraphContraction] = []
    included = set(by_key)
    use_decorated_morphisms = backend == "admcycles-decorated"
    for rank in range(1, len(levels)):
        for delta_type in levels[rank].values():
            delta_graph = delta_type.canonical_representative()
            if use_decorated_morphisms:
                for orbit in delta_type.elementary_contraction_orbits():
                    gamma_type = orbit.target()
                    key = gamma_type.canonical_key()
                    if key not in included:
                        continue
                    gamma_type = by_key[key]
                    gamma_graph = gamma_type.canonical_representative()
                    covers.append((gamma_type, delta_type))
                    contractions.append(orbit.representative().with_endpoints(delta_graph, gamma_graph))
            else:
                for edge in delta_graph.internal_edges():
                    gamma_type, contraction = delta_graph.contract(edge)
                    key = gamma_type.canonical_key()
                    if key in included:
                        gamma_type = by_key[key]
                        gamma_graph = gamma_type.canonical_representative()
                        covers.append((gamma_type, delta_type))
                        contractions.append(contraction.with_endpoints(delta_graph, gamma_graph))

    # Deduplicate cover pairs (a single cover may be witnessed by several edges)
    # while keeping every contraction witness.
    unique_covers = list({(gamma, delta): None for gamma, delta in covers})
    smooth_present = bool(levels) and curve_types.smooth().canonical_key() in levels[0]
    structurally_complete = max_codim is None or codim_cap >= dimension
    complete = (
        structurally_complete
        and enumeration_complete
        and smooth_present
        and _levels_are_contiguous(levels)
        and len(levels) == codim_cap + 1
    )
    return DMStratification(
        g=curve_types.genus(),
        n=curve_types.number_of_markings(),
        curve_types=curve_types,
        levels=levels,
        covers=unique_covers,
        contractions=tuple(contractions),
        complete=complete,
        codim_cap=codim_cap,
        backend=backend,
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
        complete: bool,
        codim_cap: int,
        backend: str | None = None,
    ) -> None:
        self._g = g
        self._n = n
        self._curve_types = curve_types
        self._levels = levels
        self._covers = covers
        self._contractions = contractions
        self._complete = complete
        self._codim_cap = codim_cap
        self._backend = backend

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
        assert len(matches) == 1, (
            f"expected exactly one stratum matching {genera}, markings={markings}, edges={edges}; "
            f"found {len(matches)}"
        )
        return matches[0]

    # -- completeness metadata ---------------------------------------------------

    def is_complete(self) -> bool:
        return self._complete

    def maximum_codim(self) -> int:
        return len(self._levels) - 1

    def enumeration_result(self) -> EnumerationResult:
        r"""Structured completeness certificate for this stratification."""
        return EnumerationResult(
            levels=self.curve_type_levels(),
            complete_through_codim=self.maximum_codim(),
            globally_complete=self.is_complete(),
            backend=self._backend,
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
