r"""Kernels, cokernels, tensor products and local presentations of quasi-coherent sheaves.

On an affine scheme ``M |-> M~`` is an equivalence onto the quasi-coherent
sheaves, so each operation is the module operation carried across.  The
specimen is multiplication by a coordinate on the affine line, whose cokernel
is the structure sheaf of the origin: nonzero, killed by the coordinate, and
zero on the open where that coordinate is a unit.
"""

from dzack_research.preamble.all import (
    AffineSpace,
    FinitelyPresentedModule,
    FreeModule,
    QQ,
    QuasiCoherentSheaves,
)


def _line_and_multiplication():
    line = AffineSpace(1, QQ, names=("x",))
    algebra = line.coordinate_ring()
    x = algebra.algebra_generator("x")
    sheaves = QuasiCoherentSheaves(line)
    structure = sheaves.associated_sheaf(FreeModule(algebra, 1))
    module = sheaves.global_sections(structure)
    multiply_by_x = sheaves.sheaf_morphisms(structure, structure)(
        {0: module.scalar_multiple(x, module.module_generator(0))}
    )
    return line, algebra, x, sheaves, structure, multiply_by_x


def test_the_sheaves_on_an_affine_scheme_are_the_category_equivalent_to_its_modules() -> None:
    line = AffineSpace(1, QQ, names=("x",))
    algebra = line.coordinate_ring()
    sheaves = QuasiCoherentSheaves(line)
    module = FreeModule(algebra, 2)
    sheaf = sheaves.associated_sheaf(module)

    assert sheaves.scheme() is line
    assert module in sheaves.module_category()
    assert sheaf in sheaves
    assert sheaf.sheaf_category() is sheaves
    # The equivalence and its inverse round-trip on the nose.
    assert sheaves.global_sections(sheaf) is module
    assert sheaves.associated_sheaf(module) is sheaf
    assert line.structure_sheaf().associated_module_sheaf(module) is sheaf


def test_multiplication_by_a_coordinate_has_zero_kernel_and_a_skyscraper_cokernel() -> None:
    line, algebra, x, sheaves, structure, multiply_by_x = _line_and_multiplication()

    kernel = sheaves.kernel(multiply_by_x)
    kernel_sections = sheaves.global_sections(kernel)
    # Q[x] is a domain, so multiplication by x is injective and the kernel
    # sheaf is zero: every one of its generators is the zero section.
    assert all(
        kernel_sections.module_generator(label) == kernel_sections.zero()
        for label in kernel_sections.module_generating_set()
    )

    cokernel = sheaves.cokernel(multiply_by_x)
    cokernel_sections = sheaves.global_sections(cokernel)
    origin_section = cokernel_sections.module_generator(0)
    assert origin_section != cokernel_sections.zero()
    assert cokernel_sections.scalar_multiple(x, origin_section) == cokernel_sections.zero()

    # Away from the origin x is a unit, so the skyscraper has no sections there.
    away = line.distinguished_open(x)
    restricted = cokernel.restriction_map(line, away)(origin_section)
    assert restricted == cokernel.sections_on_distinguished_open(away).zero()


def test_the_tensor_product_of_two_free_sheaves_has_the_product_rank() -> None:
    line = AffineSpace(1, QQ, names=("x",))
    algebra = line.coordinate_ring()
    sheaves = QuasiCoherentSheaves(line)
    rank_two = sheaves.associated_sheaf(FreeModule(algebra, 2))
    rank_three = sheaves.associated_sheaf(FreeModule(algebra, 3))

    product = sheaves.tensor_product((rank_two, rank_three))
    assert product in sheaves
    assert sheaves.global_sections(product).base_ring() is algebra
    assert sheaves.global_sections(product).module_generating_set().cardinality() == 6


def test_the_skyscraper_has_the_presentation_that_defines_it() -> None:
    r"""``O --x--> O -> O_origin -> 0`` on the affine line."""
    line, algebra, x, sheaves, structure, multiply_by_x = _line_and_multiplication()
    origin_sheaf = sheaves.associated_sheaf(FinitelyPresentedModule(multiply_by_x))

    presentation = sheaves.local_presentation(origin_sheaf)
    assert presentation.domain().module_generating_set().cardinality() == 1
    assert presentation.codomain().module_generating_set().cardinality() == 1
    # The presenting relation is multiplication by x, so the presented sheaf is
    # killed by x while its degree-zero free sheaf is not.
    presented = sheaves.global_sections(origin_sheaf)
    generator = presented.module_generator(0)
    assert generator != presented.zero()
    assert presented.scalar_multiple(x, generator) == presented.zero()
