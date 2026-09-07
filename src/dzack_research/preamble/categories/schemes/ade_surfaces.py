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
            distinguished_point,
            side_decorations,
            **rest,
        ) -> None:
            self._preamble_dynkin_letter = dynkin_letter
            self._preamble_dynkin_rank = dynkin_rank
            self._preamble_dynkin_variant = dynkin_variant
            self._preamble_is_affine_type = is_affine_type
            self._preamble_polygon = polygon
            self._preamble_distinguished_point = distinguished_point
            self._preamble_side_decorations = side_decorations
            super().__init__(**rest)

        def dynkin_letter(self) -> str:
            return self._preamble_dynkin_letter

        def dynkin_rank(self):
            return _own_ring(SageZZ)(self._preamble_dynkin_rank)

        def dynkin_variant(self):
            r"""The decorations naming this member of its family."""
            return finite_family(
                self._preamble_dynkin_variant,
                name="Dynkin variant",
            )

        def is_affine_type(self) -> bool:
            return self._preamble_is_affine_type

        @cached_method
        def coxeter_diagram(self):
            r"""The Coxeter diagram of the type, from the live diagram layer.

            The affine families have no finite Coxeter diagram of the same
            name, so the diagram is available exactly for the finite types.
            """
            from dzack_research.preamble.categories.coxeter_diagrams import (
                CoxeterDiagrams,
            )

            assert not self.is_affine_type(), (
                "the affine ADE types are named by an affine Cartan type, which "
                "the finite Coxeter-diagram layer does not build"
            )
            return CoxeterDiagrams().from_cartan_type(
                [self.dynkin_letter(), int(self.dynkin_rank())]
            )

        def polygon(self):
            r"""The integral ADE polygon ``Q``."""
            return self._preamble_polygon

        def distinguished_point(self):
            r"""The distinguished rational point ``p*`` on the boundary of ``Q``."""
            return self._preamble_distinguished_point

        def side_decorations(self):
            r"""The decorations of the sides of ``Q`` incident to ``p*``."""
            return self._preamble_side_decorations

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

        def blue_divisor(self):
            r"""``C``: the invariant divisors whose facet of ``Q`` contains ``p*``."""
            group = self.log_scheme().torus_invariant_divisor_group()
            blue = self._blue_rays()
            return group.linear_combination(
                {ray: _own_ring(SageZZ).one() for ray in blue}
            )

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
        distinguished_point=_rational_point(point),
        side_decorations=decorations,
        log_scheme=toric_base,
        boundary_divisor=toric_base.toric_boundary_divisor(),
    )


__all__ = ["ADELogPair", "ADELogPairs", "SideDecoration"]
