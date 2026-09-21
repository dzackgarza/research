r"""Archive reconciliation for a ring as its canonical rank-one module.

The archive cached a separate ``BasedFreeModule(R, {1})``.  The live owner is
stronger: an owned ring is itself the canonical free rank-one module over
itself, so every construction that asks for ``R`` as a module receives the
same mathematical parent rather than an equal parallel copy.
"""

from dzack_research.preamble.all import ZZ

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/finitely_generated/ring_as_module.sage",
    "live_owner": "src/dzack_research/preamble/categories/rings/ring_foundation.py",
    "disposition": "reconciled-live-owner",
}


def test_owned_ring_is_its_own_canonical_rank_one_module() -> None:
    integers = ZZ
    module = integers.regular_module()

    assert module is integers
    assert integers.regular_module() is module
    assert module.base_ring() is integers
    assert module.module_rank() == 1
    assert module.module_generator(0) == integers.one()


def test_mor_endpoints_use_the_same_ring_module_parent() -> None:
    module = ZZ.regular_module()
    endomorphisms = module.module_category().Mor(module, module)
    identity = endomorphisms.identity()
    generator = module.module_generator(0)

    assert identity.domain() is ZZ
    assert identity.codomain() is ZZ
    assert identity(generator) == generator
