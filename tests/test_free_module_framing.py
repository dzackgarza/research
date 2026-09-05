import pytest

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModule
from dzack_research.preamble.categories.sets import NN, Sets


def test_rank_free_module_uses_the_canonical_owned_finite_ordinal_framing() -> None:
    module = FreeModule(ZZ, 3)
    labels = module.module_generating_set()

    assert labels is Sets.Δ[2]
    assert labels.unrank(0).parent() is NN
    assert labels.unrank(2).parent() is NN
    assert module.module_generator(0) == module.module_generator(NN(0))


def test_keyed_coordinates_are_normalized_through_the_owned_framing() -> None:
    module = FreeModule(ZZ, 3)
    element = module({0: 2, NN(2): -1})

    coefficients = element.monomial_coefficients()
    assert set(coefficients) == {NN(0), NN(2)}
    assert coefficients[NN(0)] == ZZ(2)
    assert coefficients[NN(2)] == ZZ(-1)


def test_infinite_free_module_rejects_implicit_finite_prefix_coordinates() -> None:
    module = FreeModule(ZZ, NN)

    with pytest.raises(TypeError, match="finite framing"):
        module((1, 0, 0, 1))

    element = module({NN(0): 1, NN(3): 1})
    assert element.monomial_coefficients() == {NN(0): ZZ(1), NN(3): ZZ(1)}


def test_infinite_framing_is_not_enumerated_for_finite_ring_linearity_checks() -> None:
    from dzack_research.preamble.all import GF
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    field = GF(2)
    module = FreeModule(field, NN)
    identity = module_homset(module, module).elementwise(lambda element: element)

    generator = module.module_generator(NN(17))
    assert identity(generator) == generator


def test_infinite_generator_defined_morphism_keeps_its_image_family_lazy() -> None:
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    module = FreeModule(ZZ, NN)
    evaluated = []

    def generator_image(label):
        evaluated.append(label)
        return module.module_generator(label)

    identity = module_homset(module, module)(generator_image)

    assert evaluated == []
    assert identity.module_generator_images().index_set() is module.module_generating_set()
    generator = module.module_generator(NN(17))
    assert identity(generator) == generator
    assert evaluated == [NN(17)]

    with pytest.raises(TypeError, match="finite framing"):
        module_homset(module, module)({NN(0): module.module_generator(NN(0))})
