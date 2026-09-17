r"""The reduction complex of an indefinite lattice, and what it would need.

A reduction complex is a ``G``-CW structure on the symmetric space of
``O(L)(R)``: for an indefinite form the cells are the perfect domains of
Opgenorth's reduction theory, each a rational polyhedral cone spanned by the
minimal vectors of an auxiliary positive form, and two cells are adjacent when
they share a facet.  Traversing the complex from one cell, taking the
stabilizer of each cell and the transporters along its facets, yields
generators of ``O(L)`` and decides isometry of two lattices in the same genus.
The *marked* variant carries with each cell a finite family of nonzero-norm
vectors, which is how a general Lorentzian vector orbit is computed: the
traversal then answers about the pair (cell, marked family) rather than about
the cell alone.

A cell is an object of ``RationalPolyhedralCones``: the cone in
``L tensor QQ`` cut out by homogeneous half-spaces, with its faces,
intersections, transport along isometries and stabilizers.  The records below
join cells into the complex: an oriented adjacency, a face incidence, a marked
cell, and the finite explorations and completed traversals built from them.

None of this is computed here, and no registered provider of the capability
layer supplies it.  The exact reduction is owned upstream by
polyhedral_common, which reaches the Lorentzian perfect domain only as the
``h = 1`` branch inside its combined indefinite algorithm and exposes no
entry point that traverses the complex; what the layer currently offers is
the automorphism group, the vector and isotropic-subspace equivalence
witnesses, their stabilizers and orbit representatives.  The port that would
supply the traversal is ``sage-indefinite-port``, whose capability manifest
records that dispatch, and it would arrive here as one further capability
name rather than as an implementation in this file.

What *is* owned, so that a caller does not reach here for it:

- generators of ``O(L)`` for an indefinite lattice, through
  ``L.O().group_generators()``, which already goes to polyhedral_common's
  automorphism group and so does not need the cell traversal;
- the ``O(L)``-orbits of vectors of a given square, their stabilizers and
  their equivalence witnesses, through the exact indefinite backend;
- the Lorentzian component character in signature ``(1, n)``, through
  ``L.positive_cone_subgroup()``, whose product with ``<-1>`` is ``O(L)``
  because ``-1`` exchanges the two components of the positive cone.
"""

from sage.matrix.constructor import matrix as engine_matrix
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.polyhedral_cones import (
    RationalPolyhedralCones,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.engine_capabilities import engine_capabilities
from dzack_research.preamble.tensors.tensor import _engine_component_matrix


class ReductionCellAdjacency(SageObject):
    r"""An oriented adjacency of two rational reduction cells.

    It consists of the source cell, target cell, their actual common facet,
    and one lattice isometry carrying source to target.  Reversing the
    adjacency inverts that same transporter and preserves the shared face.
    """

    def __init__(self, source, target, common_face, transporter) -> None:
        if source.ambient_lattice() is not target.ambient_lattice():
            raise ValueError("adjacent reduction cells lie in one lattice")
        if common_face.ambient_lattice() is not source.ambient_lattice():
            raise ValueError("an adjacency face lies in the cells' ambient lattice")
        if not source.is_adjacent_to(target):
            raise ValueError("a reduction-cell adjacency requires a common facet")
        if not common_face.is_equal_to(source.intersection(target)):
            raise ValueError("the retained adjacency face is not the cells' intersection")
        if not source.transport(transporter).is_equal_to(target):
            raise ValueError("the retained adjacency transporter moves the source to the wrong cell")
        self._source = source
        self._target = target
        self._common_face = common_face
        self._transporter = transporter

    def source(self):
        return self._source

    def target(self):
        return self._target

    def lattice(self):
        return self.source().ambient_lattice()

    def common_face(self):
        return self._common_face

    def transporter(self):
        return self._transporter

    def reversed(self):
        return ReductionCellAdjacency(
            self.target(),
            self.source(),
            self.common_face(),
            ~self.transporter(),
        )

    def _repr_(self):
        return f"Reduction-cell adjacency {self.source()} -> {self.target()}"


class ReductionFaceIncidence(SageObject):
    r"""One exact face inclusion inside a rational reduction cell.

    The incidence retains both mathematical cells and, when requested through
    ``face_incidences`` of the cell, the subgroup preserving the pair.  It is
    therefore stronger than a dimension pair or an engine face index and can
    be transported through the lattice action without losing the actual
    embedded face.
    """

    def __init__(self, face, cell, stabilizer) -> None:
        if face.ambient_lattice() is not cell.ambient_lattice() or not face.is_face_of(cell):
            raise ValueError("a reduction-face incidence is an actual face inclusion")
        self._face = face
        self._cell = cell
        self._stabilizer = stabilizer

    def face(self):
        return self._face

    def cell(self):
        return self._cell

    def lattice(self):
        return self.cell().ambient_lattice()

    def stabilizer(self):
        return self._stabilizer

    def codimension(self):
        return self.cell().dimension() - self.face().dimension()

    def transported_by(self, isometry):
        transported_cell = self.cell().transport(isometry)
        transported_face = self.face().transport(isometry)
        return ReductionFaceIncidence(
            transported_face,
            transported_cell,
            transported_cell.face_stabilizer(
                transported_face, self.stabilizer().supergroup()
            ),
        )

    def _repr_(self):
        return f"Reduction-face incidence {self.face()} <= {self.cell()}"


class MarkedReductionCell(SageObject):
    r"""A rational reduction cell with a labelled finite family of marked vectors.

    The marks are part of the object, not a set of vectors: labels and repeated
    values are retained.  Every mark is a nonzero-norm vector of the ambient
    lattice, which is the marked reduction problem used for nonisotropic vector
    orbit traversal.
    """

    def __init__(self, cell, marked_vectors) -> None:
        assert cell in RationalPolyhedralCones(), (
            "a marked reduction cell is a rational polyhedral cone with marks"
        )
        assert marked_vectors.cardinality().is_finite(), (
            "a marked reduction cell has a finite indexed family of marks"
        )
        lattice = cell.ambient_lattice()
        for vector in marked_vectors:
            if vector.parent() is not lattice:
                raise ValueError("every marked vector belongs to the cell's ambient lattice")
            if lattice.q(vector) == lattice.base_ring().zero():
                raise ValueError("a marked reduction vector has nonzero norm")
        self._cell = cell
        self._marked_vectors = marked_vectors

    def lattice(self):
        return self.cell().ambient_lattice()

    def cell(self):
        return self._cell

    def marked_vectors(self):
        return self._marked_vectors

    def transported_by(self, isometry):
        r"""Transport the cell and every labelled mark by the same isometry."""
        marks = self.marked_vectors()
        transported_marks = finite_indexed_family(
            marks.index_set(),
            lambda label: isometry(marks[label]),
            name=f"Transported marks of {self}",
        )
        return MarkedReductionCell(
            self.cell().transport(isometry),
            transported_marks,
        )

    def is_equal_to(self, other) -> bool:
        r"""Return whether ``other``, a marked cell of the same lattice, has the same cell and the same labelled marks."""
        if not self.cell().is_equal_to(other.cell()):
            return False
        same_marks = self.marked_vectors() == other.marked_vectors()
        return same_marks is True

    def transporter_witness_to(self, other, group):
        r"""Return a finite-group element transporting both cell and labelled marks."""
        if other.lattice() is not self.lattice():
            return None
        group_cardinality = group.cardinality()
        assert group_cardinality.is_finite(), (
            "marked-cell transport requires a finite represented acting group; "
            "infinite arithmetic traversal belongs to the reduction-complex provider"
        )
        for isometry in group:
            if self.transported_by(isometry).is_equal_to(other):
                return isometry
        return None

    def stabilizer(self, group):
        r"""Return the subgroup preserving both the cell and every labelled mark."""
        if group.domain() is not self.lattice() or group.codomain() is not self.lattice():
            raise ValueError("a marked-cell stabilizer acts on the ambient lattice")

        def preserves_marked_cell(isometry):
            return self.transported_by(isometry).is_equal_to(self)

        return group.predicate_subgroup(preserves_marked_cell, f"g preserves the marked reduction cell {self}")

    def adjacency_to(self, other, group):
        r"""Return the marked adjacency when one isometry transports all retained data."""
        underlying = self.cell().adjacency_to(other.cell(), group)
        if underlying is None:
            return None
        transporter = self.transporter_witness_to(other, group)
        if transporter is None:
            return None
        return MarkedReductionCellAdjacency(self, other, underlying, transporter)

    def _repr_(self):
        return (
            f"Marked {self.cell()} with {self.marked_vectors().cardinality()} "
            "labelled vectors"
        )


class MarkedReductionCellAdjacency(SageObject):
    r"""An oriented adjacency of marked cells with one common transporter."""

    def __init__(self, source, target, cell_adjacency, transporter) -> None:
        if cell_adjacency.source() is not source.cell() or cell_adjacency.target() is not target.cell():
            raise ValueError("the underlying adjacency joins the wrong reduction cells")
        if not source.transported_by(transporter).is_equal_to(target):
            raise ValueError("the retained transporter does not move the marked source to the target")
        self._source = source
        self._target = target
        self._cell_adjacency = cell_adjacency
        self._transporter = transporter

    def source(self):
        return self._source

    def target(self):
        return self._target

    def lattice(self):
        return self.source().lattice()

    def underlying_adjacency(self):
        return self._cell_adjacency

    def common_face(self):
        return self.underlying_adjacency().common_face()

    def transporter(self):
        return self._transporter

    def reversed(self):
        return MarkedReductionCellAdjacency(
            self.target(),
            self.source(),
            self.underlying_adjacency().reversed(),
            ~self.transporter(),
        )

    def _repr_(self):
        return f"Marked reduction-cell adjacency {self.source()} -> {self.target()}"


def _unpaired_facets(cells, incident_faces_of):
    r"""The facets of the stated cells that no adjacency face accounts for."""
    unpaired = []
    for cell in cells:
        incident_faces = incident_faces_of(cell)
        for facet in cell.facets():
            if not any(facet.is_equal_to(face) for face in incident_faces):
                unpaired.append(facet)
    return finite_ordered_set(tuple(unpaired))


class RationalReductionComplexExploration(SageObject):
    r"""A finite exact exploration of a rational reduction complex.

    The object retains actual cells and oriented adjacency records.  It is a
    *complete* exploration only when every irredundant facet of every retained
    cell occurs as the common face of one retained adjacency.  Merely stopping
    a traversal therefore never turns a finite prefix into a complete domain.
    """

    def __init__(self, lattice, cells, adjacencies, *, complete=False) -> None:
        cells = finite_ordered_set(tuple(cells))
        if cells.cardinality() == 0:
            raise ValueError("a reduction-complex exploration has at least one cell")
        if any(cell.ambient_lattice() is not lattice for cell in cells):
            raise ValueError("all reduction-complex cells lie in one lattice")
        adjacencies = finite_ordered_set(tuple(adjacencies))
        for adjacency in adjacencies:
            if adjacency.lattice() is not lattice:
                raise ValueError("an adjacency lies in the wrong lattice")
            if adjacency.source() not in cells or adjacency.target() not in cells:
                raise ValueError("an adjacency joins retained cells of this exploration")
        self._lattice = lattice
        self._cells = cells
        self._adjacencies = adjacencies
        self._complete = bool(complete)
        if self._complete and self.unpaired_facets().cardinality() != 0:
            raise ValueError(
                "a complete reduction-complex exploration accounts for every retained cell facet"
            )

    def lattice(self):
        return self._lattice

    def cells(self):
        return self._cells

    def adjacencies(self):
        return self._adjacencies

    def is_complete(self) -> bool:
        return self._complete

    def unpaired_facets(self):
        r"""Return the retained cell facets not represented by an adjacency."""
        return _unpaired_facets(
            self.cells(),
            lambda cell: tuple(
                adjacency.common_face()
                for adjacency in self.adjacencies()
                if adjacency.source() is cell or adjacency.target() is cell
            ),
        )

    def adjacency_transporters(self):
        r"""Return the retained oriented cell transporters, preserving edge labels."""
        adjacencies = self.adjacencies()
        return finite_indexed_family(
            adjacencies,
            lambda adjacency: adjacency.transporter(),
            name=f"Adjacency transporters of {self}",
        )

    def generation_subgroup(self, group):
        r"""Return the subgroup generated by cell stabilizers and edge transporters.

        This is exposed only for a complete exploration and a finite represented
        acting group, where every cell stabilizer can be listed exactly.  An
        incomplete prefix is not a group-generation certificate.
        """
        if not self.is_complete():
            raise ValueError(
                "an incomplete reduction-complex exploration is not a group-generation proof"
            )
        if group.domain() is not self.lattice() or group.codomain() is not self.lattice():
            raise ValueError("the reduction-complex group acts on its ambient lattice")
        assert group.cardinality().is_finite(), (
            "group generation from the represented complete reduction complex requires a finite acting group; "
            "infinite arithmetic generation belongs to the traversal provider"
        )
        generators = []
        for cell in self.cells():
            stabilizer = cell.stabilizer(group)
            generators.extend(element for element in group if element in stabilizer)
        generators.extend(self.adjacency_transporters())
        return group.subgroup(generators)

    def generation_is_full(self, group) -> bool:
        r"""Whether the complete finite exploration generates the supplied finite group."""
        generated = self.generation_subgroup(group)
        return generated.cardinality() == group.cardinality()

    def _repr_(self):
        status = "complete" if self.is_complete() else "finite-prefix"
        return (
            f"{status} rational reduction-complex exploration with "
            f"{self.cells().cardinality()} cells in {self.lattice()}"
        )


class PerfectDomainOrbitAdjacency(SageObject):
    r"""One quotient adjacency in a complete Lorentzian perfect-domain traversal.

    The source is a selected orbit representative.  Flipping its retained
    facet produces ``neighbor``.  The backend then identifies that actual
    neighbor with the selected representative ``target`` of its orbit.  The
    source and target representatives need not themselves be adjacent or lie
    in the same orbit, so this is deliberately not a ``ReductionCellAdjacency``.
    """

    def __init__(
        self,
        source,
        target,
        neighbor,
        common_face,
        target_to_neighbor,
    ) -> None:
        lattice = source.ambient_lattice()
        if any(cell.ambient_lattice() is not lattice for cell in (target, neighbor, common_face)):
            raise ValueError("a perfect-domain adjacency lies in one ambient lattice")
        if not common_face.is_face_of(source) or not common_face.is_face_of(neighbor):
            raise ValueError("the retained perfect-domain face is not common to source and neighbor")
        if not target.transport(target_to_neighbor).is_equal_to(neighbor):
            raise ValueError("the retained orbit equivalence does not map target representative to neighbor")
        self._source = source
        self._target = target
        self._neighbor = neighbor
        self._common_face = common_face
        self._target_to_neighbor = target_to_neighbor

    def source(self):
        return self._source

    def target_representative(self):
        return self._target

    def neighbor(self):
        return self._neighbor

    def common_face(self):
        return self._common_face

    def target_to_neighbor(self):
        return self._target_to_neighbor

    def neighbor_to_target(self):
        return ~self.target_to_neighbor()


class LorentzianPerfectDomainTraversal(SageObject):
    r"""A completed orbit traversal of Lorentzian perfect domains.

    The provider returns only after every adjacency has been processed.  The
    stored generator family is exactly the family used upstream to reconstruct
    ``O(L)``: stabilizer generators of every orbit representative together
    with one equivalence matrix for every quotient adjacency.
    """

    def __init__(self, lattice, cells, adjacencies, stabilizer_generators) -> None:
        self._lattice = lattice
        self._cells = finite_ordered_set(tuple(cells))
        self._adjacencies = finite_ordered_set(tuple(adjacencies))
        self._stabilizer_generators = stabilizer_generators
        if self._cells.cardinality() == 0:
            raise ValueError("a completed perfect-domain traversal has an orbit representative")
        if any(cell.ambient_lattice() is not lattice for cell in self._cells):
            raise ValueError("perfect-domain representatives lie in the traversed lattice")
        if any(adjacency.source() not in self._cells for adjacency in self._adjacencies):
            raise ValueError("a quotient adjacency starts at a retained representative")
        if any(
            adjacency.target_representative() not in self._cells
            for adjacency in self._adjacencies
        ):
            raise ValueError("a quotient adjacency targets a retained representative orbit")
        if self.unpaired_facets().cardinality() != 0:
            raise ValueError(
                "a completed perfect-domain traversal must account for every facet of every orbit representative"
            )

    def lattice(self):
        return self._lattice

    def cells(self):
        return self._cells

    def adjacencies(self):
        return self._adjacencies

    def is_complete(self) -> bool:
        return True

    def unpaired_facets(self):
        r"""Return representative facets missing from the quotient adjacency list.

        A provider result is complete only when every irredundant facet of
        every retained orbit representative occurs as the source-side common
        face of a quotient adjacency.  This check prevents a finite traversal
        prefix from being promoted to a complete reduction domain merely
        because it used the ``total`` provider entry point.
        """
        return _unpaired_facets(
            self.cells(),
            lambda cell: tuple(
                adjacency.common_face()
                for adjacency in self.adjacencies()
                if adjacency.source() is cell
            ),
        )

    def cell_stabilizer_generators(self, cell):
        if cell not in self.cells():
            raise ValueError("the selected cell is not a representative of this traversal")
        return self._stabilizer_generators[cell]

    def group_generators(self):
        generators = []
        for cell in self.cells():
            generators.extend(self.cell_stabilizer_generators(cell))
        generators.extend(
            adjacency.target_to_neighbor() for adjacency in self.adjacencies()
        )
        return finite_ordered_set(tuple(generators))

    def generation_subgroup(self):
        r"""Return the subgroup generated by cell stabilizers and edge pairings.

        For a complete connected reduction-domain traversal this is the
        standard generation theorem: vertex stabilizers together with one
        side-pairing for every quotient adjacency generate the full arithmetic
        group acting on the complex.  The subgroup is retained explicitly so
        downstream consumers use the actual live generators rather than a
        boolean completeness flag.
        """
        return self.lattice().O().subgroup(self.group_generators())

    def generates_orthogonal_group(self) -> bool:
        r"""Return ``True`` for this completed perfect-domain traversal.

        Construction of this object has already verified that every facet of
        every orbit representative is paired.  Together with the provider's
        completed orbit traversal, the reduction-complex generation theorem
        identifies :meth:`generation_subgroup` with ``O(L)``.  Finite-prefix
        objects are represented by :class:`RationalReductionComplexExploration`
        and deliberately do not have this unconditional conclusion.
        """
        return self.unpaired_facets().cardinality() == 0


def _row_action_from_ray_permutation(rays, permutation):
    r"""Recover the integral row-action matrix realizing one ray permutation."""
    rows = tuple(tuple(SageQQ(entry) for entry in ray) for ray in rays)
    if len(permutation) != len(rows):
        raise ArithmeticError("a perfect-domain stabilizer permutation has the wrong degree")
    ext = engine_matrix(SageQQ, rows)
    pivot_rows = tuple(ext.transpose().pivots())
    if len(pivot_rows) != ext.ncols():
        raise ArithmeticError("a perfect-domain ray family does not span the ambient lattice")
    basis = engine_matrix(SageQQ, tuple(rows[index] for index in pivot_rows))
    image_basis = engine_matrix(
        SageQQ,
        tuple(rows[int(permutation[index])] for index in pivot_rows),
    )
    action = basis.inverse() * image_basis
    permuted = engine_matrix(
        SageQQ,
        tuple(rows[int(permutation[index])] for index in range(len(rows))),
    )
    if ext * action != permuted:
        raise ArithmeticError("a serialized perfect-domain permutation is not linear on its rays")
    if any(entry.denominator() != 1 for entry in action.list()):
        raise ArithmeticError("a perfect-domain stabilizer permutation is not integral")
    return tuple(
        tuple(SageZZ(entry) for entry in action.row(index))
        for index in range(action.nrows())
    )


def _perfect_domain_traversal_from_records(lattice, records):
    r"""Cross full-adjacency provider records into one completed owned traversal."""
    records = tuple(records)
    if not records:
        raise ArithmeticError("the perfect-domain provider returned no orbit representatives")
    cones = RationalPolyhedralCones()
    raw_rays = tuple(
        tuple(tuple(SageZZ(entry) for entry in row) for row in record["x"]["EXT"])
        for record in records
    )
    cells = tuple(cones.from_rays(lattice, tuple(lattice(row) for row in rays)) for rays in raw_rays)
    orthogonal_group = lattice.O()
    stabilizer_by_cell = {}
    for cell, rays, record in zip(cells, raw_rays, records, strict=True):
        stabilizer_by_cell[cell] = finite_ordered_set(
            tuple(
                orthogonal_group._from_backend_row_action(
                    _row_action_from_ray_permutation(rays, permutation)
                )
                for permutation in record["x"]["GRP"]
            )
        )
    stabilizers = finite_indexed_family(
        finite_ordered_set(cells),
        lambda cell: stabilizer_by_cell[cell],
        name=f"Perfect-domain stabilizer generators in {lattice}",
    )
    adjacencies = []
    for source_index, record in enumerate(records):
        source = cells[source_index]
        source_rays = raw_rays[source_index]
        for adjacency_record in record["ListAdj"]:
            target_index = int(adjacency_record["iOrb"])
            if target_index < 0 or target_index >= len(cells):
                raise ArithmeticError("a perfect-domain adjacency targets an unknown orbit")
            target = cells[target_index]
            target_rays = raw_rays[target_index]
            row_action = tuple(
                tuple(SageZZ(entry) for entry in row)
                for row in adjacency_record["x"]["eBigMat"]
            )
            target_to_neighbor = orthogonal_group._from_backend_row_action(row_action)
            neighbor_rays = tuple(target_to_neighbor(lattice(row)) for row in target_rays)
            neighbor = cones.from_rays(lattice, neighbor_rays)
            incidence = tuple(int(value) for value in adjacency_record["x"]["eInc"])
            if len(incidence) != len(source_rays):
                raise ArithmeticError("a perfect-domain facet incidence has the wrong length")
            face_rays = tuple(
                lattice(ray) for ray, selected in zip(source_rays, incidence, strict=True) if selected
            )
            common_face = cones.from_rays(lattice, face_rays)
            adjacencies.append(
                PerfectDomainOrbitAdjacency(
                    source,
                    target,
                    neighbor,
                    common_face,
                    target_to_neighbor,
                )
            )
    return LorentzianPerfectDomainTraversal(
        lattice,
        cells,
        adjacencies,
        stabilizers,
    )


def _lorentzian_reduction_complex(lattice, marked_vectors=None):
    r"""Return the completed Lorentzian perfect-domain traversal of ``lattice``.

    The external provider works in signature ``(n,1)``.  Negating a form of
    signature ``(1,n)`` changes no integral orthogonal-group element and no
    lattice-coordinate ray, so only the private engine Gram matrix is negated.
    A marked perfect-domain traversal is a different arithmetic operation: the
    local marked-cell objects above do not turn an unmarked traversal into the
    orbit decomposition of marked cells.
    """
    assert marked_vectors is None, (
        "the registered perfect-domain provider enumerates unmarked Lorentzian domains; "
        "marked nonzero-norm traversal requires a provider that traverses the marked cells themselves"
    )
    signature = lattice.signature_pair()
    positive = signature.first()
    negative = signature.second()
    gram = _engine_component_matrix(lattice.gram_tensor()).change_ring(SageZZ)
    match int(positive), int(negative):
        case _, 1:
            engine_gram = gram
        case 1, _:
            engine_gram = -gram
        case _:
            raise ValueError("a Lorentzian perfect-domain traversal requires signature (1,n) or (n,1)")
    records = engine_capabilities.compute(
        "lattice.lorentzian_perfect_domain_traversal",
        [list(row) for row in engine_gram.rows()],
        "total",
    )
    return _perfect_domain_traversal_from_records(lattice, records)


__all__ = [
    "LorentzianPerfectDomainTraversal",
    "MarkedReductionCell",
    "MarkedReductionCellAdjacency",
    "PerfectDomainOrbitAdjacency",
    "RationalReductionComplexExploration",
    "ReductionFaceIncidence",
    "ReductionCellAdjacency",
]
