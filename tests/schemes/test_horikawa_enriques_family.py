r"""The Enriques surface is the actual fixed-free quotient of the Horikawa K3 member."""

from dzack_research.preamble.all import QQ, Schemes
from dzack_research.preamble.catalogue import NamedLattices
from dzack_research.preamble.categories.schemes.enriques_families import (
    HorikawaEnriquesSurface,
)


def test_fixed_free_horikawa_lift_constructs_the_enriques_quotient() -> None:
    surface = HorikawaEnriquesSurface()
    quotient = surface.quotient_morphism()

    assert surface.scheme() is surface
    assert surface in Schemes(QQ)
    assert quotient.domain() is surface.k3_member().scheme()
    assert quotient.codomain() is surface.scheme()
    assert surface.k3_member().enriques_lift_is_fixed_point_free()
    assert surface.quotient_data().action_is_free()
    assert surface.is_enriques()


def test_enriques_integral_h2_retains_torsion_pullback_and_primitive_gluing() -> None:
    surface = HorikawaEnriquesSurface()
    cohomology = surface.integral_cohomology()
    free = cohomology.enriques_free_h2_lattice()
    torsion = cohomology.canonical_torsion_submodule()
    pullback = cohomology.free_h2_pullback()

    assert free is NamedLattices.E10
    assert free.module_rank() == 10
    assert torsion.cardinality() == 2
    assert pullback.domain() is free
    assert pullback.codomain() is NamedLattices.LK3
    assert all(
        cohomology.enriques_involution_on_h2()(pullback(generator))
        == pullback(generator)
        for generator in free.module_generators()
    )
    assert all(
        cohomology.torsion_h2_pullback()(generator) == NamedLattices.LK3.zero()
        for generator in torsion.module_generators()
    )

    invariant = cohomology.invariant_lattice()
    anti = cohomology.anti_invariant_lattice()
    glue = cohomology.discriminant_gluing_map()
    extension = cohomology.primitive_extension()
    assert invariant.module_rank() == 10
    assert anti.module_rank() == 12
    assert cohomology.invariant_lattice_inclusion() is extension.invariant_inclusion()
    assert cohomology.anti_invariant_lattice_inclusion() is extension.orthogonal_complement_inclusion()
    assert cohomology.primitive_extension_inclusion() is extension.orthogonal_sum_inclusion()
    assert cohomology.primitive_extension_inclusion().codomain() is NamedLattices.LK3
    assert all(
        pullback(free_generator)
        == cohomology.invariant_lattice_inclusion()(invariant_generator)
        for free_generator, invariant_generator in zip(
            free.module_generators(),
            invariant.module_generators(),
            strict=True,
        )
    )
    assert all(
        pullback(left).b(pullback(right)) == 2 * left.b(right)
        for left in free.module_generators()
        for right in free.module_generators()
    )
    assert cohomology.discriminant_gluing_subgroup().cardinality() == 1024
    assert cohomology.primitive_gluing_index() == 1024
    assert glue.domain() is cohomology.discriminant_gluing_subgroup()
    assert glue is extension.glue()


def test_lattice_representation_and_fixed_locus_satisfy_lefschetz() -> None:
    surface = HorikawaEnriquesSurface()
    cohomology = surface.integral_cohomology()

    assert cohomology.h2_trace() == -2
    assert cohomology.topological_lefschetz_number() == 0
    assert cohomology.lefschetz_matches_geometric_fixed_locus()


