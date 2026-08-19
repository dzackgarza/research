# g6k Online Provenance Snapshot (2026-02-17 UTC)

Scope: first-class checklist/reference surface creation for the `g6k` lattice-reduction package.

---

## 1. Sources surveyed

- Repository and usage/examples:
  - `https://github.com/fplll/g6k`
- Core Python API declarations:
  - `https://raw.githubusercontent.com/fplll/g6k/master/g6k/siever.pyx`

---

## 2. Extracted method/command surface

From repository README usage and script sections:

- Script workflows:
  - `full_sieve.py`
  - `hkz.py`
  - `hkz_maybe.py`
  - `bkz.py`
  - `svp_challenge.py`
  - `svp_exact.py`
  - `svp_exact_find_norm.py`
  - `lwe_challenge.py`
- Shared script flags/examples:
  - `--threads`
  - `--verbose`
  - `--seed`
  - generic override form `--PARAM VAL`

From `g6k/siever.pyx` public class/method declarations and docstrings:

- `Siever(A, params=None, seed=None)`
- `initialize_local(ll, l, r)`
- `__call__(alg=None, tracer=None, **kwds)` (README runtime usage: `g6k(alg="gauss")`)
- `itervalues()`
- `__contains__(x)`
- `insert(kappa, x)`
- `best_lifts()`
- `db_size(compressed=False)`
- `shrink_db(size)`
- `lll(start, stop)`
- `extend_left(lp)`, `shrink_left(lp)`
- `extend_right(rp)`, `shrink_right(rp)`
- `resize_db(new_size)`
- `global_histo_update(value)`
- parameter helpers: `SieverParams(...)`, `load_siever_params(...)`

---

## 3. Domain notes captured for docs

- Package is a Euclidean lattice reduction/sieving stack (SVP/BKZ-family research workflows).
- No canonical upstream documentation surface indicates indefinite arithmetic-form genus/isometry API contracts.
