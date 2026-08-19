# flatter Lattice Method Reference
## Floating-point LLL-style reduction CLI

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[CLI]` | Command-line interface |
| `[EUCLID]` | Euclidean lattice setting |
| `[RED]` | Reduction workflow |
| `[UTIL]` | Benchmark/test utility surface |

---

## 1. Scope

`flatter` is an open floating-point lattice-basis reduction package with a CLI-centric interface.

Primary surface:

- `flatter` command with reduction-control options,
- repository benchmark/test scripts for reproducible runs.

Not in scope:

- indefinite arithmetic-form classification APIs.

---

## 2. CLI Surface

Upstream README (`docs/flatter/upstream/README.md`) documents the main command and options.

Full usage line (verbatim from `flatter -h`):
```
flatter [-h] [-v] [-alpha ALPHA | -rhf RHF | -delta DELTA] [-logcond LOGCOND] [INFILE [OUTFILE]]
```

**Reduction-quality flags are mutually exclusive** (at most one may be given). Default when none is specified: `rhf = 1.0219`.

| Command / option | Argument Types | Return Type | Description | Tags |
|------------------|----------------|-------------|-------------|------|
| `flatter [OPTION] [INPUT_FILE [OUTPUT_FILE]]` | `OPTION`: flags, `INPUT_FILE`: str (optional, default stdin), `OUTPUT_FILE`: str (optional, default stdout) | integer matrix in FPLLL format (stdout) | Main reduction command; input/output in FPLLL integer-matrix format. Source: `docs/flatter/upstream/README.md` | `[CLI, EUCLID, RED]` |
| `-a ALPHA` / `-alpha ALPHA` | `ALPHA`: float | CLI flag | Reduction-quality parameter alpha (mutual-exclusive with `-rhf`, `-delta`). **Constraint not documented in upstream**; source code accepts any value without validation. Default is `0.06250805094100162` (corresponds to RHF 1.0219). Example output shows `alpha = 0` for achieved quality and `alpha = 0.0625081` for target. Source: `docs/flatter/upstream/README.md` | `[CLI, EUCLID, RED]` |
| `-rhf RHF` | `RHF`: float | CLI flag | Reduction-quality parameter: root-Hermite factor (mutual-exclusive with `-alpha`, `-delta`). **Constraint not documented in upstream**; mathematically RHF should be > 1 for meaningful reduction (alpha = 2*log2(RHF)). Default value `1.0219` when no quality flag is given. Source: `docs/flatter/upstream/README.md` | `[CLI, EUCLID, RED]` |
| `-delta DELTA` | `DELTA`: float | CLI flag | Reduction-quality parameter: analogous to LLL with this delta value (approximate; mutual-exclusive with `-alpha`, `-rhf`). **Constraint not documented in upstream**. Source code computes alpha = (0.255 / DELTA)^2. Source: `docs/flatter/upstream/README.md` | `[CLI, EUCLID, RED]` |
| `-logcond LOGCOND` | `LOGCOND`: float | CLI flag | Bound on the log condition number; separate from the reduction-quality group above. **Constraint not documented in upstream**. Source: `docs/flatter/upstream/README.md` | `[CLI, EUCLID, RED]` |
| `-p PREC` | `PREC`: int | CLI flag | Precision in bits. **Constraint not documented in upstream**. Default `0` uses auto mode. | `[CLI, EUCLID, RED]` |
| `-p` | — | CLI flag | Output profiles (print base-2 log of Gram-Schmidt norms for input and output bases). Source: `docs/flatter/upstream/README.md` | `[CLI, EUCLID]` |
| `-t THRS` | `THRS`: int | CLI flag | Number of threads. **Constraint not documented in upstream**. Default `1`. | `[CLI, EUCLID, RED]` |
| `-v` | — | CLI flag | Verbose output (print timing, input/output lattice info). Source: `docs/flatter/upstream/README.md` | `[CLI, EUCLID]` |
| `-q` | — | CLI flag | Quiet mode; do not output the reduced lattice (suppress matrix output). Source: `docs/flatter/upstream/README.md` | `[CLI, EUCLID]` |
| `-h` | — | CLI flag | Print help message. Source: `docs/flatter/upstream/README.md` | `[CLI]` |

Input/output contract documented by README:

- Input/output matrix entries are integer and represented in FPLLL plain-text format.
- Without explicit files, command reads from `stdin` and writes to `stdout`.

---

## 3. Utility Scripts

| Script / command | Argument Types | Return Type | Description | Tags |
|------------------|----------------|-------------|-------------|------|
| `./test.sh` | — | None | Repository test helper script. | `[UTIL]` |
| `./test_perf.py [NTRIALS] [NROWS] [START_R] [STEP_R]` | `NTRIALS`: int (optional), `NROWS`: int (optional), `START_R`: int (optional), `STEP_R`: int (optional) | benchmark output | Performance benchmark helper with optional dimensional controls. | `[UTIL, EUCLID, RED]` |
| `make test` | — | None | Build-system test target. | `[UTIL]` |

---

## 4. Domain Caveat

`flatter` is a Euclidean reduction package and does not expose indefinite-form genus/discriminant/isometry contracts.

---

## 5. Sources

- flatter repository/readme: `https://github.com/keeganryan/flatter`
- local provenance snapshot: `docs/flatter/upstream/flatter_online_provenance_2026-02-17.md`
