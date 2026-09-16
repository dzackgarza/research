"""Canonical grading witnesses use the category's selected grading monoid."""

from dzack_research.preamble.all import (
    NN,
    ZZ,
    GradedAlgebras,
    GradedModules,
    Modules,
    StrictlyGradedCommutativeAlgebras,
    Zmod,
)


def test_noninteger_graded_module_witness_is_concentrated_at_the_identity() -> None:
    grading = Zmod(2)
    category = GradedModules(ZZ, grading)
    module = category.an_object()
    generator = module.module_generator(0)

    assert module in category
    assert module.grading_monoid() is grading
    assert module.concentrated_degree() == grading.zero()
    identity = category.Mor(module, module).identity()
    assert identity(generator) == generator


def test_finite_and_infinite_grading_monoids_keep_the_same_module_codomain() -> None:
    finite = GradedModules(ZZ, Zmod(2)).an_object()
    infinite = GradedModules(ZZ, NN).an_object()

    assert finite in Modules(ZZ)
    assert infinite in Modules(ZZ)
    assert finite.concentrated_degree() == Zmod(2).zero()
    assert infinite.concentrated_degree() == NN.zero()


def test_noninteger_graded_algebra_witness_inherits_its_graded_module_structure() -> None:
    grading = Zmod(2)
    category = GradedAlgebras(ZZ, grading)
    algebra = category.an_object()

    assert algebra in category
    assert algebra in GradedModules(ZZ, grading)
    assert algebra.grading_monoid() is grading
    assert algebra.one() * algebra.one() == algebra.one()


def test_graded_commutative_witness_retains_the_stated_parity() -> None:
    grading = Zmod(2)
    parity = grading.Mor(grading).identity()
    category = GradedAlgebras(ZZ, grading, parity).Supercommutative()
    strict = StrictlyGradedCommutativeAlgebras(ZZ, grading, parity)

    algebra = category.an_object()
    strict_algebra = strict.an_object()

    assert category.parity_homomorphism() is parity
    assert strict.parity_homomorphism() is parity
    assert algebra in category
    assert strict_algebra in strict
    assert algebra.grading_monoid() is grading
    assert strict_algebra.grading_monoid() is grading
