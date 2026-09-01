r"""Convex polytopes and integral lattice polytopes."""

from math import factorial

from sage.categories.category import Category
from sage.geometry.polyhedron.constructor import Polyhedron
from sage.geometry.toric_lattice import ToricLattice
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.rings.rational_field import QQ
from sage.structure.parent import Parent

from dzack_research.preamble.categories.sets import Sets, finite_ordered_set


class ConvexPolytopes(Category):
    @classmethod
    def _repr_object_names(cls):
        return "convex polytopes"

    def super_categories(self):
        return [Sets()]

    def __contains__(self, candidate) -> bool:
        return isinstance(candidate, ConvexPolytopeParent)


class LatticePolytopes(Category):
    @classmethod
    def _repr_object_names(cls):
        return "lattice polytopes"

    def super_categories(self):
        return [ConvexPolytopes()]

    def __contains__(self, candidate) -> bool:
        return candidate in ConvexPolytopes() and candidate.is_lattice_polytope()


class ConvexPolygons(Category):
    @classmethod
    def _repr_object_names(cls):
        return "convex polygons"

    def super_categories(self):
        return [ConvexPolytopes()]

    def __contains__(self, candidate) -> bool:
        return candidate in ConvexPolytopes() and candidate.dimension() == 2


class LatticePolygons(Category):
    @classmethod
    def _repr_object_names(cls):
        return "lattice polygons"

    def super_categories(self):
        return [ConvexPolygons(), LatticePolytopes()]

    def __contains__(self, candidate) -> bool:
        return candidate in ConvexPolygons() and candidate in LatticePolytopes()


class ConvexPolytopeParent(Parent):
    r"""A rational convex polytope in ``N_Q`` with a chosen lattice ``N``."""

    def __init__(self, vertices, *, lattice=None, require_integral=False) -> None:
        if isinstance(vertices, ConvexPolytopeParent):
            polyhedron = vertices.polyhedron()
            if lattice is None:
                lattice = vertices.ambient_lattice()
        elif hasattr(vertices, "vertices") and hasattr(vertices, "dim"):
            polyhedron = vertices
        else:
            polyhedron = Polyhedron(vertices=[tuple(vertex) for vertex in vertices])

        ambient_dimension = int(polyhedron.ambient_dim())
        if lattice is None:
            lattice = ToricLattice(ambient_dimension, "N")
        if int(lattice.rank()) != ambient_dimension:
            raise ValueError("the ambient lattice rank must equal the coordinate dimension")

        self._polyhedron = polyhedron
        self._ambient_lattice = lattice
        self._require_integral = bool(require_integral)
        if self._require_integral and not self._vertices_are_integral():
            raise ValueError("a lattice polytope must have integral vertices")

        category = (
            LatticePolygons()
            if self._require_integral and self.dimension() == 2
            else LatticePolytopes()
            if self._require_integral
            else ConvexPolygons()
            if self.dimension() == 2
            else ConvexPolytopes()
        )
        Parent.__init__(self, category=category)

    def polyhedron(self):
        return self._polyhedron

    def ambient_lattice(self):
        return self._ambient_lattice

    def ambient_space(self):
        return (
            self.ambient_lattice()
            if self.is_lattice_polytope()
            else self.ambient_lattice().base_extend(QQ)
        )

    def dimension(self):
        return Integer(self.polyhedron().dim())

    def vertices(self):
        ambient = self.ambient_space()
        return finite_ordered_set(
            ambient(tuple(vertex)) for vertex in self.polyhedron().vertices()
        )

    def facets(self):
        return finite_ordered_set(self.polyhedron().facets())

    def normal_fan(self):
        return self.polyhedron().normal_fan()

    def volume(self):
        return QQ(self.polyhedron().volume())

    def normalized_volume(self):
        return ZZ(factorial(int(self.dimension())) * self.volume())

    def is_compact(self) -> bool:
        return True

    def _vertices_are_integral(self) -> bool:
        return all(
            coordinate in ZZ
            for vertex in self.polyhedron().vertices()
            for coordinate in vertex
        )

    def is_lattice_polytope(self) -> bool:
        return self._vertices_are_integral()

    def contains_point(self, point) -> bool:
        return bool(self.polyhedron().contains(tuple(point)))

    def interior_contains_point(self, point) -> bool:
        return bool(self.polyhedron().relative_interior_contains(tuple(point)))

    def integral_points(self):
        return finite_ordered_set(
            self.ambient_lattice()(tuple(point))
            for point in self.polyhedron().integral_points()
        )

    def interior_integral_points(self):
        return finite_ordered_set(
            point
            for point in self.integral_points()
            if self.polyhedron().relative_interior_contains(tuple(point))
        )

    def boundary_integral_points(self):
        interior = tuple(self.interior_integral_points())
        return finite_ordered_set(
            point for point in self.integral_points() if point not in interior
        )

    def n_integral_points(self):
        return self.integral_points().cardinality()

    def n_interior_points(self):
        return self.interior_integral_points().cardinality()

    def n_boundary_points(self):
        return self.boundary_integral_points().cardinality()

    def _dilate(self, scalar):
        scalar = ZZ(scalar)
        if scalar < 0:
            raise ValueError("Ehrhart dilation factors are nonnegative")
        return LatticePolytope(
            [
                tuple(scalar * coordinate for coordinate in vertex)
                for vertex in self.polyhedron().vertices()
            ],
            lattice=self.ambient_lattice(),
        )

    def ehrhart_polynomial(self, variable="t"):
        r"""Return the exact Ehrhart polynomial by interpolation."""
        if not self.is_lattice_polytope():
            raise TypeError("the Ehrhart polynomial is defined here for lattice polytopes")
        polynomial_ring = PolynomialRing(QQ, variable)
        t = polynomial_ring.gen()
        d = int(self.dimension())
        values = [
            ZZ.one() if k == 0 else self._dilate(k).n_integral_points()
            for k in range(d + 1)
        ]
        result = polynomial_ring.zero()
        for i, value in enumerate(values):
            basis = polynomial_ring.one()
            denominator = QQ.one()
            for j in range(d + 1):
                if i == j:
                    continue
                basis *= t - j
                denominator *= i - j
            result += QQ(value) / denominator * basis
        return result

    def h_star_vector(self):
        r"""Return the Ehrhart ``h*`` vector ``(h*_0,...,h*_d)``."""
        from sage.arith.misc import binomial

        if not self.is_lattice_polytope():
            raise TypeError("the h* vector is defined here for lattice polytopes")
        d = int(self.dimension())
        counts = [
            ZZ.one() if k == 0 else self._dilate(k).n_integral_points()
            for k in range(d + 1)
        ]
        return tuple(
            ZZ(
                sum(
                    (-1) ** (j - i)
                    * binomial(d + 1, j - i)
                    * counts[i]
                    for i in range(j + 1)
                )
            )
            for j in range(d + 1)
        )

    def is_reflexive(self) -> bool:
        if not self.is_lattice_polytope():
            return False
        if self.dimension() != self.polyhedron().ambient_dim():
            return False
        origin = (0,) * int(self.polyhedron().ambient_dim())
        if not self.polyhedron().interior_contains(origin):
            return False
        return bool(self.polyhedron().is_reflexive())

    def polar_dual(self):
        if self.dimension() != self.polyhedron().ambient_dim():
            raise ValueError("polar duality here requires a full-dimensional polytope")
        origin = (0,) * int(self.polyhedron().ambient_dim())
        if not self.polyhedron().interior_contains(origin):
            raise ValueError("the polar dual is bounded only when the origin is interior")
        polar = self.polyhedron().polar()
        vertices = [tuple(vertex) for vertex in polar.vertices()]
        if all(coordinate in ZZ for vertex in vertices for coordinate in vertex):
            return LatticePolytope(vertices, lattice=self.ambient_lattice().dual())
        return ConvexPolytope(vertices, lattice=self.ambient_lattice().dual())

    def is_smooth(self) -> bool:
        if not self.is_lattice_polytope():
            return False
        if self.dimension() != self.polyhedron().ambient_dim():
            return False
        return bool(self.normal_fan().is_smooth())

    def _repr_(self):
        noun = "Lattice " if self.is_lattice_polytope() else "Convex "
        noun += "Polygon" if self.dimension() == 2 else "Polytope"
        return f"{noun} of dimension {self.dimension()} with {len(self.vertices())} vertices"


def ConvexPolytope(vertices, lattice=None):
    return ConvexPolytopeParent(vertices, lattice=lattice, require_integral=False)


def ConvexPolygon(vertices, lattice=None):
    polytope = ConvexPolytope(vertices, lattice=lattice)
    if polytope.dimension() != 2:
        raise ValueError("a convex polygon has affine dimension two")
    return polytope


def LatticePolytope(vertices, lattice=None):
    return ConvexPolytopeParent(vertices, lattice=lattice, require_integral=True)


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
