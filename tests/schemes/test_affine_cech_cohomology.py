r"""Non-toric coherent cohomology from affine acyclicity."""

from dzack_research.preamble.all import FreeModule, PolynomialRing, QQ, QuotientRing, Spec
from dzack_research.preamble.categories.schemes.geometric_cohomology import (
    AffineGeometricCohomology,
    AffineGeometricCohomologyComplex,
    AffineGeometricCohomologyComplexes,
    AffineGeometricScalarCohomologyMap,
)


def _dual_number_sheaf():
    polynomial = PolynomialRing(QQ, "e")
    e = polynomial.algebra_generator("e")
    algebra = QuotientRing(polynomial, polynomial.ideal(e**2))
    scheme = Spec(algebra, base_ring=QQ)
    module = FreeModule(algebra, 1)
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
    generator = h0.module_generator(next(iter(h0.module_generating_set())))

    assert induced.domain() is h0
    assert induced.codomain() is h0
    assert induced(generator) == QQ(2) * generator
