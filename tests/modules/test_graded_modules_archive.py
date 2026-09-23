r"""Archive reconciliation for the generic decomposition surface of graded modules."""

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/graded_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/graded_modules.py",
    "disposition": "reconciled-live-owner",
}


def _tensor_algebra():
    return QQ.free_module(finite_ordered_set(("x", "y"))).tensor_algebra()




def test_archive_generic_degree_and_homogeneous_components_live_on_graded_modules() -> None:
    algebra = _tensor_algebra()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    mixed = x + y * y

    assert x.degree() == 1
    assert (y * y).degree() == 2
    assert mixed.degree() == 2
    assert x.is_homogeneous()
    assert (y * y).is_homogeneous()
    assert not mixed.is_homogeneous()

    components = mixed.homogeneous_components()
    assert set(components.index_set()) == {1, 2}
    assert components[1] == x
    assert components[2] == y * y
    assert mixed.truncate(2) == x




