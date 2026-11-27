# Rings Triage

Source for the current documentation pass: `rings/docs/SAGE_INVENTORY.md`,
`rings/docs/MAPPING.md`, Sage written category docs, and local Sage category source.

This file records the current `rings/smoketest.sage` frontier. The smoke is expected
to fail until the listed missing surfaces and structural blockers are implemented.

## Category Base-Class Mismatch

These constructors currently fail while refining through nested axiom categories.
The error reports matching class names with nonmatching class identity, so this is a
category-construction/cache boundary issue, not a missing ring method.

- `_IntegralDomains` over `_CommutativeRings`:
  `Rings().Constructors().ZZ()`
- `_Fields` over `_CommutativeRings`:
  `Rings().Constructors().QQ()`, `QQbar()`, `AA()`, `RR()`, `CC()`, `RDF()`,
  `CDF()`, `RIF()`, `CIF()`, `RealField(100)`, `ComplexField(100)`,
  `RealBallField(100)`, `ComplexBallField(100)`, `GF(5)`,
  `NumberField(x^3 - 2, 'a')`, `QuadraticField(5, 'a')`, and
  `CyclotomicField(5)`.
- `_CompleteRings` over `_TopologicalRings`:
  `Rings().Constructors().Zp(5)`, `Qp(5)`, `Zq((5, 2), names='a')`, and
  `Qq((5, 2), names='a')`.

## Missing `_sympy_`

These constructors refine far enough to expose the next missing Sage/project method:

- `Rings().Constructors().IntegerModRing(6)`
- `Rings().Constructors().PolynomialRing(ZZ, name='t')`
- `Rings().Constructors().PowerSeriesRing(ZZ, 't')`
- `Rings().Constructors().LaurentSeriesRing(ZZ, 't')`
- `Rings().Constructors().PuiseuxSeriesRing(QQ, 't')`
- `Rings().Constructors().MatrixRing(ZZ, 2)`

## Current Blocker Groups

The current ring smoke failures are implementer-facing: the next work is either fixing
the category-base identity mismatch in the axiom construction path or implementing the
listed missing `_sympy_` surface on the relevant refined parents.

## Matrix Algebra Surface Split

Matrix-algebra ownership is no longer a root decision. The constructor may remain
reachable as `Rings().Constructors().MatrixRing(...)` because Sage constructs a square
matrix space that is also a ring object. The resulting object must refine into
`Algebras(R)` and `Modules(R).Free().FiniteRank()`.

The remaining work is a surface split: ring-only constructor and object-routing glue
stays in `rings`, algebra-specific methods move to `algebras`, and free-module or
matrix-space linear methods move to `modules`. Do not hide this by moving or weakening
the matrix smoke.
