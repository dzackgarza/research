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

from dzack_research.preamble.categories.functors.core import (
    Functor,
    NaturalTransformation,
)
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


class GroupActionFunctor(Functor):
    r"""An actual action functor ``BG -> C`` on one represented object.

    ``action(g)`` must return the endomorphism of the selected object induced
    by ``g``.  Concrete action owners use this class only after their own
    action datum has been validated; the generic ``GObjects(G,C)`` constructor
    accepts this or any other genuine functor with the same endpoints.
    """

    def __init__(self, group, category, obj, action) -> None:
        self._group = group
        self._category = category
        self._object = obj
        self._action = action
        if obj not in category:
            raise TypeError(f"{obj} is not an object of {category}")
        super().__init__(group.classifying_category(), category)

    def group(self):
        return self._group

    def underlying_object(self):
        return self._object

    def _apply_object(self, obj):
        if obj is not self.domain().an_object():
            raise ValueError("BG has one object")
        return self.underlying_object()

    def _apply_morphism(self, morphism):
        endomorphisms = self.codomain().Mor(
            self.underlying_object(), self.underlying_object()
        )
        return endomorphisms(self._action(morphism.group_element()))

    def _repr_(self):
        return f"{self.group()}-action functor on {self.underlying_object()}"


def action_functor_of(acted, group, category):
    r"""Return the unique represented ``BG -> C`` action carried by ``acted``."""
    from dzack_research.preamble.categories.abstract_categories.cat import Cat

    functor_category = Cat().Mor(group.classifying_category(), category)
    if acted in functor_category:
        return acted.arrow().functor()
    functor = acted.action_functor()
    if functor.domain() != group.classifying_category() or functor.codomain() != category:
        raise ValueError("the represented action functor has the wrong endpoints")
    return functor


def _underlying_equivariant_arrow(arrow, group, category):
    r"""Forget equivariance from either a natural transformation or a concrete arrow."""
    from dzack_research.preamble.categories.abstract_categories.cat import Cat
    from dzack_research.preamble.categories.group.g_objects import EquivariantMorphism

    functor_category = Cat().Mor(group.classifying_category(), category)
    if arrow.domain() in functor_category and arrow.codomain() in functor_category:
        point = group.classifying_category().an_object()
        return arrow.component(point)
    if isinstance(arrow, EquivariantMorphism):
        return arrow.underlying_arrow()
    return category.Mor(arrow.domain(), arrow.codomain())(arrow)


class ForgetGroupActionFunctor(Functor):
    r"""Evaluation at the unique object, ``[BG,C] -> C``."""

    _faithful = True

    def __init__(self, group, category) -> None:
        from dzack_research.preamble.categories.group.g_objects import GObjects

        self._group = group
        self._category = category
        super().__init__(GObjects(group, category), category)

    def group(self):
        return self._group

    def _apply_object(self, acted):
        action = action_functor_of(acted, self.group(), self.codomain())
        return action(action.domain().an_object())

    def _apply_morphism(self, arrow):
        return _underlying_equivariant_arrow(arrow, self.group(), self.codomain())

    def _repr_(self):
        return f"Forgetful functor from {self.group()}-objects in {self.codomain()}"


class TransportGroupActionFunctor(Functor):
    r"""Postcomposition ``[BG,C] -> [BG,D]`` by a functor ``C -> D``."""

    def __init__(self, group, transport) -> None:
        from dzack_research.preamble.categories.group.g_objects import GObjects

        self._group = group
        self._transport = transport
        super().__init__(
            GObjects(group, transport.domain()),
            GObjects(group, transport.codomain()),
        )

    def group(self):
        return self._group

    def transport_functor(self):
        return self._transport

    def _apply_object(self, acted):
        action = action_functor_of(
            acted,
            self.group(),
            self.transport_functor().domain(),
        )
        return self.codomain()(action.then(self.transport_functor()))

    def _apply_morphism(self, arrow):
        source = self.object_image(arrow.domain())
        target = self.object_image(arrow.codomain())
        component = self.transport_functor()(
            _underlying_equivariant_arrow(
                arrow,
                self.group(),
                self.transport_functor().domain(),
            )
        )
        source_action = action_functor_of(
            source, self.group(), self.transport_functor().codomain()
        )
        target_action = action_functor_of(
            target, self.group(), self.transport_functor().codomain()
        )
        return self.codomain().Mor(source, target)(
            NaturalTransformation(
                source_action,
                target_action,
                lambda _obj: component,
            )
        )

    def _repr_(self):
        return f"Transport of {self.group()}-actions through {self.transport_functor()}"


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


class RestrictionOfGroupActionFunctor(Functor):
    r"""``phi^*: GObjects(G, C) -> GObjects(H, C)`` for a group morphism ``phi: H -> G``.

    A ``G``-object is a group morphism ``rho: G -> Aut_C(X)``; composing with
    ``phi`` gives ``rho phi: H -> Aut_C(X)``, so restriction changes which
    group acts and nothing about the object of ``C`` underneath.  An
    equivariant morphism stays equivariant because both endpoints restrict
    along the same ``phi``.  Nothing here uses injectivity of ``phi``: the
    inclusion of a subgroup is one case, and a surjection onto ``G`` or the
    projection of a semidirect factor is admitted on the same footing.  On
    ``Modules(R[G])`` this is restriction of scalars along ``R[H] -> R[G]``
    (Serre, *Linear Representations of Finite Groups*, §7.1), which
    ``RestrictionOfActingGroupFunctor`` computes for a subgroup with the
    module presentation in hand.
    """

    def __init__(self, group_morphism, underlying_category) -> None:
        from dzack_research.preamble.categories.group.g_objects import GObjects

        self._group_morphism = group_morphism
        self._underlying_category = underlying_category
        Functor.__init__(
            self,
            GObjects(group_morphism.codomain(), underlying_category),
            GObjects(group_morphism.domain(), underlying_category),
        )

    def group_morphism(self):
        r"""Return ``phi: H -> G``, the morphism the action is restricted along."""
        return self._group_morphism

    def _apply_object(self, acted):
        morphism = self.group_morphism()
        category = self._underlying_category

        # Preserve the represented concrete carrier when that owner already
        # knows how to equip the restricted action.  The generic fallback is
        # literally precomposition BH -> BG -> C.
        from dzack_research.preamble.categories.sets.set_categories import Sets

        if category is Sets():
            from dzack_research.preamble.categories.group.g_sets import (
                FiniteGSets,
                finite_g_set,
            )

            if acted in FiniteGSets(morphism.codomain()):
                return finite_g_set(
                    acted.point_set(),
                    morphism.domain(),
                    lambda group_element, point: acted.act(morphism(group_element), point),
                )

        from dzack_research.preamble.categories.modules.pure.modules import Modules

        match category:
            case Modules():
                base_ring = category.base_ring()
                from dzack_research.preamble.categories.algebras.group_algebras import (
                    GroupAlgebra,
                )
                from dzack_research.preamble.categories.modules.group_modules.group_modules import (
                    _equip_action,
                )

                source_modules = Modules(GroupAlgebra(base_ring, morphism.codomain()))
                if acted not in source_modules:
                    action = action_functor_of(acted, morphism.codomain(), category)
                    from dzack_research.preamble.categories.group.classifying_categories import (
                        ClassifyingFunctor,
                    )

                    return self.codomain()(ClassifyingFunctor(morphism).then(action))

                unacted = acted.unacted_module()

                def restricted_action(group_element, vector):
                    equipped = acted.equip_action_morphism()(vector)
                    image = acted.action_of(morphism(group_element))(equipped)
                    return acted.forget_action_morphism()(image)

                return _equip_action(
                    unacted,
                    morphism.domain(),
                    restricted_action,
                    _action_is_trivial=acted.is_trivial_action(),
                )
            case _:
                pass

        # The affine-scheme specialization still owns a concrete carrier and
        # its fixed-locus operations; retain that owner until the scheme stream
        # moves its two-argument compatibility constructor.
        from dzack_research.preamble.categories.schemes.schemes import Schemes

        match category:
            case Schemes():
                base_ring = category.base_ring()
                if acted in Schemes(base_ring):
                    return self.codomain()(
                        acted,
                        lambda group_element: acted.action_of(morphism(group_element)),
                    )
            case _:
                pass

        action = action_functor_of(acted, morphism.codomain(), category)
        from dzack_research.preamble.categories.group.classifying_categories import (
            ClassifyingFunctor,
        )

        return self.codomain()(ClassifyingFunctor(morphism).then(action))

    def _apply_morphism(self, arrow):
        source = self.object_image(arrow.domain())
        target = self.object_image(arrow.codomain())
        category = self._underlying_category
        underlying = _underlying_equivariant_arrow(
            arrow,
            self.group_morphism().codomain(),
            category,
        )
        source_functors = self.codomain().functor_category()
        if source in source_functors and target in source_functors:
            source_action = action_functor_of(
                source, self.group_morphism().domain(), category
            )
            target_action = action_functor_of(
                target, self.group_morphism().domain(), category
            )
            return self.codomain().Mor(source, target)(
                NaturalTransformation(
                    source_action,
                    target_action,
                    lambda _obj: underlying,
                )
            )
        return self.codomain().Mor(source, target)(underlying)

    def _repr_(self):
        morphism = self.group_morphism()
        return (
            f"Restriction of actions along {morphism.domain()} -> {morphism.codomain()}"
        )


__all__ = [
    "CoinvariantsFunctor",
    "CoinvariantsTrivialAdjunction",
    "ForgetGroupActionFunctor",
    "GroupActionFunctor",
    "InvariantsFunctor",
    "RestrictionOfGroupActionFunctor",
    "TransportGroupActionFunctor",
    "TrivialActionFunctor",
    "TrivialInvariantsAdjunction",
    "action_functor_of",
    "is_augmentation_of_group_algebra",
]
