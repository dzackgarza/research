r"""Archive reconciliation for a ring as its canonical rank-one module.

The archive cached a separate ``BasedFreeModule(R, {1})``.  The live owner is
stronger: an owned ring is itself the canonical free rank-one module over
itself, so every construction that asks for ``R`` as a module receives the
same mathematical parent rather than an equal parallel copy.
"""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    ring_as_module,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/finitely_generated/ring_as_module.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py",
    "disposition": "reconciled-live-owner",
}


def test_owned_ring_is_its_own_canonical_rank_one_module() -> None:
    integers = _own_ring(SageZZ)
    module = ring_as_module(integers)

    assert integers is ZZ
    assert module is integers
    assert ring_as_module(SageZZ) is module
    assert module.base_ring() is integers
    assert module.module_rank() == 1
    assert module.module_generator(0) == integers.one()


def test_hom_endpoints_use_the_same_ring_module_parent() -> None:
    module = ring_as_module(ZZ)
    endomorphisms = module_homset(module, module)
    identity = endomorphisms.identity()
    generator = module.module_generator(0)

    assert identity.domain() is ZZ
    assert identity.codomain() is ZZ
    assert identity(generator) == generator
