"""Coordinates are available only through selected finite framings."""

from dzack_research.preamble.all import (
    ZZ,
    FinitelyPresentedTorsionModules,
    MatrixSpaces,
)
from dzack_research.preamble.categories.sets import NN, finite_ordered_set


def test_finite_free_map_has_one_coordinate_matrix_from_its_two_framings() -> None:
    source = ZZ.free_module(finite_ordered_set(("e", "f")))
    target = ZZ.free_module(finite_ordered_set(("u", "v")))
    morphism = source.Mor(target)(
        {
            "e": target.module_generator("v"),
            "f": target.module_generator("u"),
        }
    )

    assert morphism(source.module_generator("e")) == target.module_generator("v")
    assert morphism(source.module_generator("f")) == target.module_generator("u")
    assert morphism.parent() in MatrixSpaces(ZZ)

    matrix = morphism.matrix()
    assert matrix.domain() is source.framing_source()
    assert matrix.codomain() is target.framing_source()
    source_labels = tuple(matrix.parent().column_index_set())
    target_labels = tuple(matrix.parent().row_index_set())
    assert matrix[target_labels[0], source_labels[0]] == ZZ.zero()
    assert matrix[target_labels[1], source_labels[0]] == ZZ.one()
    assert matrix[target_labels[0], source_labels[1]] == ZZ.one()
    assert matrix[target_labels[1], source_labels[1]] == ZZ.zero()


def test_relationful_map_keeps_its_presentation_instead_of_claiming_a_matrix() -> None:
    module = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((6,))
    label = module.module_generating_set()[0]
    generator = module.module_generator(label)
    doubling = module.Mor(module)({label: 2 * generator})

    assert doubling(generator) == 2 * generator
    assert doubling.parent() not in MatrixSpaces(ZZ)
    assert not hasattr(doubling, "matrix")


def test_infinite_free_map_uses_its_framing_without_a_finite_matrix() -> None:
    module = ZZ.free_module(NN)
    identity = module.Mor(module).identity()
    generator = module.module_generator(NN(3))

    assert identity(generator) == generator
    assert identity.parent() not in MatrixSpaces(ZZ)
    assert not hasattr(identity, "matrix")
