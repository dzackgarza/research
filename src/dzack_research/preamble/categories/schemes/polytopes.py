r"""Convex polytopes and integral lattice polytopes."""

from math import atan2, factorial

from sage.categories.category import Category
from sage.categories.category_with_axiom import all_axioms
from sage.geometry.polyhedron.constructor import Polyhedron
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.element import parent as engine_parent

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.rings.ring_foundation import _engine_element, _own_ring
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.tensors.tensor import tensor

for _axiom in ("Integral", "Polygon"):
    if _axiom not in all_axioms:
        all_axioms.add(_axiom)


def _owned_rational(coordinate):
    r"""One coordinate as an owned rational.

    This is the ingress boundary of the polytope constructors, and the one
    place that admits all three ways a caller writes a coordinate: as an
    ordinary integer, as an engine rational, or as an owned rational.  The
    parent of the incoming value decides which, through Sage's own parent
    function rather than by asking the value for an attribute.
    """
    if engine_parent(coordinate) in (SageZZ, SageQQ):
        return _own_ring(SageQQ)._from_engine_element(SageQQ(coordinate))
    return _own_ring(SageQQ)(coordinate)


class RegularPolytopes(OwnedCategory):
    r"""Finite spherical regular abstract polytopes named by Schlaefli symbols.

    The Schlaefli symbol ``{p_1,...,p_{n-1}}`` determines the string Coxeter
    diagram ``[p_1,...,p_{n-1}]`` of the full reflection symmetry group.  This
    owner records that abstract regular-polytope datum; it is distinct from the
    rational-coordinate convex-polytope owner below, since examples such as the
    dodecahedron require ``sqrt(5)`` coordinates in a Euclidean realization.
    """

    def an_object(self):
        return self.from_schlafli_symbol((3, 3))

    @classmethod
    def _repr_object_names(cls):
        return "finite spherical regular polytopes"

    def super_categories(self):
        return [Sets()]

    def from_schlafli_symbol(self, symbol):
        r"""Return the finite regular abstract polytope with Schlaefli symbol ``symbol``."""
        from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix

        from dzack_research.preamble.categories.coxeter_diagrams import CoxeterDiagrams

        match symbol:
            case str() as written:
                written = written.strip()
                if not (written.startswith("{") and written.endswith("}")):
                    raise ValueError("a Schlaefli symbol is written {p1,...,pr}")
                body = written[1:-1].strip()
                bonds = () if not body else tuple(int(part.strip()) for part in body.split(","))
            case _:
                bonds = tuple(int(bond) for bond in symbol)
        if not bonds or any(bond < 3 for bond in bonds):
            raise ValueError("a finite regular polytope symbol has bond orders at least three")
        rank = len(bonds) + 1
        entries = tuple(
            tuple(
                1
                if row == column
                else bonds[min(row, column)]
                if abs(row - column) == 1
                else 2
                for column in range(rank)
            )
            for row in range(rank)
        )
        diagram = CoxeterDiagrams().from_coxeter_matrix(CoxeterMatrix(entries))
        assert diagram.is_elliptic(), (
            "this Schlaefli symbol does not define a finite spherical regular polytope"
        )
        return _object_of(
            self,
            schlafli_bonds=finite_ordered_set(bonds),
            symmetry_coxeter_diagram=diagram,
        )

    class ParentMethods:
        def __init__(self, schlafli_bonds, symmetry_coxeter_diagram, **rest) -> None:
            self._schlafli_bonds = schlafli_bonds
            self._symmetry_coxeter_diagram = symmetry_coxeter_diagram
            super().__init__(**rest)

        def schlafli_symbol(self):
            return self._schlafli_bonds

        def dimension(self):
            return _own_ring(SageZZ)(self.schlafli_symbol().cardinality() + 1)

        def symmetry_coxeter_diagram(self):
            return self._symmetry_coxeter_diagram

        def symmetry_group(self):
            return self.symmetry_coxeter_diagram().coxeter_group()

        def _repr_(self):
            symbol = ",".join(str(bond) for bond in self.schlafli_symbol())
            return f"Regular polytope {{{symbol}}}"


class ConvexPolytopes(OwnedCategory):
    r"""Rational convex polytopes in a chosen coordinate lattice.

    Public coordinate data live in the owned modules ``ZZ^n`` and ``QQ^n``.
    Sage's exact ``Polyhedron`` is retained only as the private polyhedral
    computation engine.
    """

    def an_object(self):
        r"""The rational simplex on ``0, e_1/2, e_2, e_3`` in ``QQ^3``."""
        from sage.rings.rational import Rational

        return self(
            (
                (0, 0, 0),
                (Rational((1, 2)), 0, 0),
                (0, 1, 0),
                (0, 0, 1),
            )
        )

    def _call_(self, vertices, lattice=None):
        r"""Construct the convex polytope on the selected vertices."""
        return _convex_polytope(vertices, lattice=lattice)

    def from_halfspaces(self, halfspaces, lattice=None):
        r"""The polytope cut out by a family of affine halfspaces.

        Each halfspace is the pair ``(b, a)`` of the constant and the linear
        part of ``b + <a, x> >= 0`` in the coordinates of ``lattice``, so the
        family is the halfspace description of the intersection.  A polytope
        is bounded, and an unbounded intersection is refused rather than
        truncated.  Passing from this description to the vertices is the
        private polyhedral computation.
        """
        rationals = _own_ring(SageQQ)
        engine_rows = [
            [
                _engine_element(rationals, _owned_rational(constant)),
                *(
                    _engine_element(rationals, _owned_rational(coefficient))
                    for coefficient in linear_part
                ),
            ]
            for constant, linear_part in halfspaces
        ]
        polyhedron = Polyhedron(ieqs=engine_rows, base_ring=SageQQ)
        assert polyhedron.is_compact(), (
            "a polytope is a bounded intersection of halfspaces"
        )
        return _convex_polytope(engine_polyhedron=polyhedron, lattice=lattice)

    @classmethod
    def _repr_object_names(cls):
        return "convex polytopes"

    def super_categories(self):
        return [Sets()]

    class SubcategoryMethods:
        def Integral(self) -> Category:
            r"""Return this category with the axiom that every vertex is a lattice point."""
            return self._with_axiom("Integral")

        def Polygon(self) -> Category:
            r"""Return this category with the axiom that the affine dimension is two."""
            return self._with_axiom("Polygon")

    class ParentMethods:
        def __init__(self, engine_polyhedron, ambient_lattice, **rest) -> None:
            r"""A polytope is its exact polyhedron in the coordinates of ``ZZ^n``.

            The polyhedron is the private computation object that
            :func:`_convex_polytope` produced from the caller's vertices, from
            an owned polytope, from a face, a dilation or a halfspace
            description; the coordinate lattice is the owned ``ZZ^n``.
            """
            self._polyhedron = engine_polyhedron
            self._ambient_lattice = ambient_lattice
            super().__init__(**rest)

        def _engine_polyhedron(self):
            r"""Return the private exact polyhedral computation object."""
            return self._polyhedron

        def threejs_html(self):
            r"""Return a local Three.js HTML view of a three-dimensional polytope.

            The private exact Sage polyhedron remains the rendering engine.
            This method does not attach display data to the owned polytope: it
            asks Sage's existing ``Graphics3d`` Three.js serializer for a
            self-contained local HTML representation at the view boundary.
            """
            assert int(self._engine_polyhedron().ambient_dim()) == 3, (
                "a Three.js polytope view requires ambient dimension three"
            )
            graphic = self._engine_polyhedron().plot()
            rich = graphic._rich_repr_threejs(online=False)
            return rich.html.get_str()

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
            return rationals.free_module(self.ambient_lattice().module_generating_set())

        def dimension(self):
            return _own_ring(SageZZ)(int(self._engine_polyhedron().dim()))

        def vertices(self):
            if self.is_lattice_polytope():
                return finite_ordered_set(
                    tuple(
                        self.ambient_lattice()(
                            tuple(
                                self._owned_integral_coordinate(coordinate)
                                for coordinate in vertex
                            )
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
                        engine_polyhedron=facet.as_polyhedron(),
                        lattice=self.ambient_lattice(),
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
            assert self.is_lattice_polytope(), (
                "the toric variety of a polytope is defined for lattice polytopes"
            )
            return self.normal_fan().toric_variety(
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
            return _engine_vertices_are_integral(self._engine_polyhedron())

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

            engine_points = finite_ordered_set(
                tuple(self._engine_polyhedron().integral_points())
            )
            return FiniteOrderedSets().from_indexed(
                engine_points,
                lambda point: self.ambient_lattice()(
                    tuple(
                        self._owned_integral_coordinate(coordinate)
                        for coordinate in point
                    )
                ),
                name="Integral points",
            )

        def interior_integral_points(self):

            return self.integral_points().filtered(
                lambda point: self._engine_polyhedron().relative_interior_contains(
                    self._engine_coordinates(point)
                ),
                name="Interior integral points",
            )

        def boundary_integral_points(self):

            interior = self.interior_integral_points()
            return self.integral_points().filtered(
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
            assert scalar >= integers.zero(), (
                "Ehrhart dilation factors are nonnegative"
            )
            return ConvexPolytopes().Integral()(
                [tuple(scalar * coordinate for coordinate in vertex) for vertex in self.vertices()],
                lattice=self.ambient_lattice(),
            )

        def ehrhart_polynomial(self, variable="t"):
            r"""Return the exact owned Ehrhart polynomial by interpolation."""
            assert self.is_lattice_polytope(), (
                "the Ehrhart polynomial is defined here for lattice polytopes"
            )

            rationals = _own_ring(SageQQ)
            integers = _own_ring(SageZZ)
            polynomial_ring = rationals.polynomial_ring(variable)
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
            assert self.is_lattice_polytope(), (
                "the h* vector is defined here for lattice polytopes"
            )
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
            assert int(self.dimension()) == int(
                self._engine_polyhedron().ambient_dim()
            ), "polar duality here requires a full-dimensional polytope"
            origin = (SageQQ.zero(),) * int(self._engine_polyhedron().ambient_dim())
            assert self._engine_polyhedron().interior_contains(origin), (
                "the polar dual is bounded only when the origin is interior"
            )
            polar = self._engine_polyhedron().polar()
            return ConvexPolytopes()(polar.vertices())

        def is_smooth(self) -> bool:
            if not self.is_lattice_polytope():
                return False
            if int(self.dimension()) != int(self._engine_polyhedron().ambient_dim()):
                return False
            return bool(self._engine_normal_fan().is_smooth())

        def _repr_(self):
            noun = "Lattice " if self.is_lattice_polytope() else "Convex "
            noun += "Polygon" if int(self.dimension()) == 2 else "Polytope"
            return f"{noun} of dimension {self.dimension()} with {self.n_vertices()} vertices"


    class Integral(CategoryWithAxiom):
        r"""Convex polytopes all of whose vertices are lattice points."""

        def an_object(self):
            r"""The standard simplex in ``ZZ^3``."""
            return self(((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)))

        @classmethod
        def _repr_object_names(cls):
            return "lattice polytopes"

        def _call_(self, vertices, lattice=None):
            r"""Construct the lattice polytope on the selected integral vertices."""
            return _polytope_in(self, vertices, lattice)

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
                    self(
                        tuple(
                            tuple(int(coordinate) for coordinate in vertex)
                            for vertex in classified.vertices()
                        )
                    )
                    for classified in ReflexivePolytopes(dimension)
                )
            )

        class Polygon(CategoryWithAxiom):
            r"""Lattice polytopes of affine dimension two."""

            def an_object(self):
                r"""The standard triangle in ``ZZ^2``."""
                return self(((0, 0), (1, 0), (0, 1)))

            @classmethod
            def _repr_object_names(cls):
                return "lattice polygons"

            def _call_(self, vertices, lattice=None):
                r"""Construct the two-dimensional lattice polytope on ``vertices``."""
                return _polytope_in(self, vertices, lattice)

    class Polygon(CategoryWithAxiom):
        r"""Convex polytopes of affine dimension two."""

        def an_object(self):
            r"""The triangle on ``0, e_1/2, e_2``, whose vertices are not integral."""
            from sage.rings.rational import Rational

            return self(((0, 0), (Rational((1, 2)), 0), (0, 1)))

        @classmethod
        def _repr_object_names(cls):
            return "convex polygons"

        def _call_(self, vertices, lattice=None):
            r"""Construct the two-dimensional convex polytope on ``vertices``."""
            return _polytope_in(self, vertices, lattice)

        class ParentMethods:
            def _repr_svg_(self):
                r"""Render this live polygon as a deterministic notebook SVG view.

                The mathematical object remains the exact owned polygon.  Floating
                point conversion is confined to this display boundary: the exact
                engine vertices are sorted cyclically about their centroid and
                affinely rescaled into a fixed SVG viewport.
                """
                vertices = tuple(
                    tuple(float(coordinate) for coordinate in vertex)
                    for vertex in self._engine_polyhedron().vertices_list()
                )
                if len(vertices) < 3:
                    return None

                center_x = sum(vertex[0] for vertex in vertices) / len(vertices)
                center_y = sum(vertex[1] for vertex in vertices) / len(vertices)
                ordered = tuple(
                    sorted(
                        vertices,
                        key=lambda vertex: atan2(
                            vertex[1] - center_y,
                            vertex[0] - center_x,
                        ),
                    )
                )
                minimum_x = min(vertex[0] for vertex in ordered)
                maximum_x = max(vertex[0] for vertex in ordered)
                minimum_y = min(vertex[1] for vertex in ordered)
                maximum_y = max(vertex[1] for vertex in ordered)
                span_x = maximum_x - minimum_x
                span_y = maximum_y - minimum_y
                scale = 260.0 / max(span_x, span_y, 1.0)
                margin = 30.0

                def screen_point(vertex):
                    x, y = vertex
                    return (
                        margin + (x - minimum_x) * scale,
                        margin + (maximum_y - y) * scale,
                    )

                points = " ".join(
                    f"{x:.6g},{y:.6g}" for x, y in map(screen_point, ordered)
                )
                width = 2 * margin + span_x * scale
                height = 2 * margin + span_y * scale
                return (
                    f'<svg xmlns="http://www.w3.org/2000/svg" '
                    f'viewBox="0 0 {width:.6g} {height:.6g}" '
                    f'width="{width:.6g}" height="{height:.6g}">'
                    '<polygon points="'
                    + points
                    + '" fill="none" stroke="currentColor" stroke-width="2"/>'
                    "</svg>"
                )


def LatticePolytopes() -> Category:
    r"""The category of lattice polytopes."""
    return ConvexPolytopes().Integral()


def ConvexPolygons() -> Category:
    r"""The category of convex polygons."""
    return ConvexPolytopes().Polygon()


def LatticePolygons() -> Category:
    r"""The category of lattice polygons."""
    return ConvexPolytopes().Integral().Polygon()


def _polytope_in(category, vertices, lattice):
    r"""The polytope on ``vertices``, which the caller asserts lies in ``category``."""
    polytope = _convex_polytope(vertices, lattice=lattice)
    assert polytope in category, f"the vertices do not span an object of {category}"
    return polytope


def _engine_vertices_are_integral(engine_polyhedron) -> bool:
    r"""Whether every vertex of the exact polyhedron is a lattice point."""
    return all(
        coordinate in SageZZ
        for vertex in engine_polyhedron.vertices()
        for coordinate in vertex
    )


def _convex_polytope(
    vertices=None,
    lattice=None,
    engine_polyhedron=None,
):
    r"""The polytope on its data, constructed once in the category it lies in.

    A polytope is fixed by its vertices, by an owned polytope passed again, or
    by an exact polyhedron the private computation layer produced (from a
    face, a dilation, or a halfspace description); the third route is named
    rather than recognized.  Integrality of the vertices and affine dimension
    two are the two axioms the finer categories state, so they are decided on
    the polyhedron and the object is constructed in the category they select.
    """
    integers = _own_ring(SageZZ)
    rationals = _own_ring(SageQQ)
    if engine_polyhedron is not None:
        polyhedron = engine_polyhedron
    elif vertices in ConvexPolytopes():
        polyhedron = vertices._engine_polyhedron()
        if lattice is None:
            lattice = vertices.ambient_lattice()
    else:
        engine_vertices = [
            tuple(
                _engine_element(rationals, _owned_rational(coordinate))
                for coordinate in vertex
            )
            for vertex in vertices
        ]
        polyhedron = Polyhedron(vertices=engine_vertices, base_ring=SageQQ)

    ambient_dimension = int(polyhedron.ambient_dim())
    if lattice is None:
        lattice = integers.free_module(ambient_dimension)
    assert lattice.base_ring() is integers, (
        "the ambient lattice of a rational polytope is an owned ZZ-module"
    )
    assert int(lattice.module_rank()) == ambient_dimension, (
        "the ambient lattice rank must equal the coordinate dimension"
    )

    placement = ConvexPolytopes()
    if _engine_vertices_are_integral(polyhedron):
        placement = placement.Integral()
    if int(polyhedron.dim()) == 2:
        placement = placement.Polygon()
    return _object_of(
        placement,
        engine_polyhedron=polyhedron,
        ambient_lattice=lattice,
    )


__all__ = [
    "ConvexPolygons",
    "ConvexPolytopes",
    "LatticePolygons",
    "LatticePolytopes",
    "RegularPolytopes",
]
