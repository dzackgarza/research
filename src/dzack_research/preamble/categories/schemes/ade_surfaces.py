r"""ADE log pairs: the toric base of an integral ADE polygon.

An ADE type of the families \(A\), \(D\), \(E\) and their affine partners is
recorded by an integral polygon \(Q\) in the plane together with a
distinguished rational point \(p^*\) on its boundary, and by decorations on
the sides of \(Q\) incident to \(p^*\).  The toric surface \(Y=V_Q\) of the
normal fan of \(Q\) is the base of the double cover that carries the ADE
surface, and the boundary of the toric log pair \((Y,\Delta)\) splits into the
*blue* divisor \(C\), summing the invariant divisors whose facet of \(Q\)
contains \(p^*\), and its complement \(C'\).

The polygon table transcribed here is the one the archived preamble recorded
at ``archives/preamble/categories/schemes/ade_surfaces.sage``, whose stated
source is Table 1 of Alexeev--Thompson, *ADE surfaces and their moduli*.  It
has not been re-checked against that paper in this port.

What is **not** here, and why: the branch polynomial \(f\) with Newton polygon
\(Q\), the double cover \(X=V(z^2+f)\to Y\), its deck involution, and the
boundary \(D=\pi^*C\) on \(X\).  The archived branch polynomials return one
polynomial for four different decorated \(A\) families and one for both \(D\)
families, so they do not distinguish the types they are indexed by and cannot
be ported as recorded; and the cover itself needs the general cyclic-cover
construction in the root TODO.md §13, which is not live.
"""

from dataclasses import dataclass

from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.log_pairs import ToricLogPairs
from dzack_research.preamble.categories.schemes.polytopes import (
    ConvexPolytope,
    LatticePolygon,
)
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_filter,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import NN
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.tensors.tensor import tensor
from dzack_research.static_types import ProductOfNaturalNumbers


def _side(first, second):
    r"""The side of ``Q`` joining two vertices, as a point of ``NN x NN``.

    A vertex of ``Q`` is named by its position in the boundary order, which is
    a natural number, so a side is a point of the square of the natural
    numbers.
    """
    return (NN**2)((first, second))


@dataclass(frozen=True)
class SideDecoration:
    r"""The decoration of one side of ``Q`` incident to ``p*``.

    ``side`` is the point of ``NN x NN`` naming the two vertices the side
    joins, ``length_class`` is ``"long"`` or ``"short"``, and
    ``vertex_colour`` is ``"white"`` or ``"black"``.  The classification is
    Alexeev--Thompson's, and it distinguishes ADE types whose polygons
    otherwise agree.
    """

    side: ProductOfNaturalNumbers
    length_class: str
    vertex_colour: str


def _rationals():
    return _own_ring(SageQQ)


def _rational_point(coordinates):
    r"""A rational point of the plane, in the coordinate frame of ``Q``."""
    rationals = _rationals()
    return tensor.vector(
        rationals,
        tuple(rationals._from_engine_element(SageQQ(coordinate)) for coordinate in coordinates),
    )


def _has(variant, *names) -> bool:
    return any(name in variant for name in names)


def _ade_parameter(letter, rank, variant, affine):
    r"""The half-rank parameter ``n`` the polygon of a family is written in."""
    if letter == "A":
        if _has(variant[:1], "short"):
            return (rank + 3) // 2
        if _has(variant[1:2], "short"):
            return (rank + 2) // 2
        return (rank + 1) // 2
    if letter == "D":
        return (rank + 1) // 2
    return 2


def _affine_polygon_data(letter, rank, parameter):
    if letter == "A":
        return (((0, 2), (0, 0), (2 * parameter, 0), (parameter, 2)), (SageQQ(parameter) / 2, 1))
    if letter == "D":
        return (((0, 2), (0, 0), (2 * parameter - 4, 0), (4, 2)), (2, 2))
    assert letter == "E", "the affine ADE families are A, D and E"
    if rank == 6:
        return (((0, 3), (0, 0), (3, 0)), (1, 1))
    if rank == 7:
        return (((0, 4), (0, 0), (4, 0)), (2, 2))
    assert rank == 8, "the affine E family has rank 6, 7 or 8"
    return (((0, 3), (0, 0), (6, 0)), (2, 2))


def _a_family_polygon_data(rank, variant, parameter):
    left_short = _has(variant[:1], "short")
    right_short = _has(variant[1:2], "short")
    if _has(variant, "primed", "prime", "p"):
        return (
            ((2, 2), (0, 1), (0, 0), (2 * parameter - 2, 0)),
            (2, 2),
            finite_family((), name="Side decorations"),
        )
    if left_short and right_short:
        vertices = ((0, 2), (1, 0), (2 * parameter - 1, 0))
        decorations = (
            SideDecoration(_side(0, 1), "short", "black"),
            SideDecoration(_side(0, 2), "short", "black"),
        )
    elif left_short:
        vertices = ((0, 2), (1, 0), (2 * parameter - 1, 0))
        decorations = (
            SideDecoration(_side(0, 1), "short", "black"),
            SideDecoration(_side(0, 2), "long", "white"),
        )
    elif right_short:
        vertices = ((0, 2), (0, 0), (2 * parameter - 1, 0))
        decorations = (
            SideDecoration(_side(0, 1), "long", "white"),
            SideDecoration(_side(0, 2), "short", "black"),
        )
    else:
        vertices = ((0, 2), (0, 0), (2 * parameter, 0))
        decorations = (
            SideDecoration(_side(0, 1), "long", "white"),
            SideDecoration(_side(0, 2), "long", "white"),
        )
    return (vertices, (0, 2), finite_family(decorations, name="Side decorations"))


def _d_family_polygon_data(rank, variant, parameter):
    if _has(variant, "primed", "prime", "p"):
        vertices = ((2, 2), (0, 2), (0, 0), (2 * parameter - 4, 0), (parameter, 1))
    elif "short" in variant or rank % 2 == 1:
        vertices = ((2, 2), (0, 2), (0, 0), (2 * parameter - 3, 0))
    else:
        vertices = ((2, 2), (0, 2), (0, 0), (2 * parameter - 2, 0))
    return (vertices, (2, 2))


def _e_family_polygon_data(rank):
    assert rank in (6, 7, 8), "the E family has rank 6, 7 or 8"
    last = {6: 3, 7: 4, 8: 5}[rank]
    return (((2, 2), (0, 3), (0, 0), (last, 0)), (2, 2))


def _ade_polygon_data(letter, rank, variant, affine):
    r"""The polygon, distinguished point and side decorations of one ADE type."""
    parameter = _ade_parameter(letter, rank, variant, affine)
    empty = finite_family((), name="Side decorations")
    if affine:
        vertices, point = _affine_polygon_data(letter, rank, parameter)
        return (vertices, point, empty)
    if letter == "A":
        return _a_family_polygon_data(rank, variant, parameter)
    if letter == "D":
        vertices, point = _d_family_polygon_data(rank, variant, parameter)
        return (vertices, point, empty)
    assert letter == "E", "an ADE type has letter A, D or E"
    vertices, point = _e_family_polygon_data(rank)
    return (vertices, point, empty)


def _engine_pairing_values(engine_polyhedron, engine_ray):
    r"""The values ``<v, u>`` on the vertices of the polytope."""
    return tuple(
        sum(int(entry) * coordinate for entry, coordinate in zip(engine_ray, vertex))
        for vertex in engine_polyhedron.vertices()
    )


def _supports_point(engine_polyhedron, engine_ray, engine_point):
    r"""Whether the point lies on the face where ``u`` is minimized on ``Q``.

    For an inner normal ``u`` of a facet ``F`` of ``Q``, ``F`` is exactly the
    locus in ``Q`` where ``<-, u>`` attains its minimum, so this is the
    condition that ``p*`` lies on ``F``.  The arithmetic is exact and stays on
    the engine side, which is the one frame crossing this file performs.
    """
    value = sum(int(entry) * coordinate for entry, coordinate in zip(engine_ray, engine_point))
    return value == min(_engine_pairing_values(engine_polyhedron, engine_ray))


class ADELogPairs(OwnedCategoryOverBaseRing):
    r"""Toric log pairs equipped with an ADE type, its polygon and ``p*``."""

    def an_object(self):
        r"""The base log pair of the ``A_2`` polygon."""
        return ADELogPair("A", 2, self.base_ring())

    def _repr_object_names(self):
        return f"ADE log pairs over {self.base_ring()}"

    def super_categories(self):
        return [ToricLogPairs(self.base_ring())]

    class ParentMethods:
        def __init__(
            self,
            dynkin_letter,
            dynkin_rank,
            dynkin_variant,
            is_affine_type,
            polygon,
            polygon_vertex_order,
            distinguished_point,
            side_decorations,
            **rest,
        ) -> None:
            self._preamble_dynkin_letter = dynkin_letter
            self._preamble_dynkin_rank = dynkin_rank
            self._preamble_dynkin_variant = dynkin_variant
            self._preamble_is_affine_type = is_affine_type
            self._preamble_polygon = polygon
            self._preamble_polygon_vertex_order = polygon_vertex_order
            self._preamble_distinguished_point = distinguished_point
            self._preamble_side_decorations = side_decorations
            super().__init__(**rest)

        def scheme(self):
            r"""Return the scheme of this ADE base log pair, namely ``Y=V_Q``."""
            return self.log_scheme()

        def toric_scheme(self):
            r"""Return the ambient toric scheme of this base pair, again ``Y=V_Q``."""
            return self.log_scheme()

        def base(self):
            r"""Return this base ADE log pair itself."""
            return self

        def is_base(self) -> bool:
            return True

        def is_cover(self) -> bool:
            return False

        def codimension_in_toric_scheme(self):
            r"""Return zero: the base scheme is its own toric ambient scheme."""
            return _own_ring(SageZZ).zero()

        def dynkin_letter(self) -> str:
            return self._preamble_dynkin_letter

        def dynkin_rank(self):
            return _own_ring(SageZZ)(self._preamble_dynkin_rank)

        def letter(self) -> str:
            r"""Return the ADE letter; archived synonym for :meth:`dynkin_letter`."""
            return self.dynkin_letter()

        def rank(self):
            r"""Return the ADE rank; archived synonym for :meth:`dynkin_rank`."""
            return self.dynkin_rank()

        def dynkin_variant(self):
            r"""The decorations naming this member of its family."""
            return finite_family(
                self._preamble_dynkin_variant,
                name="Dynkin variant",
            )

        def is_affine_type(self) -> bool:
            return self._preamble_is_affine_type

        def variant(self):
            r"""Return the selected ADE side-decoration variant."""
            return self.dynkin_variant()

        def is_affine(self) -> bool:
            r"""Return whether this is an affine ADE family member."""
            return self.is_affine_type()

        @cached_method
        def coxeter_diagram(self):
            r"""The owned Coxeter/Dynkin diagram of this finite or affine ADE type."""
            from dzack_research.preamble.categories.coxeter_diagrams import (
                CoxeterDiagrams,
            )

            cartan_type = [self.dynkin_letter(), int(self.dynkin_rank())]
            if self.is_affine_type():
                cartan_type.append(1)
            return CoxeterDiagrams().from_cartan_type(cartan_type)

        def dynkin_diagram(self):
            r"""Return the selected ADE Dynkin diagram; archived mathematical name."""
            return self.coxeter_diagram()

        def polygon(self):
            r"""The integral ADE polygon ``Q``."""
            return self._preamble_polygon

        def polygon_vertex_order(self):
            r"""Return the boundary-ordered vertices used by the ADE side data.

            ``SideDecoration.side`` is indexed by positions in this family.
            A polytope as an unordered convex hull does not retain that
            presentation, so the ADE structure owns the order separately.
            """
            return self._preamble_polygon_vertex_order

        @cached_method
        def vertices(self):
            r"""Return the vertices of ``Q`` as the polygon's owned finite set."""
            return self.polygon().vertices()

        def distinguished_point(self):
            r"""The distinguished rational point ``p*`` on the boundary of ``Q``."""
            return self._preamble_distinguished_point

        def p_star(self):
            r"""Return the distinguished point ``p*``; archived mathematical name."""
            return self.distinguished_point()

        def polarizing_polytope(self):
            r"""Return the ADE polarizing polygon ``Q``."""
            return self.polygon()

        def side_decorations(self):
            r"""The decorations of the sides of ``Q`` incident to ``p*``."""
            return self._preamble_side_decorations

        def ade_svg(self):
            r"""Return a deterministic SVG view of the retained ADE polygon data.

            This is a view of the live log-pair object, not a second polygon
            presentation.  Vertices come from :meth:`polygon`, ``p*`` from
            :meth:`distinguished_point`, and the decorated sides from
            :meth:`side_decorations`.  Floating-point conversion is confined
            to this rendering boundary; stable ``data-*`` attributes retain
            the ADE semantics for notebook inspection and regression tests.
            """
            vertices = tuple(
                tuple(float(coordinate) for coordinate in vertex)
                for vertex in self.polygon_vertex_order()
            )
            if len(vertices) < 3:
                return None
            point = tuple(float(coordinate) for coordinate in self.p_star())
            all_x = tuple(vertex[0] for vertex in vertices) + (point[0],)
            all_y = tuple(vertex[1] for vertex in vertices) + (point[1],)
            minimum_x, maximum_x = min(all_x), max(all_x)
            minimum_y, maximum_y = min(all_y), max(all_y)
            span_x = max(maximum_x - minimum_x, 1.0)
            span_y = max(maximum_y - minimum_y, 1.0)
            scale = 260.0 / max(span_x, span_y)
            margin = 30.0

            def screen(coordinates):
                x, y = coordinates
                return (
                    margin + (x - minimum_x) * scale,
                    margin + (maximum_y - y) * scale,
                )

            width = 2 * margin + span_x * scale
            height = 2 * margin + span_y * scale
            polygon_points = " ".join(
                f"{screen(vertex)[0]:.2f},{screen(vertex)[1]:.2f}"
                for vertex in vertices
            )
            lines = [
                (
                    f'<svg xmlns="http://www.w3.org/2000/svg" '
                    f'viewBox="0 0 {width:.2f} {height:.2f}" '
                    f'data-role="ade-polygon" data-ade-type="{self.dynkin_letter()}{int(self.dynkin_rank())}">'
                ),
                f'<polygon data-role="polygon" points="{polygon_points}" fill="none" stroke="currentColor"/>',
            ]
            for position in self.side_decorations().index_set():
                decoration = self.side_decorations()[position]
                first = int(decoration.side[0])
                second = int(decoration.side[1])
                start = screen(vertices[first])
                end = screen(vertices[second])
                lines.append(
                    f'<line data-role="decorated-side" data-length-class="{decoration.length_class}" '
                    f'data-vertex-colour="{decoration.vertex_colour}" '
                    f'data-side="{first},{second}" x1="{start[0]:.2f}" y1="{start[1]:.2f}" '
                    f'x2="{end[0]:.2f}" y2="{end[1]:.2f}" stroke="currentColor" stroke-width="3"/>'
                )
            blue_coordinates = {
                tuple(float(coordinate) for coordinate in boundary_point)
                for boundary_point in self.distinguished_boundary_points()
            }
            for boundary_point in sorted(blue_coordinates):
                rendered = screen(boundary_point)
                lines.append(
                    f'<circle data-role="blue-boundary-point" data-lattice-point="{boundary_point[0]:g},{boundary_point[1]:g}" '
                    f'cx="{rendered[0]:.2f}" cy="{rendered[1]:.2f}" r="3"/>'
                )
            rendered_point = screen(point)
            lines.append(
                f'<circle data-role="p-star" data-point="{point[0]:g},{point[1]:g}" '
                f'cx="{rendered_point[0]:.2f}" cy="{rendered_point[1]:.2f}" r="6"/>'
            )
            lines.append("</svg>")
            return "".join(lines)

        def _repr_svg_(self):
            r"""Notebook SVG view retaining the ADE decorations and ``p*``."""
            return self.ade_svg()

        @cached_method
        def integral_invariants(self):
            r"""Return the archived integral polygon invariants as an owned family.

            The archive stored these values in a Python ``NamedTuple``.  Here
            their labels are the index set and the values retain their actual
            owned scalar/cardinal parents: the Euclidean volume is rational,
            normalized volume and dimension are integral, and lattice-point
            counts are cardinals.
            """
            polygon = self.polarizing_polytope()
            integers = _own_ring(SageZZ)
            labels = finite_ordered_set(
                (
                    "dimension",
                    "volume",
                    "normalized_volume",
                    "n_integral_points",
                    "n_interior_points",
                    "n_boundary_points",
                )
            )
            values = {
                "dimension": integers(self.toric_scheme().relative_dimension()),
                "volume": polygon.volume(),
                "normalized_volume": polygon.normalized_volume(),
                "n_integral_points": polygon.n_integral_points(),
                "n_interior_points": polygon.n_interior_points(),
                "n_boundary_points": polygon.n_boundary_points(),
            }
            return finite_indexed_family(
                labels,
                values.__getitem__,
                name=f"Integral invariants of {polygon}",
            )

        def _blue_rays(self):
            polygon = self.polygon()
            engine_polyhedron = polygon._engine_polyhedron()
            engine_point = polygon._engine_coordinates(self.distinguished_point())
            return finite_ordered_filter(
                self.fan().cones(1),
                lambda ray: _supports_point(
                    engine_polyhedron,
                    ray._engine_cone().rays()[0],
                    engine_point,
                ),
                name="Blue rays",
            )

        @cached_method
        def distinguished_boundary_points(self):
            r"""Return the integral boundary points lying on a blue facet of ``Q``.

            A blue facet is one containing the distinguished point ``p*``.
            Equivalently its inner normal is one of :meth:`_blue_rays`, so a
            boundary lattice point lies on a blue facet exactly when it
            minimizes the corresponding linear functional on ``Q``.  The
            returned points remain elements of the polygon's owned ambient
            lattice.
            """
            polygon = self.polygon()
            engine_polyhedron = polygon._engine_polyhedron()
            blue_rays = self._blue_rays()

            def lies_on_blue_facet(point):
                engine_point = polygon._engine_coordinates(point)
                return any(
                    _supports_point(
                        engine_polyhedron,
                        ray._engine_cone().rays()[0],
                        engine_point,
                    )
                    for ray in blue_rays
                )

            return finite_ordered_filter(
                polygon.boundary_integral_points(),
                lies_on_blue_facet,
                name="Distinguished ADE boundary points",
            )

        def blue_divisor(self):
            r"""``C``: the invariant divisors whose facet of ``Q`` contains ``p*``."""
            group = self.log_scheme().torus_invariant_divisor_group()
            blue = self._blue_rays()
            return group.linear_combination(
                {ray: _own_ring(SageZZ).one() for ray in blue}
            )

        def blue_line_divisor(self):
            r"""Return the blue divisor ``C``; archived mathematical name."""
            return self.blue_divisor()

        def complementary_divisor(self):
            r"""``C'``: the rest of the toric boundary, so that ``C + C' = Delta``."""
            return self.boundary_divisor() - self.blue_divisor()

        @cached_method
        def pyramid(self):
            r"""The 3-polytope ``P``: the cone over ``Q`` with apex ``(p*, 2)``.

            ``P`` is a lattice polytope exactly when ``p*`` is a lattice point;
            the affine families place ``p*`` at a half-integral point, and for
            those ``P`` is a rational polytope.
            """
            polygon = self.polygon()
            base = tuple(
                (*tuple(vertex), SageQQ.zero())
                for vertex in polygon._engine_polyhedron().vertices()
            )
            apex = (
                *polygon._engine_coordinates(self.distinguished_point()),
                SageQQ(2),
            )
            return ConvexPolytope((*base, apex))

        def cover_toric_threefold(self):
            r"""``V_P``, the toric threefold the double cover is cut out of."""
            pyramid = self.pyramid()
            assert pyramid.is_lattice_polytope(), (
                "V_P is the toric variety of the pyramid, which needs an "
                "integral apex; this ADE type places p* at a non-lattice point"
            )
            return pyramid.toric_variety(self.log_scheme().scheme_base_ring())

        def _repr_(self) -> str:
            prefix = "affine " if self.is_affine_type() else ""
            return (
                f"ADE log pair of {prefix}type "
                f"{self.dynkin_letter()}_{self.dynkin_rank()} on {self.polygon()}"
            )


def ADELogPair(dynkin_letter, dynkin_rank, base_ring, variant=(), affine=False):
    r"""The base log pair ``(V_Q, Delta)`` of one ADE type."""
    letter = str(dynkin_letter).upper()
    assert letter in ("A", "D", "E"), "an ADE type has letter A, D or E"
    rank = int(dynkin_rank)
    assert rank >= 1, "an ADE type has positive rank"
    variant = tuple(variant)

    vertices, point, decorations = _ade_polygon_data(letter, rank, variant, bool(affine))
    polygon = LatticePolygon(vertices)
    toric_base = polygon.toric_variety(base_ring)
    return object_of(
        ADELogPairs(toric_base.scheme_base_ring()),
        dynkin_letter=letter,
        dynkin_rank=rank,
        dynkin_variant=variant,
        is_affine_type=bool(affine),
        polygon=polygon,
        polygon_vertex_order=finite_family(
            tuple(_rational_point(vertex) for vertex in vertices),
            name="ADE polygon boundary order",
        ),
        distinguished_point=_rational_point(point),
        side_decorations=decorations,
        log_scheme=toric_base,
        boundary_divisor=toric_base.toric_boundary_divisor(),
    )


__all__ = ["ADELogPair", "ADELogPairs", "SideDecoration"]
