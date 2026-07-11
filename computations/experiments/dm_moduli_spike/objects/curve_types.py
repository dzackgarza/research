r"""The parent/element pair for stable curve types.

A :class:`StableCurveType` is an immutable ``Element`` representing an
isomorphism class of stable dual graphs -- an *index* for a stratum of
:math:`\overline{\mathcal M}_{g,n}`.  It is deliberately kept distinct from the
stratum itself (:class:`~dm_moduli_spike.objects.strata.DMStratum`) so that
graph-theoretic operations do not get entangled with the stack-geometric ones.

:class:`StableCurveTypes` is the Sage ``Parent`` of all stable curve types for a
fixed stable ``(g, n)``.  It is a ``UniqueRepresentation`` and a
``FiniteEnumeratedSet``: the set is mathematically finite (edges are bounded by
:math:`3g - 3 + n`) even when enumeration is performed lazily.
"""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, ClassVar

from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from .canonical import CanonicalKey, automorphism_number, canonical_key, to_json
from .records import StableGraphRecord

if TYPE_CHECKING:
    from sage.graphs.graph import Graph

    from .contractions import StableGraphContraction


class StableCurveType(Element):
    r"""An isomorphism class of stable dual graphs of type ``(g, n)``.

    Equality and hashing are by the colour-aware canonical key, so two records
    that differ only by a relabelling of vertices/flags define the *same*
    element.
    """

    def __init__(self, parent: StableCurveTypes, record: StableGraphRecord) -> None:
        super().__init__(parent)
        self._record = record
        self._canonical_key: CanonicalKey = canonical_key(record)

    # -- the underlying record and canonical data --------------------------------

    def record(self) -> StableGraphRecord:
        return self._record

    def canonical_key(self) -> CanonicalKey:
        return self._canonical_key

    def canonicalized(self) -> StableCurveType:
        r"""A representative in canonical form.  Isomorphism-class identity is
        already carried by :meth:`canonical_key`, so this returns ``self``; it
        exists as an explicit verb for callers that expect a canonical object."""
        return self

    # -- graph-theoretic invariants ----------------------------------------------

    def total_genus(self) -> int:
        return self._record.genus()

    def num_vertices(self) -> int:
        return self._record.num_vertices()

    def num_flags(self) -> int:
        return self._record.num_flags()

    def num_edges(self) -> int:
        return self._record.num_edges()

    def num_markings(self) -> int:
        return self._record.num_markings()

    def internal_edges(self) -> tuple[tuple[int, int], ...]:
        return self._record.internal_edges()

    def vertex_genera(self) -> tuple[int, ...]:
        return self._record.vertex_genera

    def valence(self, vertex: int) -> int:
        return self._record.valence(vertex)

    def is_stable(self) -> bool:
        return self._record.is_stable()

    def is_smooth(self) -> bool:
        r"""The generic (edge-free) type: the unique open stratum."""
        return self._record.num_edges() == 0

    def first_betti_number(self) -> int:
        return self._record.first_betti_number()

    # -- stratum-shaped invariants (dimension / codimension) ---------------------

    def codimension(self) -> int:
        r""":math:`\operatorname{codim}(\mathcal M_\Gamma) = |E(\Gamma)|`."""
        return self._record.num_edges()

    def stratum_dimension(self) -> int:
        r""":math:`\dim \mathcal M_\Gamma = \sum_v (3 w(v) - 3 + n_v)`.

        Equal to :math:`3g - 3 + n - |E|`; the two formulas are cross-checked in
        the property tests.
        """
        return sum(3 * self._record.vertex_genera[v] - 3 + self._record.valence(v) for v in range(self._record.num_vertices()))

    # -- automorphisms -----------------------------------------------------------

    def automorphism_number(self) -> int:
        r""":math:`|\operatorname{Aut}(\Gamma)|` including loop branch swaps."""
        return automorphism_number(self._record)

    # -- morphisms out -----------------------------------------------------------

    def one_edge_degenerations(self) -> tuple[StableCurveType, ...]:
        r"""All rank ``+1`` degenerations, deduplicated by canonical key: the
        upward covers in the specialization order."""
        from .enumeration import one_edge_degenerations

        return one_edge_degenerations(self)

    def contract(self, edge: tuple[int, int]) -> tuple[StableCurveType, StableGraphContraction]:
        r"""Contract one internal edge, returning the (canonicalised) image type
        together with the contraction morphism witnessing ``self -> image``."""
        from .contractions import contract_edge

        return contract_edge(self, edge)

    # -- views / serialization ---------------------------------------------------

    def sage_multigraph(self) -> Graph:
        return self._record.sage_multigraph()

    def to_json(self) -> dict[str, object]:
        return to_json(self._record, self.parent().genus(), self.parent().number_of_markings())

    # -- element protocol --------------------------------------------------------

    def _richcmp_(self, other: object, op: int) -> bool:
        from sage.structure.richcmp import richcmp

        assert isinstance(other, StableCurveType)
        return richcmp(self._canonical_key, other._canonical_key, op)

    def __hash__(self) -> int:
        return hash((self.parent().genus(), self.parent().number_of_markings(), self._canonical_key))

    def _repr_(self) -> str:
        genera = self._record.vertex_genera
        return f"Stable curve type of genus {self.total_genus()} with {self.num_edges()} node(s), vertex genera {genera}"


class StableCurveTypes(UniqueRepresentation, Parent):
    r"""The finite set of stable curve types of a fixed stable ``(g, n)``."""

    Element = StableCurveType

    if TYPE_CHECKING:
        element_class: ClassVar[type[StableCurveType]]

    def __init__(self, g: int, n: int) -> None:
        g = int(g)
        n = int(n)
        assert g >= 0 and n >= 0, f"(g, n) must be nonnegative integers; (g, n)=({g}, {n})"
        assert 2 * g - 2 + n > 0, f"(g, n)=({g}, {n}) is not in the stable range 2g - 2 + n > 0"
        self._g = g
        self._n = n
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def dimension(self) -> int:
        r""":math:`\dim \overline{\mathcal M}_{g,n} = 3g - 3 + n`."""
        return 3 * self._g - 3 + self._n

    def _repr_(self) -> str:
        return f"Stable curve types of genus {self._g} with {self._n} marking(s)"

    # -- construction ------------------------------------------------------------

    def _element_constructor_(self, data: StableGraphRecord | StableCurveType) -> StableCurveType:
        if isinstance(data, StableCurveType):
            assert data.parent() is self, f"cannot re-parent a stable curve type from {data.parent()} into {self}"
            return data
        assert isinstance(data, StableGraphRecord), f"expected a StableGraphRecord or StableCurveType; found {type(data)}"
        assert data.genus() == self._g, f"record genus {data.genus()} does not match ambient genus {self._g}"
        assert data.num_markings() == self._n, f"record has {data.num_markings()} markings, ambient has {self._n}"
        return self.element_class(self, data)

    def from_record(self, record: StableGraphRecord) -> StableCurveType:
        return self._element_constructor_(record)

    def smooth(self) -> StableCurveType:
        r"""The unique smooth (edge-free) curve type: one vertex of genus ``g``
        carrying all ``n`` markings.  This is the minimum of the specialization
        order."""
        flags = tuple(range(self._n))
        record = StableGraphRecord(
            vertex_genera=(self._g,),
            flag_vertex=(0,) * self._n,
            flag_involution=flags,
            marking_to_flag=flags,
        )
        return self.from_record(record)

    def from_vertices(
        self,
        genera: Sequence[int],
        markings: Sequence[Sequence[int]],
        edges: Sequence[tuple[int, int]],
    ) -> StableCurveType:
        r"""Build a stable curve type from a vertex-oriented description:

        * ``genera[i]`` is the genus of vertex ``i``;
        * ``markings[i]`` is the tuple of marking labels on vertex ``i``;
        * ``edges`` is a list of ``(u, v)`` vertex pairs (``u == v`` for a loop).

        Each marking becomes a leg flag; each edge becomes a pair of flags with
        the involution swapping them.
        """
        genera = tuple(int(g) for g in genera)
        markings = tuple(tuple(int(m) for m in vertex_markings) for vertex_markings in markings)
        edges = tuple((int(u), int(v)) for u, v in edges)
        assert len(genera) == len(markings), f"genera and markings must be indexed by the same vertex set; |genera|={len(genera)}, |markings|={len(markings)}"

        flag_vertex: list[int] = []
        flag_involution: list[int] = []
        marking_to_flag_by_label: dict[int, int] = {}

        for vertex, vertex_markings in enumerate(markings):
            for label in vertex_markings:
                flag = len(flag_vertex)
                flag_vertex.append(vertex)
                flag_involution.append(flag)
                assert label not in marking_to_flag_by_label, f"marking label {label} used twice"
                marking_to_flag_by_label[label] = flag

        for u, v in edges:
            flag_u = len(flag_vertex)
            flag_vertex.append(u)
            flag_involution.append(flag_u + 1)
            flag_v = len(flag_vertex)
            flag_vertex.append(v)
            flag_involution.append(flag_u)

        labels = sorted(marking_to_flag_by_label)
        assert labels == list(range(1, self._n + 1)), f"markings must be exactly 1, ..., {self._n}; found {labels}"
        marking_to_flag = tuple(marking_to_flag_by_label[label] for label in labels)

        record = StableGraphRecord(
            vertex_genera=genera,
            flag_vertex=tuple(flag_vertex),
            flag_involution=tuple(flag_involution),
            marking_to_flag=marking_to_flag,
        )
        return self.from_record(record)

    def from_json(self, data: dict[str, object]) -> StableCurveType:
        r"""Reconstruct a curve type from the versioned JSON representation
        produced by :meth:`StableCurveType.to_json`."""
        ambient = data["ambient"]
        assert isinstance(ambient, dict)
        assert int(ambient["g"]) == self._g and int(ambient["n"]) == self._n, f"JSON ambient {ambient} does not match {self}"
        raw_vertices = data["vertices"]
        raw_edges = data["edges"]
        assert isinstance(raw_vertices, list) and isinstance(raw_edges, list)
        by_id = {int(v["id"]): v for v in raw_vertices}
        order = sorted(by_id)
        position = {vertex_id: index for index, vertex_id in enumerate(order)}
        genera = tuple(int(by_id[vertex_id]["genus"]) for vertex_id in order)
        markings = tuple(tuple(int(m) for m in by_id[vertex_id]["markings"]) for vertex_id in order)
        edges = tuple((position[int(e["ends"][0])], position[int(e["ends"][1])]) for e in raw_edges)
        return self.from_vertices(genera=genera, markings=markings, edges=edges)

    # -- enumeration -------------------------------------------------------------

    def __iter__(self) -> Iterator[StableCurveType]:
        from .enumeration import all_stable_curve_types

        yield from all_stable_curve_types(self)

    def cardinality(self) -> int:
        from sage.rings.integer import Integer

        return Integer(sum(1 for _ in self))
