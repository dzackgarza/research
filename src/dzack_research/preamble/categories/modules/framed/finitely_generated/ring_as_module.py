"""A ring as its canonical free rank-one module."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.rings import owned_ring_view


@cached_function
def ring_as_module(ring):
    r"""Return the canonical free rank-one module of a ring over itself.

    When the ring is already selected as a module over itself, this is the
    ring object itself.  An ``R``-algebra ``A`` generally already carries a
    *different* module structure, namely the underlying ``R``-module.  Then
    ``A`` as a free rank-one ``A``-module is a genuinely different structured
    object and is represented by one canonical free-module parent.
    """
    result = owned_ring_view(ring)
    if result.base_ring() is result:
        return result

    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
        BasedFreeModule,
    )

    return BasedFreeModule(result, 1)
