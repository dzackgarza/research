r"""Convex polytopes and integral lattice polytopes."""

from math import factorial

from sage.categories.category import Category
from sage.geometry.polyhedron.constructor import Polyhedron
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.rings.ring_foundation import _engine_element, _own_ring
from dzack_research.preamble.tensors.tensor import tensor
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.algebras.free_algebras import PolynomialRing
from dzack_research.preamble.categories.modules.framed.framed_free_modules import BasedFreeModule
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_filter,
    finite_ordered_image,
)


class ConvexPolytopes(OwnedCategory):
    r"""Rational convex polytopes in a chosen coordinate lattice.

    Public coordinate data live in the owned modules ``ZZ^n`` and ``QQ^n``.
    Sage's exact ``Polyhedron`` is retained only as the private polyhedral
    computation engine.
    """

    def an_object(self):
        r"""The rational simplex on ``0, e_1/2, e_2, e_3`` in ``QQ^3``."""
        from sage.rings.rational import Rational

        return ConvexPolytope(
            (
                (0, 0, 0),
                (Rational((1, 2)), 0, 0),
                (0, 1, 0),
                (0, 0, 1),
            )
        )

    @classmethod
    def _repr_object_names(cls):
        return "convex polytopes"

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def __init__(self, vertices, lattice=None, require_integral=False, **rest) -> None:
            integers = _own_ring(SageZZ)
            rationals = _own_ring(SageQQ)

            if vertices in ConvexPolytopes():
                polyhedron = vertices._engine_polyhedron()
                if lattice is None:
                    lattice = vertices.ambient_lattice()
            elif hasattr(vertices, "vertices") and hasattr(vertices, "dim"):
                polyhedron = vertices
            else:
                def owned_rational(coordinate):
                    parent = getattr(coordinate, "parent", lambda: None)()
                    if parent in (SageZZ, SageQQ):
                        return rationals._from_engine_element(SageQQ(coordinate))
                    return rationals(coordinate)

                owned_vertices = tuple(
                    tuple(owned_rational(coordinate) for coordinate in vertex)
                    for vertex in vertices
                )
                engine_vertices = [
                    tuple(_engine_element(rationals, coordinate) for coordinate in vertex)
                    for vertex in owned_vertices
                ]
                polyhedron = Polyhedron(vertices=engine_vertices, base_ring=SageQQ)

            ambient_dimension = int(polyhedron.ambient_dim())
            if lattice is None:

                lattice = BasedFreeModule(integers, ambient_dimension)
            if lattice.base_ring() is not integers:
                raise TypeError("the ambient lattice of a rational polytope is an owned ZZ-module")
            if int(lattice.rank()) != ambient_dimension:
                raise ValueError("the ambient lattice rank must equal the coordinate dimension")

            self._polyhedron = polyhedron
            self._ambient_lattice = lattice
            self._require_integral = bool(require_integral)
            if self._require_integral and not self._vertices_are_integral():
                raise ValueError("a lattice polytope must have integral vertices")

            super().__init__(**rest)

        def _engine_polyhedron(self):
            r"""Return the private exact polyhedral computation object."""
            return self._polyhedron

        def _owned_rational_coordinate(self, coordinate):
            rationals = _own_ring(SageQQ)
            return rationals._from_engine_element(SageQQ(coordinate))

        def _owned_integral_coordinate(self, coordinate):
            integers = _own_ring(SageZZ)
            return integers._from_engine_element(SageZZ(coordinate))

        def _engine_coordinates(self, point):
            rationals = _own_ring(SageQQ)
            return tuple(
                _engine_element(rationals, rationals(coordinate))
                for coordinate in point
            )

        def ambient_lattice(self):
            r"""Return the owned coordinate lattice ``ZZ^n``."""
            return self._ambient_lattice

        def ambient_space(self):
            r"""Return the owned rational coordinate module ``QQ^n``."""

            rationals = _own_ring(SageQQ)
            return BasedFreeModule(
                rationals,
                self.ambient_lattice().module_generating_set(),
            )

        def dimension(self):
            return _own_ring(SageZZ)(int(self._engine_polyhedron().dim()))

        def vertices(self):
            if self.is_lattice_polytope():
                integers = _own_ring(SageZZ)
                return finite_ordered_set(
                    tuple(
                        tensor.vector(
                            integers,
                            tuple(
                                self._owned_integral_coordinate(coordinate)
                                for coordinate in vertex
                            ),
                        )
                        for vertex in self._engine_polyhedron().vertices()
                    )
                )
            rationals = _own_ring(SageQQ)
            return finite_ordered_set(
                tuple(
                    tensor.vector(
                        rationals,
                        tuple(
                            self._owned_rational_coordinate(coordinate)
                            for coordinate in vertex
                        ),
                    )
                    for vertex in self._engine_polyhedron().vertices()
                )
            )

        def n_vertices(self):
            return _own_ring(SageZZ)(int(self._engine_polyhedron().n_vertices()))

        def facets(self):
            r"""Return the codimension-one faces as owned polytopes."""
            return finite_ordered_set(
                tuple(
                    _convex_polytope(
                        facet.as_polyhedron(),
                        lattice=self.ambient_lattice(),
                        require_integral=self.is_lattice_polytope(),
                    )
                    for facet in self._engine_polyhedron().facets()
                )
            )

        def _engine_normal_fan(self):
            r"""Return the private normal-fan computation object."""
            return self._engine_polyhedron().normal_fan(direction="inner")

        @cached_method
        def normal_fan(self):
            r"""Return the normal fan ``Sigma_P`` in ``N_R`` (CLS Def. 2.3.2).

            The polytope lives in ``M_R`` for ``M`` its coordinate lattice, so
            the normal fan lives in the dual lattice ``N``.  The cone of a face
            ``Q`` is spanned by the *inner* normals of the facets containing
            ``Q``, which is the convention under which ``X_{Sigma_P}`` carries
            ``P`` as the polytope of an ample divisor.
            """
            from dzack_research.preamble.categories.schemes.toric.fans import (
                RationalPolyhedralFans,
            )

            assert int(self.dimension()) == int(
                self._engine_polyhedron().ambient_dim()
            ), "the normal fan is taken of a full-dimensional polytope"
            cocharacters = self.ambient_lattice().dual_module()
            return RationalPolyhedralFans(cocharacters).from_engine_fan(
                self._engine_normal_fan()
            )

        def toric_variety(self, base_ring):
            r"""Return ``X_P``, the toric variety of the normal fan of ``P``.

            ``P`` is retained as the polarizing polytope of the result: it is
            the polytope of the ample divisor that the construction produced,
            and it is not recoverable from the fan alone.
            """
            from dzack_research.preamble.categories.schemes.toric.toric_schemes import (
                ToricVariety,
            )

            assert self.is_lattice_polytope(), (
                "the toric variety of a polytope is defined for lattice polytopes"
            )
            return ToricVariety(
                self.normal_fan(),
                base_ring,
                polarizing_polytope=self,
            )

        def volume(self):
            rationals = _own_ring(SageQQ)
            return rationals._from_engine_element(
                SageQQ(self._engine_polyhedron().volume())
            )

        def normalized_volume(self):
            integers = _own_ring(SageZZ)
            return integers(factorial(int(self.dimension())) * self.volume())

        def is_compact(self) -> bool:
            return True

        def _vertices_are_integral(self) -> bool:
            return all(
                coordinate in SageZZ
                for vertex in self._engine_polyhedron().vertices()
                for coordinate in vertex
            )

        def is_lattice_polytope(self) -> bool:
            return self._vertices_are_integral()

        def contains_point(self, point) -> bool:
            return bool(self._engine_polyhedron().contains(self._engine_coordinates(point)))

        def interior_contains_point(self, point) -> bool:
            return bool(
                self._engine_polyhedron().relative_interior_contains(
                    self._engine_coordinates(point)
                )
            )

        def integral_points(self):
            integers = _own_ring(SageZZ)

            engine_points = finite_ordered_set(
                tuple(self._engine_polyhedron().integral_points())
            )
            return finite_ordered_image(
                engine_points,
                lambda point: tensor.vector(
                    integers,
                    (self._owned_integral_coordinate(coordinate) for coordinate in point),
                ),
                name="Integral points",
            )

        def interior_integral_points(self):

            return finite_ordered_filter(
                self.integral_points(),
                lambda point: self._engine_polyhedron().relative_interior_contains(
                    self._engine_coordinates(point)
                ),
                name="Interior integral points",
            )

        def boundary_integral_points(self):

            interior = self.interior_integral_points()
            return finite_ordered_filter(
                self.integral_points(),
                lambda point: point not in interior,
                name="Boundary integral points",
            )

        def n_integral_points(self):
            return self.integral_points().cardinality()

        def n_interior_points(self):
            return self.interior_integral_points().cardinality()

        def n_boundary_points(self):
            return self.boundary_integral_points().cardinality()

        def _dilate(self, scalar):
            integers = _own_ring(SageZZ)
            scalar = integers(scalar)
            if scalar < integers.zero():
                raise ValueError("Ehrhart dilation factors are nonnegative")
            return LatticePolytope(
                [tuple(scalar * coordinate for coordinate in vertex) for vertex in self.vertices()],
                lattice=self.ambient_lattice(),
            )

        def ehrhart_polynomial(self, variable="t"):
            r"""Return the exact owned Ehrhart polynomial by interpolation."""
            if not self.is_lattice_polytope():
                raise TypeError("the Ehrhart polynomial is defined here for lattice polytopes")

            rationals = _own_ring(SageQQ)
            integers = _own_ring(SageZZ)
            polynomial_ring = PolynomialRing(rationals, variable)
            t = polynomial_ring.algebra_generator(variable)
            d = int(self.dimension())
            values = [
                integers.one() if k == 0 else integers(int(self._dilate(k).n_integral_points()))
                for k in range(d + 1)
            ]
            result = polynomial_ring.zero()
            for i, value in enumerate(values):
                basis = polynomial_ring.one()
                denominator = rationals.one()
                for j in range(d + 1):
                    if i == j:
                        continue
                    basis *= t - j
                    denominator *= rationals(i - j)
                result += rationals(value) / denominator * basis
            return result

        def h_star_vector(self):
            r"""Return the owned Ehrhart ``h*`` vector ``(h*_0,...,h*_d)``."""
            from math import comb

            integers = _own_ring(SageZZ)
            if not self.is_lattice_polytope():
                raise TypeError("the h* vector is defined here for lattice polytopes")
            d = int(self.dimension())
            counts = [
                integers.one() if k == 0 else integers(int(self._dilate(k).n_integral_points()))
                for k in range(d + 1)
            ]
            result = []
            for j in range(d + 1):
                value = integers.zero()
                for i in range(j + 1):
                    coefficient = integers(((-1) ** (j - i)) * comb(d + 1, j - i))
                    value += coefficient * counts[i]
                result.append(value)

            return finite_family(result, name="h* vector")

        def is_reflexive(self) -> bool:
            if not self.is_lattice_polytope():
                return False
            if int(self.dimension()) != int(self._engine_polyhedron().ambient_dim()):
                return False
            origin = (SageQQ.zero(),) * int(self._engine_polyhedron().ambient_dim())
            if not self._engine_polyhedron().interior_contains(origin):
                return False
            polar = self._engine_polyhedron().polar()
            return all(
                coordinate in SageZZ
                for vertex in polar.vertices()
                for coordinate in vertex
            )

        def polar_dual(self):
            if int(self.dimension()) != int(self._engine_polyhedron().ambient_dim()):
                raise ValueError("polar duality here requires a full-dimensional polytope")
            origin = (SageQQ.zero(),) * int(self._engine_polyhedron().ambient_dim())
            if not self._engine_polyhedron().interior_contains(origin):
                raise ValueError("the polar dual is bounded only when the origin is interior")
            polar = self._engine_polyhedron().polar()
            if all(
                coordinate in SageZZ
                for vertex in polar.vertices()
                for coordinate in vertex
            ):
                return LatticePolytope(polar.vertices())
            return ConvexPolytope(polar.vertices())

        def is_smooth(self) -> bool:
            if not self.is_lattice_polytope():
                return False
            if int(self.dimension()) != int(self._engine_polyhedron().ambient_dim()):
                return False
            return bool(self._engine_normal_fan().is_smooth())

        def _repr_(self):
            noun = "Lattice " if self.is_lattice_polytope() else "Convex "
            noun += "Polygon" if int(self.dimension()) == 2 else "Polytope"
            return f"{noun} of dimension {self.dimension()} with {len(self.vertices())} vertices"



class LatticePolytopes(OwnedCategory):
    r"""Convex polytopes all of whose vertices are lattice points."""

    def an_object(self):
        r"""The standard simplex in ``ZZ^3``."""
        return LatticePolytope(((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)))

    @cached_method
    def reflexive_polytopes(self, dimension):
        r"""The reflexive polytopes of the stated dimension, up to lattice equivalence.

        The classification is Kreuzer--Skarke's; Sage carries it in
        ``sage.geometry.lattice_polytope.ReflexivePolytopes``, with dimension
        two built in and dimension three behind its optional polytope
        database.  By Batyrev's theorem the toric variety of the normal fan of
        a reflexive polytope is Gorenstein Fano, so this is the finite list a
        session searches when it wants those.
        """
        from sage.geometry.lattice_polytope import ReflexivePolytopes

        dimension = int(dimension)
        assert dimension in (2, 3), (
            "the represented reflexive-polytope classification covers "
            "dimensions two and three"
        )
        return finite_ordered_set(
            tuple(
                LatticePolytope(
                    tuple(
                        tuple(int(coordinate) for coordinate in vertex)
                        for vertex in classified.vertices()
                    )
                )
                for classified in ReflexivePolytopes(dimension)
            )
        )

    @classmethod
    def _repr_object_names(cls):
        return "lattice polytopes"

    def super_categories(self):
        return [ConvexPolytopes()]



class ConvexPolygons(OwnedCategory):
    r"""Convex polytopes of affine dimension two."""

    def an_object(self):
        r"""The triangle on ``0, e_1/2, e_2``, whose vertices are not integral."""
        from sage.rings.rational import Rational

        return ConvexPolygon(((0, 0), (Rational((1, 2)), 0), (0, 1)))

    @classmethod
    def _repr_object_names(cls):
        return "convex polygons"

    def super_categories(self):
        return [ConvexPolytopes()]



class LatticePolygons(OwnedCategory):
    r"""Lattice polytopes of affine dimension two."""

    def an_object(self):
        r"""The standard triangle in ``ZZ^2``."""
        return LatticePolygon(((0, 0), (1, 0), (0, 1)))

    @classmethod
    def _repr_object_names(cls):
        return "lattice polygons"

    def super_categories(self):
        return [ConvexPolygons(), LatticePolytopes()]





def _convex_polytope(vertices, lattice=None, require_integral=False):
    r"""Return the polytope its category generates, placed by what it is.

    Integrality of the vertices and affine dimension two are the two
    conditions the finer categories state, so the construction decides them
    once and the object is placed accordingly.
    """
    probe = object_of(
        ConvexPolytopes(),
        vertices=vertices,
        lattice=lattice,
        require_integral=require_integral,
    )
    integral = probe.is_lattice_polytope()
    plane = int(probe.dimension()) == 2
    placement = (
        LatticePolygons()
        if integral and plane
        else LatticePolytopes()
        if integral
        else ConvexPolygons()
        if plane
        else ConvexPolytopes()
    )
    if placement is ConvexPolytopes():
        return probe
    return object_of(
        placement,
        vertices=probe,
        lattice=probe.ambient_lattice(),
        require_integral=require_integral,
    )


def ConvexPolytope(vertices, lattice=None):
    return _convex_polytope(vertices, lattice=lattice, require_integral=False)


def ConvexPolygon(vertices, lattice=None):
    polytope = ConvexPolytope(vertices, lattice=lattice)
    if polytope.dimension() != 2:
        raise ValueError("a convex polygon has affine dimension two")
    return polytope


def LatticePolytope(vertices, lattice=None):
    return _convex_polytope(vertices, lattice=lattice, require_integral=True)


def LatticePolygon(vertices, lattice=None):
    polytope = LatticePolytope(vertices, lattice=lattice)
    if polytope.dimension() != 2:
        raise ValueError("a lattice polygon has affine dimension two")
    return polytope


__all__ = [
    "ConvexPolygon",
    "ConvexPolygons",
    "ConvexPolytope",
    "ConvexPolytopes",
    "LatticePolygon",
    "LatticePolygons",
    "LatticePolytope",
    "LatticePolytopes",
]
