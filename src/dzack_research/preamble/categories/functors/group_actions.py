r"""The trivial action, invariants and coinvariants as scalar change along the augmentation.

For the augmentation ``epsilon: R[G] -> R`` the adjoint triple
``R tensor_{R[G]} - -| Res_epsilon -| Hom_{R[G]}(R, -)`` is
``(-)_G -| Triv_G -| (-)^G``: restriction along ``epsilon`` equips a module
with the trivial action, scalar extension along it is the coinvariants
``M_G = R tensor_{R[G]} M`` and coextension the invariants
``M^G = Hom_{R[G]}(R, M)`` (Weibel, *An Introduction to Homological
Algebra*, §6.1).  The functors here are the scalar-change functors of
``scalar_change`` specialized to that hypothesis, with the group module's
represented equalizer and coequalizer as the computation.
"""

from dzack_research.preamble.categories.functors.scalar_change import (
    BaseChangeAdjunction,
    CoextensionOfScalarsFunctor,
    RestrictionCoextensionAdjunction,
    RestrictionOfScalarsFunctor,
    ScalarExtensionFunctor,
)
from dzack_research.preamble.categories.algebras.group_algebras import GroupAlgebras
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
from dzack_research.preamble.categories.modules.group_modules.group_modules import (
    group_module_homset,
    _trivial_action,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring


def is_augmentation_of_group_algebra(ring_map) -> bool:
    r"""Decide whether ``ring_map`` is the augmentation ``R[G] -> R``.

    The domain must be a group algebra over the codomain, and the map must
    send the chosen generators of ``G`` to ``1``; an algebra morphism out of
    ``R[G]`` is determined by its values on those generators.
    """
    source = _owned_ring(ring_map.domain())
    target = _owned_ring(ring_map.codomain())
    if source not in GroupAlgebras(target):
        return False
    return all(
        ring_map(source.module_generator(generator)) == target.one()
        for generator in source.group().group_generators()
    )


def _augmentation_data(ring_map):
    assert is_augmentation_of_group_algebra(ring_map), (
        f"{ring_map} is not the augmentation of a group algebra"
    )
    return _owned_ring(ring_map.domain()).group()


def _invariant_element(group_module, invariant_module, element):
    r"""Read an invariant-module element inside ``group_module``."""
    if group_module.is_trivial_action():
        return group_module.equip_action_morphism()(element)
    return invariant_module.inclusion()(element)


def _lift_to_invariants(group_module, invariant_module, element):
    r"""Lift a known invariant element from ``group_module``."""
    if group_module.is_trivial_action():
        return group_module.forget_action_morphism()(element)
    return invariant_module.inclusion().lift(element)


def _coinvariant_projection(group_module, coinvariants, element):
    if group_module.is_trivial_action():
        return group_module.forget_action_morphism()(element)
    return coinvariants.presentation_projection()(element)


class TrivialActionFunctor(RestrictionOfScalarsFunctor):
    r"""``Triv_G : Modules(R) -> Modules(R[G])``, restriction along the augmentation."""

    def __init__(self, ring_map) -> None:
        super().__init__(ring_map)
        self._group = _augmentation_data(ring_map)

    def group(self):
        return self._group

    def _apply_object(self, module):
        return _trivial_action(module, self.group())

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return group_module_homset(source, target)(
            lambda label: target.equip_action_morphism()(
                morphism(morphism.domain().module_generator(label))
            )
        )

    def _repr_(self):
        return f"Trivial {self.group()}-action functor"


class InvariantsFunctor(CoextensionOfScalarsFunctor):
    r"""``(-)^G : Modules(R[G]) -> Modules(R)``, coextension along the augmentation."""

    def __init__(self, ring_map) -> None:
        super().__init__(ring_map)
        self._group = _augmentation_data(ring_map)

    def group(self):
        return self._group

    def _apply_object(self, group_module):
        return group_module.module_invariants()

    def _apply_morphism(self, morphism):
        source_invariants = self(morphism.domain())
        target_invariants = self(morphism.codomain())

        def image(label):
            source = _invariant_element(
                morphism.domain(),
                source_invariants,
                source_invariants.module_generator(label),
            )
            return _lift_to_invariants(
                morphism.codomain(),
                target_invariants,
                morphism(source),
            )

        return module_homset(source_invariants, target_invariants)(image)

    def _repr_(self):
        return f"{self.group()}-invariants functor"


class CoinvariantsFunctor(ScalarExtensionFunctor):
    r"""``(-)_G : Modules(R[G]) -> Modules(R)``, scalar extension along the augmentation."""

    def __init__(self, ring_map) -> None:
        super().__init__(ring_map)
        self._group = _augmentation_data(ring_map)

    def group(self):
        return self._group

    def _apply_object(self, group_module):
        return group_module.module_coinvariants()

    def _apply_morphism(self, morphism):
        source_coinvariants = self(morphism.domain())
        target_coinvariants = self(morphism.codomain())

        def image(label):
            representative = morphism.domain().module_generator(label)
            return _coinvariant_projection(
                morphism.codomain(),
                target_coinvariants,
                morphism(representative),
            )

        return module_homset(source_coinvariants, target_coinvariants)(image)

    def _repr_(self):
        return f"{self.group()}-coinvariants functor"


class TrivialInvariantsAdjunction(RestrictionCoextensionAdjunction):
    r"""``Triv_G ⊣ (-)^G``, restriction/coextension along the augmentation."""

    _restriction_functor = TrivialActionFunctor
    _coextension_functor = InvariantsFunctor

    def unit(self, module):
        invariants = self.right_adjoint()(self.left_adjoint()(module))
        return module_homset(module, invariants)(
            lambda label: invariants.module_generator(label)
        )

    def counit(self, group_module):
        invariants = self.right_adjoint()(group_module)
        trivial = self.left_adjoint()(invariants)
        return group_module_homset(trivial, group_module)(
            lambda label: _invariant_element(
                group_module,
                invariants,
                trivial.forget_action_morphism()(trivial.module_generator(label)),
            )
        )

    def _repr_(self):
        return f"Trivial-action/invariants adjunction for {self.left_adjoint().group()}"


class CoinvariantsTrivialAdjunction(BaseChangeAdjunction):
    r"""``(-)_G ⊣ Triv_G``, base change along the augmentation."""

    _extension_functor = CoinvariantsFunctor
    _restriction_functor = TrivialActionFunctor

    def unit(self, group_module):
        coinvariants = self.left_adjoint()(group_module)
        trivial = self.right_adjoint()(coinvariants)
        if group_module.is_trivial_action():
            return group_module_homset(group_module, trivial)(
                lambda label: trivial.equip_action_morphism()(
                    group_module.forget_action_morphism()(
                        group_module.module_generator(label)
                    )
                )
            )
        projection = coinvariants.presentation_projection()
        return group_module_homset(group_module, trivial)(
            lambda label: trivial.equip_action_morphism()(
                projection(group_module.module_generator(label))
            )
        )

    def counit(self, module):
        coinvariants = self.left_adjoint()(self.right_adjoint()(module))
        if coinvariants is not module:
            raise ValueError("coinvariants of the trivial action must be the original module")
        return module_homset(module, module).identity()

    def _repr_(self):
        return f"Coinvariants/trivial-action adjunction for {self.left_adjoint().group()}"


__all__ = [
    "CoinvariantsFunctor",
    "CoinvariantsTrivialAdjunction",
    "InvariantsFunctor",
    "TrivialActionFunctor",
    "TrivialInvariantsAdjunction",
    "is_augmentation_of_group_algebra",
]
