r"""Remaining valid one-object laws from the archived identity regression.

The archived suite predates the public boundary that now refuses raw Sage
rings.  These tests retain only the mathematical identity assertions that
survive that boundary: equal represented indexing data name one set, and
module/algebra structure maps use the exact owned base ring that constructed
their objects.
"""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/test_objects_are_one_object.sage",
    "live_owner": "tests/foundations/test_one_object_archive_extended.py",
    "owner_overrides": {
        "test_compiler_runtime_names_do_not_enter_the_installed_namespace": "tests/foundations/test_session_namespace_archive.py",
        "test_a_free_module_is_one_object_per_ring_and_set": "tests/foundations/test_one_object_archive.py",
        "test_the_owned_ring_and_the_engines_key_one_free_module": "tests/foundations/test_one_object_archive.py",
        "test_a_commutative_ring_is_its_own_centre_and_an_algebra_over_itself": "tests/foundations/test_one_object_archive.py",
        "test_the_lattice_axioms_compose_in_any_order": "tests/lattices/test_lattice_axiom_archive.py",
        "test_integral_lattices_is_that_join_and_holds_the_specimens": "tests/lattices/test_lattice_axiom_archive.py",
    },
    "disposition": "reconciled-live-owner",
}










def test_discriminant_quadratic_form_scales_by_the_square() -> None:
    integers = _own_ring(SageZZ)
    discriminant = Lattices(integers)("A2").discriminant_group()
    generator = next(iter(discriminant.module_generators()))

    assert (2 * generator).q() == 4 * generator.q()
