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
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets

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


def test_equal_finite_enumerations_name_one_owned_ordered_set() -> None:
    integers = _own_ring(SageZZ)
    ordinal = Sets.Δ[2]
    written = finite_ordered_set(tuple(integers(i) for i in range(3)))

    assert written is ordinal
    assert finite_ordered_set((integers(1), integers(2))) is finite_ordered_set(
        (integers(1), integers(2))
    )


def test_free_algebra_structure_map_uses_the_exact_owned_base_ring() -> None:
    integers = _own_ring(SageZZ)
    algebra = integers.free_module(Sets.Δ[1]).symmetric_algebra()
    structure = algebra.algebra_structure_morphism()

    assert algebra.base_ring() is integers
    assert structure.domain() is integers
    assert structure(integers(3)) == integers(3) * algebra.one()


def test_lattice_module_action_uses_the_same_owned_integer_ring() -> None:
    integers = _own_ring(SageZZ)
    lattice = Lattices(integers)("A2")
    action = lattice._ring_morphism_defining_module_action()
    generator = lattice.module_generator(0)

    assert lattice.base_ring() is integers
    assert action.domain() is integers
    assert action(integers(3))(generator) == integers(3) * generator


def test_python_integers_and_owned_integers_name_the_same_finite_ordered_set() -> None:
    integers = _own_ring(SageZZ)

    from_python = finite_ordered_set((1, 2, 3))
    from_ring = finite_ordered_set((integers(1), integers(2), integers(3)))

    assert from_python is from_ring
    assert all(element.parent() is integers for element in from_python)


def test_discriminant_quadratic_form_scales_by_the_square() -> None:
    integers = _own_ring(SageZZ)
    discriminant = Lattices(integers)("A2").discriminant_group()
    generator = next(iter(discriminant.module_generators()))

    assert (2 * generator).q() == 4 * generator.q()
