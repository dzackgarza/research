r"""Category hierarchy and model for ADE surfaces as del Pezzo and anticanonical log pairs.

Hierarchy:
  LogPairs()
    ├── ToricLogPairs() ───────────────> (V, Δ_toric)
    └── ADELogPairs() ─────────────────> the cover X and the base Y alike
          ├── ADESurfaces() ───────────> X ⊂ V_P with D + eps*R
          └── ADEBaseSurfaces() ───────> Y = V_Q with C + (1+eps)/2 * B

ADELogPairs() is also a subcategory of ToricSchemes(QQ).Subobjects(): both the
cover and the base are subschemes of a toric scheme, each carrying its own
inclusion.

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
   - Branch Divisor B = div(f):
     Defined by section f(x, y) with Newton polygon Q (Eq. 3.4-3.6 in [AT21]).

3. Anticanonical ADE Surface Pair (X, D + eps * R):
   - 3D Pyramidal Polytope P = cone(Q) + (p*, 2) in N_3.
   - Ambient Toric Threefold V_P.
   - Anticanonical ADE Surface X = Z(z^2 + f(x, y)) \subset V_P.
     The branched double cover pi: X -> Y branched along B.
   - Boundary Divisor D = pi^*(C) on X.
   - Del Pezzo Involution iota_dP: z |-> -z with quotient X / iota_dP = Y.

EXAMPLES::

    sage: from dzack_research.preamble.categories.schemes.ade_surfaces import ADESurface, LogPairs, ADELogPairs
    sage: S = ADESurface('A', 3, variant=('long', 'long'))
    sage: S.category()
    Category of a d e surfaces (X, D)
    sage: S in LogPairs()
    True
    sage: S.ambient_identification()
    'PP(1,1,2,2)'
    sage: S.base().ambient_identification()
    'PP(1,1,2)'
    sage: S.base().cover() is S
    True
"""

from typing import Any, Callable, NamedTuple, Optional, Protocol, Sequence, TYPE_CHECKING
from dzack_research.preamble.owned_category_bases import Category
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.sets.owned_sets import Sets
from sage.structure.parent import Parent

if TYPE_CHECKING:
    from dzack_research.preamble.owned_category import ConstructionData
from sage.geometry.toric_lattice import ToricLattice, ToricLattice_generic
from sage.geometry.polyhedron.constructor import Polyhedron as polyhedron

from dzack_research.preamble.lexicon import Polyhedron
from sage.schemes.toric.variety import ToricVariety, ToricVariety_field
from sage.combinat.root_system.cartan_type import CartanType
from sage.rings.rational_field import QQ, RationalField
from sage.rings.integer_ring import ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.matrix.constructor import matrix
from sage.plot.graphics import Graphics
from sage.plot.line import line
from sage.plot.polygon import polygon
from sage.plot.point import point
from sage.plot.text import text

from sage.rings.rational import Rational
from sage.rings.integer import Integer
from sage.symbolic.ring import SR
from dzack_research.preamble.categories.schemes.polytopes import (
    LatticePolygon, LatticePolytope, LatticePolygons, LatticePolytopes,
    ConvexPolygon, ConvexPolytope, ConvexPolygons, ConvexPolytopes
)
from dzack_research.preamble.categories.schemes.toric.toric_schemes import (
    ToricSchemes, ToricScheme, ToricSubscheme, FormalDivisor
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
    def as_polyhedron(self) -> Polyhedron: ...
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


class IntegralInvariants(NamedTuple):
    r"""
    Integral invariants of the ambient polytope of an ADE log pair.

    Attributes:
        dimension: Dimension of the ambient toric variety.
        volume: Euclidean volume of the ambient polytope.
        normalized_volume: Normalized lattice volume.
        n_integral_points: Total lattice points in the polytope.
        n_interior_points: Interior lattice points.
        n_boundary_points: Boundary lattice points.
    """
    dimension: int
    volume: Rational
    normalized_volume: int
    n_integral_points: int
    n_interior_points: int
    n_boundary_points: int

    def __repr__(self) -> str:
        return (f"dim={self.dimension}, Vol={self.volume}, "
                f"Vol_Z={self.normalized_volume}, "
                f"|P∩Z|={self.n_integral_points}, "
                f"|Int(P)|={self.n_interior_points}, "
                f"|∂P|={self.n_boundary_points}")

    def _latex_(self) -> str:
        return (rf"\dim={self.dimension},\; "
                rf"\operatorname{{Vol}}(P)={self.volume},\; "
                rf"\operatorname{{Vol}}_\mathbb{{Z}}(P)={self.normalized_volume},\; "
                rf"|P \cap \mathbb{{Z}}|={self.n_integral_points},\; "
                rf"|\operatorname{{Int}}(P)|={self.n_interior_points},\; "
                rf"|\partial P|={self.n_boundary_points}")

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"


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
    def pyramid_polytope(self) -> Polyhedron: ...
    def area(self) -> LatticeCoord: ...
    def volume(self) -> LatticeCoord: ...
    def plot(self, **kwds: object) -> Graphics: ...


class LogPairs(Category):
    """
    The category of algebraic log pairs (X, Δ).
    """
    def super_categories(self) -> list[Category]:
        return [Sets()]

    def _repr_object_names(self) -> str:
        return "log pairs"

    def _latex_(self) -> str:
        return r"\mathbf{Cat}\left(\text{Log Pairs}\right)"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"

    class ParentMethods:
        """Generic methods for log pairs (X, Δ)."""

        def is_log_pair(self) -> bool:
            return True


class ToricLogPairs(Category):
    """
    The category of toric log pairs (V, Δ_toric): a normal toric variety V
    with a torus-invariant boundary divisor.
    """
    def super_categories(self) -> list[Category]:
        return [LogPairs()]

    def _repr_object_names(self) -> str:
        return "toric log pairs"

    def _latex_(self) -> str:
        return r"\mathbf{Cat}\left(\text{Toric Log Pairs}\right)"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"

    class ParentMethods:
        """A normal toric variety V together with a boundary divisor."""

        _variety: ToricVariety_field
        _divisor: object

        def __init__(
            self,
            variety: ToricVariety_field,
            divisor: Optional[object] = None,
            **rest: "ConstructionData",
        ) -> None:
            r"""Build the pair (V, Δ), taking the whole toric boundary by default."""
            self._variety = variety
            if divisor is None:
                nrays = variety.fan().nrays()
                self._divisor = sum((variety.divisor(i) for i in range(nrays)), variety.divisor_group().zero())
            else:
                self._divisor = divisor
            super().__init__(base=variety.base_ring(), **rest)

        def scheme(self) -> ToricVariety_field:
            return self._variety

        def variety(self) -> ToricVariety_field:
            return self._variety

        def associated_divisor(self) -> object:
            return self._divisor

        def boundary_divisor(self) -> object:
            return self._divisor

        def divisor(self) -> object:
            return self._divisor

        def ambient_space(self) -> ToricVariety_field:
            return self._variety

        def ambient_variety(self) -> ToricVariety_field:
            return self._variety

        def ambient_pair(self) -> Parent:
            return self

        def ambient_log_pair(self) -> Parent:
            return self

        def codimension(self) -> int:
            return 0

        def _repr_(self) -> str:
            return f"Toric Log Pair ({self._variety}, toric boundary)"

        def _latex_(self) -> str:
            from sage.misc.latex import latex as _latex
            return rf"\left({_latex(self._variety)},\, \Delta_{{\text{{toric}}}}\right)"

        def _repr_latex_(self) -> str:
            return "$\\displaystyle " + self._latex_() + "$"


class ADELogPairs(Category):
    """
    The category of ADE surface log pairs, both the cover X and the base Y.
    """
    def super_categories(self) -> list[Category]:
        return [LogPairs(), ToricSchemes(QQ).Subobjects()]

    def _repr_object_names(self) -> str:
        return "a d e surfaces (Y, C)"

    def _latex_(self) -> str:
        return r"\mathbf{Cat}\left(\text{ADE Surfaces } (Y, C)\right)"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"

    class ParentMethods:
        """What the cover X and the base Y answer alike."""

        def cover(self) -> Parent:
            """Return the covering ADE surface log pair (X, D + eps*R)."""
            raise NotImplementedError

        def base(self) -> Parent:
            """Return the base del Pezzo log pair (Y = V_Q, C + 1/2(1+eps)B).

            ``base`` on these pairs names the base of the double cover, not
            the base ring.  ``base_ring`` is unaffected: it reads the ring the
            construction recorded, never this method.
            """
            raise NotImplementedError

        def is_cover(self) -> bool:
            """Return True if this is the covering hypersurface X ⊂ V_P."""
            raise NotImplementedError

        def is_base(self) -> bool:
            """Return True if this is the base del Pezzo surface Y = V_Q."""
            raise NotImplementedError

        def cover_surface(self) -> Parent:
            return self.cover()

        def base_surface(self) -> Parent:
            return self.base()

        def cover_pair(self) -> Parent:
            return self.cover()

        def base_pair(self) -> Parent:
            return self.base()

        def covering_pair(self) -> Parent:
            return self.cover()

        def ade_type(self) -> str:
            """Return the ADE singularity type key."""
            return self.cover().key()

        def letter(self) -> str:
            return self.cover()._letter

        def rank(self) -> int:
            return self.cover()._rank

        def variant(self) -> tuple[str, ...]:
            return self.cover()._variant

        def is_affine(self) -> bool:
            return self.cover()._affine

        def key(self) -> str:
            return self.cover()._key

        def latex_label(self) -> str:
            return self.cover()._latex_label

        def cartan_type(self) -> CartanType:
            cov = self.cover()
            if cov is not self:
                return cov.cartan_type()
            if self._affine:
                return CartanType([self._letter, self._rank, 1])
            return CartanType([self._letter, self._rank])

        def dynkin_diagram(self) -> object:
            return self.cartan_type().dynkin_diagram()

        def p_star(self) -> LatticePoint2D:
            return self.cover()._p_star

        def polytope_matrix(self) -> matrix:
            """Return integer matrix whose rows are the vertices of the ambient polytope."""
            poly = self.polytope()
            if hasattr(poly, 'polyhedron'):
                poly = poly.polyhedron()
            verts = [[ZZ(c) for c in v] for v in poly.vertices()]
            return matrix(ZZ, verts)

        def ramification_divisor(self) -> Parent:
            r"""Return the ramification divisor R = V(z, f(x, y)) ⊂ V_P as a ToricSubscheme."""
            return self.cover().ramification_divisor()

        def branch_divisor(self) -> Parent:
            r"""Return the branch divisor B = V(f(x, y)) ⊂ V_Q as a ToricSubscheme."""
            return self.base().branch_divisor()

        def boundary_divisor(self) -> object:
            r"""Return the distinguished boundary divisor (D on X, C on Y)."""
            raise NotImplementedError

        def log_divisor(self) -> object:
            r"""Return the full expanded log pair divisor (Delta_X on X, Delta_Y on Y)."""
            raise NotImplementedError

        def log_pair(self) -> tuple[Any, ...]:
            r"""Return the constituents of the log pair."""
            raise NotImplementedError

        def log_pair_label(self) -> str:
            r"""Return LaTeX label for the log pair."""
            raise NotImplementedError

        def integral_invariants(self) -> IntegralInvariants:
            """Return integral invariants of the ambient polytope."""
            P = self.polytope()
            poly = P.polyhedron() if hasattr(P, 'polyhedron') else P
            pts = poly.integral_points()
            n_pts = len(pts)

            if hasattr(P, 'n_interior_points') and callable(P.n_interior_points):
                int_pts = P.n_interior_points()
            else:
                int_pts = sum(1 for pt in pts if all(h.eval(pt) > 0 for h in poly.Hrepresentation()))

            bnd_pts = n_pts - int_pts
            if hasattr(P, 'normalized_volume'):
                norm_vol = P.normalized_volume()
            else:
                mult = 6 if self.ambient_dimension() == 3 else (2 if self.ambient_dimension() == 2 else 1)
                norm_vol = poly.volume() * mult

            return IntegralInvariants(
                dimension=int(self.ambient_dimension()),
                volume=poly.volume(),
                normalized_volume=int(norm_vol),
                n_integral_points=int(n_pts),
                n_interior_points=int(int_pts),
                n_boundary_points=int(bnd_pts),
            )

        def cartan_type_latex(self) -> object:
            r"""Return LaTeX expression for the Cartan type with label."""
            from sage.misc.latex import LatexExpr, latex as _latex
            return LatexExpr(r"\text{Cartan type: }\," + _latex(self.cartan_type()))

        def ambient_latex(self) -> object:
            r"""Return LaTeX expression for the ambient variety with dimension and codimension."""
            from sage.misc.latex import LatexExpr
            return LatexExpr(
                r"\text{Ambient: }\," + self.ambient_identification_latex()
                + r"\quad (\dim=%d,\,\operatorname{codim}=%d)" % (self.ambient_dimension(), self.codimension())
            )

        def _repr_latex_(self) -> str:
            return "$\\displaystyle " + self._latex_() + "$"

        def _rich_repr_(self, dm: object) -> object:
            if dm.types.OutputHtml in dm.supported_output():
                html_content = self._repr_html_()
                latex_html = f"\\(\\displaystyle {self._latex_()}\\)"
                combined_html = f'<div style="font-family: sans-serif; line-height: 1.4;"><div>{latex_html}</div><div style="margin-top: 14px;">{html_content}</div></div>'
                return dm.types.OutputHtml(combined_html)
            elif dm.types.OutputLatex in dm.supported_output():
                return dm.types.OutputLatex(self._latex_())
            elif dm.types.OutputPlainText in dm.supported_output():
                return dm.types.OutputPlainText(repr(self))
            return None

        def _repr_mimebundle_(self, include: object = None, exclude: object = None) -> dict[str, str]:
            html_content = self._repr_html_() or ""
            latex_html = f"\\(\\displaystyle {self._latex_()}\\)"
            combined_html = f'<div style="font-family: sans-serif; line-height: 1.4;"><div>{latex_html}</div><div style="margin-top: 14px;">{html_content}</div></div>'
            return {
                'text/html': combined_html,
                'text/latex': self._repr_latex_(),
                'text/plain': repr(self),
            }


class ADEBaseSurfaces(Category):
    """
    The category of base del Pezzo log pairs (Y = V_Q, C) of an ADE surface.
    """
    def super_categories(self) -> list[Category]:
        return [ADELogPairs()]

    def _repr_object_names(self) -> str:
        return "a d e base surfaces (Y, C)"

    def _latex_(self) -> str:
        return r"\mathbf{Cat}\left(\text{ADE Base Surfaces } (Y, C)\right)"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"

    class ParentMethods:
        """The base del Pezzo surface pair (Y = V_Q, C) of its cover."""

        _cover: Parent

        def __init__(self, cover: Parent, **rest: "ConstructionData") -> None:
            r"""Build Y = V_Q, the toric surface of the polygon Q of ``cover``."""
            self._cover = cover
            amb_scheme = ToricScheme(cover.polygon().polyhedron(), dim=2)
            super().__init__(
                ambient=amb_scheme, equations=(0,), dim=2, base_ring=QQ, **rest
            )

        def cover(self) -> Parent:
            return self._cover

        def base(self) -> Parent:
            return self

        def is_cover(self) -> bool:
            return False

        def is_base(self) -> bool:
            return True

        def polygon(self) -> Parent:
            return self._cover.polygon()

        def polytope(self) -> Parent:
            return self.polygon()

        def polyhedron(self) -> Polyhedron:
            return self._cover.polyhedron()

        def vertices(self) -> tuple[LatticePoint2D, ...]:
            return self._cover.vertices()

        def blue_line_divisor(self) -> object:
            return self._cover.blue_line_divisor()

        def complementary_divisor(self) -> object:
            return self._cover.complementary_divisor()

        def boundary_divisor(self) -> FormalDivisor:
            r"""Return the explicit computed boundary divisor C on Y = V_Q."""
            c_div = self.blue_line_divisor()
            c_terms = []
            for coeff, poly in c_div:
                sub = ToricSubscheme(ambient=self.ambient_space(), equations=(poly,), dim=1, base_ring=self.base_ring())
                c_terms.append((coeff, sub))
            return FormalDivisor(c_terms, ambient=self.ambient_space())

        def branch_divisor(self) -> Parent:
            r"""Return the branch divisor B = V(f(x, y)) ⊂ V_Q as a ToricSubscheme."""
            f0 = self.defining_polynomial()
            return ToricSubscheme(
                ambient=self.ambient_space(),
                equations=(f0,),
                dim=1,
                base_ring=self.base_ring(),
            )

        def log_divisor(self) -> FormalDivisor:
            r"""Return the full expanded log pair divisor Delta_Y = C + 1/2(1+eps)B on Y."""
            c_div = self.boundary_divisor()
            b_sub = self.branch_divisor()
            return FormalDivisor(c_div.terms() + [('1/2(1+eps)', b_sub)], ambient=self.ambient_space())

        def log_pair(self) -> tuple[Any, ...]:
            return (self, self.log_divisor())

        def log_pair_label(self) -> str:
            return r"(Y, C + \tfrac{1+\varepsilon}{2} B)"

        def defining_polynomial(self) -> object:
            return self._cover.defining_polynomial()

        def parametric_branch_polynomial(self) -> object:
            return self._cover.parametric_branch_polynomial()

        def dynkin_diagram_data(self) -> dict[str, object]:
            return self._cover.dynkin_diagram_data()

        def volume(self) -> Rational:
            return self._cover.volume()

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

        def plot(self, **kwds: object) -> Graphics:
            return self._cover.plot2d(**kwds)

        def plot2d(self, **kwds: object) -> Graphics:
            return self.plot(**kwds)

        def _latex_(self) -> str:
            from sage.misc.latex import latex as _latex
            p_latex = _latex(self.p_star())
            Q = self.polygon()
            vol_val = Q.volume()
            norm_vol = 2 * vol_val
            n_pts = Q.n_integral_points()
            int_pts = Q.n_interior_points()
            amb_ident = self.ambient_identification_latex()
            delta_y_latex = self.log_divisor()._latex_()
            eol = "\\\\"
            dim_y = self.ambient_dimension()
            if dim_y in (2, 3):
                inv_line = rf"&\operatorname{{Vol}}_\mathbb{{Z}}(Q) = {norm_vol},\; \operatorname{{Vol}}(Q) = {vol_val},\; |Q \cap \mathbb{{Z}}^2| = {n_pts},\; |\operatorname{{Int}}(Q)| = {int_pts}"
            else:
                mat_lat = _latex(self.polytope_matrix())
                inv_line = rf"&Q = \operatorname{{conv}}\left({mat_lat}\right) \colon \operatorname{{Vol}}_\mathbb{{Z}}(Q) = {norm_vol},\; \operatorname{{Vol}}(Q) = {vol_val},\; |Q \cap \mathbb{{Z}}^{{{dim_y}}}| = {n_pts},\; |\operatorname{{Int}}(Q)| = {int_pts}"
            lines = [
                r"\begin{aligned}",
                rf"&(Y, C + \tfrac{{1+\varepsilon}}{{2}} B) \colon Y = {amb_ident} \text{{ of type }} {self._cover._latex_label} \quad \left(p^* = {p_latex}\right) {eol}",
                rf"&C + \tfrac{{1+\varepsilon}}{{2}} B = {delta_y_latex} {eol}",
                inv_line,
                r"\end{aligned}",
            ]
            return "\n".join(lines)

        def __repr__(self) -> str:
            amb = self.ambient_identification()
            delta_y = repr(self.log_divisor())
            return f"Log Pair (Y, C + 1/2(1+eps)B) where Y = {amb} of type {self._cover._key} (C + 1/2(1+eps)B = {delta_y}, p* = {self.p_star()})"

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


class ADESurfaces(Category):
    """
    The category of covering ADE surface log pairs (X ⊂ V_P, D + eps*R).

    An object is defined by Dynkin letter, rank, and variant following Table 1
    of Alexeev-Thompson ("ADE surfaces and their moduli", 2021).
    """
    def super_categories(self) -> list[Category]:
        return [ADELogPairs()]

    def _repr_object_names(self) -> str:
        return "a d e surfaces (X, D)"

    def _latex_(self) -> str:
        return r"\mathbf{Cat}\left(\text{ADE Surfaces } (X, D)\right)"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"

    class ParentMethods:
        """The anticanonical ADE surface pair (X, D + eps*R)."""


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
        _base_surface: Parent

        def __init__(self, letter: str, rank: int, variant: tuple[str, ...] = (),
                     affine: bool = False, n: Optional[int] = None,
                     **rest: "ConstructionData") -> None:
            r"""Build the ADE surface of a Dynkin letter, rank and variant."""
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

            # Construct ambient toric threefold V_P
            pyr_poly = self._construct_pyramid_polyhedron()
            amb_scheme = ToricScheme(pyr_poly, dim=3)

            # X = Z(z^2 + f(x, y)) is cut out of V_P by one equation
            eqs = (self.anticanonical_equation(),)
            super().__init__(
                ambient=amb_scheme, equations=eqs, dim=2, base_ring=QQ, **rest
            )

            # Construct underlying toric del Pezzo variety Y = V_Q and base surface
            self._del_pezzo_variety = ToricVariety(self.normal_fan())
            self._base_surface = ADEBaseSurface(self)

        def cover(self) -> Parent:
            return self

        def base(self) -> Parent:
            return self._base_surface

        def is_cover(self) -> bool:
            return True

        def is_base(self) -> bool:
            return False

        def _resolve_parameter_n(self, explicit_n: Optional[int]) -> int:
            if explicit_n is not None:
                return int(explicit_n)
            if self._letter == 'A':
                if len(self._variant) >= 1 and self._variant[0] == 'short':
                    return (self._rank + 3) // 2
                elif len(self._variant) >= 2 and self._variant[1] == 'short':
                    return (self._rank + 2) // 2
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

        def _identify_Y_ambient(self) -> str:
            """Identify the base ambient toric surface V_Q."""
            poly = self.polyhedron()
            verts = [tuple(v) for v in poly.vertices()]
            v_set = set(verts)
            for k in range(1, 10):
                if v_set == {(0, 0), (k, 0), (0, k)} or v_set == {(0, 0), (0, k), (k, 0)}:
                    return r"\mathbb{P}^2" if k == 1 else rf"\mathbb{{P}}^2 \text{{ (deg }} {k}\text{{)}}"
            return "V_Q"

        def _construct_pyramid_polyhedron(self) -> Polyhedron:
            """Construct the 3D pyramidal polyhedron P in N_3."""
            q_verts = [list(v) for v in self.vertices()]
            p_star = list(self.p_star())
            p_apex = [p_star[0], p_star[1], 2]
            p_base_verts = [[v[0], v[1], 0] for v in q_verts]
            all_3d_verts = p_base_verts + [p_apex]
            return polyhedron(vertices=all_3d_verts, base_ring=ZZ)

        def pyramid_polytope(self) -> Polyhedron:
            return self._construct_pyramid_polyhedron()

        def cover_polytope(self) -> Parent:
            return LatticePolytope(self.pyramid_polytope())

        def covering_polytope(self) -> Parent:
            return self.cover_polytope()

        def polytope(self) -> Parent:
            return self.cover_polytope()

        def polygon(self) -> Parent:
            return LatticePolygon(self.vertices())

        def polyhedron(self) -> Polyhedron:
            verts = [list(v) for v in self.vertices()]
            return polyhedron(vertices=verts, base_ring=ZZ)

        def vertices(self) -> tuple[LatticePoint2D, ...]:
            return self._vertices

        def side_decorations(self) -> dict[tuple[int, int], SideDecoration]:
            return dict(self._sides_info)

        def normal_fan(self) -> object:
            return self.polyhedron().normal_fan()

        def volume(self) -> Rational:
            if self.is_affine():
                return self.polygon().volume()
            return self.cover_polytope().polyhedron().volume()

        def normalized_volume(self) -> int:
            if self.is_affine():
                return int(2 * self.polygon().volume())
            return int(self.cover_polytope().normalized_volume())

        def boundary_divisor(self) -> FormalDivisor:
            r"""Return the explicit computed preimage boundary divisor D = pi^*(C) on X."""
            c_div = self.blue_line_divisor()
            f0 = self.defining_polynomial()
            z_var = SR.var('z')
            d_terms = []
            for coeff, poly in c_div:
                sub = ToricSubscheme(
                    ambient=self.ambient_space(),
                    equations=(poly, z_var**2 + f0),
                    dim=1,
                    base_ring=self.base_ring(),
                )
                d_terms.append((coeff, sub))
            return FormalDivisor(d_terms, ambient=self.ambient_space())

        def ramification_divisor(self) -> Parent:
            r"""Return the ramification divisor R = V(z, f(x, y)) ⊂ V_P as a ToricSubscheme."""
            f0 = self.defining_polynomial()
            return ToricSubscheme(
                ambient=self.ambient_space(),
                equations=(SR.var('z'), f0),
                dim=1,
                base_ring=self.base_ring(),
            )

        def log_divisor(self) -> FormalDivisor:
            r"""Return the full expanded log pair divisor Delta_X = D + eps*R on X."""
            d_div = self.boundary_divisor()
            r_sub = self.ramification_divisor()
            return FormalDivisor(d_div.terms() + [('eps', r_sub)], ambient=self.ambient_space())

        def log_pair(self) -> tuple[Any, ...]:
            return (self, self.log_divisor())

        def log_pair_label(self) -> str:
            return r"(X, D + \varepsilon R)"

        def del_pezzo_surface(self) -> ToricVariety_field:
            return self._del_pezzo_variety

        def variety(self) -> ToricVariety_field:
            return self._del_pezzo_variety

        def scheme(self) -> ToricVariety_field:
            return self._del_pezzo_variety

        def blue_line_divisor(self) -> object:
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

        def complementary_divisor(self) -> object:
            y_variety = self.del_pezzo_surface()
            poly_q = self.polyhedron()
            p_star = self._lattice.vector_space(QQ)(list(self.p_star()))

            non_blue_ray_indices: list[int] = []
            for idx, f in enumerate(poly_q.facets()):
                if not f.as_polyhedron().contains(p_star):
                    non_blue_ray_indices.append(idx)

            if not non_blue_ray_indices:
                return y_variety.divisor_group().zero()
            return sum((y_variety.divisor(idx) for idx in non_blue_ray_indices), y_variety.divisor_group().zero())

        def _blue_facets(self) -> list[_PolyhedronFace]:
            poly_q = self.polyhedron()
            p_star = self._lattice.vector_space(QQ)(list(self.p_star()))
            return [f for f in poly_q.facets() if f.as_polyhedron().contains(p_star)]

        def defining_polynomial(self) -> object:
            letter = self._letter
            rank = self._rank
            variant = self._variant
            affine = self._affine

            if letter == 'A':
                ring_a = PolynomialRing(QQ, names=['x', 'y'])
                x, y = ring_a.gens()
                if any(v in ('primed', 'prime', 'p') for v in variant):
                    return -QQ(1)/QQ(4) * (x * y)**2 + x**2 + y
                is_right_short = len(variant) >= 2 and variant[1] == 'short'
                is_left_short = len(variant) >= 1 and variant[0] == 'short'
                if is_left_short and is_right_short:
                    return -QQ(1)/QQ(4) * (x * y)**2 + x**2 + x + y
                elif is_left_short:
                    return -QQ(1)/QQ(4) * (x * y)**2 + x**2 + y
                elif is_right_short:
                    return -QQ(1)/QQ(4) * (x * y)**2 + x**2 + y
                return -QQ(1)/QQ(4) * (x * y)**2 + x**2 + y
            elif letter == 'D':
                ring_d = PolynomialRing(QQ, names=['x', 'y'])
                x, y = ring_d.gens()
                if affine:
                    return -QQ(1)/QQ(4) * (x * y)**2 + y**2 + x**(rank - 2)
                if any(v in ('primed', 'prime', 'p') for v in variant):
                    return -QQ(1)/QQ(4) * (x * y)**2 + x**2 + y**2
                return -QQ(1)/QQ(4) * (x * y)**2 + x**2 + y**2
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

        def anticanonical_equation(self) -> object:
            f_0 = self.defining_polynomial()
            ring_3d = PolynomialRing(QQ, names=['x', 'y', 'z'])
            x, y, z = ring_3d.gens()
            return z**2 + f_0(x, y)

        def parametric_branch_polynomial(self) -> object:
            letter = self.letter()
            rank = self.rank()

            if letter == 'A':
                c_names = [f'c{i}' for i in range(1, rank)] + ['c_pp']
                c_latex = [f'c_{{{i}}}' for i in range(1, rank)] + [r"c''"]
                ring_a = PolynomialRing(QQ, names=['x', 'y'] + c_names)
                ring_a._latex_names = ['x', 'y'] + c_latex
                gens = ring_a.gens()
                x, y = gens[0], gens[1]
                c = gens[2:]

                poly = -QQ(1)/QQ(4) * (x * y)**2 + QQ(1)/QQ(2) * (x * y) * c[-1] - QQ(1)/QQ(4) * (c[-1])**2
                poly += x**2 + x * c[0]
                for i in range(1, rank - 1):
                    poly += c[i] * x**(i + 1)
                poly += y + c[1] if rank >= 3 else y
                return poly

            elif letter == 'D':
                c_names = [f'c{i}' for i in range(1, rank - 1)] + ['cp1', 'c_pp']
                ring_d = PolynomialRing(QQ, names=['x', 'y'] + c_names)
                gens = ring_d.gens()
                x, y = gens[0], gens[1]
                c = gens[2:]

                poly = -QQ(1)/QQ(4) * (x * y)**2 + QQ(1)/QQ(2) * (x * y) * c[-1] - QQ(1)/QQ(4) * (c[-1])**2
                poly += x**2 + y**2 + x * c[0] + y * c[-2]
                if len(c) >= 3:
                    poly += c[1]
                return poly

            elif letter == 'E':
                if rank == 6:
                    c_names = ['c1', 'c2', 'c3', 'cp1', 'cp2', 'c_pp']
                    ring_e = PolynomialRing(QQ, names=['x', 'y'] + c_names)
                    gens = ring_e.gens()
                    x, y = gens[0], gens[1]
                    c1, c2, c3, cp1, cp2, c_pp = gens[2:]
                    return (-QQ(1)/QQ(4) * (x * y)**2 + x**3 + y**3 +
                            x**2 * c1 + y**2 * cp1 + QQ(1)/QQ(2) * x * y * c_pp +
                            x * c2 + y * cp2 - QQ(1)/QQ(4) * c_pp**2 + c3)
                elif rank == 8:
                    c_names = ['c1', 'c2', 'c3', 'c4', 'c5', 'cp1', 'cp2', 'c_pp']
                    ring_e = PolynomialRing(QQ, names=['x', 'y'] + c_names)
                    gens = ring_e.gens()
                    x, y = gens[0], gens[1]
                    c1, c2, c3, c4, c5, cp1, cp2, c_pp = gens[2:]
                    return (x**5 + x**4 * c1 - QQ(1)/QQ(4) * (x * y)**2 +
                            x**3 * c2 + y**3 + x**2 * c3 + y**2 * cp1 +
                            QQ(1)/QQ(2) * x * y * c_pp + x * c4 + y * cp2 -
                            QQ(1)/QQ(4) * c_pp**2 + c5)

            return self.defining_polynomial()

        def dynkin_diagram_data(self) -> dict[str, object]:
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

        def interior_integral_points(self) -> tuple[LatticePoint2D, ...]:
            poly = self.polyhedron()
            int_pts = [pt for pt in poly.integral_points() if all(h.eval(pt) > 0 for h in poly.Hrepresentation())]
            return tuple(self._lattice([p[0], p[1]]) for p in int_pts)

        def boundary_integral_points(self) -> tuple[LatticePoint2D, ...]:
            poly = self.polyhedron()
            all_pts = set(tuple(p) for p in poly.integral_points())
            int_pts = set(tuple(p) for p in self.interior_integral_points())
            bnd = sorted(all_pts - int_pts)
            return tuple(self._lattice([p[0], p[1]]) for p in bnd)

        def distinguished_boundary_points(self) -> tuple[LatticePoint2D, ...]:
            blue_facets = self._blue_facets()
            pts: set[tuple[LatticeCoord, ...]] = set()
            for f in blue_facets:
                for pt in f.as_polyhedron().integral_points():
                    pts.add(tuple(pt))
            return tuple(self._lattice([p[0], p[1]]) for p in sorted(pts))

        def n_integral_points(self) -> int:
            return len(self.polyhedron().integral_points())

        def n_interior_points(self) -> int:
            return len(self.interior_integral_points())

        def n_boundary_points(self) -> int:
            return self.n_integral_points() - self.n_interior_points()

        def plot(self, **kwds: object) -> object:
            return self.cover_polytope().plot3d(**kwds)

        def plot3d(self, **kwds: object) -> object:
            return self.cover_polytope().plot3d(**kwds)

        def plot2d(self, **kwds: object) -> Graphics:
            """2D polygon plot of Q."""
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

            for gx in range(min_x, max_x + 1):
                g_plot += line([(gx, min_y), (gx, max_y)],
                               color=grid_line_color, thickness=grid_line_width,
                               linestyle=':', zorder=1)
            for gy in range(min_y, max_y + 1):
                g_plot += line([(min_x, gy), (max_x, gy)],
                               color=grid_line_color, thickness=grid_line_width,
                               linestyle=':', zorder=1)

            all_grid = [(gx, gy) for gx in range(min_x, max_x + 1)
                        for gy in range(min_y, max_y + 1)]
            int_pts = set(tuple(p) for p in self.interior_integral_points())
            bnd_pts = set(tuple(p) for p in self.boundary_integral_points())
            dist_pts = set(tuple(p) for p in self.distinguished_boundary_points())
            amb_pts = [pt for pt in all_grid if pt not in int_pts and pt not in bnd_pts]

            g_plot += point(amb_pts, pointsize=24, color='#94A3B8', alpha=0.5, zorder=2)
            g_plot += polygon(vertices, color=fill_color, alpha=fill_alpha, zorder=3)

            blue_facets = self._blue_facets()
            for f in poly.facets():
                v_facet = [tuple(v) for v in f.vertices()]
                if len(v_facet) >= 2:
                    p1, p2 = v_facet[0], v_facet[1]
                    if f in blue_facets:
                        g_plot += line([p1, p2], color=blue_line_color, thickness=blue_line_width, zorder=6)
                    else:
                        g_plot += line([p1, p2], color=boundary_color, thickness=boundary_width, zorder=4)

            if int_pts:
                g_plot += point(list(int_pts), pointsize=44, color='#059669', zorder=8)

            other_bnd = [p for p in bnd_pts if p not in dist_pts]
            if other_bnd:
                g_plot += point(other_bnd, pointsize=48, color='#0F172A', zorder=9)

            if dist_pts:
                g_plot += point(list(dist_pts), pointsize=55, color=blue_line_color, zorder=10)

            for deco in sides.values():
                if deco.vertex_color == 'white':
                    for vi in deco.edge:
                        v_coord = vertices[vi]
                        g_plot += point(v_coord, pointsize=52, color='black', zorder=11)
                        g_plot += point(v_coord, pointsize=30, color='white', zorder=12)

            g_plot += point(p_star, pointsize=p_star_size, color=p_star_color, marker='*', zorder=15)

            center_x = sum(p[0] for p in vertices) / len(vertices)
            center_y = sum(p[1] for p in vertices) / len(vertices)

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
            g_plot += text(fr'${label}$', (float(center_x), float(center_y + label_y_offset)),
                           fontsize=label_fontsize, color='black', fontweight='bold', zorder=16)

            show_axes = kwds.get('axes', False)
            x_ticks = list(range(min_x, max_x + 1))
            y_ticks = list(range(min_y, max_y + 1))
            g_plot.axes(show_axes)
            g_plot.set_axes_range(min_x - 0.2, max_x + 0.2, min_y - 0.2, max_y + 0.2)
            g_plot.SHOW_OPTIONS['ticks'] = [x_ticks, y_ticks]
            g_plot.SHOW_OPTIONS['ticks_integer'] = True

            return g_plot

        def _latex_(self) -> str:
            from sage.misc.latex import latex as _latex
            f0_latex = _latex(self.defining_polynomial())
            amb_ident = self.ambient_identification_latex()
            delta_x_latex = self.log_divisor()._latex_()
            eol = "\\\\"

            if self.is_affine():
                norm_vol = 2 * self.volume()
                vol_val = self.volume()
                inv_line = rf"&\operatorname{{Vol}}_\mathbb{{Z}}(Q) = {norm_vol},\; \operatorname{{Vol}}(Q) = {vol_val},\; |Q \cap \mathbb{{Z}}^2| = {self.n_integral_points()},\; |\operatorname{{Int}}(Q)| = {self.n_interior_points()}"
            else:
                P = self.cover_polytope()
                vol_z = P.normalized_volume()
                vol_val = P.volume()
                dim_p = self.ambient_dimension()
                if dim_p in (2, 3):
                    inv_line = rf"&\operatorname{{Vol}}_\mathbb{{Z}}(P) = {vol_z},\; \operatorname{{Vol}}(P) = {vol_val},\; |P \cap \mathbb{{Z}}^3| = {P.n_integral_points()},\; |\operatorname{{Int}}(P)| = {P.n_interior_points()}"
                else:
                    mat_lat = _latex(self.polytope_matrix())
                    inv_line = rf"&P = \operatorname{{conv}}\left({mat_lat}\right) \colon \operatorname{{Vol}}_\mathbb{{Z}}(P) = {vol_z},\; \operatorname{{Vol}}(P) = {vol_val},\; |P \cap \mathbb{{Z}}^{{{dim_p}}}| = {P.n_integral_points()},\; |\operatorname{{Int}}(P)| = {P.n_interior_points()}"

            lines = [
                r"\begin{aligned}",
                rf"&(X, D + \varepsilon R) \colon X = \mathrm{{V}}\left(z^2 + \left({f0_latex}\right)\right) \subset {amb_ident} \text{{ of type }} {self._latex_label} {eol}",
                rf"&D + \varepsilon R = {delta_x_latex} {eol}",
                inv_line,
                r"\end{aligned}",
            ]
            return "\n".join(lines)

        def __repr__(self) -> str:
            amb = self.ambient_identification()
            f0 = self.defining_polynomial()
            delta_x = repr(self.log_divisor())
            return f"Log Pair (X, D + eps*R) where X = V(z^2 + ({f0})) ⊂ {amb} of type {self._key} (D + eps*R = {delta_x})"

        def _repr_html_(self) -> Optional[str]:
            try:
                from dzack_research.preamble.categories.schemes.threejs_viewer import generate_threejs_polytope_html
                P = self.cover_polytope()
                poly = P.polyhedron()
                verts = [list(v) for v in poly.vertices()]
                facets = [[verts.index(list(v)) for v in f.vertices()] for f in poly.facets()]
                int_pts = [list(p) for p in P.interior_integral_points()]
                bnd_pts = [list(p) for p in P.boundary_integral_points()]
                p_star_3d = [self.p_star()[0], self.p_star()[1], 2]
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


def ToricLogPair(
    variety: ToricVariety_field, divisor: Optional[object] = None
) -> Parent:
    r"""Return the toric log pair (V, Δ_toric) of ``variety``."""
    return object_of(ToricLogPairs(), variety=variety, divisor=divisor)


def ADEBaseSurface(cover: Parent) -> Parent:
    r"""Return the base del Pezzo log pair (Y = V_Q, C) of ``cover``."""
    return object_of(ADEBaseSurfaces(), cover=cover)


def ADESurface(
    letter: str,
    rank: int,
    variant: tuple[str, ...] = (),
    affine: bool = False,
    n: Optional[int] = None,
) -> Parent:
    r"""Return the ADE surface log pair (X, D + eps*R) of a Dynkin type."""
    return object_of(
        ADESurfaces(),
        letter=letter,
        rank=rank,
        variant=variant,
        affine=affine,
        n=n,
    )
