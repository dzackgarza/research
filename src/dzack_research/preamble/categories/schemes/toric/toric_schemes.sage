r"""Category subtree for toric schemes, ambient toric varieties, and toric subobjects.

Hierarchy:
  Schemes(S)
    ├── Varieties(S)
    │     └── ToricSchemes(S) ──────────────> V_P, V_Q
    └── ToricSubschemes(S) ─────────────────> X ⊂ V_P, Y = V_Q
"""

from typing import Any, Optional, Self, Sequence, TYPE_CHECKING
from sage.categories.category import Category
from sage.structure.parent import Parent
from sage.rings.rational_field import QQ as SageQQ
from sage.rings.integer_ring import ZZ as SageZZ
from sage.matrix.constructor import matrix
from sage.modules.free_module_element import vector
from sage.structure.sage_object import SageObject
from sage.misc.latex import latex
from sage.schemes.toric.variety import ToricVariety_field, ToricVariety as NativeToricVariety

from dzack_research.preamble.lexicon import Polyhedron
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.varieties import Varieties

if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from dzack_research.preamble.owned_category import ConstructionData


class FormalDivisor(SageObject):
    r"""
    A formal linear combination of subschemes / prime divisors with coefficients
    in QQ or the rational polynomial ring QQ[eps] / field of fractions.
    """
    _terms: list[tuple[Any, Any]]
    _ambient: Optional[Any]

    def __init__(self, terms: Sequence[tuple[Any, Any]], ambient: Optional[Any] = None) -> None:
        self._terms = list(terms)
        self._ambient = ambient

    def terms(self) -> list[tuple[Any, Any]]:
        return list(self._terms)

    def components(self) -> list[Any]:
        return [sub for _, sub in self._terms]

    def coefficients(self) -> list[Any]:
        return [coeff for coeff, _ in self._terms]

    def ambient_space(self) -> Optional[Any]:
        return self._ambient

    def __len__(self) -> int:
        return len(self._terms)

    def __getitem__(self, idx: int) -> tuple[Any, Any]:
        return self._terms[idx]

    def __iter__(self) -> Any:
        return iter(self._terms)

    def __add__(self, other: Any) -> "FormalDivisor":
        if isinstance(other, FormalDivisor):
            return FormalDivisor(self._terms + other._terms, ambient=self._ambient or other._ambient)
        raise TypeError(f"Cannot add FormalDivisor and {type(other)}")

    def _latex_(self) -> str:
        pieces = []
        for coeff, sub in self._terms:
            if hasattr(sub, 'equations') and sub.equations():
                eqs_lat = r",\, ".join(latex(eq) for eq in sub.equations())
                sub_lat = rf"\mathrm{{V}}\left({eqs_lat}\right)"
            elif hasattr(sub, '_latex_'):
                sub_lat = sub._latex_()
            else:
                sub_lat = str(latex(sub))

            if coeff == 1:
                pieces.append(sub_lat)
            elif coeff == -1:
                pieces.append(f"- {sub_lat}")
            elif coeff in ('eps', r'\varepsilon', 'e'):
                pieces.append(rf"\varepsilon\, {sub_lat}")
            elif coeff in ('1/2(1+eps)', r'\tfrac{1+\varepsilon}{2}', '(1+eps)/2'):
                pieces.append(rf"\tfrac{{1+\varepsilon}}{{2}}\, {sub_lat}")
            else:
                c_lat = latex(coeff)
                pieces.append(rf"{c_lat}\, {sub_lat}")
        return " + ".join(pieces).replace("+ -", "- ")

    def __repr__(self) -> str:
        pieces = []
        for coeff, sub in self._terms:
            if hasattr(sub, 'equations'):
                eqs = ", ".join(str(eq) for eq in sub.equations())
                sub_str = f"V({eqs})"
            else:
                sub_str = str(sub)

            if coeff == 1:
                pieces.append(sub_str)
            elif coeff == -1:
                pieces.append(f"-{sub_str}")
            elif coeff in ('eps', r'\varepsilon', 'e'):
                pieces.append(f"eps*{sub_str}")
            elif coeff in ('1/2(1+eps)', r'\tfrac{1+\varepsilon}{2}', '(1+eps)/2'):
                pieces.append(f"1/2(1+eps)*{sub_str}")
            else:
                pieces.append(f"{coeff}*{sub_str}")
        return " + ".join(pieces).replace("+ -", "- ")


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
            polytope_or_fan: Any,
            dim: Optional[int] = None,
            identification: Optional[str] = None,
            **rest: "ConstructionData",
        ) -> None:
            r"""Build the toric scheme of a polytope or a fan."""
            if isinstance(polytope_or_fan, Polyhedron) or hasattr(polytope_or_fan, 'vertices'):
                self._polytope = polytope_or_fan
                self._dim = int(polytope_or_fan.dimension()) if dim is None else int(dim)
                self._fan = getattr(polytope_or_fan, 'normal_fan', lambda: None)()
            else:
                self._fan = polytope_or_fan
                self._polytope = None
                self._dim = int(polytope_or_fan.dimension()) if (polytope_or_fan and hasattr(polytope_or_fan, 'dimension')) else (dim or 2)

            self._identification = identification or self._identify_ambient()
            self._native_variety = None
            super().__init__(**rest)

        def is_toric(self) -> bool:
            r"""Return True: every object in ToricSchemes(S) is a toric scheme."""
            return True

        def fan(self) -> Any:
            r"""Return the rational polyhedral fan Σ."""
            return self._fan

        def normal_fan(self) -> Any:
            r"""Return the normal fan of the polarizing polytope."""
            return self._fan

        def polytope(self) -> Any:
            r"""Return the polarizing integral lattice polytope P."""
            return self._polytope

        def polyhedron(self) -> Any:
            r"""Alias for polytope()."""
            return self._polytope

        def dimension(self) -> int:
            r"""Return the algebraic dimension of the toric scheme."""
            return self._dim

        def subscheme(self, *equations: Any, dim: Optional[int] = None) -> Parent:
            r"""Construct a toric subscheme X ↪ V cut out by equations."""
            eq_list = equations[0] if (len(equations) == 1 and isinstance(equations[0], (list, tuple))) else list(equations)
            return ToricSubscheme(ambient=self, equations=eq_list, dim=dim, base_ring=self.base_ring())

        def ambient_identification(self) -> str:
            r"""Return geometric identification string (e.g. PP^2, PP^1 x PP^1, PP(w_i), V_P, V_Q)."""
            return self._identification

        def ambient_identification_latex(self) -> str:
            r"""Return LaTeX formatted identification."""
            if hasattr(self, '_identification_latex') and self._identification_latex:
                return self._identification_latex
            ident = self._identification
            if ident == "P^2" or ident == "PP^2":
                return r"\mathbb{P}^2"
            if ident == "P^3" or ident == "PP^3":
                return r"\mathbb{P}^3"
            if ident == "P^1 x P^1" or ident == "PP^1 x PP^1":
                return r"\mathbb{P}^1 \times \mathbb{P}^1"
            if ident.startswith("P(") or ident.startswith("PP("):
                weights = ident[ident.index("(") + 1 : ident.index(")")]
                return rf"\mathbb{{P}}({weights})"
            return rf"{ident}"

        def _identify_ambient(self) -> str:
            r"""Compute standard geometric identification from fan rays or polytope shape."""
            ident_str, ident_latex = self._classify_fan_or_poly()
            self._identification_latex = ident_latex
            return ident_str

        def _classify_fan_or_poly(self) -> tuple[str, str]:
            r"""Classify the toric variety from its normal fan or polytope."""
            fan = self._fan
            poly = self._polytope
            if fan is None and poly is not None and hasattr(poly, 'normal_fan'):
                try:
                    fan = poly.normal_fan()
                except Exception:
                    pass

            if fan is None:
                d = self._dim
                return f"V_P(dim={d})", rf"V_P \subset \mathbb{{R}}^{{{d}}}"

            try:
                rays = [vector(SageZZ, [int(c) for c in r]) for r in fan.rays()]
            except Exception:
                return r"V(\Sigma)", r"V(\Sigma)"

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


class ToricSubschemes(OwnedCategoryOverBaseRing):
    r"""Category of subschemes X ↪ V of a toric scheme V."""

    def _repr_object_names(self) -> str:
        return f"toric subschemes over {self.base_ring()}"

    def super_categories(self) -> list[Category]:
        r"""Return [Schemes(S)]."""
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.schemes.schemes import Schemes

        return [Schemes(self.base_ring())]

    class ParentMethods:
        r"""Parent methods for a subscheme X ↪ V of a toric scheme V.

        The data this level adds are the toric scheme V that X sits in and the
        family of equations cutting X out of it, together with the dimension
        of X.  Everything else is read off V: its polytope P, its
        identification string, and the invariants of P.
        """

        def __init__(
            self: Self,
            ambient: Parent,
            equations: Sequence[Any] = (),
            dim: Optional[int] = None,
            **rest: "ConstructionData",
        ) -> None:
            r"""Build the subscheme of ``ambient`` cut out by ``equations``."""
            self._ambient = ambient
            self._equations = tuple(equations)
            if dim is not None:
                self._dim = int(dim)
            else:
                amb_dim = ambient.dimension() if hasattr(ambient, 'dimension') else 2
                codim = len(self._equations) if self._equations and self._equations != (0,) else 0
                self._dim = max(0, amb_dim - codim)
            super().__init__(**rest)

        def ambient_scheme(self) -> Parent:
            r"""Return the toric scheme V of which X is a subscheme."""
            return self._ambient

        def inclusion_morphism(self) -> "Morphism":
            r"""Return the structure inclusion morphism i: X -> V."""
            assert False, (
                "inclusion_morphism is not yet built for a toric subscheme"
            )

        def ambient_space(self) -> Parent:
            r"""Return the toric scheme V that X sits in."""
            return self.ambient_scheme()

        def ambient_toric_variety(self) -> Parent:
            r"""Alias for ambient_space()."""
            return self.ambient_scheme()

        def equations(self) -> tuple[Any, ...]:
            r"""Return the tuple of defining equations cutting out X in V."""
            return self._equations

        def defining_equations(self) -> tuple[Any, ...]:
            r"""Alias for equations()."""
            return self._equations

        def defining_polynomial(self) -> Any:
            r"""Return the principal defining polynomial for hypersurfaces (or 0 for ambient)."""
            if self._equations:
                return self._equations[0]
            return 0

        def dimension(self) -> int:
            r"""Return the algebraic dimension of the subscheme X."""
            return self._dim

        def ambient_dimension(self) -> int:
            r"""Return the dimension of the toric scheme V."""
            ambient = self.ambient_scheme()
            if hasattr(ambient, 'dimension'):
                return int(ambient.dimension())
            return self._dim

        def codimension(self) -> int:
            r"""Return the codimension of X in V: dim(V) - dim(X)."""
            return self.ambient_dimension() - self.dimension()

        def is_hypersurface(self) -> bool:
            r"""Return True if X is a hypersurface in V (codimension 1)."""
            return self.codimension() == 1

        def is_ambient(self) -> bool:
            r"""Return True if X is the whole of V (codimension 0)."""
            return self.codimension() == 0

        def ambient_polytope(self) -> Any:
            r"""Return the lattice polytope P of the toric scheme V."""
            ambient = self.ambient_scheme()
            if hasattr(ambient, 'polytope'):
                return ambient.polytope()
            if hasattr(ambient, 'polyhedron'):
                return ambient.polyhedron()
            return None

        def polytope(self) -> Any:
            r"""Alias for ambient_polytope()."""
            return self.ambient_polytope()

        def ambient_identification(self) -> str:
            r"""Return the geometric identification string for V."""
            ambient = self.ambient_scheme()
            if hasattr(ambient, 'ambient_identification'):
                return ambient.ambient_identification()
            return f"V_{{P}} \\subset \\mathbb{{R}}^{{{self.ambient_dimension()}}}"

        def ambient_identification_latex(self) -> str:
            r"""Return the LaTeX representation of the identification of V."""
            ambient = self.ambient_scheme()
            if hasattr(ambient, 'ambient_identification_latex'):
                return ambient.ambient_identification_latex()
            return self.ambient_identification()

        def _repr_(self) -> str:
            if not self._equations or self._equations == (0,):
                return f"{self.ambient_identification()}"
            eqs_str = ", ".join(str(eq) for eq in self._equations)
            return f"V({eqs_str}) ⊂ {self.ambient_identification()}"

        def _latex_(self) -> str:
            if not self._equations or self._equations == (0,):
                return self.ambient_identification_latex()
            eqs_lat = r",\, ".join(latex(eq) for eq in self._equations)
            return rf"\mathrm{{V}}\left({eqs_lat}\right) \subset {self.ambient_identification_latex()}"


def ToricScheme(
    polytope_or_fan: Any,
    dim: Optional[int] = None,
    identification: Optional[str] = None,
    base_ring: Any = SageQQ,
) -> Parent:
    r"""Return the toric scheme V of a lattice polytope P or a rational fan Σ."""
    return object_of(
        ToricSchemes(base_ring),
        polytope_or_fan=polytope_or_fan,
        dim=dim,
        identification=identification,
        base_ring=base_ring,
    )


def ToricSubscheme(
    ambient: Parent,
    equations: Sequence[Any] = (),
    dim: Optional[int] = None,
    base_ring: Any = SageQQ,
) -> Parent:
    r"""Return the subscheme X ↪ V cut out of the toric scheme ``ambient``."""
    return object_of(
        ToricSubschemes(base_ring),
        ambient=ambient,
        equations=equations,
        dim=dim,
        base_ring=base_ring,
    )
