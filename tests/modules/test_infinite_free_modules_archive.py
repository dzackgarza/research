from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreeModuleOn,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.set_categories import Sets

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/categories/modules/pure/free_modules.sage",
        "live_owner": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/tests/test_infinite_modules.sage",
        "live_owner": "src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py",
        "disposition": "reconciled-live-owner",
    },
)


def _countable_labels():
    return Sets.Δ[Sets.ℵ[0]]


def test_countably_framed_free_module_is_not_forced_finite() -> None:
    integers = _own_ring(SageZZ)
    labels = _countable_labels()
    module = FreeModuleOn(integers, labels)

    assert labels not in Sets().Finite()
    assert module.base_ring() is integers
    assert module.module_generating_set() is labels


def test_countable_free_module_generators_are_available_by_label() -> None:
    integers = _own_ring(SageZZ)
    module = FreeModuleOn(integers, _countable_labels())

    first = module.module_generator(0)
    seventh = module.module_generator(7)

    assert first in module
    assert seventh in module
    assert first != seventh


def test_countable_free_module_operations_do_not_require_a_finite_basis() -> None:
    integers = _own_ring(SageZZ)
    module = FreeModuleOn(integers, _countable_labels())
    x = module.module_generator(0)
    y = module.module_generator(5)

    assert x + y == y + x
    assert x + module.zero() == x
    assert (x + y) - y == x
    assert integers(2) * x == x + x


def test_finiteness_remains_a_property_of_the_framing_not_of_every_free_module() -> None:
    integers = _own_ring(SageZZ)
    infinite = FreeModuleOn(integers, _countable_labels())
    finite = FreeModuleOn(integers, Sets.Δ[2])

    assert finite.module_generating_set() in Sets().Finite()
    assert infinite.module_generating_set() not in Sets().Finite()
