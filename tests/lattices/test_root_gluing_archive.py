r"""Named root-lattice glue reconstructions retained from the archive suite.

Nikulin's isotropic-subgroup/overlattice correspondence and Conway--Sloane's
root-lattice glue tables give the two concrete reconstructions below.  The
assertions are on the live owned inclusions and discriminant classes.
"""

from dzack_research.preamble.all import Lattices


def test_a1_four_has_a_proper_index_two_overlattice_of_d4_genus() -> None:
    source = Lattices.A1 ** 4
    inclusion = source.maximal_overlattice()
    target = inclusion.codomain()

    assert inclusion.index() == 2
    assert target.is_even()
    assert target.genus() == Lattices.D4.genus()


def test_order_five_a4_a4_glue_reconstructs_e8() -> None:
    source = Lattices.A4 + Lattices.A4
    discriminant = source.discriminant_group()
    summand_inclusions = tuple(
        summand.embedding().discriminant_inclusion()
        for summand in source.summands()
    )
    first = summand_inclusions[0](
        summand_inclusions[0].domain().module_generators()[0]
    )
    second = summand_inclusions[1](
        summand_inclusions[1].domain().module_generators()[0]
    )
    glue_class = first + 2 * second
    glue = discriminant.subobject_generated_by((glue_class,))
    inclusion = discriminant.overlattice_from_isotropic_subobject(glue)
    target = inclusion.codomain()

    assert tuple(discriminant.invariants()) == (5, 5)
    assert glue_class.q() == 0
    assert glue.cardinality() == 5
    assert discriminant.orthogonal_quotient(glue).cardinality() == 1
    assert inclusion.index() == 5
    assert target.is_even()
    assert target.is_unimodular()
    assert target.is_isometric(Lattices.E8) is True
