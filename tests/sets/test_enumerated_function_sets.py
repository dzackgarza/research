import pytest
from sage.all import SR
from sage.rings.infinity import Infinity

from dzack_research.preamble.all import (
    NN,
    ZZ,
    EnumeratedByIntegers,
    EnumeratedByNaturals,
    FourierCharacters,
    FunctionEnumeratedSets,
    HermitePolynomials,
    InfiniteEnumeratedSets,
    Lattices,
    LaurentMonomials,
    SincTranslates,
)
from dzack_research.preamble.categories.sets.enumerated.function_sets import (
    IndexedSymbolicFunctionSet,
    indexed_symbol,
)


def test_symbolic_function_sets_share_one_indexed_parent() -> None:
    for function_set in (
        FourierCharacters(),
        HermitePolynomials(),
        LaurentMonomials(),
        SincTranslates(),
    ):
        assert isinstance(function_set, IndexedSymbolicFunctionSet)


def test_hermite_polynomials_are_enumerated_by_naturals() -> None:
    hermite = HermitePolynomials()
    H0 = hermite.function(0)
    H3 = hermite.function(3)

    assert hermite in FunctionEnumeratedSets()
    assert hermite in EnumeratedByNaturals()
    assert hermite in InfiniteEnumeratedSets()
    assert hermite.index_set() is NN
    assert hermite.cardinality() == Infinity
    assert H0 in hermite
    assert H3 in hermite
    assert hermite.rank(H3) == 3
    assert hermite.unrank(3) == H3
    assert H0 in SR
    assert str(H0) == "H_0"
    assert 1 not in hermite
    assert indexed_symbol("H", -1, "H") not in hermite
    with pytest.raises(IndexError):
        hermite.unrank(-1)


def test_integer_indexed_function_sets() -> None:
    laurent = LaurentMonomials()
    sinc = SincTranslates()
    fourier = FourierCharacters()
    z_m1 = laurent.function(-1)
    sinc_1 = sinc.function(1)
    F0 = fourier.function(0)

    assert laurent in EnumeratedByIntegers()
    assert sinc in FunctionEnumeratedSets()
    assert fourier in InfiniteEnumeratedSets()
    assert repr(laurent.index_set()) == "Integer Ring"
    assert z_m1 in laurent
    assert laurent.function(-1) == laurent.unrank(laurent.rank(z_m1))
    assert str(z_m1) == "z_m1"
    assert sinc.function(-1) in sinc
    assert str(sinc_1) == "sinc_1"
    assert str(F0) == "F_0"
    assert F0 in fourier
    assert 1 not in fourier
    with pytest.raises(IndexError):
        laurent.unrank(-1)


def test_a_lattice_may_be_free_on_hermite_polynomials() -> None:
    hermite = HermitePolynomials()
    lattice = Lattices(ZZ)(ZZ**NN, module_generators=hermite)
    H0 = hermite.function(0)
    H2 = hermite.function(2)

    assert lattice.module_generating_set() is hermite
    assert lattice.module_generator(H0) * lattice.module_generator(H2) == 0
    assert lattice.module_generator(H0) * lattice.module_generator(H0) == 1
    assert repr(lattice.module_generator(H0)) == "H_0"
