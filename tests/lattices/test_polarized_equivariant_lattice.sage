r"""The polarized Enriques arithmetic group inside \(O(L_{K3})\)."""

from dzack_research.preamble.all import *


def test_polarization_restricts_extensions_across_two_hyperbolic_planes() -> None:
    r"""On U + U, exchange the summands; the fixed and opposite lattices are U(2).

    The stabilizer of e+2f in O(U(2)) is trivial.  Its discriminant action
    therefore permits only the two signs on the opposite U(2), whereas
    the stabilizer of e+f also permits exchanging its isotropic lines.
    """
    lattice = Lattices(ZZ)([[0, 1, 0, 0], [1, 0, 0, 0],
                            [0, 0, 0, 1], [0, 0, 1, 0]])
    e, f, u, v = tuple(lattice.module_generators().values())
    involution = lattice.O()({0: u, 1: v, 2: e, 3: f})
    restricted = involution.polarized(e + u + 2 * (f + v)).coinvariant_extension_subgroup()
    symmetric = involution.polarized(e + u + f + v).coinvariant_extension_subgroup()
    opposite = restricted.supergroup().domain()
    a, b = tuple(opposite.module_generators().values())
    exchange = opposite.O()({0: b, 1: a})
    negation = opposite.O()({0: -a, 1: -b})

    assert negation in restricted
    assert exchange not in restricted
    assert exchange in symmetric


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


def test_coinvariant_discriminant_transport_preserves_inverse_and_glue() -> None:
    r"""Conjugating across full glue preserves the action and its inverse.

    This exercises the exact forward/inverse transport rather than asking the
    generic finite presented-module solver to rediscover an inverse.
    """
    lattice = Lattices(ZZ)([[0, 1, 0, 0], [1, 0, 0, 0],
                            [0, 0, 0, 1], [0, 0, 1, 0]])
    e, f, u, v = tuple(lattice.module_generators().values())
    involution = lattice.O()({0: u, 1: v, 2: e, 3: f})
    extension = involution.polarized(e + u + f + v).primitive_extension()
    invariant_group = extension.invariant.discriminant_image()
    _, invariant_form, coinvariant_form, *_ = extension._coinvariant_glue_inverse_maps()
    for generator in invariant_group.group_generators():
        transported = extension._coinvariant_discriminant_from_invariant(generator)
        transported_inverse = extension._coinvariant_discriminant_from_invariant(generator.inverse())
        assert transported.parent() is coinvariant_form.O()
        assert transported_inverse.parent() is coinvariant_form.O()
        for element in coinvariant_form.module_generators():
            assert transported_inverse(transported(element)) == element
            assert transported(transported_inverse(element)) == element
