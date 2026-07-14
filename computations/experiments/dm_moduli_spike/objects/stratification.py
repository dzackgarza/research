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

**Full and truncated stratifications** use codimension as rank and one-edge
covers.  An **induced subposet** on an arbitrary subset ``S`` may have poset
rank unequal to ambient codimension, and Hasse covers may witness multi-edge
contractions.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING

from .contractions import StableGraphContraction, contract_edges
from .graph_types import StableGraphType, StableGraphTypes
from .isomorphisms import transport_contraction_via_canonical_relabeling

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset


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

    globally_complete = is_effective_full and len(levels) == codim_cap + 1 and _levels_are_contiguous(levels)
    return _finish_stratification(
        curve_types,
        levels,
        max_codim=max_codim,
        codim_cap=codim_cap,
        dimension=dimension,
        exhaustive=globally_complete,
        backend="pure-sage",
        induced_subposet=False,
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
    codim_cap, _is_effective_full = _normalize_codim_cap(max_codim, dimension)
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
        induced_subposet=induced_order,
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


def _contraction_witness(
    delta_type: StableGraphType,
    gamma_type: StableGraphType,
) -> StableGraphContraction | None:
    from .edge_orbits import _elementary_contraction_data

    delta_graph = delta_type.canonical_representative()
    gamma_graph = gamma_type.canonical_representative()

    for target, contraction, _orbit_size in _elementary_contraction_data(delta_type):
        if target == gamma_type:
            return transport_contraction_via_canonical_relabeling(contraction, domain=delta_graph, codomain=gamma_graph)

    edge_diff = delta_type.num_edges() - gamma_type.num_edges()
    if edge_diff <= 0:
        return None

    edges = delta_graph.internal_edges()
    from itertools import combinations

    for subset in combinations(range(len(edges)), edge_diff):
        chosen = tuple(edges[index] for index in subset)
        target_type, contraction = contract_edges(delta_graph, chosen)
        if gamma_type.parent()(target_type) == gamma_type:
            return transport_contraction_via_canonical_relabeling(contraction, domain=delta_graph, codomain=gamma_graph)
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
    induced_subposet: bool = False,
) -> DMStratification:
    from .edge_orbits import _elementary_contraction_data

    by_key: dict[object, StableGraphType] = {}
    for level in levels:
        by_key.update(level)

    all_types = _all_types(levels)
    if induced_subposet:
        cover_pairs = _induced_cover_pairs(all_types)
    else:
        cover_pairs = []
        included = set(by_key)
        for rank in range(1, len(levels)):
            for delta_type in levels[rank].values():
                for target, _contraction, _size in _elementary_contraction_data(delta_type):
                    key = target.canonical_key()
                    if key not in included:
                        continue
                    gamma_type = by_key[key]
                    cover_pairs.append((gamma_type, delta_type))

    unique_covers = list({(gamma, delta): None for gamma, delta in cover_pairs})
    contractions: list[StableGraphContraction] = []
    for gamma_type, delta_type in unique_covers:
        witness = _contraction_witness(delta_type, gamma_type)
        if witness is not None:
            contractions.append(witness)

    _, is_effective_full = _normalize_codim_cap(max_codim, dimension)
    smooth_present = bool(levels) and curve_types.smooth().canonical_key() in levels[0]
    has_full_rank_support = is_effective_full and smooth_present and _levels_are_contiguous(levels) and len(levels) == codim_cap + 1
    is_truncation = max_codim is not None and int(max_codim) < dimension
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
        induced_subposet=induced_subposet,
        is_truncation=is_truncation,
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
        induced_subposet: bool = False,
        is_truncation: bool = False,
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
        self._induced_subposet = induced_subposet
        self._is_truncation = is_truncation

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def dimension(self) -> int:
        return self._curve_types.dimension()

    # -- ranks and strata --------------------------------------------------------

    def curve_type_levels(self) -> list[tuple[StableGraphType, ...]]:
        return [tuple(level.values()) for level in self._levels]

    def strata_by_codimension(self) -> tuple[tuple[StableGraphType, ...], ...]:
        return tuple(tuple(level.values()) for level in self._levels)

    def rank_buckets(self) -> tuple[tuple[StableGraphType, ...], ...]:
        r"""Deprecated alias for :meth:`strata_by_codimension`."""
        return self.strata_by_codimension()

    def rank_sizes(self) -> tuple[int, ...]:
        return tuple(len(level) for level in self._levels)

    def cardinality(self) -> int:
        return sum(len(level) for level in self._levels)

    def strata(self, codim: int | None = None) -> tuple[StableGraphType, ...]:
        if codim is None:
            return tuple(gamma for bucket in self.strata_by_codimension() for gamma in bucket)
        if codim < 0 or codim >= len(self._levels):
            return ()
        return tuple(self._levels[codim].values())

    def boundary_strata(self) -> tuple[StableGraphType, ...]:
        r"""Every stratum of positive codimension (the boundary
        :math:`\partial \overline{\mathcal M}_{g,n}`)."""
        return tuple(gamma for codim in range(1, len(self._levels)) for gamma in self.strata(codim))

    # -- morphisms ---------------------------------------------------------------

    def covers(self) -> tuple[tuple[StableGraphType, StableGraphType], ...]:
        r"""Specialization covers ``(generic, special)``: each pair
        ``(Gamma, Delta)`` has ``Delta -> Gamma`` by contraction to a distinct
        target ``[\Gamma/e]`` (one-edge in full/truncated mode; possibly
        multi-edge in an induced subposet)."""
        return tuple(self._covers)

    def contraction_witnesses(self) -> tuple[StableGraphContraction, ...]:
        return self._contractions

    def find_unique_type(
        self,
        *,
        vertex_genera: Sequence[int],
        marking_blocks: Sequence[Sequence[int]],
        loops: Sequence[int] | None = None,
        edge_multiset: Sequence[tuple[int, int, int]] | None = None,
    ) -> StableGraphType:
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
        matches = [gamma for level in self._levels for gamma in level.values() if gamma == candidate]
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

    def is_full_stratification(self) -> bool:
        r"""True when this object is the complete stratification of :math:`\overline{\mathcal M}_{g,n}`."""
        return self.is_exhaustive() and self.has_full_rank_support()

    def is_codimension_truncation(self) -> bool:
        r"""True when built with ``max_codim < dim`` but complete through that cap."""
        return self._is_truncation and self.complete_through_codim() == self.maximum_codim()

    def is_induced_subposet(self) -> bool:
        r"""True when covers were recovered from an induced order on a type subset."""
        return self._induced_subposet

    def complete_through_codim(self) -> int:
        r"""Highest codimension level enumerated completely in this object."""
        if not _levels_are_contiguous(self._levels):
            return max(0, len(self._levels) - 1) if self._levels else -1
        return self.maximum_codim()

    def maximum_codim(self) -> int:
        return len(self._levels) - 1

    def backend(self) -> str | None:
        return self._backend

    # -- posets ------------------------------------------------------------------

    def _facade_poset(self) -> FinitePoset:
        from sage.combinat.posets.posets import Poset

        strata = [gamma for level in self._levels for gamma in level.values()]
        cover_relations = [[gamma, delta] for gamma, delta in self._covers]
        return Poset((strata, cover_relations), cover_relations=True, facade=True)

    def specialization_poset(self) -> FinitePoset:
        r"""Generic below special; Sage ``FinitePoset`` of :class:`StableGraphType`."""
        return self._facade_poset()

    def closure_poset(self) -> FinitePoset:
        r"""Special below generic (the dual of the specialization poset)."""
        return self.specialization_poset().dual()

    def __repr__(self) -> str:
        if self.is_full_stratification():
            status = "full"
        elif self.is_codimension_truncation():
            status = f"truncated through codim {self.complete_through_codim()}"
        elif self.is_induced_subposet():
            status = "induced subposet"
        else:
            status = f"partial through codim {self.complete_through_codim()}"
        return f"Stratification of Mbar({self._g}, {self._n}) [{status}], rank sizes {self.rank_sizes()}"
