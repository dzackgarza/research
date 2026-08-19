# latticegen Reference
## fplll latticegen CLI for lattice basis instance generation

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[GEN]` | Instance generation |
| `[ZZMOD]` | Integer-basis lattice setting |
| `[EUCLID]` | Euclidean lattice benchmark setting |

---

## 1. Scope and Naming Collision

"latticegen" refers to two different ecosystems:

1. **IN SCOPE**: `fplll` ecosystem utility (`latticegen`) for lattice basis instance generation (benchmark/reduction pipelines). This CLI generates integer lattice bases for LLL/BKZ/SVP/CVP benchmarking and operates on free Z-modules used in bilinear-form lattice reduction workflows.
2. **OUT OF SCOPE**: Python package `latticegen` (`TAdeJong/moire-lattice-generator`) for moire lattice image synthesis/analysis. This package targets image processing and does not provide bilinear-form lattice-theoretic APIs per the project scope definition.

This file documents only the in-scope fplll latticegen CLI.

---

## 2. fplll latticegen (benchmark instance generator)

### 2.1 What it is

`latticegen` in `fplll` is a command-line generator for integer lattice bases used with LLL/BKZ/SVP/CVP benchmarking.

### 2.2 Typical usage

- Generate instance with `latticegen ...`
- Pipe/read into `fplll`/`fpylll` for reduction or search

### 2.3 Global options

| Flag | Arguments | Description |
|------|-----------|-------------|
| `-randseed` | `<int>` or `time` | Seed for reproducibility. Must be first option if used. |
| `--help` | none | Print usage help |
| `--version` | none | Print version info |

### 2.4 Generator methods

`latticegen [-randseed <int|time>] <method> <args...>`

| Method | Arguments | Generator | Semantics |
|--------|-----------|-----------|-----------|
| `r` | `<d> <b>` | `gen_intrel` | Knapsack-like matrix of dimension d x (d+1): i-th row starts with random integer of bit-length ≤b, followed by i-th canonical unit vector. |
| `s` | `<d> <b> <b2>` | `gen_simdioph` | Simultaneous Diophantine approximation structure: first row starts with random integer of bit-length ≤b2 followed by d-1 integers of bit-length ≤b; i-th row for i>1 is i-th canonical unit vector scaled by 2^b. |
| `u` | `<d> <b>` | `gen_uniform` | Uniform random d x d matrix with entries of bit-length ≤b. |
| `n` | `<d> <b> <c>` | `gen_ntrulike` / `gen_ntrulike_bits` | NTRU-like matrix [[I, Rot(h)], [0, q*I]] (2d x 2d). Selector `c='b'` samples q with bit-length b; `c='q'` uses provided q value. Warning: not a genuine NTRU public key. |
| `N` | `<d> <b> <c>` | `gen_ntrulike2` / `gen_ntrulike2_bits` | NTRU-like alternate [[q*I, 0], [Rot(h), I]] (2d x 2d). Same selector semantics as `n`. |
| `q` | `<d> <k> <b> <c>` | `gen_qary` / `gen_qary_bits` / `gen_qary_prime` | q-ary (SIS/LWE) matrix [[I, H], [0, q*I]] where H is (d-k) x k uniform mod q. Selector: `c='b'` samples q of bit-length b; `c='p'` samples then updates to smallest prime ≥q; `c='q'` uses provided value. Goldstein-Mayer lattices: k=1, q prime. |
| `t` | `<d> <f>` | `gen_trg` | Lower-triangular d x d matrix with B_ii = 2^((d-i+1)^f) and B_ij uniform in [-B_jj/2, B_jj/2] for j<i. |
| `T` | `<d>` | `gen_trg2` | Lower-triangular d x d matrix with diagonal B_ii = vec[i] read from stdin, off-diagonal uniform as in `t`. |

Selector values in source:

- For `n` / `N`: `c in {'b','q'}`.
- For `q`: `c in {'b','q','p'}`.

| Option family | Purpose | Tags |
|---------------|---------|------|
| random/uniform style families | Synthetic random lattice bases | `[GEN, ZZMOD, EUCLID]` |
| knapsack/NTRU-style families | Structured cryptanalytic benchmark lattices | `[GEN, ZZMOD, EUCLID]` |
| dimension/seed controls | Reproducible scaling studies | `[GEN]` |

---

## 3. Selection Guide

Use `fplll latticegen` when you need:

- integer basis instances,
- reduction benchmark corpora,
- cryptanalytic test lattices for `fpylll`/`fplll`.

---

## 4. Out-of-Scope Reference: Python `latticegen` (moire package)

The PyPI package `latticegen` (`TAdeJong/moire-lattice-generator`) is for moire lattice image synthesis and does not provide bilinear-form lattice-theoretic APIs. It is **out of scope** for this project's documentation coverage. Documented here only to prevent naming collision confusion.

---

## 5. Sources

### Local upstream snapshots

- `docs/latticegen/upstream/latticegen_online_provenance_2026-02-19.md`

### Canonical upstream

- fplll README.md: https://raw.githubusercontent.com/fplll/fplll/master/README.md
- fplll `latticegen.cpp`: https://raw.githubusercontent.com/fplll/fplll/master/fplll/latticegen.cpp
- fplll Doxygen: https://fplll.github.io/fplll/latticegen_8cpp.html
- fplll repository: https://github.com/fplll/fplll
