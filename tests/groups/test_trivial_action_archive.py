r"""Archive reconciliation for the trivial-action lattice functor.

The archive's ``TrivialActionFunctor`` was the restriction functor
``epsilon^*: Lat -> Lat_G`` along the augmentation, with coinvariants and
invariants as its left and right adjoints.  The live owner generalizes this to
all modules, so this specimen keeps the archived lattice case and a nonidentity
map inside that general construction.
"""

from dzack_research.preamble.all import ZZ, Groups, Lattices, Modules

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/functors/trivial_action.sage",
    "live_owner": "src/dzack_research/preamble/categories/functors/group_actions.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_trivial_action_is_the_live_functor_on_a_nonidentity_lattice_map() -> None:
    group = Groups.C(2)
    lattice = Lattices(ZZ)("A2")
    labels = tuple(lattice.module_generating_set())
    negation = lattice.module_category().Mor(lattice, lattice)(
        {label: -lattice.module_generator(label) for label in labels}
    )

    trivial = Modules(ZZ).trivial_action(group)
    acted = trivial(lattice)
    acted_negation = trivial(negation)

    assert acted.is_trivial_action()
    displayed = repr(acted.module_generators())
    assert displayed.startswith("Module generators: [")
    assert "Indexed family" not in displayed
    assert acted_negation.domain() is acted
    assert acted_negation.codomain() is acted
    for label in labels:
        generator = acted.module_generator(label)
        assert acted_negation(generator) == -generator


def test_archived_coinvariant_trivial_invariant_adjunctions_use_the_same_live_object() -> None:
    group = Groups.C(2)
    lattice = Lattices(ZZ)("A2")
    trivial_invariants = Modules(ZZ).trivial_invariants_adjunction(group)
    acted = trivial_invariants.left_adjoint()(lattice)

    invariants = trivial_invariants.right_adjoint()(acted)
    assert invariants.module_rank() == lattice.module_rank()
    unit = trivial_invariants.unit(lattice)
    counit = trivial_invariants.counit(acted)
    for label in lattice.module_generating_set():
        generator = lattice.module_generator(label)
        assert counit(unit(generator)) == acted.module_generator(label)

    coinvariants_trivial = Modules(ZZ[group]).coinvariants_trivial_adjunction()
    coinvariants = coinvariants_trivial.left_adjoint()(acted)
    assert coinvariants is lattice
    counit = coinvariants_trivial.counit(lattice)
    for label in lattice.module_generating_set():
        generator = lattice.module_generator(label)
        assert counit(generator) == generator
