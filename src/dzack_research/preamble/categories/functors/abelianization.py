r"""Abelianization as the left adjoint to the inclusion of abelian groups.

For the owned group categories,

``(-)^ab ⊣ i : Ab -> Grp``.

The implementation uses GAP's natural quotient by the derived subgroup.  The
quotient map itself is retained as the unit, and morphisms are transported by
the universal property of that quotient rather than by a presentation chosen
in Python.
"""

from sage.groups.libgap_group import GroupLibGAP
from sage.libs.gap.libgap import libgap
from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.group.group_morphisms import group_homset
from dzack_research.preamble.categories.group.groups import (
    OwnedAbelianGroups,
    OwnedGroups,
    _gap_model,
    refine_group,
)
from dzack_research.preamble.refine import refine


class AbelianizationFunctor(Functor):
    r"""``G -> G/[G,G] : Grp -> Ab``."""

    def __init__(self) -> None:
        super().__init__(OwnedGroups(), OwnedAbelianGroups())

    def _apply_object(self, group):
        model = _gap_model(group)
        derived = libgap.DerivedSubgroup(model)
        projection = libgap.NaturalHomomorphismByNormalSubgroup(model, derived)
        quotient = refine_group(GroupLibGAP(projection.Range()))
        quotient = refine(quotient, OwnedAbelianGroups())
        quotient._preamble_abelianization_projection = group_homset(group, quotient)(
            projection
        )
        return quotient

    def source_group(self, abelianization):
        projection = getattr(
            abelianization,
            "_preamble_abelianization_projection",
            None,
        )
        if projection is None or projection.codomain() is not abelianization:
            raise ValueError(f"{abelianization} is not an abelianization construction")
        return projection.domain()

    def quotient_projection_from_image(self, abelianization):
        self.source_group(abelianization)
        return abelianization._preamble_abelianization_projection

    def quotient_projection(self, group):
        quotient = self(group)
        projection = self.quotient_projection_from_image(quotient)
        if projection.domain() is not group:
            raise ValueError("the abelianization quotient has the wrong source group")
        return projection

    def _apply_morphism(self, morphism):
        source_abelianization = self(morphism.domain())
        target_abelianization = self(morphism.codomain())
        source_projection = self.quotient_projection_from_image(source_abelianization).gap()
        target_projection = self.quotient_projection_from_image(target_abelianization).gap()
        source_model = _gap_model(source_abelianization)
        target_model = _gap_model(target_abelianization)
        engine_morphism = morphism.gap()
        generators = tuple(source_model.GeneratorsOfGroup())
        images = tuple(
            target_projection.Image(
                engine_morphism.Image(
                    source_projection.PreImagesRepresentative(generator)
                )
            )
            for generator in generators
        )
        induced = libgap.GroupHomomorphismByImages(
            source_model,
            target_model,
            list(generators),
            list(images),
        )
        if induced.is_bool():
            raise ValueError("the group morphism did not induce a map on abelianizations")
        return group_homset(source_abelianization, target_abelianization)(induced)

    def _repr_(self):
        return "Abelianization functor"


class AbelianGroupInclusionFunctor(Functor):
    r"""The full inclusion ``Ab -> Grp``."""

    def __init__(self) -> None:
        super().__init__(OwnedAbelianGroups(), OwnedGroups())

    def _apply_object(self, group):
        return group

    def _apply_morphism(self, morphism):
        return morphism

    def _repr_(self):
        return "Inclusion of abelian groups into groups"


class AbelianizationAdjunction(Adjunction):
    r"""``(-)^ab ⊣ i``."""

    def __init__(self) -> None:
        super().__init__(AbelianizationFunctor(), AbelianGroupInclusionFunctor())

    def unit(self, group):
        return self.left_adjoint().quotient_projection(group)

    def counit(self, abelian_group):
        abelianization = self.left_adjoint()(abelian_group)
        projection = self.left_adjoint().quotient_projection_from_image(
            abelianization
        ).gap()
        quotient_model = _gap_model(abelianization)
        target_model = _gap_model(abelian_group)
        generators = tuple(quotient_model.GeneratorsOfGroup())
        images = tuple(
            projection.PreImagesRepresentative(generator)
            for generator in generators
        )
        engine = libgap.GroupHomomorphismByImages(
            quotient_model,
            target_model,
            list(generators),
            list(images),
        )
        if engine.is_bool():
            raise ValueError("the abelianization of an abelian group did not canonically identify with it")
        return group_homset(abelianization, abelian_group)(engine)

    def hom_set_isomorphism_forward(self, abelianized_morphism):
        projection = self.left_adjoint().quotient_projection_from_image(
            abelianized_morphism.domain()
        )
        return abelianized_morphism * projection

    def hom_set_isomorphism_inverse(self, group_morphism, codomain=None):
        target = group_morphism.codomain()
        if target not in OwnedAbelianGroups():
            raise TypeError("the universal abelianization map factors only through an abelian codomain")
        if codomain is not None and codomain is not target:
            raise ValueError("the stated codomain does not match the group morphism")
        source_abelianization = self.left_adjoint()(group_morphism.domain())
        projection = self.left_adjoint().quotient_projection_from_image(
            source_abelianization
        ).gap()
        source_model = _gap_model(source_abelianization)
        target_model = _gap_model(target)
        engine_morphism = group_morphism.gap()
        generators = tuple(source_model.GeneratorsOfGroup())
        images = tuple(
            engine_morphism.Image(projection.PreImagesRepresentative(generator))
            for generator in generators
        )
        factored = libgap.GroupHomomorphismByImages(
            source_model,
            target_model,
            list(generators),
            list(images),
        )
        if factored.is_bool():
            raise ValueError("the map to the abelian group did not factor through abelianization")
        return group_homset(source_abelianization, target)(factored)

    def _repr_(self):
        return "Abelianization/inclusion adjunction"


@cached_function
def abelianization_adjunction() -> AbelianizationAdjunction:
    return AbelianizationAdjunction()


__all__ = [
    "AbelianGroupInclusionFunctor",
    "AbelianizationAdjunction",
    "AbelianizationFunctor",
    "abelianization_adjunction",
]
