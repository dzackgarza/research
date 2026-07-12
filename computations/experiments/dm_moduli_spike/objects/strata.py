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
:class:`~dm_moduli_spike.objects.curve_types.StableCurveType` that indexes it.
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
    r"""A symbolic moduli factor :math:`\mathcal M_{g,n}` (open) or
    :math:`\overline{\mathcal M}_{g,n}` (compact)."""

    __slots__ = ("_g", "_n", "_compact")

    def __init__(self, g: int, n: int, compact: bool = False) -> None:
        self._g = int(g)
        self._n = int(n)
        self._compact = bool(compact)

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def is_compact(self) -> bool:
        return self._compact

    def dimension(self) -> int:
        return 3 * self._g - 3 + self._n

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ModuliFactor) and (self._g, self._n, self._compact) == (other._g, other._n, other._compact)

    def __hash__(self) -> int:
        return hash((self._g, self._n, self._compact))

    def __repr__(self) -> str:
        bar = "Mbar" if self._compact else "M"
        return f"{bar}({self._g}, {self._n})"


class QuotientStackSignature:
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

    def automorphism_group(self):
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
            isinstance(other, QuotientStackSignature)
            and self._product == other._product
            and self._group_order == other._group_order
            and self._compact == other._compact
            and self._curve_type == other._curve_type
        )

    def __hash__(self) -> int:
        return hash((self._product, self._group_order, self._compact, self._curve_type))

    def __repr__(self) -> str:
        factors = " x ".join(repr(factor) for factor in self._product) or "point"
        return f"QuotientStackSignature(product=({factors}), |Aut|={self._group_order})"


QuotientStackPresentation = QuotientStackSignature


class ClutchingDatum:
    r"""Symbolic datum for the clutching (gluing) morphism

    .. math::

        \prod_v \overline{\mathcal M}_{w(v), n_v} \longrightarrow \overline{\mathcal M}_{g,n},

    recording boundary factors, the ambient target, the automorphism group, and
    the indexing dual graph.
    """

    __slots__ = ("_source_factors", "_target", "_group_order", "_curve_type")

    def __init__(
        self,
        source_factors: tuple[ModuliFactor, ...],
        target: ModuliFactor,
        group_order: int,
        curve_type: StableGraphType,
    ) -> None:
        self._source_factors = source_factors
        self._target = target
        self._group_order = _validate_group_order(group_order)
        self._curve_type = curve_type

    def source_factors(self) -> tuple[ModuliFactor, ...]:
        return self._source_factors

    def target(self) -> ModuliFactor:
        return self._target

    def group_order(self) -> int:
        return self._group_order

    def automorphism_group(self):
        return self._curve_type.automorphism_group()

    def automorphism_action(self) -> AutomorphismAction:
        return self._curve_type.automorphism_action()

    def local_markings_by_factor(self) -> tuple[tuple[int, ...], ...]:
        r"""Marking labels carried on each moduli factor (by vertex index)."""
        record = self._curve_type.canonical_representative()
        return tuple(record.markings_at(vertex) for vertex in range(record.num_vertices()))

    def gluing_partition(self) -> tuple[frozenset[int], ...]:
        r"""Partition of ``{1, ..., n}`` into the marking sets on each factor."""
        return tuple(frozenset(block) for block in self.local_markings_by_factor())

    def edge_incidence(self) -> tuple[tuple[int, int], ...]:
        r"""Vertex pairs for each internal edge (in half-edge record order)."""
        record = self._curve_type.canonical_representative()
        return tuple(
            (record.flag_vertex[flag], record.flag_vertex[partner])
            for flag, partner in record.internal_edges()
        )

    def external_marking_slots(self) -> tuple[tuple[int, int], ...]:
        r"""Assignment of each external label ``1, ..., n`` to ``(vertex, slot)``."""
        record = self._curve_type.canonical_representative()
        slots: list[tuple[int, int] | None] = [None] * self._target.number_of_markings()
        for vertex in range(record.num_vertices()):
            for slot, label in enumerate(record.markings_at(vertex)):
                slots[label - 1] = (vertex, slot)
        assert all(entry is not None for entry in slots), "marking slot assignment is incomplete"
        return tuple(entry for entry in slots if entry is not None)

    def edge_branch_pairs(self) -> tuple[tuple[int, int], ...]:
        r"""Each internal edge as an ordered half-edge branch pair ``(flag, partner)``."""
        record = self._curve_type.canonical_representative()
        return tuple(record.internal_edges())

    def gluing_map(self) -> tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]:
        r"""Typed gluing data: external marking slots and internal edge branch pairs."""
        return (self.external_marking_slots(), self.edge_branch_pairs())

    def curve_type(self) -> StableGraphType:
        return self._curve_type

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, ClutchingDatum)
            and self._source_factors == other._source_factors
            and self._target == other._target
            and self._group_order == other._group_order
            and self._curve_type == other._curve_type
        )

    def __hash__(self) -> int:
        return hash((self._source_factors, self._target, self._group_order, self._curve_type))

    def __repr__(self) -> str:
        factors = " x ".join(repr(factor) for factor in self._source_factors) or "point"
        return f"ClutchingDatum({factors} -> {self._target!r}, |Aut|={self._group_order})"


ClutchingMorphism = ClutchingDatum


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
            raise ValueError(
                f"curve type belongs to Mbar({parent.genus()}, {parent.number_of_markings()}), "
                f"not Mbar({g}, {n})"
            )
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
            ModuliFactor(record.vertex_genera[v], record.valence(v), compact=compact)
            for v in range(record.num_vertices())
        )

    def open_stack_presentation(self) -> QuotientStackSignature:
        r""":math:`[\prod_v \mathcal M_{w(v), n_v} / \operatorname{Aut}(\Gamma)]`."""
        return QuotientStackSignature(
            self._factors(compact=False),
            self._curve_type.automorphism_number(),
            compact=False,
            curve_type=self._curve_type,
        )

    def closure_normalization_presentation(self) -> QuotientStackSignature:
        r""":math:`[\prod_v \overline{\mathcal M}_{w(v), n_v} / \operatorname{Aut}(\Gamma)]`."""
        return QuotientStackSignature(
            self._factors(compact=True),
            self._curve_type.automorphism_number(),
            compact=True,
            curve_type=self._curve_type,
        )

    def clutching_morphism(self) -> ClutchingDatum:
        return ClutchingDatum(
            self._factors(compact=True),
            ModuliFactor(self._g, self._n, compact=True),
            self._curve_type.automorphism_number(),
            curve_type=self._curve_type,
        )

    def relabel_markings(self, sigma: Callable[[int], int]) -> DMStratum:
        r"""Apply a permutation of ``{1, ..., n}`` to the marking labels."""
        record = self._curve_type.canonical_representative()
        genera = record.vertex_genera
        markings = tuple(record.markings_at(vertex) for vertex in range(record.num_vertices()))
        relabeled_markings = tuple(
            tuple(int(sigma(marking)) for marking in vertex_markings)
            for vertex_markings in markings
        )
        edges = tuple(
            (record.flag_vertex[flag], record.flag_vertex[partner])
            for flag, partner in record.internal_edges()
        )
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
