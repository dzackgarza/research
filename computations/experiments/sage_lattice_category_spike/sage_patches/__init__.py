r"""Isolated subtree for corrections to Sage upstream defects.

Gap-ledger entry-6 protocol: a suspected Sage bug is a filed issue plus a
ledger row, never an inline workaround scattered through owned domain code.
Every correction lives HERE, one module per upstream defect, in one of three
forms:

- **monkey-patch**: mutates the Sage surface at import of this package (none
  currently exist — the known defects sit on cython extension types, which
  are immutable, so they cannot be patched in place);
- **re-export**: a corrected callable that owned code calls INSTEAD of the
  defective Sage method; the defect documentation lives on the callable;
- **eager import**: forces a lazy Sage submodule to load at import of this
  package, so a cold coercion branch that resolves it as an attribute does not
  raise; the module is imported for its side effect only.

Import guarantee: the spike package imports this subtree at its own import,
and the test conftest imports it again explicitly, so every consumer and
every test run carries all patches. Owned domain code never encodes an
upstream-defect correction inline; it routes through this namespace.
"""

from . import laurent_polynomial_ring_coercion_import  # noqa: F401  (eager load; side effect only)
from .brown_indecomposable import brown_indecomposable
from .multiplicative_order import multiplicative_order

__all__ = ["brown_indecomposable", "multiplicative_order"]

__all__ = ["multiplicative_order"]
