r"""Subtree for subschemes, open immersions and closed embeddings.

Hierarchy:
  Schemes(S)
    └── Subschemes(S)          ──> the scheme A together with the scheme B it sits in
          ├── OpenSubschemes(S)
          └── ClosedSubschemes(S)
"""

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from sage.structure.parent import Parent

from typing import Self, TYPE_CHECKING

if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.schemes.generic.morphism import SchemeMorphism_point
    from dzack_research.preamble.owned_category import ConstructionData

    from typing import Protocol

    class AmbientSpaceParent(Protocol):
        def dimension_relative(self) -> "Integer": ...

    class SubschemeParent(Protocol):
        r"""What a subscheme has from its placement on Sage's
        ``AlgebraicScheme_subscheme``."""

        def ambient_space(self) -> "AmbientSpaceParent": ...
        def dimension(self) -> "Integer": ...


class Subschemes(OwnedCategoryOverBaseRing):
    r"""Category of subschemes A of a scheme B."""

    def _repr_object_names(self) -> str:
        return f"subschemes over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return [Schemes(S)]."""
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.schemes.schemes import Schemes

        return [Schemes(self.base_ring())]

    class ParentMethods:
        r"""Parent methods for a subscheme A of a scheme B."""

        def __init__(
            self: Self,
            ambient: Parent,
            **rest: "ConstructionData",
        ) -> None:
            r"""Build the subscheme sitting in the scheme ``ambient``."""
            self._ambient = ambient
            super().__init__(**rest)

        def ambient_scheme(self: Self) -> Parent:
            r"""Return the scheme B of which this is a subscheme."""
            return self._ambient

        def inclusion_morphism(self: Self) -> "Morphism":
            r"""Return the structure inclusion morphism i: A -> B."""
            assert False, "inclusion_morphism must be implemented by concrete Subscheme"


class ClosedSubschemes(OwnedCategoryOverBaseRing):
    r"""Category of closed subschemes V -> X."""

    def _repr_object_names(self) -> str:
        return f"closed subschemes over {self.base_ring()}"

    def super_categories(self) -> list:
        r"""Return [Subschemes(S)]."""
        return [Subschemes(self.base_ring())]

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
        r"""Return [Subschemes(S)]."""
        return [Subschemes(self.base_ring())]


def install_subschemes() -> None:
    r"""Register post-init hooks and installation for subschemes."""
    pass


install_subschemes()
