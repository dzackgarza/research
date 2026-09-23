r"""Non-toric coherent cohomology from affine acyclicity."""

from dzack_research.preamble.all import QQ
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




