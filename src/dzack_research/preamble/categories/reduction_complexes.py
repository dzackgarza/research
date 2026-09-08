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


def rational_reduction_cell(lattice, inequalities, *, equations=()):
    r"""Return the homogeneous rational cell cut out by the selected walls."""
    return RationalReductionCell(lattice, inequalities, equations=equations)


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
    "RationalReductionCell",
    "lorentzian_reduction_complex",
    "rational_reduction_cell",
]
