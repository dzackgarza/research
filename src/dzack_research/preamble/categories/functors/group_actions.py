r"""The adjoint triple around the trivial ``G``-action.

For a fixed ring ``R`` and group ``G``:

``(-)_G ⊣ Triv_G ⊣ (-)^G``.

The Hom-sets on the acted side are the actual equivariant Hom-sets supplied by
``GroupModuleHomset``; ordinary module maps are not silently substituted.
"""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.modules.pure.modules import FinitelyPresentedModules
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
from dzack_research.preamble.categories.modules.group_modules.group_modules import (
    FinitelyPresentedGroupModules,
    group_module_homset,
    trivial_group_action,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring


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


class TrivialActionFunctor(Functor):
    r"""``Triv_G`` on represented finitely-presented ``R``-modules."""

    def __init__(self, base_ring, group) -> None:
        self._base_ring = _owned_ring(base_ring)
        self._group = group
        super().__init__(
            FinitelyPresentedModules(self._base_ring),
            FinitelyPresentedGroupModules(self._base_ring, group),
        )

    def group(self):
        return self._group

    def _apply_object(self, module):
        return trivial_group_action(module, self.group())

    def chosen_preimage(self, image):
        if image.is_trivial_action():
            return image.unacted_module()
        return super().chosen_preimage(image)

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


class InvariantsFunctor(Functor):
    r"""``(-)^G`` on represented finitely-presented ``R[G]``-modules."""

    def __init__(self, base_ring, group) -> None:
        self._base_ring = _owned_ring(base_ring)
        self._group = group
        super().__init__(
            FinitelyPresentedGroupModules(self._base_ring, group),
            FinitelyPresentedModules(self._base_ring),
        )

    def _apply_object(self, group_module):
        return group_module.module_invariants()

    def chosen_preimage(self, image):
        inclusion = getattr(image, "inclusion", lambda: None)()
        if inclusion is not None:
            return inclusion.codomain()
        return super().chosen_preimage(image)

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
        return f"{self._group}-invariants functor"


class CoinvariantsFunctor(Functor):
    r"""``(-)_G`` on represented finitely-presented ``R[G]``-modules."""

    def __init__(self, base_ring, group) -> None:
        self._base_ring = _owned_ring(base_ring)
        self._group = group
        super().__init__(
            FinitelyPresentedGroupModules(self._base_ring, group),
            FinitelyPresentedModules(self._base_ring),
        )

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
        return f"{self._group}-coinvariants functor"


class TrivialInvariantsAdjunction(Adjunction):
    r"""``Triv_G ⊣ (-)^G``."""

    def __init__(self, base_ring, group) -> None:
        self._base_ring = _owned_ring(base_ring)
        self._group = group
        super().__init__(
            TrivialActionFunctor(self._base_ring, group),
            InvariantsFunctor(self._base_ring, group),
        )

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
        return f"Trivial-action/invariants adjunction for {self._group}"


class CoinvariantsTrivialAdjunction(Adjunction):
    r"""``(-)_G ⊣ Triv_G``."""

    def __init__(self, base_ring, group) -> None:
        self._base_ring = _owned_ring(base_ring)
        self._group = group
        super().__init__(
            CoinvariantsFunctor(self._base_ring, group),
            TrivialActionFunctor(self._base_ring, group),
        )

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
        return f"Coinvariants/trivial-action adjunction for {self._group}"


@cached_function
def trivial_invariants_adjunction(base_ring, group) -> TrivialInvariantsAdjunction:
    return TrivialInvariantsAdjunction(base_ring, group)


@cached_function
def coinvariants_trivial_adjunction(base_ring, group) -> CoinvariantsTrivialAdjunction:
    return CoinvariantsTrivialAdjunction(base_ring, group)
