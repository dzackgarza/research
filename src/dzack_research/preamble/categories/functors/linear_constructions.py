r"""Duality, arrow kernels/cokernels, and additive/form biproduct functors."""

from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.abstract_categories.functors import Bifunctor, ContravariantFunctor
from dzack_research.preamble.categories.abstract_categories.arrow_categories import ArrowCategory
from dzack_research.preamble.categories.abstract_categories.constructions import (
    Biproduct,
    Cokernel,
    Kernel,
)
from dzack_research.preamble.categories.modules.pure.modules import biproduct_morphism
from dzack_research.preamble.categories.modules.pure.modules import FinitelyGeneratedFreeModules
from dzack_research.preamble.categories.modules.pure.modules import FinitelyPresentedModules
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring
from dzack_research.preamble.categories.lattice_morphisms import lattice_homset
from dzack_research.preamble.categories.lattices import Lattices


class DualizationFunctor(ContravariantFunctor):
    r"""Finite-free duality ``(-)^* : C^op -> C``."""

    def __init__(self, base_ring) -> None:
        category = FinitelyGeneratedFreeModules(_owned_ring(base_ring))
        super().__init__(category, category)

    def _apply_contravariant_object(self, module):
        return module.dual_module()

    def _apply_contravariant_morphism(self, morphism):
        source_dual = self(morphism.codomain())
        target_dual = self(morphism.domain())
        images = {}
        for codomain_label in morphism.codomain().module_generating_set():
            coefficients = {}
            for domain_label in morphism.domain().module_generating_set():
                image_coefficients = module_coefficients(
                    morphism(morphism.domain().module_generator(domain_label)),
                    morphism.codomain(),
                )
                coefficient = image_coefficients.get(
                    codomain_label, morphism.domain().base_ring().zero()
                )
                if coefficient:
                    coefficients[domain_label] = coefficient
            images[codomain_label] = target_dual.linear_combination(coefficients)
        return module_homset(source_dual, target_dual)(images)

    def double_dual_morphism(self, module):
        r"""Return the canonical finite-free biduality map ``M -> M**``."""
        double_dual = self(self(module))
        return module_homset(module, double_dual)(
            {
                label: double_dual.module_generator(label)
                for label in module.module_generating_set()
            }
        )


class BiproductBifunctor(Bifunctor):
    r"""The direct-sum/biproduct bifunctor on finitely presented modules."""

    def __init__(self, base_ring) -> None:
        category = FinitelyPresentedModules(_owned_ring(base_ring))
        super().__init__(category, category, category)

    def _apply_pair_object(self, left, right):
        return Biproduct(left, right)

    def _apply_pair_morphism(self, left_morphism, right_morphism):
        return biproduct_morphism(
            left_morphism,
            right_morphism,
            source=self(left_morphism.domain(), right_morphism.domain()),
            target=self(left_morphism.codomain(), right_morphism.codomain()),
        )


class _ArrowConstructionFunctor(Functor):
    r"""A functor out of the genuine arrow category of a represented category."""

    def __init__(self, object_category, codomain) -> None:
        super().__init__(ArrowCategory(object_category), codomain)


class KernelArrowFunctor(_ArrowConstructionFunctor):
    r"""The kernel functor from the finite-free module arrow category."""

    def __init__(self, base_ring) -> None:
        ring = _owned_ring(base_ring)
        finite_free = FinitelyGeneratedFreeModules(ring)
        super().__init__(finite_free, finite_free)

    def _apply_object(self, arrow_object):
        return Kernel(arrow_object.arrow())

    def _apply_morphism(self, square):
        source_kernel = self(square.domain())
        target_kernel = self(square.codomain())
        return module_homset(source_kernel, target_kernel)(
            {
                label: target_kernel.inclusion().lift(
                    square.left()(
                        source_kernel.inclusion()(source_kernel.module_generator(label))
                    )
                )
                for label in source_kernel.module_generating_set()
            }
        )


class CokernelArrowFunctor(_ArrowConstructionFunctor):
    r"""The cokernel functor from the finite-free module arrow category."""

    def __init__(self, base_ring) -> None:
        ring = _owned_ring(base_ring)
        category = FinitelyPresentedModules(ring)
        super().__init__(category, category)

    def _apply_object(self, arrow_object):
        return Cokernel(arrow_object.arrow())

    def _apply_morphism(self, square):
        source_cokernel = self(square.domain())
        target_cokernel = self(square.codomain())
        target_projection = target_cokernel.cokernel_projection()
        return module_homset(source_cokernel, target_cokernel)(
            {
                label: target_projection(
                    square.right()(
                        square.domain().arrow().codomain().module_generator(label)
                    )
                )
                for label in source_cokernel.module_generating_set()
            }
        )


class OrthogonalDirectSumBifunctor(Bifunctor):
    r"""The orthogonal-direct-sum bifunctor on finite-rank lattices."""

    def __init__(self, base_ring) -> None:

        category = Lattices(_owned_ring(base_ring))
        super().__init__(category, category, category)

    def _apply_pair_object(self, left, right):
        if not left.is_finite_rank() or not right.is_finite_rank():
            raise NotImplementedError("the active orthogonal-sum bifunctor uses finite concatenated bases")
        return left + right

    @staticmethod
    def _embed_summand(element, summand, target, offset):
        coefficients = module_coefficients(element, summand)
        summand_labels = summand.module_generating_set()
        target_labels = target.module_generating_set()
        return target.linear_combination(
            {
                target_labels.unrank(offset + int(summand_labels.rank(label))): coefficient
                for label, coefficient in coefficients.items()
            }
        )

    def _apply_pair_morphism(self, left_morphism, right_morphism):

        source = self(left_morphism.domain(), right_morphism.domain())
        target = self(left_morphism.codomain(), right_morphism.codomain())
        source_labels = source.module_generating_set()
        left_source_labels = left_morphism.domain().module_generating_set()
        right_source_labels = right_morphism.domain().module_generating_set()
        left_source_rank = int(left_source_labels.cardinality())
        left_target_rank = int(left_morphism.codomain().module_generating_set().cardinality())

        def image(source_label):
            position = int(source_labels.rank(source_label))
            if position < left_source_rank:
                label = left_source_labels.unrank(position)
                return self._embed_summand(
                    left_morphism(left_morphism.domain().module_generator(label)),
                    left_morphism.codomain(),
                    target,
                    0,
                )
            label = right_source_labels.unrank(position - left_source_rank)
            return self._embed_summand(
                right_morphism(right_morphism.domain().module_generator(label)),
                right_morphism.codomain(),
                target,
                left_target_rank,
            )

        return lattice_homset(source, target)(image)


__all__ = [
    "BiproductBifunctor",
    "CokernelArrowFunctor",
    "DualizationFunctor",
    "KernelArrowFunctor",
    "OrthogonalDirectSumBifunctor",
]
