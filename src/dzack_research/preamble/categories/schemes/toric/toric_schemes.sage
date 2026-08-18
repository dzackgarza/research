r"""Category subtree for toric schemes, ambient toric varieties, and toric subobjects.

Hierarchy:
  Schemes(S)
    └── Varieties(S)
          └── ToricSchemes(S) ─────────────> ToricScheme (V_P, V_Q)
                └── .Subobject ────────────> ToricSubscheme (X ⊂ V_P, Y = V_Q)
"""

from typing import Any, Callable, Optional, Sequence, TYPE_CHECKING
from sage.categories.category import Category
from sage.structure.parent import Parent
from sage.categories.morphism import Morphism
from sage.rings.rational_field import QQ as SageQQ
from sage.rings.integer_ring import ZZ as SageZZ
from sage.matrix.constructor import matrix
from sage.geometry.polyhedron.constructor import Polyhedron
from sage.geometry.polyhedron.base import Polyhedron_base
from sage.schemes.toric.variety import ToricVariety_field, ToricVariety as NativeToricVariety

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.schemes import SchemeElement, Schemes
from dzack_research.preamble.categories.schemes.varieties import Varieties, Variety
from dzack_research.preamble.categories.schemes.subschemes import Subscheme
from dzack_research.preamble.refine import refine


class ToricSchemes(OwnedCategoryOverBaseRing):
    r"""Category of toric schemes / varieties over a base scheme or ring S."""

    def _repr_object_names(self) -> str:
        return f"toric schemes over {self.base_ring()}"

    def super_categories(self) -> list[Category]:
        r"""Return [Varieties(S)]."""
        return [Varieties(self.base_ring())]

    class ParentMethods:
        r"""Parent methods for objects in ToricSchemes(S)."""

        def is_toric(self) -> bool:
            r"""Return True: every object in ToricSchemes(S) is a toric scheme."""
            return True


class ToricSubscheme(Subscheme):
    r"""
    A subscheme X ↪ V of an ambient toric scheme V.

    Carries:
    - The ambient toric scheme V (accessed via .ambient_space() or .ambient_toric_variety())
    - The defining equations cutting out X in V (accessed via .equations() or .defining_equations())
    - The ambient polytope P associated with V (accessed via .ambient_polytope() or .polytope())
    - The ambient variety identification string (e.g. PP^2, PP^3, PP(w_i), V_P, V_Q)
    - Integral polytope invariants (Vol_ZZ, |P ∩ ZZ^n|, |Int(P) ∩ ZZ^n|)
    """
    _ambient_toric: "ToricScheme"
    _equations: tuple[Any, ...]
    _dim: int

    def __init__(
        self,
        ambient: "ToricScheme",
        equations: Sequence[Any] = (),
        dim: Optional[int] = None,
        base_ring: Any = SageQQ,
    ) -> None:
        Subscheme.__init__(self, ambient=ambient, base_ring=base_ring)
        self._ambient_toric = ambient
        self._equations = tuple(equations)
        if dim is not None:
            self._dim = int(dim)
        else:
            amb_dim = ambient.dimension() if hasattr(ambient, 'dimension') else 2
            codim = len(self._equations) if self._equations and self._equations != (0,) else 0
            self._dim = max(0, amb_dim - codim)

    def ambient_space(self) -> "ToricScheme":
        r"""Return the ambient toric scheme V."""
        return self._ambient_toric

    def ambient_toric_variety(self) -> "ToricScheme":
        r"""Alias for ambient_space()."""
        return self._ambient_toric

    def ambient_scheme(self) -> "ToricScheme":
        r"""Alias for ambient_space()."""
        return self._ambient_toric

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
        r"""Return the dimension of the ambient toric variety V."""
        if hasattr(self._ambient_toric, 'dimension'):
            return int(self._ambient_toric.dimension())
        return self._dim

    def codimension(self) -> int:
        r"""Return the codimension of X in ambient V: dim(V) - dim(X)."""
        return self.ambient_dimension() - self.dimension()

    def is_hypersurface(self) -> bool:
        r"""Return True if X is a hypersurface in ambient V (codimension 1)."""
        return self.codimension() == 1

    def is_ambient(self) -> bool:
        r"""Return True if X is the entire ambient toric variety V (codimension 0)."""
        return self.codimension() == 0

    def ambient_polytope(self) -> Any:
        r"""Return the lattice polytope P of the ambient toric variety V."""
        if hasattr(self._ambient_toric, 'polytope'):
            return self._ambient_toric.polytope()
        if hasattr(self._ambient_toric, 'polyhedron'):
            return self._ambient_toric.polyhedron()
        return None

    def polytope(self) -> Any:
        r"""Alias for ambient_polytope()."""
        return self.ambient_polytope()

    def ambient_identification(self) -> str:
        r"""Return the geometric identification string for the ambient toric variety."""
        if hasattr(self._ambient_toric, 'ambient_identification'):
            return self._ambient_toric.ambient_identification()
        return f"V_{{P}} \\subset \\mathbb{{R}}^{{{self.ambient_dimension()}}}"

    def ambient_identification_latex(self) -> str:
        r"""Return the LaTeX representation of the ambient toric variety identification."""
        if hasattr(self._ambient_toric, 'ambient_identification_latex'):
            return self._ambient_toric.ambient_identification_latex()
        return self.ambient_identification()


class ToricScheme(Variety):
    r"""
    A toric scheme / variety V defined by a rational fan Σ or lattice polytope P.
    """
    Subobject = ToricSubscheme

    _fan: Optional[Any]
    _polytope: Optional[Any]
    _dim: int
    _identification: str
    _native_variety: Optional[ToricVariety_field]

    def __init__(
        self,
        polytope_or_fan: Any,
        dim: Optional[int] = None,
        identification: Optional[str] = None,
        base_ring: Any = SageQQ,
    ) -> None:
        Variety.__init__(self, base_ring=base_ring)
        refine(self, ToricSchemes(base_ring))

        if isinstance(polytope_or_fan, Polyhedron_base) or hasattr(polytope_or_fan, 'vertices'):
            self._polytope = polytope_or_fan
            self._dim = int(polytope_or_fan.dimension()) if dim is None else int(dim)
            self._fan = getattr(polytope_or_fan, 'normal_fan', lambda: None)()
        else:
            self._fan = polytope_or_fan
            self._polytope = None
            self._dim = int(polytope_or_fan.dimension()) if (polytope_or_fan and hasattr(polytope_or_fan, 'dimension')) else (dim or 2)

        self._identification = identification or self._identify_ambient()
        self._native_variety = None

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

    def subscheme(self, *equations: Any, dim: Optional[int] = None) -> ToricSubscheme:
        r"""Construct a ToricSubscheme X ↪ V cut out by equations."""
        eq_list = equations[0] if (len(equations) == 1 and isinstance(equations[0], (list, tuple))) else list(equations)
        return ToricSubscheme(ambient=self, equations=eq_list, dim=dim, base_ring=self.base_ring())

    def ambient_identification(self) -> str:
        r"""Return geometric identification string (e.g. PP^2, PP^1 x PP^1, PP(w_i), V_P, V_Q)."""
        return self._identification

    def ambient_identification_latex(self) -> str:
        r"""Return LaTeX formatted identification."""
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
        return rf"V_{{{ident}}}" if not ident.startswith("V_") else rf"{ident}"

    def _identify_ambient(self) -> str:
        r"""Compute standard geometric identification from fan rays or polytope shape."""
        if self._polytope is not None:
            verts = [tuple(v) for v in self._polytope.vertices()]
            d = self._dim
            if d == 2:
                # Standard P^2 simplices: conv((0,0), (k, 0), (0, k))
                v_set = set(verts)
                for k in range(1, 10):
                    if v_set == {(0, 0), (k, 0), (0, k)} or v_set == {(0, 0), (0, k), (k, 0)}:
                        return r"\mathbb{P}^2" if k == 1 else rf"\mathbb{{P}}^2 \text{{ (deg {k})}}"
                # P^1 x P^1 rectangles: [0, a] x [0, b]
                for a in range(1, 6):
                    for b in range(1, 6):
                        if v_set == {(0, 0), (a, 0), (0, b), (a, b)}:
                            return r"\mathbb{P}^1 \times \mathbb{P}^1"
                # Check 3 rays for weighted projective planes P(a, b, c)
                if self._fan is not None and hasattr(self._fan, 'rays'):
                    rays = list(self._fan.rays())
                    if len(rays) == 3:
                        # Find kernel vector
                        M = matrix(SageZZ, [[r[0], r[1]] for r in rays]).transpose()
                        ker = M.right_kernel().basis()
                        if ker:
                            w = ker[0]
                            if all(c > 0 for c in w):
                                return rf"\mathbb{{P}}({w[0]},{w[1]},{w[2]})"
                            if all(c < 0 for c in w):
                                return rf"\mathbb{{P}}({-w[0]},{-w[1]},{-w[2]})"
                return r"V_Q"
            elif d == 3:
                # 3D simplex: conv((0,0,0), (k,0,0), (0,k,0), (0,0,k))
                v_set = set(verts)
                for k in range(1, 6):
                    if v_set == {(0, 0, 0), (k, 0, 0), (0, k, 0), (0, 0, k)}:
                        return r"\mathbb{P}^3" if k == 1 else rf"\mathbb{{P}}^3 \text{{ (deg {k})}}"
                return r"V_P"
            else:
                return rf"V_P \subset \mathbb{{R}}^{{{d}}}"
        return rf"V(\Sigma) \subset \mathbb{{R}}^{self._dim}"

    def to_native_toric_variety(self) -> ToricVariety_field:
        r"""Construct or return the native Sage ToricVariety."""
        if self._native_variety is None:
            if self._fan is not None:
                self._native_variety = NativeToricVariety(self._fan)
            elif self._polytope is not None:
                fan = self._polytope.normal_fan()
                self._native_variety = NativeToricVariety(fan)
        return self._native_variety
