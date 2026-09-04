r"""The tensor--internal-Hom adjunction on modules with chosen finite presentations."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.modules.pure.modules import ModulesWithChosenFinitePresentation
from dzack_research.preamble.categories.modules.internal_hom import (
    InternalHom,
    internal_hom_morphism,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.abstract_categories.constructions import TensorProduct
from dzack_research.preamble.categories.modules.pure.modules import BilinearMap
from dzack_research.preamble.categories.modules.tensor_products import tensor_product_morphism
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring


class TensorByFunctor(Functor):
    r"""The endofunctor ``- tensor_R M`` on chosen finite presentations."""

    def __init__(self, fixed_module) -> None:
        self._fixed_module = fixed_module
        ring = _owned_ring(fixed_module.base_ring())
        category = ModulesWithChosenFinitePresentation(ring)
        if fixed_module not in category:
            raise TypeError("the fixed tensor factor must carry a chosen finite presentation")
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
        ring = _owned_ring(fixed_source.base_ring())
        category = ModulesWithChosenFinitePresentation(ring)
        if fixed_source not in category:
            raise TypeError("the fixed internal-Hom source must carry a chosen finite presentation")
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


    def unit(self, module):
        tensor = self.left_adjoint()(module)
        internal_hom = self.right_adjoint()(tensor)
        return module_homset(module, internal_hom)(
            lambda module_label: module_homset(self.fixed_module(), tensor)(
                lambda fixed_label: tensor.pure_tensor(
                    module.module_generator(module_label),
                    self.fixed_module().module_generator(fixed_label),
                )
            )
        )

    def counit(self, module):
        internal_hom = self.right_adjoint()(module)
        tensor = self.left_adjoint()(internal_hom)
        evaluation = BilinearMap(
            internal_hom,
            self.fixed_module(),
            module,
            lambda hom_label, fixed_label: internal_hom.module_generator(hom_label)(
                self.fixed_module().module_generator(fixed_label)
            ),
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
