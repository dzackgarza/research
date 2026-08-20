r"""Subtree for open subschemes and closed embeddings.

Hierarchy:
  Schemes(S).Subobjects()
    ├── OpenSubschemes(S)
    └── ClosedSubschemes(S)

A subscheme is its inclusion, so the scheme it sits in is
``inclusion().codomain()``.  The objects of both categories below are Sage
subschemes the preamble adopts, and Sage builds that arrow itself.
"""

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.schemes.generic.morphism import SchemeMorphism_point

    from typing import Protocol

    class AmbientSpaceParent(Protocol):
        def dimension_relative(self) -> "Integer": ...

    class SubschemeParent(Protocol):
        r"""What a subscheme has from its placement on Sage's
        ``AlgebraicScheme_subscheme``."""

        def ambient_space(self) -> "AmbientSpaceParent": ...
        def dimension(self) -> "Integer": ...
        def embedding_morphism(self) -> "Morphism": ...


class ClosedSubschemes(OwnedCategoryOverBaseRing):
    r"""Category of closed subschemes V -> X."""

    def _repr_object_names(self) -> str:
        return f"closed subschemes over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return [Schemes(S).Subobjects()]."""
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.schemes.schemes import Schemes

        return [Schemes(self.base_ring()).Subobjects()]

    class ParentMethods:
        r"""Parent methods for closed subschemes V -> X."""

        def inclusion(self: "SubschemeParent") -> "Morphism":
            r"""Return the closed embedding V -> X, which Sage builds."""
            return self.embedding_morphism()

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
        r"""Return [Schemes(S).Subobjects()]."""
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.schemes.schemes import Schemes

        return [Schemes(self.base_ring()).Subobjects()]

    class ParentMethods:
        r"""Parent methods for open subschemes U -> X."""

        def inclusion(self: "SubschemeParent") -> "Morphism":
            r"""Return the open immersion U -> X, which Sage builds."""
            return self.embedding_morphism()


def install_subschemes() -> None:
    r"""Register post-init hooks and installation for subschemes."""
    pass


install_subschemes()
