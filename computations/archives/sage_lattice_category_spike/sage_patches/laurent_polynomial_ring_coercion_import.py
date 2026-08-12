r"""Sage upstream defect: cold coercion touching Laurent polynomial rings raises
``AttributeError: module 'sage.rings.polynomial' has no attribute
'laurent_polynomial_ring'``.

A coercion/pushout branch tests ``isinstance(R,
sage.rings.polynomial.laurent_polynomial_ring.LaurentPolynomialRing_mpair)`` by
resolving ``laurent_polynomial_ring`` as an ATTRIBUTE of the already-imported
``sage.rings.polynomial`` package. Under a bare ``sage -python`` process the
submodule is not auto-imported, so the attribute does not exist yet and the
``isinstance`` check raises before anything can trigger the lazy load. Full
``sage`` startup imports enough that the attribute is always present, which hides
the defect there.

Observed 2026-07-04: ``lc.Lattice("A2").discriminant_group().brown_invariant()``
(an odd-prime discriminant form, whose Gauss-sum evaluation enters the offending
coercion branch) raised on the FIRST such call of a fresh process, while trivial
and 2-adic forms did not — so whether it fired depended on test collection order.
Minimal repro (no spike): the same brown-invariant call on Sage's own
``IntegralLattice(matrix(ZZ,2,[2,1,1,2]))`` raises cold and succeeds once the
submodule is imported.

Form: this is neither a monkey-patch nor a re-export but the third correction
kind — a one-line EAGER IMPORT that loads the lazy submodule so the attribute
resolves for every subsequent cold coercion. Importing this subtree at package
import (and again in the test conftest) guarantees the load happens before any
owned lattice object evaluates a Gauss sum.
"""

import sage.rings.polynomial.laurent_polynomial_ring  # noqa: F401  (eager load; see module docstring)
