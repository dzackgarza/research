r"""Category subtree for algebraic varieties over S, curves, surfaces, and toric varieties.

Hierarchy:
  Schemes(S)
    └── Varieties(S)
          ├── Curves(S)   (dim = 1)
          ├── Surfaces(S) (dim = 2)
          └── ToricVariety
"""

from typing import TYPE_CHECKING
from dzack_research.preamble.categories.schemes.schemes import Schemes
from dzack_research.preamble.refine import refine
if TYPE_CHECKING:
    from sage.rings.ring import Field
    from sage.rings.ring import Ring

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.schemes import SchemeElement
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent
from dzack_research.preamble.categories.schemes.schemes import Scheme
from sage.rings.rational_field import QQ as SageQQ
from sage.categories.category_with_axiom import (
    all_axioms,
    axiom,
)
import sage.schemes.curves.constructor as _sage_curve_const
import sage.schemes.toric.variety as _sage_toric
from sage.rings.integer_ring import ZZ as SageZZ


from typing import Self

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage.categories.rings import Ring
    from dzack_research.preamble.lexicon import OrderedSet

    from typing import Protocol

    class CurveParent(Protocol):
        r"""What a curve has from its placement: Sage's
        ``sage.schemes.curves.curve`` computes the genus, and the two genera
        below are named views of it."""

        def genus(self) -> "Integer": ...


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

    def __init__(self, base_ring: "Ring" = SageZZ) -> None:
        r"""Initialize the variety and refine into Varieties(S)."""
        Scheme.__init__(self, base_ring=base_ring)
        refine(self, Varieties(base_ring))


class Varieties(OwnedCategoryOverBaseRing):
    r"""Category of algebraic varieties over S: integral, separated schemes of finite type over S."""

    def _repr_object_names(self) -> str:
        return f"varieties over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return Schemes(self.base_ring())."""
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

    class ElementMethods:
        r"""Variety element methods."""

    class MorphismMethods:
        r"""Variety morphism methods."""


# ---------------------------------------------------------------------------
# ToricVarieties: Varieties(S)
# ---------------------------------------------------------------------------


def ToricVariety(
    fan: "Parent",
    coordinate_names: "OrderedSet" = None,
    names: "OrderedSet" = None,
    coordinate_indices: "OrderedSet" = None,
    base_ring: "Ring" = SageQQ,
    base_field: "Field" = None,
) -> "Parent":
    r"""Construct the toric variety of ``fan``, placing it in ``Varieties(R)``."""
    obj = _NativeToricVariety(
        fan, coordinate_names, names, coordinate_indices, base_ring, base_field
    )
    toric_variety: "Parent" = refine(obj, Varieties(obj.base_ring()))
    return toric_variety


# ---------------------------------------------------------------------------
# Curves(S): Dimension = 1
# ---------------------------------------------------------------------------


def Curve(F: "Parent", A: "Parent | None" = None) -> "Parent":
    r"""Construct the curve cut out by ``F``, placing it in ``Curves(R)``."""
    obj = _NativeCurve(F, A)
    curve: "Parent" = refine(obj, Curves(obj.base_ring()))
    return curve


class Curves(OwnedCategoryOverBaseRing):
    r"""Category of algebraic curves over S (varieties of dimension 1)."""

    def _repr_object_names(self) -> str:
        return f"curves over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return Varieties(self.base_ring())."""
        return [Varieties(self.base_ring())]

    class ParentMethods:
        r"""Curve parent methods."""

        def dimension(self: Self) -> "Integer":
            r"""Return 1."""
            return 1

        def arithmetic_genus(self: "CurveParent") -> "Integer":
            r"""Return p_a = 1 - chi(O_C), the arithmetic genus of the curve."""
            return self.genus()

        def geometric_genus(self: "CurveParent") -> "Integer":
            r"""Return p_g = g(C_tilde), the geometric genus."""
            return self.genus()

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

    def __init__(self, base_ring: "Ring" = SageZZ) -> None:
        r"""Initialize the surface and refine into Surfaces(S)."""
        Variety.__init__(self, base_ring=base_ring)
        refine(self, Surfaces(base_ring))

    def dimension(self) -> "Integer":
        r"""Return 2, the dimension of a surface."""
        return 2


class Surfaces(OwnedCategoryOverBaseRing):
    r"""Category of algebraic surfaces over S (varieties of dimension 2)."""

    def _repr_object_names(self) -> str:
        return f"surfaces over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return Varieties(self.base_ring())."""
        return [Varieties(self.base_ring())]

    class ParentMethods:
        r"""Surface parent methods."""

        def dimension(self) -> "Integer":
            r"""Return 2."""
            return 2

    class ElementMethods:
        r"""Surface element methods."""

    class MorphismMethods:
        r"""Surface morphism methods."""


def install_varieties() -> None:
    r"""Register post-init hooks and installation for varieties, curves, surfaces, and toric varieties."""
    pass


install_varieties()
