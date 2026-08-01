r"""Category subtree for schemes over S under the schemes category tree.

Hierarchy:
  LocallyRingedSpaces()
    └── Schemes(S)
          ├── .Affine()
          ├── .Projective()
          ├── .QuasiAffine()
          ├── .QuasiProjective()
          ├── .Integral()
          ├── .Separated()
          ├── .FiniteType()
          ├── .Normal()
          ├── .Smooth()
          ├── .OpenImmersion()
          └── .ClosedEmbedding()
"""

from typing import Any

from sage.categories.category_types import Category_over_base_ring
from sage.categories.category_with_axiom import (
    all_axioms,
    axiom,
)
from sage.rings.integer_ring import ZZ

# Register scheme axioms in Sage's axiom registry if not already present
for _axiom_name in (
    "Affine",
    "Projective",
    "QuasiAffine",
    "QuasiProjective",
    "Integral",
    "Separated",
    "FiniteType",
    "Normal",
    "Smooth",
    "OpenImmersion",
    "ClosedEmbedding",
):
    if _axiom_name not in all_axioms:
        all_axioms.add(_axiom_name)


class SchemeElement(Element):
    r"""Point or section of a scheme."""


class Scheme(LocallyRingedSpace):
    r"""A scheme over S: a locally ringed space locally isomorphic to affine schemes."""

    Element = SchemeElement

    def __init__(self, base_ring: Any = ZZ) -> None:
        r"""Initialize the scheme and refine into Schemes(S)."""
        LocallyRingedSpace.__init__(self, base_ring=base_ring)
        refine(self, Schemes(base_ring))


class SchemeMorphism(Morphism):
    r"""Morphism of schemes over S."""


class Schemes(Category_over_base_ring):
    r"""Category of schemes over a base scheme or ring S."""

    def _repr_object_names(self) -> str:
        return f"schemes over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return LocallyRingedSpaces(), of which schemes are a subcategory."""
        return [LocallyRingedSpaces()]

    class SubcategoryMethods:
        r"""Axiom subcategories offered on Schemes(S)."""

        Affine = axiom("Affine")
        Projective = axiom("Projective")
        QuasiAffine = axiom("QuasiAffine")
        QuasiProjective = axiom("QuasiProjective")
        Integral = axiom("Integral")
        Separated = axiom("Separated")
        FiniteType = axiom("FiniteType")
        Normal = axiom("Normal")
        Smooth = axiom("Smooth")
        OpenImmersion = axiom("OpenImmersion")
        ClosedEmbedding = axiom("ClosedEmbedding")

    class ParentMethods:
        r"""Scheme parent methods."""

        def base_scheme(self: Any) -> Any:
            r"""Return the base scheme or ring S."""
            if hasattr(self, "base_ring") and callable(self.base_ring):
                return self.base_ring()
            return self.category().base_ring()

        def is_affine(self: Any) -> bool:
            r"""Return whether the scheme is affine."""
            return self.category().is_subcategory(Schemes(self.base_scheme()).Affine())

        def is_projective(self: Any) -> bool:
            r"""Return whether the scheme is projective."""
            return self.category().is_subcategory(Schemes(self.base_scheme()).Projective())

        def dimension(self: Any) -> Any:
            r"""Return the dimension of the scheme."""
            raise NotImplementedError("dimension must be implemented by concrete Scheme")

    class Affine:
        class ParentMethods:
            r"""Affine scheme methods (backed by coordinate ring A = S[x1,...,xn]/I)."""

            def coordinate_ring(self: Any) -> Any:
                r"""Return the coordinate ring A = S[x1,...,xn]/I of the affine scheme Spec(A)."""
                if hasattr(self, "coordinate_ring"):
                    return self.coordinate_ring()
                raise NotImplementedError("coordinate_ring must be implemented by concrete Affine Scheme")

    class Projective:
        class ParentMethods:
            r"""Projective scheme methods (structure morphism X -> S is projective)."""

            def structure_morphism(self: Any) -> Any:
                r"""Return the projective structure morphism f: X -> S."""
                raise NotImplementedError("structure_morphism must be implemented by concrete Projective Scheme")

            def projective_embedding(self: Any, line_bundle: Any = None) -> Any:
                r"""Return a closed immersion i_L: X -> P^n_S induced by a very ample line bundle L in Pic(X)."""
                raise NotImplementedError("projective_embedding must be implemented by concrete Projective Scheme")

    class QuasiAffine:
        class ParentMethods:
            r"""Quasi-affine scheme methods (open subscheme of an affine scheme)."""

    class QuasiProjective:
        class ParentMethods:
            r"""Quasi-projective scheme methods (open subscheme of a projective scheme)."""

    class ElementMethods:
        r"""Scheme element methods."""

    class MorphismMethods:
        r"""Scheme morphism methods."""


def install_schemes() -> None:
    r"""Register post-init hooks and installation for schemes."""
    pass
