# fpylll Lattice Reduction Reference
## Canonical API surface for Euclidean lattice reduction/search

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Positive-definite Euclidean lattice regime |
| `[ZZMOD]` | Integer basis-matrix setting |
| `[EUCLID]` | Euclidean metric algorithms |
| `[RED]` | Reduction algorithms |
| `[ENUM]` | Enumeration/SVP/CVP search |
| `[SRC]` | Signature taken from upstream source files |

---

## 1. Scope

`fpylll` is a Python interface to `fplll` for Euclidean lattice algorithms.

Primary scope:

- basis reduction (`LLL`, `BKZ`),
- Gram-Schmidt machinery (`GSO`),
- enumeration/SVP/CVP search.

Out of scope:

- arithmetic genus/spinor-genus/discriminant-form classification,
- indefinite quadratic-form classification semantics.

---

## 2. Core Data Structures and Contracts

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `IntegerMatrix(arg0, arg1=None, int_type='mpz')` | `arg0`: int or `IntegerMatrix`; `arg1`: int or None (optional, default `None`); `int_type`: str (optional, default `'mpz'`, accepts `'mpz'` or `'long'`) | `IntegerMatrix` | Integer matrix container for lattice basis/Gram workflows. When `arg0`, `arg1` are integers, creates an `arg0 × arg1` zero matrix; when `arg0` is an `IntegerMatrix` and `arg1` is `None`, creates a copy. Source: `integer_matrix.pyx` | `[ZZMOD, EUCLID, SRC]` |
| `GSO.Mat(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)` | `B`: `IntegerMatrix`; `U`: `IntegerMatrix` (optional, default `None`); `UinvT`: `IntegerMatrix` (optional, default `None`); `flags`: int (optional, default `GSO_DEFAULT`); `float_type`: str (optional, default `'double'`); `gram`: bool (optional, default `False`); `update`: bool (optional, default `False`) | `MatGSO` | Build GSO state from basis matrix `B`; optional transform tracking (`U`, `UinvT`); `flags` controls INT_GRAM, ROW_EXPO, OP_FORCE_LONG; `gram=True` treats `B` as a Gram matrix; `update=True` calls `update_gso()`. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)` | `B`: `IntegerMatrix`; `U`: `IntegerMatrix` (optional); `UinvT`: `IntegerMatrix` (optional); `flags`: int (optional); `float_type`: str (optional); `gram`: bool (optional); `update`: bool (optional) | `MatGSO` | Alias for `GSO.Mat`; same constructor surface. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `LLL.Reduction(M, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)` | `M`: `MatGSO`; `delta`: float (optional, default `0.99`); `eta`: float (optional, default `0.51`); `flags`: int (optional, default `LLL_DEFAULT`; valid flags: `LLL.DEFAULT`, `LLL.VERBOSE`, `LLL.EARLY_RED`, `LLL.SIEGEL`) | `LLL.Reduction` | Stateful LLL reducer over GSO object `M`; validates `0.25 < delta <= 1.0` and `0.5 <= eta < sqrt(delta)` before reduction. Calling the object (`__call__`) supports partial-range reduction: `.__call__(kappa_min=0, kappa_start=0, kappa_end=-1, size_reduction_start=0)` where `kappa_end=-1` defaults to `M.d`. `.size_reduction(kappa_min=0, kappa_end=-1, size_reduction_start=0)` performs only size reduction on the given row range. Properties: `.delta`, `.eta`, `.final_kappa`, `.last_early_red`, `.zeros`, `.nswaps`. Source: `lll.pyx` | `[RED, EUCLID, SRC]` |
| `BKZ.Param(block_size, strategies=BKZ_DEFAULT_STRATEGY, delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, auto_abort=None, gh_factor=None, min_success_probability=BKZ_DEF_MIN_SUCCESS_PROBABILITY, rerandomization_density=BKZ_DEF_RERANDOMIZATION_DENSITY, dump_gso_filename=None, **kwds)` | `block_size`: int (**must be > 0**, raises ValueError otherwise); `strategies`: str or list of `Strategy` (optional, default `BKZ_DEFAULT_STRATEGY`); `delta`: float (optional, default `LLL_DEF_DELTA`, **must satisfy `0.25 < delta < 1.0`** per `bkz_param.pyx` docstring — note strict upper bound, unlike LLL's `delta <= 1.0`); `flags`: int (optional, default `BKZ_DEFAULT`); `max_loops`: int (optional, default `0`, **must be >= 0**, raises ValueError otherwise; setting `> 0` auto-enables `BKZ_MAX_LOOPS` flag); `max_time`: int (optional, default `0`, **must be >= 0**, raises ValueError otherwise; setting `> 0` auto-enables `BKZ_MAX_TIME` flag); `auto_abort`: `None`, `True`, or `(scale, max_iter)` tuple (optional, default `None`; `True` maps to fpLLL default `(1.0, 5)`); `gh_factor`: float (optional, default `None`; **if set must be > 0**, raises ValueError otherwise; non-None/non-False value auto-enables `BKZ_GH_BND` flag; `True` maps to `BKZ_DEF_GH_FACTOR`); `min_success_probability`: float (optional, default `BKZ_DEF_MIN_SUCCESS_PROBABILITY`); `rerandomization_density`: int (optional, default `BKZ_DEF_RERANDOMIZATION_DENSITY`); `dump_gso_filename`: str (optional, default `None`; auto-enables `BKZ_DUMP_GSO` flag); `**kwds`: dict | `BKZ.Param` | BKZ parameter object specifying block size, strategy file, abort conditions, and pruning controls. Source: `bkz_param.pyx` | `[RED, EUCLID, SRC]` |
| `BKZ.Reduction(M, lll_obj, param)` | `M`: `MatGSO`; `lll_obj`: `LLL.Reduction`; `param`: `BKZ.Param` | `BKZ.Reduction` | Stateful BKZ reducer over GSO object `M` with LLL helper and BKZ parameter object. Source: `bkz.pyx` | `[RED, EUCLID, SRC]` |

---

## 3. MatGSO Instance Methods

The following methods are available on a `MatGSO` object (returned by `GSO.Mat(...)`). All indices are 0-based. GSO coefficients must be computed (via `update_gso()` or `update=True` at construction) before coefficient-access methods are called; calling them on a stale object yields undefined values.

### 3a. GSO Coefficient Access

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `LLL.reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)` | `B`: `IntegerMatrix`; `U`: `IntegerMatrix` (optional, default `None`); `delta`: float (optional, default `0.99`); `eta`: float (optional, default `0.51`); `method`: str (optional, default `None`, valid values: `'wrapper'`, `'proved'`, `'heuristic'`, `'fast'`, `None`); `float_type`: str (optional, default `None`); `precision`: int (optional, default `0`); `flags`: int (optional, default `LLL_DEFAULT`) | `IntegerMatrix` (returns modified `B`) | One-shot reduction of basis matrix `B` (modified in-place and returned); optional transform matrix `U` tracks unimodular transformation; `method` selects backend. Coupling constraint: `method='wrapper'` or `None` requires `float_type=None`; `method='fast'` requires `float_type` in `{'double', 'long double', 'dd', 'qd'}`. Source: `lll.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |
| `lll_reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)` | `B`: `IntegerMatrix`; `U`: `IntegerMatrix` (optional); `delta`: float (optional); `eta`: float (optional); `method`: str (optional, valid values same as `LLL.reduction`); `float_type`: str (optional); `precision`: int (optional); `flags`: int (optional) | `IntegerMatrix` (returns modified `B`) | Module-level alias with the same contract as `LLL.reduction`; same method/float_type coupling constraints apply. Source: `lll.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |
| `LLL.is_reduced(B, delta=0.99, eta=0.51)` | `B`: `IntegerMatrix`; `delta`: float (optional, default `0.99`); `eta`: float (optional, default `0.51`) | `bool` | Predicate for LLL-reducedness under given Lovász/size-reduction parameters. Source: `lll.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |
| `MatGSO.get_gram(i, j)` | `i`: int; `j`: int; requires `0 ≤ j ≤ i < d` | `float` | Returns Gram coefficient: if `row_expo_enabled=False`, returns `⟨b_i, b_j⟩`; if `row_expo_enabled=True`, returns `⟨b_i, b_j⟩ / 2^{r_i + r_j}` where `r_i`, `r_j` are row exponents. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.get_int_gram(i, j)` | `i`: int; `j`: int; requires `0 ≤ j ≤ i < d` | `int` | Returns exact integer Gram coefficient `⟨b_i, b_j⟩`; valid only when `row_expo_enabled=False`. Source: `gso.pyx` | `[ZZMOD, EUCLID, SRC]` |
| `MatGSO.get_r(i, j)` | `i`: int; `j`: int | `float` | Returns `⟨b_i, b*_j⟩` (the r-coefficient of the GSO decomposition). GSO must have been computed. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.get_r_exp(i, j)` | `i`: int; `j`: int | `tuple` `(float, int)` | Returns `(f, x)` such that `⟨b_i, b*_j⟩ = f · 2^x`. If `row_expo_enabled=False`, `x = 0`; if `row_expo_enabled=True`, `x = r_i + r_j`. Assumes `r(i, j)` is valid. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.get_mu(i, j)` | `i`: int; `j`: int | `float` | Returns μ_{i,j} = `⟨b_i, b*_j⟩ / ‖b*_j‖²`. GSO must have been computed. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.get_mu_exp(i, j)` | `i`: int; `j`: int | `tuple` `(float, int)` | Returns `(f, x)` such that `f · 2^x = ⟨b_i, b*_j⟩ / ‖b*_j‖²`. If `row_expo_enabled=False`, `x = 0`; if `row_expo_enabled=True`, `x = r_i - r_j`. Assumes `μ(i, j)` is valid. Source: `gso.pyx` | `[EUCLID, SRC]` |

### 3b. GSO Update Methods

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `MatGSO.update_gso()` | (none) | `bool` | Recomputes all GSO coefficients (μ and r) from scratch. Returns `True` on success. Must be called before any coefficient-access method if `update=False` was used at construction. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.update_gso_row(i, last_j)` | `i`: int; `last_j`: int | `bool` | Updates `r_{i,j}` and `μ_{i,j}` for all `j ∈ [0, last_j]`. Requires that coefficients above row `i` in columns `[0, min(last_j, i-1)]` are already valid. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.discover_all_rows()` | (none) | `None` | Enables `row_addmul` for all rows even if GSO has never been computed; used to seed row operations before an initial GSO computation. Source: `gso.pyx` | `[EUCLID, SRC]` |

### 3c. Lattice Geometry Methods

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `MatGSO.get_current_slope(start_row, stop_row)` | `start_row`: int; `stop_row`: int (exclusive) | `float` | Returns slope of the least-squares line fitted to log-lengths of GSO vectors in the index range `[start_row, stop_row)`. A more negative slope indicates better LLL quality. Declared in `bkz.h`. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.get_root_det(start_row, stop_row)` | `start_row`: int; `stop_row`: int (exclusive) | `float` | Returns the (squared) root determinant `(∏_{i=start_row}^{stop_row-1} r_{i,i})^{1/(stop_row - start_row)}` of the sub-basis `[start_row, stop_row)`. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.get_log_det(start_row, stop_row)` | `start_row`: int; `stop_row`: int (exclusive) | `float` | Returns the natural log of the (squared) determinant `∑_{i=start_row}^{stop_row-1} log(r_{i,i})` of the sub-basis `[start_row, stop_row)`. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.get_slide_potential(start_row, stop_row, block_size)` | `start_row`: int; `stop_row`: int (exclusive); `block_size`: int | `float` | Returns the slide potential of the sub-basis, used as a quality measure for slide reduction. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.r(start=0, end=-1)` | `start`: int (optional, default `0`); `end`: int (optional, default `-1` → `d`) | `tuple` of `float` | Returns the diagonal r-vector `(r_{i,i})` for `i ∈ [start, end)`. Convenience wrapper around `get_r(i, i)`. Source: `gso.pyx` | `[EUCLID, SRC]` |

### 3d. Basis Conversion Methods

These methods require the `MatGSO` object to have been constructed over a **basis** (not a Gram matrix); if `gram=True` was passed at construction, they raise `TypeError`.

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `MatGSO.from_canonical(w, start=0, dimension=-1)` | `w`: tuple-like of length `B.ncols`; `start`: int (optional, default `0`); `dimension`: int (optional, default `-1` → `d - start`) | `tuple` of `float` | Converts vector `w` from the canonical basis `ℤ^n` to the GSO basis `B^*`, returning coordinates wrt `B^*`. Raises `TypeError` if used on a Gram-mode object. **Float-type caveat**: `dpe` float_type raises `NotImplementedError`. Inverse of `to_canonical`. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.to_canonical(v, start=0)` | `v`: tuple-like of length `d`; `start`: int (optional, default `0`) | `tuple` of `float` | Converts vector `v` in GSO coordinates to the canonical basis, returning a vector in `ℝ^n`. Raises `TypeError` if used on a Gram-mode object. **Float-type caveat**: `dpe`, `qd`, and some `long_*` combinations raise `NotImplementedError`. Inverse of `from_canonical`. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.babai(v, start=0, dimension=-1, gso=False)` | `v`: tuple-like; `start`: int (optional, default `0`); `dimension`: int (optional, default `-1` → `d - start`); `gso`: bool (optional, default `False`) | `tuple` of `int` | Babai nearest-plane algorithm. If `gso=False`, `v` is a canonical-basis vector and `from_canonical` is applied internally (requires basis object); if `gso=True`, `v` is already in GSO coordinates and a Gram-mode object is acceptable. Returns coefficient vector wrt `B`. **Stability note**: `CVP.babai()` is more numerically stable (repeated nearest-plane at variable precision) but does not support float target vectors; `MatGSO.babai` accepts float targets. Some float_type/int_type combinations raise `NotImplementedError`. Source: `gso.pyx` | `[ENUM, EUCLID, SRC]` |

### 3e. Row Operation Methods

`row_addmul` must be bracketed by `row_op_begin` / `row_op_end` (or use the `row_ops` context manager). Calling `row_op_end` invalidates GSO coefficients for the modified rows, requiring a fresh `update_gso()` or `update_gso_row()`.

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `MatGSO.row_op_begin(first, last)` | `first`: int; `last`: int (exclusive) | `None` | Must be called before a sequence of `row_addmul` calls. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.row_op_end(first, last)` | `first`: int; `last`: int (exclusive) | `None` | Must be called after `row_addmul` sequence; invalidates GSO for rows `[first, last)`. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.row_ops(first, last)` | `first`: int; `last`: int (exclusive) | context manager | Returns a `MatGSORowOpContext` that calls `row_op_begin`/`row_op_end` on enter/exit. Preferred over manual `row_op_begin`/`row_op_end` pairing. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.row_addmul(i, j, x)` | `i`: int (target); `j`: int (source); `x`: float | `None` | Sets `b_i ← b_i + x · b_j`. Must be bracketed by `row_op_begin`/`row_op_end`. If `row_op_force_long=True`, `x` is converted via `(2^expo · long)` rather than `(2^expo · ZT)`, which is faster for `mpz_t` but may lose precision. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.move_row(old_r, new_r)` | `old_r`: int; `new_r`: int | `None` | Row `old_r` becomes row `new_r`; intermediate rows are shifted. **Constraint**: if `new_r < old_r`, then `old_r` must be `< n_known_rows`. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.swap_rows(i, j)` | `i`: int; `j`: int | `None` | Swaps rows `i` and `j` in the basis matrix. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.negate_row(i)` | `i`: int | `None` | Sets `b_i ← −b_i`. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.create_row()` | (none) | `None` | Appends a zero row to `B` (and to `U` if `transform_enabled`). **Constraint**: raises `ValueError` if `inverse_transform_enabled=True`. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO.remove_last_row()` | (none) | `None` | Removes the last row of `B` (and `U` if `transform_enabled`). **Constraint**: raises `ValueError` if `inverse_transform_enabled=True`. Source: `gso.pyx` | `[EUCLID, SRC]` |

---

## 4. LLL Surface

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `LLL.reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)` | `B`: `IntegerMatrix`; `U`: `IntegerMatrix` or `None` (optional, default `None`); `delta`: float (optional, default `0.99`); `eta`: float (optional, default `0.51`); `method`: str or `None` (optional, default `None`; one of `'wrapper'`, `'proved'`, `'heuristic'`, `'fast'`, `None`); `float_type`: str or `None` (optional, default `None`); `precision`: int (optional, default `0`); `flags`: int (optional, default `LLL_DEFAULT`) | `IntegerMatrix` | Reduces basis matrix `B` in place; returns `B`. Optional transform matrix `U` tracks unimodular transformation. **Method/float_type constraints**: `method='wrapper'` requires `float_type=None`; `method='fast'` requires `float_type` in `('double', 'long double', 'dd', 'qd')`; `method=None` defaults to `'wrapper'`. Source: `lll.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |
| `lll_reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)` | `B`: `IntegerMatrix`; `U`: `IntegerMatrix` or `None` (optional); `delta`: float (optional); `eta`: float (optional); `method`: str or `None` (optional; one of `'wrapper'`, `'proved'`, `'heuristic'`, `'fast'`, `None`); `float_type`: str or `None` (optional); `precision`: int (optional); `flags`: int (optional) | `IntegerMatrix` | Module-level alias with the same contract as `LLL.reduction`; reduces `B` in place and returns `B`. Same method/float_type constraints apply. Source: `lll.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |
| `LLL.is_reduced(M, delta=0.99, eta=0.51)` | `M`: `IntegerMatrix` or `MatGSO`; `delta`: float (optional, default `0.99`); `eta`: float (optional, default `0.51`) | `bool` | Predicate for LLL-reducedness under given Lovász/size-reduction parameters. Accepts either an `IntegerMatrix` (GSO is recomputed internally) or a `MatGSO` object (existing GSO state is reused). **Caution**: may return `False` for a genuinely LLL-reduced matrix if the internal floating-point precision is too low. Source: `lll.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |

Additional LLL surface (from `wrapper.pyx` / `lll.pyx`):

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `LLL.Wrapper(B, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)` | `B`: `IntegerMatrix` (must have `int_type='mpz'`; raises `NotImplementedError` for non-mpz types); `delta`: float (optional, default `0.99`); `eta`: float (optional, default `0.51`); `flags`: int (optional, default `LLL_DEFAULT`) | `LLL.Wrapper` | Stateful LLL wrapper object. Calls `__call__()` to run LLL on `B` in place. **Single-use**: `__call__()` may only be called once; raises `ValueError` on repeated invocation. Internally wraps the C++ `Wrapper` class. **mpz-only restriction**: unlike `LLL.Reduction`, only accepts `IntegerMatrix` with `int_type='mpz'`. Source: `wrapper.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |

Parameter constraints from docs/source:

- `delta` must satisfy `0.25 < delta <= 1.0`,
- `eta` must satisfy `0.5 <= eta < sqrt(delta)`,
- invalid parameter ranges raise errors before running reduction.

---

## 5. BKZ Surface

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `BKZ.reduction(B, param, U=None, float_type=None, precision=0)` | `B`: `IntegerMatrix`; `param`: `BKZ.Param`; `U`: `IntegerMatrix` or `None` (optional, default `None`); `float_type`: str or `None` (optional, default `None`); `precision`: int (optional, default `0`) | `IntegerMatrix` | Reduces basis `B` in place using BKZ parameter object `param`; returns `B`. Source: `bkz.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |
| `BKZ.Reduction(M, lll_obj, param)` | `M`: `MatGSO`; `lll_obj`: `LLL.Reduction`; `param`: `BKZ.Param` | `BKZ.Reduction` | Stateful BKZ for repeated tours over the same GSO object. Source: `bkz.pyx` | `[RED, EUCLID, SRC]` |
| `BKZ.Param(block_size, strategies=BKZ_DEFAULT_STRATEGY, delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, auto_abort=None, gh_factor=None, min_success_probability=BKZ_DEF_MIN_SUCCESS_PROBABILITY, rerandomization_density=BKZ_DEF_RERANDOMIZATION_DENSITY, dump_gso_filename=None, **kwds)` | See Core Data Structures section for full typed argument contracts including validity constraints (`block_size > 0`, `max_loops >= 0`, `max_time >= 0`, `gh_factor > 0` if set, `0.25 < delta < 1.0`). | `BKZ.Param` | Full BKZ tuning surface (block size, strategies, abort/loop/time controls, GH/pruning controls). Source: `bkz_param.pyx` | `[RED, EUCLID, SRC]` |
| `BKZ.EasyParam(block_size, **kwds)` | `block_size`: int; `**kwds`: dict (keyword arguments forwarded, with `flags` XOR-applied against defaults) | `BKZ.Param` | Convenience parameter builder: sets `strategies=default_strategy` and enables `BKZ_AUTO_ABORT` by default; `flags` kwarg is XOR-applied against `BKZ_DEFAULT|BKZ_AUTO_ABORT`. Source: `bkz_param.pyx` | `[RED, EUCLID, SRC]` |

Documentation caveat:

- Current `modules.html` exposes BKZ section headers but not the full member signatures.
- BKZ signatures above are source-anchored to upstream `bkz.pyx` / `bkz_param.pyx`.

---

## 6. Enumeration, SVP, and CVP

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `Enumeration(M, nr_solutions=1, strategy=EvaluatorStrategy.BEST_N_SOLUTIONS, sub_solutions=False, callbackf=None)` | `M`: `MatGSO`; `nr_solutions`: int (optional, default `1`); `strategy`: `EvaluatorStrategy` (optional, default `BEST_N_SOLUTIONS`, one of `BEST_N_SOLUTIONS`, `OPPORTUNISTIC_N_SOLUTIONS`, `FIRST_N_SOLUTIONS`); `sub_solutions`: bool (optional, default `False`); `callbackf`: callable or `None` (optional, default `None`; if provided, used as C++-level callback evaluator) | `Enumeration` | Enumeration context bound to a GSO object `M`. **Callback**: if `callbackf` is provided, it must be a predicate accepting a candidate solution coordinate list and returning `bool` to accept/reject the candidate. **Strategy semantics**: `BEST_N_SOLUTIONS` keeps the `nr_solutions` shortest; `OPPORTUNISTIC_N_SOLUTIONS` updates bound on each find; `FIRST_N_SOLUTIONS` stops after `nr_solutions` without bound updates. Source: `enumeration.pyx` | `[ENUM, PD, EUCLID, SRC]` |
| `Enumeration.enumerate(first, last, max_dist, max_dist_expo, target=None, subtree=None, pruning=None, dual=False, subtree_reset=False)` | `first`: int; `last`: int; `max_dist`: float; `max_dist_expo`: int; `target`: list (optional, default `None`); `subtree`: object (optional, default `None`); `pruning`: object (optional, default `None`); `dual`: bool (optional, default `False`); `subtree_reset`: bool (optional, default `False`) | `list` of tuples `(vector, norm)` | Bounded subtree enumeration over basis index window `[first, last)`. Source: `enumeration.pyx` | `[ENUM, PD, EUCLID, SRC]` |
| `Enumeration.get_nodes(level=None)` | `level`: int (optional, default `None`) | `int` or `dict` | Return node counts globally (`level=None`) or at specific level. Source: `enumeration.pyx` | `[ENUM, EUCLID, SRC]` |
| `SVP.shortest_vector(B, method='fast', flags=SVP_DEFAULT, pruning=True, preprocess=True, max_aux_solutions=0)` | `B`: `IntegerMatrix`; `method`: str (optional, default `'fast'`, one of `'fast'` or `'proved'`); `flags`: int (optional, default `SVP_DEFAULT`, accepts `SVP.DEFAULT`, `SVP.VERBOSE`, `SVP.OVERRIDE_BND`); `pruning`: bool or list (optional, default `True`); `preprocess`: bool or int (optional, default `True`); `max_aux_solutions`: int (optional, default `0`) | `tuple` `(vector, norm)` or `(vector, aux_solutions)` | SVP wrapper. **Proof guarantee**: `method='proved'` returns a provably shortest vector and is incompatible with custom `pruning` (raises `ValueError`); `method='fast'` is heuristic. **Preprocessing**: if `preprocess=True` and `d > strategy_block_size`, runs BKZ preprocessing; if `preprocess=2`, runs LLL only; if `preprocess > 2`, runs BKZ with that block size. **Pruning behavior**: if `pruning=True`, pruning parameters are auto-computed (disabled for `d <= 20`); if a list, must have length `B.nrows`. **Dimension limit**: raises `NotImplementedError` if `B.nrows > MAX_ENUM_DIM`. **mpz-only**: raises `NotImplementedError` if `B` was not constructed with `int_type='mpz'`. **Aux solutions**: if `max_aux_solutions > 0`, returns `(vector, aux_solutions)` where `aux_solutions` is a tuple of additional short-ish vectors. Source: `svpcvp.pyx` | `[ENUM, PD, EUCLID, ZZMOD, SRC]` |
| `CVP.closest_vector(B, t, method='fast', flags=CVP_DEFAULT)` | `B`: `IntegerMatrix`; `t`: list (target vector, must have integer entries); `method`: str (optional, default `'fast'`, one of `'fast'` or `'proved'`); `flags`: int (optional, default `CVP_DEFAULT`, accepts `CVP.DEFAULT` or `CVP.VERBOSE`) | `tuple` (vector) | CVP wrapper for target vector `t`. **Precondition**: `B` must be LLL-reduced with `delta=LLL.DEFAULT_DELTA` (≈0.99) and `eta=LLL.DEFAULT_ETA` (≈0.51). **Proof guarantee**: `method='proved'` returns a provably closest vector; `method='fast'` is heuristic. **Dimension limit**: raises `NotImplementedError` if `B.nrows > MAX_ENUM_DIM` (compile-time constant). **mpz-only**: raises `NotImplementedError` if `B` was not constructed with `int_type='mpz'`. Source: `svpcvp.pyx` | `[ENUM, PD, EUCLID, ZZMOD, SRC]` |
| `CVP.babai(B, t, *args, **kwargs)` | `B`: `IntegerMatrix`; `t`: list (target vector); `*args`: tuple; `**kwargs`: dict | `list` (vector) | Babai nearest-plane approximation workflow. Source: `svpcvp.pyx` | `[ENUM, EUCLID, SRC]` |

Practical caveat:

- `CVP.closest_vector`/`CVP.babai` are normally used after LLL preprocessing.

---

## 7. Pruning and Utility Methods

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `Pruning.run(radius, cost, gso_r, target, metric='probability', flags=Pruning.GRADIENT, pruning=None, float_type='double')` | `radius`: float (squared enumeration radius); `cost`: float (preprocessing cost, ≥1); `gso_r`: list of lists (r-coefficients, accepts single list auto-wrapped); `target`: float (success probability or solution count); `metric`: str (optional, default `'probability'`, one of `'probability'`, `'solutions'`); `flags`: int (optional, default `Pruning.GRADIENT`, accepts `Pruning.GRADIENT`, `Pruning.NELDER_MEAD`, `Pruning.VERBOSE`, `Pruning.ZEALOUS`, `Pruning.SINGLE`, `Pruning.HALF`, `Pruning.START_FROM_INPUT`, `Pruning.CVP`); `pruning`: `PruningParams` or None (optional, default `None`, output container); `float_type`: str (optional, default `'double'`) | `PruningParams` | Static pruning optimizer. **Preproc cost**: must be ≥1, expressed in enumeration nodes (~100 CPU cycles/node). **Metric constraints**: if `metric='probability'`, requires `0 < target < 1`; if `metric='solutions'`, requires `target > 0`. **gso_r**: accepts single list auto-wrapped to `[gso_r]`. Returns `PruningParams` object with `.coefficients`, `.expectation`, `.gh_factor` properties. Source: `pruner.pyx` | `[ENUM, EUCLID, SRC]` |
| `PruningParams(gh_factor, coefficients, expectation=1.0, metric='probability', detailed_cost=())` | `gh_factor`: float (>0, ratio of radius to Gaussian heuristic); `coefficients`: list (pruning coefficients); `expectation`: float (optional, default `1.0`, success probability or solution count); `metric`: str (optional, default `'probability'`, one of `'probability'`, `'solutions'`); `detailed_cost`: tuple (optional, default `()`) | `PruningParams` | Pruning parameters container. **Constraint**: `gh_factor` must be > 0. **Metric constraints**: if `metric='probability'`, requires `0 < expectation ≤ 1`. Properties: `.gh_factor`, `.coefficients` (tuple), `.expectation`, `.metric` (returns `'probability'` or `'solutions'`), `.detailed_cost`. Source: `pruner.pyx` | `[ENUM, EUCLID, SRC]` |
| `PruningParams.LinearPruningParams(block_size, level)` | `block_size`: int; `level`: int | `PruningParams` | Construct linear pruning params: all coefficients = 1, except last `level` coefficients which decay linearly with slope `-1/block_size`. Source: `pruner.pyx` | `[ENUM, EUCLID, SRC]` |
| `svp_probability(pr, float_type='double')` | `pr`: `PruningParams` or list (pruning coefficients); `float_type`: str (optional, default `'double'`) | `float` | Compute success probability for enumeration with given pruning parameters. **Auto-wrap**: if `pr` is a list, it is auto-wrapped in a `PruningParams` object. Source: `pruner.pyx` | `[ENUM, EUCLID, SRC]` |
| `fpylll.util.adjust_radius_to_gh_bound(dist, dist_expo, block_size, root_det, gh_factor)` | `dist`: float; `dist_expo`: int; `block_size`: int; `root_det`: float; `gh_factor`: float | `tuple` `(adjusted_dist, adjusted_expo)` | Adjust enumeration radius with GH-bound heuristic scaling. Source: `util` module | `[ENUM, EUCLID, SRC]` |
| `fpylll.util.gaussian_heuristic(r)` | `r`: list (squared GSO lengths) | `float` | Compute Gaussian heuristic from squared GSO lengths `r`. Source: `util` module | `[ENUM, EUCLID, SRC]` |

---

## 8. Indefinite Caveat

`fpylll` is a Euclidean lattice stack. It does not provide indefinite arithmetic-form classification contracts (genus/discriminant forms/local-global invariants).

For indefinite workflows, use arithmetic lattice stacks (Hecke/Indefinite.jl/Sage quadratic-form tooling) and treat `fpylll` as a PD reduction/search backend.

---

## 9. Practical Workflow Pattern

1. Build `IntegerMatrix` basis.
2. Construct `GSO.Mat` state.
3. Run `LLL.reduction` preconditioning.
4. Run `BKZ.reduction` with explicit `BKZ.Param` if stronger basis quality is needed.
5. Run `SVP.shortest_vector` / `CVP.closest_vector`.
6. Tune enumeration using `Pruning.run` and GH-bound utilities.

---

## 10. Sources

- fpylll modules index: `https://fpylll.readthedocs.io/en/latest/modules.html`
- fpylll GSO module: `https://fpylll.readthedocs.io/en/latest/modules.html#module-fpylll.fplll.gso`
- fpylll LLL module: `https://fpylll.readthedocs.io/en/latest/modules.html#module-fpylll.fplll.lll`
- fpylll enumeration module: `https://fpylll.readthedocs.io/en/latest/modules.html#module-fpylll.fplll.enumeration`
- fpylll utility module: `https://fpylll.readthedocs.io/en/latest/modules.html#module-fpylll.util`
- fpylll source (`bkz.pyx`): `https://raw.githubusercontent.com/fplll/fpylll/master/src/fpylll/fplll/bkz.pyx`
- fpylll source (`bkz_param.pyx`): `https://raw.githubusercontent.com/fplll/fpylll/master/src/fpylll/fplll/bkz_param.pyx`
- fpylll source (`svpcvp.pyx`): `https://raw.githubusercontent.com/fplll/fpylll/master/src/fpylll/fplll/svpcvp.pyx`
- fpylll source (`pruner.pyx`): `https://raw.githubusercontent.com/fplll/fpylll/master/src/fpylll/fplll/pruner.pyx`
- canonical provenance note: `docs/fpylll/upstream/fpylll_online_provenance_2026-02-18.md`
