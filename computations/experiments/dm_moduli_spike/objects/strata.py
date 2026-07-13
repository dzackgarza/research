r"""Geometric strata and their symbolic stack signatures.

For a stable graph :math:`\Gamma`, the locally closed substack of curves with
dual graph :math:`\Gamma` is

.. math::

    \mathcal M_\Gamma \simeq
    \Big[\prod_{v \in V(\Gamma)} \mathcal M_{w(v), n_v} \big/ \operatorname{Aut}(\Gamma)\Big],

and the analogous quotient using :math:`\overline{\mathcal M}_{w(v), n_v}` is the
normalisation of the closure of the stratum.  These are represented here as
*symbolic, typed signatures*: the spike records the moduli factors, the
automorphism group (not merely its order), and the indexing dual graph, without
evaluating the quotient as an algebraic stack.

A :class:`DMStratum` is the stratum itself, kept distinct from the
:class:`~dm_moduli_spike.objects.graph_types.StableGraphType` that indexes it.
"""

from __future__ import annotations

from collections.abc import Callable

from .automorphism_action import AutomorphismAction
from .graph_types import StableGraphType


def _validate_group_order(group_order: int) -> int:
    order = int(group_order)
    if order <= 0:
        raise ValueError(f"automorphism group order must be positive; found {group_order!r}")
    return order


class ModuliFactor:
    r"""A symbolic moduli factor :math:`\overline{\mathcal M}_{g(v),H(v)}`.

    The finite set ``flags`` records the half-edges :math:`H(v)=\partial^{-1}(v)`
    on the indexing stable graph; marking sections are the leg flags among them.
    """

    __slots__ = ("_g", "_n", "_compact", "_flags")

    def __init__(
        self,
        g: int,
        n: int,
        compact: bool = False,
        *,
        flags: tuple[int, ...] | None = None,
    ) -> None:
        self._g = int(g)
        self._n = int(n)
        self._compact = bool(compact)
        if flags is None:
            self._flags = tuple(range(self._n))
        else:
            self._flags = tuple(int(flag) for flag in flags)
            assert len(self._flags) == self._n, f"|flags|={len(self._flags)} must equal valence {self._n}"

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def flags(self) -> tuple[int, ...]:
        r"""Half-edges :math:`H(v)` on this factor."""
        return self._flags

    def is_compact(self) -> bool:
        return self._compact

    def dimension(self) -> int:
        return 3 * self._g - 3 + self._n

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ModuliFactor) and (self._g, self._n, self._compact, self._flags) == (other._g, other._n, other._compact, other._flags)

    def __hash__(self) -> int:
        return hash((self._g, self._n, self._compact, self._flags))

    def __repr__(self) -> str:
        bar = "Mbar" if self._compact else "M"
        if self._flags == tuple(range(self._n)):
            return f"{bar}({self._g}, {self._n})"
        return f"{bar}({self._g}, H={self._flags})"


class QuotientStackPresentation:
    r"""Symbolic signature of
    :math:`[\prod_v \mathcal M_{w(v), n_v} / \operatorname{Aut}(\Gamma)]`."""

    __slots__ = ("_product", "_group_order", "_compact", "_curve_type")

    def __init__(
        self,
        product: tuple[ModuliFactor, ...],
        group_order: int,
        compact: bool,
        curve_type: StableGraphType,
    ) -> None:
        self._product = product
        self._group_order = _validate_group_order(group_order)
        self._compact = bool(compact)
        self._curve_type = curve_type

    def product(self) -> tuple[ModuliFactor, ...]:
        return self._product

    def group_order(self) -> int:
        r""":math:`|\operatorname{Aut}(\Gamma)|`."""
        return self._group_order

    def automorphism_action(self) -> AutomorphismAction:
        return self._curve_type.automorphism_action()

    def automorphism_group(self) -> object:
        return self._curve_type.automorphism_group()

    def is_compact(self) -> bool:
        return self._compact

    def curve_type(self) -> StableGraphType:
        r"""The indexing stable dual graph in canonical form."""
        return self._curve_type

    def dimension(self) -> int:
        return sum(factor.dimension() for factor in self._product)

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, QuotientStackPresentation)
            and self._product == other._product
            and self._group_order == other._group_order
            and self._compact == other._compact
            and self._curve_type == other._curve_type
        )

    def __hash__(self) -> int:
        return hash((self._product, self._group_order, self._compact, self._curve_type))

    def __repr__(self) -> str:
        factors = " x ".join(repr(factor) for factor in self._product) or "point"
        return f"QuotientStackPresentation(product=({factors}), |Aut|={self._group_order})"


class ClutchingMorphism:
    r"""Symbolic clutching (gluing) morphism
    :math:`\xi_\Gamma:\prod_v \overline{\mathcal M}_{g(v),H(v)}\to\overline{\mathcal M}_{g,n}`.

    Half-edges on the indexing graph are the local coordinates on each factor;
    internal edges pair the corresponding sections via ``internal_edges()``.
    """

    __slots__ = ("_source_factors", "_target_g", "_target_n", "_group_order", "_curve_type")

    def __init__(
        self,
        source_factors: tuple[ModuliFactor, ...],
        target_genus: int,
        target_markings: int,
        group_order: int,
        curve_type: StableGraphType,
    ) -> None:
        self._source_factors = source_factors
        self._target_g = int(target_genus)
        self._target_n = int(target_markings)
        self._group_order = _validate_group_order(group_order)
        self._curve_type = curve_type

    def source_factors(self) -> tuple[ModuliFactor, ...]:
        return self._source_factors

    def genus(self) -> int:
        r"""Ambient genus :math:`g` of the clutching target :math:`\overline{\mathcal M}_{g,n}`."""
        return self._target_g

    def number_of_markings(self) -> int:
        r"""Ambient marking count :math:`n`` of the clutching target."""
        return self._target_n

    def group_order(self) -> int:
        return self._group_order

    def automorphism_group(self) -> object:
        return self._curve_type.automorphism_group()

    def automorphism_action(self) -> AutomorphismAction:
        return self._curve_type.automorphism_action()

    def markings_by_vertex(self) -> tuple[tuple[int, ...], ...]:
        r"""External marking labels on each vertex factor: :math:`(L(v))_{v\in V}`."""
        record = self._curve_type.canonical_representative()
        return tuple(record.markings_at(vertex) for vertex in range(record.num_vertices()))

    def edge_incidence(self) -> tuple[tuple[int, int], ...]:
        r"""Vertex pairs for each internal edge (in half-edge record order)."""
        record = self._curve_type.canonical_representative()
        return tuple((record.flag_vertex[flag], record.flag_vertex[partner]) for flag, partner in record.internal_edges())

    def marking_flags(self) -> tuple[int, ...]:
        r"""External labels ``1, ..., n`` as flag indices on the indexing graph."""
        return self._curve_type.canonical_representative().marking_to_flag

    def flags_at(self, vertex: int) -> tuple[int, ...]:
        r"""Half-edges (flags) incident to ``vertex``."""
        return self._curve_type.canonical_representative().flags_at(vertex)

    def internal_edges(self) -> tuple[tuple[int, int], ...]:
        r"""Internal edges as ordered flag pairs ``(f, iota(f))`` with ``f < iota(f)``."""
        return self._curve_type.canonical_representative().internal_edges()

    def node_flag_pairs(self) -> tuple[tuple[int, int], ...]:
        r"""Alias for :meth:`internal_edges` in clutching vocabulary."""
        return self.internal_edges()

    def gluing_map(
        self,
    ) -> tuple[tuple[int, ...], tuple[tuple[int, int], ...]]:
        r"""Half-edge gluing data: marking flags and internal edge flag pairs."""
        return (self.marking_flags(), self.internal_edges())

    def curve_type(self) -> StableGraphType:
        return self._curve_type

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, ClutchingMorphism)
            and self._source_factors == other._source_factors
            and (self._target_g, self._target_n) == (other._target_g, other._target_n)
            and self._group_order == other._group_order
            and self._curve_type == other._curve_type
        )

    def __hash__(self) -> int:
        return hash((self._source_factors, self._target_g, self._target_n, self._group_order, self._curve_type))

    def __repr__(self) -> str:
        factors = " x ".join(repr(factor) for factor in self._source_factors) or "point"
        return f"ClutchingMorphism({factors} -> Mbar({self._target_g}, {self._target_n}), |Aut|={self._group_order})"


class DMStratum:
    r"""The geometric stratum :math:`\mathcal M_\Gamma` indexed by a stable curve
    type.  Distinct from its indexing graph: this object owns the stack-geometric
    vocabulary (dimension, codimension, quotient signature, clutching datum)."""

    __slots__ = ("_curve_type", "_g", "_n")

    def __init__(self, curve_type: StableGraphType, g: int, n: int) -> None:
        parent = curve_type.parent()
        g = int(g)
        n = int(n)
        if parent.genus() != g or parent.number_of_markings() != n:
            raise ValueError(f"curve type belongs to Mbar({parent.genus()}, {parent.number_of_markings()}), not Mbar({g}, {n})")
        self._curve_type = curve_type
        self._g = g
        self._n = n

    def curve_type(self) -> StableGraphType:
        return self._curve_type

    def dimension(self) -> int:
        return self._curve_type.stratum_dimension()

    def codimension(self) -> int:
        return self._curve_type.codimension()

    def _factors(self, compact: bool) -> tuple[ModuliFactor, ...]:
        record = self._curve_type.canonical_representative()
        return tuple(
            ModuliFactor(
                record.vertex_genera[v],
                record.valence(v),
                compact=compact,
                flags=record.flags_at(v),
            )
            for v in range(record.num_vertices())
        )

    def open_stack_presentation(self) -> QuotientStackPresentation:
        r""":math:`[\prod_v \mathcal M_{g(v),H(v)} / \operatorname{Aut}(\Gamma)]`."""
        return QuotientStackPresentation(
            self._factors(compact=False),
            self._curve_type.automorphism_number(),
            compact=False,
            curve_type=self._curve_type,
        )

    def closure_normalization_presentation(self) -> QuotientStackPresentation:
        r""":math:`[\prod_v \overline{\mathcal M}_{g(v),H(v)} / \operatorname{Aut}(\Gamma)]`."""
        return QuotientStackPresentation(
            self._factors(compact=True),
            self._curve_type.automorphism_number(),
            compact=True,
            curve_type=self._curve_type,
        )

    def clutching_morphism(self) -> ClutchingMorphism:
        return ClutchingMorphism(
            self._factors(compact=True),
            self._g,
            self._n,
            self._curve_type.automorphism_number(),
            curve_type=self._curve_type,
        )

    def relabel_markings(self, sigma: Callable[[int], int]) -> DMStratum:
        r"""Apply a permutation of ``{1, ..., n}`` to the marking labels."""
        record = self._curve_type.canonical_representative()
        genera = record.vertex_genera
        markings = tuple(record.markings_at(vertex) for vertex in range(record.num_vertices()))
        relabeled_markings = tuple(tuple(int(sigma(marking)) for marking in vertex_markings) for vertex_markings in markings)
        edges = tuple((record.flag_vertex[flag], record.flag_vertex[partner]) for flag, partner in record.internal_edges())
        relabeled = self._curve_type.parent().from_vertices(
            genera=genera,
            markings=relabeled_markings,
            edges=edges,
        )
        return DMStratum(relabeled, self._g, self._n)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, DMStratum) and self._curve_type == other._curve_type and (self._g, self._n) == (other._g, other._n)

    def __hash__(self) -> int:
        return hash((self._curve_type, self._g, self._n))

    def __repr__(self) -> str:
        return f"Stratum of codim {self.codimension()} (dim {self.dimension()}) in Mbar({self._g}, {self._n})"
