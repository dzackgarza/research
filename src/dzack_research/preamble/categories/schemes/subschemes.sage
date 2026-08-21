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

from collections.abc import Sequence
from typing import TYPE_CHECKING

from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.structure.parent import Parent

from dzack_research.preamble.owned_category import object_of

if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.schemes.generic.morphism import SchemeMorphism_point
    from dzack_research.preamble.lexicon import RingElement
    from dzack_research.preamble.owned_category import ConstructionData

    from typing import Protocol

    class SubschemeParent(Protocol):
        r"""What a subscheme has from its placement on Sage's
        ``AlgebraicScheme_subscheme``."""

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
            r"""Return dim(X) - dim(V), the codimension of V in X."""
            return self.inclusion().codomain().dimension() - self.dimension()

        def intersection_multiplicity(
            self: "SubschemeParent",
            other: "SubschemeParent",
            point: "SchemeMorphism_point",
        ) -> "Integer":
            r"""Return $i(p;\, V\cdot W)$, the multiplicity of $V\cap W$ at $p$.

            The length of the stalk at $p$ of the structure sheaf of the
            scheme-theoretic intersection $V\cap W$, taken over the local
            ring $\mathcal O_{X,p}$ of the common codomain scheme.

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
            assert self.inclusion().codomain() == other.inclusion().codomain(), (
                "an intersection multiplicity is read in one scheme; "
                f"{self} maps to {self.inclusion().codomain()} and {other} "
                f"maps to {other.inclusion().codomain()}"
            )
            return super().intersection_multiplicity(other, point)


class EquationDefinedClosedSubschemes(OwnedCategoryOverBaseRing):
    r"""Closed subschemes presented by equations in a specified scheme."""

    def _repr_object_names(self) -> str:
        return f"equation-defined closed subschemes over {self.base_ring()}"

    def super_categories(self) -> list:
        return [ClosedSubschemes(self.base_ring())]

    class ParentMethods:
        def __init__(
            self,
            scheme: Parent,
            equations: "Sequence[RingElement]" = (),
            dimension: int | None = None,
            **rest: "ConstructionData",
        ) -> None:
            self._equations = tuple(equations)
            self._dimension = (
                int(scheme.dimension()) - len(self._equations)
                if dimension is None
                else int(dimension)
            )
            super().__init__(base=scheme.base_ring(), **rest)
            from dzack_research.preamble.categories.schemes.schemes import Schemes

            self._inclusion = SetMorphism(
                Hom(self, scheme, Schemes(self.base_ring())),
                lambda point: point,
            )

        def inclusion(self) -> "Morphism":
            r"""Return the closed embedding into the specified scheme."""
            return self._inclusion

        def equations(self) -> tuple["RingElement", ...]:
            r"""Return the equations that define this closed subscheme."""
            return self._equations

        def dimension(self) -> int:
            r"""Return the declared dimension of the closed subscheme."""
            return self._dimension

        def defining_polynomial(self) -> "RingElement":
            r"""Return the equation of a principal closed subscheme."""
            assert len(self.equations()) == 1, (
                "a defining polynomial is available for one equation"
            )
            return self.equations()[0]


def EquationDefinedClosedSubscheme(
    scheme: Parent,
    equations: "Sequence[RingElement]" = (),
    dimension: int | None = None,
) -> Parent:
    r"""Return the closed subscheme of ``scheme`` cut out by ``equations``."""
    return object_of(
        EquationDefinedClosedSubschemes(scheme.base_ring()),
        scheme=scheme,
        equations=equations,
        dimension=dimension,
    )


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
