# flatter Online Provenance Snapshot (2026-02-17 UTC)

Scope: first-class checklist/reference surface creation for `flatter`.

---

## 1. Sources surveyed

- Repository and canonical CLI documentation:
  - `https://github.com/keeganryan/flatter`

---

## 2. Extracted method/command surface

From README usage section:

- Main command:
  - `flatter [OPTION] [INPUT_FILE [OUTPUT_FILE]]`
- Documented options (constraints NOT explicitly stated in upstream README):
  - `-a ALPHA` — reduction parameter; no explicit range documented in upstream. Code default is `0.06250805094100162` (RHF 1.0219).
  - `-rhf R` — root-Hermite factor parameter; no explicit range documented in upstream.
  - `-logcond C` — log-condition number parameter; no explicit range documented in upstream.
  - `-p PREC` — precision in bits; no explicit range documented in upstream. Code default is `0` (auto mode).
  - `-t THRS` — thread count; no explicit range documented in upstream. Code default is `1`.
  - `-v`, `-q`, `-h` — verbose, quiet, help flags.
- **NOTE**: Previous versions of this provenance file incorrectly claimed explicit range constraints. The upstream README only describes parameter purposes, not valid ranges.
- Input/output contract:
  - integer matrix text format,
  - default `stdin`/`stdout` behavior if file paths are omitted.

From README benchmark/testing section:

- `./test.sh`
- `./test_perf.py [NTRIALS] [NROWS] [START_R] [STEP_R]`
- `make test`

---

## 3. Domain notes captured for docs

- `flatter` is positioned as a Euclidean floating-point lattice reduction tool.
- No upstream surface advertises indefinite arithmetic-form genus/isometry APIs.
