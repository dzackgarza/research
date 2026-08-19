# fpylll Lattice Reference

Local upstream sources:
- `docs/fpylll/upstream/src/integer_matrix.pyx` — IntegerMatrix API
- `docs/fpylll/upstream/src/gso.pyx` — MatGSO (Gram-Schmidt orthogonalization) API
- `docs/fpylll/upstream/src/lll.pyx` — LLL reduction API
- `docs/fpylll/upstream/src/bkz.pyx` — BKZ reduction API
- `docs/fpylll/upstream/src/bkz_param.pyx` — BKZ parameter API
- `docs/fpylll/upstream/src/enumeration.pyx` — Enumeration API
- `docs/fpylll/upstream/src/svpcvp.pyx` — SVP/CVP API
- `docs/fpylll/upstream/src/pruner.pyx` — Pruning API
- `docs/fpylll/upstream/docs/modules.rst` — Module overview

---

## 1. Core Data Structures

### IntegerMatrix

**`IntegerMatrix(arg0, arg1=None, int_type='mpz')`**
- **Signature**: `IntegerMatrix(arg0, arg1=None, int_type='mpz')`
- **Description**: Dense integer matrix constructor. Supports `mpz` (arbitrary precision) and `long` (fixed-size) integer types.
- **Source**: `integer_matrix.pyx:298-361`

**`IntegerMatrix.from_matrix(A, nrows=None, ncols=None, **kwds)`**
- **Signature**: `classmethod IntegerMatrix.from_matrix(A, nrows=None, ncols=None, **kwds)`
- **Description**: Construct from matrix-like object with element access `A[i,j]` or `A[i][j]`.
- **Source**: `integer_matrix.pyx:363-373`

**`IntegerMatrix.from_iterable(nrows, ncols, it, **kwds)`**
- **Signature**: `classmethod IntegerMatrix.from_iterable(nrows, ncols, it, **kwds)`
- **Description**: Construct from iterable `it` of integers. Requires `it` to have length at least `nrows * ncols`. Accepts same `**kwds` as the constructor (e.g. `int_type`).
- **Source**: `integer_matrix.pyx:414-429`

**`IntegerMatrix.identity(cls, nrows, int_type='mpz')`**
- **Signature**: `classmethod IntegerMatrix.identity(nrows, int_type='mpz')`
- **Description**: Construct a new `nrows × nrows` identity matrix.
- **Source**: `integer_matrix.pyx:432-447`

**`IntegerMatrix.random(cls, d, algorithm, int_type='mpz', **kwds)`**
- **Signature**: `classmethod IntegerMatrix.random(d, algorithm, int_type='mpz', **kwds)`
- **Description**: Construct a random lattice basis matrix. The shape depends on the algorithm:
  - `'intrel'` (kwarg: `bits=b`): produces `d × (d+1)` knapsack-like matrix; i-th row = random `b`-bit integer followed by i-th canonical unit vector.
  - `'simdioph'` (kwargs: `bits=b1`, `bits2=b2`): produces `d × d` simultaneous Diophantine approximation matrix.
  - `'uniform'` (kwarg: `bits=b`): produces `d × d` matrix with independent random `b`-bit entries.
  - `'ntrulike'` (kwarg: `bits=b` OR `q`): produces `2d × 2d` NTRU-like matrix `[[I, rot(h)], [0, qI]]`; note: does NOT produce genuine NTRU lattices.
  - `'ntrulike2'` (kwarg: `bits=b` OR `q`): produces `2d × 2d` matrix `[[qI, 0], [rot(h), I]]`.
  - `'qary'` (kwarg: `bits=b` OR `q`, and `k`): produces `d × d` q-ary matrix with determinant `q^k`, shape `[[qI_{k×k}, 0], [H, I_{(d-k)×(d-k)}]]`. Corresponds to SIS/LWE lattices.
  - `'trg'` (kwarg: `alpha`): produces `d × d` lower-triangular matrix with `B_{ii} = 2^{(d-i+1)^alpha}`.
- **Constraints**: Unknown algorithm raises `ValueError: "Algorithm '%s' unknown."`.
- **Source**: `integer_matrix.pyx:449-628`

**`IntegerMatrix.randomize(algorithm, **kwds)`**
- **Signature**: `IntegerMatrix.randomize(algorithm, **kwds)`
- **Description**: Randomize matrix entries in-place. The `algorithm` and `**kwds` arguments are identical to `IntegerMatrix.random()`. Supported algorithms: `'intrel'`, `'simdioph'`, `'uniform'`, `'ntrulike'`, `'ntrulike2'`, `'qary'`, `'trg'`.
- **Constraints**: Requires `algorithm` to be one of the valid random generation algorithms. Raises `ValueError: "Algorithm '%s' unknown."` for invalid algorithm.
- **Source**: `integer_matrix.pyx:974-1110`

**`IntegerMatrix.gen_identity(nrows=-1)`**
- **Signature**: `IntegerMatrix.gen_identity(int nrows=-1)`
- **Description**: Generate identity matrix in-place. If `nrows=-1`, uses the current number of rows.
- **Parameters**: `nrows`: number of rows (default: -1, uses current nrows)
- **Source**: `integer_matrix.pyx:1112-1127`

**`IntegerMatrix.clear()`**
- **Signature**: `IntegerMatrix.clear()`
- **Description**: Clear the matrix, releasing memory.
- **Source**: `integer_matrix.pyx:1129-1139`

**`IntegerMatrix.is_empty()`**
- **Signature**: `IntegerMatrix.is_empty()`
- **Description**: Check if the matrix is empty.
- **Returns**: `bool`
- **Source**: `integer_matrix.pyx:1141-1151`

**`IntegerMatrix.resize(rows, cols)`**
- **Signature**: `IntegerMatrix.resize(int rows, int cols)`
- **Description**: Resize the matrix to have `rows` rows and `cols` columns.
- **Parameters**: 
  - `rows`: new number of rows
  - `cols`: new number of columns
- **Source**: `integer_matrix.pyx:1153-1180`

**`IntegerMatrix.swap_rows(r1, r2)`**
- **Signature**: `IntegerMatrix.swap_rows(int r1, int r2)`
- **Description**: Swap two rows in the matrix.
- **Parameters**: 
  - `r1`: first row index
  - `r2`: second row index
- **Source**: `integer_matrix.pyx:1193-1213`

**`IntegerMatrix.rotate_left(first, last)`**
- **Signature**: `IntegerMatrix.rotate_left(int first, int last)`
- **Description**: Rotate rows in range `[first, last)` left by one position.
- **Parameters**: 
  - `first`: start of range (inclusive)
  - `last`: end of range (exclusive)
- **Source**: `integer_matrix.pyx:1214-1231`

**`IntegerMatrix.rotate_right(first, last)`**
- **Signature**: `IntegerMatrix.rotate_right(int first, int last)`
- **Description**: Rotate rows in range `[first, last)` right by one position.
- **Parameters**: 
  - `first`: start of range (inclusive)
  - `last`: end of range (exclusive)
- **Source**: `integer_matrix.pyx:1232-1249`

**`IntegerMatrix.rotate(first, middle, last)`**
- **Signature**: `IntegerMatrix.rotate(int first, int middle, int last)`
- **Description**: Rotate rows in range `[first, last)` such that row `middle` moves to position `first`.
- **Parameters**: 
  - `first`: start of range (inclusive)
  - `middle`: pivot position
  - `last`: end of range (exclusive)
- **Source**: `integer_matrix.pyx:1250-1283`

**`IntegerMatrix.rotate_gram_left(first, last, n_valid_rows)`**
- **Signature**: `IntegerMatrix.rotate_gram_left(int first, int last, int n_valid_rows)`
- **Description**: Rotate Gram matrix rows in range `[first, last)` left by one position.
- **Parameters**: 
  - `first`: start of range (inclusive)
  - `last`: end of range (exclusive)
  - `n_valid_rows`: number of valid rows
- **Source**: `integer_matrix.pyx:1284-1302`

**`IntegerMatrix.rotate_gram_right(first, last, n_valid_rows)`**
- **Signature**: `IntegerMatrix.rotate_gram_right(int first, int last, int n_valid_rows)`
- **Description**: Rotate Gram matrix rows in range `[first, last)` right by one position.
- **Parameters**: 
  - `first`: start of range (inclusive)
  - `last`: end of range (exclusive)
  - `n_valid_rows`: number of valid rows
- **Source**: `integer_matrix.pyx:1303-1321`

**`IntegerMatrix.transpose()`**
- **Signature**: `IntegerMatrix.transpose()`
- **Description**: Return the transpose of the matrix.
- **Returns**: New `IntegerMatrix` that is the transpose.
- **Source**: `integer_matrix.pyx:1322-1340`

**`IntegerMatrix.int_type`** (property)
- **Signature**: `property IntegerMatrix.int_type`
- **Description**: Return the integer type (`'mpz'` or `'long'`).
- **Returns**: `str`
- **Source**: `integer_matrix.pyx:780-789`

**`IntegerMatrix.nrows`** (property)
- **Signature**: `property IntegerMatrix.nrows`
- **Description**: Number of rows in the matrix.
- **Returns**: `int`
- **Source**: `integer_matrix.pyx:844-856`

**`IntegerMatrix.ncols`** (property)
- **Signature**: `property IntegerMatrix.ncols`
- **Description**: Number of columns in the matrix.
- **Returns**: `int`
- **Source**: `integer_matrix.pyx:857-868`

### MatGSO (Gram-Schmidt Orthogonalization)

**`MatGSO(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)`**
- **Signature**: `MatGSO(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)`
- **Description**: Provides interface for elementary basis operations, Gram matrix, and Gram-Schmidt orthogonalization. Stores integral basis `B`, μ-coefficients, and r-coefficients. When `gram=True`, the input `B` is interpreted as the Gram matrix of the lattice (not a basis), and `GSO_INT_GRAM` is added to flags automatically.
- **Constraints**:
  - `float_type` must be one of: `'double'`, `'long_double'`, `'dpe'`, `'mpfr'`, `'dd'`, `'qd'` (the latter two require the QD library to be compiled in).
  - `GSO.INT_GRAM` flag (`GSO_INT_GRAM`): **cannot** be combined with `GSO.ROW_EXPO` (`GSO_ROW_EXPO`); they are mutually exclusive.
  - `GSO.ROW_EXPO` flag: **only** compatible with `float_type='double'` and `float_type='long_double'`; **must not** be used with `'dpe'`, `'dd'`, `'qd'`, or `'mpfr'`.
  - When `gram=True`: diagonal entries of `B` must be `>= 0`; raises `ValueError: "Diagonal of input matrix has negative entries."` otherwise.
  - `U` and `UinvT`, if provided, must have the same `int_type` as `B` (raises `TypeError: "U.int_type != B.int_type"` otherwise) and the same number of rows (raises `ValueError: "U.nrows != B.nrows"` otherwise).
  - `UinvT` requires `U` to be non-None (raises `ValueError: "Uinvt != None but U == None."` otherwise).
- **Source**: `gso.pyx:98-313`

**`MatGSO.update_gso()`**
- **Signature**: `MatGSO.update_gso()`
- **Description**: Compute/update Gram-Schmidt orthogonalization.
- **Source**: `gso.pyx:140-165`

**`MatGSO.get_gram(i, j)`**
- **Signature**: `MatGSO.get_gram(int i, int j)`
- **Description**: Return floating-point Gram matrix coefficient. If `GSO.ROW_EXPO` is disabled, returns `⟨b_i, b_j⟩`; if enabled, returns `⟨b_i, b_j⟩ / 2^{r_i + r_j}` where `r_i`, `r_j` are row exponents.
- **Constraints**: `0 ≤ i < d` and `0 ≤ j ≤ i`. Valid only within `n_known_rows`.
- **Source**: `gso.pyx:996-1042`

**`MatGSO.get_int_gram(i, j)`**
- **Signature**: `MatGSO.get_int_gram(int i, int j)`
- **Description**: Return exact integer Gram matrix coefficient `⟨b_i, b_j⟩`. Unlike `get_gram`, this returns an exact Python integer regardless of `float_type`.
- **Constraints**: `0 ≤ i < d` and `0 ≤ j ≤ i`. Valid only within `n_known_rows`. `GSO.ROW_EXPO` must be disabled (docstring states "If `enable_row_expo` is false, returns the dot product").
- **Source**: `gso.pyx:1044-1093`

**`MatGSO.get_mu(i, j)`**
- **Signature**: `MatGSO.get_mu(int i, int j)`
- **Description**: Get Gram-Schmidt coefficient μ_{i,j} = ⟨b_i, b^*_j⟩ / ‖b^*_j‖^2 for i > j.
- **Source**: `gso.pyx:1210-1253`

**`MatGSO.get_r(i, j)`**
- **Signature**: `MatGSO.get_r(int i, int j)`
- **Description**: Get coefficient r_{i,j} = ⟨b_i, b^*_j⟩ for i ≥ j.
- **Source**: `gso.pyx:1095-1147`

**`MatGSO.get_current_slope(start_row, stop_row)`**
- **Signature**: `MatGSO.get_current_slope(int start_row, int stop_row)`
- **Description**: Compute the slope of the least-squares line fitted to the log-lengths of GSO vectors from `start_row` to `stop_row` (exclusive). Negative slope indicates a good (short) basis; used as a quality indicator for LLL/BKZ outputs.
- **Constraints**: `0 ≤ start_row < stop_row ≤ d`. Calls the C++ `get_current_slope` from `bkz.h`.
- **Source**: `gso.pyx:1717-1796`

**`MatGSO.get_root_det(start_row, stop_row)`**
- **Signature**: `MatGSO.get_root_det(int start_row, int stop_row)`
- **Description**: Return `(vol(L_{[start_row, stop_row)}))^{1/(stop_row - start_row)}` — the `(stop_row - start_row)`-th root of the determinant of the projected sublattice. Returns a float (converted via `.get_d()`).
- **Constraints**: `0 ≤ start_row < stop_row ≤ d`.
- **Source**: `gso.pyx:1798-1876`

**`MatGSO.get_log_det(start_row, stop_row)`**
- **Signature**: `MatGSO.get_log_det(int start_row, int stop_row)`
- **Description**: Return log of the determinant of the projected sublattice spanned by rows `start_row..stop_row-1`.
- **Constraints**: `0 ≤ start_row < stop_row ≤ d`.
- **Source**: `gso.pyx:1877-1955`

**`MatGSO.from_canonical(w, start=0, dimension=-1)`**
- **Signature**: `MatGSO.from_canonical(w, int start=0, int dimension=-1)`
- **Description**: Convert vector `w` in the canonical basis ℤ^n to a coordinate vector in the Gram-Schmidt basis `B^*`. This is the inverse of `to_canonical`. Only defined for GSO objects over a basis (raises `TypeError` for Gram-matrix mode objects).
- **Parameters**:
  - `w`: tuple-like of dimension `M.B.ncols`
  - `start`: consider only subbasis starting at this row index
  - `dimension`: number of vectors to consider (`-1` = all)
- **Returns**: tuple of floats of dimension `dimension` (or `M.d` if `dimension=-1`)
- **Constraints**: Only for `mat_gso_gso_t` objects (not `gram=True` mode); raises `TypeError: "This function is only defined for GSO objects over a basis"` otherwise. The `dpe`, `long_dpe`, and `long_mpfr` float types are not yet implemented (commented out upstream).
- **Source**: `gso.pyx:2037-2175`

**`MatGSO.to_canonical(v, start=0)`**
- **Signature**: `MatGSO.to_canonical(v, int start=0)`
- **Description**: Convert coordinate vector `v` wrt the Gram-Schmidt basis `B^*` back to the canonical basis ℤ^n. Inverse of `from_canonical`.
- **Source**: `gso.pyx:2177-2305`

**`MatGSO.babai(v, start=0, dimension=-1, gso=False)`**
- **Signature**: `MatGSO.babai(v, int start=0, int dimension=-1, gso=False)`
- **Description**: Return integer coefficient vector `w` such that `‖w⋅B - v‖` is small, using Babai's nearest plane algorithm. Returns coordinates wrt `B` (not the ambient vector). When `gso=True`, `v` is treated as a coordinate vector wrt the Gram-Schmidt basis `B^*`; when `gso=False` (default), `v` is in the canonical basis. Numerically less stable than `CVP.babai()` but supports floating-point target vectors and non-canonical input.
- **Constraints**: When `gso=False`, only defined for GSO objects over a basis (raises `TypeError` for Gram-matrix mode).
- **Source**: `gso.pyx:2306-2556`

**`MatGSO.G`** (property)
- **Signature**: `property MatGSO.G`
- **Description**: Return the Gram matrix. If this GSO object operates on a Gram matrix, return that. If operating on a basis with `GSO.INT_GRAM` set, construct and return the Gram matrix. Otherwise raises `NotImplementedError`.
- **Constraints**: Requires `GSO.INT_GRAM` flag to be set.
- **Source**: `gso.pyx:445-561`

**`MatGSO.float_type`** (property)
- **Signature**: `property MatGSO.float_type`
- **Description**: Return the float type (`'double'`, `'long double'`, `'dpe'`, `'dd'`, `'qd'`, or `'mpfr'`).
- **Returns**: `str`
- **Source**: `gso.pyx:563-592`

**`MatGSO.int_type`** (property)
- **Signature**: `property MatGSO.int_type`
- **Description**: Return the integer type (`'mpz'` or `'long'`).
- **Returns**: `str`
- **Source**: `gso.pyx:594-614`

**`MatGSO.d`** (property)
- **Signature**: `property MatGSO.d`
- **Description**: Number of rows of `B` (dimension of the lattice).
- **Returns**: `int`
- **Source**: `gso.pyx:616-664`

**`MatGSO.n_known_rows`** (property)
- **Signature**: `property MatGSO.n_known_rows`
- **Description**: Number of rows for which Gram-Schmidt coefficients have been computed.
- **Returns**: `int`
- **Source**: `gso.pyx`

**`MatGSO.swap_rows(i, j)`**
- **Signature**: `MatGSO.swap_rows(int i, int j)`
- **Description**: Swap rows `i` and `j` in the GSO object.
- **Parameters**: 
  - `i`: first row index
  - `j`: second row index
- **Source**: `gso.pyx:1497-1531`

---

## 2. LLL Surface

### LLL Reduction

**`LLL.Wrapper(B, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)`**
- **Signature**: `LLL.Wrapper(B, double delta=LLL_DEF_DELTA, double eta=LLL_DEF_ETA, int flags=LLL_DEFAULT)`
- **Description**: Low-level LLL wrapper that operates directly on an `IntegerMatrix`. Call the object (via `W()`) to run LLL. Lighter-weight than `LLL.Reduction` because it does not require a pre-built `MatGSO` object.
- **Constraints**:
  - `B` must have `int_type='mpz'` (GMP integers); raises `NotImplementedError: "Only integer matrices over GMP integers (mpz_t) are supported."` for `int_type='long'`.
  - `__call__()` (i.e. `W()`) may only be invoked **once**; a second call raises `ValueError: "lll() may only be called once."`.
- **Source**: `wrapper.pyx:13-78`

**`LLL.reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)`**
- **Signature**: `LLL.reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)`
- **Description**: Run LLL reduction on integer matrix B. If U is provided, stores transformation matrix.
- **Constraints**: `delta` must satisfy `0.25 < delta ≤ 1`. `eta` must satisfy `0 ≤ eta < sqrt(delta)`.
- **Parameters**:
  - `method`: one of `'wrapper'`, `'proved'`, `'heuristic'`, `'fast'`, or `None`
  - `float_type`: `'double'`, `'long_double'`, `'dpe'`, `'mpfr'`, `'dd'`, `'qd'`
  - `precision`: bit precision for mpfr float type
- **Source**: `lll.pyx:550-622`

**`LLL.is_reduced(M, delta=0.99, eta=0.51)`**
- **Signature**: `LLL.is_reduced(M, delta=0.99, eta=0.51)`
- **Description**: Test if matrix M is LLL-reduced with parameters (delta, eta). May return False for LLL-reduced matrices if precision is too small.
- **Source**: `lll.pyx:624-692`

**`LLL.Reduction(M, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)`**
- **Signature**: `LLL.Reduction(M, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)`
- **Description**: LLL reduction object constructor. Takes MatGSO object M.
- **Source**: `lll.pyx:46-70`

**`LLL.Reduction.__call__(kappa_min=0, kappa_start=0, kappa_end=-1, size_reduction_start=0)`**
- **Signature**: `LLL.Reduction.__call__(kappa_min=0, kappa_start=0, kappa_end=-1, size_reduction_start=0)`
- **Description**: Execute LLL reduction with given parameters.
- **Source**: `lll.pyx:215-305`

**`LLL.Reduction.size_reduction(kappa_min=0, kappa_end=-1, size_reduction_start=0)`**
- **Signature**: `LLL.Reduction.size_reduction(kappa_min=0, kappa_end=-1, size_reduction_start=0)`
- **Description**: Perform size reduction only.
- **Source**: `lll.pyx:307-379`

**`LLL.Reduction.final_kappa`**
- **Signature**: `property LLL.Reduction.final_kappa`
- **Description**: Final kappa index after reduction.
- **Source**: `lll.pyx:381-419`

**`LLL.Reduction.last_early_red`**
- **Signature**: `property LLL.Reduction.last_early_red`
- **Description**: Last index where early reduction was applied.
- **Source**: `lll.pyx:421-459`

**`LLL.Reduction.zeros`**
- **Signature**: `property LLL.Reduction.zeros`
- **Description**: Number of zero vectors encountered.
- **Source**: `lll.pyx:461-499`

**`LLL.Reduction.nswaps`**
- **Signature**: `property LLL.Reduction.nswaps`
- **Description**: Number of swaps performed.
- **Source**: `lll.pyx:501-539`

---

## 3. BKZ Surface

### BKZ Reduction

**`BKZ.reduction(B, param, U=None, float_type=None, precision=0)`**
- **Signature**: `BKZ.reduction(B, param, U=None, float_type=None, precision=0)`
- **Description**: Run BKZ reduction on integer matrix `B` in-place. `param` must be a `BKZ.Param` object. Returns modified matrix `B`.
- **Constraints**:
  - `B` must be an `IntegerMatrix` with `int_type='mpz'` (GMP integers); raises `NotImplementedError` for `int_type='long'`: "C++ BKZ is not implemented over longs, try the Python version."
  - Euclidean lattice reduction workflow; not an indefinite genus/isometry classifier.
- **Source**: `bkz.pyx:1109-1187`

**`BKZ.Reduction(M, lll_obj, param)`**
- **Signature**: `BKZ.Reduction(M, lll_obj, param)`
- **Description**: BKZ reduction object constructor. Takes MatGSO object M, LLL object, and BKZ param.
- **Source**: `bkz.pyx:200-280`

**`BKZ.AutoAbort(M, num_rows, start_row=0)`**
- **Signature**: `BKZ.AutoAbort(M, num_rows, start_row=0)`
- **Description**: Utility class for aborting BKZ when slope no longer improves.
- **Source**: `bkz.pyx:51-165`

**`BKZ.AutoAbort.test_abort(scale=1.0, max_no_dec=5)`**
- **Signature**: `BKZ.AutoAbort.test_abort(scale=1.0, int max_no_dec=5)`
- **Description**: Test if new slope fails to be smaller than `scale * old_slope` for `max_no_dec` iterations.
- **Parameters**:
  - `scale`: target decrease (default 1.0)
  - `max_no_dec`: number of rounds allowed to be stuck (default 5)
- **Returns**: `bool`
- **Source**: `bkz.pyx:138-179`

**`BKZ.Reduction(M, lll_obj, param)`**
- **Signature**: `BKZ.Reduction(M, lll_obj, param)`
- **Description**: BKZ reduction object constructor. Takes MatGSO object M, LLL object, and BKZ param.
- **Source**: `bkz.pyx:200-280`

**`BKZ.Reduction.__call__()`**
- **Signature**: `BKZ.Reduction.__call__()`
- **Description**: Execute BKZ reduction. Returns `bool` indicating success.
- **Source**: `bkz.pyx:305-373`

**`BKZ.Reduction.svp_preprocessing(kappa, block_size, param)`**
- **Signature**: `BKZ.Reduction.svp_preprocessing(int kappa, int block_size, BKZParam param)`
- **Description**: Preprocess before calling (Dual-)SVP oracle.
- **Parameters**:
  - `kappa`: index
  - `block_size`: block size
  - `param`: reduction parameters
- **Constraints**: `0 <= kappa < d`, `2 <= block_size <= d`
- **Source**: `bkz.pyx:375-450`

**`BKZ.Reduction.svp_postprocessing(kappa, block_size, solution)`**
- **Signature**: `BKZ.Reduction.svp_postprocessing(int kappa, int block_size, tuple solution)`
- **Description**: Postprocess after SVP oracle call.
- **Parameters**:
  - `kappa`: index
  - `block_size`: block size
  - `solution`: tuple of coordinates
- **Source**: `bkz.pyx:451-564`

**`BKZ.Reduction.svp_reduction(kappa, block_size, param, dual=False)`**
- **Signature**: `BKZ.Reduction.svp_reduction(int kappa, int block_size, BKZParam param, dual=False)`
- **Description**: Run SVP reduction (or dual SVP if `dual=True`).
- **Parameters**:
  - `kappa`: index
  - `block_size`: block size
  - `param`: reduction parameters
  - `dual`: if `True`, run dual SVP (default `False`)
- **Returns**: `bool`
- **Source**: `bkz.pyx:566-678`

**`BKZ.Reduction.status`**
- **Signature**: `property BKZ.Reduction.status`
- **Description**: Status code of BKZ reduction.
- **Source**: `bkz.pyx:1028-1065`

**`BKZ.Reduction.lll_status`**
- **Signature**: `property BKZ.Reduction.lll_status`
- **Description**: Status code of LLL preprocessing.
- **Source**: `bkz.pyx:1067-1095`

**`BKZ.Param(block_size, strategies=BKZ_DEFAULT_STRATEGY, delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, auto_abort=None, gh_factor=None, min_success_probability=BKZ_DEF_MIN_SUCCESS_PROBABILITY, rerandomization_density=BKZ_DEF_RERANDOMIZATION_DENSITY, dump_gso_filename=None, **kwds)`**
- **Signature**: `BKZ.Param(block_size, strategies=BKZ_DEFAULT_STRATEGY, delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, auto_abort=None, gh_factor=None, min_success_probability=BKZ_DEF_MIN_SUCCESS_PROBABILITY, rerandomization_density=BKZ_DEF_RERANDOMIZATION_DENSITY, dump_gso_filename=None, **kwds)`
- **Description**: BKZ parameter object. `block_size` is the required parameter.
- **Constraints**:
  - `block_size` must satisfy `block_size >= 1` (raises `ValueError: "block size must be > 0"` otherwise). Upstream docstring states range as "1 to nrows". The "500" upper bound cited elsewhere is not enforced in source; the practical limit is the number of matrix rows.
  - `delta` must satisfy `0.25 < delta < 1.0` (upstream docstring: "`0.25 < δ < 1.0`"; upper endpoint is exclusive unlike the LLL.reduction convention of `≤ 1`).
  - `max_loops` must be `>= 0`; raises `ValueError` otherwise.
- **Source**: `bkz_param.pyx:314-388`

---

## 4. Enumeration / SVP / CVP

### Enumeration

**`Enumeration(M, nr_solutions=1, strategy=EvaluatorStrategy.BEST_N_SOLUTIONS, sub_solutions=False)`**
- **Signature**: `Enumeration(M, nr_solutions=1, strategy=EvaluatorStrategy.BEST_N_SOLUTIONS, sub_solutions=False)`
- **Description**: Create enumeration object for SVP/CVP.
- **Source**: `enumeration.pyx`

**`Enumeration.enumerate(first, last, max_dist, max_dist_expo, target=None, subtree=None, pruning=None, dual=False, subtree_reset=False)`**
- **Signature**: `Enumeration.enumerate(first, last, max_dist, max_dist_expo, target=None, subtree=None, pruning=None, dual=False, subtree_reset=False)`
- **Description**: Perform enumeration. Returns list of solutions.
- **Source**: `enumeration.pyx`

**`Enumeration.get_nodes(level=None)`**
- **Signature**: `Enumeration.get_nodes(level=None)`
- **Description**: Get enumeration node counts.
- **Source**: `enumeration.pyx`

### SVP

**`SVP.shortest_vector(B, method='fast', flags=SVP_DEFAULT, pruning=True, preprocess=True, max_aux_solutions=0)`**
- **Signature**: `SVP.shortest_vector(B, method='fast', flags=SVP_DEFAULT, pruning=True, preprocess=True, max_aux_solutions=0)`
- **Description**: Find shortest non-zero vector in lattice. Returns a tuple of coordinates for the solution vector (in the ambient space, not lattice coordinates). If `max_aux_solutions > 0`, returns `(tuple, tuple_of_aux_solutions)`.
- **Constraints**:
  - `B` must be an `IntegerMatrix` with `int_type='mpz'` (GMP integers); raises `NotImplementedError` for `int_type='long'`.
  - `B.nrows` must not exceed `FPLLL_MAX_ENUM_DIM` (build-time constant, typically 256); raises `NotImplementedError` otherwise.
  - `method='proved'` is **incompatible with providing pruning parameters** (`pruning` must be `None` or `False` when `method='proved'`); raises `ValueError` otherwise.
  - When `pruning=True` and `B.nrows <= 20`, pruning is silently disabled (upstream hack for small dimensions).
- **Caveat**: `method='fast'` is heuristic; result is guaranteed only for `method='proved'`.
- **Source**: `svpcvp.pyx:41-157`

### CVP

**`CVP.closest_vector(B, t, method='fast', flags=CVP_DEFAULT)`**
- **Signature**: `CVP.closest_vector(B, t, method='fast', flags=CVP_DEFAULT)`
- **Description**: Find closest vector to target `t` (∈ ZZ^n) in lattice. Returns a tuple of coordinates in the ambient space.
- **Constraints**:
  - **B must be LLL-reduced** with `delta=LLL.DEFAULT_DELTA` and `eta=LLL.DEFAULT_ETA` — upstream states this explicitly: "The basis must be LLL-reduced with delta=LLL.DEFAULT_DELTA and eta=LLL.DEFAULT_ETA." Result is guaranteed only for `method='proved'`.
  - `B` must be an `IntegerMatrix` with `int_type='mpz'` (GMP integers); raises `NotImplementedError` for `int_type='long'`.
  - `B.nrows` must not exceed `FPLLL_MAX_ENUM_DIM`; raises `NotImplementedError` otherwise.
- **Source**: `svpcvp.pyx:165-242`

**`CVP.babai(B, t, *args, **kwargs)`**
- **Signature**: `CVP.babai(B, t, *args, **kwargs)`
- **Description**: Babai's nearest plane algorithm for CVP.
- **Caveat**: Practical CVP workflows assume LLL-preconditioned basis input.
- **Source**: `svpcvp.pyx`

---

## 5. Pruning and Utilities

### Pruning

**`Pruning.run(radius, cost, gso_r, target, metric='probability', flags=Pruning.GRADIENT, pruning=None, float_type='double')`**
- **Signature**: `Pruning.run(radius, cost, gso_r, target, metric='probability', flags=Pruning.GRADIENT, pruning=None, float_type='double')`
- **Description**: Compute pruning parameters.
- **Source**: `pruner.pyx`

### Utilities

**`fpylll.util.adjust_radius_to_gh_bound(dist, dist_expo, block_size, root_det, gh_factor)`**
- **Signature**: `fpylll.util.adjust_radius_to_gh_bound(dist, dist_expo, block_size, root_det, gh_factor)`
- **Description**: Adjust enumeration radius to Gaussian heuristic bound.
- **Source**: `fpylll.util` module

**`fpylll.util.gaussian_heuristic(r)`**
- **Signature**: `fpylll.util.gaussian_heuristic(r)`
- **Description**: Compute Gaussian heuristic for radius r.
- **Source**: `fpylll.util` module

---

## Definiteness and Domain Caveat

fpylll is a Euclidean lattice reduction library. It does not expose indefinite arithmetic-form classification semantics (genus, spinor genus, signature-based classification). The methods operate on lattices as free modules with symmetric positive-definite bilinear forms (inner products), not on the broader class of indefinite bilinear-form lattices.

---

## References

- fpylll modules: `https://fpylll.readthedocs.io/en/latest/modules.html`
- fpylll repository: `https://github.com/fplll/fpylll`
- fpylll docs home: `https://fpylll.readthedocs.io/`
