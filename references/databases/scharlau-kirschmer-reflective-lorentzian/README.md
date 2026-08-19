# Scharlau–Kirschmer reflective Lorentzian lattice database

Third-party classification data, migrated 2026-08-20 from the
lattice-research corpus (`tests/fixtures/lorentzian_lattices.json`).

- **Source**: http://www.math.rwth-aachen.de/~Markus.Kirschmer/lorentz/index.html
- **Authors**: R. Scharlau and M. Kirschmer (n > 5); C. Walhorn (n = 4);
  I. Turkalj (n = 5)
- **Content**: 674 strongly squarefree reflective Lorentzian lattices, each
  record carrying signature, determinant, genus symbol, and Gram matrix
  (every record also repeats the source attribution inline).
- **Completeness**: complete for n = 4, 5; for n > 5 complete under the
  assumption that the determinant has no prime divisor greater than 19.

This is an external oracle for reflectivity and Vinberg-algorithm work. It
is reference data: never rewritten as repo mathematics, consumed read-only.
