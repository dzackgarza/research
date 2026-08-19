"""FormCodomain — typed descriptor for form value codomains.

Provides integral, rational, torsion_bilinear, and torsion_quadratic codomain
constructors. Uses Phase 0 Sage patches for QQ/ZZ and QQ/2ZZ quotient modules.
"""

from __future__ import annotations

from typing import Any

from sage.all import QQ, ZZ


class FormCodomain:
    """Typed descriptor for form values living in a codomain S over base ring R."""

    def __init__(self, base_ring: Any, codomain: Any) -> None:
        self._base_ring = base_ring
        self._codomain = codomain

    def base_ring(self) -> Any:
        return self._base_ring

    def codomain(self) -> Any:
        return self._codomain

    def coerce(self, value: Any) -> Any:
        return self._codomain(value)

    def __repr__(self) -> str:
        return f"FormCodomain({self._base_ring} -> {self._codomain})"

    @staticmethod
    def integral(R: Any) -> FormCodomain:
        return FormCodomain(R, R)

    @staticmethod
    def rational(R: Any) -> FormCodomain:
        if R is ZZ:
            return FormCodomain(R, QQ)
        return FormCodomain(R, R.fraction_field())

    @staticmethod
    def torsion_bilinear(R: Any) -> FormCodomain:
        if R is ZZ:
            import src.sage_patches.fraction_quotients as fq

            fq.install()
            return FormCodomain(R, QQ / ZZ)
        raise NotImplementedError(f"torsion_bilinear not implemented for {R}")

    @staticmethod
    def torsion_quadratic(R: Any) -> FormCodomain:
        if R is ZZ:
            import src.sage_patches.fraction_quotients as fq

            fq.install()
            return FormCodomain(R, QQ / (2 * ZZ))
        raise NotImplementedError(f"torsion_quadratic not implemented for {R}")
