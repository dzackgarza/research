import pytest

from dzack_research.preamble.all import NN, QQ, ZZ, Lattices




def test_infinite_metric_map_targets_the_full_algebraic_dual() -> None:
    lattice = Lattices(QQ)(QQ**NN)
    dual = lattice.linear_dual()
    correlation = lattice.metric_map()
    e0 = lattice.basis_vector(0)
    e1 = lattice.basis_vector(1)
    e3 = lattice.basis_vector(3)

    assert dual is lattice.module_category().Mor(lattice, QQ.regular_module())
    assert correlation.domain() is lattice
    assert correlation.codomain() is dual

    first_covector = correlation(e0)
    assert first_covector.parent() is dual
    assert first_covector(e0) == 1
    assert first_covector(e1) == 0

    all_ones = dual(lambda _label: QQ.regular_module()(1))
    assert all_ones.parent() is dual
    assert all_ones(e0) == all_ones(e1) == all_ones(e3) == 1
    # Every vector of QQ^(NN) has finite support, whereas all_ones does not.
    # Thus the represented diagonal correlation is injective but not onto the
    # full algebraic dual.
    assert lattice.is_nondegenerate() is True
    assert lattice.gram_tensor().is_unimodular() is False
    with pytest.raises(AssertionError, match="cokernel construction"):
        lattice.is_unimodular()


def test_nondegenerate_and_unimodular_are_distinct_and_perfectness_retains_an_inverse() -> None:
    doubled_line = Lattices(ZZ)([[2]])
    assert doubled_line.is_nondegenerate() is True
    assert doubled_line.is_unimodular() is False

    plane = Lattices(ZZ)("U")
    correlation = plane.correlation_isomorphism()
    for generator in plane.module_generators():
        assert correlation.inverse()(correlation.forward()(generator)) == generator
    for functional in correlation.forward().codomain().module_generators():
        assert correlation.forward()(correlation.inverse()(functional)) == functional












