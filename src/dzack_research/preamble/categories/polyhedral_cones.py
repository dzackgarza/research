r"""Exact rational polyhedral cones retained by homogeneous half-spaces."""

from sage.arith.functions import lcm
from sage.arith.misc import gcd
from sage.geometry.cone import Cone as SageCone
from sage.geometry.polyhedron.constructor import Polyhedron
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.element import parent as element_parent

from dzack_research.preamble.categories.abstract_categories.objects import OwnedParameterizedCategory
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of


def _primitive_integral_coordinates(coordinates):
    rationals = tuple(SageQQ(coordinate) for coordinate in coordinates)
    scale = lcm(tuple(coordinate.denominator() for coordinate in rationals))
    integers = tuple(SageZZ(scale * coordinate) for coordinate in rationals)
    content = gcd(tuple(abs(coordinate) for coordinate in integers if coordinate))
    if content == 0:
        return integers
    return tuple(coordinate // content for coordinate in integers)


def _owned_vector(module, coordinates):
    ring = module.base_ring()
    return module.linear_combination(
        {
            label: ring(int(coordinate))
            for label, coordinate in zip(module.module_generating_set(), coordinates, strict=True)
            if coordinate
        }
    )


def _integral_covector(lattice, coordinates):
    r"""The primitive integral covector of ``lattice`` on the ray of the rational ``coordinates``.

    A homogeneous half-space ``a(x) >= 0`` is unchanged by a positive
    rescaling of ``a``, so a rational covector is stated by the primitive
    integral covector on its ray.
    """
    return _owned_vector(lattice.dual_module(), _primitive_integral_coordinates(tuple(coordinates)))


def _ambient_vector(lattice, ambient, vector):
    r"""Read a lattice or rational-coordinate vector in ``lattice tensor QQ``."""
    match element_parent(vector):
        case parent if parent is ambient:
            return vector
        case parent if parent is lattice:
            coefficients = lattice.framing_coefficients(vector)
            rationals = ambient.base_ring()
            return ambient.linear_combination(
                {
                    label: rationals(coefficient)
                    for label, coefficient in coefficients.items()
                }
            )
        case _:
            return ambient(vector)


def _evaluate_covector(lattice, ambient, covector, vector):
    dual = lattice.dual_module()
    covector = dual(covector)
    vector = _ambient_vector(lattice, ambient, vector)
    rationals = ambient.base_ring()
    covector_coefficients = dual.framing_coefficients(covector)
    vector_coefficients = ambient.framing_coefficients(vector)
    return sum(
        (
            rationals(covector_coefficients.get(label, lattice.base_ring().zero()))
            * vector_coefficients.get(label, rationals.zero())
            for label in lattice.module_generating_set()
        ),
        rationals.zero(),
    )


def _cone_contains(lattice, ambient, halfspaces, equations, vector) -> bool:
    zero = ambient.base_ring().zero()
    return all(
        _evaluate_covector(lattice, ambient, covector, vector) >= zero
        for covector in halfspaces
    ) and all(
        _evaluate_covector(lattice, ambient, covector, vector) == zero
        for covector in equations
    )


def _cone_from_engine_polyhedron(lattice, polyhedron, wall_roots=None):
    r"""The cone whose homogeneous H-representation is that of Sage's exact ``polyhedron``.

    Private engine crossing of :meth:`RationalPolyhedralCones.from_rays` and
    of the cone operations that compute a new cone in the engine.
    """
    assert all(inequality.b() == 0 for inequality in polyhedron.inequalities()), (
        f"{polyhedron} is not a cone in {lattice}: a cone is cut out by homogeneous "
        f"inequalities, but some inequality has a nonzero constant term"
    )
    assert all(equation.b() == 0 for equation in polyhedron.equations()), (
        f"{polyhedron} is not a cone in {lattice}: a cone is cut out by homogeneous "
        f"equations, but some equation has a nonzero constant term"
    )
    return _rational_polyhedral_cone(
        lattice,
        tuple(_integral_covector(lattice, inequality.A()) for inequality in polyhedron.inequalities()),
        equation_covectors=tuple(
            _integral_covector(lattice, equation.A()) for equation in polyhedron.equations()
        ),
        wall_roots=wall_roots,
    )


class RationalPolyhedralCones(OwnedParameterizedCategory):
    r"""Rational polyhedral cones in a selected integral coordinate lattice.

    A cone is retained by homogeneous integral covectors ``ell`` defining
    ``ell(x) >= 0``.  Sage's exact polyhedral objects are private computation
    engines; the public object retains the ambient lattice and the covectors.
    """

    def parameter_category(self):
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            FramedFreeModules,
        )

        return FramedFreeModules(_own_ring(SageZZ))

    def ambient_lattice(self):
        return self.base()

    @cached_method
    def ambient_space(self):
        rationals = _own_ring(SageQQ)
        return rationals.free_module(self.ambient_lattice().module_generating_set())

    @classmethod
    def _repr_object_names(cls):
        return "rational polyhedral cones"

    def super_categories(self):
        return [Sets().Subobjects(self.ambient_space())]

    def an_object(self):
        dual = self.ambient_lattice().dual_module()
        return _rational_polyhedral_cone(
            self.ambient_lattice(),
            tuple(dual.module_generators()),
        )

    def from_rays(self, rays, *, wall_roots=None):
        r"""Return the cone generated by the rays in this category's lattice.

        The rays are nonzero vectors of ``lattice``; the half-spaces cutting
        the cone out are computed by the exact polyhedral engine.  The
        ``wall_roots``, when stated, are the roots of ``lattice`` whose
        mirrors contain the cone, so that
        :meth:`ParentMethods.reflection_group` is the subgroup of the
        reflection group fixing the cone pointwise.
        """
        lattice = self.ambient_lattice()
        labels = tuple(lattice.module_generating_set())
        zero = lattice.base_ring().zero()

        def engine_row(ray):
            coefficients = lattice.framing_coefficients(lattice(ray))
            return tuple(SageQQ(int(coefficients.get(label, zero))) for label in labels)

        rows = tuple(engine_row(ray) for ray in rays)
        return _cone_from_engine_polyhedron(
            lattice,
            Polyhedron(vertices=[(0,) * len(labels)], rays=rows, base_ring=SageQQ),
            wall_roots=wall_roots,
        )

    class ParentMethods:
        def __init__(
            self,
            lattice,
            halfspace_covectors,
            equation_covectors=(),
            wall_roots=None,
            complete=None,
            **rest,
        ):
            self._lattice = lattice
            dual = lattice.dual_module()
            self._halfspace_covectors = finite_ordered_set(
                tuple(dual(covector) for covector in halfspace_covectors)
            )
            self._equation_covectors = finite_ordered_set(
                tuple(dual(covector) for covector in equation_covectors)
            )
            self._wall_roots = None if wall_roots is None else finite_ordered_set(tuple(wall_roots))
            self._complete = complete
            labels = tuple(dual.module_generating_set())

            def engine_row(covector):
                coefficients = dual.framing_coefficients(covector)
                return [SageQQ.zero()] + [
                    SageQQ(int(coefficients.get(label, 0))) for label in labels
                ]

            rows = [engine_row(covector) for covector in self._halfspace_covectors]
            equations = [engine_row(covector) for covector in self._equation_covectors]
            self._engine = Polyhedron(ieqs=rows, eqns=equations, base_ring=SageQQ)
            super().__init__(**rest)

        def ambient_lattice(self):
            return self._lattice

        def ambient_space(self):
            return self.codomain()

        def halfspace_covectors(self):
            return self._halfspace_covectors

        def equation_covectors(self):
            return self._equation_covectors

        def wall_roots(self):
            return self._wall_roots

        def reflection_group(self):
            r"""Return the subgroup generated by reflections in the retained wall roots.

            This operation is available exactly when the cone was constructed
            from roots of its ambient lattice.  It uses those retained roots,
            not a second root enumeration.
            """
            if self._wall_roots is None:
                raise ValueError(
                    f"{self} has no reflection group: it was not constructed with the roots "
                    f"whose mirrors are its walls"
                )
            lattice = self.ambient_lattice()
            return lattice.O().subgroup(
                tuple(lattice.reflection(root) for root in self._wall_roots)
            )

        weyl_group = reflection_group

        def coxeter_diagram(self):
            r"""Return the exact Coxeter diagram determined by the retained wall roots."""
            if self._wall_roots is None:
                raise ValueError(
                    f"{self} has no Coxeter diagram: it was not constructed with the roots "
                    f"whose mirrors are its walls"
                )
            from dzack_research.preamble.categories.coxeter_diagrams import CoxeterDiagrams

            return CoxeterDiagrams().from_roots(tuple(self._wall_roots))

        def _transport_covector(self, covector, isometry):
            self.ambient_lattice()
            target = isometry.codomain()
            inverse = ~isometry
            target_dual = target.dual_module()
            return target_dual.linear_combination(
                {
                    label: self.evaluate_covector(
                        covector,
                        inverse(target.module_generator(label)),
                    )
                    for label in target.module_generating_set()
                }
            )

        def transport(self, isometry):
            r"""Transport this cone and all retained defining covectors along an isometry."""
            source = self.ambient_lattice()
            if isometry.domain() is not source:
                raise ValueError(
                    f"cannot transport {self} along {isometry}: the cone lies in {source}, "
                    f"but the isometry has domain {isometry.domain()}"
                )
            target = isometry.codomain()
            roots = None
            if self._wall_roots is not None:
                roots = tuple(isometry(root) for root in self._wall_roots)
            return _rational_polyhedral_cone(
                target,
                tuple(
                    self._transport_covector(covector, isometry)
                    for covector in self._halfspace_covectors
                ),
                equation_covectors=tuple(
                    self._transport_covector(covector, isometry)
                    for covector in self._equation_covectors
                ),
                wall_roots=roots,
                complete=self.is_complete_wall_set(),
            )

        def chamber_complex(self):
            r"""Return the lazy Weyl-chamber complex generated by this root chamber."""
            if self._wall_roots is None:
                raise ValueError(
                    f"{self} generates no Weyl chamber complex: it was not constructed with "
                    f"the roots whose mirrors are its walls"
                )
            from dzack_research.preamble.categories.chamber_complexes import (
                WeylChamberComplexes,
            )
            from dzack_research.preamble.owned_category import _object_of

            return _object_of(
                WeylChamberComplexes(),
                fundamental_chamber=self,
            )

        def is_complete_wall_set(self):
            return self._complete

        def _engine_polyhedron(self):
            return self._engine

        def dimension(self):
            return self.ambient_lattice().base_ring()(int(self._engine.dim()))

        def is_pointed(self) -> bool:
            return len(tuple(self._engine.lines())) == 0

        def evaluate_covector(self, covector, vector):
            return _evaluate_covector(
                self.ambient_lattice(),
                self.ambient_space(),
                covector,
                vector,
            )

        def contains(self, vector) -> bool:
            return _cone_contains(
                self.ambient_lattice(),
                self.ambient_space(),
                self.halfspace_covectors(),
                self.equation_covectors(),
                vector,
            )

        def primitive_rays(self):
            lattice = self.ambient_lattice()
            return finite_ordered_set(
                tuple(_owned_vector(lattice, _primitive_integral_coordinates(ray)) for ray in self._engine.rays())
            )

        def lineality_generators(self):
            lattice = self.ambient_lattice()
            return finite_ordered_set(
                tuple(_owned_vector(lattice, _primitive_integral_coordinates(line)) for line in self._engine.lines())
            )

        def face_on_covector(self, covector):
            r"""Intersect this cone with the homogeneous wall ``covector=0``."""
            dual = self.ambient_lattice().dual_module()
            covector = dual(covector)
            return _rational_polyhedral_cone(
                self.ambient_lattice(),
                tuple(self._halfspace_covectors),
                equation_covectors=tuple(self._equation_covectors) + (covector,),
                complete=self.is_complete_wall_set(),
            )

        def _covector_from_engine_hrepresentation(self, inequality):
            r"""Cross one private homogeneous H-row back to the owned dual lattice."""
            if inequality.b() != 0:
                raise ArithmeticError(
                    f"a face of {self} was computed with the inequality {inequality}, which "
                    f"has a nonzero constant term; a face of a cone is cut out by "
                    f"homogeneous inequalities"
                )
            dual = self.ambient_lattice().dual_module()
            coordinates = _primitive_integral_coordinates(inequality.A())
            return _owned_vector(dual, coordinates)

        def _face_from_engine_face(self, face):
            r"""Cross one nonempty engine face using its ambient active inequalities."""
            active = tuple(
                self._covector_from_engine_hrepresentation(relation)
                for relation in face.ambient_Hrepresentation()
            )
            return _rational_polyhedral_cone(
                self.ambient_lattice(),
                tuple(self._halfspace_covectors),
                equation_covectors=tuple(self._equation_covectors) + active,
                complete=self.is_complete_wall_set(),
            )

        def faces(self, dimension):
            r"""Return all nonempty faces of the stated dimension as owned cones.

            Sage's exact polyhedron engine computes the face incidence and
            reports the ambient H-representations active on each face.  Those
            active rows are crossed back as owned equality covectors, so the
            public face remains an exact cone rather than an engine face.
            """
            dimension = int(dimension)
            if dimension < 0 or dimension > int(self.dimension()):
                return finite_ordered_set(())
            return finite_ordered_set(
                tuple(
                    self._face_from_engine_face(face)
                    for face in self._engine.faces(dimension)
                )
            )

        def ambient_dimension(self):
            r"""Return the rank of the ambient lattice, the dimension of ``L tensor QQ``."""
            return self.ambient_lattice().module_rank()

        def intersection(self, other):
            r"""Return the cone cut out by the half-spaces and equations of both cones."""
            assert other.ambient_lattice() is self.ambient_lattice(), (
                f"cannot intersect {self} with {other}: they are cones in different "
                f"lattices, {self.ambient_lattice()} and {other.ambient_lattice()}"
            )
            return _rational_polyhedral_cone(
                self.ambient_lattice(),
                tuple(self._halfspace_covectors) + tuple(other.halfspace_covectors()),
                equation_covectors=tuple(self._equation_covectors) + tuple(other.equation_covectors()),
            )

        def is_equal_to(self, other) -> bool:
            r"""Return whether the two cones are the same subset of ``L tensor QQ``.

            Two presentations by different covector families can cut out one
            cone, so this compares the cones and not their presentations.
            """
            return (
                other.ambient_lattice() is self.ambient_lattice()
                and self._engine_polyhedron() == other._engine_polyhedron()
            )

        def is_face_of(self, other) -> bool:
            r"""Return whether this cone is a face of ``other``."""
            if other.ambient_lattice() is not self.ambient_lattice():
                return False
            polyhedron = self._engine_polyhedron()
            return any(
                face.as_polyhedron() == polyhedron
                for face in other._engine_polyhedron().faces(int(polyhedron.dim()))
            )

        def is_adjacent_to(self, other) -> bool:
            r"""Return whether the two cones share a common facet."""
            if other.ambient_lattice() is not self.ambient_lattice():
                return False
            common = self.intersection(other)
            return (
                common.dimension() == self.dimension() - 1
                and common.dimension() == other.dimension() - 1
                and common.is_face_of(self)
                and common.is_face_of(other)
            )

        def transporter_witness_to(self, other, group):
            r"""Return one element of the finite group ``group`` carrying this cone to ``other``, or ``None``.

            The search runs over the elements of the represented finite
            group; an infinite arithmetic group is handled by the surrounding traversal.
            """
            if other.ambient_lattice() is not self.ambient_lattice():
                return None
            lattice = self.ambient_lattice()
            assert group.domain() is lattice and group.codomain() is lattice, (
                f"cannot search {group} for an element carrying {self} to {other}: the "
                f"group must act on {lattice}, but it acts by maps {group.domain()} -> "
                f"{group.codomain()}"
            )
            assert group.cardinality().is_finite(), (
                f"cannot search {group} for an element carrying {self} to {other}: the "
                f"search runs over the elements of a finite group, and this group is "
                f"infinite; an infinite arithmetic group is handled by the reduction complex"
            )
            for isometry in group:
                if self.transport(isometry).is_equal_to(other):
                    return isometry
            return None

        def stabilizer(self, group):
            r"""Return the subgroup of ``group`` carrying this cone onto itself."""
            lattice = self.ambient_lattice()
            assert group.domain() is lattice and group.codomain() is lattice, (
                f"cannot form the stabilizer of {self} in {group}: the group must act on "
                f"{lattice}, but it acts by maps {group.domain()} -> {group.codomain()}"
            )
            return group.predicate_subgroup(
                lambda isometry: self.transport(isometry).is_equal_to(self),
                f"g preserves the rational polyhedral cone {self}",
            )

        def face_stabilizer(self, face, group):
            r"""Return the subgroup of ``group`` preserving this cone and its face ``face``.

            Membership in the cone stabilizer is required: the group may
            preserve the lower-dimensional face while moving the cone to
            another cone containing it.
            """
            assert face.is_face_of(self), (
                f"cannot form the stabilizer of {face} as a face of {self}: it is not a "
                f"face of that cone"
            )
            return self.stabilizer(group).intersection(face.stabilizer(group))

        def face_incidences(self, dimension, group):
            r"""Return the face inclusions of ``dimension`` with the subgroup stabilizing each pair."""
            from dzack_research.preamble.categories.reduction_complexes import (
                ReductionFaceIncidence,
            )
            from dzack_research.preamble.categories.sets.indexed_families import (
                finite_indexed_family,
            )

            return finite_indexed_family(
                self.faces(dimension),
                lambda face: ReductionFaceIncidence(
                    face,
                    self,
                    self.face_stabilizer(face, group),
                ),
                name=f"Face incidences of dimension {dimension} in {self}",
            )

        def adjacency_to(self, other, group):
            r"""Return the adjacency of this cone to ``other`` across their common facet, or ``None``.

            It exists when the cones share a facet and the finite group
            ``group`` carries this cone to ``other``; it retains the common
            facet and that transporter.
            """
            from dzack_research.preamble.categories.reduction_complexes import (
                ReductionCellAdjacency,
            )

            if not self.is_adjacent_to(other):
                return None
            transporter = self.transporter_witness_to(other, group)
            if transporter is None:
                return None
            return ReductionCellAdjacency(self, other, self.intersection(other), transporter)

        def with_marks(self, marked_vectors):
            r"""Return this cone with the labelled finite family ``marked_vectors`` of nonzero-norm lattice vectors."""
            from dzack_research.preamble.categories.reduction_complexes import (
                MarkedReductionCell,
            )

            return MarkedReductionCell(self, marked_vectors)

        def nonempty_faces(self):
            r"""Return every geometric face, from the zero face through this cone."""
            return finite_ordered_set(
                tuple(
                    face
                    for dimension in range(int(self.dimension()) + 1)
                    for face in self.faces(dimension)
                )
            )

        def facet_covectors(self):
            if self._engine.dim() <= 0:
                return finite_ordered_set(())
            facets = []
            for covector in self._halfspace_covectors:
                if self.face_on_covector(covector).dimension() == self.dimension() - 1:
                    facets.append(covector)
            return finite_ordered_set(tuple(facets))

        def facets(self):
            from dzack_research.preamble.categories.sets.indexed_families import (
                finite_indexed_family,
            )

            facets = self.facet_covectors()
            return finite_indexed_family(
                facets,
                self.face_on_covector,
                name="Facets of a rational polyhedral cone",
            )

        def hilbert_basis(self):
            assert self.is_pointed(), (
                f"cannot compute the Hilbert basis of {self}: it is computed only for a "
                f"pointed cone, and this cone contains the lines {self.lineality_generators()}"
            )
            lattice = self.ambient_lattice()
            rows = [tuple(int(entry) for entry in ray.to_tuple()) for ray in self.primitive_rays()]
            cone = SageCone(rows)
            return finite_ordered_set(tuple(_owned_vector(lattice, row) for row in cone.Hilbert_basis()))

        def ideal_rays(self):
            r"""Return the isotropic extremal rays when the ambient module is a lattice."""
            lattice = self.ambient_lattice()
            from dzack_research.preamble.categories.lattices import Lattices

            if lattice not in Lattices(lattice.base_ring()):
                raise TypeError(
                    f"{self} has no isotropic rays: it lies in {lattice}, which has no "
                    f"quadratic form; it is in {lattice.category()}"
                )
            return finite_ordered_set(tuple(ray for ray in self.primitive_rays() if lattice.q(ray) == 0))

        def timelike_rays(self):
            r"""Return the positive-square extremal rays in the repository's hyperbolic convention."""
            lattice = self.ambient_lattice()
            from dzack_research.preamble.categories.lattices import Lattices

            if lattice not in Lattices(lattice.base_ring()):
                raise TypeError(
                    f"{self} has no timelike rays: it lies in {lattice}, which has no "
                    f"quadratic form; it is in {lattice.category()}"
                )
            return finite_ordered_set(tuple(ray for ray in self.primitive_rays() if lattice.q(ray) > 0))

        def lies_in_closed_positive_cone(self, timelike) -> bool:
            r"""Whether this cone lies in one closed sheet of a signature ``(1,n)`` light cone.

            The exact criterion is ray/lineality based: the cone is pointed,
            every extremal ray has nonnegative square, and all nonzero rays
            pair with the selected timelike vector with one weak sign.  This
            distinguishes ideal isotropic rays from ordinary timelike rays and
            never inspects the cone's vertex at the origin.
            """
            lattice = self.ambient_lattice()
            from dzack_research.preamble.categories.lattices import Lattices

            if lattice not in Lattices(lattice.base_ring()):
                raise TypeError(
                    f"cannot decide whether {self} lies in the closed positive cone of "
                    f"{timelike}: it lies in {lattice}, which has no quadratic form; it is "
                    f"in {lattice.category()}"
                )
            timelike = lattice(timelike)
            if lattice.q(timelike) <= 0 or not self.is_pointed():
                return False
            rays = tuple(self.primitive_rays())
            if any(lattice.q(ray) < 0 for ray in rays):
                return False
            pairings = tuple(lattice.b(ray, timelike) for ray in rays)
            return all(value >= 0 for value in pairings)

        def _repr_(self):
            return f"Rational polyhedral cone in {self.ambient_lattice()} cut out by {self.halfspace_covectors().cardinality()} half-spaces"


def _rational_polyhedral_cone(
    lattice,
    halfspace_covectors,
    *,
    equation_covectors=(),
    wall_roots=None,
    complete=None,
):
    category = RationalPolyhedralCones(lattice)
    ambient = category.ambient_space()
    halfspaces = tuple(halfspace_covectors)
    equations = tuple(equation_covectors)
    subset = ambient.condition_set(
        lambda vector: _cone_contains(
            lattice,
            ambient,
            halfspaces,
            equations,
            vector,
        )
    )
    return Sets().Subobjects(ambient).object(
        subset.inclusion(),
        categories=(category,),
        construction_data={
            "lattice": lattice,
            "halfspace_covectors": halfspaces,
            "equation_covectors": equations,
            "wall_roots": wall_roots,
            "complete": complete,
        },
    )


__all__ = ["RationalPolyhedralCones"]
