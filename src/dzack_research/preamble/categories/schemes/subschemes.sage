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

from typing import Self, TYPE_CHECKING

if TYPE_CHECKING:
    from sage.categories.rings import Ring
    from sage.schemes.generic.morphism import SchemeMorphism_point

    from typing import Protocol

    class AmbientSpaceParent(Protocol):
        def dimension_relative(self) -> "Integer": ...

    class SubschemeParent(Protocol):
        r"""What a subscheme has from its placement on Sage's
        ``AlgebraicScheme_subscheme``."""

        def ambient_space(self) -> "AmbientSpaceParent": ...
        def dimension(self) -> "Integer": ...


class Subscheme(Scheme):
    r"""A subscheme A of a scheme B, carrying the inclusion morphism i: A -> B."""

    Element = SchemeElement

    def __init__(self, ambient: "Parent", base_ring: "Ring" = SageZZ) -> None:
        r"""Initialize the subscheme and record its ambient scheme B."""
        Scheme.__init__(self, base_ring=base_ring)
        self._ambient = ambient

    def ambient_scheme(self) -> "Parent":
        r"""Return the ambient scheme B of which this is a subscheme."""
        return self._ambient

    def inclusion_morphism(self) -> "Morphism":
        r"""Return the structure inclusion morphism i: A -> B."""
        assert False, "inclusion_morphism must be implemented by concrete Subscheme"


class ClosedSubschemes(OwnedCategoryOverBaseRing):
    r"""Category of closed subschemes V -> X."""

    def _repr_object_names(self) -> str:
        return f"closed subschemes over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return [Schemes(S)]."""
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.schemes.schemes import Schemes

        return [Schemes(self.base_ring())]

    class ParentMethods:
        r"""Parent methods for closed subschemes V -> X."""

        def codimension(self: "SubschemeParent") -> "Integer":
            r"""Return dim(X) - dim(V), the codimension of V in ambient X."""
            amb = self.ambient_space()
            dim_amb = amb.dimension_relative()
            return dim_amb - self.dimension()

        def intersection_multiplicity(
            self: "SubschemeParent",
            other: "SubschemeParent",
            point: "SchemeMorphism_point",
        ) -> "Integer":
            r"""Return $i(p;\, V\cdot W)$, the multiplicity of $V\cap W$ at $p$.

            The length of the stalk at $p$ of the structure sheaf of the
            scheme-theoretic intersection $V\cap W$, taken over the local
            ring $\mathcal O_{X,p}$ of the ambient scheme both sit in.

            The definition is not yet sayable on this surface: ``stalk``
            stands as a declared, unmet obligation on
            ``LocallyRingedSpaces`` (``categories/schemes/ringed_spaces.sage``),
            while ``length`` is already there on a finitely generated module.
            Once ``stalk`` answers, this body becomes that definition --
            ``self.intersection(other).stalk(point).length()`` -- and the
            delegation below goes away.  Until then the engine computes it by
            Serre's Tor formula on the two defining ideals, which is the same
            number whenever the intersection is proper and finite; that
            hypothesis is the engine's to state and to check.

            ``super()`` reaches the engine because override-refine puts these
            ``ParentMethods`` ahead of the concrete class
            (``dzack_research.preamble.refine``).
            """
            assert self.ambient_space() == other.ambient_space(), (
                "an intersection multiplicity is read inside one ambient "
                f"scheme; {self} sits in {self.ambient_space()} and {other} "
                f"sits in {other.ambient_space()}"
            )
            return super().intersection_multiplicity(other, point)

class OpenSubschemes(OwnedCategoryOverBaseRing):
    r"""Category of open subschemes U -> X."""

    def _repr_object_names(self) -> str:
        return f"open subschemes over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return [Schemes(S)]."""
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.schemes.schemes import Schemes

        return [Schemes(self.base_ring())]


class OpenSubscheme(Subscheme):
    r"""An open subscheme U -> X."""

    Element = SchemeElement

    def __init__(self, ambient: "Parent", base_ring: "Ring" = SageZZ) -> None:
        r"""Initialize the open subscheme and refine into OpenSubschemes(base_ring)."""
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.refine import refine

        Subscheme.__init__(self, ambient=ambient, base_ring=base_ring)
        refine(self, OpenSubschemes(base_ring))


class ClosedSubscheme(Subscheme):
    r"""A closed subscheme Z -> X."""

    Element = SchemeElement

    def __init__(self, ambient: "Parent", base_ring: "Ring" = SageZZ) -> None:
        r"""Initialize the closed subscheme and refine into ClosedSubschemes(base_ring)."""
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.refine import refine

        Subscheme.__init__(self, ambient=ambient, base_ring=base_ring)
        refine(self, ClosedSubschemes(base_ring))


class QuasiScheme(Scheme):
    r"""A quasi-scheme V(I) \ V(J) (quasi-affine or quasi-projective open subscheme)."""

    Element = SchemeElement

    def __init__(self, base_ring: "Ring" = SageZZ) -> None:
        r"""Initialize the quasi-scheme."""
        Scheme.__init__(self, base_ring=base_ring)


def install_subschemes() -> None:
    r"""Register post-init hooks and installation for subschemes."""
    pass


install_subschemes()
