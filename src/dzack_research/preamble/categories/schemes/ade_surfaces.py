r"""ADE log pairs: the toric base of an integral ADE polygon.

An ADE type of the families \(A\), \(D\), \(E\) and their affine partners is
recorded by an integral polygon \(Q\) in the plane together with a
distinguished rational point \(p^*\) on its boundary, and by decorations on
the sides of \(Q\) incident to \(p^*\).  The toric surface \(Y=V_Q\) of the
normal fan of \(Q\) is the base of the double cover that carries the ADE
surface, and the boundary of the toric log pair \((Y,\Delta)\) splits into the
*blue* divisor \(C\), summing the invariant divisors whose facet of \(Q\)
contains \(p^*\), and its complement \(C'\).

The low-level polygon constructor retains the archived table for compatibility.
The source-admitted :class:`AT21ToricADEPair` separately checks the toric shape
range against Alexeev--Thompson, *ADE surfaces and their moduli*, Theorems 4.8
and 4.10 and Lemma 3.25, and checks Lemma 3.4's divisor identity
``L=-2(K_Y+C)=2C'`` on the live toric surface.  Branch sections are elements of
that actual polarizing linear system; Table 5 normal forms are admitted only
where their affine-coordinate support has been checked against the retained
polygon.
"""

from dataclasses import dataclass

from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.log_pairs import ToricLogPairs
from dzack_research.preamble.categories.schemes.polytopes import (
    ConvexPolytopes,
    LatticePolygons,
)
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import NN
from dzack_research.preamble.owned_category import _object_of
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


def _validated_at21_low_level_variant(letter, rank, variant, affine):
    if letter not in ("A", "D", "E"):
        raise ValueError("an AT21 ADE shape has type A, D or E")
    if rank < 1:
        raise ValueError("an AT21 ADE rank is positive")
    if affine:
        if variant != "pure":
            raise ValueError("the represented toric affine shapes are the pure source shapes")
        if letter == "D" and rank >= 4 and rank % 2 == 0:
            return ()
        if letter == "E" and rank in (7, 8):
            return ()
        raise ValueError(
            "AT21 toric affine shapes represented here are tilde D_even, tilde E7 and tilde E8; tilde A is nontoric"
        )
    if letter == "A":
        if variant == "pure" and rank % 2 == 1:
            return ()
        if variant == "short" and rank % 2 == 0:
            return ("long", "short")
        if variant == "both-short" and rank % 2 == 1:
            return ("short", "short")
        if variant == "prime":
            return ("prime",)
        raise ValueError(
            "finite toric A shapes use odd pure A, even one-short A, odd both-short A, or the AT21 toric priming"
        )
    if letter == "D":
        if variant == "pure" and rank >= 4 and rank % 2 == 0:
            return ()
        if variant == "short" and rank >= 5 and rank % 2 == 1:
            return ("short",)
        if variant == "prime" and rank >= 4 and rank % 2 == 0:
            return ("prime",)
        raise ValueError(
            "finite toric D shapes use even D, odd one-short D, or the even toric priming of AT21 Lemma 3.25"
        )
    if rank not in (6, 7, 8) or variant != "pure":
        raise ValueError("finite toric E shapes are the source E6, E7 and E8 pure shapes")
    return ()


class ADELogPairs(OwnedCategoryOverBaseRing):
    r"""Toric log pairs equipped with an ADE type, its polygon and ``p*``."""

    def an_object(self):
        r"""The base log pair of the ``A_2`` polygon."""
        return self("A", 2)

    def _call_(self, dynkin_letter, dynkin_rank, variant=(), affine=False):
        r"""Construct the base log pair of one ADE type over this category's base."""
        letter = str(dynkin_letter).upper()
        assert letter in ("A", "D", "E"), "an ADE type has letter A, D or E"
        rank = int(dynkin_rank)
        assert rank >= 1, "an ADE type has positive rank"
        variant = tuple(variant)

        vertices, point, decorations = _ade_polygon_data(
            letter,
            rank,
            variant,
            bool(affine),
        )
        polygon = LatticePolygons()(vertices)
        toric_base = polygon.toric_variety(self.base_ring())
        return _object_of(
            self,
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

    def at21(self, dynkin_letter, dynkin_rank, *, variant="pure", affine=False):
        r"""Construct the source-admitted toric AT21 enhancement of one ADE pair."""
        letter = str(dynkin_letter).upper()
        rank = int(dynkin_rank)
        source_variant = str(variant).lower().replace("_", "-")
        affine = bool(affine)
        low_variant = _validated_at21_low_level_variant(
            letter,
            rank,
            source_variant,
            affine,
        )
        pair = self(letter, rank, variant=low_variant, affine=affine)
        branch_class = pair.log_scheme().polarizing_divisor()
        expected = _own_ring(SageZZ)(2) * pair.complementary_divisor()
        if branch_class != expected:
            raise ArithmeticError(
                "the selected polygon does not satisfy AT21 Lemma 3.4: "
                "L=-2(K_Y+C)=2C'"
            )
        branch_line_bundle = pair.log_scheme().invertible_sheaf_of_divisor(branch_class)
        return ToricLogPairs(self.base_ring())(
            pair.log_scheme(),
            pair.blue_divisor(),
            _engine=_AT21ToricADEPairEngine,
            construction_data={
                "base_pair": pair,
                "source_variant": source_variant,
                "branch_divisor_class": branch_class,
                "branch_line_bundle": branch_line_bundle,
            },
        )

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
            self._dynkin_letter = dynkin_letter
            self._dynkin_rank = dynkin_rank
            self._dynkin_variant = dynkin_variant
            self._is_affine_type = is_affine_type
            self._polygon = polygon
            self._polygon_vertex_order = polygon_vertex_order
            self._distinguished_point = distinguished_point
            self._side_decorations = side_decorations
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
            return self._dynkin_letter

        def dynkin_rank(self):
            return _own_ring(SageZZ)(self._dynkin_rank)

        def letter(self) -> str:
            r"""Return the ADE letter; archived synonym for :meth:`dynkin_letter`."""
            return self.dynkin_letter()

        def rank(self):
            r"""Return the ADE rank; archived synonym for :meth:`dynkin_rank`."""
            return self.dynkin_rank()

        def dynkin_variant(self):
            r"""The decorations naming this member of its family."""
            return finite_family(
                self._dynkin_variant,
                name="Dynkin variant",
            )

        def is_affine_type(self) -> bool:
            return self._is_affine_type

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
            return self._polygon

        def polygon_vertex_order(self):
            r"""Return the boundary-ordered vertices used by the ADE side data.

            ``SideDecoration.side`` is indexed by positions in this family.
            A polytope as an unordered convex hull does not retain that
            presentation, so the ADE structure owns the order separately.
            """
            return self._polygon_vertex_order

        @cached_method
        def vertices(self):
            r"""Return the vertices of ``Q`` as the polygon's owned finite set."""
            return self.polygon().vertices()

        def distinguished_point(self):
            r"""The distinguished rational point ``p*`` on the boundary of ``Q``."""
            return self._distinguished_point

        def p_star(self):
            r"""Return the distinguished point ``p*``; archived mathematical name."""
            return self.distinguished_point()

        def polarizing_polytope(self):
            r"""Return the ADE polarizing polygon ``Q``."""
            return self.polygon()

        def side_decorations(self):
            r"""The decorations of the sides of ``Q`` incident to ``p*``."""
            return self._side_decorations

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
            return self.fan().cones(1).filtered(
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

            return polygon.boundary_integral_points().filtered(
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

            ``P`` is a lattice polytope exactly when ``p*`` is a lattice point.
            In the affine ``A`` family the archived formula ``p*=(n/2,1)``
            can be integral or half-integral according to ``n``; in the latter
            cases ``P`` is a rational polytope.
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
            return ConvexPolytopes()((*base, apex))

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


__all__ = ["ADELogPairs", "SideDecoration"]


class _AT21ToricADEPairEngine:
    r"""A source-admitted toric ADE base pair with its branch linear system.

    This is the toric part of Alexeev--Thompson's classification, not a second
    scheme model.  The underlying object of :class:`ADELogPairs` remains the actual toric
    surface with its boundary.  Admission uses AT21 Theorems 4.8 and 4.10 for
    the pure finite/affine shapes and Lemma 3.25 for the primed shapes that
    remain toric.  In particular ``tilde A`` is not admitted here (AT21
    Remark 3.11) and there is no affine ``E6`` case.

    ``variant`` is one of ``pure``, ``short``, ``both-short`` or ``prime``.
    The name records the source shape rather than asking the archive polygon
    parser to infer parity from a loose token sequence.
    """

    def __init__(
        self,
        *,
        base_pair,
        source_variant,
        branch_divisor_class,
        branch_line_bundle,
        **rest,
    ) -> None:
        self._base_pair = base_pair
        self._source_variant = source_variant
        self._branch_divisor_class = branch_divisor_class
        self._branch_line_bundle = branch_line_bundle
        super().__init__(**rest)

    def base_pair(self):
        return self._base_pair

    def scheme(self):
        return self.log_scheme()

    toric_scheme = scheme

    def complementary_divisor(self):
        return self.base_pair().complementary_divisor()

    def source_variant(self):
        return self._source_variant

    def dynkin_letter(self):
        return self.base_pair().dynkin_letter()

    def dynkin_rank(self):
        return self.base_pair().dynkin_rank()

    def is_affine_type(self):
        return self.base_pair().is_affine_type()

    def polygon(self):
        return self.base_pair().polygon()

    def distinguished_point(self):
        return self.base_pair().distinguished_point()

    def side_decorations(self):
        return self.base_pair().side_decorations()

    def coxeter_diagram(self):
        return self.base_pair().coxeter_diagram()

    def pyramid(self):
        return self.base_pair().pyramid()

    def cover_toric_threefold(self):
        return self.base_pair().cover_toric_threefold()

    def branch_divisor_class(self):
        r"""Return ``L=-2(K_Y+C)=2C'`` from AT21 Lemma 3.4."""
        return self._branch_divisor_class

    def branch_line_bundle(self):
        return self._branch_line_bundle

    def branch_section_space(self):
        return self.scheme().divisor_section_space(self.branch_divisor_class())

    def branch_section(self, character_coefficients):
        r"""Construct a branch section from coefficients indexed by lattice points of ``Q``."""
        sections = self.branch_section_space()
        characters = {
            tuple(int(coordinate) for coordinate in character): character
            for character in sections.module_generating_set()
        }
        coefficients = {}
        for coordinates, coefficient in dict(character_coefficients).items():
            key = tuple(int(value) for value in coordinates)
            if key not in characters:
                raise ValueError(f"{key} is not a lattice point of the ADE branch polytope")
            value = self.scheme().scheme_base_ring()(coefficient)
            if value != self.scheme().scheme_base_ring().zero():
                coefficients[characters[key]] = value
        return sections.linear_combination(coefficients)

    @cached_method
    def full_newton_branch_section(self):
        r"""A branch section whose Newton polygon is the whole selected ``Q``."""
        return self.branch_section(
            {
                tuple(int(coordinate) for coordinate in vertex): self.scheme().scheme_base_ring().one()
                for vertex in self.polygon().vertices()
            }
        )

    def branch_newton_polygon(self, section):
        r"""Return the convex hull of the nonzero character terms of ``section``."""
        from dzack_research.preamble.categories.schemes.polytopes import LatticePolygons

        sections = self.branch_section_space()
        coefficients = sections.framing_coefficients(sections(section))
        support = tuple(
            tuple(int(coordinate) for coordinate in character)
            for character, coefficient in coefficients.items()
            if coefficient != sections.base_ring().zero()
        )
        if len(support) < 3:
            raise ValueError("a branch Newton polygon requires two-dimensional support")
        return LatticePolygons()(support, lattice=self.scheme().character_lattice())

    def source_normal_form_section(self, *, constant=1):
        r"""Return the AT21 Table 5 normal-form specimen in the D/E families.

        With all deformation parameters except ``c_0`` specialized to zero,
        Table 5 gives
        ``-x^2y^2/4 + y^2 + x^(n-2) + c_0`` for ``D_n`` and
        ``-x^2y^2/4 + y^3 + x^(n-3) + c_0`` for ``E_n``.
        The four exponent vectors are literal character-lattice points of the
        retained source polygon.  The A-table uses a different affine chart
        normalization and is deliberately not guessed here.
        """
        assert not self.is_affine_type(), (
            "the represented Table 5 normal forms require a finite D/E shape"
        )
        rank = int(self.dynkin_rank())
        if self.dynkin_letter() == "D":
            terms = {
                (2, 2): -SageQQ(1) / 4,
                (0, 2): 1,
                (rank - 2, 0): 1,
                (0, 0): constant,
            }
        elif self.dynkin_letter() == "E":
            terms = {
                (2, 2): -SageQQ(1) / 4,
                (0, 3): 1,
                (rank - 3, 0): 1,
                (0, 0): constant,
            }
        else:
            assert self.dynkin_letter() in ("D", "E"), (
                "the represented Table 5 branch normal form is the D/E source normalization; "
                "type A uses its separate affine-chart normalization"
            )
        return self.branch_section(terms)

    def branch_subscheme(self, section):
        return self.scheme().zero_subscheme_of_divisor_section(
            self.branch_divisor_class(),
            section,
            line_bundle=self.branch_line_bundle(),
        )

    def double_cover(self, section=None):
        selected = (
            self.full_newton_branch_section()
            if section is None
            else self.branch_section_space()(section)
        )
        return _at21_ade_double_cover(self, selected)

    def _repr_(self):
        prefix = "affine " if self.is_affine_type() else ""
        return f"AT21 toric ADE pair of {prefix}type {self.dynkin_letter()}_{self.dynkin_rank()} ({self.source_variant()})"



class _AT21ADEDoubleCoverEngine:
    r"""Private realization of the AT21 hypersurface scheme with its cover data."""

    def __init__(
        self,
        *,
        base_pair,
        branch_section,
        ambient_toric_threefold,
        ambient_polarizing_divisor,
        ambient_hypersurface_section,
        ambient_projection,
        **rest,
    ) -> None:
        self._base_pair = base_pair
        self._branch_section = branch_section
        self._ambient = ambient_toric_threefold
        self._ambient_divisor = ambient_polarizing_divisor
        self._ambient_section = ambient_hypersurface_section
        self._ambient_projection = ambient_projection
        super().__init__(**rest)

    def base_pair(self):
        return self._base_pair

    def base_scheme(self):
        return self.base_pair().scheme()

    def branch_section(self):
        return self._branch_section

    def branch_subscheme(self):
        return self.base_pair().branch_subscheme(self.branch_section())

    def ambient_toric_threefold(self):
        return self._ambient

    def ambient_polarizing_divisor(self):
        return self._ambient_divisor

    def ambient_hypersurface_section(self):
        return self._ambient_section

    def scheme(self):
        return self

    def ambient_projection(self):
        return self._ambient_projection

    @cached_method
    def _cover_structure(self):
        from dzack_research.preamble.categories.sets.indexed_families import (
            finite_indexed_family,
        )

        cover = self
        ambient = self.ambient_toric_threefold()
        base_pair = self.base_pair()
        ambient_projection = self.ambient_projection()
        cover_atlas = cover.gluing_datum()
        local_cover_maps = {}
        local_global_cover_maps = {}
        local_deck = {}
        base = base_pair.scheme().scheme_base_ring()
        for cone in ambient.gluing_datum().chart_indices():
            local_cover = cover_atlas.chart(cone)
            target_cone = ambient_projection.chart_target(cone)
            to_target_chart = (
                ambient_projection.chart_morphism(cone) * local_cover.inclusion()
            )
            local_cover_maps[cone] = to_target_chart
            local_global_cover_maps[cone] = (
                base_pair.scheme().gluing_datum().chart_embedding(target_cone)
                * to_target_chart
            )

            ambient_chart = ambient.affine_chart(cone)
            algebra = ambient_chart.coordinate_algebra()
            labels = tuple(algebra.algebra_generating_set())
            images = {}
            for position, character in enumerate(cone.semigroup_generators()):
                height = int(tuple(character)[-1])
                scalar = -base.one() if height % 2 else base.one()
                images[labels[position]] = algebra.scalar_multiple(
                    scalar,
                    algebra.algebra_generator(labels[position]),
                )
            ambient_automorphism = ambient_chart.Mor(ambient_chart)(
                algebra.Mor(algebra)(images)
            )
            local_deck[cone] = local_cover.corestriction(
                ambient_automorphism * local_cover.inclusion()
            )

        cover_morphism = cover.Mor(base_pair.scheme())(local_global_cover_maps)
        deck = cover.Mor(cover)(
            {
                cone: cover.gluing_datum().chart_embedding(cone) * local_deck[cone]
                for cone in cover.gluing_datum().chart_indices()
            }
        )
        local_cover_family = finite_indexed_family(
            cover.gluing_datum().chart_index_set(),
            lambda cone: local_cover_maps[cone],
            name="Local maps of the AT21 double cover to the toric base charts",
        )
        local_deck_family = finite_indexed_family(
            cover.gluing_datum().chart_index_set(),
            lambda cone: local_deck[cone],
            name="Local deck involutions of the AT21 double cover",
        )
        if any(
            local_cover_maps[cone] * local_deck[cone] != local_cover_maps[cone]
            for cone in cover.gluing_datum().chart_indices()
        ):
            raise ArithmeticError("the pyramid deck involution does not lie over the ADE base")
        if any(
            local_deck[cone] * local_deck[cone]
            != local_deck[cone].domain().categorical_identity_morphism()
            for cone in cover.gluing_datum().chart_indices()
        ):
            raise ArithmeticError("the pyramid deck map is not an involution")

        ramification = cover.chartwise_fixed_subscheme(local_deck_family)
        base_boundary = base_pair.scheme().torus_invariant_divisor_support_subscheme(
            base_pair.boundary_divisor()
        )
        base_boundary_atlas = base_boundary.gluing_datum()
        pulled_boundary_local = {}
        for cone in cover.gluing_datum().chart_indices():
            target_cone = ambient_projection.chart_target(cone)
            local_boundary = base_boundary_atlas.chart(target_cone)
            pullback = local_cover_maps[cone].coordinate_algebra_morphism()
            equations = tuple(
                pullback(equation) for equation in local_boundary.defining_equations()
            )
            pulled_boundary_local[cone] = cover_atlas.chart(cone).closed_subscheme(equations)
        pulled_boundary = cover.chartwise_closed_subscheme(
            pulled_boundary_local,
            name="Pulled-back AT21 boundary",
        )
        return {
            "cover_morphism": cover_morphism,
            "local_cover_maps": local_cover_family,
            "local_deck": local_deck_family,
            "deck": deck,
            "ramification": ramification,
            "base_boundary": base_boundary,
            "pulled_boundary": pulled_boundary,
        }

    def cover_morphism(self):
        return self._cover_structure()["cover_morphism"]

    def local_cover_map(self, cone):
        return self._cover_structure()["local_cover_maps"][
            self.gluing_datum().normalize_chart_index(cone)
        ]

    def deck_involution(self):
        return self._cover_structure()["deck"]

    def local_deck_involution(self, cone):
        return self._cover_structure()["local_deck"][
            self.gluing_datum().normalize_chart_index(cone)
        ]

    def ramification_subscheme(self):
        return self._cover_structure()["ramification"]

    def boundary_subscheme(self):
        r"""Return ``D=pi^{-1}(C)`` scheme-theoretically."""
        return self._cover_structure()["pulled_boundary"]

    pulled_back_boundary = boundary_subscheme

    def base_boundary_subscheme(self):
        return self._cover_structure()["base_boundary"]

    def boundary_divisor(self):
        from dzack_research.preamble.categories.divisors.divisor_groups import FormalDivisorGroups

        return FormalDivisorGroups(_rationals()).from_terms(
            ((_rationals().one(), self.boundary_subscheme()),)
        )

    @cached_method
    def log_boundary_coefficient_ring(self):
        return _rationals().polynomial_ring("epsilon")

    def log_boundary_divisor(self):
        r"""Return the equipped cover boundary ``D + epsilon R`` of AT21 Section 2."""
        from dzack_research.preamble.categories.divisors.divisor_groups import FormalDivisorGroups

        coefficients = self.log_boundary_coefficient_ring()
        epsilon = coefficients.algebra_generator("epsilon")
        return FormalDivisorGroups(coefficients).from_terms(
            (
                (coefficients.one(), self.boundary_subscheme()),
                (epsilon, self.ramification_subscheme()),
            ),
        )

    def equipped_pair(self):
        r"""Return the live equipped pair ``(X, D + epsilon R)``."""
        return self, self.log_boundary_divisor()

    def dynkin_diagram(self):
        return self.base_pair().coxeter_diagram()

    def polarizing_polytope(self):
        return self.base_pair().polygon()

    def local_surface_singularity(self):
        r"""Return the source normal-form surface singularity for the E8 orbit specimen."""
        from dzack_research.preamble.categories.schemes.singularities import (
            IsolatedHypersurfaceSingularity,
        )

        assert self.base_pair().dynkin_letter() == "E" and int(self.base_pair().dynkin_rank()) == 8, (
            "the represented AT21 local/global singularity specimen is the E8 specialization"
        )
        ring = self.base_scheme().scheme_base_ring().polynomial_ring(("x", "y", "z"))
        x, y, z = tuple(ring.algebra_generators())
        return IsolatedHypersurfaceSingularity(
            ring,
            z**2 - x * y * z + y**3 + x**5,
        )

    def local_global_singularity_comparison(self):
        singularity = self.local_surface_singularity()
        rank = self.base_pair().dynkin_rank()
        return finite_family(
            (
                ("global_dynkin_rank", rank),
                ("local_milnor_number", singularity.milnor_number()),
                ("local_tjurina_number", singularity.tjurina_number()),
            ),
            name="AT21 E8 local/global singularity comparison",
        )

    def _repr_(self):
        return f"AT21 double cover of {self.base_pair()}"


def _at21_ade_double_cover(base_pair, branch_section):
    r"""Construct the AT21 hypersurface through the toric zero-subscheme owner."""
    selected_branch = base_pair.branch_section_space()(branch_section)
    ambient = base_pair.cover_toric_threefold()
    ambient_divisor = ambient.polarizing_divisor()
    ambient_sections = ambient.divisor_section_space(ambient_divisor)
    ambient_by_coordinates = {
        tuple(int(coordinate) for coordinate in character): character
        for character in ambient_sections.module_generating_set()
    }
    coefficients = {}
    branch_coefficients = base_pair.branch_section_space().framing_coefficients(selected_branch)
    for character, coefficient in branch_coefficients.items():
        key = (*tuple(int(value) for value in character), 0)
        if key not in ambient_by_coordinates:
            raise ArithmeticError("a branch character is absent from the pyramid hyperplane section")
        coefficients[ambient_by_coordinates[key]] = coefficient
    apex = (
        *tuple(int(value) for value in base_pair.distinguished_point()),
        2,
    )
    if apex not in ambient_by_coordinates:
        raise ArithmeticError("the pyramid apex is absent from its polarizing section space")
    coefficients[ambient_by_coordinates[apex]] = base_pair.scheme().scheme_base_ring().one()
    ambient_section = ambient_sections.linear_combination(coefficients)

    source_lattice = ambient.cocharacter_lattice()
    target_lattice = base_pair.scheme().cocharacter_lattice()
    source_labels = tuple(source_lattice.module_generating_set())
    target_labels = tuple(target_lattice.module_generating_set())
    if len(source_labels) != 3 or len(target_labels) != 2:
        raise ArithmeticError("the ADE pyramid projection expects ranks three and two")
    projection_lattice_map = source_lattice.module_category().Mor(source_lattice, target_lattice)(
        {
            source_labels[0]: target_lattice.module_generator(target_labels[0]),
            source_labels[1]: target_lattice.module_generator(target_labels[1]),
            source_labels[2]: target_lattice.zero(),
        }
    )
    ambient_projection = ambient.toric_morphism(
        projection_lattice_map,
        base_pair.scheme(),
    )
    return ambient.zero_subscheme_of_divisor_section(
        ambient_divisor,
        ambient_section,
        _engine=_AT21ADEDoubleCoverEngine,
        construction_data={
            "base_pair": base_pair,
            "branch_section": selected_branch,
            "ambient_toric_threefold": ambient,
            "ambient_polarizing_divisor": ambient_divisor,
            "ambient_hypersurface_section": ambient_section,
            "ambient_projection": ambient_projection,
        },
    )


__all__ = [
    "ADELogPairs",
    "SideDecoration",
]
