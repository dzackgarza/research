r"""The tensor--internal-Hom adjunction for finitely presented modules."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    FinitelyPresentedModules,
)
from dzack_research.preamble.categories.modules.internal_hom import (
    InternalHom,
    internal_hom_morphism,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.abstract_categories import TensorProduct
from dzack_research.preamble.categories.modules.tensor_products import (
    BilinearMap,
    tensor_product_morphism,
)
from dzack_research.preamble.categories.rings import owned_ring_view


class TensorByFunctor(Functor):
    r"""The endofunctor ``- tensor_R M`` on finitely presented modules."""

    def __init__(self, fixed_module) -> None:
        self._fixed_module = fixed_module
        ring = owned_ring_view(fixed_module.base_ring())
        category = FinitelyPresentedModules(ring)
        if fixed_module not in category:
            raise TypeError("the fixed tensor factor must be finitely presented")
        super().__init__(category, category)

    def fixed_module(self):
        return self._fixed_module

    def _apply_object(self, module):
        return TensorProduct(module, self.fixed_module())

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        identity = module_homset(self.fixed_module(), self.fixed_module()).identity()
        return tensor_product_morphism(
            morphism,
            identity,
            source=source,
            target=target,
        )

    def _repr_(self):
        return f"- tensor {self.fixed_module()}"


class InternalHomFromFunctor(Functor):
    r"""The endofunctor ``Hom_R(M,-)`` represented by internal Hom modules."""

    def __init__(self, fixed_source) -> None:
        self._fixed_source = fixed_source
        ring = owned_ring_view(fixed_source.base_ring())
        category = FinitelyPresentedModules(ring)
        if fixed_source not in category:
            raise TypeError("the fixed internal-Hom source must be finitely presented")
        super().__init__(category, category)

    def fixed_source(self):
        return self._fixed_source

    def _apply_object(self, module):
        return InternalHom(self.fixed_source(), module)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        identity = module_homset(self.fixed_source(), self.fixed_source()).identity()
        return internal_hom_morphism(
            source,
            target,
            identity,
            morphism,
        )

    def _repr_(self):
        return f"Internal Hom({self.fixed_source()}, -)"


class TensorHomAdjunction(Adjunction):
    r"""The adjunction ``- tensor_R M ⊣ Hom_R(M,-)``."""

    def __init__(self, fixed_module) -> None:
        self._fixed_module = fixed_module
        super().__init__(
            TensorByFunctor(fixed_module),
            InternalHomFromFunctor(fixed_module),
        )

    def fixed_module(self):
        return self._fixed_module

    def hom_set_isomorphism_forward(self, tensor_morphism):
        r"""Curry ``A tensor M -> N`` to ``A -> Hom(M,N)``."""
        tensor_source = tensor_morphism.domain()
        left, fixed = tensor_source.tensor_factors()
        if fixed is not self.fixed_module():
            raise ValueError("the morphism domain has the wrong fixed tensor factor")
        internal_hom = self.right_adjoint()(tensor_morphism.codomain())
        return module_homset(left, internal_hom)(
            {
                left_label: module_homset(
                    self.fixed_module(), tensor_morphism.codomain()
                )(
                    {
                        fixed_label: tensor_morphism(
                            tensor_source.pure_tensor(
                                left.module_generator(left_label),
                                self.fixed_module().module_generator(fixed_label),
                            )
                        )
                        for fixed_label in self.fixed_module().module_generating_set()
                    }
                )
                for left_label in left.module_generating_set()
            }
        )

    def hom_set_isomorphism_inverse(self, internal_hom_morphism, codomain=None):
        r"""Uncurry ``A -> Hom(M,N)`` to ``A tensor M -> N``."""
        internal_hom = internal_hom_morphism.codomain()
        if internal_hom.source_module() is not self.fixed_module():
            raise ValueError("the internal Hom has the wrong fixed source")
        target = internal_hom.target_module()
        if codomain is not None and codomain is not target:
            raise ValueError("the stated codomain is not the internal-Hom target")
        left = internal_hom_morphism.domain()
        tensor = self.left_adjoint()(left)
        bilinear = BilinearMap(
            left,
            self.fixed_module(),
            target,
            {
                (left_label, fixed_label): internal_hom_morphism(
                    left.module_generator(left_label)
                )(
                    self.fixed_module().module_generator(fixed_label)
                )
                for left_label in left.module_generating_set()
                for fixed_label in self.fixed_module().module_generating_set()
            },
        )
        return tensor.from_bilinear(bilinear)

    def unit(self, module):
        tensor = self.left_adjoint()(module)
        internal_hom = self.right_adjoint()(tensor)
        return module_homset(module, internal_hom)(
            {
                module_label: module_homset(self.fixed_module(), tensor)(
                    {
                        fixed_label: tensor.pure_tensor(
                            module.module_generator(module_label),
                            self.fixed_module().module_generator(fixed_label),
                        )
                        for fixed_label in self.fixed_module().module_generating_set()
                    }
                )
                for module_label in module.module_generating_set()
            }
        )

    def counit(self, module):
        internal_hom = self.right_adjoint()(module)
        tensor = self.left_adjoint()(internal_hom)
        evaluation = BilinearMap(
            internal_hom,
            self.fixed_module(),
            module,
            {
                (hom_label, fixed_label): internal_hom.module_generator(hom_label)(
                    self.fixed_module().module_generator(fixed_label)
                )
                for hom_label in internal_hom.module_generating_set()
                for fixed_label in self.fixed_module().module_generating_set()
            },
        )
        return tensor.from_bilinear(evaluation)

    def _repr_(self):
        return f"Tensor/internal-Hom adjunction with {self.fixed_module()}"


@cached_function
def tensor_hom_adjunction(fixed_module) -> TensorHomAdjunction:
    return TensorHomAdjunction(fixed_module)


__all__ = [
    "InternalHomFromFunctor",
    "TensorByFunctor",
    "TensorHomAdjunction",
    "tensor_hom_adjunction",
]
