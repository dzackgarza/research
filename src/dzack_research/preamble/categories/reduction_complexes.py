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
from sage.modules.free_module_element import vector as sage_vector
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.group.predicate_subgroups import (
    predicate_subgroup,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
)
from dzack_research.preamble.tensors import tensor
from dzack_research.preamble.tensors.tensor import _engine_component_matrix


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

    def transporter_witness_to(self, other, group):
        r"""Return one element of a finite represented group carrying this cell to ``other``.

        This is the exact local transporter operation used by a reduction
        complex once a finite cell-stabilizer/quotient group is represented.
        Infinite arithmetic traversal remains the separate provider obligation
        of :func:`lorentzian_reduction_complex`.
        """
        if other.lattice() is not self.lattice():
            return None
        if group.domain() is not self.lattice() or group.codomain() is not self.lattice():
            raise ValueError("a cell transporter group acts on the ambient lattice")
        group_cardinality = group.cardinality()
        if not group_cardinality.is_finite():
            raise NotImplementedError(
                "cell transporter search through an infinite arithmetic group belongs to the reduction-complex traversal provider"
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

        return predicate_subgroup(
            group,
            preserves_cell,
            f"g preserves the rational reduction cell {self}",
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
        if not group_cardinality.is_finite():
            raise NotImplementedError(
                "marked-cell transport through an infinite arithmetic group belongs to the reduction-complex traversal provider"
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

        return predicate_subgroup(
            group,
            preserves_marked_cell,
            f"g preserves the marked reduction cell {self}",
        )

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
        if not group.cardinality().is_finite():
            raise NotImplementedError(
                "arithmetic-group generation from a complete Lorentzian reduction complex belongs to the traversal provider"
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


def rational_reduction_complex_exploration(
    lattice,
    cells,
    adjacencies,
    *,
    complete=False,
):
    r"""Return the finite exact reduction-complex exploration on the selected data."""
    return RationalReductionComplexExploration(
        lattice,
        cells,
        adjacencies,
        complete=complete,
    )


def rational_reduction_cell(lattice, inequalities, *, equations=()):
    r"""Return the homogeneous rational cell cut out by the selected walls."""
    return RationalReductionCell(lattice, inequalities, equations=equations)


def marked_reduction_cell(cell, marked_vectors):
    r"""Return ``cell`` equipped with the selected finite indexed family of marks."""
    return MarkedReductionCell(cell, marked_vectors)


def lorentzian_reduction_complex(lattice, marked_vectors=None):
    r"""Return the reduction complex of ``lattice``, optionally with marked vectors."""
    assert False, (
        f"the reduction complex of {lattice} is not computed: its cells are the "
        "perfect domains of Opgenorth's indefinite reduction, and no provider "
        "registered in the capability layer traverses them; the port that "
        "would supply one is sage-indefinite-port.  For "
        "generators of O(L) use L.O().group_generators(), for vector orbits "
        "use L.O().vector_orbit_representatives(square), and for the "
        f"Lorentzian component character use L.positive_cone_subgroup(); the "
        f"marked family {marked_vectors} would only be needed by the traversal "
        "this absence names"
    )


__all__ = [
    "MarkedReductionCell",
    "MarkedReductionCellAdjacency",
    "RationalReductionComplexExploration",
    "ReductionCellAdjacency",
    "RationalReductionCell",
    "lorentzian_reduction_complex",
    "marked_reduction_cell",
    "rational_reduction_cell",
    "rational_reduction_complex_exploration",
]
