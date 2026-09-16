r"""Free bilinear/quadratic formed objects and their forgetful adjunctions."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    BilinearFormModules,
    FormedModuleMorphism,
    FormModules,
    QuadraticFormModules,
    _represented_value_module,
    _value_as_module_element,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import BilinearMap, FinitelyPresentedModules, Modules

from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring


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


class _ForgetTheFormFunctor(_UnderlyingFormModuleFunctor):
    r"""Forget the selected form from one represented formed-module category."""

    _faithful = True

    def __init__(self, base_ring, formed_category) -> None:
        ring = _owned_ring(base_ring)

        super().__init__(formed_category, Modules(ring))


class _BilinearUnderlyingModuleFunctor(_UnderlyingFormModuleFunctor):
    def __init__(self, base_ring) -> None:
        ring = _owned_ring(base_ring)
        self._base_ring = ring
        super().__init__(
            BilinearFormModules(ring).FinitelyPresented(),
            FinitelyPresentedModules(ring),
        )

    def base_ring(self):
        return self._base_ring

    def _repr_(self):
        return f"Underlying-module functor on bilinear formed {self.base_ring()}-modules"


class _QuadraticUnderlyingModuleFunctor(_UnderlyingFormModuleFunctor):
    def __init__(self, base_ring) -> None:
        ring = _owned_ring(base_ring)
        self._base_ring = ring
        super().__init__(
            QuadraticFormModules(ring).FinitelyPresented(),
            FinitelyPresentedModules(ring),
        )

    def base_ring(self):
        return self._base_ring

    def _repr_(self):
        return f"Underlying-module functor on quadratic formed {self.base_ring()}-modules"


class _FreeBilinearFormFunctor(Functor):
    r"""Send ``M`` to ``(M, M tensor M, universal pure tensor)``."""

    def __init__(self, base_ring) -> None:
        ring = _owned_ring(base_ring)
        self._base_ring = ring
        super().__init__(
            FinitelyPresentedModules(ring),
            BilinearFormModules(ring).FinitelyPresented(),
        )

    def base_ring(self):
        return self._base_ring

    def _repr_(self):
        return f"Free bilinear-form functor on {self.base_ring()}-modules"

    def _apply_object(self, module):

        classifier = Modules(self.base_ring()).tensor_product((module, module))
        formed = FormModules(module.base_ring())(
            module.bilinear_forms(classifier)(
                lambda left, right: classifier.pure_tensor(left, right)
            )
        )
        return formed

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        module_map = (
            target.equip_form_morphism()
            * morphism
            * source.forget_form_morphism()
        )
        value_map = morphism.tensor_product_map(
            morphism,
            source=source.value_module(),
            target=target.value_module(),
        )
        return source.Mor(target)((module_map, value_map))


class _FreeQuadraticFormFunctor(Functor):
    r"""Send ``M`` to ``(M, Gamma^2(M), gamma_2)``."""

    def __init__(self, base_ring) -> None:
        ring = _owned_ring(base_ring)
        self._base_ring = ring
        super().__init__(
            FinitelyPresentedModules(ring),
            QuadraticFormModules(ring).FinitelyPresented(),
        )

    def base_ring(self):
        return self._base_ring

    def _repr_(self):
        return f"Free quadratic-form functor on {self.base_ring()}-modules"

    def _apply_object(self, module):

        classifier = module.divided_square()
        formed = FormModules(module.base_ring())(
            module.quadratic_map(classifier, classifier.quadratic)
        )
        return formed

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        module_map = (
            target.equip_form_morphism()
            * morphism
            * source.forget_form_morphism()
        )
        value_map = morphism.divided_square()
        return source.Mor(target)((module_map, value_map))


class _TautologicalFormFunctor(Functor):
    r"""Abstract base for a free form classified by a functorial square."""

    def _classifying_square(self, module):
        raise NotImplementedError("a tautological form functor must supply its classifier")


class _FreeFormAdjunction(Adjunction):
    def _repr_(self):
        return f"{self.left_adjoint()} ⊣ {self.right_adjoint()}"

    def unit(self, module):
        return self.left_adjoint()(module).equip_form_morphism()

    def _counit_value_map(self, free_formed, formed):
        raise NotImplementedError("a free-form adjunction must classify the target form")

    def counit(self, formed):
        free_formed = self.left_adjoint()(self.right_adjoint()(formed))
        return free_formed.Mor(formed)(
            (
                free_formed.forget_form_morphism(),
                self._counit_value_map(free_formed, formed),
            )
        )


class _BilinearFreeFormAdjunction(_FreeFormAdjunction):
    r"""The tautological bilinear-form classifier adjunction."""

    def __init__(self, base_ring) -> None:
        super().__init__(
            _FreeBilinearFormFunctor(base_ring),
            _BilinearUnderlyingModuleFunctor(base_ring),
        )

    def _counit_value_map(self, free_formed, formed):
        module = self.right_adjoint()(formed)
        target_values = _represented_value_module(formed)
        bilinear = BilinearMap(
            module,
            module,
            target_values,
            lambda left_label, right_label: _value_as_module_element(
                formed,
                formed.b(
                    module.module_generator(left_label),
                    module.module_generator(right_label),
                ),
            ),
        )
        return free_formed.value_module().from_bilinear(bilinear)


class _QuadraticFreeFormAdjunction(_FreeFormAdjunction):
    r"""The divided-square quadratic-form classifier adjunction."""

    def __init__(self, base_ring) -> None:
        super().__init__(
            _FreeQuadraticFormFunctor(base_ring),
            _QuadraticUnderlyingModuleFunctor(base_ring),
        )

    def _counit_value_map(self, free_formed, formed):
        self.right_adjoint()(formed)
        target_values = _represented_value_module(formed)
        return free_formed.value_module().from_quadratic(
            lambda element: _value_as_module_element(
                formed,
                formed.norm(element),
            ),
            target_values,
        )


@cached_function
def _bilinear_free_form_adjunction(base_ring) -> _BilinearFreeFormAdjunction:
    return _BilinearFreeFormAdjunction(base_ring)


@cached_function
def _quadratic_free_form_adjunction(base_ring) -> _QuadraticFreeFormAdjunction:
    return _QuadraticFreeFormAdjunction(base_ring)


__all__ = []
