"""
SPEC for the general indefinite lattice-isometry backend.

Tests in this file describe required future behavior. The filename keeps them
out of default pytest collection, and they must remain here, failing, until
the general DutSik-backed backend is implemented.
"""

from __future__ import annotations

from sage.all import IntegralLattice
from src.lattices.lattices import Lattice


class TestGeneralIndefiniteIsometrySpec:
    def test_odd_indefinite_basis_change_is_detected_as_an_isometry(self) -> None:
        native_left = IntegralLattice(3 * IntegralLattice("U").inner_product_matrix())
        first_basis_vector, second_basis_vector = tuple(native_left.basis())
        native_right = type(native_left)(
            native_left.ambient_module(),
            native_left.submodule((first_basis_vector, first_basis_vector + second_basis_vector)).basis_matrix(),
            native_left.inner_product_matrix(),
        )
        left = Lattice.from_gram(native_left.gram_matrix())
        right = Lattice.from_gram(native_right.gram_matrix())
        assert left.discriminant_group().is_p_elementary(3)
        assert not left.discriminant_group().is_p_elementary(2)
        assert left.discriminant_group().isomorphic_as_groups(right.discriminant_group())
        assert left.discriminant_group().is_isometric_to(right.discriminant_group())
        assert left.is_rationally_isometric_to(right)
        assert left.is_locally_isometric_to(right, 2)
        assert left.is_locally_isometric_to(right, 3)
        assert left.is_locally_isometric_to(right, 5)
        assert left.is_in_same_genus_as(right)
        assert left.is_isometric_to(right)
