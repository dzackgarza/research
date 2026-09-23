import pytest
from sage.misc.unknown import Unknown

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.sets import NN


def test_infinite_free_algebra_morphism_keeps_generator_images_lazy() -> None:
    module = ZZ.free_module(NN)
    algebra = module.tensor_algebra()
    evaluated = []

    def generator_image(label):
        evaluated.append(label)
        return algebra.algebra_generator(label)

    identity = Algebras(algebra.base_ring()).Associative().Unital().Mor(algebra, algebra)(generator_image)

    assert evaluated == []
    assert identity.algebra_generator_images().index_set() is algebra.algebra_generating_set()
    generator = algebra.algebra_generator(NN(3))
    assert identity(generator) == generator
    assert evaluated == [NN(3)]

    with pytest.raises(TypeError, match="callable or indexed family"):
        Algebras(algebra.base_ring()).Associative().Unital().Mor(algebra, algebra)({NN(0): algebra.algebra_generator(NN(0))})


def test_infinite_graded_map_retains_unknown_degree_hypothesis_but_structural_maps_derive_it() -> None:
    module = ZZ.free_module(NN)
    algebra = module.tensor_algebra()
    mor = GradedAlgebras(ZZ).Mor(algebra, algebra)

    stated = mor(lambda label: algebra.algebra_generator(label))
    identity = mor.identity()
    composite = identity * identity

    assert stated.degree_preservation_decision() is Unknown
    assert identity.degree_preservation_decision() is True
    assert composite.degree_preservation_decision() is True
    assert composite.underlying_algebra_morphism().domain() is algebra
    assert composite.underlying_algebra_morphism().codomain() is algebra
