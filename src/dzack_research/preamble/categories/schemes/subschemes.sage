r"""Subtree for subschemes, open immersions, closed embeddings, and quasischemes.

Hierarchy:
  Subscheme(Scheme) ──> inclusion_morphism i: A -> B
    ├── OpenSubscheme(Subscheme)   ──> OpenSubschemes(S)
    ├── ClosedSubscheme(Subscheme) ──> ClosedSubschemes(S)
    └── QuasiScheme(Scheme)       ──> QuasiAffine / QuasiProjective (V(I) \ V(J))
"""

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.schemes import SchemeElement
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent
from dzack_research.preamble.categories.schemes.schemes import Scheme
from sage.rings.integer_ring import ZZ as SageZZ


class Subscheme(Scheme):
    r"""A subscheme A of a scheme B, carrying the inclusion morphism i: A -> B."""

    Element = SchemeElement

    def __init__(self, ambient, base_ring=SageZZ) -> None:
        r"""Initialize the subscheme and record its ambient scheme B."""
        Scheme.__init__(self, base_ring=base_ring)
        self._ambient = ambient

    def ambient_scheme(self):
        r"""Return the ambient scheme B of which this is a subscheme."""
        return self._ambient

    def inclusion_morphism(self):
        r"""Return the structure inclusion morphism i: A -> B."""
        assert False, "inclusion_morphism must be implemented by concrete Subscheme"


class ClosedSubschemes(OwnedCategoryOverBaseRing):
    r"""Category of closed subschemes V -> X."""

    def _repr_object_names(self) -> str:
        return f"closed subschemes over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return [Schemes(S)]."""
        return [Schemes(self.base_ring())]

    class ParentMethods:
        r"""Parent methods for closed subschemes V -> X."""

        def codimension(self):
            r"""Return dim(X) - dim(V), the codimension of V in ambient X."""
            amb = self.ambient_space()
            dim_amb = amb.dimension_relative()
            return dim_amb - self.dimension()

class OpenSubschemes(OwnedCategoryOverBaseRing):
    r"""Category of open subschemes U -> X."""

    def _repr_object_names(self) -> str:
        return f"open subschemes over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return [Schemes(S)]."""
        return [Schemes(self.base_ring())]


class OpenSubscheme(Subscheme):
    r"""An open subscheme U -> X."""

    Element = SchemeElement

    def __init__(self, ambient, base_ring=SageZZ) -> None:
        r"""Initialize the open subscheme and refine into OpenSubschemes(base_ring)."""
        Subscheme.__init__(self, ambient=ambient, base_ring=base_ring)
        refine(self, OpenSubschemes(base_ring))


class ClosedSubscheme(Subscheme):
    r"""A closed subscheme Z -> X."""

    Element = SchemeElement

    def __init__(self, ambient, base_ring=SageZZ) -> None:
        r"""Initialize the closed subscheme and refine into ClosedSubschemes(base_ring)."""
        Subscheme.__init__(self, ambient=ambient, base_ring=base_ring)
        refine(self, ClosedSubschemes(base_ring))


class QuasiScheme(Scheme):
    r"""A quasi-scheme V(I) \ V(J) (quasi-affine or quasi-projective open subscheme)."""

    Element = SchemeElement

    def __init__(self, base_ring=SageZZ) -> None:
        r"""Initialize the quasi-scheme."""
        Scheme.__init__(self, base_ring=base_ring)


def install_subschemes() -> None:
    r"""Register post-init hooks and installation for subschemes."""
    pass
