# FLINT Lattice Reference

Local upstream sources:
- `docs/flint/upstream/fmpz_lll.rst` — LLL reduction APIs
- `docs/flint/upstream/fmpz_mat.rst` — HNF/SNF and related matrix APIs

---

## 1. LLL Context and Reduction

### Context Initialization

**`fmpz_lll_context_init_default(fl)`**
- **Signature**: `void fmpz_lll_context_init_default(fmpz_lll_t fl)`
- **Description**: Sets `fl->delta=0.99`, `fl->eta=0.51`, `fl->rt=Z_BASIS`, `fl->gt=APPROX`
- **Source**: `fmpz_lll.rst:16-19`

**`fmpz_lll_context_init(fl, delta, eta, rt, gt)`**
- **Signature**: `void fmpz_lll_context_init(fmpz_lll_t fl, double delta, double eta, rep_type rt, gram_type gt)`
- **Constraints**: `delta in (0.25, 1)`, `eta in (0.5, sqrt(delta))` — endpoints exclusive
- **Source**: `fmpz_lll.rst:21-31`

**`fmpz_lll_randtest(fl, state)`**
- **Signature**: `void fmpz_lll_randtest(fmpz_lll_t fl, flint_rand_t state)`
- **Description**: Random LLL context parameters
- **Source**: `fmpz_lll.rst:38-43`

### Main LLL Functions

**`fmpz_lll(B, U, fl)`**
- **Signature**: `void fmpz_lll(fmpz_mat_t B, fmpz_mat_t U, const fmpz_lll_t fl)`
- **Description**: Main LLL reduction function. Reduces `B` in place. `U` captures unimodular transformations if non-NULL.
- **Source**: `fmpz_lll.rst:315-335`

**`fmpz_lll_with_removal(B, U, gs_B, fl)`**
- **Signature**: `int fmpz_lll_with_removal(fmpz_mat_t B, fmpz_mat_t U, const fmpz_t gs_B, const fmpz_lll_t fl)`
- **Returns**: New dimension of `B` after removal
- **Source**: `fmpz_lll.rst:338-347`

### LLL Variants (Floating-Point)

**`fmpz_lll_d(B, U, fl)`**
- **Signature**: `int fmpz_lll_d(fmpz_mat_t B, fmpz_mat_t U, const fmpz_lll_t fl)`
- **Caveat**: Heuristic — may return with `B` unreduced. See `fmpz_lll.rst:133-141`
- **Source**: `fmpz_lll.rst:143-158`

**`fmpz_lll_d_heuristic(B, U, fl)`**
- **Signature**: `int fmpz_lll_d_heuristic(fmpz_mat_t B, fmpz_mat_t U, const fmpz_lll_t fl)`
- **Caveat**: Heuristic — may return with `B` unreduced
- **Source**: `fmpz_lll.rst:160-164`

**`fmpz_lll_d_with_removal(B, U, gs_B, fl)`**
- **Signature**: `int fmpz_lll_d_with_removal(fmpz_mat_t B, fmpz_mat_t U, const fmpz_t gs_B, const fmpz_lll_t fl)`
- **Returns**: New dimension of `B` if removals desired
- **Caveat**: Heuristic
- **Source**: `fmpz_lll.rst:202-205`

**`fmpz_lll_d_heuristic_with_removal(B, U, gs_B, fl)`**
- **Signature**: `int fmpz_lll_d_heuristic_with_removal(fmpz_mat_t B, fmpz_mat_t U, const fmpz_t gs_B, const fmpz_lll_t fl)`
- **Caveat**: Heuristic
- **Source**: `fmpz_lll.rst:207-211`

**`fmpz_lll_mpf2(B, U, prec, fl)`**
- **Signature**: `int fmpz_lll_mpf2(fmpz_mat_t B, fmpz_mat_t U, flint_bitcnt_t prec, const fmpz_lll_t fl)`
- **Source**: `fmpz_lll.rst:166-172`

**`fmpz_lll_mpf(B, U, fl)`**
- **Signature**: `int fmpz_lll_mpf(fmpz_mat_t B, fmpz_mat_t U, const fmpz_lll_t fl)`
- **Returns**: 0 on success, -1 if precision maxes out
- **Source**: `fmpz_lll.rst:174-181`

**`fmpz_lll_mpf_with_removal(B, U, gs_B, fl)`**
- **Signature**: `int fmpz_lll_mpf_with_removal(fmpz_mat_t B, fmpz_mat_t U, const fmpz_t gs_B, const fmpz_lll_t fl`
- **Source**: `fmpz_lll.rst:218-225`

**`fmpz_lll_wrapper(B, U, fl)`**
- **Signature**: `int fmpz_lll_wrapper(fmpz_mat_t B, fmpz_mat_t U, const fmpz_lll_t fl)`
- **Description**: Adaptive wrapper — tries `fmpz_lll_d`, then heuristic, then `fmpz_lll_mpf`
- **Source**: `fmpz_lll.rst:183-199`

**`fmpz_lll_wrapper_with_removal(B, U, gs_B, fl)`**
- **Signature**: `int fmpz_lll_wrapper_with_removal(fmpz_mat_t B, fmpz_mat_t U, const fmpz_t gs_B, const fmpz_lll_t fl)`
- **Source**: `fmpz_lll.rst:227-234`

**`fmpz_lll_d_with_removal_knapsack(B, U, gs_B, fl)`**
- **Signature**: `int fmpz_lll_d_with_removal_knapsack(fmpz_mat_t B, fmpz_mat_t U, const fmpz_t gs_B, const fmpz_lll_t fl)`
- **Caveat**: Heuristic — may return unreduced
- **Source**: `fmpz_lll.rst:236-241`

**`fmpz_lll_wrapper_with_removal_knapsack(B, U, gs_B, fl)`**
- **Signature**: `int fmpz_lll_wrapper_with_removal_knapsack(fmpz_mat_t B, fmpz_mat_t U, const fmpz_t gs_B, const fmpz_lll_t fl)`
- **Source**: `fmpz_lll.rst:243-251`

### ULLL (Unscheduled LLL)

**`fmpz_lll_with_removal_ulll(FM, UM, new_size, gs_B, fl)`**
- **Signature**: `int fmpz_lll_with_removal_ulll(fmpz_mat_t FM, fmpz_mat_t UM, slong new_size, const fmpz_t gs_B, const fmpz_lll_t fl)`
- **Description**: ULLL — augments lattice with identity, scales down, reduces
- **Source**: `fmpz_lll.rst:258-267`

**`fmpz_lll_storjohann_ulll(FM, new_size, fl)`**
- **Signature**: `void fmpz_lll_storjohann_ulll(fmpz_mat_t FM, slong new_size, const fmpz_lll_t fl)`
- **Caveat**: Not tested — use at own risk
- **Source**: `fmpz_lll.rst:302-308`

### LLL Reducedness Checking

**`fmpz_lll_is_reduced(B, fl, prec)`**
- **Signature**: `int fmpz_lll_is_reduced(const fmpz_mat_t B, const fmpz_lll_t fl, flint_bitcnt_t prec)`
- **Returns**: Conclusive: non-zero if reduced, zero if not
- **Source**: `fmpz_lll.rst:289-295`

**`fmpz_lll_is_reduced_d(B, fl)`**
- **Signature**: `int fmpz_lll_is_reduced_d(const fmpz_mat_t B, const fmpz_lll_t fl)`
- **Returns**: Non-zero = definitely reduced, zero = inconclusive
- **Source**: `fmpz_lll.rst:276-287`

**`fmpz_lll_is_reduced_mpfr(B, fl, prec)`**
- **Signature**: `int fmpz_lll_is_reduced_mpfr(const fmpz_mat_t B, const fmpz_lll_t fl, flint_bitcnt_t prec)`
- **Source**: `fmpz_lll.rst:277`

**`fmpz_lll_is_reduced_with_removal(B, fl, gs_B, newd, prec)`**
- **Signature**: `int fmpz_lll_is_reduced_with_removal(const fmpz_mat_t B, const fmpz_lll_t fl, const fmpz_t gs_B, int newd, flint_bitcnt_t prec)`
- **Returns**: Conclusive
- **Source**: `fmpz_lll.rst:290`

**`fmpz_lll_is_reduced_d_with_removal(B, fl, gs_B, newd)`**
- **Signature**: `int fmpz_lll_is_reduced_d_with_removal(const fmpz_mat_t B, const fmpz_lll_t fl, const fmpz_t gs_B, int newd)`
- **Source**: `fmpz_lll.rst:278`

**`fmpz_lll_is_reduced_mpfr_with_removal(B, fl, gs_B, newd, prec)`**
- **Signature**: `int fmpz_lll_is_reduced_mpfr_with_removal(const fmpz_mat_t B, const fmpz_lll_t fl, const fmpz_t gs_B, int newd, flint_bitcnt_t prec)`
- **Source**: `fmpz_lll.rst:279`

### Reducedness Checking (Direct)

**`fmpz_mat_is_reduced(A, delta, eta)`**
- **Signature**: `int fmpz_mat_is_reduced(const fmpz_mat_t A, double delta, double eta)`
- **Returns**: Non-zero if `A` is LLL-reduced with factor (delta, eta)
- **Source**: `fmpz_mat.rst:1439-1444`

**`fmpz_mat_is_reduced_gram(A, delta, eta)`**
- **Signature**: `int fmpz_mat_is_reduced_gram(const fmpz_mat_t A, double delta, double eta)`
- **Assumes**: `A` is the Gram matrix of the basis
- **Source**: `fmpz_mat.rst:1440`

**`fmpz_mat_is_reduced_with_removal(A, delta, eta, gs_B, newd)`**
- **Signature**: `int fmpz_mat_is_reduced_with_removal(const fmpz_mat_t A, double delta, double eta, const fmpz_t gs_B, int newd)`
- **Source**: `fmpz_mat.rst:1446-1452`

**`fmpz_mat_is_reduced_gram_with_removal(A, delta, eta, gs_B, newd)`**
- **Signature**: `int fmpz_mat_is_reduced_gram_with_removal(const fmpz_mat_t A, double delta, double eta, const fmpz_t gs_B, int newd)`
- **Source**: `fmpz_mat.rst:1447`

### Classical LLL

**`fmpz_mat_lll_original(A, delta, eta)`**
- **Signature**: `void fmpz_mat_lll_original(fmpz_mat_t A, const fmpq_t delta, const fmpq_t eta)`
- **Source**: `fmpz_mat.rst:1460-1465`

**`fmpz_mat_lll_storjohann(A, delta, eta)`**
- **Signature**: `void fmpz_mat_lll_storjohann(fmpz_mat_t A, const fmpq_t delta, const fmpq_t eta)`
- **Source**: `fmpz_mat.rst:1472-1483`

---

## 2. Hermite Normal Form

**`fmpz_mat_hnf(H, A)`**
- **Signature**: `void fmpz_mat_hnf(fmpz_mat_t H, const fmpz_mat_t A)`
- **Aliasing**: Allowed
- **Source**: `fmpz_mat.rst:1230-1238`

**`fmpz_mat_hnf_transform(H, U, A)`**
- **Signature**: `void fmpz_mat_hnf_transform(fmpz_mat_t H, fmpz_mat_t U, const fmpz_mat_t A)`
- **Description**: Returns `H` and transformation matrix `U` where `U*A = H`
- **Source**: `fmpz_mat.rst:1240-1249`

**`fmpz_mat_hnf_classical(H, A)`**
- **Signature**: `void fmpz_mat_hnf_classical(fmpz_mat_t H, const fmpz_mat_t A)`
- **Source**: `fmpz_mat.rst:1251-1258`

**`fmpz_mat_hnf_xgcd(H, A)`**
- **Signature**: `void fmpz_mat_hnf_xgcd(fmpz_mat_t H, const fmpz_mat_t A)`
- **Source**: `fmpz_mat.rst:1260-1268`

**`fmpz_mat_hnf_modular(H, A, D)`**
- **Signature**: `void fmpz_mat_hnf_modular(fmpz_mat_t H, const fmpz_mat_t A, const fmpz_t D)`
- **Constraint**: `A` assumed rank `n`, `D` positive multiple of det of non-zero rows of `H`
- **Source**: `fmpz_mat.rst:1270-1280`

**`fmpz_mat_hnf_modular_eldiv(A, D)`**
- **Signature**: `void fmpz_mat_hnf_modular_eldiv(fmpz_mat_t A, const fmpz_t D)`
- **Constraint**: `A` rank `n`, `D` positive multiple of largest elementary divisor
- **Source**: `fmpz_mat.rst:1282-1287`

**`fmpz_mat_hnf_minors(H, A)`**
- **Signature**: `void fmpz_mat_hnf_minors(fmpz_mat_t H, const fmpz_mat_t A)`
- **Constraint**: `A` assumed rank `n`
- **Source**: `fmpz_mat.rst:1289-1298`

**`fmpz_mat_hnf_pernet_stein(H, A, state)`**
- **Signature**: `void fmpz_mat_hnf_pernet_stein(fmpz_mat_t H, const fmpz_mat_t A, flint_rand_t state)`
- **Source**: `fmpz_mat.rst:1300-1307`

**`fmpz_mat_is_in_hnf(A)`**
- **Signature**: `int fmpz_mat_is_in_hnf(const fmpz_mat_t A)`
- **Returns**: 1 if in HNF, 0 otherwise
- **Source**: `fmpz_mat.rst:1309-1312`

---

## 3. Smith Normal Form

**`fmpz_mat_snf(S, A)`**
- **Signature**: `void fmpz_mat_snf(fmpz_mat_t S, const fmpz_mat_t A)`
- **Aliasing**: Allowed
- **Source**: `fmpz_mat.rst:1319-1327`

**`fmpz_mat_snf_diagonal(S, A)`**
- **Signature**: `void fmpz_mat_snf_diagonal(fmpz_mat_t S, const fmpz_mat_t A)`
- **Constraint**: `A` must be diagonal matrix
- **Source**: `fmpz_mat.rst:1329-1336`

**`fmpz_mat_snf_kannan_bachem(S, A)`**
- **Signature**: `void fmpz_mat_snf_kannan_bachem(fmpz_mat_t S, const fmpz_mat_t A)`
- **Source**: `fmpz_mat.rst:1338-1345`

**`fmpz_mat_snf_iliopoulos(S, A, mod)`**
- **Signature**: `void fmpz_mat_snf_iliopoulos(fmpz_mat_t S, const fmpz_mat_t A, const fmpz_t mod)`
- **Constraint**: `A` must be nonsingular `n x n`
- **Source**: `fmpz_mat.rst:1347-1354`

**`fmpz_mat_is_in_snf(A)`**
- **Signature**: `int fmpz_mat_is_in_snf(const fmpz_mat_t A)`
- **Returns**: 1 if in SNF, 0 otherwise
- **Source**: `fmpz_mat.rst:1356-1359`

---

## 4. Gram Matrix

**`fmpz_mat_gram(B, A)`**
- **Signature**: `void fmpz_mat_gram(fmpz_mat_t B, const fmpz_mat_t A)`
- **Description**: Computes Gram matrix of lattice spanned by rows of `A`
- **Source**: `fmpz_mat.rst:1366-1372`

---

## Domain Caveat

FLINT methods here are integer-matrix and Euclidean reduction/normal-form surfaces, not indefinite genus/isometry classification APIs.

---

## References

- FLINT `fmpz_lll` docs: `https://flintlib.org/doc/fmpz_lll.html`
- FLINT `fmpz_mat` docs: `https://flintlib.org/doc/fmpz_mat.html`
- FLINT docs index: `https://flintlib.org/doc/`
