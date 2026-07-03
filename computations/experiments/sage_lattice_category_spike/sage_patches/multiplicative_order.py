r"""Sage upstream defect: ``identity_matrix(ZZ, n).multiplicative_order()``
raises ``IndexError: list index out of range`` (Factorization indexing inside
the order computation) — the multiplicative order of the identity is ``1``.

Observed 2026-07-04 while enumerating an isometry subgroup (gap-ledger row
19a). ``Matrix`` is a cython extension type, so the method cannot be
monkey-patched in place; this corrected callable is the re-export owned code
calls instead of the method.
"""

from sage.rings.integer_ring import ZZ


def multiplicative_order(matrix):
    r"""``matrix.multiplicative_order()`` with the identity case corrected."""
    if matrix.is_one():
        return ZZ.one()
    return matrix.multiplicative_order()
