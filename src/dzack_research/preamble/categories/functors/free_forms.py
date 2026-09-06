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
from dzack_research.preamble.categories.modules.pure.modules import FinitelyPresentedModules
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    module_homset,
)
from dzack_research.preamble.categories.modules.powers import (
    DividedSquare,
    divided_square_morphism,
)
from dzack_research.preamble.categories.abstract_categories.constructions import TensorSquare
from dzack_research.preamble.categories.modules.pure.modules import BilinearMap
from dzack_research.preamble.categories.modules.tensor_products import tensor_product_morphism
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring
from dzack_research.preamble.categories.forms.forms import (
    BilinearForms,
    QuadraticMap,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules


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
        ring = _owned_ring(base_ring)

        super().__init__(formed_category, Modules(ring))


class BilinearUnderlyingModuleFunctor(_UnderlyingFormModuleFunctor):
    def __init__(self, base_ring) -> None:
        ring = _owned_ring(base_ring)
        self._base_ring = ring
        super().__init__(
            FinitelyPresentedBilinearFormModules(ring),
            FinitelyPresentedModules(ring),
        )

    def base_ring(self):
        return self._base_ring

    def _repr_(self):
        return f"Underlying-module functor on bilinear formed {self.base_ring()}-modules"


class QuadraticUnderlyingModuleFunctor(_UnderlyingFormModuleFunctor):
    def __init__(self, base_ring) -> None:
        ring = _owned_ring(base_ring)
        self._base_ring = ring
        super().__init__(
            FinitelyPresentedQuadraticFormModules(ring),
            FinitelyPresentedModules(ring),
        )

    def base_ring(self):
        return self._base_ring

    def _repr_(self):
        return f"Underlying-module functor on quadratic formed {self.base_ring()}-modules"


class FreeBilinearFormFunctor(Functor):
    r"""Send ``M`` to ``(M, M tensor M, universal pure tensor)``."""

    def __init__(self, base_ring) -> None:
        ring = _owned_ring(base_ring)
        self._base_ring = ring
        super().__init__(
            FinitelyPresentedModules(ring),
            FinitelyPresentedBilinearFormModules(ring),
        )

    def base_ring(self):
        return self._base_ring

    def _repr_(self):
        return f"Free bilinear-form functor on {self.base_ring()}-modules"

    def _apply_object(self, module):

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
        ring = _owned_ring(base_ring)
        self._base_ring = ring
        super().__init__(
            FinitelyPresentedModules(ring),
            FinitelyPresentedQuadraticFormModules(ring),
        )

    def base_ring(self):
        return self._base_ring

    def _repr_(self):
        return f"Free quadratic-form functor on {self.base_ring()}-modules"

    def _apply_object(self, module):

        classifier = DividedSquare(module)
        formed = FormModule(
            QuadraticMap(module, classifier, classifier.quadratic)
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
    def _repr_(self):
        return f"{self.left_adjoint()} ⊣ {self.right_adjoint()}"

    def unit(self, module):
        return self.left_adjoint()(module).equip_form_morphism()

    def _counit_value_map(self, free_formed, formed):
        raise NotImplementedError("a free-form adjunction must classify the target form")

    def counit(self, formed):
        free_formed = self.left_adjoint()(self.right_adjoint()(formed))
        return formed_module_homset(free_formed, formed)(
            (
                free_formed.forget_form_morphism(),
                self._counit_value_map(free_formed, formed),
            )
        )


FormForgetfulAdjunction = _FreeFormAdjunction


class BilinearFreeFormAdjunction(_FreeFormAdjunction):
    r"""The tautological bilinear-form classifier adjunction."""

    def __init__(self, base_ring) -> None:
        super().__init__(
            FreeBilinearFormFunctor(base_ring),
            BilinearUnderlyingModuleFunctor(base_ring),
        )

    def _counit_value_map(self, free_formed, formed):
        module = self.right_adjoint()(formed)
        target_values = _represented_value_module(formed)
        target_form = formed.form()
        bilinear = BilinearMap(
            module,
            module,
            target_values,
            lambda left_label, right_label: _value_as_module_element(
                formed,
                target_form(
                    module.module_generator(left_label),
                    module.module_generator(right_label),
                ),
            ),
        )
        return free_formed.value_module().from_bilinear(bilinear)


class QuadraticFreeFormAdjunction(_FreeFormAdjunction):
    r"""The divided-square quadratic-form classifier adjunction."""

    def __init__(self, base_ring) -> None:
        super().__init__(
            FreeQuadraticFormFunctor(base_ring),
            QuadraticUnderlyingModuleFunctor(base_ring),
        )

    def _counit_value_map(self, free_formed, formed):
        module = self.right_adjoint()(formed)
        target_values = _represented_value_module(formed)
        target_form = formed.form()
        return free_formed.value_module().from_quadratic(
            lambda element: _value_as_module_element(
                formed,
                target_form(element),
            ),
            target_values,
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
