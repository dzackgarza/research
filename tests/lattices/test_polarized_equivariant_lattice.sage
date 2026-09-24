r"""The polarized Enriques arithmetic group inside \(O(L_{K3})\)."""

from dzack_research.preamble.all import *


def test_negation_centralizes_the_enriques_involution_but_leaves_its_polarized_group() -> None:
    r"""\(-1\) is central in \(O(L)\), so it commutes with \(\iota\); it sends
    \(h\neq0\) to \(-h\neq h\), so it does not fix a polarization.  The
    involution fixes every vector of its invariant lattice, hence \(h\).
    """
    lattice = NamedLattices.LK3
    involution = Involutions.I_En
    invariant = involution.primitive_extension().invariant
    inclusion = invariant.inclusion()
    first, second = invariant.module_generators()
    polarization = inclusion(first) + inclusion(second)

    polarized = involution.polarized(polarization)
    centralizer = polarized.centralizer_group()
    stabilizer = polarized.polarization_stabilizer()
    group = polarized.polarized_group()

    assert involution(polarization) == polarization
    assert involution in centralizer
    assert involution in stabilizer
    assert involution in group

    negation = lattice.O()(
        {label: -lattice.module_generator(label) for label in lattice.module_generating_set()}
    )
    assert negation in centralizer
    assert negation not in stabilizer
    assert negation not in group
