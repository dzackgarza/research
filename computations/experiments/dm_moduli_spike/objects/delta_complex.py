r"""Symmetric Δ-complex / cone complex attached to `\Gamma_{g,n}`.

Cells are indexed by stable graphs (and Aut-orbits on their edges).  The thin
poset order complex recovers the classical boundary complex for
`\overline{\mathcal M}_{0,n}`; for `g>0` that identification is **refused**.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .edge_orbits import automorphism_edge_orbit_indices

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset
    from sage.topology.simplicial_complex import SimplicialComplex

    from .gamma import StableGraphCategory
    from .records import _GraphRecord
    from .stable_graphs import StableGraph


class SymmetricDeltaComplex:
    r"""Symmetric Δ-complex of dual-graph strata for `\Gamma_{g,n}`.

    The underlying thinification is :meth:`StableGraphCategory.specialization_poset`.
    Edge cells of a graph `G` are the Aut-orbits on `E(G)` (cone coordinates
    for the generalized cone complex).
    """

    __slots__ = ("_category",)

    def __init__(self, category: StableGraphCategory) -> None:
        self._category = category

    def category(self) -> StableGraphCategory:
        return self._category

    def genus(self) -> int:
        return self._category.genus()

    def number_of_markings(self) -> int:
        return self._category.number_of_markings()

    def specialization_poset(self) -> FinitePoset:
        return self._category.specialization_poset()

    def edge_orbit_cells(self, graph: _GraphRecord | StableGraph) -> tuple[tuple[tuple[int, int], ...], ...]:
        r"""Aut-orbits on internal edges of `G` (cone generators modulo Aut)."""
        graph = self._category.object(graph)
        edges = graph.internal_edges()
        orbits = automorphism_edge_orbit_indices(graph.canonical_representative())
        return tuple(tuple(edges[i] for i in orbit) for orbit in orbits)

    def cone_dimension(self, graph: _GraphRecord | StableGraph) -> int:
        r"""Dimension of the open cone for `G`: number of Aut edge orbits."""
        return len(self.edge_orbit_cells(graph))

    def boundary_specialization_poset(self) -> FinitePoset:
        r"""Specialization poset with the smooth stratum removed."""
        poset = self.specialization_poset()
        minima = list(poset.minimal_elements())
        assert len(minima) == 1
        smooth = minima[0]
        return poset.subposet([element for element in poset if element != smooth])

    def order_complex(self) -> SimplicialComplex:
        r"""Order complex of the boundary specialization poset (thinification).

        For `g=0` this is the classical combinatorial model of the boundary of
        `\overline{\mathcal M}_{0,n}`.  For `g>0` use
        :meth:`as_dm_boundary_complex` only after reading its refusal.
        """
        return self.boundary_specialization_poset().order_complex()

    def as_dm_boundary_complex(self) -> SimplicialComplex:
        r"""Identify the thin order complex with the DM boundary complex.

        Allowed only for genus `0`.  For `g>0` the thinification ignores
        automorphism quotients of strata; raising is mandatory.
        """
        if self.genus() > 0:
            raise ValueError(
                "order complex of the thinification of Gamma_{g,n} is not the "
                "Deligne–Mumford boundary complex for g>0 (missing Aut quotients); "
                "use order_complex() only as a combinatorial thin-poset complex"
            )
        return self.order_complex()

    def __repr__(self) -> str:
        return f"SymmetricDeltaComplex(Gamma_{self.genus()},{self.number_of_markings()})"


def symmetric_delta_complex(g: int, n: int) -> SymmetricDeltaComplex:
    from .gamma import StableGraphCategory

    return SymmetricDeltaComplex(StableGraphCategory(g, n))
