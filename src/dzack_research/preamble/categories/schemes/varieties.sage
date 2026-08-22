r"""Category subtree for algebraic varieties over S, curves, surfaces, and toric varieties.

Hierarchy:
  Schemes(S)
    └── Varieties(S)
          ├── Curves(S)   (dim = 1)
          └── Surfaces(S) (dim = 2)
"""

from typing import TYPE_CHECKING
from dzack_research.preamble.categories.schemes.schemes import Schemes
from dzack_research.preamble.categories.schemes.subschemes import ClosedSubschemes
from dzack_research.preamble.refine import refine

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from sage.structure.parent import Parent
from sage.rings.rational_field import QQ as SageQQ
from sage.categories.category_with_axiom import (
    all_axioms,
    axiom,
)
import sage.schemes.curves.constructor as _sage_curve_const
import sage.schemes.toric.variety as _sage_toric


from typing import Self

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage.rings.ring import Field
    from sage.categories.rings import Ring
    from dzack_research.preamble.lexicon import OrderedSet

_NativeToricVariety = _sage_toric.ToricVariety
_NativeCurve = _sage_curve_const.Curve

# Register dimension and toric axioms in Sage's axiom registry if not already present
for _axiom_name in ("DimensionOne", "DimensionTwo", "Toric"):
    if _axiom_name not in all_axioms:
        all_axioms.add(_axiom_name)


# ---------------------------------------------------------------------------
# Varieties(S)
# ---------------------------------------------------------------------------


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
    r"""Construct the curve cut out by ``F``, placing it in ``Curves(R)``.

    ``F`` cuts the curve out of a scheme, so what is built is also a
    closed subscheme of that scheme, and it is placed there too.  Codimension
    and intersection multiplicity are read off that placement; dimension one
    is what ``Curves(R)`` states.
    """
    obj = _NativeCurve(F, A)
    base_ring = obj.base_ring()
    curve: "Parent" = refine(obj, [Curves(base_ring), ClosedSubschemes(base_ring)])
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

    class ElementMethods:
        r"""Curve element methods."""

    class MorphismMethods:
        r"""Curve morphism methods."""


# ---------------------------------------------------------------------------
# Surfaces(S): Dimension = 2
# ---------------------------------------------------------------------------


class Surfaces(OwnedCategoryOverBaseRing):
    r"""Category of algebraic surfaces over S (varieties of dimension 2)."""

    def _repr_object_names(self) -> str:
        return f"surfaces over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return Varieties(self.base_ring())."""
        return [Varieties(self.base_ring())]

    class ParentMethods:
        r"""Surface parent methods."""

        def dimension(self: Self) -> "Integer":
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
