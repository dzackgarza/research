import pytest
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/test_lattice_generator_syntax.sage",
    "live_owner": "src/dzack_research/preamble/categories/lattices.py",
    "disposition": "reconciled-live-owner",
}


def test_explicit_lattice_names_bind_the_selected_generators() -> None:
    integers = _own_ring(SageZZ)
    lattice = Lattices(integers)("U", names=("e", "f"))

    assert lattice.variable_names() == ("e", "f")
    assert lattice._first_ngens(2) == tuple(lattice.module_generators())


def test_preparser_ellipsis_names_expand_to_the_lattice_rank() -> None:
    integers = _own_ring(SageZZ)
    lattice = Lattices(integers)(
        "E8",
        names=("a1", "Ellipsis", "a8"),
    )

    assert lattice.variable_names() == tuple(f"a{index}" for index in range(1, 9))
    assert lattice._first_ngens(8) == tuple(lattice.module_generators())


def test_named_generator_count_must_match_the_rank() -> None:
    integers = _own_ring(SageZZ)

    with pytest.raises(AssertionError, match="rank 8"):
        Lattices(integers)("E8", names=("a1", "Ellipsis", "a5"))


def test_orthogonal_power_is_repeated_direct_sum_not_tensor_power() -> None:
    integers = _own_ring(SageZZ)
    hyperbolic_plane = Lattices(integers)("U")
    triple = hyperbolic_plane**3

    assert triple.module_rank() == 6
    assert triple.signature_pair() == (3, 3)
