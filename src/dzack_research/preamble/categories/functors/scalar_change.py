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
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedModules,
    FramedModules,
    Modules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _owned_ring,
)


class _ScalarExtensionModuleMorphism(ModuleMorphism):
    r"""``S tensor_R f`` with the exact linearity premise carried by ``f``."""

    def __init__(self, parent, source_morphism, generator_images, functor) -> None:
        self._source_morphism = source_morphism
        self._extension_functor = functor
        super().__init__(
            parent,
            generator_images,
            scalar_extension_of=source_morphism,
            scalar_extension_functor=functor,
        )
        # Scalar extension is functorial on genuinely linear maps.  When the
        # input is only conditional, the image carries exactly that condition;
        # reconstructing it from generator images must not promote it to True.
        self._linearity_decision = source_morphism.linearity_decision()


class _RestrictionModuleMorphism(ModuleMorphism):
    r"""Restriction of scalars of one module map, with its source premise."""

    def __init__(self, parent, source_morphism, action) -> None:
        self._source_morphism = source_morphism
        super().__init__(parent, action, elementwise=True)

    def _elementwise_linearity_derivation(self):
        return self._source_morphism.linearity_decision()


class _CoextensionFunctorImageMorphism(ModuleMorphism):
    r"""Postcomposition on ``Hom_R(S,-)`` induced by an admitted module map."""

    def __init__(self, parent, source_morphism, action) -> None:
        self._source_morphism = source_morphism
        super().__init__(parent, action, elementwise=True)

    def _elementwise_linearity_derivation(self):
        return self._source_morphism.linearity_decision()


class _ScalarChangeStructureMorphism(ModuleMorphism):
    r"""A scalar-change unit or counit map, linear by its defining formula."""

    def _elementwise_linearity_derivation(self):
        return True


class _ScalarExtensionFunctor(Functor):
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
        # Restriction of scalars does not erase relations.  In particular
        # S tensor_R Res_f(M) cannot be replaced by a free module merely
        # because a generating family of Res_f(M) was selected.
        match self.ring_map():
            case ring_map if ring_map.is_identity():
                return module
            case _:
                return module.base_change(self.ring_map())

    def _apply_morphism(self, morphism):
        match self.ring_map():
            case ring_map if ring_map.is_identity():
                return morphism
            case _:
                pass
        source_module = morphism.domain()
        target_module = morphism.codomain()
        assert source_module in FramedModules(source_module.base_ring()), (
            "represented scalar extension of a module morphism currently requires a selected source framing"
        )
        assert target_module in FramedModules(target_module.base_ring()), (
            "represented scalar extension of a module morphism currently requires a selected target framing"
        )
        source = self(source_module)
        target = self(target_module)

        def image(label):
            original = source_module.module_generator(label)
            coefficients = target_module.framing_coefficients(morphism(original))
            return target.linear_combination(
                {
                    target_label: self._target_ring(
                        self.ring_map()(coefficient)
                    )
                    for target_label, coefficient in coefficients.items()
                }
            )

        hom = source.module_category().Mor(source, target)
        return _ScalarExtensionModuleMorphism(
            hom,
            morphism,
            image,
            self,
        )

    def _repr_(self):
        return f"Scalar extension along {self.ring_map()}"


class _RestrictionOfScalarsFunctor(Functor):
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
    # action was stated on, and elements pass to it by coercion.  Along any
    # other map the image is the restricted-scalars view.

    def _restricts_group_modules(self) -> bool:
        return self._target_ring in GroupAlgebras(self._source_ring)

    def _apply_object(self, module):
        if self._restricts_group_modules():
            return module.unformed_module()
        return module.restrict_scalars(self.ring_map())

    def _restricted_element(self, source_module, restricted, element):
        r"""Read an element of ``source_module`` in its restriction ``restricted``."""
        return restricted(element)

    def _extension_element(self, source_module, restricted, element):
        r"""Read an element of ``restricted`` back in ``source_module``."""
        if self._restricts_group_modules():
            return source_module(element)
        return element.underlying_element()

    def _apply_morphism(self, morphism):
        # Restriction changes which ring acts and never the underlying map, so
        # ``Res_f(g)`` is ``g``: its element action is the original one read
        # through the restricted parents, and its ``R``-linearity is the
        # ``S``-linearity of ``g`` along ``f``, not a runtime condition.  A
        # framing of the source is therefore not part of the statement.
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return _RestrictionModuleMorphism(
            source.module_category().Mor(source, target),
            morphism,
            lambda element: self._restricted_element(
                morphism.codomain(),
                target,
                morphism(
                    self._extension_element(morphism.domain(), source, element)
                ),
            ),
        )

    def _repr_(self):
        return f"Restriction of scalars along {self.ring_map()}"


class _CoextensionOfScalarsFunctor(Functor):
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
        return scalars.module_category().Mor(scalars, scalars)(
            {
                label: scalars.module_generator(label) * scalar
                for label in scalars.module_generating_set()
            }
        )

    # A coextended module over a group algebra is a group module built on
    # ``Hom_R(S, M)``, whose elements pass to it by coercion; over any other
    # ring it is the general module built on ``Hom_R(S, M)``.

    def _coextends_to_group_modules(self) -> bool:
        return self._target_ring in GroupAlgebras(self._source_ring)

    def _hom_element(self, coextended, element):
        r"""Read an element of ``Hom_R(S, M)`` off the coextended module."""
        if self._coextends_to_group_modules():
            return coextended.unformed_module()(element)
        return element.underlying_element()

    def _coextended_element(self, coextended, hom_element):
        return coextended(hom_element)

    def _linear_map(self, domain, codomain, function):
        r"""The ``S``-linear map given elementwise by ``function``."""
        if self._coextends_to_group_modules():
            source_module = domain.unformed_module()
            target_module = codomain.unformed_module()
            underlying = _ScalarChangeStructureMorphism(
                source_module.module_category().Mor(source_module, target_module),
                lambda element: target_module(function(domain(element))),
                elementwise=True,
            )
            return domain.Mor(codomain)._from_equivariant_images(underlying)
        return _ScalarChangeStructureMorphism(domain.module_category().Mor(domain, codomain), function, elementwise=True)

    def _apply_object(self, module):
        scalars = self.scalars_as_module()
        hom = scalars.module_category().Mor(scalars, module)
        identity = module.module_category().Mor(module, module).identity()
        endomorphisms = Modules(self._source_ring).End(hom)
        action = self._target_ring.Mor(endomorphisms)(
            lambda scalar: self._right_multiplication(scalar).internal_hom_map(
                identity,
                source_internal_hom=hom,
                target_internal_hom=hom,
            ),
        )
        return Modules(self._target_ring)(hom, action)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        scalars = self.scalars_as_module()
        identity = scalars.module_category().Mor(scalars, scalars).identity()
        postcomposition = identity.internal_hom_map(
            morphism,
            source_internal_hom=scalars.module_category().Mor(
                scalars, morphism.domain()
            ),
            target_internal_hom=scalars.module_category().Mor(
                scalars, morphism.codomain()
            ),
        )
        if self._coextends_to_group_modules():
            return source.Mor(target)._from_equivariant_images(postcomposition)
        return _CoextensionFunctorImageMorphism(
            source.module_category().Mor(source, target),
            postcomposition,
            lambda element: self._coextended_element(
                target,
                postcomposition(self._hom_element(source, element)),
            ),
        )

    def _repr_(self):
        return f"Coextension of scalars along {self.ring_map()}"


class _BaseChangeAdjunction(Adjunction):
    r"""``S tensor_R - ⊣ Res_f``."""

    _extension_functor = _ScalarExtensionFunctor
    _restriction_functor = _RestrictionOfScalarsFunctor

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        super().__init__(
            self._extension_functor(ring_map),
            self._restriction_functor(ring_map),
        )

    def unit(self, module):
        extended = self.left_adjoint()(module)
        restricted = self.right_adjoint()(extended)
        return module.module_category().Mor(module, restricted)(
            lambda label: restricted(extended.module_generator(label))
        )

    def counit(self, module):
        restricted = self.right_adjoint()(module)
        extended = self.left_adjoint()(restricted)
        return extended.module_category().Mor(extended, module)(
            lambda label: restricted.module_generator(label).underlying_element()
        )


    def _repr_(self):
        return f"Scalar-extension/restriction adjunction along {self._ring_map}"


class _RestrictionCoextensionAdjunction(Adjunction):
    r"""``Res_f ⊣ Hom_R(S, -)``.

    The unit sends ``n`` to ``s |-> s n`` and the counit evaluates at ``1``.
    """

    _restriction_functor = _RestrictionOfScalarsFunctor
    _coextension_functor = _CoextensionOfScalarsFunctor

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
        hom = scalars.module_category().Mor(scalars, restricted)

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
        return _ScalarChangeStructureMorphism(
            restricted.module_category().Mor(restricted, module),
            lambda element: self.right_adjoint()._hom_element(
                coextended, self.left_adjoint()._extension_element(restricted, element)
            )(one),
            elementwise=True,
        )

    def _repr_(self):
        return f"Restriction/coextension adjunction along {self._ring_map}"


@cached_function
def _base_change_adjunction(ring_map) -> _BaseChangeAdjunction:
    return _BaseChangeAdjunction(ring_map)


@cached_function
def _restriction_coextension_adjunction(ring_map) -> _RestrictionCoextensionAdjunction:
    return _RestrictionCoextensionAdjunction(ring_map)
