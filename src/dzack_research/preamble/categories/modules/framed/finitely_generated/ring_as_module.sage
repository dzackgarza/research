r"""\(R\) as the free rank-one module over itself, one object per ring."""

from typing import TYPE_CHECKING

from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
from dzack_research.preamble.categories.rings.rings import engine_ring
from dzack_research.preamble.categories.sets.owned_sets import Sets

if TYPE_CHECKING:
    from sage.categories.modules import Module
    from sage.rings.ring import Ring


_RING_AS_MODULE: dict = {}


def ring_as_module(ring: "Ring") -> "Module":
    r"""Return \(R\) as a module over itself: free of rank one on \(\{1\}\).

    One object per ring, and that is the point rather than an optimisation.
    A framed free module carries value equality, so two separately built
    copies of \(R\) compare equal while being distinct -- and a morphism
    checks that its images belong to *its* codomain, which the copy is not.
    Every submodule of \(R\) is taken inside this one.
    """
    # One object per ring means per ring, not per name for it: the owned view
    # and the engine's copy are the same \(R\), and keying them apart would
    # build the second copy this function exists to prevent.
    ring = engine_ring(ring)
    module = _RING_AS_MODULE.get(ring)
    if module is None:
        module = BasedFreeModule(ring, Sets.Δ[0])
        _RING_AS_MODULE[ring] = module
    return module
