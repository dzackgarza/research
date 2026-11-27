"""Refine Sage's quotient codomains ``QQ/ZZ`` and ``QQ/nZZ`` as modules.

Sage already owns the quotient-class arithmetic through ``QmodnZ``.  This
patch keeps that arithmetic as the backend and only records the missing module
category semantics needed by form codomains.
"""

from __future__ import annotations

from sage.all import QQ, ZZ, Modules
from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.rings.ideal import Ideal_generic
from sage.rings.integer_ring import IntegerRing_class
from sage.rings.rational_field import RationalField
from sage.structure.parent import Parent

_native_rational_field_truediv = RationalField.__truediv__
_installed = False


def refine_fraction_quotient(parent: QmodnZ) -> QmodnZ:
    r"""Refine a Sage ``QmodnZ`` parent as a ``ZZ``-module."""

    assert parent.base_ring() is ZZ, "fraction quotient codomain must be a ZZ-module"
    parent._refine_category_(Modules(ZZ))
    return parent


def _quotient_codomain_truediv(
    self: RationalField,
    denominator: IntegerRing_class | Ideal_generic,
) -> Parent:
    quotient = _native_rational_field_truediv(self, denominator)
    match quotient:
        case QmodnZ():
            return refine_fraction_quotient(quotient)
        case _:
            return quotient


def install() -> None:
    r"""Install the ``QQ/ZZ`` and ``QQ/nZZ`` module-codomain refinement."""

    global _installed
    if _installed:
        return

    RationalField.__truediv__ = _quotient_codomain_truediv
    refine_fraction_quotient(QQ / ZZ)
    refine_fraction_quotient(QQ / (2 * ZZ))
    _installed = True
