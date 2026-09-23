r"""Even symmetric bilinear forms and their integral quadratic refinements."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    BilinearFormModules,
    QuadraticFormModules,
    SymmetricBilinearFormModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def test_even_a2_has_the_integral_half_norm_quadratic_module() -> None:
    integers = _own_ring(SageZZ)
    lattice = Lattices(integers)("A2")
    quadratic = lattice.to_quadratic_module()
    generators = tuple(quadratic.module_generators())

    assert quadratic in QuadraticFormModules(integers)
    assert tuple(quadratic.q(generator) for generator in generators) == (-1, -1)
    assert quadratic.q(generators[0] + generators[1]) == -1

    polarized = quadratic.associated_bilinear_module()
    assert polarized in BilinearFormModules(integers)
    assert polarized in SymmetricBilinearFormModules(integers)
    original_generators = tuple(lattice.module_generators())
    polarized_generators = tuple(polarized.module_generators())
    for i, left in enumerate(polarized_generators):
        for j, right in enumerate(polarized_generators):
            assert polarized.b(left, right) == lattice.b(
                original_generators[i], original_generators[j]
            )


