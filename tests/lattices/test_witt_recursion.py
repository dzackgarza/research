r"""Exact rank-decreasing data for the represented higher-Witt recursion."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.eichler_criterion import (
    EichlerOrthogonalFactorizationDatum,
    EichlerRecursiveStabilizerDatum,
    two_u_eichler_model,
)
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def test_covering_stabilizers_restrict_to_rank_one_smaller_orthogonal_complements() -> None:
    integers = _own_ring(SageZZ)
    model = two_u_eichler_model(Lattices(integers)("A2"))
    lattice = model.lattice()
    recursive = model.recursive_stabilizer_data(integers(-2))

    assert recursive.cardinality() > 0
    for discriminant_class in recursive.index_set():
        datum = recursive[discriminant_class]
        assert isinstance(datum, EichlerRecursiveStabilizerDatum)
        vector = datum.vector()
        perpendicular = datum.perpendicular_lattice()
        inclusion = perpendicular.inclusion()
        assert vector.parent() is lattice
        assert vector.q() == -2
        assert int(perpendicular.module_rank()) + 1 == int(lattice.module_rank())
        assert datum.rank_drop() == 1
        assert datum.restricted_generators().index_set() is datum.stabilizer_generators()
        for generator in datum.stabilizer_generators():
            restricted = datum.restricted_generators()[generator]
            assert generator(vector) == vector
            assert restricted in perpendicular.O()
            for label in perpendicular.module_generating_set():
                element = perpendicular.module_generator(label)
                assert inclusion(restricted(element)) == generator(inclusion(element))


def test_every_live_orthogonal_generator_factors_through_stable_eichler_and_discriminant_parts() -> None:
    integers = _own_ring(SageZZ)
    model = two_u_eichler_model(Lattices(integers)("A2"))
    lattice = model.lattice()
    stable = model.stable_kernel()

    for generator in lattice.O().group_generators():
        factorization = model.factor_orthogonal_isometry(generator)
        assert isinstance(factorization, EichlerOrthogonalFactorizationDatum)
        assert factorization.isometry() == generator
        assert factorization.stable_factor() in stable
        assert factorization.discriminant_lift() in lattice.O()
        assert (
            factorization.discriminant_lift().discriminant_morphism()
            == generator.discriminant_morphism()
        )
        assert factorization.reconstruct() == generator


def test_source_defined_approximate_family_has_the_expected_four_n_shape() -> None:
    integers = _own_ring(SageZZ)
    model = two_u_eichler_model(Lattices(integers)("A2"))
    family = model.approximate_generating_family()
    rank = int(model.lattice().module_rank())

    assert int(family.cardinality()) == 4 * rank
    assert all(generator in model.lattice().O() for generator in family)
