r"""Direct and inverse image on fixed-ambient module subobject categories."""

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.abstract_categories import Subobjects
from dzack_research.preamble.categories.modules.subobjects import _element_from_row


def _inverse_image_subobject(morphism, subobject):
    r"""Construct the pullback/preimage subobject of ``subobject`` along ``morphism``."""
    if subobject.inclusion().codomain() is not morphism.codomain():
        raise ValueError("the subobject is not in the morphism codomain")
    source = morphism.domain()
    left = morphism.tensor().dual_tensor()
    right = subobject.inclusion().tensor().dual_tensor()
    from dzack_research.preamble.tensors import tensor

    stacked = tensor.matrix(left.base_ring(), left.stack(-right))
    kernel = tensor.matrix(left.base_ring(), stacked.left_kernel().basis_matrix())
    source_coefficients = tensor.matrix(
        left.base_ring(), kernel.matrix_from_columns(range(left.nrows()))
    )
    return source.subobject_on(
        _element_from_row(source, row)
        for row in source_coefficients.rows()
    )


class DirectImageSubobjectFunctor(Functor):
    r"""The monotone map ``f_* : Sub(M) -> Sub(N)``."""

    def __init__(self, morphism) -> None:
        self._morphism = morphism
        super().__init__(Subobjects(morphism.domain()), Subobjects(morphism.codomain()))

    def morphism(self):
        return self._morphism

    def _apply_object(self, subobject):
        return (self.morphism() * subobject.inclusion()).image()

    def _apply_morphism(self, order_morphism):
        return self.codomain().hom(
            self(order_morphism.domain()),
            self(order_morphism.codomain()),
        ).canonical_morphism()


class InverseImageSubobjectFunctor(Functor):
    r"""The monotone map ``f^{-1} : Sub(N) -> Sub(M)``."""

    def __init__(self, morphism) -> None:
        self._morphism = morphism
        super().__init__(Subobjects(morphism.codomain()), Subobjects(morphism.domain()))

    def morphism(self):
        return self._morphism

    def _apply_object(self, subobject):
        return _inverse_image_subobject(self.morphism(), subobject)

    def _apply_morphism(self, order_morphism):
        return self.codomain().hom(
            self(order_morphism.domain()),
            self(order_morphism.codomain()),
        ).canonical_morphism()


class SubobjectImageAdjunction(Adjunction):
    r"""The Galois connection ``f_* ⊣ f^{-1}`` on fixed-ambient subobjects."""

    def __init__(self, morphism) -> None:
        self._morphism = morphism
        super().__init__(
            DirectImageSubobjectFunctor(morphism),
            InverseImageSubobjectFunctor(morphism),
        )

    def hom_set_isomorphism_forward(self, order_morphism, source_subobject):
        r"""Transpose ``f_*(A) <= B`` to ``A <= f^{-1}(B)``.

        The indexed source ``A`` is explicit: direct image is not injective on
        objects, so it cannot be reconstructed from ``f_*(A)``.
        """
        direct_source = self.left_adjoint()(source_subobject)
        if order_morphism.domain() is not direct_source:
            raise ValueError("the order morphism does not start at the direct image of the stated source")
        original_target = order_morphism.codomain()
        inverse_target = self.right_adjoint()(original_target)
        return self.right_adjoint().codomain().hom(
            source_subobject, inverse_target
        ).canonical_morphism()

    def hom_set_isomorphism_inverse(self, order_morphism, codomain=None):
        r"""Transpose ``A <= f^{-1}(B)`` to ``f_*(A) <= B``.

        The indexed target ``B`` is explicit because inverse image is not
        injective on objects.
        """
        if codomain is None:
            raise TypeError("the target subobject is required for the inverse Hom-set transpose")
        original_source = order_morphism.domain()
        inverse_target = self.right_adjoint()(codomain)
        if order_morphism.codomain() is not inverse_target:
            raise ValueError("the order morphism does not land in the inverse image of the stated target")
        direct_source = self.left_adjoint()(original_source)
        return self.left_adjoint().codomain().hom(
            direct_source, codomain
        ).canonical_morphism()

    def unit(self, subobject):
        target = self.right_adjoint()(self.left_adjoint()(subobject))
        return self.left_adjoint().domain().hom(subobject, target).canonical_morphism()

    def counit(self, subobject):
        source = self.left_adjoint()(self.right_adjoint()(subobject))
        return self.left_adjoint().codomain().hom(source, subobject).canonical_morphism()


def subobject_image_adjunction(morphism) -> SubobjectImageAdjunction:
    return SubobjectImageAdjunction(morphism)


__all__ = [
    "DirectImageSubobjectFunctor",
    "InverseImageSubobjectFunctor",
    "SubobjectImageAdjunction",
    "subobject_image_adjunction",
]
