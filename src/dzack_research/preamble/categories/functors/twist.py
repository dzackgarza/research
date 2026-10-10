r"""The lattice twist endofunctor ``L |-> L(a)``.

For a nonzero integer ``a``, the twist keeps the underlying framed module and
scales the symmetric bilinear form by ``a``.  A lattice morphism keeps the same
coordinate matrix, because ``A^t G_M A = G_L`` implies
``A^t (a G_M) A = a G_L``.  The object action delegates to the lattice owner's
existing :meth:`twist` implementation; this module adds only the categorical
morphism action required by the archived contract.
"""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


class TwistFunctor(Functor):
    r"""The faithful endofunctor ``L |-> L(a)`` of integral lattices."""

    _faithful = True

    def __init__(self, scale) -> None:
        integers = _own_ring(SageZZ)
        self._scale = integers(scale)
        if self._scale == integers.zero():
            raise ValueError(
                f"the twist L(n) of a lattice needs a nonzero integer n, but n = {scale}"
            )
        category = Lattices(integers)
        super().__init__(category, category)

    def scale(self):
        return self._scale

    def _apply_object(self, lattice):
        return lattice.twist(self.scale())

    def _apply_morphism(self, morphism):
        from dzack_research.preamble.categories.abstract_categories.mor_categories import CategoricalIsomorphism
        from dzack_research.preamble.categories.lattice_morphisms import (
            LatticeEmbeddingMethods,
            LatticeIsometryMethods,
        )

        source = self(morphism.domain())
        target = self(morphism.codomain())

        def transported(arrow, domain, codomain):
            def image(label):
                original_image = arrow(arrow.domain().module_generator(label))
                coordinates = arrow.codomain().framing_morphism().lift(original_image)
                return codomain.linear_combination(
                    {basis_label: coordinates(basis_label) for basis_label in coordinates.support().domain()}
                )

            return domain.module_category().Mor(domain, codomain)(image)

        forward = transported(morphism, source, target)
        if isinstance(morphism, (LatticeIsometryMethods, CategoricalIsomorphism)):
            backward = transported(morphism.inverse(), target, source)
            inverse_pair = source.module_category().Core().Mor(source, target)(forward, backward)
            return source.Isom(target)(inverse_pair)
        if isinstance(morphism, LatticeEmbeddingMethods):
            return source.Emb(target)(forward)
        return source.Mor(target)(forward)

    def _repr_(self):
        return f"Twist by {self.scale()}"


__all__ = ["TwistFunctor"]
