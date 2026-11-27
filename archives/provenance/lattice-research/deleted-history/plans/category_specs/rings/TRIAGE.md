# Rings Triage

Source: `sage /home/dzack/research/plans/category_specs/rings/smoketest.sage`

This file records the ring-side failures exposed by the current smoke test. In every case below, Sage successfully constructs the upstream ring object, and the failure happens during refinement because the current spec surface requires methods that the refined object does not implement.

## Missing `completion`

These constructors fail with `AssertionError: Not implemented method: completion`.

- `Rings().NamedRings().RR()`
- `Rings().NamedRings().CC()`
- `Rings().NamedRings().RDF()`
- `Rings().NamedRings().CDF()`
- `Rings().NamedRings().RIF()`
- `Rings().NamedRings().CIF()`
- `Rings().NamedRings().RealField(100)`
- `Rings().NamedRings().ComplexField(100)`
- `Rings().NamedRings().RealBallField(100)`
- `Rings().NamedRings().ComplexBallField(100)`
- `Rings().NamedRings().Zp(5)`
- `Rings().NamedRings().Qp(5)`
- `Rings().NamedRings().Zq((5, 2), names='a')`
- `Rings().NamedRings().Qq((5, 2), names='a')`

## Missing `gcd`

These constructors fail with `AssertionError: Not implemented method: gcd`.

- `Rings().NamedRings().ZZ()`
- `Rings().NamedRings().QQbar()`
- `Rings().NamedRings().AA()`
- `Rings().NamedRings().GF(5)`
- `Rings().NamedRings().NumberField(x^3 - 2, 'a')`
- `Rings().NamedRings().CyclotomicField(5)`

## Missing `S_class_group`

This constructor fails with `AssertionError: Not implemented method: S_class_group`.

- `Rings().NamedRings().QQ()`

## Missing `is_algebraically_closed`

These constructors fail with `AssertionError: Not implemented method: is_algebraically_closed`.

- `Rings().NamedRings().IntegerModRing(6)`
- `Rings().NamedRings().PolynomialRing(ZZ, 't')`

## Missing `Aut`

This constructor fails with `AssertionError: Not implemented method: Aut`.

- `Rings().NamedRings().QuadraticField(5, 'a')`

## Missing `extension`

These constructors fail with `AssertionError: Not implemented method: extension`.

- `Rings().NamedRings().PowerSeriesRing(ZZ, 't')`
- `Rings().NamedRings().LaurentSeriesRing(ZZ, 't')`
- `Rings().NamedRings().PuiseuxSeriesRing(QQ, 't')`

## Missing `End`

This constructor now fails with `AssertionError: Not implemented method: End`.

- `Rings().NamedRings().MatrixRing(ZZ, 2)`

This changed after removing module-theoretic redeclarations from the
matrix-algebra ring spec. The previous `annihilator` failure was a spec
placement error in `rings/constructions.py`; once matrix algebras inherit
their module surface instead of redeclaring it locally, refinement reaches
the next real missing surface on the Sage object.

## Consequence

The ring subtree now has a precise missing-method inventory for the constructors exercised by the smoke test. The next pass should decide, method by method, whether the spec is correct and Sage needs adaptation, or whether the method currently sits on the wrong ring subcategory.

## Named Constructor Identity Notes

`RealField`, `ComplexField`, `RealIntervalField`, `ComplexIntervalField`, `RealBallField`, and `ComplexBallField` are constructor families parameterized by precision (and related options). `RR`, `CC`, `RIF`, and `CIF` are fixed named objects at Sage's default precision choices for their respective families.

Use exact identity statements rather than informal "equals" language:

- `RR is RealField(53)` is `True`.
- `CC is ComplexField(53)` is `True`.
- `RIF is RealIntervalField(53)` is `True`.
- `CIF is ComplexIntervalField(53)` is `True`.
- `RDF is RealField(53)` is `False`.
- `CDF is ComplexField(53)` is `False`.
- `RR is RDF` is `False`.
- `CC is CDF` is `False`.

Interpretation for spec work:

- `RR` / `CC` can have one-object category refinements.
- `RealField(...)` / `ComplexField(...)` and related precision families remain multi-object parameterized subcategories.
- `RDF` / `CDF` remain distinct one-object targets from the MPFR-backed `RealField` / `ComplexField` families.
