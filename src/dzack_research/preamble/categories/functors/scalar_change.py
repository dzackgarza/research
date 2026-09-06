r"""Scalar extension, restriction and coextension along a specified ring morphism.

For ``f: R -> S`` the three functors ``S tensor_R -``, ``Res_f`` and
``Hom_R(S, -)`` form the adjoint triple ``S tensor_R - -| Res_f -| Hom_R(S, -)``
(Weibel, *An Introduction to Homological Algebra*, Proposition 2.3.10 and
Exercise 2.3.6).  Induction, restriction and coinduction along a subgroup
``H <= G`` are these functors along ``R[H] -> R[G]``; their transversal
realization lives in ``group_induction``.
"""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras.group_algebras import GroupAlgebras
from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.modules.internal_hom import (
    InternalHom,
    internal_hom_morphism,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedModules,
    FramedModules,
    Modules,
    RestrictedScalarsModuleView,
    restrict_scalars,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _owned_ring,
    ring_morphism,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreshFreeModuleOn


class ScalarExtensionFunctor(Functor):
    r"""``S tensor_R - : Mod_R -> Mod_S`` along ``f:R -> S``.

    The mathematical functor is defined on every module.  The live computation
    presently materializes the represented framed/free/presented cases for
    which the module layer has an exact constructor.
    """

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        self._source_ring = _owned_ring(ring_map.domain())
        self._target_ring = _owned_ring(ring_map.codomain())
        super().__init__(Modules(self._source_ring), Modules(self._target_ring))

    def ring_map(self):
        return self._ring_map

    def _apply_object(self, module):

        if isinstance(module, RestrictedScalarsModuleView):
            if (
                _engine_ring(module.ring_map().domain()) is _engine_ring(self._source_ring)
                and _engine_ring(module.ring_map().codomain()) is _engine_ring(self._target_ring)
                and module in FramedModules(self._source_ring)
            ):
                image = FreshFreeModuleOn(
                    self._target_ring, module.module_generating_set()
                )
                return image
        return module.base_change(self.ring_map())

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())

        def image(label):
            original = morphism.domain().module_generator(label)
            coefficients = module_coefficients(morphism(original), morphism.codomain())
            return target.linear_combination(
                {
                    target_label: self._target_ring(
                        self.ring_map()(coefficient)
                    )
                    for target_label, coefficient in coefficients.items()
                }
            )

        return module_homset(source, target)(image)

    def _repr_(self):
        return f"Scalar extension along {self.ring_map()}"


class RestrictionOfScalarsFunctor(Functor):
    r"""``Res_f : Mod_S -> Mod_R`` along ``f:R -> S``."""

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        self._source_ring = _owned_ring(ring_map.domain())
        self._target_ring = _owned_ring(ring_map.codomain())
        super().__init__(Modules(self._target_ring), Modules(self._source_ring))

    def ring_map(self):
        return self._ring_map

    # Along ``R -> R[G]`` an ``R[G]``-module is an ``R``-module with a chosen
    # action, and restriction forgets the action: the image is the module the
    # action was equipped on, read through the forget and equip morphisms.
    # Along any other map the image is the restricted-scalars view.

    def _restricts_group_modules(self) -> bool:
        return self._target_ring in GroupAlgebras(self._source_ring)

    def _apply_object(self, module):
        if self._restricts_group_modules():
            return module.unacted_module()
        return restrict_scalars(module, self.ring_map())

    def _restricted_element(self, restricted, element):
        r"""Read an element of the ``S``-module in its restriction ``restricted``."""
        if self._restricts_group_modules():
            return self.chosen_preimage(restricted).forget_action_morphism()(element)
        return restricted(element)

    def _extension_element(self, restricted, element):
        r"""Read an element of ``restricted`` back in the ``S``-module it restricts."""
        if self._restricts_group_modules():
            return self.chosen_preimage(restricted).equip_action_morphism()(element)
        return element.underlying_element()

    def _apply_morphism(self, morphism):
        # Restriction changes which ring acts and never the underlying map, so
        # ``Res_f(g)`` is ``g``: its element action is the original one read
        # through the restricted parents, and its ``R``-linearity is the
        # ``S``-linearity of ``g`` along ``f``, not a runtime condition.  A
        # framing of the source is therefore not part of the statement.
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return module_homset(source, target).elementwise(
            lambda element: self._restricted_element(
                target, morphism(self._extension_element(source, element))
            ),
            verify_linearity=False,
        )

    def _repr_(self):
        return f"Restriction of scalars along {self.ring_map()}"


class CoextensionOfScalarsFunctor(Functor):
    r"""``Hom_R(S, -) : Mod_R -> Mod_S`` along ``f: R -> S``, the right adjoint of ``Res_f``.

    ``S`` acts on ``Hom_R(S, M)`` through its right regular action,
    ``(s . phi)(t) = phi(t s)``.  The Hom is represented when ``S`` is a
    finitely framed ``R``-module; ``Hom_ZZ(ZZ[x], M)`` is a countable product
    the module layer does not build, and is refused.
    """

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        self._source_ring = _owned_ring(ring_map.domain())
        self._target_ring = _owned_ring(ring_map.codomain())
        super().__init__(Modules(self._source_ring), Modules(self._target_ring))

    def ring_map(self):
        return self._ring_map

    def scalars_as_module(self):
        r"""``S`` as an ``R``-module, the domain of every ``Hom_R(S, M)``."""
        scalars, ring = self._target_ring, self._source_ring
        assert scalars in Modules(ring), f"{scalars} is not placed as a module over {ring}"
        assert scalars in FramedModules(ring) and scalars in FinitelyGeneratedModules(ring), (
            f"Hom_R(S, -) is represented here for S finitely framed over R; {scalars} is not"
        )
        return scalars

    def _right_multiplication(self, scalar):
        scalars = self.scalars_as_module()
        return module_homset(scalars, scalars)(
            {
                label: scalars.module_generator(label) * scalar
                for label in scalars.module_generating_set()
            }
        )

    # A coextended module over a group algebra is a group module, whose
    # elements are those of ``Hom_R(S, M)`` transported along the equip and
    # forget morphisms; over any other ring it is the general module carried
    # by ``Hom_R(S, M)``.

    def _coextends_to_group_modules(self) -> bool:
        return self._target_ring in GroupAlgebras(self._source_ring)

    def _hom_element(self, coextended, element):
        r"""Read an element of ``Hom_R(S, M)`` off the coextended module."""
        if self._coextends_to_group_modules():
            return coextended.forget_action_morphism()(element)
        return element.underlying_element()

    def _coextended_element(self, coextended, hom_element):
        if self._coextends_to_group_modules():
            return coextended.equip_action_morphism()(hom_element)
        return coextended(hom_element)

    def _linear_map(self, domain, codomain, function):
        r"""The ``S``-linear map given elementwise by ``function``."""
        if self._coextends_to_group_modules():
            return domain.Mor(codomain)._from_equivariant_images(
                function, elementwise=True, verify_linearity=False
            )
        return module_homset(domain, codomain).elementwise(function, verify_linearity=False)

    def _apply_object(self, module):
        scalars = self.scalars_as_module()
        hom = InternalHom(scalars, module)
        identity = module_homset(module, module).identity()
        endomorphisms = Modules(self._source_ring).End(hom)
        action = ring_morphism(
            self._target_ring,
            endomorphisms,
            lambda scalar: internal_hom_morphism(
                hom, hom, self._right_multiplication(scalar), identity
            ),
        )
        return Modules(self._target_ring)(hom, action)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        scalars = self.scalars_as_module()
        postcomposition = internal_hom_morphism(
            InternalHom(scalars, morphism.domain()),
            InternalHom(scalars, morphism.codomain()),
            module_homset(scalars, scalars).identity(),
            morphism,
        )
        return self._linear_map(
            source,
            target,
            lambda element: self._coextended_element(
                target, postcomposition(self._hom_element(source, element))
            ),
        )

    def _repr_(self):
        return f"Coextension of scalars along {self.ring_map()}"


class BaseChangeAdjunction(Adjunction):
    r"""``S tensor_R - ⊣ Res_f``."""

    _extension_functor = ScalarExtensionFunctor
    _restriction_functor = RestrictionOfScalarsFunctor

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        super().__init__(
            self._extension_functor(ring_map),
            self._restriction_functor(ring_map),
        )

    def unit(self, module):
        extended = self.left_adjoint()(module)
        restricted = self.right_adjoint()(extended)
        if restricted not in FramedModules(module.base_ring()):
            raise NotImplementedError(
                "the current module Hom surface cannot yet materialize the unit into an unframed restriction"
            )
        return module_homset(module, restricted)(
            lambda label: restricted(extended.module_generator(label))
        )

    def counit(self, module):
        restricted = self.right_adjoint()(module)
        extended = self.left_adjoint()(restricted)
        return module_homset(extended, module)(
            lambda label: restricted.module_generator(label).underlying_element()
        )


    def _repr_(self):
        return f"Scalar-extension/restriction adjunction along {self._ring_map}"


class RestrictionCoextensionAdjunction(Adjunction):
    r"""``Res_f ⊣ Hom_R(S, -)``.

    The unit sends ``n`` to ``s |-> s n`` and the counit evaluates at ``1``.
    """

    _restriction_functor = RestrictionOfScalarsFunctor
    _coextension_functor = CoextensionOfScalarsFunctor

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        super().__init__(
            self._restriction_functor(ring_map),
            self._coextension_functor(ring_map),
        )

    def unit(self, module):
        restricted = self.left_adjoint()(module)
        coextended = self.right_adjoint()(restricted)
        scalars = self.right_adjoint().scalars_as_module()
        hom = InternalHom(scalars, restricted)

        def image(element):
            return self.right_adjoint()._coextended_element(
                coextended,
                hom(
                    {
                        label: self.left_adjoint()._restricted_element(
                            restricted,
                            module.scalar_multiple(scalars.module_generator(label), element),
                        )
                        for label in scalars.module_generating_set()
                    }
                ),
            )

        return self.right_adjoint()._linear_map(module, coextended, image)

    def counit(self, module):
        coextended = self.right_adjoint()(module)
        restricted = self.left_adjoint()(coextended)
        one = self.right_adjoint().scalars_as_module().one()
        return module_homset(restricted, module).elementwise(
            lambda element: self.right_adjoint()._hom_element(
                coextended, self.left_adjoint()._extension_element(restricted, element)
            )(one),
            verify_linearity=False,
        )

    def _repr_(self):
        return f"Restriction/coextension adjunction along {self._ring_map}"


@cached_function
def base_change_adjunction(ring_map) -> BaseChangeAdjunction:
    return BaseChangeAdjunction(ring_map)


@cached_function
def restriction_coextension_adjunction(ring_map) -> RestrictionCoextensionAdjunction:
    return RestrictionCoextensionAdjunction(ring_map)
