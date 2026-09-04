r"""Direct and inverse image on fixed-ambient module subobject categories."""

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.abstract_categories.constructions import Subobjects
from dzack_research.preamble.categories.abstract_categories.constructions import Biproduct


def _inverse_image_subobject(morphism, subobject):
    r"""Construct the pullback/preimage as the source image of ``ker(f,-i)``."""
    if subobject.inclusion().codomain() is not morphism.codomain():
        raise ValueError("the subobject is not in the morphism codomain")

    direct_sum = Biproduct(morphism.domain(), subobject)
    difference = direct_sum.from_summands(morphism, -subobject.inclusion())
    kernel = difference.kernel()
    return (direct_sum.left_projection() * kernel.inclusion()).image()


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
        return self.codomain().Mor(
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
        return self.codomain().Mor(
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


    def unit(self, subobject):
        target = self.right_adjoint()(self.left_adjoint()(subobject))
        return self.left_adjoint().domain().Mor(subobject, target).canonical_morphism()

    def counit(self, subobject):
        source = self.left_adjoint()(self.right_adjoint()(subobject))
        return self.left_adjoint().codomain().Mor(source, subobject).canonical_morphism()


def subobject_image_adjunction(morphism) -> SubobjectImageAdjunction:
    return SubobjectImageAdjunction(morphism)


__all__ = [
    "DirectImageSubobjectFunctor",
    "InverseImageSubobjectFunctor",
    "SubobjectImageAdjunction",
    "subobject_image_adjunction",
]
