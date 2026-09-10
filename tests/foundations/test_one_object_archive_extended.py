r"""Remaining valid one-object laws from the archived identity regression.

The archived suite predates the public boundary that now refuses raw Sage
rings.  These tests retain only the mathematical identity assertions that
survive that boundary: equal represented indexing data name one set, and
module/algebra structure maps use the exact owned base ring that constructed
their objects.
"""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.free_algebras import FreeAlgebraOn
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets


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
    algebra = FreeAlgebraOn(integers, Sets.Δ[1])
    structure = algebra._ring_morphism_defining_algebra_structure()

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
