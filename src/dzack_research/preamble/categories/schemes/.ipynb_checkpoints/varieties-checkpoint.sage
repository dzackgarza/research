r"""Category subtree for algebraic varieties over S, curves, surfaces, and toric varieties shadowing native Sage types.

Hierarchy:
  Schemes(S)
    └── Varieties(S)
          ├── Curves(S)   (dim = 1)
          ├── Surfaces(S) (dim = 2)
          └── ToricVariety
"""

from typing import Any

from sage.categories.category_types import Category_over_base_ring
from sage.categories.category_with_axiom import (
    all_axioms,
    axiom,
)
import sage.schemes.curves.constructor as _sage_curve_const
import sage.schemes.toric.variety as _sage_toric
from sage.rings.integer_ring import ZZ

_NativeToricVariety = _sage_toric.ToricVariety
_NativeCurve = _sage_curve_const.Curve

# Register dimension and toric axioms in Sage's axiom registry if not already present
for _axiom_name in ("DimensionOne", "DimensionTwo", "Toric"):
    if _axiom_name not in all_axioms:
        all_axioms.add(_axiom_name)


# ---------------------------------------------------------------------------
# Varieties(S)
# ---------------------------------------------------------------------------


class Variety(Scheme):
    r"""An algebraic variety over S: an integral, separated scheme of finite type over S."""

    Element = SchemeElement

    def __init__(self, base_ring: Any = ZZ) -> None:
        r"""Initialize the variety and refine into Varieties(S)."""
        Scheme.__init__(self, base_ring=base_ring)
        refine(self, Varieties(base_ring))


class Varieties(Category_over_base_ring):
    r"""Category of algebraic varieties over S: integral, separated schemes of finite type over S."""

    def _repr_object_names(self) -> str:
        return f"varieties over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return Schemes(S)."""
        return [Schemes(self.base_ring())]

    class SubcategoryMethods:
        r"""Axiom subcategories on Varieties(S)."""

        DimensionOne = axiom("DimensionOne")
        DimensionTwo = axiom("DimensionTwo")
        Curve = axiom("DimensionOne")
        Surface = axiom("DimensionTwo")
        Toric = axiom("Toric")

    class ParentMethods:
        r"""Variety parent methods."""

        def function_field(self: Any) -> Any:
            r"""Return K(X), the function field of the variety."""
            raise NotImplementedError("function_field must be implemented by concrete Variety")

        def divisor_group(self: Any) -> Any:
            r"""Return Div(X), the divisor group of the variety."""
            raise NotImplementedError("divisor_group must be implemented by concrete Variety")

        def picard_group(self: Any) -> Any:
            r"""Return Pic(X), the Picard group of the variety."""
            raise NotImplementedError("picard_group must be implemented by concrete Variety")

    class ElementMethods:
        r"""Variety element methods."""

    class MorphismMethods:
        r"""Variety morphism methods."""


# ---------------------------------------------------------------------------
# ToricVarieties: Varieties(S)
# ---------------------------------------------------------------------------


def ToricVariety(*args: Any, **kwargs: Any) -> Any:
    r"""Construct a toric variety shadowing native Sage ToricVariety, placing it in Varieties(R)."""
    obj = _NativeToricVariety(*args, **kwargs)
    base_r = obj.base_ring() if hasattr(obj, "base_ring") else ZZ
    return refine(obj, Varieties(base_r))


# ---------------------------------------------------------------------------
# Curves(S): Dimension = 1
# ---------------------------------------------------------------------------


def Curve(*args: Any, **kwargs: Any) -> Any:
    r"""Construct an algebraic curve shadowing native Sage Curve, placing it in Curves(R)."""
    obj = _NativeCurve(*args, **kwargs)
    base_r = obj.base_ring() if hasattr(obj, "base_ring") else ZZ
    return refine(obj, Curves(base_r))


class Curves(Category_over_base_ring):
    r"""Category of algebraic curves over S (varieties of dimension 1)."""

    def _repr_object_names(self) -> str:
        return f"curves over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return Varieties(S)."""
        return [Varieties(self.base_ring())]

    class ParentMethods:
        r"""Curve parent methods."""

        def dimension(self: Any) -> int:
            r"""Return 1."""
            return 1

        def arithmetic_genus(self: Any) -> Any:
            r"""Return p_a = 1 - chi(O_C), the arithmetic genus of the curve."""
            if hasattr(self, "genus"):
                return self.genus()
            raise NotImplementedError("arithmetic_genus must be implemented by concrete Curve")

        def geometric_genus(self: Any) -> Any:
            r"""Return p_g = g(C_tilde), the geometric genus."""
            if hasattr(self, "genus"):
                return self.genus()
            raise NotImplementedError("geometric_genus must be implemented by concrete Curve")

    class ElementMethods:
        r"""Curve element methods."""

    class MorphismMethods:
        r"""Curve morphism methods."""


# ---------------------------------------------------------------------------
# Surfaces(S): Dimension = 2
# ---------------------------------------------------------------------------


class Surface(Variety):
    r"""An algebraic surface over S: a 2-dimensional variety over S."""

    Element = SchemeElement

    def __init__(self, base_ring: Any = ZZ) -> None:
        r"""Initialize the surface and refine into Surfaces(S)."""
        Variety.__init__(self, base_ring=base_ring)
        refine(self, Surfaces(base_ring))

    def dimension(self) -> int:
        r"""Return 2, the dimension of a surface."""
        return 2


class Surfaces(Category_over_base_ring):
    r"""Category of algebraic surfaces over S (varieties of dimension 2)."""

    def _repr_object_names(self) -> str:
        return f"surfaces over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return Varieties(S)."""
        return [Varieties(self.base_ring())]

    class ParentMethods:
        r"""Surface parent methods."""

        def dimension(self: Any) -> int:
            r"""Return 2."""
            return 2

        def intersection_form(self: Any) -> Any:
            r"""Return the intersection pairing on Pic(X) / NS(X)."""
            raise NotImplementedError("intersection_form must be implemented by concrete Surface")

    class ElementMethods:
        r"""Surface element methods."""

    class MorphismMethods:
        r"""Surface morphism methods."""


def install_varieties() -> None:
    r"""Register post-init hooks and installation for varieties, curves, surfaces, and toric varieties."""
    pass
