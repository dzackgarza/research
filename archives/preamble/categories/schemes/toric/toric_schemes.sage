r"""Category subtree for toric schemes and toric varieties.

Hierarchy:
  Schemes(S)
    └── Varieties(S)
          └── ToricSchemes(S) ──────────────> V_P, V_Q

An equation-defined closed subscheme of a toric scheme belongs to
``EquationDefinedClosedSubschemes(S)``. It is not toric in general.
"""

from typing import Self, TYPE_CHECKING
from sage.categories.category import Category
from sage.structure.parent import Parent
from sage.rings.rational_field import QQ as SageQQ
from sage.rings.integer_ring import ZZ as SageZZ
from sage.matrix.constructor import matrix
from sage.modules.free_module_element import vector
from sage.schemes.toric.variety import ToricVariety_field, ToricVariety as NativeToricVariety
from sage.geometry.fan import RationalPolyhedralFan

from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.varieties import Varieties
from dzack_research.preamble.categories.schemes.polytopes import ConvexPolytopes

if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.categories.rings import Ring
    from dzack_research.preamble.lexicon import RingElement
    from dzack_research.preamble.owned_category import ConstructionData


class ToricSchemes(OwnedCategoryOverBaseRing):
    r"""Category of toric schemes / varieties over a base scheme or ring S."""

    def _repr_object_names(self) -> str:
        return f"toric schemes over {self.base_ring()}"

    def super_categories(self) -> list[Category]:
        r"""Return [Varieties(S)]."""
        return [Varieties(self.base_ring())]

    class ParentMethods:
        r"""Parent methods for objects in ToricSchemes(S).

        A toric scheme V is defined by a rational fan Σ or a lattice polytope P.
        """

        def __init__(
            self: Self,
            polytope_or_fan: Parent | RationalPolyhedralFan,
            dim: int | None = None,
            identification: str | None = None,
            **rest: "ConstructionData",
        ) -> None:
            r"""Build the toric scheme of a polytope or a fan."""
            if isinstance(polytope_or_fan, Parent) and polytope_or_fan in ConvexPolytopes():
                self._polytope = polytope_or_fan
                self._dim = int(polytope_or_fan.dimension()) if dim is None else int(dim)
                self._fan = polytope_or_fan.normal_fan()
            else:
                assert isinstance(polytope_or_fan, RationalPolyhedralFan)
                self._fan = polytope_or_fan
                self._polytope = None
                self._dim = int(polytope_or_fan.dim()) if dim is None else int(dim)

            self._identification_latex = None
            self._identification = identification or self._identify_toric_scheme()
            self._native_variety = None
            super().__init__(**rest)

        def is_toric(self) -> bool:
            r"""Return True: every object in ToricSchemes(S) is a toric scheme."""
            return True

        def fan(self) -> RationalPolyhedralFan:
            r"""Return the rational polyhedral fan Σ."""
            return self._fan

        def polytope(self) -> Parent | None:
            r"""Return the polarizing integral lattice polytope P."""
            return self._polytope

        def dimension(self) -> int:
            r"""Return the algebraic dimension of the toric scheme."""
            return self._dim

        def subscheme(
            self,
            *equations: "RingElement",
            dim: int | None = None,
        ) -> Parent:
            r"""Construct the closed subscheme cut out by equations."""
            from dzack_research.preamble.categories.schemes.subschemes import (
                EquationDefinedClosedSubscheme,
            )

            eq_list = equations[0] if (len(equations) == 1 and isinstance(equations[0], (list, tuple))) else list(equations)
            return EquationDefinedClosedSubscheme(
                self,
                equations=eq_list,
                dimension=dim,
            )

        def standard_identification(self) -> str:
            r"""Return geometric identification string (e.g. PP^2, PP^1 x PP^1, PP(w_i), V_P, V_Q)."""
            return self._identification

        def standard_identification_latex(self) -> str:
            r"""Return LaTeX formatted identification."""
            if self._identification_latex:
                return self._identification_latex
            ident = self._identification
            if ident == "P^2" or ident == "PP^2":
                return r"\mathbb{P}^2"
            if ident == "P^3" or ident == "PP^3":
                return r"\mathbb{P}^3"
            if ident == "P^1 x P^1" or ident == "PP^1 x PP^1":
                return r"\mathbb{P}^1 \times \mathbb{P}^1"
            if ident.startswith("P(") or ident.startswith("PP("):
                _, _, weights_and_closing_parenthesis = ident.partition("(")
                weights, _, _ = weights_and_closing_parenthesis.partition(")")
                return rf"\mathbb{{P}}({weights})"
            return rf"{ident}"

        def _identify_toric_scheme(self) -> str:
            r"""Compute standard geometric identification from fan rays or polytope shape."""
            ident_str, ident_latex = self._classify_fan_or_poly()
            self._identification_latex = ident_latex
            return ident_str

        def _classify_fan_or_poly(self) -> tuple[str, str]:
            r"""Classify the toric variety from its normal fan or polytope."""
            fan = self._fan
            assert fan is not None
            rays = [vector(SageZZ, [int(c) for c in r]) for r in fan.rays()]

            n_rays = len(rays)
            d = self._dim

            if d == 2:
                if n_rays == 3:
                    M = matrix(SageZZ, [list(r) for r in rays]).transpose()
                    ker = M.right_kernel().basis()
                    if ker:
                        v = ker[0]
                        w = sorted([abs(int(c)) for c in v])
                        if w == [1, 1, 1]:
                            return "PP^2", r"\mathbb{P}^2"
                        return f"PP({w[0]},{w[1]},{w[2]})", rf"\mathbb{{P}}({w[0]},{w[1]},{w[2]})"
                elif n_rays == 4:
                    pts = set((int(r[0]), int(r[1])) for r in rays)
                    if pts == {(1,0), (0,1), (-1,0), (0,-1)}:
                        return "PP^1 x PP^1", r"\mathbb{P}^1 \times \mathbb{P}^1"
                    if pts in ({(1,0), (0,1), (-1,0), (1,-2)}, {(1,0), (-1,2), (-1,0), (0,-1)}):
                        return "FF_2", r"\mathbb{F}_2"
                    if pts in ({(1,0), (0,-1), (-1,-1), (0,1)}, {(1,0), (0,1), (-1,-1), (0,-1)}):
                        return "FF_1", r"\mathbb{F}_1"
                    if pts in ({(1,0), (-1,-2), (-2,-1), (0,1)}, {(1,0), (-1,-2), (-1,-1), (0,1)}, {(1,0), (0,-1), (-2,-1), (0,1)}):
                        return "Bl_1(PP(1,1,2))", r"\operatorname{Bl}_1(\mathbb{P}(1,1,2))"
                    if pts == {(1,0), (-1,-2), (-2,-3), (0,1)}:
                        return "Bl_1(PP(1,2,3))", r"\operatorname{Bl}_1(\mathbb{P}(1,2,3))"
                    return "ToricSurface(4-rays)", r"V_Q"
                return f"ToricSurface({n_rays}-rays)", r"V_Q"

            elif d == 3:
                if n_rays == 4:
                    M = matrix(SageZZ, [list(r) for r in rays]).transpose()
                    ker = M.right_kernel().basis()
                    if ker:
                        v = ker[0]
                        w = sorted([abs(int(c)) for c in v])
                        if w == [1, 1, 1, 1]:
                            return "PP^3", r"\mathbb{P}^3"
                        return f"PP({w[0]},{w[1]},{w[2]},{w[3]})", rf"\mathbb{{P}}({w[0]},{w[1]},{w[2]},{w[3]})"
                elif n_rays == 5:
                    # 3D pyramid over a 2D quadrangle: projective cone / anticanonical bundle
                    side_rays = [vector(SageZZ, [r[0], r[1]]) for r in rays if not (r[0] == 0 and r[1] == 0)]
                    pts = set((int(r[0]), int(r[1])) for r in side_rays)
                    if pts == {(1,0), (0,1), (-1,0), (0,-1)}:
                        base_id, base_latex = "PP^1 x PP^1", r"\mathbb{P}^1 \times \mathbb{P}^1"
                    elif pts in ({(1,0), (0,1), (-1,0), (1,-2)}, {(1,0), (-1,2), (-1,0), (0,-1)}):
                        base_id, base_latex = "FF_2", r"\mathbb{F}_2"
                    elif pts in ({(1,0), (0,-1), (-1,-1), (0,1)}, {(1,0), (0,1), (-1,-1), (0,-1)}):
                        base_id, base_latex = "FF_1", r"\mathbb{F}_1"
                    elif pts in ({(1,0), (-1,-2), (-2,-1), (0,1)}, {(1,0), (-1,-2), (-1,-1), (0,1)}, {(1,0), (0,-1), (-2,-1), (0,1)}):
                        base_id, base_latex = "Bl_1(PP(1,1,2))", r"\operatorname{Bl}_1(\mathbb{P}(1,1,2))"
                    elif pts == {(1,0), (-1,-2), (-2,-3), (0,1)}:
                        base_id, base_latex = "Bl_1(PP(1,2,3))", r"\operatorname{Bl}_1(\mathbb{P}(1,2,3))"
                    else:
                        base_id, base_latex = "Y", r"Y"
                    return f"Cone_P(1,2)({base_id})", rf"\mathbb{{P}}_{{{base_latex}}}(\mathcal{{O}} \oplus \mathcal{{O}}(-K))"
                return f"ToricThreefold({n_rays}-rays)", r"V_P"

            return f"ToricVariety(dim={d})", rf"V_P \subset \mathbb{{R}}^{{{d}}}"

        def to_native_toric_variety(self) -> ToricVariety_field:
            r"""Construct or return the native Sage ToricVariety."""
            if self._native_variety is None:
                if self._fan is not None:
                    self._native_variety = NativeToricVariety(self._fan)
                elif self._polytope is not None:
                    fan = self._polytope.normal_fan()
                    self._native_variety = NativeToricVariety(fan)
            return self._native_variety

def ToricScheme(
    polytope_or_fan: Parent | RationalPolyhedralFan,
    dim: int | None = None,
    identification: str | None = None,
    base_ring: "Ring" = SageQQ,
) -> Parent:
    r"""Return the toric scheme V of a lattice polytope P or a rational fan Σ."""
    return object_of(
        ToricSchemes(base_ring),
        polytope_or_fan=polytope_or_fan,
        dim=dim,
        identification=identification,
        base_ring=base_ring,
    )
