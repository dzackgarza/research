r"""Isolated subtree for corrections to Sage upstream defects.

Gap-ledger entry-6 protocol: a suspected Sage bug is a filed issue plus a
ledger row, never an inline workaround scattered through owned domain code.
Every correction lives HERE, one module per upstream defect, in one of two
forms:

- **monkey-patch**: mutates the Sage surface at import of this package (none
  currently exist — the known defects sit on cython extension types, which
  are immutable, so they cannot be patched in place);
- **re-export**: a corrected callable that owned code calls INSTEAD of the
  defective Sage method; the defect documentation lives on the callable.

Import guarantee: the spike package imports this subtree at its own import,
and the test conftest imports it again explicitly, so every consumer and
every test run carries all patches. Owned domain code never encodes an
upstream-defect correction inline; it routes through this namespace.
"""

from .multiplicative_order import multiplicative_order

__all__ = ["multiplicative_order"]
