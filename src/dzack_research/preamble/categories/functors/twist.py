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
        source = self(morphism.domain())
        target = self(morphism.codomain())
        original_target = morphism.codomain()

        def image(label):
            original_image = morphism(
                morphism.domain().module_generator(label)
            )
            return target.linear_combination(
                original_target.framing_coefficients(original_image)
            )

        return source.Mor(target)(image)

    def _repr_(self):
        return f"Twist by {self.scale()}"


__all__ = ["TwistFunctor"]
