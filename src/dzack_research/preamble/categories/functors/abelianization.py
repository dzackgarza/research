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
from dzack_research.preamble.categories.group.groups import (
    OwnedAbelianGroups,
    OwnedFiniteAbelianGroups,
    OwnedGroups,
    _element_from_engine,
    _element_to_engine,
    _gap_model,
    _own_group,
)
from dzack_research.preamble.refine import refine


class _AbelianizationFunctor(Functor):
    r"""``G -> G/[G,G] : Grp -> Ab``."""

    def __init__(self) -> None:
        super().__init__(OwnedGroups(), OwnedAbelianGroups())
        self._quotient_projections = {}

    def _apply_object(self, group):
        model = _gap_model(group)
        derived = libgap.DerivedSubgroup(model)
        projection = libgap.NaturalMorphismByNormalSubgroup(model, derived)
        quotient = _own_group(GroupLibGAP(projection.Range()))
        # A quotient of a finite group is finite.
        placement = (
            OwnedFiniteAbelianGroups() if group.is_finite() is True else OwnedAbelianGroups()
        )
        quotient = refine(quotient, placement)
        quotient_projection = group.Mor(quotient)(projection)
        self._quotient_projections[id(group)] = (
            group,
            quotient,
            quotient_projection,
        )
        return quotient

    def quotient_projection(self, group):
        quotient = self(group)
        stored = self._quotient_projections.get(id(group))
        if (
            stored is None
            or stored[0] is not group
            or stored[1] is not quotient
        ):
            raise KeyError("the group has no retained abelianization quotient projection")
        projection = stored[2]
        if projection.domain() is not group or projection.codomain() is not quotient:
            raise ValueError("the retained abelianization quotient projection has the wrong endpoints")
        return projection

    def _apply_morphism(self, morphism):
        source_abelianization = self(morphism.domain())
        target_abelianization = self(morphism.codomain())
        source_projection = self.quotient_projection(morphism.domain()).gap()
        target_projection = self.quotient_projection(morphism.codomain()).gap()
        source_model = _gap_model(source_abelianization)
        target_model = _gap_model(target_abelianization)
        source_group = morphism.domain()
        target_group = morphism.codomain()
        generators = tuple(source_model.GeneratorsOfGroup())
        images = tuple(
            target_projection.Image(
                _element_to_engine(
                    target_group,
                    morphism(
                        _element_from_engine(
                            source_group,
                            source_projection.PreImagesRepresentative(generator),
                        )
                    ),
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
        return source_abelianization.Mor(target_abelianization)(induced)

    def _repr_(self):
        return "Abelianization functor"


class _AbelianGroupInclusionFunctor(Functor):
    r"""The full inclusion ``Ab -> Grp``."""

    def __init__(self) -> None:
        super().__init__(OwnedAbelianGroups(), OwnedGroups())

    def _apply_object(self, group):
        return group

    def _apply_morphism(self, morphism):
        return morphism

    def _repr_(self):
        return "Inclusion of abelian groups into groups"


class _AbelianizationAdjunction(Adjunction):
    r"""``(-)^ab ⊣ i``."""

    def __init__(self) -> None:
        super().__init__(_AbelianizationFunctor(), _AbelianGroupInclusionFunctor())

    def _unit_component(self, group):
        return self.left_adjoint().quotient_projection(group)

    def _counit_component(self, abelian_group):
        abelianization = self.left_adjoint()(abelian_group)
        projection = self.left_adjoint().quotient_projection(abelian_group).gap()
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
        return abelianization.Mor(abelian_group)(engine)


    def _repr_(self):
        return "Abelianization/inclusion adjunction"


@cached_function
def _abelianization_functor() -> _AbelianizationFunctor:
    return _AbelianizationFunctor()


@cached_function
def _abelianization_adjunction() -> _AbelianizationAdjunction:
    return _AbelianizationAdjunction()


__all__ = []
