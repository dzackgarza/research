# latticegen (fplll) Online Provenance Capture (2026-02-19)

Date captured: 2026-02-19
Assignment context: documentation coverage audit for in-scope lattice-theory methods.

## Canonical sources used

- fplll README.md (latticegen section):
  - `https://raw.githubusercontent.com/fplll/fplll/master/README.md`
- fplll latticegen.cpp source:
  - `https://raw.githubusercontent.com/fplll/fplll/master/fplll/latticegen.cpp`
- fplll Doxygen reference:
  - `https://fplll.github.io/fplll/latticegen_8cpp.html`

## Signature fidelity notes captured

- All command signatures verified against `print_help()` in `latticegen.cpp` and README.md.
- Method selectors for `n`, `N`, `q` confirmed as single-character values:
  - `n` / `N`: `c` in `{'b', 'q'}`
  - `q`: `c` in `{'b', 'q', 'p'}`
- `-randseed` option confirmed to accept either integer or literal `time`.
- `--help` and `--version` flags confirmed in source but not surfaced in `print_help()`.

## Semantic notes from README

- `r d b`: knapsack-like matrix (d x (d+1))
- `s d b b2`: simultaneous Diophantine approximation structure
- `u d b`: uniform random entries
- `n d b c`: NTRU-like matrix [[I, Rot(h)], [0, q*I]]
- `N d b c`: NTRU-like alternate [[q*I, 0], [Rot(h), I]]
- `q d k b c`: q-ary SIS/LWE lattice; Goldstein-Mayer when k=1 and q prime
- `t d f`: triangular with geometric decay B_ii = 2^((d-i+1)^f)
- `T d`: triangular with weights from stdin

## Scope gate note

Only the fplll latticegen CLI is in scope. The Python package `latticegen` (TAdeJong/moire-lattice-generator) is for moire pattern image synthesis and does not provide bilinear-form lattice-theoretic APIs; it is out of scope.
