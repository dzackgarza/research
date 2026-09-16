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

from sage.geometry.polyhedron.constructor import Polyhedron
from sage.matrix.constructor import matrix as engine_matrix
from sage.modules.free_module_element import vector as sage_vector
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
)
from dzack_research.preamble.engine_capabilities import engine_capabilities
from dzack_research.preamble.tensors.tensor import _engine_component_matrix, tensor


def _coordinates(vector):
    components = getattr(vector, "components", None)
    if callable(components):
        return tuple(components())
    return tuple(vector)


def _owned_rational_vector(entries):
    rationals = _own_ring(SageQQ)
    return tensor.vector(
        rationals,
        [rationals._from_engine_element(SageQQ(entry)) for entry in entries],
    )


def _engine_rational_vector(vector):
    return sage_vector(SageQQ, [SageQQ(entry) for entry in _coordinates(vector)])


def _ray_key(entries):
    entries = tuple(SageQQ(entry) for entry in entries)
    first = next((entry for entry in entries if entry != 0), None)
    if first is None:
        raise ValueError("the zero vector does not define a ray")
    scale = abs(first)
    return tuple(entry / scale for entry in entries)


def _line_key(entries):
    entries = tuple(SageQQ(entry) for entry in entries)
    first = next((entry for entry in entries if entry != 0), None)
    if first is None:
        raise ValueError("the zero vector does not define a line")
    return tuple(entry / first for entry in entries)


class RationalReductionCell(SageObject):
    r"""An exact homogeneous rational polyhedral cell in lattice coordinates.

    The public definition is its finite family of rational wall covectors and
    linear equations.  Sage's exact polyhedral engine is private and supplies
    irredundant facets, extreme rays, intersections, and dimensions.  All
    inequalities use the convention ``a(x) >= 0``.
    """

    def __init__(self, lattice, inequalities, *, equations=()) -> None:
        self._lattice = lattice
        rank = int(lattice.module_rank())
        self._inequalities = finite_ordered_set(
            tuple(_owned_rational_vector(_coordinates(wall)) for wall in inequalities)
        )
        self._equations = finite_ordered_set(
            tuple(_owned_rational_vector(_coordinates(wall)) for wall in equations)
        )
        for wall in tuple(self._inequalities) + tuple(self._equations):
            if len(_coordinates(wall)) != rank:
                raise ValueError("a reduction-cell wall has the lattice rank")
        self._engine = Polyhedron(
            ieqs=[[0, *map(SageQQ, _coordinates(wall))] for wall in self._inequalities],
            eqns=[[0, *map(SageQQ, _coordinates(wall))] for wall in self._equations],
            base_ring=SageQQ,
        )
        if not self._engine.contains(sage_vector(SageQQ, [0] * rank)):
            raise ArithmeticError("a homogeneous reduction cell must contain the origin")

    @classmethod
    def _from_engine(cls, lattice, polyhedron):
        if any(inequality.b() != 0 for inequality in polyhedron.inequalities()):
            raise ArithmeticError("a reduction-cell intersection acquired an affine inequality")
        if any(equation.b() != 0 for equation in polyhedron.equations()):
            raise ArithmeticError("a reduction-cell intersection acquired an affine equation")
        inequalities = tuple(
            _owned_rational_vector(inequality.A())
            for inequality in polyhedron.inequalities()
        )
        equations = tuple(
            _owned_rational_vector(equation.A())
            for equation in polyhedron.equations()
        )
        return cls(lattice, inequalities, equations=equations)

    @classmethod
    def from_rays(cls, lattice, rays):
        r"""Return the exact homogeneous cell generated by the selected rational rays."""
        rows = tuple(tuple(SageQQ(entry) for entry in _coordinates(ray)) for ray in rays)
        if not rows:
            raise ValueError("a ray-presented reduction cell requires at least one ray")
        return cls._from_engine(
            lattice,
            Polyhedron(rays=rows, base_ring=SageQQ),
        )

    def lattice(self):
        return self._lattice

    def inequalities(self):
        return self._inequalities

    def equations(self):
        return self._equations

    def dimension(self):
        return int(self._engine.dim())

    def ambient_dimension(self):
        return int(self.lattice().module_rank())

    def facets(self):
        r"""Return the irredundant facet-defining covectors."""
        return finite_ordered_set(
            tuple(
                _owned_rational_vector(inequality.A())
                for inequality in self._engine.inequalities()
            )
        )

    def faces(self, dimension):
        r"""Return the exact faces of the selected dimension.

        Faces are returned as reduction cells in the same ambient lattice, so
        incidences, stabilizers and transporters use the same mathematical
        carrier as the ambient cell rather than private engine face handles.
        """
        dimension = int(dimension)
        if dimension < 0 or dimension > self.dimension():
            return finite_ordered_set(())
        return finite_ordered_set(
            tuple(
                RationalReductionCell._from_engine(
                    self.lattice(), face.as_polyhedron()
                )
                for face in self._engine.faces(dimension)
            )
        )

    def facet(self, wall):
        r"""Return the codimension-one face cut out by one irredundant wall."""
        wall = _owned_rational_vector(_coordinates(wall))
        wall_key = _ray_key(_coordinates(wall))
        if all(
            _ray_key(_coordinates(candidate)) != wall_key
            for candidate in self.facets()
        ):
            raise ValueError("the selected covector is not an irredundant facet wall")
        return RationalReductionCell(
            self.lattice(),
            tuple(self.inequalities()),
            equations=tuple(self.equations()) + (wall,),
        )

    def extreme_rays(self):
        r"""Return the exact extreme rays in the chosen lattice coordinates."""
        return finite_ordered_set(
            tuple(_owned_rational_vector(ray) for ray in self._engine.rays())
        )

    def lineality_generators(self):
        r"""Return exact generators of the cell's linear lineality space."""
        return finite_ordered_set(
            tuple(_owned_rational_vector(line) for line in self._engine.lines())
        )

    def contains(self, vector) -> bool:
        return bool(self._engine.contains(_engine_rational_vector(vector)))

    def intersection(self, other):
        if other.lattice() is not self.lattice():
            raise ValueError("reduction cells are intersected in one ambient lattice")
        return RationalReductionCell._from_engine(
            self.lattice(), self._engine.intersection(other._engine)
        )

    def is_equal_to(self, other) -> bool:
        r"""Return whether two cells are the same exact rational polyhedral cone."""
        return (
            isinstance(other, RationalReductionCell)
            and other.lattice() is self.lattice()
            and self._engine == other._engine
        )

    def transported_by(self, isometry):
        r"""Return the image of this cell under a lattice isometry.

        If ``C`` is cut out by row covectors ``a`` with ``a(x) >= 0`` and
        ``g`` has coordinate matrix ``M`` (column-image convention), then
        ``g(C)`` is cut out by ``a M^{-1}``, since ``a(M^{-1}y) >= 0`` is the
        transported inequality.  Equations transform by the same rule.
        """
        lattice = self.lattice()
        if isometry.domain() is not lattice or isometry.codomain() is not lattice:
            raise ValueError("a reduction cell is transported by an automorphism of its lattice")
        inverse = _engine_component_matrix(isometry.matrix()).change_ring(SageQQ).inverse()

        def transported(covector):
            return _owned_rational_vector(_engine_rational_vector(covector) * inverse)

        return RationalReductionCell(
            lattice,
            tuple(transported(wall) for wall in self.inequalities()),
            equations=tuple(transported(wall) for wall in self.equations()),
        )

    def with_marks(self, marked_vectors):
        r"""Return this cell equipped with the selected labelled finite family of marks."""
        return MarkedReductionCell(self, marked_vectors)

    def transporter_witness_to(self, other, group):
        r"""Return one element of a finite represented group carrying this cell to ``other``.

        This is the exact local transporter operation used by a reduction
        complex once a finite cell-stabilizer/quotient group is represented.
        Infinite arithmetic traversal remains the separate provider obligation
        of the ambient lattice's ``lorentzian_reduction_complex`` method.
        """
        if other.lattice() is not self.lattice():
            return None
        if group.domain() is not self.lattice() or group.codomain() is not self.lattice():
            raise ValueError("a cell transporter group acts on the ambient lattice")
        group_cardinality = group.cardinality()
        assert group_cardinality.is_finite(), (
            "cell transporter search requires a finite represented acting group; "
            "infinite arithmetic traversal belongs to the reduction-complex provider"
        )
        for isometry in group:
            if self.transported_by(isometry).is_equal_to(other):
                return isometry
        return None

    def adjacency_to(self, other, group):
        r"""Return the exact adjacent-cell record from this cell to ``other``.

        The record exists only when the two cells share a codimension-one face
        and the supplied represented group contains an isometry carrying the
        source cell to the target cell.  It retains the common face and the
        transporter as mathematical objects rather than recomputing either
        from incidence labels later.
        """
        if not self.is_adjacent_to(other):
            return None
        transporter = self.transporter_witness_to(other, group)
        if transporter is None:
            return None
        return ReductionCellAdjacency(
            self,
            other,
            self.intersection(other),
            transporter,
        )

    def is_face_of(self, other) -> bool:
        if other.lattice() is not self.lattice():
            return False
        return any(
            face.as_polyhedron() == self._engine
            for face in other._engine.faces(self.dimension())
        )

    def is_adjacent_to(self, other) -> bool:
        if other.lattice() is not self.lattice():
            return False
        common = self.intersection(other)
        return (
            common.dimension() == self.dimension() - 1
            and common.dimension() == other.dimension() - 1
            and common.is_face_of(self)
            and common.is_face_of(other)
        )

    def stabilizer(self, group):
        r"""Return the subgroup preserving this cone setwise."""
        if group.domain() is not self.lattice() or group.codomain() is not self.lattice():
            raise ValueError("a reduction-cell stabilizer acts on the ambient lattice")
        ray_keys = frozenset(_ray_key(ray) for ray in self.extreme_rays())
        line_keys = frozenset(
            _line_key(line) for line in self.lineality_generators()
        )

        def preserves_cell(isometry):
            matrix = _engine_component_matrix(isometry.matrix()).change_ring(SageQQ)
            transformed_rays = frozenset(
                _ray_key(matrix * _engine_rational_vector(ray))
                for ray in self.extreme_rays()
            )
            transformed_lines = frozenset(
                _line_key(matrix * _engine_rational_vector(line))
                for line in self.lineality_generators()
            )
            return transformed_rays == ray_keys and transformed_lines == line_keys

        return group.predicate_subgroup(preserves_cell, f"g preserves the rational reduction cell {self}")

    def face_stabilizer(self, face, group):
        r"""Return the subgroup preserving this cell and ``face`` setwise.

        This is the cell-face stabilizer occurring in reduction-complex group
        generation.  Requiring membership in the cell stabilizer is essential:
        the ambient orthogonal group may preserve the lower-dimensional cone
        while moving the chosen perfect domain to another cell.
        """
        if not isinstance(face, RationalReductionCell) or not face.is_face_of(self):
            raise ValueError("a face stabilizer is attached to an actual face of this cell")
        cell_stabilizer = self.stabilizer(group)
        face_stabilizer = face.stabilizer(group)
        return cell_stabilizer.intersection(face_stabilizer)

    def face_incidences(self, dimension, group):
        r"""Return the represented incidences with faces of ``dimension``.

        Every record owns the embedded face and the subgroup stabilizing the
        pair ``face <= cell``.  This is the incidence datum consumed by an
        exact reduction-complex traversal when assembling quotient cells.
        """
        faces = self.faces(dimension)
        return finite_indexed_family(
            faces,
            lambda face: ReductionFaceIncidence(
                face,
                self,
                self.face_stabilizer(face, group),
            ),
            name=f"Face incidences of dimension {dimension} in {self}",
        )

    def _repr_(self):
        return (
            f"{self.dimension()}-dimensional rational reduction cell in "
            f"{self.lattice()}"
        )


class ReductionCellAdjacency(SageObject):
    r"""An oriented adjacency of two rational reduction cells.

    It consists of the source cell, target cell, their actual common facet,
    and one lattice isometry carrying source to target.  Reversing the
    adjacency inverts that same transporter and preserves the shared face.
    """

    def __init__(self, source, target, common_face, transporter) -> None:
        if source.lattice() is not target.lattice():
            raise ValueError("adjacent reduction cells lie in one lattice")
        if common_face.lattice() is not source.lattice():
            raise ValueError("an adjacency face lies in the cells' ambient lattice")
        if not source.is_adjacent_to(target):
            raise ValueError("a reduction-cell adjacency requires a common facet")
        if not common_face.is_equal_to(source.intersection(target)):
            raise ValueError("the retained adjacency face is not the cells' intersection")
        if not source.transported_by(transporter).is_equal_to(target):
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
        return self.source().lattice()

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
    :meth:`RationalReductionCell.face_incidences`, the subgroup preserving the
    pair.  It is therefore stronger than a dimension pair or an engine face
    index and can be transported through the lattice action without losing the
    actual embedded face.
    """

    def __init__(self, face, cell, stabilizer) -> None:
        if face.lattice() is not cell.lattice() or not face.is_face_of(cell):
            raise ValueError("a reduction-face incidence is an actual face inclusion")
        self._face = face
        self._cell = cell
        self._stabilizer = stabilizer

    def face(self):
        return self._face

    def cell(self):
        return self._cell

    def lattice(self):
        return self.cell().lattice()

    def stabilizer(self):
        return self._stabilizer

    def codimension(self):
        return self.cell().dimension() - self.face().dimension()

    def transported_by(self, isometry):
        transported_cell = self.cell().transported_by(isometry)
        transported_face = self.face().transported_by(isometry)
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
        if not isinstance(cell, RationalReductionCell):
            raise TypeError("a marked reduction cell requires a rational reduction cell")
        if not isinstance(marked_vectors, IndexedFamily):
            raise TypeError("marked vectors are supplied as an owned indexed family")
        if marked_vectors.cardinality().is_finite() is not True:
            raise ValueError("a marked reduction cell has finitely many marks")
        lattice = cell.lattice()
        for vector in marked_vectors:
            if vector.parent() is not lattice:
                raise ValueError("every marked vector belongs to the cell's ambient lattice")
            if lattice.q(vector) == lattice.base_ring().zero():
                raise ValueError("a marked reduction vector has nonzero norm")
        self._cell = cell
        self._marked_vectors = marked_vectors

    def lattice(self):
        return self.cell().lattice()

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
            self.cell().transported_by(isometry),
            transported_marks,
        )

    def is_equal_to(self, other) -> bool:
        if not isinstance(other, MarkedReductionCell):
            return False
        if not self.cell().is_equal_to(other.cell()):
            return False
        same_marks = self.marked_vectors() == other.marked_vectors()
        return same_marks is True

    def transporter_witness_to(self, other, group):
        r"""Return a finite-group element transporting both cell and labelled marks."""
        if not isinstance(other, MarkedReductionCell):
            return None
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
        if not isinstance(other, MarkedReductionCell):
            return None
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
        if not isinstance(source, MarkedReductionCell) or not isinstance(
            target, MarkedReductionCell
        ):
            raise TypeError("a marked adjacency joins marked reduction cells")
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
        if any(cell.lattice() is not lattice for cell in cells):
            raise ValueError("all reduction-complex cells lie in one lattice")
        adjacencies = finite_ordered_set(tuple(adjacencies))
        for adjacency in adjacencies:
            if not isinstance(adjacency, ReductionCellAdjacency):
                raise TypeError("a reduction-complex edge is a ReductionCellAdjacency")
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
        unpaired = []
        for cell in self.cells():
            incident_faces = tuple(
                adjacency.common_face()
                for adjacency in self.adjacencies()
                if adjacency.source() is cell or adjacency.target() is cell
            )
            for wall in cell.facets():
                facet = cell.facet(wall)
                if not any(facet.is_equal_to(face) for face in incident_faces):
                    unpaired.append(facet)
        return finite_ordered_set(tuple(unpaired))

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
        lattice = source.lattice()
        if any(cell.lattice() is not lattice for cell in (target, neighbor, common_face)):
            raise ValueError("a perfect-domain adjacency lies in one ambient lattice")
        if not common_face.is_face_of(source) or not common_face.is_face_of(neighbor):
            raise ValueError("the retained perfect-domain face is not common to source and neighbor")
        if not target.transported_by(target_to_neighbor).is_equal_to(neighbor):
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
        if any(cell.lattice() is not lattice for cell in self._cells):
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
        missing = []
        for cell in self.cells():
            source_faces = tuple(
                adjacency.common_face()
                for adjacency in self.adjacencies()
                if adjacency.source() is cell
            )
            for wall in cell.facets():
                facet = cell.facet(wall)
                if not any(facet.is_equal_to(face) for face in source_faces):
                    missing.append(facet)
        return finite_ordered_set(tuple(missing))

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
    raw_rays = tuple(
        tuple(tuple(SageZZ(entry) for entry in row) for row in record["x"]["EXT"])
        for record in records
    )
    cells = tuple(
        RationalReductionCell.from_rays(lattice, rays)
        for rays in raw_rays
    )
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
            neighbor_rays = tuple(
                tuple(SageZZ(entry) for entry in target_to_neighbor(lattice(row)).to_tuple())
                for row in target_rays
            )
            neighbor = RationalReductionCell.from_rays(lattice, neighbor_rays)
            incidence = tuple(int(value) for value in adjacency_record["x"]["eInc"])
            if len(incidence) != len(source_rays):
                raise ArithmeticError("a perfect-domain facet incidence has the wrong length")
            face_rays = tuple(
                ray for ray, selected in zip(source_rays, incidence, strict=True) if selected
            )
            common_face = RationalReductionCell.from_rays(lattice, face_rays)
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
    "RationalReductionCell",
]
