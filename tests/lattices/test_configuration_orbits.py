r"""Pairing configuration graphs, their automorphism groups, and permutation lifting.

For a simply-laced root lattice framed by its simple roots, the permutations
of the framing preserving every pairing are the Dynkin diagram automorphisms,
so their group has order ``|O(L)| / |W(L)|``.  The two orders are the values
the repository already records in its Coxeter session: ``A2`` gives ``12/6``,
``A3`` gives ``48/24``, ``D4`` gives ``1152/192`` which is triality, and
``E8`` gives ``696729600/696729600``, the trivial group.

``A1 + A1 + A1`` separates a pairing graph from a bare vertex count: three
mutually orthogonal roots admit every permutation, so its group has order six
where the ``A3`` chain on the same three vectors admits only the reversal.
"""

import pytest

from dzack_research.preamble.all import (
    Lattices,
    NamedLattices,
    ZZ,
    vector_configuration,
)

# Cartan type: (order of the diagram automorphism group, |O(L)|, |W(L)|)
ROOT_BASES = {
    "A2": (2, 12, 6),
    "A3": (2, 48, 24),
    "D4": (6, 1152, 192),
    "E8": (1, 696729600, 696729600),
}


@pytest.mark.parametrize("name", sorted(ROOT_BASES))
def test_a_root_basis_pairing_graph_has_the_diagram_automorphisms(name) -> None:
    diagram_order, isometry_order, weyl_order = ROOT_BASES[name]
    root_lattice = Lattices(ZZ)(name)
    configuration = vector_configuration(root_lattice, root_lattice.module_generators())

    assert configuration.rank() == root_lattice.rank()
    assert configuration.frames_its_lattice()
    assert configuration.configuration_automorphism_group().order() == diagram_order
    assert diagram_order * weyl_order == isometry_order
    assert configuration.diagram_automorphism_isometries().cardinality() == diagram_order


def test_orthogonal_roots_admit_every_permutation_but_a_chain_does_not() -> None:
    chain = Lattices(ZZ)("A3")
    orthogonal = NamedLattices.A1 ** 3
    assert chain.rank() == orthogonal.rank() == 3

    chain_configuration = vector_configuration(chain, chain.module_generators())
    orthogonal_configuration = vector_configuration(
        orthogonal, orthogonal.module_generators()
    )
    assert chain_configuration.configuration_automorphism_group().order() == 2
    assert orthogonal_configuration.configuration_automorphism_group().order() == 6


def test_the_swap_of_the_A2_simple_roots_lifts_to_an_involution_of_O_A2() -> None:
    root_lattice = Lattices(ZZ)("A2")
    positions = root_lattice.module_generating_set()
    first, second = positions[0], positions[1]
    configuration = vector_configuration(root_lattice, root_lattice.module_generators())

    swap = {first: second, second: first}.__getitem__
    assert configuration.preserves_every_pairing(swap)

    restricted = configuration.configuration_isometry(swap)
    assert restricted(configuration.module_generator(first)) == (
        configuration.module_generator(second)
    )

    lifted = configuration.ambient_isometry(swap)
    assert lifted.parent() is root_lattice.Aut()
    assert lifted * lifted == root_lattice.Aut().one()
    assert lifted != root_lattice.Aut().one()
    assert lifted(root_lattice.module_generator(first)) == root_lattice.module_generator(
        second
    )


def test_a_permutation_moving_a_pairing_is_refused() -> None:
    root_lattice = Lattices(ZZ)("A3")
    positions = root_lattice.module_generating_set()
    first, second, third = (positions[index] for index in range(3))
    configuration = vector_configuration(root_lattice, root_lattice.module_generators())

    # The A3 chain is 1-2-3, so exchanging an end with the middle breaks the
    # pairing b(first, third) = 0.
    broken = {first: second, second: first, third: third}.__getitem__
    assert not configuration.preserves_every_pairing(broken)
    with pytest.raises(AssertionError):
        configuration.configuration_isometry(broken)
