"""Phase 3 end-state assertions for ``category_specs``.

These tests record mathematical behavior expected after concrete category
interceptors and constructor redefinitions are installed.
"""

from __future__ import annotations

import importlib

import pytest
from sage.all import QQ, ZZ
from sage.categories.ring_ideals import RingIdeals

importlib.import_module("category_specs")

rings = importlib.import_module("category_specs.rings")
sage_modules = importlib.import_module("category_specs.modules")

Rings = rings.Rings
Modules = sage_modules.Modules

# ---------------------------------------------------------------------------
# 1. Instantiation
# ---------------------------------------------------------------------------


class TestInstantiation:
    def test_pow_returns_free_module(self) -> None:
        M = ZZ**2
        assert M.rank() == 2
        assert M in Modules(ZZ).Free().FinitelyPresented()

    def test_quotient_returns_ring(self) -> None:
        Q = ZZ.quotient(6 * ZZ)
        assert Q in Modules(ZZ).FinitelyPresented()

    def test_ideal_returns_ideal(self) -> None:
        I = ZZ.ideal(6)
        assert I.gens() == (6,)
        assert I in RingIdeals(ZZ)


# ---------------------------------------------------------------------------
# 2. Seed enrollment + idempotent install
# ---------------------------------------------------------------------------


class TestSeedEnrollment:
    @pytest.mark.parametrize("R", [ZZ, QQ])
    def test_core_ring_is_refined(self, R: object) -> None:
        assert R in Rings()

    def test_gf_is_refined(self) -> None:
        from sage.all import GF

        assert GF(7) in Rings()

    def test_finite_field_alias_is_refined(self) -> None:
        from sage.all import FiniteField

        assert FiniteField(11) in Rings()

    def test_zp_is_refined(self) -> None:
        from sage.rings.padics.factory import Zp

        assert Zp(5) in Rings()

    def test_static_axiom_registration_is_idempotent(self) -> None:
        from category_specs.axioms import register_all

        register_all()
        register_all()
        assert ZZ in Rings()


# ---------------------------------------------------------------------------
# 3. Non-regression sanity
# ---------------------------------------------------------------------------


class TestNonRegression:
    def test_ideal_gens_round_trip(self) -> None:
        assert ZZ.ideal(6).gens() == (6,)

    def test_free_module_rank(self) -> None:
        assert (ZZ**2).rank() == 2

    def test_zp_precision_cap(self) -> None:
        from sage.rings.padics.factory import Zp

        assert Zp(5).precision_cap() > 0


# ---------------------------------------------------------------------------
# 4. Constructor-specific promotion contracts
# ---------------------------------------------------------------------------


class TestConstructorPromotion:
    def test_free_module_constructor_promotes_to_free_finitely_presented(self) -> None:
        from sage.modules.free_module import FreeModule

        M = FreeModule(ZZ, 3)
        assert M.rank() == 3
        assert M in Modules(ZZ).Free().FinitelyPresented()

    def test_vector_space_constructor_promotes_to_free_finitely_presented_over_field(
        self,
    ) -> None:
        from sage.modules.free_module import VectorSpace

        V = VectorSpace(QQ, 4)
        assert V.dimension() == 4
        assert V in Modules(QQ).Free().FinitelyPresented()
        assert V in Modules(QQ).OverField()

    def test_combinatorial_free_module_all_alias_promotes_only_to_free(self) -> None:
        from sage.all import CombinatorialFreeModule

        M = CombinatorialFreeModule(QQ, ZZ)
        assert M in Modules(QQ).Free()
        assert M not in Modules(QQ).FinitelyPresented()

    def test_matrix_space_all_alias_promotes_to_free_finitely_presented(self) -> None:
        from sage.all import MatrixSpace

        M = MatrixSpace(ZZ, 2, 3)
        assert M.nrows() == 2
        assert M.ncols() == 3
        assert M in Modules(ZZ).Free().FinitelyPresented()

    def test_univariate_polynomial_ring_over_field_is_ring(self) -> None:
        from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

        R = PolynomialRing(QQ, "x")
        assert R in Rings()

    def test_multivariate_polynomial_ring_over_field_is_not_promoted_to_pid(
        self,
    ) -> None:
        from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

        R = PolynomialRing(QQ, ("x", "y"))
        assert R not in Rings()

    def test_polynomial_ring_over_nonfield_is_not_promoted_to_pid(self) -> None:
        from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

        R = PolynomialRing(ZZ, "x")
        assert R not in Rings()

    def test_univariate_laurent_polynomial_ring_over_field_is_ring(self) -> None:
        from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing

        R = LaurentPolynomialRing(QQ, "x")
        assert R in Rings()

    def test_univariate_power_series_ring_over_field_is_ring(self) -> None:
        from sage.rings.power_series_ring import PowerSeriesRing

        R = PowerSeriesRing(QQ, "t")
        assert R in Rings()

    def test_integer_mod_ring_constructor_promotes_to_finitely_presented_zz_module(
        self,
    ) -> None:
        from sage.rings.finite_rings.integer_mod_ring import IntegerModRing

        R = IntegerModRing(9)
        assert R.order() == 9
        assert R in Modules(ZZ).FinitelyPresented()

    def test_number_field_constructor_promotes_field_and_preserves_integer_ring(
        self,
    ) -> None:
        from sage.all import QuadraticField
        from sage.categories.dedekind_domains import DedekindDomains

        K = QuadraticField(5, "a")
        assert K in Rings()
        OK = K.ring_of_integers()
        assert OK in DedekindDomains()
        assert Modules(OK) == Modules(OK).OverDedekindDomain()
