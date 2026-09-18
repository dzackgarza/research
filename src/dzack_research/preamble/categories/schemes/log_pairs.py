r"""Log pairs \((X,\Delta)\) and the toric log pairs among them.

A log pair is a variety together with a chosen effective boundary divisor.
The pair is the object: neither the variety nor the divisor alone answers the
questions a log pair is asked, and the log canonical class \(K_X+\Delta\) is
the first of them.

For a toric variety the boundary is the sum of the torus-invariant prime
divisors, one for each ray of the fan, and Cox--Little--Schenck,
*Toric Varieties*, Thm. 8.2.3 gives \(K_X=-\sum_{\rho}D_\rho\).  The toric
boundary is therefore anticanonical, and \((X,\Delta_{\mathrm{toric}})\) is
log Calabi--Yau -- a statement this layer computes rather than asserts.
"""

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of


class LogPairs(OwnedCategoryOverBaseRing):
    r"""Pairs ``(X, Delta)`` of a variety and a chosen boundary divisor."""

    def an_object(self):
        r"""The projective plane with its toric boundary, a log Calabi--Yau pair."""
        from sage.rings.integer_ring import ZZ as SageZZ

        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
        from dzack_research.preamble.categories.schemes.toric.fans import (
            RationalPolyhedralFans,
        )

        cocharacters = _own_ring(SageZZ).free_module(2)
        plane = RationalPolyhedralFans(cocharacters).projective_space_fan().toric_variety(
            self.base_ring()
        )
        return plane.log_pair()

    def _call_(self, log_scheme, boundary_divisor):
        r"""The log pair ``(X, Delta)`` of a scheme over this base and a divisor on it."""
        assert log_scheme.scheme_base_ring() == self.base_ring(), (
            f"the scheme of an object of {self} lies over {self.base_ring()}"
        )
        return _object_of(self, log_scheme=log_scheme, boundary_divisor=boundary_divisor)

    def _repr_object_names(self):
        return f"log pairs over {self.base_ring()}"

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def __init__(self, log_scheme, boundary_divisor, **rest) -> None:
            self._log_scheme = log_scheme
            self._boundary_divisor = boundary_divisor
            super().__init__(**rest)

        def log_scheme(self):
            r"""The variety ``X`` of the pair."""
            return self._log_scheme

        def boundary_divisor(self):
            r"""The boundary ``Delta``."""
            return self._boundary_divisor

        def boundary_divisor_group(self):
            r"""The divisor group ``Delta`` is an element of."""
            return self.boundary_divisor().parent()

        def canonical_divisor(self):
            r"""The canonical divisor ``K_X``, asked of the variety."""
            return self.log_scheme().canonical_divisor()

        def log_canonical_divisor(self):
            r"""``K_X + Delta``, the class whose vanishing is log Calabi--Yau."""
            return self.canonical_divisor() + self.boundary_divisor()

        def is_log_calabi_yau(self) -> bool:
            r"""Whether ``K_X + Delta`` is the zero divisor."""
            return (
                self.log_canonical_divisor()
                == self.boundary_divisor_group().zero()
            )

        def _repr_(self) -> str:
            return f"Log pair ({self.log_scheme()}, {self.boundary_divisor()})"


class ToricLogPairs(OwnedCategoryOverBaseRing):
    r"""Log pairs whose variety is toric and whose boundary is torus-invariant."""

    def an_object(self):
        r"""The projective plane with the sum of its three invariant lines."""
        return LogPairs(self.base_ring()).an_object()

    def _call_(
        self,
        toric_variety,
        boundary_divisor,
        *,
        _engine=None,
        construction_data=None,
    ):
        r"""The toric log pair of a toric variety and a torus-invariant boundary."""
        assert toric_variety.scheme_base_ring() == self.base_ring(), (
            f"the variety of an object of {self} lies over {self.base_ring()}"
        )
        assert boundary_divisor.parent() is toric_variety.torus_invariant_divisor_group(), (
            "the boundary of a toric log pair is a torus-invariant divisor"
        )
        return _object_of(
            self,
            _engine=None if _engine is None else (self, _engine, None),
            log_scheme=toric_variety,
            boundary_divisor=boundary_divisor,
            **dict(construction_data or {}),
        )

    def _repr_object_names(self):
        return f"toric log pairs over {self.base_ring()}"

    def super_categories(self):
        return [LogPairs(self.base_ring())]

    class ParentMethods:
        def fan(self):
            r"""The fan of the variety of the pair."""
            return self.log_scheme().fan()

        def is_toric_boundary(self) -> bool:
            r"""Whether ``Delta`` is the full toric boundary ``sum_rho D_rho``."""
            return self.boundary_divisor() == self.log_scheme().toric_boundary_divisor()


def _log_pair(log_scheme, boundary_divisor):
    r"""The log pair of a variety and a chosen boundary divisor on it."""
    return LogPairs(log_scheme.scheme_base_ring())(log_scheme, boundary_divisor)


def _toric_log_pair(toric_variety, boundary_divisor):
    r"""The toric log pair of a toric variety and a torus-invariant boundary."""
    return ToricLogPairs(toric_variety.scheme_base_ring())(toric_variety, boundary_divisor)


__all__ = ["LogPairs", "ToricLogPairs"]
