r"""Non-toric coherent cohomology from affine acyclicity."""

from dzack_research.preamble.all import QQ, Spec
from dzack_research.preamble.categories.modules.cochain_complexes import CochainComplexes
from dzack_research.preamble.categories.schemes.geometric_cohomology import (
    AffineCoverRefinementCohomologyMap,
    AffineGeometricCohomology,
    AffineGeometricCohomologyComplex,
    AffineGeometricCohomologyComplexes,
    AffineGeometricScalarCohomologyMap,
)


def _dual_number_sheaf():
    polynomial = QQ.polynomial_ring("e")
    e = polynomial.algebra_generator("e")
    algebra = polynomial.quotient_ring(polynomial.ideal(e**2))
    scheme = Spec(algebra, base_ring=QQ)
    module = algebra.free_module(1)
    return scheme.associated_module_sheaf(module)


def test_nonreduced_affine_scheme_has_actual_geometric_cohomology_complex() -> None:
    sheaf = _dual_number_sheaf()
    complex_ = AffineGeometricCohomologyComplex(sheaf)
    h0 = AffineGeometricCohomology(sheaf, 0)
    h1 = AffineGeometricCohomology(sheaf, 1)

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
    h0 = AffineGeometricCohomology(sheaf, 0)
    induced = AffineGeometricScalarCohomologyMap(sheaf, 0, QQ(2))
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
    comparison = AffineCoverRefinementCohomologyMap(refinement, sheaf, 0)

    assert comparison.source_complex().geometric_cover() is coarse
    assert comparison.target_complex().geometric_cover() is refinement.fine_cover()
    assert comparison.cochain_map().domain() is comparison.source_complex()
    assert comparison.cochain_map().codomain() is comparison.target_complex()

    source = comparison.cohomology_map().domain()
    generator = source.module_generator(next(iter(source.module_generating_set())))
    assert comparison.cohomology_map()(generator) != comparison.cohomology_map().codomain().zero()

    source_complex = comparison.source_complex()
    target_complex = comparison.target_complex()
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
        target_times_two(comparison.cohomology_map()(generator))
        == comparison.cohomology_map()(source_times_two(generator))
    )
