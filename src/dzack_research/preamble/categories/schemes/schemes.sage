r"""Category subtree for schemes over S under the schemes category tree.

Hierarchy:
  LocallyRingedSpaces()
    └── Schemes(S)
          ├── AffineSpaces(S)
          ├── ProjectiveSpaces(S)
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

from sage.categories.category_types import Category_over_base_ring
from sage.categories.category_with_axiom import (
    all_axioms,
    axiom,
)
from sage.matrix.constructor import matrix
from sage.misc.cachefunc import cached_method
from sage.schemes.toric.all import toric_varieties
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

    def __init__(self, base_ring=ZZ) -> None:
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

        def base_scheme(self):
            r"""Return the base scheme or ring S."""
            return self.base_ring()

        def is_affine(self) -> bool:
            r"""Return whether the scheme is affine."""
            return self.category().is_subcategory(Schemes(self.base_scheme()).Affine())

        def is_projective(self) -> bool:
            r"""Return whether the scheme is projective."""
            return self.category().is_subcategory(Schemes(self.base_scheme()).Projective())


class AffineSpaces(Category_over_base_ring):
    r"""Category of affine spaces AA^n over a base scheme or ring S."""

    def _repr_object_names(self) -> str:
        return f"affine spaces over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return [Schemes(S)]."""
        return [Schemes(self.base_ring())]

    class ParentMethods:
        r"""Parent methods for AffineSpaces category."""

        @cached_method
        def picard_group(self):
            r"""Return \(\operatorname{Pic}(\mathbb A^n)=0\)."""
            return PicardGroup(Free_ZZ(Sets.Δ[-1]))

        @cached_method
        def class_group(self):
            r"""Return \(\operatorname{Cl}(\mathbb A^n)=0\)."""
            return ClassGroup(Free_ZZ(Sets.Δ[-1]))

        def closed_subscheme(self, *equations):
            r"""Return V(f1,...,fk) subset AA^n refined into ClosedSubschemes(R)."""
            eqs = equations[0] if len(equations) == 1 and isinstance(equations[0], (list, tuple)) else list(equations)
            sub = self.subscheme(eqs)
            return refine(sub, ClosedSubschemes(self.base_ring()))

        def basic_open(self, f):
            r"""Return D(f) = AA^n \ V(f) as an OpenSubschemes(R)."""
            sub = self.subscheme([], principal_open=f)
            return refine(sub, OpenSubschemes(self.base_ring()))


class ProjectiveSpaces(Category_over_base_ring):
    r"""Category of projective spaces PP^n over a base scheme or ring S."""

    def _repr_object_names(self) -> str:
        return f"projective spaces over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return [Schemes(S)]."""
        return [Schemes(self.base_ring())]

    class ParentMethods:
        r"""Parent methods for ProjectiveSpaces category."""

        def fan(self):
            r"""Return the rational polyhedral fan of PP^n."""
            return toric_varieties.P(int(self.dimension_relative())).fan()

        @cached_method
        def picard_group(self):
            r"""Return \(\operatorname{Pic}(\mathbb P^n)\cong\mathbb Z\)."""
            return PicardGroup(Free_ZZ(Sets.Δ[0]))

        @cached_method
        def class_group(self):
            r"""Return \(\operatorname{Cl}(\mathbb P^n)\cong\mathbb Z\)."""
            return ClassGroup(Free_ZZ(Sets.Δ[0]))

        def hyperplane(self, i=0):
            r"""Return the hyperplane H_i = (x_i = 0) subset PP^n as a ClosedSubschemes(R)."""
            sub = self.subscheme([self.gen(i)])
            return refine(sub, ClosedSubschemes(self.base_ring()))

        def closed_subscheme(self, *equations):
            r"""Return V(f1,...,fk) subset PP^n refined into ClosedSubschemes(R)."""
            eqs = equations[0] if len(equations) == 1 and isinstance(equations[0], (list, tuple)) else list(equations)
            sub = self.subscheme(eqs)
            return refine(sub, ClosedSubschemes(self.base_ring()))

        def basic_open(self, f):
            r"""Return D(f) = PP^n \ V(f) as an OpenSubschemes(R)."""
            sub = self.subscheme([], principal_open=f)
            return refine(sub, OpenSubschemes(self.base_ring()))


def install_schemes() -> None:
    r"""Register post-init hooks and installation for schemes."""
    pass
