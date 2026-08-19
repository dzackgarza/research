r"""The twist endofunctor \(L\mapsto L(a)\) of the integral-lattice category.

Nikulin's \(L(a)\): the same module with the bilinear form scaled by a fixed
nonzero integer \(a\) (Nikulin's notation).  An isometry-preserving operation on forms and
the identity on everything else -- \(A^tG_MA=G_L\) gives
\(A^t(aG_M)A=aG_L\), so a morphism's matrix does not move -- which is what
makes it a genuine endofunctor rather than a family of object methods.

The object action *is* the category method :meth:`twist` that every lattice
already has; the functor adds the morphism action and the categorical shape,
it does not add a second implementation of the scaling.
"""

from typing import TYPE_CHECKING

from dzack_research.preamble.categories.abstract_categories.functors import Functor
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ

if TYPE_CHECKING:
    from sage.categories.modules import Module
    from sage.categories.morphism import Morphism
    from dzack_research.preamble.lexicon import RingElement


class TwistFunctor(Functor):
    r"""\(L\mapsto L(a)\): the form scaled by \(a\), morphisms unchanged."""

    # Faithful by declaration: the morphism action keeps the matrix, so it
    # is injective on homsets.
    _faithful = True

    def __init__(self, scale: "RingElement") -> None:
        assert scale in SageZZ and scale != 0, (
            f"a twist scales the form by a nonzero integer; found {scale!r}. "
            "Scaling by 0 forgets the form rather than twisting it, and a "
            "non-integer scale leaves the integral-lattice category."
        )
        self._scale = SageZZ(scale)
        # Local: the lattice node imports the functors' package, so a
        # module-level import here would close that cycle; it is built by
        # call time.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices

        Functor.__init__(self, IntegralLattices(), IntegralLattices())

    def scale(self) -> "RingElement":
        return self._scale

    @cached_method
    def _apply_functor(self, lattice: "Module") -> "Module":
        r"""Return \(L(a)\), the same object on every call.

        Cached because a functor must be well defined on objects:
        \(F(\operatorname{dom}f)\) has to *be* the domain of \(F(f)\), not
        merely an isometric copy.  The scaling itself is the lattice's own
        :meth:`twist` -- one implementation, reached through the functor.
        """
        return lattice.twist(self._scale)

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        r"""Return the same matrix read between the twisted parents."""
        # Local: the utilities and lattice nodes are built by call time.
        from dzack_research.preamble.utilities import zipsum

        source, target = self(morphism.domain()), self(morphism.codomain())
        return source.Hom(target)(
            {
                label: zipsum(row, target.module_generators(), target.zero())
                for label, row in zip(
                    source.module_generating_set(),
                    morphism.matrix().rows(),
                )
            }
        )

    def _repr_(self) -> str:
        return f"Twist by {self._scale}"
