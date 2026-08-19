# fpylll Method Test Gap Checklist

Tracks fpylll-relevant methods documented in `docs/fpylll/lattice/research_readme.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Core Data Structures

### IntegerMatrix

- [ ] `IntegerMatrix(arg0, arg1=None, int_type='mpz')`
- [ ] `IntegerMatrix.from_matrix(A, nrows=None, ncols=None, **kwds)`
- [ ] `IntegerMatrix.from_iterable(nrows, ncols, it, **kwds)`
- [ ] `IntegerMatrix.identity(nrows, int_type='mpz')`
- [ ] `IntegerMatrix.random(d, algorithm, int_type='mpz', **kwds)`
- [ ] `IntegerMatrix.randomize(algorithm, **kwds)`
- [ ] `IntegerMatrix.gen_identity(nrows=-1)`
- [ ] `IntegerMatrix.clear()`
- [ ] `IntegerMatrix.is_empty()`
- [ ] `IntegerMatrix.resize(rows, cols)`
- [ ] `IntegerMatrix.swap_rows(r1, r2)`
- [ ] `IntegerMatrix.rotate_left(first, last)`
- [ ] `IntegerMatrix.rotate_right(first, last)`
- [ ] `IntegerMatrix.rotate(first, middle, last)`
- [ ] `IntegerMatrix.rotate_gram_left(first, last, n_valid_rows)`
- [ ] `IntegerMatrix.rotate_gram_right(first, last, n_valid_rows)`
- [ ] `IntegerMatrix.transpose()`
- [ ] `IntegerMatrix.int_type` (property)
- [ ] `IntegerMatrix.nrows` (property)
- [ ] `IntegerMatrix.ncols` (property)

### MatGSO

- [ ] `GSO.Mat(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)`
- [ ] `MatGSO(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)`
- [ ] `MatGSO.update_gso()`
- [ ] `MatGSO.get_gram(i, j)`
- [ ] `MatGSO.get_int_gram(i, j)`
- [ ] `MatGSO.get_mu(i, j)`
- [ ] `MatGSO.get_r(i, j)`
- [ ] `MatGSO.get_current_slope(start_row, stop_row)`
- [ ] `MatGSO.get_root_det(start_row, stop_row)`
- [ ] `MatGSO.get_log_det(start_row, stop_row)`
- [ ] `MatGSO.from_canonical(w, start=0, dimension=-1)`
- [ ] `MatGSO.to_canonical(v, start=0)`
- [ ] `MatGSO.babai(v, start=0, dimension=-1, gso=False)`
- [ ] `MatGSO.G` (property)
- [ ] `MatGSO.float_type` (property)
- [ ] `MatGSO.int_type` (property)
- [ ] `MatGSO.d` (property)
- [ ] `MatGSO.n_known_rows` (property)
- [ ] `MatGSO.swap_rows(i, j)`

### BKZ Parameters

- [ ] `BKZ.Param(block_size, strategies=BKZ_DEFAULT_STRATEGY, delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, auto_abort=None, gh_factor=None, min_success_probability=BKZ_DEF_MIN_SUCCESS_PROBABILITY, rerandomization_density=BKZ_DEF_RERANDOMIZATION_DENSITY, dump_gso_filename=None, **kwds)`

## 2. LLL Surface

- [ ] `LLL.Wrapper(B, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)`
  - Constraint: `B` must have `int_type='mpz'`; callable only once.
- [ ] `LLL.reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)`
- [ ] `lll_reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)`
- [ ] `LLL.is_reduced(M, delta=0.99, eta=0.51)`
- [ ] `LLL.Reduction(M, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)`
- [ ] `LLL.Reduction.__call__(kappa_min=0, kappa_start=0, kappa_end=-1, size_reduction_start=0)`
- [ ] `LLL.Reduction.size_reduction(kappa_min=0, kappa_end=-1, size_reduction_start=0)`
- [ ] `LLL.Reduction.final_kappa` (property)
- [ ] `LLL.Reduction.last_early_red` (property)
- [ ] `LLL.Reduction.zeros` (property)
- [ ] `LLL.Reduction.nswaps` (property)

## 3. BKZ Surface

- [ ] `BKZ.reduction(B, param, U=None, float_type=None, precision=0)`
  - Contract note: `param` in `BKZ.reduction` is a `BKZ.Param` object; `B` must have `int_type='mpz'`.
- [ ] `BKZ.Reduction(M, lll_obj, param)`
- [ ] `BKZ.AutoAbort(M, num_rows, start_row=0)`
- [ ] `BKZ.AutoAbort.test_abort(scale=1.0, max_no_dec=5)`
- [ ] `BKZ.Reduction.__call__()`
- [ ] `BKZ.Reduction.svp_preprocessing(kappa, block_size, param)`
- [ ] `BKZ.Reduction.svp_postprocessing(kappa, block_size, solution)`
- [ ] `BKZ.Reduction.svp_reduction(kappa, block_size, param, dual=False)`
- [ ] `BKZ.Reduction.status` (property)
- [ ] `BKZ.Reduction.lll_status` (property)

## 4. Enumeration / SVP / CVP

- [ ] `Enumeration(M, nr_solutions=1, strategy=EvaluatorStrategy.BEST_N_SOLUTIONS, sub_solutions=False)`
- [ ] `Enumeration.enumerate(first, last, max_dist, max_dist_expo, target=None, subtree=None, pruning=None, dual=False, subtree_reset=False)`
- [ ] `Enumeration.get_nodes(level=None)`
- [ ] `SVP.shortest_vector(B, method='fast', flags=SVP_DEFAULT, pruning=True, preprocess=True, max_aux_solutions=0)`
  - Caveat: `method='fast'` is heuristic; `method='proved'` is the proof-oriented mode.
- [ ] `CVP.closest_vector(B, t, method='fast', flags=CVP_DEFAULT)`
  - Constraint: `B` must be LLL-reduced with `delta=LLL.DEFAULT_DELTA` and `eta=LLL.DEFAULT_ETA`.
- [ ] `CVP.babai(B, t, *args, **kwargs)`
  - Caveat: practical CVP workflows assume LLL-preconditioned basis input.

## 5. Pruning and Utilities

- [ ] `Pruning.run(radius, cost, gso_r, target, metric='probability', flags=Pruning.GRADIENT, pruning=None, float_type='double')`
- [ ] `fpylll.util.adjust_radius_to_gh_bound(dist, dist_expo, block_size, root_det, gh_factor)`
- [ ] `fpylll.util.gaussian_heuristic(r)`

---

## Definiteness and Domain Caveat

- fpylll is a Euclidean lattice stack; it does not expose indefinite arithmetic-form classification semantics.

---

## References

- `docs/fpylll/lattice/research_readme.md`
- `docs/fpylll/upstream/fpylll_online_provenance_2026-02-18.md`
- fpylll module docs: `https://fpylll.readthedocs.io/en/latest/modules.html`
- fpylll package docs home: `https://fpylll.readthedocs.io/`
- fpylll repository: `https://github.com/fplll/fpylll`
