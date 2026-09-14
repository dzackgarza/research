r"""Archive reconciliation for the hyperbolic triangle TDD specimens.

The source assertions are
``archives/preamble/tests/coxeter_tdd_specs/system/test_classification_examples.sage``:
the compact triangle ``[3,7]`` is Lannér, while ``[3,infinity]`` is
quasi-Lannér.  They are stated here through the live Coxeter/Vinberg owners,
with exact Coxeter bonds and subdiagram types rather than a numerical Gram
approximation.
"""

from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
from sage.rings.infinity import Infinity

from dzack_research.preamble.all import CoxeterDiagrams, finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/coxeter_tdd_specs/system/test_classification_examples.sage",
    "live_owner": "tests/lattices/test_coxeter_literature.py",
    "owner_overrides": {
        "test_the_two_three_seven_triangle_is_a_lanner_simplex": "tests/lattices/test_coxeter_hyperbolic_tdd_archive.py",
        "test_the_three_infinity_triangle_is_quasi_lanner": "tests/lattices/test_coxeter_hyperbolic_tdd_archive.py",
    },
    "disposition": "reconciled-live-owner",
}


def _triangle(first, second, third):
    entries = (
        (1, first, third),
        (first, 1, second),
        (third, second, 1),
    )
    engine_entries = tuple(
        tuple(-1 if entry is Infinity else entry for entry in row)
        for row in entries
    )
    return CoxeterDiagrams().from_coxeter_matrix(CoxeterMatrix(engine_entries))


def test_two_three_seven_triangle_is_lanner_not_quasi_lanner() -> None:
    r"""The ``(2,3,7)`` reflection triangle is compact hyperbolic."""
    diagram = _triangle(3, 7, 2)
    invariants = diagram.vinberg_invariant_matrix()

    assert invariants.coxeter_entry(0, 1) == 3
    assert invariants.coxeter_entry(1, 2) == 7
    assert invariants.coxeter_entry(0, 2) == 2
    assert not invariants.is_crystallographic()
    assert invariants.is_hyperbolic()
    assert invariants.is_compact_hyperbolic()
    assert not invariants.is_paracompact_hyperbolic()

    vertices = diagram.index_set()
    for omitted in vertices:
        subdiagram = diagram.induced_subdiagram(
            finite_ordered_set([vertex for vertex in vertices if vertex != omitted])
        )
        assert subdiagram.is_elliptic()


def test_three_infinity_triangle_is_quasi_lanner_not_lanner() -> None:
    r"""The ``[3,infinity]`` triangle has one ideal vertex and finite volume."""
    diagram = _triangle(3, Infinity, 2)
    invariants = diagram.vinberg_invariant_matrix()

    assert invariants.coxeter_entry(0, 1) == 3
    assert invariants.coxeter_entry(1, 2) is Infinity
    assert invariants.coxeter_entry(0, 2) == 2
    assert invariants.is_hyperbolic()
    assert invariants.is_paracompact_hyperbolic()
    assert not invariants.is_compact_hyperbolic()

    ideal_vertex = diagram.induced_subdiagram((1, 2))
    assert ideal_vertex.is_parabolic()
    vertices = diagram.index_set()
    for omitted in vertices:
        subdiagram = diagram.induced_subdiagram(
            finite_ordered_set([vertex for vertex in vertices if vertex != omitted])
        )
        assert subdiagram.is_elliptic() or subdiagram.is_parabolic()


def test_elliptic_parabolic_and_hyperbolic_specimens_are_pairwise_distinguished() -> None:
    elliptic = CoxeterDiagrams().from_cartan_type(["A", 2])
    parabolic = CoxeterDiagrams().from_cartan_type(["A", 2, 1])
    hyperbolic = _triangle(3, 7, 2)

    assert elliptic.is_elliptic() and not elliptic.is_parabolic()
    assert parabolic.is_parabolic() and not parabolic.is_elliptic()
    invariants = hyperbolic.vinberg_invariant_matrix()
    assert invariants.is_hyperbolic()
    assert not invariants.is_elliptic()
    assert not invariants.is_parabolic()
