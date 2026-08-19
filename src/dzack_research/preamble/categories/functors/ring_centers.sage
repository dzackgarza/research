r"""\(Z:\operatorname{core}(\mathbf{Rings})\to\mathbf{CRings}\), the centre.

The centre is functorial on isomorphisms and on nothing wider.  An
isomorphism \(f:A\to B\) carries \(Z(A)\) onto \(Z(B)\): if \(z\) commutes
with all of \(A\) then \(f(z)\) commutes with all of \(f(A)=B\), and
\(f^{-1}\) carries the centre back.  A general ring map does not.  The
inclusion \(\QQ[t]\hookrightarrow\Lambda(F_\QQ\{e_1,e_2\})\) sending \(t\) to
\(e_1\) is the counterexample: \(t\) is central in \(\QQ[t]\), its image is
not central in \(\Lambda\), and there is no map \(Z(\QQ[t])\to Z(\Lambda)\)
extending it.

Surjections work as well -- \(f(A)=B\) is all the argument above uses -- and
are deliberately not modelled here: a surjection is a declared datum in this
preamble, and \(\operatorname{core}\) is the source the ratified design asks
for.  Widening the source to the epimorphisms is a separate declaration.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.rings.ring import Ring

    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Core,
    )

from sage.categories.commutative_rings import CommutativeRings
from dzack_research.preamble.categories.abstract_categories.functors import Functor
from sage.categories.homset import Hom
from sage.categories.morphism import Morphism
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings as SageRings

from dzack_research.preamble.categories.rings.rings import OwnedRings


class RingCenterFunctor(Functor):
    r"""\(Z\), from the isomorphisms of rings to the commutative rings."""

    def __init__(self) -> None:
        super().__init__(OwnedRings().core(), CommutativeRings())

    def _apply_functor(self, ring: "Ring") -> "Ring":
        return ring.ring_center()

    if TYPE_CHECKING:
        # This functor is defined on the *core*: its ``arrow`` gate is what
        # refuses a morphism that was never declared invertible.
        def domain(self) -> "Core": ...

    def _apply_functor_to_morphism(self, morphism: Morphism) -> Morphism:
        r"""Return \(Z(f):Z(A)\to Z(B)\), the restriction of \(f\).

        The source category is what refuses a non-invertible arrow: the
        restriction exists because \(f\) is onto its codomain, and an arrow
        that has not been declared invertible cannot be taken to be.
        """
        source = self.domain().arrow(morphism)
        return SetMorphism(
            Hom(
                source.domain().ring_center(),
                source.codomain().ring_center(),
                SageRings(),
            ),
            source,
        )
