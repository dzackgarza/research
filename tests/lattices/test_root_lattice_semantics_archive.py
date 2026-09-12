r"""Archived ADE root-lattice semantics on the live root-lattice owner.

The archived ``RootLattices`` category retained the selected Cartan type and
simple-root framing together with highest roots, Coxeter numbers, simple
reflections, fundamental weights, root signs/heights, and coroots.  The
``A2`` specimen is small enough to distinguish all of these operations from
mere root enumeration.
"""

from dzack_research.preamble.all import ZZ, Lattices

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/integrallattice/root_lattices.sage",
    "live_owner": "src/dzack_research/preamble/categories/lattices.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_a2_selected_simple_system_and_highest_root_are_live() -> None:
    lattice = Lattices(ZZ)("A2")
    first, second = lattice.simple_roots()
    highest = lattice.highest_root()

    assert str(lattice.cartan_type()) == "['A', 2]"
    assert lattice.coxeter_number() == 3
    assert highest == first + second
    assert highest.is_root()
    assert highest.is_positive_root()
    assert highest.height() == 2
    assert (-highest).is_negative_root()
    assert (-highest).height() == -2
    assert first.height() == 1
    assert second.height() == 1


def test_archived_simple_reflections_act_on_the_selected_root_framing() -> None:
    lattice = Lattices(ZZ)("A2")
    first, second = lattice.simple_roots()
    first_reflection, second_reflection = lattice.simple_reflections()

    assert first_reflection(first) == -first
    assert second_reflection(second) == -second
    assert first_reflection(second) == first + second
    assert second_reflection(first) == first + second

    coxeter = first_reflection * second_reflection
    assert coxeter * coxeter * coxeter == lattice.Aut().one()
    assert coxeter != lattice.Aut().one()


def test_archived_fundamental_weights_and_coroots_live_in_the_metric_dual() -> None:
    lattice = Lattices(ZZ)("A2")
    roots = tuple(lattice.simple_roots())
    weights = tuple(lattice.fundamental_weights())
    dual_basis = tuple(lattice.dual_basis())

    assert len(weights) == 2
    assert weights == tuple(-weight for weight in dual_basis)

    correlation = lattice.correlation_morphism()
    dual_lattice = lattice.dual_lattice()
    for root in roots:
        coroot = root.coroot()
        assert coroot.parent() is dual_lattice
        assert coroot == -correlation(root)


def test_archived_a2_root_sign_partition_is_exact() -> None:
    lattice = Lattices(ZZ)("A2")
    roots = tuple(lattice.roots())
    positive = tuple(root for root in roots if root.is_positive_root())
    negative = tuple(root for root in roots if root.is_negative_root())

    assert len(roots) == 6
    assert len(positive) == 3
    assert len(negative) == 3
    assert {root.height() for root in positive} == {1, 2}
    assert {root.height() for root in negative} == {-1, -2}
    assert set(negative) == {-root for root in positive}
