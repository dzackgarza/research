r"""Free bilinear/quadratic formed objects and their forgetful adjunctions."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    FinitelyPresentedBilinearFormModules,
    FinitelyPresentedQuadraticFormModules,
    FormModule,
    FormedModuleMorphism,
    _represented_value_module,
    _value_as_module_element,
    formed_module_homset,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    FinitelyPresentedModules,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    module_homset,
)
from dzack_research.preamble.categories.modules.quadratic_square import (
    DividedSquare,
    divided_square_morphism,
)
from dzack_research.preamble.categories.abstract_categories import TensorSquare
from dzack_research.preamble.categories.modules.tensor_products import (
    BilinearMap,
    tensor_product_morphism,
)
from dzack_research.preamble.categories.rings import owned_ring_view


class _UnderlyingFormModuleFunctor(Functor):
    r"""Forget the selected form while retaining the module object itself."""

    def _apply_object(self, formed):
        return formed

    def _apply_morphism(self, morphism):
        if isinstance(morphism, FormedModuleMorphism):
            return morphism.module_morphism()
        if isinstance(morphism, ModuleMorphism):
            return morphism
        raise TypeError("a formed-module morphism must carry an underlying module map")


class ForgetTheFormFunctor(_UnderlyingFormModuleFunctor):
    r"""Forget the selected form from one represented formed-module category."""

    _faithful = True

    def __init__(self, base_ring, formed_category) -> None:
        ring = owned_ring_view(base_ring)
        from dzack_research.preamble.categories.modules import Modules

        super().__init__(formed_category, Modules(ring))


class BilinearUnderlyingModuleFunctor(_UnderlyingFormModuleFunctor):
    def __init__(self, base_ring) -> None:
        ring = owned_ring_view(base_ring)
        super().__init__(
            FinitelyPresentedBilinearFormModules(ring),
            FinitelyPresentedModules(ring),
        )


class QuadraticUnderlyingModuleFunctor(_UnderlyingFormModuleFunctor):
    def __init__(self, base_ring) -> None:
        ring = owned_ring_view(base_ring)
        super().__init__(
            FinitelyPresentedQuadraticFormModules(ring),
            FinitelyPresentedModules(ring),
        )


class FreeBilinearFormFunctor(Functor):
    r"""Send ``M`` to ``(M, M tensor M, universal pure tensor)``."""

    def __init__(self, base_ring) -> None:
        ring = owned_ring_view(base_ring)
        super().__init__(
            FinitelyPresentedModules(ring),
            FinitelyPresentedBilinearFormModules(ring),
        )

    def _apply_object(self, module):
        from dzack_research.preamble.categories.forms import BilinearForms

        classifier = TensorSquare(module)
        formed = FormModule(
            BilinearForms(module, classifier)(
                lambda left, right: classifier.pure_tensor(left, right)
            )
        )
        formed._preamble_form_classifier = classifier
        return formed

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        module_map = (
            target.equip_form_morphism()
            * morphism
            * source.forget_form_morphism()
        )
        value_map = tensor_product_morphism(
            morphism,
            morphism,
            source=source.value_module(),
            target=target.value_module(),
        )
        return formed_module_homset(source, target)((module_map, value_map))


class FreeQuadraticFormFunctor(Functor):
    r"""Send ``M`` to ``(M, Gamma^2(M), gamma_2)``."""

    def __init__(self, base_ring) -> None:
        ring = owned_ring_view(base_ring)
        super().__init__(
            FinitelyPresentedModules(ring),
            FinitelyPresentedQuadraticFormModules(ring),
        )

    def _apply_object(self, module):
        from dzack_research.preamble.categories.forms import QuadraticForms

        classifier = DividedSquare(module)
        formed = FormModule(
            QuadraticForms(module, classifier)(classifier.quadratic)
        )
        formed._preamble_form_classifier = classifier
        return formed

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        module_map = (
            target.equip_form_morphism()
            * morphism
            * source.forget_form_morphism()
        )
        value_map = divided_square_morphism(
            morphism,
            source=source.value_module(),
            target=target.value_module(),
        )
        return formed_module_homset(source, target)((module_map, value_map))


class TautologicalFormFunctor(Functor):
    r"""Abstract base for a free form classified by a functorial square."""

    def _classifying_square(self, module):
        raise NotImplementedError("a tautological form functor must supply its classifier")


TautologicalBilinearFormFunctor = FreeBilinearFormFunctor
TautologicalQuadraticFormFunctor = FreeQuadraticFormFunctor


class _FreeFormAdjunction(Adjunction):
    def unit(self, module):
        return self.left_adjoint()(module).equip_form_morphism()

    def counit(self, formed):
        identity = module_homset(formed, formed).identity()
        return self.hom_set_isomorphism_inverse(identity, formed)


FormForgetfulAdjunction = _FreeFormAdjunction


class BilinearFreeFormAdjunction(_FreeFormAdjunction):
    r"""The tautological bilinear-form classifier adjunction."""

    def __init__(self, base_ring) -> None:
        super().__init__(
            FreeBilinearFormFunctor(base_ring),
            BilinearUnderlyingModuleFunctor(base_ring),
        )

    def hom_set_isomorphism_forward(self, formed_morphism):
        if not isinstance(formed_morphism, FormedModuleMorphism):
            raise TypeError("the bilinear transpose starts from a general formed morphism")
        source = formed_morphism.domain()
        return formed_morphism.module_morphism() * source.equip_form_morphism()

    def hom_set_isomorphism_inverse(self, module_morphism, codomain=None):
        formed_target = module_morphism.codomain()
        if codomain is not None and codomain is not formed_target:
            raise ValueError("the stated codomain differs from the formed target")
        source_module = module_morphism.domain()
        free_formed = self.left_adjoint()(source_module)
        target_values = _represented_value_module(formed_target)
        target_form = formed_target.form()
        bilinear = BilinearMap(
            source_module,
            source_module,
            target_values,
            {
                (left_label, right_label): _value_as_module_element(
                    formed_target,
                    target_form(
                        module_morphism(source_module.module_generator(left_label)),
                        module_morphism(source_module.module_generator(right_label)),
                    ),
                )
                for left_label in source_module.module_generating_set()
                for right_label in source_module.module_generating_set()
            },
        )
        value_map = free_formed.value_module().from_bilinear(bilinear)
        underlying_map = module_morphism * free_formed.forget_form_morphism()
        return formed_module_homset(free_formed, formed_target)(
            (underlying_map, value_map)
        )


class QuadraticFreeFormAdjunction(_FreeFormAdjunction):
    r"""The divided-square quadratic-form classifier adjunction."""

    def __init__(self, base_ring) -> None:
        super().__init__(
            FreeQuadraticFormFunctor(base_ring),
            QuadraticUnderlyingModuleFunctor(base_ring),
        )

    def hom_set_isomorphism_forward(self, formed_morphism):
        if not isinstance(formed_morphism, FormedModuleMorphism):
            raise TypeError("the quadratic transpose starts from a general formed morphism")
        source = formed_morphism.domain()
        return formed_morphism.module_morphism() * source.equip_form_morphism()

    def hom_set_isomorphism_inverse(self, module_morphism, codomain=None):
        formed_target = module_morphism.codomain()
        if codomain is not None and codomain is not formed_target:
            raise ValueError("the stated codomain differs from the formed target")
        source_module = module_morphism.domain()
        free_formed = self.left_adjoint()(source_module)
        target_values = _represented_value_module(formed_target)
        target_form = formed_target.form()
        value_map = free_formed.value_module().from_quadratic(
            lambda element: _value_as_module_element(
                formed_target,
                target_form(module_morphism(element)),
            ),
            target_values,
        )
        underlying_map = module_morphism * free_formed.forget_form_morphism()
        return formed_module_homset(free_formed, formed_target)(
            (underlying_map, value_map)
        )


BilinearFormForgetfulAdjunction = BilinearFreeFormAdjunction
QuadraticFormForgetfulAdjunction = QuadraticFreeFormAdjunction


@cached_function
def bilinear_free_form_adjunction(base_ring) -> BilinearFreeFormAdjunction:
    return BilinearFreeFormAdjunction(base_ring)


@cached_function
def quadratic_free_form_adjunction(base_ring) -> QuadraticFreeFormAdjunction:
    return QuadraticFreeFormAdjunction(base_ring)


__all__ = [
    "BilinearFreeFormAdjunction",
    "BilinearFormForgetfulAdjunction",
    "BilinearUnderlyingModuleFunctor",
    "FreeBilinearFormFunctor",
    "FreeQuadraticFormFunctor",
    "ForgetTheFormFunctor",
    "FormForgetfulAdjunction",
    "QuadraticFreeFormAdjunction",
    "QuadraticFormForgetfulAdjunction",
    "QuadraticUnderlyingModuleFunctor",
    "TautologicalBilinearFormFunctor",
    "TautologicalFormFunctor",
    "TautologicalQuadraticFormFunctor",
    "bilinear_free_form_adjunction",
    "quadratic_free_form_adjunction",
]
