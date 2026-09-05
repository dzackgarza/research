import pytest

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.algebras.algebras import algebra_homset
from dzack_research.preamble.categories.algebras.sparse_free_algebras import (
    SparseTensorAlgebraOf,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModule
from dzack_research.preamble.categories.sets import NN


def test_infinite_free_algebra_morphism_keeps_generator_images_lazy() -> None:
    module = FreeModule(ZZ, NN)
    algebra = SparseTensorAlgebraOf(module)
    evaluated = []

    def generator_image(label):
        evaluated.append(label)
        return algebra.algebra_generator(label)

    identity = algebra_homset(algebra, algebra)(generator_image)

    assert evaluated == []
    assert identity.algebra_generator_images().index_set() is algebra.algebra_generating_set()
    generator = algebra.algebra_generator(NN(3))
    assert identity(generator) == generator
    assert evaluated == [NN(3)]

    with pytest.raises(TypeError, match="callable or indexed family"):
        algebra_homset(algebra, algebra)({NN(0): algebra.algebra_generator(NN(0))})
