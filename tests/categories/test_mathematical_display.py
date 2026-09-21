"""Public displays expose mathematical data rather than implementation roles."""

from dzack_research.preamble.all import Lattices, Sets, ZZ
from dzack_research.preamble.categories.sets import NN, finite_ordered_set
from dzack_research.preamble.tensors import tensor


def test_finite_free_generators_display_the_selected_labels_and_values() -> None:
    module = ZZ.free_module(finite_ordered_set(("x", "y")))
    displayed = repr(module.module_generators())

    assert displayed.startswith("Module generators: [")
    assert "x" in displayed and "y" in displayed
    assert "Indexed family" not in displayed


def test_lattice_refinement_does_not_rename_the_inherited_module_generators() -> None:
    lattice = Lattices(ZZ)("U")
    displayed = repr(lattice.module_generators())

    assert displayed.startswith("Module generators: [")
    assert "Lattice" not in displayed


def test_infinite_generator_family_displays_its_semantic_role_and_index_set() -> None:
    module = ZZ.free_module(NN)
    displayed = repr(module.module_generators())

    assert displayed == "Module generators over NN = {0, 1, 2, ...}"
    assert "object at 0x" not in displayed


def test_nonidentity_map_display_exposes_its_endpoints() -> None:
    source = Sets.Δ[1]
    target = Sets.Δ[2]
    morphism = Sets().Mor(source, target)(lambda point: target(int(point) + 1))
    displayed = repr(morphism)

    assert "From:" in displayed and repr(source) in displayed
    assert "To:" in displayed and repr(target) in displayed
    assert "object at 0x" not in displayed


def test_tensor_display_renders_owned_coefficients_not_an_engine_object() -> None:
    vector = tensor.vector(ZZ, [1, 2])
    displayed = repr(vector)

    assert "Type (1, 0) tensor" in displayed
    assert "[1, 2]" in displayed
    assert "object at 0x" not in displayed
