# g6k Lattice Method Reference
## General Sieve Kernel for high-dimensional Euclidean lattice reduction

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[CLI]` | Script/command-line surface |
| `[PY]` | Python API surface |
| `[EUCLID]` | Euclidean lattice setting |
| `[SVP]` | Shortest-vector/sieving workflow |
| `[BKZ]` | BKZ/HKZ reduction workflow |

---

## 1. Scope

`g6k` is an open lattice-reduction research stack centered on progressive sieving and BKZ/SVP challenge workflows.

Primary surface:

- script-driven experiments (`full_sieve`, `hkz`, `bkz`, challenge scripts),
- Python `Siever` API for local context, sieve database operations, and block-management primitives.

Not in scope:

- indefinite quadratic-form genus/isometry classification contracts.

---

## 2. Script and CLI Surface

The upstream README documents these script entry points and shared flag forms:

| Script / flag | Argument Types | Return Type | Description | Tags |
|---------------|----------------|-------------|-------------|------|
| `python full_sieve.py [--threads T] [--verbose V] [--seed S] d` | `T`: int, `V`: int, `S`: int, `d`: int | None (CLI) | Full progressive sieve run for dimension `d`. | `[CLI, EUCLID, SVP]` |
| `python hkz.py [--threads T] [--verbose V] [--seed S] d` | `T`: int, `V`: int, `S`: int, `d`: int | None (CLI) | HKZ-oriented reduction workflow. | `[CLI, EUCLID, BKZ]` |
| `python hkz_maybe.py [--threads T] [--verbose V] [--seed S] d` | `T`: int, `V`: int, `S`: int, `d`: int | None (CLI) | Alternative HKZ script workflow. | `[CLI, EUCLID, BKZ]` |
| `python bkz.py [options]` | `options`: various (keyword args) | None (CLI) | BKZ experiment script. | `[CLI, EUCLID, BKZ]` |
| `python svp_challenge.py [options]` | `options`: various (keyword args) | None (CLI) | SVP challenge workflow. | `[CLI, EUCLID, SVP]` |
| `python svp_exact.py [options]` | `options`: various (keyword args) | None (CLI) | Exact SVP workflow. | `[CLI, EUCLID, SVP]` |
| `python svp_exact_find_norm.py [options]` | `options`: various (keyword args) | None (CLI) | Exact-SVP norm-finding workflow. | `[CLI, EUCLID, SVP]` |
| `python lwe_challenge.py [options]` | `options`: various (keyword args) | None (CLI) | LWE challenge workflow using lattice reduction primitives. | `[CLI, EUCLID, BKZ]` |
| `--threads` / `--verbose` / `--seed` | `T`, `V`, `S`: int | CLI flag | Shared script flags documented in examples. | `[CLI, EUCLID]` |
| `--PARAM VAL` | `PARAM`: str, `VAL`: any | CLI flag | Generic parameter-override form documented for script invocation. | `[CLI, EUCLID]` |

---

## 3. Python API (`g6k.siever.Siever`)

Upstream README usage examples and `g6k/siever.pyx` method definitions provide the following public surface:

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `Siever(A, params=None, seed=None)` | `A`: numpy array/matrix, `params`: `SieverParams` (optional), `seed`: int (optional) | `Siever` object | Construct siever from basis matrix `A` and optional parameter object. | `[PY, EUCLID, SVP]` |
| `initialize_local(ll, l, r)` | `ll`: int, `l`: int, `r`: int | None | Initialize local sieving context/window with indices ll, l, r. | `[PY, EUCLID, SVP]` |
| `__call__(alg=None, tracer=None, **kwds)` | `alg`: str (optional), `tracer`: callable (optional), `**kwds`: various | None | Run sieve kernel in local context; README example uses `g6k(alg="gauss")`. | `[PY, EUCLID, SVP]` |
| `itervalues()` | — | iterator | Iterator over database vectors. | `[PY, EUCLID, SVP]` |
| `__contains__(x)` | `x`: vector | bool | Membership check in sieve database. | `[PY, EUCLID, SVP]` |
| `insert(kappa, x)` | `kappa`: int, `x`: vector | None | Insert transformed vector with insertion index `kappa`. | `[PY, EUCLID, SVP]` |
| `best_lifts()` | — | list | Return best database lifts by index. | `[PY, EUCLID, SVP]` |
| `db_size(compressed=False)` | `compressed`: bool (optional) | int | Return current database size (compressed or full view). | `[PY, EUCLID, SVP]` |
| `shrink_db(size)` | `size`: int | None | Shrink database to target size. | `[PY, EUCLID, SVP]` |
| `lll(start, stop)` | `start`: int, `stop`: int | None | Run LLL over local interval [start, stop). | `[PY, EUCLID, BKZ]` |
| `extend_left(lp)` / `shrink_left(lp)` | `lp`: int | None | Adjust left boundary of local window. | `[PY, EUCLID, BKZ]` |
| `extend_right(rp)` / `shrink_right(rp)` | `rp`: int | None | Adjust right boundary of local window. | `[PY, EUCLID, BKZ]` |
| `resize_db(new_size)` | `new_size`: int | None | Resize database limit. | `[PY, EUCLID, SVP]` |
| `global_histo_update(value)` | `value`: float | None | Update global histogram/statistics. | `[PY, EUCLID, SVP]` |

Parameter helpers exposed in the same source module:

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `SieverParams(...)` | various keyword arguments | `SieverParams` object | Parameter object for siever configuration. | `[PY, EUCLID]` |
| `load_siever_params(...)` | filename: str or dict | `SieverParams` object | Load/parse parameter configuration input. | `[PY, EUCLID]` |

---

## 4. Domain Caveat

`g6k` is a Euclidean reduction/sieving framework. It does not provide arithmetic indefinite-form genus/discriminant/isometry contracts.

---

## 5. Sources

- g6k repository README: `https://github.com/fplll/g6k`
- siever API source: `https://raw.githubusercontent.com/fplll/g6k/master/g6k/siever.pyx`
- local provenance snapshot: `docs/g6k/upstream/g6k_online_provenance_2026-02-17.md`
