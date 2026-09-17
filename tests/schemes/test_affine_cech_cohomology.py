r"""Non-toric coherent cohomology from affine acyclicity."""

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.modules.cochain_complexes import CochainComplexes
from dzack_research.preamble.categories.schemes.geometric_cohomology import (
    AffineGeometricCohomologyComplexes,
)


def _dual_number_sheaf():
    polynomial = QQ.polynomial_ring("e")
    e = polynomial.algebra_generator("e")
    algebra = polynomial.quotient_ring(polynomial.ideal(e**2))
    scheme = (algebra).affine_spectrum(base_ring=QQ)
    module = algebra.free_module(1)
    return scheme.associated_module_sheaf(module)


def test_nonreduced_affine_scheme_has_actual_geometric_cohomology_complex() -> None:
    sheaf = _dual_number_sheaf()
    complex_ = sheaf.geometric_cohomology_complex()
    h0 = sheaf.geometric_cohomology(0)
    h1 = sheaf.geometric_cohomology(1)

    assert complex_ in AffineGeometricCohomologyComplexes(sheaf.module().base_ring())
    assert complex_.geometric_sheaf() is sheaf
    assert complex_.geometric_scheme() is sheaf.scheme()
    assert "affine" in complex_.acyclicity_reason()
    assert complex_.augmentation().domain() is complex_.graded_piece(0)
    assert complex_.augmentation().codomain() is sheaf.global_sections()
    assert h0.module_rank() == 1
    assert h1.is_zero()


def test_nonidentity_scalar_map_is_induced_through_the_affine_complex() -> None:
    sheaf = _dual_number_sheaf()
    h0 = sheaf.geometric_cohomology(0)
    induced = sheaf.geometric_scalar_cohomology_map(0, QQ(2))
    source = induced.domain()
    generator = source.module_generator(next(iter(source.module_generating_set())))

    assert h0.module_rank() == source.module_rank()
    assert induced(generator) == QQ(2) * generator


def test_unit_cover_refinement_has_an_actual_cochain_and_cohomology_comparison() -> None:
    sheaf = _dual_number_sheaf()
    scheme = sheaf.scheme()
    one = scheme.coordinate_algebra().one()
    coarse = scheme.distinguished_open_cover(one)
    repeated = scheme.distinguished_open_cover(one, one)
    refinement = coarse.common_refinement(repeated)
    cochain_map = refinement.geometric_cochain_map(sheaf)
    comparison = refinement.geometric_cohomology_comparison(sheaf, 0)

    assert cochain_map.domain().geometric_cover() is coarse
    assert cochain_map.codomain().geometric_cover() is refinement.fine_cover()
    assert comparison.domain() is CochainComplexes(cochain_map.domain().base_ring()).cohomology(0)(cochain_map.domain())
    assert comparison.codomain() is CochainComplexes(cochain_map.codomain().base_ring()).cohomology(0)(cochain_map.codomain())

    source = comparison.domain()
    generator = source.module_generator(next(iter(source.module_generating_set())))
    assert comparison(generator) != comparison.codomain().zero()

    source_complex = cochain_map.domain()
    target_complex = cochain_map.codomain()
    source_times_two = CochainComplexes(source_complex.base_ring()).cohomology(0)(
        QQ(2)
        * CochainComplexes(source_complex.base_ring()).Mor(
            source_complex, source_complex
        ).identity()
    )
    target_times_two = CochainComplexes(target_complex.base_ring()).cohomology(0)(
        QQ(2)
        * CochainComplexes(target_complex.base_ring()).Mor(
            target_complex, target_complex
        ).identity()
    )
    assert (
        target_times_two(comparison(generator))
        == comparison(source_times_two(generator))
    )
