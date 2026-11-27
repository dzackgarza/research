# Regression Tests — Rings Spec

These files prove that the `Rings()` spec does not break existing Sage code.
Each test takes a constructor that previously worked through bare Sage (`ZZ`, `QQ`, `GF(p)`, etc.) and runs the same documented examples through the spec-wrapped call (`Rings().Constructors().X(...)`).  If anything breaks, the spec has introduced a regression.

Every assertion was copied verbatim from the Sage source doctests cited below; no values were invented.
No `try/except` — a failure is a finding.

| File | Sage source |
| --- | --- |
| `named_ring_constructors.sage` | all modules below (identity + category membership overview) |
| `integer_ring.sage` | `sage.rings.integer_ring`, `sage.rings.integer` |
| `rational_field.sage` | `sage.rings.rational_field`, `sage.rings.rational` |
| `finite_fields.sage` | `sage.rings.finite_rings` |
| `integer_mod_rings.sage` | `sage.rings.finite_rings.integer_mod_ring` |
| `number_fields.sage` | `sage.rings.number_field.number_field` |
| `padic_rings.sage` | `sage.rings.padics` |
| `polynomial_rings.sage` | `sage.rings.polynomial` |
| `power_series_rings.sage` | `sage.rings.power_series_ring`, `sage.rings.laurent_series_ring`, `sage.rings.puiseux_series_ring` |
| `real_and_complex_fields.sage` | `sage.rings.real_mpfr`, `sage.rings.complex_mpfr`, `sage.rings.real_double`, `sage.rings.complex_double`, `sage.rings.real_interval_field`, `sage.rings.complex_interval_field` |
| `matrix_rings.sage` | `sage.matrix.matrix_space` |
