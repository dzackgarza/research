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

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.owned_category_bases import (
    HomsetsCategory,
    SubobjectsCategory,
)
from sage.structure.parent import Parent
from dzack_research.preamble.categories.schemes.ringed_spaces import LocallyRingedSpaces
from sage.structure.element import Element
from sage.categories.category_with_axiom import (
    all_axioms,
    axiom,
)
from sage.matrix.constructor import matrix
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.schemes.toric.all import toric_varieties

from dzack_research.preamble.categories.sets.owned_sets import Sets

from collections.abc import Sequence
from typing import Self, TYPE_CHECKING

if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.geometry.fan import RationalPolyhedralFan
    from sage.categories.rings import Ring
    from dzack_research.preamble.lexicon import RingElement
    from sage.structure.parent import ElementConstructorInput

    from typing import Protocol

    class SchemeParent(Protocol):
        r"""What these categories' objects have from their placement on Sage's
        ``sage.schemes.generic.ambient_space.AmbientSpace``."""

        def base_ring(self) -> "Ring": ...
        def category(self) -> Category: ...
        def subscheme(
            self,
            equations: "RingElement | Sequence[RingElement]",
            **keywords: "ElementConstructorInput",
        ) -> Parent: ...
        def gen(self, i: "Integer") -> Element: ...
        def dimension_relative(self) -> "Integer": ...

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


class Schemes(OwnedCategoryOverBaseRing):
    r"""Category of schemes over a base scheme or ring S.

    A scheme is a locally ringed space that is locally isomorphic to an
    affine scheme.
    """

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

    class Subobjects(SubobjectsCategory):
        r"""Subschemes: a scheme A together with an inclusion A -> B.

        The scheme A sits in is ``inclusion().codomain()`` and is read from
        there, so no object of this category records it a second time.
        """

    class ElementMethods:
        r"""Scheme element methods: a point or a section."""

    class Homsets(HomsetsCategory):
        r"""Homsets in \(\operatorname{Sch}/S\)."""

        class ElementMethods:
            r"""Scheme morphisms in \(\operatorname{Sch}/S\).

            Point evaluation at an S-point p: S -> X is the composition f * p.
            A preimage or fiber over an S-point, or over a subobject Z -> Y,
            is the fiber product X \times_Y Z.
            """

            @abstract_method
            def compose(self: Self, g: "Morphism") -> "Morphism":
                r"""Return the composition (g o self): X -> Z for g: Y -> Z."""
                ...

            @abstract_method
            def pullback(self: Self, Z: "Morphism | Parent") -> Parent:
                r"""Return the fiber product X \times_Y Z for a morphism Z -> Y."""
                ...

            def evaluate_at(self: Self, p: "Morphism") -> "Morphism":
                r"""Return the value of self at an S-point p: S -> X."""
                return self * p

class AffineSpaces(OwnedCategoryOverBaseRing):
    r"""Category of affine spaces AA^n over a base scheme or ring S."""

    def _repr_object_names(self) -> str:
        return f"affine spaces over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return [Schemes(S)]."""
        return [Schemes(self.base_ring())]

    class ParentMethods:
        r"""Parent methods for AffineSpaces category."""

        @cached_method
        def picard_group(self: "SchemeParent") -> "PicardGroup":
            r"""Return \(\operatorname{Pic}(\mathbb A^n)=0\)."""
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.divisors.picard_groups import PicardGroup
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import Free_ZZ

            picard: "PicardGroup" = PicardGroup(Free_ZZ(Sets.Δ[-1]))
            return picard

        @cached_method
        def class_group(self: "SchemeParent") -> "ClassGroup":
            r"""Return \(\operatorname{Cl}(\mathbb A^n)=0\)."""
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.divisors.class_groups import ClassGroup
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import Free_ZZ

            divisor_classes: "ClassGroup" = ClassGroup(Free_ZZ(Sets.Δ[-1]))
            return divisor_classes

        def closed_subscheme(
            self: "SchemeParent",
            *equations: "RingElement",
        ) -> Parent:
            r"""Return V(f1,...,fk) subset AA^n refined into ClosedSubschemes(R)."""
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.schemes.subschemes import ClosedSubschemes
            from dzack_research.preamble.refine import refine

            eqs = equations[0] if len(equations) == 1 and isinstance(equations[0], (list, tuple)) else list(equations)
            sub = self.subscheme(eqs)
            closed: Parent = refine(sub, ClosedSubschemes(self.base_ring()))
            return closed

        def basic_open(self: "SchemeParent", f: "RingElement") -> Parent:
            r"""Return D(f) = AA^n \ V(f) as an OpenSubschemes(R)."""
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.schemes.subschemes import OpenSubschemes
            from dzack_research.preamble.refine import refine

            sub = self.subscheme([], principal_open=f)
            distinguished_open: Parent = refine(sub, OpenSubschemes(self.base_ring()))
            return distinguished_open


class ProjectiveSpaces(OwnedCategoryOverBaseRing):
    r"""Category of projective spaces PP^n over a base scheme or ring S."""

    def _repr_object_names(self) -> str:
        return f"projective spaces over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return [Schemes(S)]."""
        return [Schemes(self.base_ring())]

    class ParentMethods:
        r"""Parent methods for ProjectiveSpaces category."""

        def fan(self: "SchemeParent") -> "RationalPolyhedralFan":
            r"""Return the rational polyhedral fan of PP^n."""
            fan: "RationalPolyhedralFan" = toric_varieties.P(
                int(self.dimension_relative())
            ).fan()
            return fan

        @cached_method
        def picard_group(self: "SchemeParent") -> "PicardGroup":
            r"""Return \(\operatorname{Pic}(\mathbb P^n)\cong\mathbb Z\)."""
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.divisors.picard_groups import PicardGroup
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import Free_ZZ

            picard: "PicardGroup" = PicardGroup(Free_ZZ(Sets.Δ[0]))
            return picard

        @cached_method
        def class_group(self: "SchemeParent") -> "ClassGroup":
            r"""Return \(\operatorname{Cl}(\mathbb P^n)\cong\mathbb Z\)."""
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.divisors.class_groups import ClassGroup
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import Free_ZZ

            divisor_classes: "ClassGroup" = ClassGroup(Free_ZZ(Sets.Δ[0]))
            return divisor_classes

        def hyperplane(self: "SchemeParent", i: "Integer" = 0) -> Parent:
            r"""Return the hyperplane H_i = (x_i = 0) subset PP^n as a ClosedSubschemes(R)."""
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.schemes.subschemes import ClosedSubschemes
            from dzack_research.preamble.refine import refine

            sub = self.subscheme([self.gen(i)])
            hyperplane: Parent = refine(sub, ClosedSubschemes(self.base_ring()))
            return hyperplane

        def closed_subscheme(
            self: "SchemeParent",
            *equations: "RingElement",
        ) -> Parent:
            r"""Return V(f1,...,fk) subset PP^n refined into ClosedSubschemes(R)."""
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.schemes.subschemes import ClosedSubschemes
            from dzack_research.preamble.refine import refine

            eqs = equations[0] if len(equations) == 1 and isinstance(equations[0], (list, tuple)) else list(equations)
            sub = self.subscheme(eqs)
            closed: Parent = refine(sub, ClosedSubschemes(self.base_ring()))
            return closed

        def basic_open(self: "SchemeParent", f: "RingElement") -> Parent:
            r"""Return D(f) = PP^n \ V(f) as an OpenSubschemes(R)."""
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.schemes.subschemes import OpenSubschemes
            from dzack_research.preamble.refine import refine

            sub = self.subscheme([], principal_open=f)
            distinguished_open: Parent = refine(sub, OpenSubschemes(self.base_ring()))
            return distinguished_open


def install_schemes() -> None:
    r"""Register post-init hooks and installation for schemes."""
    pass


install_schemes()
