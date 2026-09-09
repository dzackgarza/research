r"""Archive reconciliation for the generic decomposition surface of graded modules."""

from dzack_research.preamble.all import GradedModules, QQ, TensorAlgebraOn
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreshFreeModuleOn,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def _tensor_algebra():
    return TensorAlgebraOn(QQ, finite_ordered_set(("x", "y")))


def _finite_graded_module():
    labels = finite_ordered_set(("a", "b", "c"))
    degrees = {"a": 0, "b": 1, "c": 1}

    def selected_degree(generator):
        coefficient_labels = tuple(generator.monomial_coefficients())
        if len(coefficient_labels) != 1:
            raise ValueError("a selected module generator has singleton support")
        return degrees[coefficient_labels[0]]

    return FreshFreeModuleOn(
        QQ,
        labels,
        _extra_categories=(GradedModules(QQ),),
        _extra_construction_data={"degree_on_module_generator": selected_degree},
    )


def test_archive_generic_degree_and_homogeneous_components_live_on_graded_modules() -> None:
    algebra = _tensor_algebra()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    mixed = x + y * y

    assert x.degree() == 1
    assert (y * y).degree() == 2
    assert mixed.degree() == 2
    assert x.is_homogeneous()
    assert (y * y).is_homogeneous()
    assert not mixed.is_homogeneous()

    components = mixed.homogeneous_components()
    assert set(components) == {1, 2}
    assert components[1] == x
    assert components[2] == y * y
    assert mixed.truncate(2) == x


def test_archive_degree_piece_generator_selection_is_the_live_framing() -> None:
    module = _finite_graded_module()
    degree_one = module.module_generators_of_degree(1)

    assert degree_one.cardinality() == 2
    assert all(module.degree_on_module_generator(generator) == 1 for generator in degree_one)
    piece = module.graded_piece(1)
    assert piece.ambient_module() is module
    assert piece.module_generating_set().cardinality() == 2


def test_archive_zero_is_homogeneous_of_degree_minus_infinity() -> None:
    algebra = _tensor_algebra()
    zero = algebra.zero()

    assert zero.is_homogeneous()
    assert str(zero.degree()) == "-Infinity"
    assert zero.homogeneous_components() == {}
    assert zero.truncate(3) == zero
