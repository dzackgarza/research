r"""Category hierarchy and model for ADE surfaces as del Pezzo and anticanonical log pairs.

Hierarchy:
  Objects()
    └── LogPairs()
          └── ADELogPairs()

Mathematical Foundations (Alexeev-Thompson [AT21], arXiv:1712.07932):
---------------------------------------------------------------------
1. Integral Polygon Q \subset N and distinguished point p* \in N:
   - For pure shapes (Table 1), p* is (0, 2) for A-types, and (2, 2) for D/E/affine types.
   - All opposite sides of Q are at lattice distance d_i = 2 from p* (Lemma 2.1).

2. Del Pezzo ADE Surface Pair (Y, C + (1+eps)/2 * B):
   - Y = V_Q is the polarized toric variety (Y, L) defined by normal_fan(Q).
   - Boundary Divisor C (the "blue line"):
     The torus-invariant 1-cycle supported strictly on the sides of Q passing through p*.
   - Complementary Divisor C':
     Supported on sides not passing through p*. Satisfies L ~ 2*C'.
   - Adjunction:
     K_Y + C + C' ~ 0  ==>  -2(K_Y + C) ~ L is ample and Cartier.
     (Y, C) is a log del Pezzo surface with log canonical singularities.
   - Branch Divisor B = div(f):
     Defined by section f(x, y) with Newton polygon Q (Eq. 3.4-3.6 in [AT21]).

3. Anticanonical ADE Surface Pair (X, D + eps * R):
   - 3D Pyramidal Polytope P = cone(Q) + (p*, 2) in N_3.
   - Ambient Toric Threefold V_P.
   - Anticanonical ADE Surface X = Z(w^2 + f(x, y)) \subset V_P.
     The branched double cover pi: X -> Y branched along B.
   - Boundary Divisor D = pi^*(C) on X.
   - Del Pezzo Involution iota_dP: w |-> -w with quotient X / iota_dP = Y.

EXAMPLES::

    sage: from dzack_research.preamble.categories.schemes.ade_surfaces import ADESurface, LogPairs, ADELogPairs
    sage: S = ADESurface('A', 3, variant=('long', 'long'))
    sage: S.category()
    Category of a d e log pairs (Y, C + ½(1+ε)B)
    sage: S in LogPairs()
    True
    sage: S.del_pezzo_surface()
    2-d toric variety covered by 3 affine patches
    sage: S.blue_line_divisor()
    V(z0) + V(z2)
    sage: S.defining_polynomial()
    -1/4*x^2*y^2 + x^2 + y
"""

from typing import NamedTuple, Optional, Callable, Sequence, Protocol, TYPE_CHECKING
from sage.categories.category import Category
from sage.categories.objects import Objects
from sage.structure.parent import Parent
from sage.geometry.toric_lattice import ToricLattice, ToricLattice_generic
from sage.geometry.polyhedron.constructor import Polyhedron
from sage.geometry.polyhedron.base import Polyhedron_base
from sage.schemes.toric.variety import ToricVariety, ToricVariety_field
from sage.combinat.root_system.cartan_type import CartanType
from sage.rings.rational_field import QQ, RationalField
from sage.rings.integer_ring import ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.plot.graphics import Graphics
from sage.plot.line import line
from sage.plot.polygon import polygon
from sage.plot.point import point
from sage.plot.text import text

from sage.rings.rational import Rational
from sage.rings.integer import Integer
from dzack_research.preamble.categories.schemes.polytopes import (
    LatticePolygon, LatticePolytope, LatticePolygons, LatticePolytopes,
    ConvexPolygon, ConvexPolytope, ConvexPolygons, ConvexPolytopes
)

# Valid side decorations for distinguished edges incident to p*
VALID_DECORATIONS = frozenset({
    'long', 'short', 'l', 's', 'standard', 'decorated', 'plain',
    'primed', 'prime', 'p',
})

# Domain semantic types for exact lattice geometry
LatticeCoord = int | Integer | Rational
LatticePoint2D = Sequence[LatticeCoord]


class _PolyhedronFace(Protocol):
    def as_polyhedron(self) -> Polyhedron_base: ...
    def vertices(self) -> Sequence[LatticePoint2D]: ...
    def integral_points(self) -> Sequence[LatticePoint2D]: ...
    def ambient_Hrepresentation(self) -> Sequence[_HRepresentation]: ...


class _HRepresentation(Protocol):
    def A(self) -> Sequence[Integer]: ...
    def eval(self, pt: object) -> LatticeCoord: ...


class _Polyhedron(Protocol):
    def facets(self) -> Sequence[_PolyhedronFace]: ...
    def vertices(self) -> Sequence[LatticePoint2D]: ...
    def integral_points(self) -> Sequence[LatticePoint2D]: ...
    def volume(self) -> LatticeCoord: ...
    def normal_fan(self) -> object: ...


class SideDecoration(NamedTuple):
    """
    Metadata for a distinguished side of an ADE polygon Q adjacent to p*.

    Attributes:
        edge: Tuple of vertex indices (i, j)
        decoration_type: 'long' or 'short'
        vertex_color: 'white' (hollow) or 'black' (solid)
    """
    edge: tuple[int, int]
    decoration_type: str
    vertex_color: str


class _ADESurfaceInterface(Protocol):
    _letter: str
    _rank: int
    _variant: tuple[str, ...]
    _affine: bool
    _key: str
    _latex_label: str
    _lattice: ToricLattice_generic
    _ambient_space: Callable[[Sequence[LatticeCoord]], LatticePoint2D]
    _vertices: tuple[LatticePoint2D, ...]
    _p_star: LatticePoint2D
    _sides_info: dict[tuple[int, int], SideDecoration]
    _del_pezzo_variety: ToricVariety_field

    def variety(self) -> ToricVariety_field: ...
    def del_pezzo_surface(self) -> ToricVariety_field: ...
    def blue_line_divisor(self) -> object: ...
    def defining_polynomial(self) -> object: ...
    def letter(self) -> str: ...
    def rank(self) -> int: ...
    def is_affine(self) -> bool: ...
    def cartan_type(self) -> CartanType: ...
    def dynkin_diagram(self) -> object: ...
    def vertices(self) -> tuple[LatticePoint2D, ...]: ...
    def p_star(self) -> LatticePoint2D: ...
    def p_star_index(self) -> Optional[int]: ...
    def side_decorations(self) -> dict[tuple[int, int], SideDecoration]: ...
    def latex_label(self) -> str: ...
    def ambient_space(self) -> Callable[[Sequence[LatticeCoord]], LatticePoint2D]: ...
    def polyhedron(self) -> _Polyhedron: ...
    def dynkin_diagram_data(self) -> dict[str, object]: ...
    def pyramid_polytope(self) -> Polyhedron_base: ...
    def area(self) -> LatticeCoord: ...
    def volume(self) -> LatticeCoord: ...
    def plot(self, **kwds: object) -> Graphics: ...


class LogPairs(Category):
    """
    The category of algebraic log pairs (X, Δ).

    A log pair consists of:
    - An underlying scheme or variety X (accessed via .scheme() or .variety())
    - An associated boundary divisor Δ (accessed via .associated_divisor() or .boundary_divisor())
    - An ambient scheme or projective toric variety V (accessed via .ambient_variety())
    - An ambient toric log pair (V, Δ_toric) (accessed via .ambient_pair())

    EXAMPLES::

        sage: from dzack_research.preamble.categories.schemes.ade_surfaces import LogPairs, ToricLogPair
        sage: LogPairs()
        Category of log pairs
        sage: LogPairs().super_categories()
        [Category of objects]
    """
    def super_categories(self) -> list[Category]:
        return [Objects()]

    def _repr_object_names(self) -> str:
        return "log pairs"

    def _latex_(self) -> str:
        return r"\mathbf{Cat}\left(\text{Log Pairs}\right)"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"

    class ParentMethods:
        """
        Generic geometric and algebraic methods for log pairs (X, Δ).
        """
        def scheme(self: _ADESurfaceInterface) -> object:
            """
            Return the underlying scheme or variety X of the log pair (X, Δ).
            """
            return self.variety()

        def variety(self: _ADESurfaceInterface) -> object:
            """
            Return the underlying scheme or variety X of the log pair (X, Δ).
            """
            return self.del_pezzo_surface()

        def associated_divisor(self: _ADESurfaceInterface) -> object:
            """
            Return the underlying associated boundary divisor Δ of the log pair (X, Δ).
            """
            return self.boundary_divisor()

        def boundary_divisor(self: _ADESurfaceInterface) -> object:
            """
            Return the distinguished boundary divisor C (the 'blue line') on Y.
            """
            return self.blue_line_divisor()

        def divisor(self: _ADESurfaceInterface) -> object:
            """
            Alias for associated_divisor().
            """
            return self.associated_divisor()

        def ambient_space(self: _ADESurfaceInterface) -> object:
            """
            Return the ambient scheme or projective toric variety V.
            """
            return self.del_pezzo_surface()

        def ambient_variety(self: _ADESurfaceInterface) -> object:
            """
            Alias for ambient_space().
            """
            return self.ambient_space()

        def ambient_pair(self: _ADESurfaceInterface) -> "ToricLogPair":
            """
            Return the ambient projective toric variety as a toric log pair (V, Δ_toric)
            where Δ_toric is the full toric boundary divisor.
            """
            return ToricLogPair(self.ambient_variety())

        def ambient_log_pair(self: _ADESurfaceInterface) -> "ToricLogPair":
            """
            Alias for ambient_pair().
            """
            return self.ambient_pair()

        def codimension(self: _ADESurfaceInterface) -> int:
            """
            Return the codimension of the underlying scheme in its ambient variety.
            """
            return 0

        def del_pezzo_surface(self: _ADESurfaceInterface) -> ToricVariety_field:
            """
            Return the polarized toric del Pezzo surface Y = V_Q.
            """
            return self._del_pezzo_variety

        def blue_line_divisor(self: _ADESurfaceInterface) -> object:
            """
            Return the distinguished boundary divisor C (the 'blue line') on Y = V_Q.
            """
            y_variety = self.del_pezzo_surface()
            poly_q = self.polyhedron()
            p_star = self._lattice.vector_space(QQ)(list(self.p_star()))

            blue_ray_indices: list[int] = []
            for idx, f in enumerate(poly_q.facets()):
                if f.as_polyhedron().contains(p_star):
                    blue_ray_indices.append(idx)

            if not blue_ray_indices:
                return y_variety.divisor_group().zero()
            return sum((y_variety.divisor(idx) for idx in blue_ray_indices), y_variety.divisor_group().zero())

        def _blue_facets(self: _ADESurfaceInterface) -> list[_PolyhedronFace]:
            """Return the list of facets of Q passing through p*."""
            poly_q = self.polyhedron()
            p_star = self._lattice.vector_space(QQ)(list(self.p_star()))
            return [f for f in poly_q.facets() if f.as_polyhedron().contains(p_star)]

        def is_on_blue_boundary(self: _ADESurfaceInterface, pt: Sequence[LatticeCoord]) -> bool:
            """Return True if pt lies on the distinguished boundary divisor C."""
            pt_vec = self._lattice.vector_space(QQ)(list(pt))
            return any(f.as_polyhedron().contains(pt_vec) for f in self._blue_facets())

        def polygon(self: _ADESurfaceInterface) -> LatticePolygon:
            """
            Return the base 2-dimensional integral lattice polygon Q in category LatticePolygons().
            """
            return LatticePolygon(vertices=self.vertices(), lattice=self._lattice)

        def base_polygon(self: _ADESurfaceInterface) -> LatticePolygon:
            """
            Alias for polygon(): return the base 2-dimensional integral lattice polygon Q.
            """
            return self.polygon()

        def cover_polytope(self: _ADESurfaceInterface) -> LatticePolytope:
            r"""
            Return the 3-dimensional integral lattice polytope P \subset N \oplus \ZZ
            formed as the pyramid over Q \times {0} with apex (p^*_x, p^*_y, 2),
            corresponding to the monomial z^2 in the covering equation z^2 + f(x, y) = 0.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.schemes.ade_surfaces import ADESurface
                sage: s = ADESurface('A', 3, variant=('long', 'long'))
                sage: P = s.cover_polytope()
                sage: P.dimension()
                3
                sage: P.category()
                Category of lattice polytopes
                sage: P.volume()
                8/3
                sage: P.normalized_volume()
                16
            """
            p_star = self.p_star()
            verts_3d = [(v[0], v[1], 0) for v in self.vertices()] + [(p_star[0], p_star[1], 2)]
            return LatticePolytope(verts_3d)

        def newton_polytope(self: _ADESurfaceInterface) -> LatticePolytope:
            r"""
            Alias for cover_polytope(): the 3-dimensional Newton polytope of z^2 + f(x, y).
            """
            return self.cover_polytope()

        def integral_points(self: _ADESurfaceInterface) -> tuple[LatticePoint2D, ...]:
            """Return all integral lattice points in Q."""
            return self.polygon().integral_points()

        def interior_integral_points(self: _ADESurfaceInterface) -> tuple[LatticePoint2D, ...]:
            """Return all strictly interior integral lattice points of Q."""
            return self.polygon().interior_integral_points()

        def boundary_integral_points(self: _ADESurfaceInterface) -> tuple[LatticePoint2D, ...]:
            """Return all boundary integral lattice points of Q."""
            return self.polygon().boundary_integral_points()

        def distinguished_boundary_points(self: _ADESurfaceInterface) -> tuple[LatticePoint2D, ...]:
            """Return all integral lattice points lying on the distinguished divisor C."""
            return tuple(p for p in self.boundary_integral_points() if self.is_on_blue_boundary(p))

        def n_integral_points(self: _ADESurfaceInterface) -> int:
            """Total number of integral lattice points in Q."""
            return self.polygon().n_integral_points()

        def n_interior_points(self: _ADESurfaceInterface) -> int:
            """Number of interior integral lattice points in Q."""
            return self.polygon().n_interior_points()

        def n_boundary_points(self: _ADESurfaceInterface) -> int:
            """Number of boundary integral lattice points in Q."""
            return self.polygon().n_boundary_points()

        def invariants(self: _ADESurfaceInterface) -> dict[str, object]:
            """
            Return a dictionary of fundamental geometric invariants for this ADE surface.
            """
            poly_inv = self.polygon().invariants()
            cover_inv = self.cover_polytope().invariants()
            return {
                "key": self.key(),
                "latex_label": self.latex_label(),
                "dynkin_type": self.dynkin_type(),
                "rank": self.rank(),
                "p_star": self.p_star(),
                "area": self.area(),
                "normalized_volume": self.normalized_volume(),
                "n_integral_points": self.n_integral_points(),
                "n_boundary_points": self.n_boundary_points(),
                "n_interior_points": self.n_interior_points(),
                "n_distinguished_points": len(self.distinguished_boundary_points()),
                "cover_volume": cover_inv["volume"],
                "cover_normalized_volume": cover_inv["normalized_volume"],
                "cover_integral_points": cover_inv["n_integral_points"],
            }

        def n_distinguished_points(self: _ADESurfaceInterface) -> int:
            """Number of integral lattice points on the distinguished divisor C."""
            return len(self.distinguished_boundary_points())

        def area(self: _ADESurfaceInterface) -> Rational:
            """Return Euclidean area of Q."""
            return self.polygon().area()

        def normalized_volume(self: _ADESurfaceInterface) -> Integer:
            """Return normalized lattice volume 2 * Area(Q)."""
            return self.polygon().normalized_volume()

        def invariants(self: _ADESurfaceInterface) -> dict[str, object]:
            """Return geometric and combinatorial invariants of the ADE surface pair."""
            p_star_vec = self._lattice.vector_space(QQ)(list(self.p_star()))
            poly = self.polyhedron()
            return {
                "letter": self.letter(),
                "rank": self.rank(),
                "affine": self.is_affine(),
                "p_star": tuple(self.p_star()),
                "p_star_in_polytope": poly.contains(p_star_vec),
                "p_star_in_interior": poly.interior_contains(p_star_vec),
                "area": self.area(),
                "normalized_volume": self.normalized_volume(),
                "n_integral_points": self.n_integral_points(),
                "n_boundary_points": self.n_boundary_points(),
                "n_interior_points": self.n_interior_points(),
                "n_distinguished_points": self.n_distinguished_points(),
            }

        def defining_polynomial(self: _ADESurfaceInterface) -> object:
            """
            Return the canonical unperturbed branch polynomial f_0(x, y) = f(x, y; c=0)
            from Alexeev-Thompson [AT21], Section 3, Equations (3.4)--(3.6).
            """
            letter = self.letter()
            rank = self.rank()
            affine = self.is_affine()

            if letter == 'A':
                ring_a = PolynomialRing(QQ, names=['x', 'y'])
                x, y = ring_a.gens()
                if affine:
                    return -QQ(1)/QQ(4) * (x * y)**2 + x**(rank + 1) + y**2
                return -QQ(1)/QQ(4) * (x * y)**2 + y + x**(rank - 1)
            elif letter == 'D':
                ring_d = PolynomialRing(QQ, names=['x', 'y'])
                x, y = ring_d.gens()
                if affine:
                    return -QQ(1)/QQ(4) * (x * y)**2 + x**4 + y**(rank - 2)
                return -QQ(1)/QQ(4) * (x * y)**2 + y**2 + x**(rank - 2)
            elif letter == 'E':
                ring_e = PolynomialRing(QQ, names=['x', 'y'])
                x, y = ring_e.gens()
                if affine:
                    if rank == 6:
                        return -QQ(1)/QQ(4) * (x * y)**2 + x**3 + y**3
                    elif rank == 7:
                        return -QQ(1)/QQ(4) * (x * y)**2 + x**4 + y**3
                    elif rank == 8:
                        return -QQ(1)/QQ(4) * (x * y)**2 + x**6 + y**3
                return -QQ(1)/QQ(4) * (x * y)**2 + y**3 + x**(rank - 3)
            else:
                ring_gen = PolynomialRing(QQ, names=['x', 'y'])
                x, y = ring_gen.gens()
                return -QQ(1)/QQ(4) * (x * y)**2 + y**2 + x**2

        def anticanonical_equation(self: _ADESurfaceInterface) -> object:
            """
            Return the global anticanonical double cover defining equation z^2 + f_0(x, y) = 0
            in the anticanonical toric threefold V_P.
            """
            f_0 = self.defining_polynomial()
            ring_3d = PolynomialRing(QQ, names=['x', 'y', 'z'])
            x, y, z = ring_3d.gens()
            f_in_3d = f_0(x, y) # pyright: ignore[reportCallIssue]
            return z**2 + f_in_3d

        def is_toric(self: _ADESurfaceInterface) -> bool:
            return False

        def is_toric_base(self: _ADESurfaceInterface) -> bool:
            return True


class ToricLogPair(Parent):
    r"""
    A toric log pair (V, Δ_toric) consisting of a normal toric variety V
    and a torus-invariant boundary divisor (by default, the full toric boundary Δ_toric = ∑ D_ρ).

    EXAMPLES::

        sage: from dzack_research.preamble.categories.schemes.ade_surfaces import ToricLogPair, LogPairs
        sage: from sage.schemes.toric.variety import ToricVariety
        sage: V = ToricVariety(Polyhedron([(0,2), (0,0), (2,0)]).normal_fan())
        sage: P = ToricLogPair(V)
        sage: P in LogPairs()
        True
        sage: P.scheme()
        2-d toric variety covered by 3 affine patches
        sage: P.associated_divisor()
        V(z0) + V(z1) + V(z2)
        sage: P.codimension()
        0
    """
    _variety: ToricVariety_field
    _divisor: object

    def __init__(self, variety: ToricVariety_field, divisor: Optional[object] = None) -> None:
        self._variety = variety
        if divisor is None:
            nrays = variety.fan().nrays()
            self._divisor = sum((variety.divisor(i) for i in range(nrays)), variety.divisor_group().zero())
        else:
            self._divisor = divisor
        super().__init__(base=variety.base_ring(), category=LogPairs())

    def scheme(self) -> ToricVariety_field:
        """Return the underlying toric variety V."""
        return self._variety

    def variety(self) -> ToricVariety_field:
        """Return the underlying toric variety V."""
        return self._variety

    def associated_divisor(self) -> object:
        """Return the toric boundary divisor Δ_toric."""
        return self._divisor

    def boundary_divisor(self) -> object:
        """Return the toric boundary divisor Δ_toric."""
        return self._divisor

    def divisor(self) -> object:
        """Return the toric boundary divisor Δ_toric."""
        return self._divisor

    def ambient_space(self) -> ToricVariety_field:
        """Return the ambient toric variety V."""
        return self._variety

    def ambient_variety(self) -> ToricVariety_field:
        """Return the ambient toric variety V."""
        return self._variety

    def ambient_pair(self) -> "ToricLogPair":
        """Return self (already a toric log pair)."""
        return self

    def ambient_log_pair(self) -> "ToricLogPair":
        """Return self."""
        return self

    def codimension(self) -> int:
        """Return 0 (variety is its own ambient space)."""
        return 0

    def _repr_(self) -> str:
        return f"Toric Log Pair ({self._variety}, toric boundary)"

    def _latex_(self) -> str:
        from sage.misc.latex import latex as _latex
        return rf"\left({_latex(self._variety)},\, \Delta_{{\text{{toric}}}}\right)"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"


class ADELogPairs(LogPairs):
    """
    The category of ADE del Pezzo log pairs (Y, C + ½(1+ε)B).

    EXAMPLES::

        sage: from dzack_research.preamble.categories.schemes.ade_surfaces import ADELogPairs, LogPairs
        sage: ADELogPairs()
        Category of a d e log pairs (Y, C + ½(1+ε)B)
        sage: ADELogPairs().super_categories()
        [Category of log pairs]
    """
    def super_categories(self) -> list[Category]:
        return [LogPairs()]

    def _repr_object_names(self) -> str:
        return "a d e log pairs (Y, C + ½(1+ε)B)"

    def _latex_(self) -> str:
        return r"\mathbf{Cat}\left(\text{ADE Log Pairs } \left(Y, C + \frac{1+\varepsilon}{2}B\right)\right)"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"

    class ParentMethods:
        """
        Domain methods for ADE log pairs following Alexeev-Thompson [AT21].
        """
        def letter(self: _ADESurfaceInterface) -> str:
            return self._letter

        def rank(self: _ADESurfaceInterface) -> int:
            return self._rank

        def variant(self: _ADESurfaceInterface) -> tuple[str, ...]:
            return self._variant

        def is_affine(self: _ADESurfaceInterface) -> bool:
            return self._affine

        def key(self: _ADESurfaceInterface) -> str:
            return self._key

        def latex_label(self: _ADESurfaceInterface) -> str:
            return self._latex_label

        def cartan_type(self: _ADESurfaceInterface) -> CartanType:
            if self._affine:
                return CartanType([self._letter, self._rank, 1])
            return CartanType([self._letter, self._rank])

        def dynkin_diagram(self: _ADESurfaceInterface) -> object:
            return self.cartan_type().dynkin_diagram()

        def vertices(self: _ADESurfaceInterface) -> tuple[LatticePoint2D, ...]:
            return self._vertices

        def p_star(self: _ADESurfaceInterface) -> LatticePoint2D:
            return self._p_star

        def side_decorations(self: _ADESurfaceInterface) -> dict[tuple[int, int], SideDecoration]:
            return dict(self._sides_info)

        def ambient_space(self: _ADESurfaceInterface) -> Callable[[Sequence[LatticeCoord]], LatticePoint2D]:
            return self._ambient_space

        def normal_fan(self: _ADESurfaceInterface) -> object:
            return self.polyhedron().normal_fan()

        def polyhedron(self: _ADESurfaceInterface) -> _Polyhedron:
            verts = [list(v) for v in self.vertices()]
            return Polyhedron(vertices=verts, base_ring=ZZ)

        def parametric_branch_polynomial(self: _ADESurfaceInterface) -> object:
            """
            Return the universal parametric polynomial f(x, y; c) from [AT21] Eq (3.4)--(3.6).
            """
            letter = self.letter()
            rank = self.rank()

            if letter == 'A':
                c_names = [f'c{i}' for i in range(1, rank)] + ['c_pp']
                c_latex = [f'c_{{{i}}}' for i in range(1, rank)] + [r"c''"]
                ring_a = PolynomialRing(QQ, names=['x', 'y'] + c_names)
                ring_a._latex_names = ['x', 'y'] + c_latex
                gens = ring_a.gens()
                x, y = gens[0], gens[1]
                coeffs = gens[2:-1]
                c_pp = gens[-1]
                px = x**(rank - 1) + sum(coeffs[i] * x**(rank - 2 - i) for i in range(rank - 1))
                return -QQ(1)/QQ(4) * (x * y - c_pp)**2 + px + y
            elif letter == 'D':
                deg_p = rank - 2
                deg_q = 2
                c_p_names = [f'c{i}' for i in range(1, deg_p + 1)]
                c_p_latex = [f'c_{{{i}}}' for i in range(1, deg_p + 1)]
                c_q_names = [f'cp{j}' for j in range(1, deg_q)]
                c_q_latex = [f"c'_{{{j}}}" for j in range(1, deg_q)]
                all_c_names = c_p_names + c_q_names + ['c_pp']
                all_c_latex = c_p_latex + c_q_latex + [r"c''"]
                ring_d = PolynomialRing(QQ, names=['x', 'y'] + all_c_names)
                ring_d._latex_names = ['x', 'y'] + all_c_latex
                gens = ring_d.gens()
                x, y = gens[0], gens[1]
                px = x**deg_p + sum(gens[2 + i] * x**(deg_p - 1 - i) for i in range(deg_p))
                qy = y**deg_q + gens[2 + deg_p] * y
                c_pp = gens[-1]
                return -QQ(1)/QQ(4) * (x * y - c_pp)**2 + px + qy
            elif letter == 'E':
                deg_p = rank - 3
                deg_q = 3
                c_p_names = [f'c{i}' for i in range(1, deg_p + 1)]
                c_p_latex = [f'c_{{{i}}}' for i in range(1, deg_p + 1)]
                c_q_names = [f'cp{j}' for j in range(1, deg_q)]
                c_q_latex = [f"c'_{{{j}}}" for j in range(1, deg_q)]
                all_c_names = c_p_names + c_q_names + ['c_pp']
                all_c_latex = c_p_latex + c_q_latex + [r"c''"]
                ring_e = PolynomialRing(QQ, names=['x', 'y'] + all_c_names)
                ring_e._latex_names = ['x', 'y'] + all_c_latex
                gens = ring_e.gens()
                x, y = gens[0], gens[1]
                px = x**deg_p + sum(gens[2 + i] * x**(deg_p - 1 - i) for i in range(deg_p))
                qy = y**deg_q + sum(gens[2 + deg_p + j - 1] * y**(deg_q - j) for j in range(1, deg_q))
                c_pp = gens[-1]
                return -QQ(1)/QQ(4) * (x * y - c_pp)**2 + px + qy
            else:
                ring_gen = PolynomialRing(QQ, names=['x', 'y'])
                x, y = ring_gen.gens()
                return -QQ(1)/QQ(4) * (x * y)**2 + y**2 + x**2

        def dynkin_diagram_data(self: _ADESurfaceInterface) -> dict[str, object]:
            """
            Extract internal Dynkin tree root nodes from the polygon Q.
            """
            poly_q = self.polyhedron()
            v_space = self._lattice.vector_space(QQ)
            p_star = v_space(list(self.p_star()))

            blue_facets: list[_PolyhedronFace] = []
            non_blue_facets: list[_PolyhedronFace] = []
            for f in poly_q.facets():
                facet_pts = [v_space(list(v)) for v in f.vertices()]
                if p_star in facet_pts:
                    blue_facets.append(f)
                else:
                    non_blue_facets.append(f)

            c_points: set[tuple[LatticeCoord, ...]] = set()
            for f_blue in blue_facets:
                for pt in f_blue.as_polyhedron().integral_points():
                    c_points.add(tuple(pt))

            corners = [v_space(list(v)) for v in poly_q.vertices()]

            boundary_nodes: list[LatticePoint2D] = []
            corner_nodes: list[LatticePoint2D] = []
            boundary_edges: list[tuple[LatticePoint2D, LatticePoint2D]] = []

            for f_non_blue in non_blue_facets:
                f_poly = f_non_blue.as_polyhedron()
                pts = list(f_poly.integral_points())
                if len(pts) > 1:
                    pts.sort(key=lambda p: (p[0], p[1]))
                    for i in range(len(pts) - 1):
                        p1, p2 = pts[i], pts[i+1]
                        if tuple(p1) not in c_points and tuple(p2) not in c_points:
                            boundary_edges.append((p1, p2))
                for pt in pts:
                    if tuple(pt) not in c_points and pt not in boundary_nodes:
                        boundary_nodes.append(pt)
                        if pt in corners:
                            corner_nodes.append(pt)

            internal_nodes: list[tuple[int, int]] = []
            internal_edges: list[tuple[LatticePoint2D, tuple[int, int]]] = []
            for c in corner_nodes:
                int_pt = (int(c[0]) + 1, int(c[1]) + 1)
                internal_nodes.append(int_pt)
                internal_edges.append((c, int_pt))

            all_nodes: Sequence[object] = list(boundary_nodes) + list(internal_nodes)
            all_edges: Sequence[object] = list(boundary_edges) + list(internal_edges)

            node_types: dict[object, str] = {}
            for n_int in internal_nodes:
                node_types[n_int] = 'circled_white'

            for n_bnd in boundary_nodes:
                d = abs(n_bnd[0] - p_star[0]) + abs(n_bnd[1] - p_star[1])
                if n_bnd in corner_nodes:
                    node_types[n_bnd] = 'black'
                else:
                    node_types[n_bnd] = 'black' if d % 2 == 0 else 'white'

            return {
                'nodes': all_nodes,
                'edges': all_edges,
                'node_types': node_types,
            }

        def pyramid_polytope(self: _ADESurfaceInterface) -> Polyhedron_base:
            """
            Return the 3D anticanonical pyramidal polytope P in N_3.
            """
            if self.is_affine():
                raise ValueError("Anticanonical pyramidal 3D cone is only defined for Type III classical ADE surfaces with p* on boundary")

            q_verts = [list(v) for v in self.vertices()]
            p_star = list(self.p_star())
            p_apex = [p_star[0], p_star[1], 2]
            p_base_verts = [[v[0], v[1], 0] for v in q_verts]
            all_3d_verts = p_base_verts + [p_apex]
            return Polyhedron(vertices=all_3d_verts, base_ring=ZZ)

        def area(self: _ADESurfaceInterface) -> LatticeCoord:
            return self.polyhedron().volume()

        def volume(self: _ADESurfaceInterface) -> LatticeCoord:
            return self.area()

        def p_star_index(self: _ADESurfaceInterface) -> Optional[int]:
            p = tuple(self.p_star())
            for i, v in enumerate(self.vertices()):
                if tuple(v) == p:
                    return i
            return None

        def plot2d(self: _ADESurfaceInterface, **kwds: object) -> Graphics:
            """
            Return a publication-quality Sage Graphics object adhering to
            Alexeev-Thompson visual conventions for the 2D polygon Q.
            """
            grid_line_color = kwds.get('grid_line_color', '#CBD5E1')
            grid_line_width = kwds.get('grid_line_width', 0.75)
            fill_color = kwds.get('fill_color', '#E0F2FE')
            fill_alpha = kwds.get('fill_alpha', 0.75)
            boundary_color = kwds.get('boundary_color', '#1E293B')
            boundary_width = kwds.get('boundary_width', 2.0)
            blue_line_color = kwds.get('blue_line_color', '#2563EB')
            blue_line_width = kwds.get('blue_line_width', 4.2)
            p_star_size = kwds.get('p_star_size', 220)
            p_star_color = kwds.get('p_star_color', '#DC2626')
            label_fontsize = kwds.get('label_fontsize', 14)
            label_y_offset = kwds.get('label_y_offset', -0.1)
            side_label_fontsize = kwds.get('side_label_fontsize', 10)

            vertices = [tuple(v) for v in self.vertices()]
            p_star = tuple(self.p_star())
            sides = self.side_decorations()
            label = self.latex_label()
            poly = self.polyhedron()

            all_pts = list(vertices) + [p_star]
            min_x = int(min(p[0] for p in all_pts) - 1)
            max_x = int(max(p[0] for p in all_pts) + 1)
            min_y = int(min(p[1] for p in all_pts) - 1)
            max_y = int(max(p[1] for p in all_pts) + 1)

            g_plot = Graphics()

            # Render integer lattice grid lines
            for gx in range(min_x, max_x + 1):
                g_plot += line([(gx, min_y), (gx, max_y)],
                               color=grid_line_color, thickness=grid_line_width,
                               linestyle=':', zorder=1)
            for gy in range(min_y, max_y + 1):
                g_plot += line([(min_x, gy), (max_x, gy)],
                               color=grid_line_color, thickness=grid_line_width,
                               linestyle=':', zorder=1)

            # Classify all lattice points in the bounding box
            all_grid = [(gx, gy) for gx in range(min_x, max_x + 1)
                        for gy in range(min_y, max_y + 1)]
            int_pts = set(tuple(p) for p in self.interior_integral_points())
            bnd_pts = set(tuple(p) for p in self.boundary_integral_points())
            dist_pts = set(tuple(p) for p in self.distinguished_boundary_points())
            amb_pts = [pt for pt in all_grid if pt not in int_pts and pt not in bnd_pts]

            # Ambient background lattice points outside Q
            g_plot += point(amb_pts, pointsize=24, color='#94A3B8', alpha=0.5, zorder=2)

            # Polygon interior
            g_plot += polygon(vertices, color=fill_color, alpha=fill_alpha, zorder=3)

            # Boundary edges: distinguish blue line facets (passing through p*) vs non-blue facets
            blue_facets = self._blue_facets()
            for f in poly.facets():
                v_facet = [tuple(v) for v in f.vertices()]
                if len(v_facet) >= 2:
                    p1, p2 = v_facet[0], v_facet[1]
                    if f in blue_facets:
                        g_plot += line([p1, p2], color=blue_line_color, thickness=blue_line_width, zorder=6)
                    else:
                        g_plot += line([p1, p2], color=boundary_color, thickness=boundary_width, zorder=4)

            # Interior lattice points (teal/emerald)
            if int_pts:
                g_plot += point(list(int_pts), pointsize=44, color='#059669', zorder=8)

            # Non-blue boundary lattice points (solid black)
            other_bnd = [p for p in bnd_pts if p not in dist_pts]
            if other_bnd:
                g_plot += point(other_bnd, pointsize=48, color='#0F172A', zorder=9)

            # Distinguished boundary points on blue line (bright blue)
            if dist_pts:
                g_plot += point(list(dist_pts), pointsize=55, color=blue_line_color, zorder=10)

            # Long-side white vertex markers for A-types
            for deco in sides.values():
                if deco.vertex_color == 'white':
                    for vi in deco.edge:
                        v_coord = vertices[vi]
                        g_plot += point(v_coord, pointsize=52, color='black', zorder=11)
                        g_plot += point(v_coord, pointsize=30, color='white', zorder=12)

            # Distinguished point p* marked with red star
            g_plot += point(p_star, pointsize=p_star_size, color=p_star_color, marker='*', zorder=15)

            # Center of polygon for LaTeX label placement
            center_x = sum(p[0] for p in vertices) / len(vertices)
            center_y = sum(p[1] for p in vertices) / len(vertices)

            # Long/Short Side Annotation Labels
            for deco in sides.values():
                v1, v2 = vertices[deco.edge[0]], vertices[deco.edge[1]]
                mid_x = (v1[0] + v2[0]) / 2
                mid_y = (v1[1] + v2[1]) / 2
                dx = float(v2[0] - v1[0])
                dy = float(v2[1] - v1[1])
                length = (dx**2 + dy**2)**0.5
                perp_x = -dy / length * 0.25 if length > 0 else 0
                perp_y = dx / length * 0.25 if length > 0 else 0.25
                g_plot += text(deco.decoration_type, (float(mid_x) + perp_x, float(mid_y) + perp_y),
                               fontsize=side_label_fontsize, color='black', fontweight='bold', zorder=16)
            # Render centered LaTeX label
            g_plot += text(fr'${label}$', (float(center_x), float(center_y + label_y_offset)),
                           fontsize=label_fontsize, color='black', fontweight='bold', zorder=16)

            # Optional interior Dynkin diagram visualization (Notation 821--838 in [AT21])
            show_dynkin_diagram = kwds.get('show_dynkin_diagram', False)
            if show_dynkin_diagram:
                dynkin = self.dynkin_diagram_data()
                dynkin_edge_color = kwds.get('dynkin_edge_color', '#3182ce')
                dynkin_edge_width = kwds.get('dynkin_edge_width', 3)
                dynkin_edges = dynkin.get('edges', [])
                if isinstance(dynkin_edges, list):
                    for e in dynkin_edges:
                        if isinstance(e, tuple) and len(e) >= 2:
                            p1, p2 = e[0], e[1]
                            g_plot += line([(p1[0], p1[1]), (p2[0], p2[1])],
                                           color=dynkin_edge_color, thickness=dynkin_edge_width, zorder=6)
                node_types_dict = dynkin.get('node_types', {})
                if isinstance(node_types_dict, dict):
                    for n, ntype in node_types_dict.items():
                        if isinstance(n, (tuple, list)) and len(n) >= 2:
                            coord = (n[0], n[1])
                            if ntype == 'black':
                                g_plot += point(coord, pointsize=35, color='black', zorder=13)
                            elif ntype == 'white':
                                g_plot += point(coord, pointsize=40, color='black', zorder=13)
                                g_plot += point(coord, pointsize=24, color='white', zorder=14)
                            elif ntype == 'circled_white':
                                g_plot += point(coord, pointsize=55, color=dynkin_edge_color, zorder=12)
                                g_plot += point(coord, pointsize=40, color='white', zorder=13)
                                g_plot += point(coord, pointsize=30, color='black', zorder=14)
                                g_plot += point(coord, pointsize=18, color='white', zorder=15)

            # Configure axes with strictly integer ticks
            show_axes = kwds.get('axes', False)
            x_ticks = list(range(min_x, max_x + 1))
            y_ticks = list(range(min_y, max_y + 1))
            g_plot.axes(show_axes)
            g_plot.set_axes_range(min_x - 0.2, max_x + 0.2, min_y - 0.2, max_y + 0.2)
            g_plot.SHOW_OPTIONS['ticks'] = [x_ticks, y_ticks]
            g_plot.SHOW_OPTIONS['ticks_integer'] = True

            return g_plot

        def _plot_2d(self: _LatticePolytopeInterface, **kwds: object) -> Graphics:
            """Alias for plot2d."""
            return self.plot2d(**kwds)

        def _plot_(self: _LatticePolytopeInterface, **kwds: object) -> Graphics:
            """Internal hook for Sage plot(S)."""
            return self.plot(**kwds)


class ADEBaseSurface(Parent):
    r"""
    The base del Pezzo log pair (Y = V_Q, C + 1/2(1+eps) B) for an ADE surface.

    EXAMPLES::

        sage: from dzack_research.preamble.categories.schemes.ade_surfaces import ADESurface
        sage: s = ADESurface('A', 3, variant=('long', 'long'))
        sage: B = s.base()
        sage: B
        ADE Base Log Pair for A_3 (Y = V_Q, C + ½(1+ε)B, p*=(0, 2))
        sage: B.polygon()
        Lattice Polygon with 3 vertices
        sage: B.area()
        4
    """
    _cover: object

    def __init__(self, cover: object) -> None:
        self._cover = cover
        super().__init__(base=QQ, category=ADELogPairs())

    def cover(self) -> object:
        """Return the covering ADE surface log pair (X, D + eps*R)."""
        return self._cover

    def cover_surface(self) -> object:
        """Alias for cover()."""
        return self.cover()

    def cover_pair(self) -> object:
        """Alias for cover()."""
        return self.cover()

    def covering_pair(self) -> object:
        """Alias for cover()."""
        return self.cover()

    def base(self) -> object:
        """Return self (the base log pair)."""
        return self

    def base_surface(self) -> object:
        """Return self (the base log pair)."""
        return self

    def base_pair(self) -> object:
        """Return self (the base log pair)."""
        return self

    def is_log_pair(self) -> bool:
        """Return True: ADEBaseSurface is a log pair (Y, C + 1/2(1+eps)B)."""
        return True

    def scheme(self) -> ToricVariety_field:
        """Return the underlying toric del Pezzo variety Y = V_Q."""
        return self._cover.del_pezzo_surface()

    def variety(self) -> ToricVariety_field:
        """Return the underlying toric del Pezzo variety Y = V_Q."""
        return self._cover.del_pezzo_surface()

    def del_pezzo_surface(self) -> ToricVariety_field:
        """Return the polarized toric del Pezzo surface Y = V_Q."""
        return self._cover.del_pezzo_surface()

    def associated_divisor(self) -> object:
        r"""
        Return the associated boundary divisor Δ_Y = C + ½(1+ε)B on Y.
        """
        return self._cover.blue_line_divisor()

    def boundary_divisor(self) -> object:
        """Return the distinguished boundary divisor C (the 'blue line') on Y."""
        return self._cover.blue_line_divisor()

    def divisor(self) -> object:
        """Alias for associated_divisor()."""
        return self.associated_divisor()

    def blue_line_divisor(self) -> object:
        """Return the distinguished boundary divisor C (the 'blue line') on Y."""
        return self._cover.blue_line_divisor()

    def branch_divisor(self) -> object:
        """Return the branch divisor B = div(f) on Y."""
        return self.defining_polynomial()

    def ambient_space(self) -> ToricVariety_field:
        """Return the ambient projective toric variety Y = V_Q."""
        return self._cover.del_pezzo_surface()

    def ambient_variety(self) -> ToricVariety_field:
        """Return the ambient projective toric variety Y = V_Q."""
        return self._cover.del_pezzo_surface()

    def ambient_pair(self) -> ToricLogPair:
        """Return the ambient toric variety as a toric log pair (V_Q, Δ_toric)."""
        return ToricLogPair(self.ambient_variety())

    def ambient_log_pair(self) -> ToricLogPair:
        """Alias for ambient_pair()."""
        return self.ambient_pair()

    def codimension(self) -> int:
        """Return 0 (base del Pezzo surface is the ambient toric surface V_Q)."""
        return 0

    def polygon(self) -> LatticePolygon:
        """Return the base 2D lattice polygon Q in category LatticePolygons()."""
        return self._cover.polygon()

    def polyhedron(self) -> Polyhedron_base:
        """Return the Sage Polyhedron for Q."""
        return self._cover.polyhedron()

    def vertices(self) -> tuple[LatticePoint2D, ...]:
        """Return vertices of Q."""
        return self._cover.vertices()

    def p_star(self) -> LatticePoint2D:
        """Return distinguished point p*."""
        return self._cover.p_star()

    def blue_line_divisor(self) -> object:
        """Return boundary divisor C."""
        return self._cover.blue_line_divisor()

    def defining_polynomial(self) -> object:
        """Return branch polynomial f(x, y)."""
        return self._cover.defining_polynomial()

    def parametric_branch_polynomial(self) -> object:
        """Return parametric polynomial f(x, y; c_i)."""
        return self._cover.parametric_branch_polynomial()

    def dynkin_diagram_data(self) -> dict[str, object]:
        """Return Dynkin diagram embedded in Q."""
        return self._cover.dynkin_diagram_data()

    def area(self) -> Rational:
        """Area of Q."""
        return self._cover.area()

    def volume(self) -> Rational:
        """Volume of Q."""
        return self._cover.volume()

    def normalized_volume(self) -> Integer:
        """Normalized volume of Q (2*Area)."""
        return self._cover.normalized_volume()

    def integral_points(self) -> tuple[LatticePoint2D, ...]:
        return self._cover.integral_points()

    def interior_integral_points(self) -> tuple[LatticePoint2D, ...]:
        return self._cover.interior_integral_points()

    def boundary_integral_points(self) -> tuple[LatticePoint2D, ...]:
        return self._cover.boundary_integral_points()

    def distinguished_boundary_points(self) -> tuple[LatticePoint2D, ...]:
        return self._cover.distinguished_boundary_points()

    def n_integral_points(self) -> int:
        return self._cover.n_integral_points()

    def n_interior_points(self) -> int:
        return self._cover.n_interior_points()

    def n_boundary_points(self) -> int:
        return self._cover.n_boundary_points()

    def n_distinguished_points(self) -> int:
        return self._cover.n_distinguished_points()

    def invariants(self) -> dict[str, object]:
        return self._cover.invariants()

    def plot(self, **kwds: object) -> object:
        """Render the 2D publication plot of Q."""
        return ADELogPairs.ParentMethods.plot2d(self._cover, **kwds)

    def tikz(self, **kwds: object) -> str:
        """Render TikZ code for Q."""
        return self._cover.tikz(**kwds)

    def _repr_(self) -> str:
        return f"ADE Base Log Pair for {self._cover._key} (Y = V_Q, C + ½(1+ε)B, p*={self.p_star()})"

    def _latex_(self) -> str:
        r"""LaTeX representation of the 2D base del Pezzo log pair."""
        from sage.misc.latex import latex as _latex
        f0_latex = _latex(self.defining_polynomial())
        c_latex = _latex(self.blue_line_divisor())
        p_latex = _latex(self.p_star())
        eol = "\\\\"
        lines = [
            r"\begin{aligned}",
            rf"&\mathbf{{ADE\ Base\ Log\ Pair\ }} \left(Y = V_Q,\, C + \tfrac{{1+\varepsilon}}{{2}}B\right) \text{{ for }} {self._cover._latex_label} \quad \left(p^* = {p_latex}\right) {eol}",
            rf"&\text{{Underlying Variety: }} Y = V_Q,\quad \text{{Associated Divisor: }} \Delta_Y = C + \tfrac{{1+\varepsilon}}{{2}}B {eol}",
            rf"&\text{{Boundary Divisor: }} C = {c_latex},\quad \text{{Branch Divisor: }} B = \operatorname{{div}}\left({f0_latex}\right) {eol}",
            rf"&\text{{Base Polygon }} Q \subset N_\mathbb{{R}} \colon \operatorname{{Area}}(Q) = {self.area()},\, |Q \cap N| = {self.n_integral_points()},\, |\partial Q \cap N| = {self.n_boundary_points()},\, |\operatorname{{Int}}(Q) \cap N| = {self.n_interior_points()},\, |C \cap N| = {self.n_distinguished_points()}",
            r"\end{aligned}",
        ]
        return "\n".join(lines)

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"

    def _repr_html_(self) -> str:
        """Render high-definition 2D vector SVG representation for Jupyter."""
        try:
            from dzack_research.preamble.categories.schemes.svg_2d_viewer import generate_2d_polygon_svg
            verts = [list(v) for v in self.vertices()]
            int_pts = [list(p) for p in self.interior_integral_points()]
            bnd_pts = [list(p) for p in self.boundary_integral_points()]
            dist_pts = [list(p) for p in self.distinguished_boundary_points()]
            blue_facets = [[[float(c) for c in v] for v in f.vertices()] for f in self._cover._blue_facets()]
            p_star = [float(c) for c in self.p_star()]
            sides = self._cover.side_decorations()
            return generate_2d_polygon_svg(
                verts,
                interior_points=int_pts,
                boundary_points=bnd_pts,
                distinguished_points=dist_pts,
                blue_facets=blue_facets,
                p_star=p_star,
                side_decorations=sides,
                latex_label=self._cover._latex_label,
                theme="dark",
                width=480,
                height=380,
            )
        except Exception:
            return ""

    def _rich_repr_(self, dm: object) -> object:
        if dm.types.OutputHtml in dm.supported_output():
            svg_html = self._repr_html_()
            latex_html = f"\\(\\displaystyle {self._latex_()}\\)"
            html_out = f'<div style="font-family: sans-serif; line-height: 1.4;"><div>{latex_html}</div><div style="margin-top: 14px; max-width: 520px;">{svg_html}</div></div>'
            return dm.types.OutputHtml(html_out)
        elif dm.types.OutputLatex in dm.supported_output():
            return dm.types.OutputLatex(self._latex_())
        elif dm.types.OutputImagePng in dm.supported_output():
            p = self.plot()
            if hasattr(p, '_rich_repr_'):
                return p._rich_repr_(dm)
        elif dm.types.OutputPlainText in dm.supported_output():
            return dm.types.OutputPlainText(repr(self))
        return None

    def _repr_mimebundle_(self, include: object = None, exclude: object = None) -> dict[str, str]:
        svg_html = self._repr_html_()
        latex_html = f"\\(\\displaystyle {self._latex_()}\\)"
        html_out = f'<div style="font-family: sans-serif; line-height: 1.4;"><div>{latex_html}</div><div style="margin-top: 14px; max-width: 520px;">{svg_html}</div></div>'
        return {
            'text/html': html_out,
            'text/latex': self._repr_latex_(),
            'text/plain': repr(self),
        }


class ADESurface(Parent):
    """
    An ADE surface defined by Dynkin letter, rank, and variant following
    Table 1 of Alexeev-Thompson ("ADE surfaces and their moduli", 2021).

    EXAMPLES::

        sage: from dzack_research.preamble.categories.schemes.ade_surfaces import ADESurface
        sage: s = ADESurface('A', 3, variant=('long', 'long'))
        sage: s
        ADE Cover Log Pair for A_3 (X ⊂ V_P, D + εR, p*=(0, 2))
        sage: s.base()
        ADE Base Log Pair for A_3 (Y = V_Q, C + ½(1+ε)B, p*=(0, 2))
        sage: s.covering_polytope()
        Lattice Polytope of dimension 3 with 4 vertices
    """
    _letter: str
    _rank: int
    _variant: tuple[str, ...]
    _affine: bool
    _key: str
    _latex_label: str
    _lattice: ToricLattice_generic
    _ambient_space: Callable[[Sequence[LatticeCoord]], LatticePoint2D]
    _vertices: tuple[LatticePoint2D, ...]
    _p_star: LatticePoint2D
    _sides_info: dict[tuple[int, int], SideDecoration]
    _del_pezzo_variety: ToricVariety_field
    _base_surface: ADEBaseSurface

    def __init__(self, letter: str, rank: int, variant: tuple[str, ...] = (),
                 affine: bool = False, n: Optional[int] = None) -> None:
        self._letter = str(letter).upper()
        if self._letter not in ('A', 'D', 'E'):
            raise ValueError(f"Dynkin letter must be 'A', 'D', or 'E', got '{letter}'")

        self._rank = int(rank)
        if self._rank < 1:
            raise ValueError(f"Rank must be positive integer, got {rank}")

        if not isinstance(variant, tuple):
            raise TypeError(f"variant must be a tuple of strings, got {type(variant).__name__}")
        for v in variant:
            if v not in VALID_DECORATIONS:
                raise ValueError(f"Invalid decoration '{v}'. Must be one of {sorted(VALID_DECORATIONS)}")

        self._variant = variant
        self._affine = bool(affine)

        # 2D ambient integer lattice and rational space
        self._lattice = ToricLattice(2, 'N')
        self._ambient_space = self._lattice.vector_space(QQ)

        self._n = self._resolve_parameter_n(n)
        self._key, self._latex_label, self._vertices, self._p_star, self._sides_info = self._construct_geometry()

        # Initialize Parent with base field and ADELogPairs category
        super().__init__(base=QQ, category=ADELogPairs())

        # Construct underlying toric del Pezzo variety Y = V_Q and base surface
        self._del_pezzo_variety = ToricVariety(self.normal_fan())
        self._base_surface = ADEBaseSurface(self)

    def _resolve_parameter_n(self, explicit_n: Optional[int]) -> int:
        if explicit_n is not None:
            return int(explicit_n)
        if self._letter == 'A':
            if len(self._variant) >= 1 and self._variant[0] == 'short':
                # ^-A_{2n-3} has rank = 2n-3 ==> n = (rank + 3) // 2
                return (self._rank + 3) // 2
            elif len(self._variant) >= 2 and self._variant[1] == 'short':
                # A_{2n-2}^- has rank = 2n-2 ==> n = (rank + 2) // 2
                return (self._rank + 2) // 2
            # A_{2n-1} has rank = 2n-1 ==> n = (rank + 1) // 2
            return (self._rank + 1) // 2
        if self._letter == 'D':
            return (self._rank + 1) // 2
        return 2

    def _construct_geometry(self) -> tuple[str, str, tuple[LatticePoint2D, ...], LatticePoint2D, dict[tuple[int, int], SideDecoration]]:
        if self._affine:
            return self._build_affine_family()
        if self._letter == 'A':
            return self._build_A_family()
        if self._letter == 'D':
            return self._build_D_family()
        if self._letter == 'E':
            return self._build_E_family()
        raise ValueError(f"Unknown Dynkin type: '{self._letter}_{self._rank}'")

    def _build_A_family(self) -> tuple[str, str, tuple[LatticePoint2D, ...], LatticePoint2D, dict[tuple[int, int], SideDecoration]]:
        """
        Pure and Toric Primed A-shapes from Table 1 and Table 4 of Alexeev-Thompson [AT21]:
        - A_{2n-1} (n>=1): p* = (0,2), vertices: (0,2), (0,0), (2n,0)
        - A_{2n-2}^- (n>=1): p* = (0,2), vertices: (0,2), (0,0), (2n-1,0)
        - ^-A_{2n-3}^- (n>=2): p* = (0,2), vertices: (0,2), (1,0), (2n-1,0)
        - 'A_{2n-1} (n>=2, Table 4): p* = (2,2), vertices: (2,2), (0,1), (0,0), (2n-2,0)
        """
        n = self._n
        rank = self._rank
        variant = self._variant
        is_primed = any(v in ('primed', 'prime', 'p') for v in variant)
        left_short = len(variant) >= 1 and variant[0] == 'short'
        right_short = len(variant) >= 2 and variant[1] == 'short'

        sides: dict[tuple[int, int], SideDecoration] = {}

        if is_primed:
            key = f"A_{rank}_prime"
            latex = f"A'_{{{rank}}}"
            raw_v = [(2, 2), (0, 1), (0, 0), (2 * n - 2, 0)]
            p_star = self._ambient_space([QQ(2), QQ(2)])
        elif left_short and right_short:
            key = f"minus_A_{rank}_minus"
            latex = f"^{{-}}A_{{{rank}}}^{{-}}"
            raw_v = [(0, 2), (1, 0), (2 * n - 1, 0)]
            sides[(0, 1)] = SideDecoration((0, 1), 'short', 'black')
            sides[(0, 2)] = SideDecoration((0, 2), 'short', 'black')
            p_star = self._ambient_space([QQ(0), QQ(2)])
        elif left_short:
            key = f"minus_A_{rank}"
            latex = f"^{{-}}A_{{{rank}}}"
            raw_v = [(0, 2), (1, 0), (2 * n - 1, 0)]
            sides[(0, 1)] = SideDecoration((0, 1), 'short', 'black')
            sides[(0, 2)] = SideDecoration((0, 2), 'long', 'white')
            p_star = self._ambient_space([QQ(0), QQ(2)])
        elif right_short:
            key = f"A_{rank}_minus"
            latex = f"A_{{{rank}}}^{{-}}"
            raw_v = [(0, 2), (0, 0), (2 * n - 1, 0)]
            sides[(0, 1)] = SideDecoration((0, 1), 'long', 'white')
            sides[(0, 2)] = SideDecoration((0, 2), 'short', 'black')
            p_star = self._ambient_space([QQ(0), QQ(2)])
        else:
            key = f"A_{rank}"
            latex = f"A_{{{rank}}}"
            raw_v = [(0, 2), (0, 0), (2 * n, 0)]
            sides[(0, 1)] = SideDecoration((0, 1), 'long', 'white')
            sides[(0, 2)] = SideDecoration((0, 2), 'long', 'white')
            p_star = self._ambient_space([QQ(0), QQ(2)])

        vertices = tuple(self._lattice([x, y]) for x, y in raw_v)
        return key, latex, vertices, p_star, sides

    def _build_D_family(self) -> tuple[str, str, tuple[LatticePoint2D, ...], LatticePoint2D, dict[tuple[int, int], SideDecoration]]:
        """
        Pure and Toric Primed D-shapes from Table 1 and Table 4 of Alexeev-Thompson [AT21]:
        - D_{2n} (n>=2): p* = (2,2), vertices: (2,2), (0,2), (0,0), (2n-2,0)
        - D_{2n-1}^- (n>=3): p* = (2,2), vertices: (2,2), (0,2), (0,0), (2n-3,0)
        - D_{2n}' (n>=3, Table 4): p* = (2,2), vertices: (2,2), (0,2), (0,0), (2n-4,0), (n,1)
        """
        n = self._n
        rank = self._rank
        variant = self._variant
        is_primed = any(v in ('primed', 'prime', 'p') for v in variant)
        is_short = 'short' in variant or rank % 2 == 1

        if is_primed:
            key = f"D_{rank}_prime"
            latex = f"D'_{{{rank}}}"
            raw_v = [(2, 2), (0, 2), (0, 0), (2 * n - 4, 0), (n, 1)]
        elif is_short:
            key = f"D_{rank}_minus"
            latex = f"D_{{{rank}}}^{{-}}"
            raw_v = [(2, 2), (0, 2), (0, 0), (2 * n - 3, 0)]
        else:
            key = f"D_{rank}"
            latex = f"D_{{{rank}}}"
            raw_v = [(2, 2), (0, 2), (0, 0), (2 * n - 2, 0)]

        vertices = tuple(self._lattice([x, y]) for x, y in raw_v)
        p_star = self._ambient_space([QQ(2), QQ(2)])
        return key, latex, vertices, p_star, {}

    def _build_E_family(self) -> tuple[str, str, tuple[LatticePoint2D, ...], LatticePoint2D, dict[tuple[int, int], SideDecoration]]:
        """
        Pure E-shapes from Table 1 of Alexeev-Thompson [AT21]:
        - ^-E_6^-: p* = (2,2), vertices: (2,2), (0,3), (0,0), (3,0)
        - ^-E_7:   p* = (2,2), vertices: (2,2), (0,3), (0,0), (4,0)
        - ^-E_8^-: p* = (2,2), vertices: (2,2), (0,3), (0,0), (5,0)
        """
        rank = self._rank
        variant = self._variant
        if rank == 6:
            key = "minus_E_6_minus" if 'short' in variant else "E_6"
            latex = "^{-}E_6^{-}" if key == "minus_E_6_minus" else "E_6"
            raw_v = [(2, 2), (0, 3), (0, 0), (3, 0)]
        elif rank == 7:
            key = "minus_E_7" if 'decorated' in variant or 'short' in variant else "E_7"
            latex = "^{-}E_7" if key == "minus_E_7" else "E_7"
            raw_v = [(2, 2), (0, 3), (0, 0), (4, 0)]
        elif rank == 8:
            key = "minus_E_8_minus" if 'short' in variant else "E_8"
            latex = "^{-}E_8^{-}" if key == "minus_E_8_minus" else "E_8"
            raw_v = [(2, 2), (0, 3), (0, 0), (5, 0)]
        else:
            raise ValueError(f"Invalid E rank: {rank}")

        vertices = tuple(self._lattice([x, y]) for x, y in raw_v)
        p_star = self._ambient_space([QQ(2), QQ(2)])
        return key, latex, vertices, p_star, {}

    def _build_affine_family(self) -> tuple[str, str, tuple[LatticePoint2D, ...], LatticePoint2D, dict[tuple[int, int], SideDecoration]]:
        """
        Type II pure affine shapes from Table 1 of Alexeev-Thompson [AT21]:
        - ~D_{2n} (n>=2): p* = (2,2), vertices: (0,2), (0,0), (2n-4,0), (4,2)
        - ~E_7:           p* = (2,2), vertices: (0,4), (0,0), (4,0)
        - ~E_8^-:         p* = (2,2), vertices: (0,3), (0,0), (6,0)
        - ~A_{2n-1}:      p* = (n/2, 1), vertices: (0,2), (0,0), (2n,0), (n,2)
        """
        letter = self._letter
        rank = self._rank
        n = self._n

        if letter == 'A':
            key = f"tilde_A_{rank}"
            latex = f"\\tilde{{A}}_{{{rank}}}"
            raw_v = [(0, 2), (0, 0), (2 * n, 0), (n, 2)]
            raw_p = [QQ(n) / 2, QQ(1)]
        elif letter == 'D':
            key = f"tilde_D_{rank}"
            latex = f"\\tilde{{D}}_{{{rank}}}"
            raw_v = [(0, 2), (0, 0), (2 * n - 4, 0), (4, 2)]
            raw_p = [QQ(2), QQ(2)]
        elif letter == 'E':
            if rank == 6:
                key = "tilde_E_6"
                latex = "\\tilde{E}_6"
                raw_v = [(0, 3), (0, 0), (3, 0)]
                raw_p = [QQ(1), QQ(1)]
            elif rank == 7:
                key = "tilde_E_7"
                latex = "\\tilde{E}_7"
                raw_v = [(0, 4), (0, 0), (4, 0)]
                raw_p = [QQ(2), QQ(2)]
            elif rank == 8:
                key = "tilde_E_8"
                latex = "\\tilde{E}_8"
                raw_v = [(0, 3), (0, 0), (6, 0)]
                raw_p = [QQ(2), QQ(2)]
            else:
                raise ValueError(f"Invalid affine E rank: {rank}")
        else:
            raise ValueError(f"Unknown affine type: '{letter}_{rank}'")

        vertices = tuple(self._lattice([x, y]) for x, y in raw_v)
        p_star = self._ambient_space(raw_p)
        return key, latex, vertices, p_star, {}

    def _repr_(self) -> str:
        return f"ADE Cover Log Pair for {self._key} (X ⊂ V_P, D + εR, p*={self._p_star})"

    def tikz(self: _ADESurfaceInterface, scale: float = 0.8, show_dynkin_diagram: bool = False) -> str:
        r"""
        Return standard TikZ picture LaTeX code representing the ADE surface polytope Q.
        """
        vertices = [tuple(v) for v in self.vertices()]
        p_star = tuple(self.p_star())
        sides = self.side_decorations()
        label = self.latex_label()
        p_idx = self.p_star_index()
        nv = len(vertices)

        all_pts = list(vertices) + [p_star]
        min_x = min(int(p[0]) for p in all_pts) - 1
        max_x = max(int(p[0]) for p in all_pts) + 1
        min_y = min(int(p[1]) for p in all_pts) - 1
        max_y = max(int(p[1]) for p in all_pts) + 1

        center_x = sum(p[0] for p in vertices) / len(vertices)
        center_y = sum(p[1] for p in vertices) / len(vertices)

        header = [
            rf"\begin{{tikzpicture}}[scale={scale}, baseline]",
            r"\definecolor{blueLine}{HTML}{3182CE}",
            r"\definecolor{starRed}{HTML}{E53E3E}",
            r"\tikzset{ade vertex white/.style={circle, draw=black, fill=white, inner sep=1.8pt, thick}}",
            r"\tikzset{ade vertex black/.style={circle, fill=black, inner sep=2pt}}",
            r"\tikzset{ade star/.style={star, star points=5, star point ratio=2.25, fill=starRed, inner sep=2.5pt}}",
        ]

        grid_lines = [
            rf"\draw[dotted, lightgray] ({min_x},{min_y}) grid ({max_x},{max_y});",
            rf"\foreach \x in {{{min_x},...,{max_x}}} \foreach \y in {{{min_y},...,{max_y}}} \fill[darkgray] (\x,\y) circle (1pt);",
        ]

        poly_path = " -- ".join(f"({v[0]},{v[1]})" for v in vertices) + " -- cycle"
        poly_lines = [
            rf"\fill[fill=gray!12] {poly_path};",
            rf"\draw[black, thick] {poly_path};",
        ]

        # Blue Line: distinguished boundary facets passing through p*
        blue_lines: list[str] = []
        blue_facets = self._blue_facets()
        poly = self.polyhedron()
        for f in poly.facets():
            v_facet = [tuple(v) for v in f.vertices()]
            if len(v_facet) >= 2 and f in blue_facets:
                p1, p2 = v_facet[0], v_facet[1]
                blue_lines.append(rf"\draw[blueLine, line width=2.8pt] ({p1[0]},{p1[1]}) -- ({p2[0]},{p2[1]});")

        # Vertex nodes
        vert_lines: list[str] = []
        for i, v in enumerate(vertices):
            if p_idx is not None and i == p_idx:
                continue
            v_style = "ade vertex black"
            for deco in sides.values():
                if i in deco.edge and deco.vertex_color == 'white':
                    v_style = "ade vertex white"
                    break
            vert_lines.append(rf"\node[{v_style}] at ({v[0]},{v[1]}) {{}};")

        # Distinguished point p*
        star_line = rf"\node[ade star] at ({p_star[0]},{p_star[1]}) {{}};"

        # Centered mathematical label
        label_line = rf"\node at ({float(center_x):.2f},{float(center_y):.2f}) {{$\mathbf{{{label}}}$}};"

        # Side decoration text labels
        side_lines: list[str] = []
        for deco in sides.values():
            v1, v2 = vertices[deco.edge[0]], vertices[deco.edge[1]]
            mid_x = float(v1[0] + v2[0]) / 2.0
            mid_y = float(v1[1] + v2[1]) / 2.0
            dx = float(v2[0] - v1[0])
            dy = float(v2[1] - v1[1])
            length = (dx**2 + dy**2)**0.5
            perp_x = -dy / length * 0.3 if length > 0 else 0
            perp_y = dx / length * 0.3 if length > 0 else 0.3
            side_lines.append(
                rf"\node[font=\footnotesize\bfseries] at ({mid_x + perp_x:.2f},{mid_y + perp_y:.2f}) {{{deco.decoration_type}}};"
            )

        dynkin_lines: list[str] = []
        if show_dynkin_diagram:
            dynkin = self.dynkin_diagram_data()
            edges = dynkin.get('edges', [])
            if isinstance(edges, list):
                for e in edges:
                    if isinstance(e, tuple) and len(e) >= 2:
                        p1, p2 = e[0], e[1]
                        dynkin_lines.append(rf"\draw[blueLine, thick] ({p1[0]},{p1[1]}) -- ({p2[0]},{p2[1]});")
            node_types_dict = dynkin.get('node_types', {})
            if isinstance(node_types_dict, dict):
                for n, ntype in node_types_dict.items():
                    if isinstance(n, (tuple, list)) and len(n) >= 2:
                        if ntype == 'black':
                            dynkin_lines.append(rf"\node[ade vertex black] at ({n[0]},{n[1]}) {{}};")
                        elif ntype == 'white':
                            dynkin_lines.append(rf"\node[ade vertex white] at ({n[0]},{n[1]}) {{}};")
                        elif ntype == 'circled_white':
                            dynkin_lines.append(rf"\node[circle, draw=blueLine, fill=white, inner sep=2.5pt, thick] at ({n[0]},{n[1]}) {{}};")

        return "\n".join([
            *header,
            *grid_lines,
            *poly_lines,
            *blue_lines,
            *vert_lines,
            star_line,
            label_line,
            *side_lines,
            *dynkin_lines,
            r"\end{tikzpicture}",
        ])

    def base(self) -> ADEBaseSurface:
        """Return the base del Pezzo log pair (Y = V_Q, C + 1/2(1+eps) B)."""
        return self._base_surface

    def base_surface(self) -> ADEBaseSurface:
        """Alias for base()."""
        return self.base()

    def base_pair(self) -> ADEBaseSurface:
        """Alias for base()."""
        return self.base()

    def cover(self) -> _ADESurfaceInterface:
        """Return self (the covering ADE surface log pair (X, D + eps*R))."""
        return self

    def cover_surface(self) -> _ADESurfaceInterface:
        """Alias for cover()."""
        return self.cover()

    def cover_pair(self) -> _ADESurfaceInterface:
        """Alias for cover()."""
        return self.cover()

    def covering_pair(self) -> _ADESurfaceInterface:
        """Alias for cover()."""
        return self.cover()

    def ambient_variety(self) -> ToricVariety_field:
        r"""
        Return the ambient projective toric threefold V_P defined by the 3D pyramid P.
        """
        return ToricVariety(self.cover_polytope().normal_fan())

    def ambient_space(self) -> ToricVariety_field:
        """Return the ambient toric threefold V_P."""
        return self.ambient_variety()

    def ambient_pair(self) -> ToricLogPair:
        r"""
        Return the ambient toric variety as a toric log pair (V_P, Δ_toric)
        where Δ_toric = ∑ D_ρ is the full toric boundary divisor.
        """
        return ToricLogPair(self.ambient_variety())

    def ambient_log_pair(self) -> ToricLogPair:
        """Alias for ambient_pair()."""
        return self.ambient_pair()

    def scheme(self) -> object:
        r"""
        Return the underlying anticanonical surface variety X \subset V_P,
        a codimension 1 subscheme of the ambient toric threefold V_P.
        """
        VP = self.ambient_variety()
        try:
            return VP.subscheme([])
        except Exception:
            return VP

    def variety(self) -> object:
        r"""Alias for scheme(): the codimension 1 hypersurface X \subset V_P."""
        return self.scheme()

    def codimension(self) -> int:
        """Return 1 (hypersurface of codimension 1 in the toric threefold V_P)."""
        return 1

    def associated_divisor(self) -> object:
        r"""
        Return the associated boundary divisor Δ_X = D + εR on X.
        """
        return self.blue_line_divisor()

    def boundary_divisor(self) -> object:
        r"""
        Return the preimage boundary divisor D = π*(C) on X.
        """
        return self.blue_line_divisor()

    def divisor(self) -> object:
        """Alias for associated_divisor()."""
        return self.associated_divisor()

    def ramification_divisor(self) -> object:
        r"""
        Return the ramification divisor R on X.
        """
        return self.defining_polynomial()

    def covering_polytope(self) -> LatticePolytope:
        r"""Return the 3-dimensional integral lattice polytope P \subset \mathbb{R}^3."""
        return self.cover_polytope()

    def polytope(self) -> LatticePolytope:
        """Alias for cover_polytope(): the 3D lattice polytope P."""
        return self.cover_polytope()

    def plot(self, **kwds: object) -> object:
        """
        Plot the 3-dimensional covering polytope P for the ADE surface.
        """
        return self.cover_polytope().plot3d(**kwds)

    def plot3d(self, **kwds: object) -> object:
        """Plot the 3-dimensional covering polytope P."""
        return self.cover_polytope().plot3d(**kwds)

    def plot2d(self, **kwds: object) -> object:
        """Plot the 2-dimensional base polygon Q."""
        return self.base().plot(**kwds)

    def _plot_(self: _ADESurfaceInterface, **kwds: object) -> object:
        """Sage standard plotting hook."""
        return self.plot(**kwds)

    def _latex_(self) -> str:
        r"""
        Return mathematical LaTeX representation of the 3D covering ADE anticanonical log pair.
        """
        from sage.misc.latex import latex as _latex
        f0_latex = _latex(self.defining_polynomial())
        p_latex = _latex(self.p_star())
        P = self.cover_polytope()
        eol = "\\\\"

        lines = [
            r"\begin{aligned}",
            rf"&\mathbf{{ADE\ Cover\ Log\ Pair\ }} \left(X \subset V_P,\, D + \varepsilon R\right) \text{{ of type }} {self._latex_label} \quad \left(p^* = {p_latex}\right) {eol}",
            rf"&\text{{Underlying Scheme: }} X = Z\left(z^2 + \left({f0_latex}\right)\right) \subset V_P \text{{ (codimension 1)}} {eol}",
            rf"&\text{{Associated Divisor: }} \Delta_X = D + \varepsilon R,\quad \text{{Ambient Toric Pair: }} \left(V_P,\, \Delta_{{\text{{toric}}}}\right) {eol}",
            rf"&\text{{Cover Polytope }} P \subset N \oplus \mathbb{{Z}} \colon \operatorname{{Vol}}(P) = {P.volume()},\, \operatorname{{Vol}}_\mathbb{{Z}}(P) = {P.normalized_volume()},\, |P \cap N_3| = {P.n_integral_points()} {eol}",
            rf"&\text{{Base Del Pezzo Log Pair: }} \left(Y = V_Q,\, C + \tfrac{{1+\varepsilon}}{{2}}B\right)",
            r"\end{aligned}",
        ]
        return "\n".join(lines)

    def _repr_latex_(self) -> str:
        """Return MathJax LaTeX for IPython/Jupyter display."""
        return "$\\displaystyle " + self._latex_() + "$"

    def _rich_repr_(self: _ADESurfaceInterface, dm: object) -> object:
        """Rich display hook for Sage display manager: renders the 3D Three.js model."""
        if dm.types.OutputHtml in dm.supported_output():
            html = self._repr_html_()
            if html:
                latex_html = f"\\(\\displaystyle {self._latex_()}\\)"
                combined_html = f'<div style="font-family: sans-serif; line-height: 1.4;"><div>{latex_html}</div><div style="margin-top: 14px;">{html}</div></div>'
                return dm.types.OutputHtml(combined_html)
        elif dm.types.OutputSceneThreejs in dm.supported_output():
            return self.cover_polytope()._rich_repr_(dm)
        elif dm.types.OutputLatex in dm.supported_output():
            return dm.types.OutputLatex(self._latex_())
        elif dm.types.OutputPlainText in dm.supported_output():
            return dm.types.OutputPlainText(repr(self))
        return None

    def _repr_html_(self: _ADESurfaceInterface) -> Optional[str]:
        """HTML representation hook for Jupyter Notebooks: renders the 3D Three.js interactive canvas."""
        try:
            from dzack_research.preamble.categories.schemes.threejs_viewer import generate_threejs_polytope_html
            P = self.cover_polytope()
            poly = P.polyhedron()
            verts = [list(v) for v in poly.vertices()]
            facets = [[verts.index(list(v)) for v in f.vertices()] for f in poly.facets()]
            int_pts = [list(p) for p in P.interior_integral_points()]
            bnd_pts = [list(p) for p in P.boundary_integral_points()]
            p_star_3d = [self.p_star()[0], self.p_star()[1], 0]
            return generate_threejs_polytope_html(
                verts,
                facets,
                interior_points=int_pts,
                boundary_points=bnd_pts,
                p_star=p_star_3d,
                title=f"ADE Cover Hypersurface {self._key} (X ⊂ V_P)",
                latex_label=self._latex_label,
                invariants=P.invariants(),
            )
        except Exception:
            return self.cover_polytope()._repr_html_()

    def _repr_mimebundle_(self: _ADESurfaceInterface, include: object = None, exclude: object = None) -> dict[str, str]:
        """IPython / Jupyter display bundle showing 3D LaTeX summary and 3D Three.js canvas."""
        html_3d = self._repr_html_() or ""
        latex_html = f"\\(\\displaystyle {self._latex_()}\\)"
        combined_html = f'<div style="font-family: sans-serif; line-height: 1.4;"><div>{latex_html}</div><div style="margin-top: 14px;">{html_3d}</div></div>'
        return {
            'text/html': combined_html,
            'text/latex': self._repr_latex_(),
            'text/plain': repr(self),
        }
