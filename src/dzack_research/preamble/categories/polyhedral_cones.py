r"""Exact rational polyhedral cones retained by homogeneous half-spaces."""

from sage.arith.functions import lcm
from sage.arith.misc import gcd
from sage.geometry.cone import Cone as SageCone
from sage.geometry.polyhedron.constructor import Polyhedron
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.modules.framed.framed_free_modules import BasedFreeModule
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_coefficients
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import object_of


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


class RationalPolyhedralCones(OwnedCategory):
    r"""Rational polyhedral cones in a selected integral coordinate lattice.

    A cone is retained by homogeneous integral covectors ``ell`` defining
    ``ell(x) >= 0``.  Sage's exact polyhedral objects are private computation
    engines; the public object retains the ambient lattice and the covectors.
    """

    @classmethod
    def _repr_object_names(cls):
        return "rational polyhedral cones"

    def super_categories(self):
        return [Sets()]

    def an_object(self):
        integers = _own_ring(SageZZ)
        lattice = BasedFreeModule(integers, 2)
        dual = lattice.dual_module()
        return rational_polyhedral_cone(lattice, tuple(dual.module_generators()))

    class ParentMethods:
        def __init__(self, lattice, halfspace_covectors, wall_roots=None, complete=None, **rest):
            self._lattice = lattice
            dual = lattice.dual_module()
            self._halfspace_covectors = finite_ordered_set(
                tuple(dual(covector) for covector in halfspace_covectors)
            )
            self._wall_roots = None if wall_roots is None else finite_ordered_set(tuple(wall_roots))
            self._complete = complete
            labels = tuple(dual.module_generating_set())
            rows = []
            for covector in self._halfspace_covectors:
                coefficients = module_coefficients(covector, dual)
                rows.append([SageQQ.zero()] + [SageQQ(int(coefficients.get(label, 0))) for label in labels])
            self._engine = Polyhedron(ieqs=rows, base_ring=SageQQ)
            super().__init__(**rest)

        def ambient_lattice(self):
            return self._lattice

        def halfspace_covectors(self):
            return self._halfspace_covectors

        def wall_roots(self):
            return self._wall_roots

        def is_complete_wall_set(self):
            return self._complete

        def _engine_polyhedron(self):
            return self._engine

        def dimension(self):
            return self.ambient_lattice().base_ring()(int(self._engine.dim()))

        def is_pointed(self) -> bool:
            return len(tuple(self._engine.lines())) == 0

        def evaluate_covector(self, covector, vector):
            lattice = self.ambient_lattice()
            dual = lattice.dual_module()
            covector = dual(covector)
            vector = lattice(vector)
            covector_coefficients = module_coefficients(covector, dual)
            vector_coefficients = module_coefficients(vector, lattice)
            return sum(
                (
                    covector_coefficients.get(label, lattice.base_ring().zero())
                    * vector_coefficients.get(label, lattice.base_ring().zero())
                    for label in lattice.module_generating_set()
                ),
                lattice.base_ring().zero(),
            )

        def contains(self, vector) -> bool:
            lattice = self.ambient_lattice()
            return all(
                self.evaluate_covector(covector, vector) >= lattice.base_ring().zero()
                for covector in self._halfspace_covectors
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

        def facet_covectors(self):
            if self._engine.dim() <= 0:
                return finite_ordered_set(())
            labels = tuple(self.ambient_lattice().dual_module().module_generating_set())
            facets = []
            all_rows = [list(inequality) for inequality in self._engine.inequalities()]
            for covector in self._halfspace_covectors:
                coefficients = module_coefficients(covector, self.ambient_lattice().dual_module())
                equation = [SageQQ.zero()] + [SageQQ(int(coefficients.get(label, 0))) for label in labels]
                face = Polyhedron(ieqs=all_rows, eqns=[equation], base_ring=SageQQ)
                if face.dim() == self._engine.dim() - 1:
                    facets.append(covector)
            return finite_ordered_set(tuple(facets))

        def hilbert_basis(self):
            assert self.is_pointed(), "the Hilbert basis is requested here only for a pointed cone"
            lattice = self.ambient_lattice()
            rows = [tuple(int(entry) for entry in ray.to_tuple()) for ray in self.primitive_rays()]
            cone = SageCone(rows)
            return finite_ordered_set(tuple(_owned_vector(lattice, row) for row in cone.Hilbert_basis()))

        def ideal_rays(self):
            r"""Return the isotropic extremal rays when the ambient module is a lattice."""
            lattice = self.ambient_lattice()
            from dzack_research.preamble.categories.lattices import Lattices

            if lattice not in Lattices(lattice.base_ring()):
                raise TypeError("ideal rays require a formed lattice ambient")
            return finite_ordered_set(tuple(ray for ray in self.primitive_rays() if lattice.q(ray) == 0))

        def timelike_rays(self):
            r"""Return the positive-square extremal rays in the repository's hyperbolic convention."""
            lattice = self.ambient_lattice()
            from dzack_research.preamble.categories.lattices import Lattices

            if lattice not in Lattices(lattice.base_ring()):
                raise TypeError("timelike rays require a formed lattice ambient")
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
                raise TypeError("the positive-cone test requires a formed lattice ambient")
            timelike = lattice(timelike)
            if lattice.q(timelike) <= 0 or not self.is_pointed():
                return False
            rays = tuple(self.primitive_rays())
            if any(lattice.q(ray) < 0 for ray in rays):
                return False
            pairings = tuple(lattice.b(ray, timelike) for ray in rays)
            nonnegative = all(value >= 0 for value in pairings)
            nonpositive = all(value <= 0 for value in pairings)
            return nonnegative or nonpositive

        def _repr_(self):
            return f"Rational polyhedral cone in {self.ambient_lattice()} cut out by {self.halfspace_covectors().cardinality()} half-spaces"


def rational_polyhedral_cone(lattice, halfspace_covectors, *, wall_roots=None, complete=None):
    return object_of(
        RationalPolyhedralCones(),
        lattice=lattice,
        halfspace_covectors=tuple(halfspace_covectors),
        wall_roots=wall_roots,
        complete=complete,
    )


__all__ = ["RationalPolyhedralCones", "rational_polyhedral_cone"]
